"""
Operational control on the capacity partition Λ_job + Λ_W = Λ_M.

Companion to LINEAGE_OPERATIONAL_CONTROL.md.
Does not change official v2. Scores Λ_W, not Q.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math
from typing import Literal

try:
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_R
    from lineage_ops_v2 import mm1_sojourn, renewal_lambda_M, stability_margin
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_R
    from lineage_ops_v2 import mm1_sojourn, renewal_lambda_M, stability_margin


STEP_M = 0.05
STEP_PI = 0.10
STEP_NU = 1.0  # Hz
PI_HARD = 0.85
U_CRITICAL = 0.25

OpsAction = Literal[
    "unstable_shed_load",
    "shed_load",
    "repair_health",
    "raise_mass",
    "cut_bottleneck_latency",
]


def lambda_job(M: float, Pi: float, nu_star: float) -> float:
    """Theorem 1: Λ_job = M Π ν*."""
    return float(M) * float(Pi) * float(nu_star)


def lambda_W(M: float, Pi: float, nu_star: float) -> float:
    """Theorem 2: Λ_W = M (1−Π) ν*  (0 if unstable)."""
    if Pi >= 1.0:
        return 0.0
    return float(M) * (1.0 - float(Pi)) * float(nu_star)


def partition(M: float, Pi: float, nu_star: float) -> dict[str, float]:
    installed = renewal_lambda_M(M, nu_star)
    job = lambda_job(M, Pi, nu_star)
    resp = lambda_W(M, Pi, nu_star)
    return {
        "Lambda_M": installed,
        "Lambda_job": job,
        "Lambda_W": resp,
        "sum": job + resp,
    }


def step_scores(M: float, Pi: float, nu_star: float) -> dict[str, float]:
    """Theorem 4: expected ΔΛ_W for one feasible tick."""
    eta = max(0.0, 1.0 - float(Pi))
    shed = float(M) * min(STEP_PI, max(0.0, float(Pi))) * float(nu_star)
    return {
        "raise_mass": STEP_M * eta * float(nu_star),
        "shed_load": shed,
        "cut_bottleneck_latency": float(M) * eta * STEP_NU,
    }


def ops_action(M: float, Pi: float, nu_star: float, u: float) -> OpsAction:
    """Hard safety first, then argmax ΔΛ_W."""
    if Pi >= 1.0:
        return "unstable_shed_load"
    if Pi >= PI_HARD:
        return "shed_load"
    if u < U_CRITICAL:
        return "repair_health"
    scores = step_scores(M, Pi, nu_star)
    return max(scores, key=scores.get)  # type: ignore[return-value]


def ops_action_text(action: OpsAction, Pi: float, W: float, tau_star: float) -> str:
    if action == "unstable_shed_load":
        return "Π ≥ 1. Utilization reading is unstable. Shed load."
    if action == "shed_load":
        return (
            f"Shed flux. Margin {1.0 - Pi:.3f}, sojourn {W:.3f} s "
            f"against service {tau_star:.3f} s."
        )
    if action == "repair_health":
        return "Usable fraction is critical. Repair uncertainty, fracture, or drift before ascent."
    if action == "raise_mass":
        return "Raise structural mass. Responsiveness is limited by M, not the clock."
    return "Cut the slowest pipe. Responsiveness is limited by ν*."


def shed_pi(Pi: float, delta: float) -> float:
    if delta <= 0.0:
        raise ValueError("shed delta must be > 0")
    return max(0.0, float(Pi) - float(delta))


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}
    part = partition(WORK_M, WORK_PI, WORK_R)
    results["partition"] = abs(part["sum"] - part["Lambda_M"]) < 1e-12
    results["job_formula"] = abs(part["Lambda_job"] - WORK_M * WORK_PI * WORK_R) < 1e-12
    results["W_formula"] = abs(part["Lambda_W"] - WORK_M * (1.0 - WORK_PI) * WORK_R) < 1e-12
    results["W_is_M_over_sojourn"] = abs(
        part["Lambda_W"] - WORK_M / mm1_sojourn(1.0 / WORK_R, WORK_PI)
    ) < 1e-12

    scores = step_scores(WORK_M, WORK_PI, WORK_R)
    results["shed_wins_working_point"] = (
        scores["shed_load"] > scores["cut_bottleneck_latency"] > scores["raise_mass"]
    )
    results["working_action"] = ops_action(WORK_M, WORK_PI, WORK_R, 0.84) == "shed_load"

    results["hard_unstable"] = ops_action(WORK_M, 1.0, WORK_R, 0.84) == "unstable_shed_load"
    results["hard_hot"] = ops_action(WORK_M, 0.90, WORK_R, 0.84) == "shed_load"
    results["hard_health"] = ops_action(WORK_M, 0.20, WORK_R, 0.10) == "repair_health"

    # Low utilization, slow clock: cut can win Λ_W.
    results["cut_can_win"] = (
        ops_action(0.20, 0.10, 2.0, 0.90) == "cut_bottleneck_latency"
        or step_scores(0.20, 0.10, 2.0)["cut_bottleneck_latency"]
        >= step_scores(0.20, 0.10, 2.0)["shed_load"]
    )

    shed = shed_pi(WORK_PI, STEP_PI)
    results["shed_raises_W"] = lambda_W(WORK_M, shed, WORK_R) > part["Lambda_W"]
    results["shed_lowers_job"] = lambda_job(WORK_M, shed, WORK_R) < part["Lambda_job"]
    return results


def render_working_point() -> str:
    part = partition(WORK_M, WORK_PI, WORK_R)
    scores = step_scores(WORK_M, WORK_PI, WORK_R)
    action = ops_action(WORK_M, WORK_PI, WORK_R, 0.84)
    W = mm1_sojourn(1.0 / WORK_R, WORK_PI)
    lines = [
        "working_point  operational control",
        f"Lambda_M        {part['Lambda_M']:.6f}",
        f"Lambda_job      {part['Lambda_job']:.6f}",
        f"Lambda_W        {part['Lambda_W']:.6f}",
        f"dW_raise_mass   {scores['raise_mass']:.6f}",
        f"dW_shed_load    {scores['shed_load']:.6f}",
        f"dW_cut_nu       {scores['cut_bottleneck_latency']:.6f}",
        f"ops_action      {action}",
        f"W_sojourn       {W:.6f}",
        f"margin          {stability_margin(WORK_PI):.6f}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("control_checks_passed", len(suite))
    print()
    print(render_working_point())
