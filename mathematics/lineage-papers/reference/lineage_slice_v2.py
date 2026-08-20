"""
Computable slice v1 — telemetry to Lineage quantities.

This module does not replace the official law in lineage_capacity_v2.py.
It answers a narrower question: given a generic observation record, what
numbers do you actually compute?

Weight policy
-------------
- Law evaluation uses v2 official α*, β* (ALPHA_IDENTIFIED / BETA_IDENTIFIED).
- Identification uses the linearized instrument, not the quadratic law.
- Promotion-bundle weights are historical Stage E evidence only.

Capacity budget
---------------
v2 writes Q_eff = Q − λ_H H − λ_E E − λ_D D. That is well-posed only when
the λ are in capacity units. This slice uses the equivalent operational form

    u = clip(1 − λ_H H − λ_E Ê − λ_D D)
    Q_eff = u · Q

with penalties in [0, 1] and λ_H + λ_E + λ_D ≤ 1. Additive v2 is recovered
by setting λ_abstract = λ_frac · Q.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from typing import Any, Mapping

try:
    from lineage_capacity_v2 import (
        ALPHA_EQUAL,
        ALPHA_IDENTIFIED,
        BETA_EQUAL,
        BETA_IDENTIFIED,
        CognitiveMassV2,
        CognitiveMomentumV2,
        LineageEquationV2,
        PropagationBoundV2,
        coherence_energy,
        organism_barrier,
        plasticity_allowed,
    )
except ImportError:  # pragma: no cover - script/module dual use
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_capacity_v2 import (
        ALPHA_EQUAL,
        ALPHA_IDENTIFIED,
        BETA_EQUAL,
        BETA_IDENTIFIED,
        CognitiveMassV2,
        CognitiveMomentumV2,
        LineageEquationV2,
        PropagationBoundV2,
        coherence_energy,
        organism_barrier,
        plasticity_allowed,
    )


# Historical Stage E promotion simplex (synthetic ID). Not operational default.
# Normalized to a probability simplex (source digits summed to 1.001 / 0.999).
ALPHA_PROMOTION: dict[str, float] = {
    "C_id": 0.148 / 1.001,
    "C_mem": 0.258 / 1.001,
    "C_graph": 0.379 / 1.001,
    "C_perm": 0.216 / 1.001,
}

BETA_PROMOTION: dict[str, float] = {
    "F_wm": 0.199 / 0.999,
    "F_ret": 0.262 / 0.999,
    "F_path": 0.222 / 0.999,
    "F_ctrl": 0.160 / 0.999,
    "F_merge": 0.156 / 0.999,
}


# Saturation / mix constants. These are first-slice hyperparameters, not laws.
K_MEM = 200.0
K_LINK = 0.25
K_WM_TURN = 8.0
K_WM_COUNT = 5.0
K_PATH = 40.0
K_CTRL = 20.0
K_MERGE = 12.0

# Penalty fractions for the multiplicative budget. Sum ≤ 1.
LAMBDA_H = 0.25
LAMBDA_E = 0.25
LAMBDA_D = 0.25


def clip01(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return float(x)


def sat(z: float, k: float) -> float:
    """z / (z + k) for z ≥ 0, k > 0. Saturating count normalizer."""
    if k <= 0.0:
        raise ValueError("saturation constant k must be positive")
    z = max(0.0, float(z))
    return z / (z + k)


@dataclass
class TelemetryRecord:
    """
    Generic one-window observation. No private engine required.

    Counts are non-negative. Scores already in [0, 1] stay in [0, 1].
    Latencies are seconds. Missing optional fields fall back as documented.
    """

    # Identity / mass
    identity_alert_count: float = 0.0
    identity_axis_count: float = 8.0
    mean_identity_drift: float = 0.0
    memory_entries: float = 0.0
    memory_index_coverage: float | None = None
    graph_nodes: float = 0.0
    graph_edges: float = 0.0
    healthy_edge_ratio: float | None = None
    permanence_integrity: float | None = None
    checkpoint_success_ratio: float = 0.0

    # Flux
    wm_items: float = 0.0
    wm_turnover: float | None = None
    retrieval_attempts: float = 0.0
    retrieval_hits: float = 0.0
    mean_retrieval_score: float = 0.0
    pathway_events: float = 0.0
    control_actions: float = 0.0
    merge_writes: float = 0.0
    merge_confidence: float = 0.0

    # Latencies (seconds)
    tau_retrieval_s: float = 0.100
    tau_pathway_s: float = 0.050
    tau_working_memory_s: float = 0.030
    tau_sync_s: float = 0.020
    tau_settling_s: float = 0.010
    channel_capacity_hz: float | None = None

    # Penalties / organism
    belief_entropy: float | None = None
    fracture_score: float | None = None
    graph_weights: list[list[float]] | None = None
    graph_state: list[float] | None = None
    reserve: float = 0.5
    reserve_min: float = 0.1
    neural_health: float = 0.2
    neural_health_max: float = 0.9
    blood_health: float = 0.1
    blood_health_max: float = 0.9
    mode: str = "adaptive"

    weight_table: str = "official"  # official | equal | promotion

    def to_json(self) -> dict[str, Any]:
        data = asdict(self)
        return data


def _alpha_beta(table: str) -> tuple[dict[str, float], dict[str, float]]:
    if table == "official":
        return dict(ALPHA_IDENTIFIED), dict(BETA_IDENTIFIED)
    if table == "equal":
        return dict(ALPHA_EQUAL), dict(BETA_EQUAL)
    if table == "promotion":
        return dict(ALPHA_PROMOTION), dict(BETA_PROMOTION)
    raise ValueError(f"unknown weight_table: {table}")


def estimate_C_id(rec: TelemetryRecord) -> float:
    axes = max(1.0, float(rec.identity_axis_count))
    alert = float(rec.identity_alert_count) / axes
    return clip01(1.0 - 0.6 * alert - 0.4 * float(rec.mean_identity_drift))


def estimate_C_mem(rec: TelemetryRecord) -> float:
    density = sat(rec.memory_entries, K_MEM)
    if rec.memory_index_coverage is None:
        return density
    return clip01(0.7 * density + 0.3 * clip01(rec.memory_index_coverage))


def estimate_C_graph(rec: TelemetryRecord) -> float:
    nodes = max(1.0, float(rec.graph_nodes))
    degree = float(rec.graph_edges) / nodes
    cohesion = sat(degree, K_LINK)
    if rec.healthy_edge_ratio is None:
        return cohesion
    return clip01(0.6 * cohesion + 0.4 * clip01(rec.healthy_edge_ratio))


def estimate_C_perm(rec: TelemetryRecord) -> float:
    if rec.permanence_integrity is not None:
        return clip01(rec.permanence_integrity)
    return clip01(rec.checkpoint_success_ratio)


def estimate_F_wm(rec: TelemetryRecord) -> float:
    if rec.wm_turnover is not None:
        return sat(rec.wm_turnover, K_WM_TURN)
    return sat(rec.wm_items, K_WM_COUNT)


def estimate_F_ret(rec: TelemetryRecord) -> float:
    attempts = max(1.0, float(rec.retrieval_attempts))
    hit_rate = float(rec.retrieval_hits) / attempts
    return clip01(0.6 * clip01(hit_rate) + 0.4 * clip01(rec.mean_retrieval_score))


def estimate_F_path(rec: TelemetryRecord) -> float:
    return sat(rec.pathway_events, K_PATH)


def estimate_F_ctrl(rec: TelemetryRecord) -> float:
    return sat(rec.control_actions, K_CTRL)


def estimate_F_merge(rec: TelemetryRecord) -> float:
    return clip01(0.6 * sat(rec.merge_writes, K_MERGE) + 0.4 * clip01(rec.merge_confidence))


def estimate_H_mu(rec: TelemetryRecord) -> float:
    if rec.belief_entropy is not None:
        return clip01(rec.belief_entropy)
    return clip01(1.0 - float(rec.merge_confidence))


def estimate_E_norm(rec: TelemetryRecord) -> float:
    """
    Scale-free graph fracture in [0, 1].

    Prefer Ê = (zᵀ L z) / (n ‖z‖²). Else 1 − healthy_edge_ratio.
    Else explicit fracture_score. Else 0 (declared missing).
    """
    if rec.graph_weights is not None and rec.graph_state is not None:
        z = [float(x) for x in rec.graph_state]
        n = len(z)
        if n == 0:
            return 0.0
        energy = coherence_energy(rec.graph_weights, z)
        denom = n * sum(x * x for x in z)
        if denom <= 0.0:
            return 0.0
        return clip01(energy / denom)
    if rec.healthy_edge_ratio is not None:
        return clip01(1.0 - float(rec.healthy_edge_ratio))
    if rec.fracture_score is not None:
        return clip01(rec.fracture_score)
    return 0.0


def estimate_D_drift(rec: TelemetryRecord) -> float:
    return clip01(rec.mean_identity_drift)


def estimate_primitives(rec: TelemetryRecord) -> dict[str, float]:
    return {
        "C_id": estimate_C_id(rec),
        "C_mem": estimate_C_mem(rec),
        "C_graph": estimate_C_graph(rec),
        "C_perm": estimate_C_perm(rec),
        "F_wm": estimate_F_wm(rec),
        "F_ret": estimate_F_ret(rec),
        "F_path": estimate_F_path(rec),
        "F_ctrl": estimate_F_ctrl(rec),
        "F_merge": estimate_F_merge(rec),
        "H_mu": estimate_H_mu(rec),
        "E_norm": estimate_E_norm(rec),
        "D_drift": estimate_D_drift(rec),
    }


def usable_fraction(
    H_mu: float,
    E_norm: float,
    D_drift: float,
    lam_H: float = LAMBDA_H,
    lam_E: float = LAMBDA_E,
    lam_D: float = LAMBDA_D,
) -> float:
    raw = 1.0 - lam_H * H_mu - lam_E * E_norm - lam_D * D_drift
    return clip01(raw)


def phi_org_slice(
    H_mu: float,
    E_norm: float,
    D_drift: float,
    gate_open: bool,
) -> dict[str, float]:
    """
    First explicit organism barrier on the computable slice.

    Φ_sub = 0 until substrate activations are instrumented (declared).
    Φ_gov = D_drift
    Φ_sig = H_mu
    Φ_sup = Ê
    Φ_gate = 1 if plasticity closed, else 0
    Φ_org = Φ_sub + Φ_gov + Φ_sig + Φ_sup + Φ_gate
    """
    phi_sub = 0.0
    phi_gov = clip01(D_drift)
    phi_sig = clip01(H_mu)
    phi_sup = clip01(E_norm)
    phi_gate = 0.0 if gate_open else 1.0
    total = organism_barrier(phi_sub, phi_gov, phi_sig, phi_sup) + phi_gate
    return {
        "Phi_sub": phi_sub,
        "Phi_gov": phi_gov,
        "Phi_sig": phi_sig,
        "Phi_sup": phi_sup,
        "Phi_gate": phi_gate,
        "Phi_org": total,
    }


def linear_instrument(M: float, Pi: float, scale: float = 1.0, bias: float = 0.0) -> float:
    """
    Identification instrument, not the governing law.

        Q_lin = s (M + Π) + b

    Used because ν*⁴ amplification makes β unidentifiable in the quadratic.
    """
    return scale * (M + Pi) + bias


def health_zone(usable: float) -> str:
    if usable >= 0.70:
        return "steady"
    if usable >= 0.45:
        return "guarded"
    if usable >= 0.25:
        return "repair"
    return "critical"


# Typical one-tick intervention sizes. Sensitivity ≠ raw derivative.
TYPICAL_STEP = {
    "dQ_dM": 0.05,   # hard to move structure
    "dQ_dPi": 0.10,  # flux can move more
    "dQ_dnu": 1.00,  # Hz; ~cutting 15 ms off a 120 ms bottleneck
}


def ascent_hint(gradients: Mapping[str, float]) -> str:
    """
    Largest expected ΔQ among feasible one-tick steps.

    Raw ∂Q/∂M is inflated by r⁴. The calculus layer requires feasible
    intervention size, so the hint scores |∂Q| · typical_step.
    """
    keys = ("dQ_dM", "dQ_dPi", "dQ_dnu")
    best = max(
        keys,
        key=lambda k: abs(float(gradients.get(k, 0.0))) * TYPICAL_STEP[k],
    )
    return {
        "dQ_dM": "raise_mass",
        "dQ_dPi": "raise_flux",
        "dQ_dnu": "cut_bottleneck_latency",
    }[best]


@dataclass
class SliceResult:
    primitives: dict[str, float]
    weight_table: str
    alpha: dict[str, float]
    beta: dict[str, float]
    terms: dict[str, float]
    gradients: dict[str, float]
    usable: float
    Q_eff: float
    Q_lin: float
    zone: str
    hint: str
    gate_open: bool
    phi: dict[str, float]

    def to_dict(self) -> dict[str, Any]:
        return {
            "primitives": self.primitives,
            "weight_table": self.weight_table,
            "alpha": self.alpha,
            "beta": self.beta,
            "terms": self.terms,
            "gradients": self.gradients,
            "usable": self.usable,
            "Q_eff": self.Q_eff,
            "Q_lin": self.Q_lin,
            "zone": self.zone,
            "hint": self.hint,
            "gate_open": self.gate_open,
            "phi": self.phi,
        }


def compute_slice(rec: TelemetryRecord) -> SliceResult:
    prim = estimate_primitives(rec)
    alpha, beta = _alpha_beta(rec.weight_table)
    mass = CognitiveMassV2(
        C_id=prim["C_id"],
        C_mem=prim["C_mem"],
        C_graph=prim["C_graph"],
        C_perm=prim["C_perm"],
        alpha=alpha,
    )
    mom = CognitiveMomentumV2(
        F_wm=prim["F_wm"],
        F_ret=prim["F_ret"],
        F_path=prim["F_path"],
        F_ctrl=prim["F_ctrl"],
        F_merge=prim["F_merge"],
        beta=beta,
    )
    prop = PropagationBoundV2(
        tau_retrieval_s=rec.tau_retrieval_s,
        tau_pathway_s=rec.tau_pathway_s,
        tau_working_memory_s=rec.tau_working_memory_s,
        tau_sync_s=rec.tau_sync_s,
        tau_settling_s=rec.tau_settling_s,
        channel_capacity_hz=rec.channel_capacity_hz,
    )
    eq = LineageEquationV2(mass=mass, momentum=mom, propagation=prop)
    terms = eq.capacity_terms()
    grads = eq.gradients()
    usable = usable_fraction(prim["H_mu"], prim["E_norm"], prim["D_drift"])
    q = terms["Q"]
    q_eff = usable * q
    gate = plasticity_allowed(
        rec.mode,
        rec.reserve,
        rec.reserve_min,
        rec.neural_health,
        rec.neural_health_max,
        rec.blood_health,
        rec.blood_health_max,
    )
    phi = phi_org_slice(prim["H_mu"], prim["E_norm"], prim["D_drift"], gate)
    return SliceResult(
        primitives=prim,
        weight_table=rec.weight_table,
        alpha=alpha,
        beta=beta,
        terms=terms,
        gradients=grads,
        usable=usable,
        Q_eff=q_eff,
        Q_lin=linear_instrument(terms["M"], terms["Pi"]),
        zone=health_zone(usable),
        hint=ascent_hint(grads),
        gate_open=gate,
        phi=phi,
    )


def worked_example_record() -> TelemetryRecord:
    """Pinned loaded-but-coherent agent used in CONCRETE_COMPUTABLE_SLICE.md."""
    return TelemetryRecord(
        identity_alert_count=1.0,
        identity_axis_count=8.0,
        mean_identity_drift=0.15,
        memory_entries=120.0,
        memory_index_coverage=0.55,
        graph_nodes=40.0,
        graph_edges=70.0,
        healthy_edge_ratio=0.80,
        permanence_integrity=0.82,
        checkpoint_success_ratio=0.90,
        wm_items=4.0,
        wm_turnover=6.0,
        retrieval_attempts=20.0,
        retrieval_hits=14.0,
        mean_retrieval_score=0.72,
        pathway_events=25.0,
        control_actions=8.0,
        merge_writes=5.0,
        merge_confidence=0.70,
        tau_retrieval_s=0.120,
        tau_pathway_s=0.040,
        tau_working_memory_s=0.030,
        tau_sync_s=0.020,
        tau_settling_s=0.015,
        belief_entropy=0.35,
        graph_weights=[[0.0, 1.0, 0.5], [1.0, 0.0, 0.2], [0.5, 0.2, 0.0]],
        graph_state=[0.2, 0.5, 0.1],
        reserve=0.50,
        neural_health=0.20,
        blood_health=0.10,
        mode="adaptive",
        weight_table="official",
    )


# Pinned from the formulas (checked in the suite). Rounded for the paper.
WORKED_EXAMPLE_PINNED = {
    "C_id": 0.865000,
    "C_mem": 0.427500,
    "C_graph": 0.845000,
    "C_perm": 0.820000,
    "F_wm": 0.428571,
    "F_ret": 0.708000,
    "F_path": 0.384615,
    "F_ctrl": 0.285714,
    "F_merge": 0.456471,
    "M": 0.720350,
    "Pi": 0.468109,
    "nu_star": 8.333333,
    "zone": "steady",
    "hint": "cut_bottleneck_latency",
    "usable": 0.839722,
    "gate_open": True,
}


def run_slice_suite() -> dict[str, bool]:
    results: dict[str, bool] = {}
    rec = worked_example_record()
    out = compute_slice(rec)
    p = out.primitives

    def near(a: float, b: float, tol: float = 1e-5) -> bool:
        return abs(a - b) <= tol

    results["C_id"] = near(p["C_id"], WORKED_EXAMPLE_PINNED["C_id"])
    results["C_mem"] = near(p["C_mem"], WORKED_EXAMPLE_PINNED["C_mem"])
    results["C_graph"] = near(p["C_graph"], WORKED_EXAMPLE_PINNED["C_graph"])
    results["C_perm"] = near(p["C_perm"], WORKED_EXAMPLE_PINNED["C_perm"])
    results["F_wm"] = near(p["F_wm"], WORKED_EXAMPLE_PINNED["F_wm"])
    results["F_ret"] = near(p["F_ret"], WORKED_EXAMPLE_PINNED["F_ret"])
    results["F_path"] = near(p["F_path"], WORKED_EXAMPLE_PINNED["F_path"])
    results["F_ctrl"] = near(p["F_ctrl"], WORKED_EXAMPLE_PINNED["F_ctrl"])
    results["F_merge"] = near(p["F_merge"], WORKED_EXAMPLE_PINNED["F_merge"], 1e-5)
    results["M"] = near(out.terms["M"], WORKED_EXAMPLE_PINNED["M"], 1e-5)
    results["Pi"] = near(out.terms["Pi"], WORKED_EXAMPLE_PINNED["Pi"], 1e-5)
    results["nu_star"] = near(out.terms["nu_star"], WORKED_EXAMPLE_PINNED["nu_star"], 1e-5)
    results["zone"] = out.zone == WORKED_EXAMPLE_PINNED["zone"]
    results["hint"] = out.hint == WORKED_EXAMPLE_PINNED["hint"]
    results["usable"] = near(out.usable, WORKED_EXAMPLE_PINNED["usable"], 1e-5)
    results["gate_open"] = out.gate_open is True
    raw_mass_hint = max(
        ("dQ_dM", "dQ_dPi", "dQ_dnu"),
        key=lambda k: abs(out.gradients[k]),
    )
    results["raw_grad_prefers_mass"] = raw_mass_hint == "dQ_dM"
    results["scaled_hint_cuts_latency"] = out.hint == "cut_bottleneck_latency"

    # Rest reduction still holds on the slice-built equation.
    rest_rec = worked_example_record()
    rest_rec.wm_turnover = 0.0
    rest_rec.retrieval_attempts = 1.0
    rest_rec.retrieval_hits = 0.0
    rest_rec.mean_retrieval_score = 0.0
    rest_rec.pathway_events = 0.0
    rest_rec.control_actions = 0.0
    rest_rec.merge_writes = 0.0
    rest_rec.merge_confidence = 0.0
    # Force zero flux regardless of score mix
    rest = compute_slice(rest_rec)
    # F_ret uses attempts=1 hits=0 score=0 => 0; others sat(0)=0
    results["rest_flux_near_zero"] = rest.terms["Pi"] < 1e-12
    results["rest_matches_E0"] = abs(rest.terms["Q"] - rest.terms["rest_energy"]) < 1e-9

    # Multiplicative budget bounds
    results["usable_in_unit"] = 0.0 <= out.usable <= 1.0
    results["Q_eff_le_Q"] = out.Q_eff <= out.terms["Q"] + 1e-12

    # Missing coverage falls back
    bare = TelemetryRecord(memory_entries=120.0)
    results["mem_fallback"] = abs(estimate_C_mem(bare) - sat(120.0, K_MEM)) < 1e-12

    # Weight tables are simplexes
    for name, table in (
        ("official", (ALPHA_IDENTIFIED, BETA_IDENTIFIED)),
        ("equal", (ALPHA_EQUAL, BETA_EQUAL)),
        ("promotion", (ALPHA_PROMOTION, BETA_PROMOTION)),
    ):
        a, b = table
        results[f"simplex_{name}_alpha"] = abs(sum(a.values()) - 1.0) < 1e-9
        results[f"simplex_{name}_beta"] = abs(sum(b.values()) - 1.0) < 1e-9

    # Linear instrument is not the law
    results["linear_ne_quadratic"] = abs(out.Q_lin - out.terms["Q"]) > 1.0

    # Gate closes in crisis
    crisis = worked_example_record()
    crisis.mode = "pathological"
    results["gate_closes"] = compute_slice(crisis).gate_open is False

    return results


def render_worked_example() -> str:
    rec = worked_example_record()
    out = compute_slice(rec)
    lines = [
        "worked_example  loaded-but-coherent",
        f"weight_table    {out.weight_table}",
        f"C_id            {out.primitives['C_id']:.6f}",
        f"C_mem           {out.primitives['C_mem']:.6f}",
        f"C_graph         {out.primitives['C_graph']:.6f}",
        f"C_perm          {out.primitives['C_perm']:.6f}",
        f"F_wm            {out.primitives['F_wm']:.6f}",
        f"F_ret           {out.primitives['F_ret']:.6f}",
        f"F_path          {out.primitives['F_path']:.6f}",
        f"F_ctrl          {out.primitives['F_ctrl']:.6f}",
        f"F_merge         {out.primitives['F_merge']:.6f}",
        f"M               {out.terms['M']:.6f}",
        f"Pi              {out.terms['Pi']:.6f}",
        f"nu_star         {out.terms['nu_star']:.6f}",
        f"r               {out.terms['r']:.6f}",
        f"M_tilde         {out.terms['M_tilde']:.6f}",
        f"Pi_tilde        {out.terms['Pi_tilde']:.6f}",
        f"Q               {out.terms['Q']:.6f}",
        f"E0              {out.terms['rest_energy']:.6f}",
        f"H_mu            {out.primitives['H_mu']:.6f}",
        f"E_norm          {out.primitives['E_norm']:.6f}",
        f"D_drift         {out.primitives['D_drift']:.6f}",
        f"usable          {out.usable:.6f}",
        f"Q_eff           {out.Q_eff:.6f}",
        f"Q_lin           {out.Q_lin:.6f}",
        f"Phi_org         {out.phi['Phi_org']:.6f}",
        f"zone            {out.zone}",
        f"hint            {out.hint}",
        f"gate_open       {out.gate_open}",
        f"dQ_dM           {out.gradients['dQ_dM']:.6f}",
        f"dQ_dPi          {out.gradients['dQ_dPi']:.6f}",
        f"dQ_dnu          {out.gradients['dQ_dnu']:.6f}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Computable Lineage slice")
    parser.add_argument("--example", action="store_true", help="print worked example")
    parser.add_argument("--json", metavar="PATH", help="compute from a telemetry JSON file")
    args = parser.parse_args()

    suite = run_slice_suite()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("slice_validation_checks_passed", len(suite))

    if args.example or args.json is None:
        print()
        print(render_worked_example())

    if args.json:
        with open(args.json, encoding="utf-8") as fh:
            payload = json.load(fh)
        rec = TelemetryRecord(**payload)
        print()
        print(json.dumps(compute_slice(rec).to_dict(), indent=2, sort_keys=True))
