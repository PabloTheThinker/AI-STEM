"""
Wait-closed loop on the five-stage tandem.

The plant emits a measured sojourn from the Lindley simulator.
The controller sees that measurement. It does not see Q.

Official Q stays on the tick as audit. A Q-scored counterfactual
controller is kept so the first-action fork can be checked:
wait-loop sheds, Q-loop cuts.

Companion to LINEAGE_CLOSED_LOOP.md.
Does not change official v2.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import argparse
import inspect
import json
import math
import sys
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Callable, Literal, Mapping

try:
    from lineage_control_v2 import STEP_PI, U_CRITICAL, shed_pi
    from lineage_core_v2 import WORK_M, WORK_PI, family_Q
    from lineage_network_v2 import (
        DEFAULT_KAPPA,
        DEFAULT_W_MAX,
        WORK_TAUS,
        service_sum,
    )
    from lineage_sim_v2 import SEED, simulate_tandem
    from lineage_traffic_v2 import (
        arrival_rate,
        miss_probability,
        shed_star,
        traffic_sojourn,
    )
    from lineage_use_v2 import evaluate_mapping, record_from_mapping, record_taus
except ImportError:  # pragma: no cover
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_control_v2 import STEP_PI, U_CRITICAL, shed_pi
    from lineage_core_v2 import WORK_M, WORK_PI, family_Q
    from lineage_network_v2 import (
        DEFAULT_KAPPA,
        DEFAULT_W_MAX,
        WORK_TAUS,
        service_sum,
    )
    from lineage_sim_v2 import SEED, simulate_tandem
    from lineage_traffic_v2 import (
        arrival_rate,
        miss_probability,
        shed_star,
        traffic_sojourn,
    )
    from lineage_use_v2 import evaluate_mapping, record_from_mapping, record_taus


SCHEMA = "fudoshin.lineage.loop/v1"
HOT_PI = 0.60
SLA_GUARD_S = 0.010
STEP_TAU_FRAC = 0.10
REPAIR_U = 0.15
LOOP_JOBS = 16_000
LOOP_WARMUP = 3_000
REL_ERR_MAX = 0.05

LoopAction = Literal[
    "unstable_shed_load",
    "shed_load",
    "repair_health",
    "raise_mass",
    "cut_bottleneck_latency",
    "hold",
]


@dataclass(frozen=True)
class PlantState:
    """Controllable plant. Q is not a coordinate."""

    M: float
    Pi: float
    taus: tuple[float, ...]
    u: float

    def tau_star(self) -> float:
        return max(self.taus)

    def nu_star(self) -> float:
        return 1.0 / self.tau_star()

    def r(self) -> float:
        return self.nu_star()


@dataclass(frozen=True)
class Observation:
    mean_W: float
    p_miss: float
    formula_W: float
    jobs: float
    source: Literal["measured", "formula"]

    @property
    def residual_s(self) -> float | None:
        if self.source != "measured":
            return None
        if not math.isfinite(self.mean_W) or not math.isfinite(self.formula_W):
            return None
        return self.mean_W - self.formula_W


@dataclass(frozen=True)
class Action:
    name: LoopAction
    amount: float
    reason: str
    scored_q: bool = False


@dataclass(frozen=True)
class Tick:
    t: int
    state: PlantState
    obs: Observation
    action: Action
    Q: float


@dataclass
class LoopResult:
    ticks: list[Tick]
    final: Observation
    final_state: PlantState


Controller = Callable[[PlantState, Observation, float], Action]


def hot_state(Pi: float = HOT_PI) -> PlantState:
    return PlantState(M=WORK_M, Pi=float(Pi), taus=WORK_TAUS, u=0.84)


def working_state() -> PlantState:
    return PlantState(M=WORK_M, Pi=WORK_PI, taus=WORK_TAUS, u=0.84)


def formula_wait(state: PlantState, kappa: float = DEFAULT_KAPPA) -> float:
    if state.Pi >= 1.0:
        return math.inf
    return traffic_sojourn(state.taus, state.Pi, kappa)


def audit_Q(state: PlantState) -> float:
    """Official Q for the card. Not an input to wait_controller."""
    return family_Q(state.M, state.Pi, state.r())


def measure(
    state: PlantState,
    n_jobs: int = LOOP_JOBS,
    warmup: int = LOOP_WARMUP,
    seed: int = SEED,
    w_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> Observation:
    """Exogenous sojourn. The simulator contains no sojourn formula."""
    theory = formula_wait(state, kappa)
    if state.Pi >= 1.0 or not math.isfinite(theory):
        return Observation(
            mean_W=math.inf,
            p_miss=1.0,
            formula_W=math.inf,
            jobs=0.0,
            source="measured",
        )
    lam = arrival_rate(state.Pi, state.taus)
    sim = simulate_tandem(
        lam, state.taus, n_jobs=n_jobs, warmup=warmup, seed=seed, w_max=w_max
    )
    return Observation(
        mean_W=float(sim["mean_W"]),
        p_miss=float(sim["p_miss"]),
        formula_W=theory,
        jobs=float(sim["jobs"]),
        source="measured",
    )


def window_seed(state: PlantState, t: int, seed0: int = SEED) -> int:
    return (
        int(seed0)
        + 31 * int(t)
        + int(round(state.Pi * 1000.0))
        + int(round(state.tau_star() * 10_000.0))
    )


def wait_controller(
    state: PlantState,
    measured_W: float,
    w_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> Action:
    """
    Gate on health and measured wait. Size a shed from the traffic
    model, then let the next measurement correct the residual.
    Does not take Q.
    """
    if state.Pi >= 1.0:
        return Action(
            "unstable_shed_load",
            min(STEP_PI, float(state.Pi)),
            "Π ≥ 1. Utilization reading is unstable.",
            False,
        )
    if state.u < U_CRITICAL:
        return Action(
            "repair_health",
            REPAIR_U,
            "usable fraction is critical; repair before flux.",
            False,
        )
    if math.isinf(measured_W) or measured_W > float(w_max):
        target = max(service_sum(state.taus) + 1e-9, float(w_max) - SLA_GUARD_S)
        delta = shed_star(state.taus, state.Pi, target, kappa)
        if delta <= 1e-12:
            delta = min(STEP_PI, 0.02)
        return Action(
            "shed_load",
            min(delta, STEP_PI),
            "measured wait exceeds the mean SLA.",
            False,
        )
    return Action("hold", 0.0, "measured wait is under the mean SLA.", False)


def q_controller(
    state: PlantState,
    measured_W: float = 0.0,
    w_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> Action:
    """Official-Q counterfactual: always cut the bottleneck. Ignores wait."""
    del measured_W, w_max, kappa
    return Action(
        "cut_bottleneck_latency",
        STEP_TAU_FRAC,
        "official ∂Q hint: Q grows as ν*².",
        True,
    )


def open_controller(
    state: PlantState,
    measured_W: float = 0.0,
    w_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> Action:
    del state, measured_W, w_max, kappa
    return Action("hold", 0.0, "open loop: observe only.", False)


def decide(
    controller: Controller,
    state: PlantState,
    obs: Observation,
    w_max: float,
) -> Action:
    return controller(state, obs, w_max)


def _wait_as_controller(
    state: PlantState, obs: Observation, w_max: float
) -> Action:
    return wait_controller(state, obs.mean_W, w_max)


def _q_as_controller(
    state: PlantState, obs: Observation, w_max: float
) -> Action:
    return q_controller(state, obs.mean_W, w_max)


def _open_as_controller(
    state: PlantState, obs: Observation, w_max: float
) -> Action:
    return open_controller(state, obs.mean_W, w_max)


CONTROLLERS: dict[str, Controller] = {
    "wait": _wait_as_controller,
    "q": _q_as_controller,
    "open": _open_as_controller,
}


def apply_action(state: PlantState, action: Action) -> PlantState:
    name = action.name
    amount = float(action.amount)
    if name in {"shed_load", "unstable_shed_load"}:
        if amount <= 0.0:
            return state
        return replace(state, Pi=shed_pi(state.Pi, amount))
    if name == "cut_bottleneck_latency":
        taus = list(state.taus)
        idx = max(range(len(taus)), key=lambda i: taus[i])
        frac = min(0.95, max(0.0, amount))
        taus[idx] = max(1e-6, taus[idx] * (1.0 - frac))
        return replace(state, taus=tuple(taus))
    if name == "repair_health":
        return replace(state, u=min(1.0, state.u + max(0.0, amount)))
    if name == "raise_mass":
        return replace(state, M=min(1.0, state.M + max(0.0, amount)))
    return state


def run_loop(
    state: PlantState,
    controller: Controller,
    ticks: int = 6,
    w_max: float = DEFAULT_W_MAX,
    n_jobs: int = LOOP_JOBS,
    warmup: int = LOOP_WARMUP,
    seed0: int = SEED,
    kappa: float = DEFAULT_KAPPA,
) -> LoopResult:
    if ticks < 1:
        raise ValueError("ticks must be ≥ 1")
    history: list[Tick] = []
    current = state
    for t in range(ticks):
        obs = measure(
            current,
            n_jobs=n_jobs,
            warmup=warmup,
            seed=window_seed(current, t, seed0),
            w_max=w_max,
            kappa=kappa,
        )
        action = decide(controller, current, obs, w_max)
        history.append(
            Tick(t=t, state=current, obs=obs, action=action, Q=audit_Q(current))
        )
        current = apply_action(current, action)
    final = measure(
        current,
        n_jobs=n_jobs,
        warmup=warmup,
        seed=window_seed(current, ticks, seed0),
        w_max=w_max,
        kappa=kappa,
    )
    return LoopResult(ticks=history, final=final, final_state=current)


def plant_from_mapping(
    data: Mapping[str, Any],
) -> tuple[PlantState, float | None]:
    """
    Accept a plant dict {M, Pi, taus, u} or a telemetry window.
    Optional measured_wait_s is the exogenous residual.
    """
    measured_raw = data.get("measured_wait_s")
    measured = None if measured_raw is None else float(measured_raw)
    if "Pi" in data and "taus" in data:
        taus_raw = data["taus"]
        if not isinstance(taus_raw, (list, tuple)) or not taus_raw:
            raise ValueError("taus must be a non-empty array")
        return (
            PlantState(
                M=float(data.get("M", WORK_M)),
                Pi=float(data["Pi"]),
                taus=tuple(float(t) for t in taus_raw),
                u=float(data.get("u", 0.84)),
            ),
            measured,
        )
    rec, _ = record_from_mapping(data)
    card = evaluate_mapping(data)
    return (
        PlantState(
            M=float(card["M"]),
            Pi=float(card["Pi"]),
            taus=record_taus(rec),
            u=float(card["u"]),
        ),
        measured,
    )


def replay_window(
    data: Mapping[str, Any],
    w_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> dict[str, Any]:
    state, measured = plant_from_mapping(data)
    theory = formula_wait(state, kappa)
    if measured is None:
        used = theory
        source: Literal["measured", "formula"] = "formula"
    else:
        used = measured
        source = "measured"
    action = wait_controller(state, used, w_max, kappa)
    residual = None
    if measured is not None and math.isfinite(theory):
        residual = measured - theory
    return {
        "schema": SCHEMA,
        "action": action.name,
        "amount": action.amount,
        "reason": action.reason,
        "scored_q": action.scored_q,
        "wait_used": used,
        "wait_source": source,
        "formula_W": theory,
        "residual_s": residual,
        "p_over_sla": miss_probability(state.taus, state.Pi, w_max, kappa)
        if state.Pi < 1.0
        else 1.0,
        "M": state.M,
        "Pi": state.Pi,
        "u": state.u,
        "taus": list(state.taus),
        "Q": audit_Q(state),
    }


def replay_jsonl(
    path: Path,
    w_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    text = path.read_text(encoding="utf-8")
    stripped = text.strip()
    if stripped.startswith("{"):
        try:
            one = json.loads(stripped)
        except json.JSONDecodeError:
            one = None
        if isinstance(one, dict):
            rows.append(replay_window(one, w_max, kappa))
            return rows
    for n, line in enumerate(text.splitlines(), start=1):
        raw = line.strip()
        if not raw:
            continue
        try:
            data = json.loads(raw)
            rows.append(replay_window(data, w_max, kappa))
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            rows.append({"line": n, "error": str(exc)})
    return rows


def _tick_dict(tick: Tick) -> dict[str, Any]:
    return {
        "t": tick.t,
        "Pi": tick.state.Pi,
        "M": tick.state.M,
        "u": tick.state.u,
        "tau_star": tick.state.tau_star(),
        "measured_W": tick.obs.mean_W,
        "formula_W": tick.obs.formula_W,
        "p_miss": tick.obs.p_miss,
        "residual_s": tick.obs.residual_s,
        "action": tick.action.name,
        "amount": tick.action.amount,
        "scored_q": tick.action.scored_q,
        "Q": tick.Q,
    }


def result_dict(result: LoopResult) -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "ticks": [_tick_dict(t) for t in result.ticks],
        "final": {
            "Pi": result.final_state.Pi,
            "M": result.final_state.M,
            "u": result.final_state.u,
            "tau_star": result.final_state.tau_star(),
            "measured_W": result.final.mean_W,
            "formula_W": result.final.formula_W,
            "p_miss": result.final.p_miss,
            "residual_s": result.final.residual_s,
            "Q": audit_Q(result.final_state),
        },
    }


def render_result(result: LoopResult, title: str) -> str:
    lines = [
        title,
        f"{'t':>3}  {'Pi':>7}  {'meas_W':>8}  {'form_W':>8}  {'p_miss':>7}  "
        f"{'action':<24}  {'amt':>6}  {'Q':>7}",
    ]
    for tick in result.ticks:
        lines.append(
            f"{tick.t:3d}  {tick.state.Pi:7.4f}  {tick.obs.mean_W:8.4f}  "
            f"{tick.obs.formula_W:8.4f}  {tick.obs.p_miss:7.3f}  "
            f"{tick.action.name:<24}  {tick.action.amount:6.3f}  {tick.Q:7.3f}"
        )
    lines.append(
        f"end {result.final_state.Pi:7.4f}  {result.final.mean_W:8.4f}  "
        f"{result.final.formula_W:8.4f}  {result.final.p_miss:7.3f}  "
        f"{'—':<24}  {'':>6}  {audit_Q(result.final_state):7.3f}"
    )
    return "\n".join(lines)


def _relative_errors(result: LoopResult) -> list[float]:
    errs: list[float] = []
    points = [tick.obs for tick in result.ticks] + [result.final]
    for obs in points:
        if obs.formula_W > 0.0 and math.isfinite(obs.formula_W):
            errs.append(abs(obs.mean_W - obs.formula_W) / obs.formula_W)
    return errs


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}

    params = inspect.signature(wait_controller).parameters
    results["wait_controller_has_no_Q"] = not any(
        name.lower() in {"q", "q_eff", "official_q"} for name in params
    )
    body = inspect.getsource(wait_controller)
    results["wait_body_does_not_score_Q"] = (
        "family_Q" not in body and "core_q" not in body and "Q_eff" not in body
    )

    wp = working_state()
    wp_obs = measure(wp, seed=SEED + 3)
    wp_act = wait_controller(wp, wp_obs.mean_W)
    results["working_point_holds"] = (
        wp_act.name == "hold" and wp_obs.mean_W < DEFAULT_W_MAX
    )
    results["working_q_still_cuts"] = (
        q_controller(wp, wp_obs.mean_W).name == "cut_bottleneck_latency"
    )

    sick = PlantState(M=WORK_M, Pi=0.20, taus=WORK_TAUS, u=0.10)
    results["health_repairs"] = (
        wait_controller(sick, 0.25).name == "repair_health"
    )
    unstable = PlantState(M=WORK_M, Pi=1.0, taus=WORK_TAUS, u=0.84)
    results["unstable_sheds"] = (
        wait_controller(unstable, math.inf).name == "unstable_shed_load"
    )

    start = hot_state()
    opened = run_loop(start, CONTROLLERS["open"], ticks=3)
    closed = run_loop(start, CONTROLLERS["wait"], ticks=4)
    qloop = run_loop(start, CONTROLLERS["q"], ticks=2)

    results["open_loop_stays_over"] = all(
        tick.obs.mean_W > DEFAULT_W_MAX for tick in opened.ticks
    ) and opened.final.mean_W > DEFAULT_W_MAX
    results["closed_first_action_sheds"] = (
        closed.ticks[0].action.name == "shed_load"
    )
    results["q_first_action_cuts"] = (
        qloop.ticks[0].action.name == "cut_bottleneck_latency"
    )
    results["closed_meets_mean_sla"] = closed.final.mean_W <= DEFAULT_W_MAX
    results["open_does_not_meet"] = opened.final.mean_W > DEFAULT_W_MAX
    results["wait_never_scores_q"] = all(
        not tick.action.scored_q for tick in closed.ticks
    ) and qloop.ticks[0].action.scored_q
    errs = _relative_errors(closed)
    results["formula_tracks_mechanism"] = bool(errs) and max(errs) < REL_ERR_MAX
    results["tail_survives_mean_repair"] = closed.final.p_miss > 0.20

    shed = apply_action(
        start, Action("shed_load", 0.05, "check", False)
    )
    results["apply_shed_lowers_Pi"] = abs(shed.Pi - (start.Pi - 0.05)) < 1e-12
    cut = apply_action(
        start, Action("cut_bottleneck_latency", 0.10, "check", True)
    )
    results["apply_cut_lowers_tau"] = cut.tau_star() < start.tau_star()
    held = apply_action(start, Action("hold", 0.0, "check", False))
    results["hold_is_noop"] = held == start

    here = Path(__file__).resolve().parent
    sample = here / "hot_windows.jsonl"
    replayed = replay_jsonl(sample)
    results["replay_four_windows"] = len(replayed) == 4 and all(
        "error" not in row for row in replayed
    )
    results["replay_hot_formula_sheds"] = replayed[0].get("action") == "shed_load"
    results["replay_hot_measured_sheds"] = replayed[1].get("action") == "shed_load"
    results["replay_working_holds"] = replayed[2].get("action") == "hold"
    results["replay_health_repairs"] = replayed[3].get("action") == "repair_health"
    results["replay_exogenous_residual"] = (
        replayed[1].get("wait_source") == "measured"
        and replayed[1].get("residual_s") is not None
    )
    results["replay_does_not_score_Q"] = all(
        row.get("scored_q") is False for row in replayed
    )
    return results


def render_working_point() -> str:
    closed = run_loop(hot_state(), CONTROLLERS["wait"], ticks=4)
    opened = run_loop(hot_state(), CONTROLLERS["open"], ticks=3)
    qloop = run_loop(hot_state(), CONTROLLERS["q"], ticks=2)
    return "\n\n".join(
        [
            render_result(opened, "open loop  Π=0.60  observe only"),
            render_result(closed, "wait loop  Π=0.60  measure → shed/hold"),
            render_result(qloop, "Q loop     Π=0.60  official hint (cut)"),
        ]
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Wait-closed loop. Official Q is audit, not the plant."
    )
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--replay", type=Path)
    parser.add_argument("--ticks", type=int, default=6)
    parser.add_argument("--pi", type=float, default=HOT_PI)
    parser.add_argument(
        "--controller", choices=tuple(CONTROLLERS), default="wait"
    )
    parser.add_argument(
        "--compare",
        action="store_true",
        help="run wait, Q, and open controllers from the same start",
    )
    parser.add_argument("--w-max", type=float, default=DEFAULT_W_MAX)
    parser.add_argument("--jobs", type=int, default=LOOP_JOBS)
    parser.add_argument("--warmup", type=int, default=LOOP_WARMUP)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if args.replay is not None:
        rows = replay_jsonl(args.replay, w_max=args.w_max)
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            for i, row in enumerate(rows):
                if "error" in row:
                    print(f"{i}  ERROR  {row['error']}")
                    continue
                print(
                    f"{i}  {row['action']:<24} amt={row['amount']:.4f}  "
                    f"wait={row['wait_used']:.4f} ({row['wait_source']})  "
                    f"formula={row['formula_W']:.4f}"
                )
        return 0

    if args.run or args.compare:
        start = hot_state(args.pi)
        kwargs = {
            "ticks": args.ticks,
            "w_max": args.w_max,
            "n_jobs": args.jobs,
            "warmup": args.warmup,
        }
        if args.compare:
            payload = {
                name: result_dict(run_loop(start, ctrl, **kwargs))
                for name, ctrl in CONTROLLERS.items()
            }
            if args.json:
                print(json.dumps(payload, indent=2))
            else:
                for name, ctrl in CONTROLLERS.items():
                    print(
                        render_result(
                            run_loop(start, ctrl, **kwargs), f"{name} loop"
                        )
                    )
                    print()
            return 0
        result = run_loop(start, CONTROLLERS[args.controller], **kwargs)
        if args.json:
            print(json.dumps(result_dict(result), indent=2))
        else:
            print(
                render_result(
                    result, f"{args.controller} loop  Π={args.pi:.3f}"
                )
            )
        return 0

    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        return 1
    print("loop_checks_passed", len(suite))
    print()
    print(render_working_point())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
