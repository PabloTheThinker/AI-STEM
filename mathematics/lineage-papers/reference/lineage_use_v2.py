"""
Operator instrument for the official Lineage Equation.

One telemetry window in. A dashboard card out. Compare two windows.
Preview a bottleneck cut. The law is unchanged.

    python3 lineage_use_v2.py --example
    python3 lineage_use_v2.py example_telemetry.json
    python3 lineage_use_v2.py --compare before.json after.json
    python3 lineage_use_v2.py window.json --cut-ms 20
    python3 lineage_use_v2.py --batch windows.jsonl

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import fields, replace
from pathlib import Path
from typing import Any, Mapping

try:
    from lineage_capacity_v2 import usable_fraction
    from lineage_core_v2 import core_q, little_L, load_ratio, regime
    from lineage_control_v2 import (
        lambda_W,
        lambda_job,
        ops_action,
        ops_action_text,
        shed_pi,
        step_scores,
    )
    from lineage_ops_v2 import mm1_sojourn, ops_card
    from lineage_slice_v2 import (
        SliceResult,
        TelemetryRecord,
        compute_slice,
        worked_example_record,
    )
except ImportError:  # pragma: no cover
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_capacity_v2 import usable_fraction
    from lineage_core_v2 import core_q, little_L, load_ratio, regime
    from lineage_control_v2 import (
        lambda_W,
        lambda_job,
        ops_action,
        ops_action_text,
        shed_pi,
        step_scores,
    )
    from lineage_ops_v2 import mm1_sojourn, ops_card
    from lineage_slice_v2 import (
        SliceResult,
        TelemetryRecord,
        compute_slice,
        worked_example_record,
    )


SCHEMA = "fudoshin.lineage.use/v1"

KNOWN_FIELDS = {f.name for f in fields(TelemetryRecord)}

TAU_FIELDS: tuple[tuple[str, str], ...] = (
    ("retrieval", "tau_retrieval_s"),
    ("pathway", "tau_pathway_s"),
    ("working_memory", "tau_working_memory_s"),
    ("sync", "tau_sync_s"),
    ("settling", "tau_settling_s"),
)

HINT_ACTION = {
    "cut_bottleneck_latency": "Cut the slowest pipe.",
    "raise_mass": "Raise structural mass (identity, memory, graph, permanence).",
    "raise_flux": "Raise directed flux (retrieval, pathway, control, merge).",
}

OPTIONAL_DECLARED_MISSING = (
    ("memory_index_coverage", "C_mem falls back to entry saturation only"),
    ("healthy_edge_ratio", "C_graph falls back to mean-degree saturation only"),
    ("permanence_integrity", "C_perm falls back to checkpoint_success_ratio"),
    ("wm_turnover", "F_wm falls back to wm_items"),
    ("belief_entropy", "H falls back to 1 − merge_confidence"),
    ("graph_weights", "Ê falls back to 1 − healthy_edge_ratio or fracture_score"),
)


class TelemetryError(ValueError):
    """A window that cannot be evaluated."""


def _as_float(name: str, value: Any) -> float:
    if isinstance(value, bool):
        raise TelemetryError(f"{name}: expected a number, got boolean")
    try:
        out = float(value)
    except (TypeError, ValueError) as exc:
        raise TelemetryError(f"{name}: expected a number, got {value!r}") from exc
    if not math.isfinite(out):
        raise TelemetryError(f"{name}: must be finite")
    return out


def record_from_mapping(data: Mapping[str, Any]) -> tuple[TelemetryRecord, list[str]]:
    """
    Load a window. Extra keys are ignored (logs have extra fields).
    Invalid windows raise TelemetryError.
    """
    if not isinstance(data, Mapping):
        raise TelemetryError("telemetry must be a JSON object")
    warnings: list[str] = []
    extra = sorted(str(k) for k in data if k not in KNOWN_FIELDS)
    if extra:
        warnings.append("ignored extra fields: " + ", ".join(extra))

    kwargs: dict[str, Any] = {}
    for key, raw in data.items():
        if key not in KNOWN_FIELDS:
            continue
        if key in {"graph_weights", "graph_state"}:
            kwargs[key] = raw
            continue
        if key in {"mode", "weight_table"}:
            kwargs[key] = str(raw)
            continue
        if raw is None:
            kwargs[key] = None
            continue
        kwargs[key] = _as_float(key, raw)

    rec = TelemetryRecord(**kwargs)
    _validate(rec, warnings)
    return rec, warnings


def _validate(rec: TelemetryRecord, warnings: list[str]) -> None:
    if rec.weight_table not in {"official", "equal", "promotion"}:
        raise TelemetryError(
            f"weight_table: unknown {rec.weight_table!r} (official|equal|promotion)"
        )
    for name, field in TAU_FIELDS:
        tau = float(getattr(rec, field))
        if tau <= 0.0:
            raise TelemetryError(f"{field}: latency must be > 0 s ({name})")
    counts = (
        "identity_alert_count",
        "identity_axis_count",
        "memory_entries",
        "graph_nodes",
        "graph_edges",
        "wm_items",
        "retrieval_attempts",
        "retrieval_hits",
        "pathway_events",
        "control_actions",
        "merge_writes",
    )
    for name in counts:
        if float(getattr(rec, name)) < 0.0:
            raise TelemetryError(f"{name}: count must be ≥ 0")
    if rec.retrieval_hits > rec.retrieval_attempts:
        warnings.append(
            f"retrieval_hits {rec.retrieval_hits:g} > attempts {rec.retrieval_attempts:g}"
        )
    if rec.graph_weights is not None and rec.graph_state is not None:
        n = len(rec.graph_state)
        if any(len(row) != n for row in rec.graph_weights) or len(rec.graph_weights) != n:
            raise TelemetryError("graph_weights must be square and match graph_state")


def bottleneck(rec: TelemetryRecord) -> dict[str, Any]:
    named = [(name, float(getattr(rec, field))) for name, field in TAU_FIELDS]
    name, tau = max(named, key=lambda item: item[1])
    return {
        "name": name,
        "field": dict(TAU_FIELDS)[name],
        "tau_s": tau,
        "tau_ms": tau * 1000.0,
        "nu_star_hz": 1.0 / tau,
    }


def declared_missing(rec: TelemetryRecord) -> list[str]:
    missing: list[str] = []
    for name, note in OPTIONAL_DECLARED_MISSING:
        if getattr(rec, name) is None:
            missing.append(f"{name} ({note})")
    return missing


def _action(rec: TelemetryRecord, out: SliceResult) -> str:
    stem = HINT_ACTION[out.hint]
    if out.hint == "cut_bottleneck_latency":
        bn = bottleneck(rec)
        return (
            f"{stem} {bn['name']} is slowest at {bn['tau_ms']:.1f} ms "
            f"({bn['nu_star_hz']:.3f} Hz)."
        )
    return stem


def evaluate(rec: TelemetryRecord, warnings: list[str] | None = None) -> dict[str, Any]:
    """Dashboard card for one window. Law unchanged."""
    out = compute_slice(rec)
    Q = float(out.terms["Q"])
    m_t = float(out.terms["M_tilde"])
    p_t = float(out.terms["Pi_tilde"])
    M = float(out.terms["M"])
    Pi = float(out.terms["Pi"])
    r = float(out.terms["r"])
    q2 = Q * Q if Q > 0.0 else 1.0
    eps = load_ratio(M, Pi, r) if M != 0.0 else float("inf")
    q_core = core_q(M, Pi, r)
    nu = float(out.terms["nu_star"])
    ops = ops_card(M, Pi, nu, float(out.usable))
    action = ops_action(M, Pi, nu, float(out.usable))
    W = float(ops["W_sojourn"])
    tau_star = 1.0 / nu if nu else math.inf
    bn = bottleneck(rec)
    warn = list(warnings or [])
    if Pi >= 1.0:
        warn.append("Π ≥ 1: utilization reading is unstable; sojourn is infinite")
    return {
        "schema": SCHEMA,
        "weight_table": out.weight_table,
        "Q": Q,
        "Q_eff": float(out.Q_eff),
        "E0": float(out.terms["rest_energy"]),
        "q": q_core,
        "eps": eps,
        "L": little_L(Pi, 1.0 / r if r else 0.0),
        "regime": regime(eps) if math.isfinite(eps) else "transport",
        "u": float(out.usable),
        "rest_share": (m_t * m_t) / q2,
        "transport_share": (p_t * p_t) / q2,
        "M": M,
        "Pi": Pi,
        "nu_star_hz": nu,
        "Lambda_M": ops["Lambda_M"],
        "Lambda_q": ops["Lambda_q"],
        "Lambda_eff": ops["Lambda_eff"],
        "Lambda_job": lambda_job(M, Pi, nu),
        "Lambda_W": lambda_W(M, Pi, nu),
        "C_shannon": ops["C_shannon"],
        "eta": ops["eta"],
        "W_sojourn": W,
        "zone": out.zone,
        "hint": out.hint,
        "action": _action(rec, out),
        "ops_action": action,
        "ops_text": ops_action_text(action, Pi, W if math.isfinite(W) else 0.0, tau_star),
        "ops_scores": step_scores(M, Pi, nu),
        "gate_open": bool(out.gate_open),
        "Phi_org": float(out.phi["Phi_org"]),
        "bottleneck": bn,
        "missing": declared_missing(rec),
        "warnings": warn,
    }


def evaluate_mapping(data: Mapping[str, Any]) -> dict[str, Any]:
    rec, warnings = record_from_mapping(data)
    return evaluate(rec, warnings)


def compare(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "Q",
        "Q_eff",
        "u",
        "E0",
        "q",
        "eps",
        "L",
        "Lambda_M",
        "Lambda_job",
        "Lambda_W",
        "eta",
        "W_sojourn",
        "rest_share",
        "transport_share",
        "Phi_org",
    )
    delta = {k: float(after[k]) - float(before[k]) for k in keys}
    return {
        "schema": SCHEMA,
        "before": before,
        "after": after,
        "delta": delta,
        "zone_changed": before["zone"] != after["zone"],
        "hint_changed": before["hint"] != after["hint"],
        "regime_changed": before["regime"] != after["regime"],
        "bottleneck_changed": before["bottleneck"]["name"] != after["bottleneck"]["name"],
    }


def cut_bottleneck(rec: TelemetryRecord, cut_ms: float) -> TelemetryRecord:
    if cut_ms <= 0.0:
        raise TelemetryError("cut-ms must be > 0")
    bn = bottleneck(rec)
    new_tau = float(getattr(rec, bn["field"])) - cut_ms / 1000.0
    if new_tau <= 0.0:
        raise TelemetryError(
            f"cut of {cut_ms:g} ms would zero {bn['name']} "
            f"(now {bn['tau_ms']:.1f} ms)"
        )
    return replace(rec, **{bn["field"]: new_tau})


def what_if_cut(rec: TelemetryRecord, cut_ms: float, warnings: list[str] | None = None) -> dict[str, Any]:
    before = evaluate(rec, warnings)
    after_rec = cut_bottleneck(rec, cut_ms)
    after = evaluate(after_rec)
    card = compare(before, after)
    card["cut_ms"] = float(cut_ms)
    card["cut_channel"] = before["bottleneck"]["name"]
    return card


def what_if_shed(rec: TelemetryRecord, delta_pi: float, warnings: list[str] | None = None) -> dict[str, Any]:
    """Move Π only. M, ν*, u held. Operations lever."""
    before = evaluate(rec, warnings)
    new_pi = shed_pi(float(before["Pi"]), delta_pi)
    after = dict(before)
    nu = float(before["nu_star_hz"])
    M = float(before["M"])
    u = float(before["u"])
    tau = 1.0 / nu if nu else math.inf
    after["Pi"] = new_pi
    after["eta"] = 1.0 - new_pi
    after["Lambda_job"] = lambda_job(M, new_pi, nu)
    after["Lambda_W"] = lambda_W(M, new_pi, nu)
    after["W_sojourn"] = mm1_sojourn(tau, new_pi) if math.isfinite(tau) else math.inf
    action = ops_action(M, new_pi, nu, u)
    after["ops_action"] = action
    after["ops_text"] = ops_action_text(
        action, new_pi, after["W_sojourn"] if math.isfinite(after["W_sojourn"]) else 0.0, tau
    )
    after["ops_scores"] = step_scores(M, new_pi, nu)
    card = compare(before, after)
    card["shed_pi"] = float(delta_pi)
    return card


def render_card(card: dict[str, Any]) -> str:
    bn = card["bottleneck"]
    missing = card["missing"] or ["(none)"]
    warnings = card["warnings"] or ["(none)"]
    lines = [
        f"schema          {card['schema']}",
        f"weight_table    {card['weight_table']}",
        f"Q               {card['Q']:.6f}",
        f"Q_eff           {card['Q_eff']:.6f}",
        f"u               {card['u']:.6f}",
        f"q               {card['q']:.6f}",
        f"eps             {card['eps']:.6f}",
        f"L               {card['L']:.6f}",
        f"regime          {card['regime']}",
        f"Lambda_M        {card['Lambda_M']:.6f} Hz",
        f"Lambda_job      {card['Lambda_job']:.6f} Hz",
        f"Lambda_W        {card['Lambda_W']:.6f} Hz",
        f"Lambda_eff      {card['Lambda_eff']:.6f} Hz",
        f"C_shannon       {card['C_shannon']:.6f} Hz",
        f"eta             {card['eta']:.6f}",
        f"W_sojourn       {card['W_sojourn']:.6f} s",
        f"ops_action      {card['ops_action']}",
        f"ops_text        {card['ops_text']}",
        f"E0              {card['E0']:.6f}",
        f"rest_share      {card['rest_share']:.6f}",
        f"transport_share {card['transport_share']:.6f}",
        f"zone            {card['zone']}",
        f"hint            {card['hint']}",
        f"action          {card['action']}",
        f"gate_open       {card['gate_open']}",
        f"Phi_org         {card['Phi_org']:.6f}",
        f"bottleneck      {bn['name']}  {bn['tau_ms']:.1f} ms  {bn['nu_star_hz']:.3f} Hz",
        f"missing         {'; '.join(missing)}",
        f"warnings        {'; '.join(warnings)}",
    ]
    return "\n".join(lines)


def render_compare(card: dict[str, Any]) -> str:
    d = card["delta"]
    extra = []
    if "cut_ms" in card:
        extra.append(f"cut             {card['cut_ms']:g} ms off {card['cut_channel']}")
    if "shed_pi" in card:
        extra.append(f"shed            Π − {card['shed_pi']:g}")
    lines = extra + [
        f"ΔQ              {d['Q']:+.6f}",
        f"ΔQ_eff          {d['Q_eff']:+.6f}",
        f"Δu              {d['u']:+.6f}",
        f"ΔLambda_job     {d['Lambda_job']:+.6f} Hz",
        f"ΔLambda_W       {d['Lambda_W']:+.6f} Hz",
        f"ΔW_sojourn      {d['W_sojourn']:+.6f} s",
        f"zone_changed    {card['zone_changed']}",
        f"hint_changed    {card['hint_changed']}",
        f"bottleneck_changed {card['bottleneck_changed']}",
        "",
        "AFTER",
        render_card(card["after"]),
    ]
    return "\n".join(lines)


def _load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def run_checks() -> dict[str, bool]:
    rec = worked_example_record()
    card = evaluate(rec)
    suite: dict[str, bool] = {}
    suite["schema"] = card["schema"] == SCHEMA
    suite["example_Q"] = abs(card["Q"] - 50.176) < 5e-3
    suite["example_zone"] = card["zone"] == "steady"
    suite["example_hint"] = card["hint"] == "cut_bottleneck_latency"
    suite["bottleneck_retrieval"] = card["bottleneck"]["name"] == "retrieval"
    suite["shares_sum_one"] = abs(card["rest_share"] + card["transport_share"] - 1.0) < 1e-9
    suite["Q_eff_is_uQ"] = abs(card["Q_eff"] - card["u"] * card["Q"]) < 1e-9
    suite["core_q_near_M"] = abs(float(card["q"]) - float(card["M"])) < 0.01
    suite["regime_rest"] = card["regime"] == "rest"
    suite["Q_is_r2_q"] = abs(float(card["Q"]) - float(card["q"]) * float(card["nu_star_hz"]) ** 2) < 1e-6
    suite["lambda_M"] = abs(float(card["Lambda_M"]) - float(card["M"]) * float(card["nu_star_hz"])) < 1e-9
    suite["Q_is_nu_lambda_q"] = abs(float(card["Q"]) - float(card["nu_star_hz"]) * float(card["Lambda_q"])) < 1e-6
    suite["eta_is_one_minus_Pi"] = abs(float(card["eta"]) - (1.0 - float(card["Pi"]))) < 1e-12
    suite["partition"] = abs(
        float(card["Lambda_job"]) + float(card["Lambda_W"]) - float(card["Lambda_M"])
    ) < 1e-9
    suite["ops_sheds"] = card["ops_action"] == "shed_load"
    suite["hint_still_cuts"] = card["hint"] == "cut_bottleneck_latency"

    shed = what_if_shed(rec, 0.10)
    suite["shed_raises_LW"] = shed["delta"]["Lambda_W"] > 0.0
    suite["shed_drops_job"] = shed["delta"]["Lambda_job"] < 0.0

    messy = dict(
        identity_alert_count=1,
        extra_log_field="noise",
        tau_retrieval_s="0.12",
        retrieval_attempts=10,
        retrieval_hits=12,
        weight_table="official",
    )
    loaded, warnings = record_from_mapping(messy)
    suite["ignores_extra"] = any("extra_log_field" in w for w in warnings)
    suite["coerces_tau"] = abs(loaded.tau_retrieval_s - 0.12) < 1e-12
    suite["warns_hits"] = any("retrieval_hits" in w for w in warnings)

    try:
        record_from_mapping({"tau_retrieval_s": 0.0})
        suite["rejects_zero_tau"] = False
    except TelemetryError:
        suite["rejects_zero_tau"] = True

    cut = what_if_cut(rec, 20.0)
    suite["cut_raises_Q"] = cut["delta"]["Q"] > 0.0
    suite["cut_raises_nu"] = cut["after"]["nu_star_hz"] > card["nu_star_hz"]

    same = compare(card, card)
    suite["compare_zero"] = all(abs(v) < 1e-12 for v in same["delta"].values())

    # Official additive budget barely moves this Q; usable does.
    from lineage_capacity_v2 import LineageEquationV2, CognitiveMassV2, CognitiveMomentumV2, PropagationBoundV2

    eq = LineageEquationV2(
        mass=CognitiveMassV2(C_id=0.865, C_mem=0.4275, C_graph=0.845, C_perm=0.820),
        momentum=CognitiveMomentumV2(
            F_wm=0.428571, F_ret=0.708, F_path=0.384615, F_ctrl=0.285714, F_merge=0.456471
        ),
        propagation=PropagationBoundV2(tau_retrieval_s=0.120),
    )
    add = eq.effective_capacity(0.35, 0.141, 0.15, 1.0, 1.0, 1.0)
    use = eq.usable_capacity(0.35, 0.141, 0.15)
    suite["additive_near_raw"] = abs(add - eq.total_capacity()) < 1.0
    suite["usable_moves"] = (eq.total_capacity() - use) > 5.0
    suite["usable_fraction_import"] = 0.0 < usable_fraction(0.35, 0.141, 0.15) < 1.0
    return suite


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Use the Lineage Equation on a telemetry window."
    )
    parser.add_argument("path", nargs="?", help="telemetry JSON object")
    parser.add_argument("--example", action="store_true", help="pinned loaded-but-coherent window")
    parser.add_argument("--json", dest="json_out", action="store_true", help="print JSON")
    parser.add_argument("--compare", nargs=2, metavar=("BEFORE", "AFTER"), help="two windows")
    parser.add_argument("--cut-ms", type=float, dest="cut_ms", help="preview cutting bottleneck by this many ms")
    parser.add_argument("--shed-pi", type=float, dest="shed_pi", help="preview dropping utilization Π by this amount")
    parser.add_argument("--batch", metavar="JSONL", help="one JSON object per line")
    parser.add_argument("--self-test", action="store_true", help="run instrument checks")
    args = parser.parse_args(argv)

    if args.self_test:
        suite = run_checks()
        failed = [k for k, v in suite.items() if not v]
        for k, v in suite.items():
            print(f"{'PASS' if v else 'FAIL':4s}  {k}")
        print("use_checks_passed", len(suite) - len(failed))
        return 0 if not failed else 1

    if (
        not args.example
        and args.path is None
        and args.compare is None
        and args.batch is None
    ):
        args.example = True

    if args.batch:
        for line_no, line in enumerate(Path(args.batch).read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                card = evaluate_mapping(json.loads(line))
            except (TelemetryError, json.JSONDecodeError) as exc:
                print(json.dumps({"line": line_no, "error": str(exc)}), flush=True)
                continue
            print(json.dumps(card, sort_keys=True), flush=True)
        return 0

    if args.compare:
        before = evaluate_mapping(_load_json(Path(args.compare[0])))
        after = evaluate_mapping(_load_json(Path(args.compare[1])))
        card = compare(before, after)
        print(json.dumps(card, indent=2, sort_keys=True) if args.json_out else render_compare(card))
        return 0

    if args.example:
        rec, warnings = worked_example_record(), []
    elif args.path:
        rec, warnings = record_from_mapping(_load_json(Path(args.path)))
    else:
        rec, warnings = worked_example_record(), []

    if args.cut_ms is not None:
        card = what_if_cut(rec, args.cut_ms, warnings)
        print(json.dumps(card, indent=2, sort_keys=True) if args.json_out else render_compare(card))
        return 0

    if args.shed_pi is not None:
        card = what_if_shed(rec, args.shed_pi, warnings)
        print(json.dumps(card, indent=2, sort_keys=True) if args.json_out else render_compare(card))
        return 0

    card = evaluate(rec, warnings)
    print(json.dumps(card, indent=2, sort_keys=True) if args.json_out else render_card(card))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
