"""
Operations, Little, renewal-reward, Buckingham, M/M/1.

Companion to LINEAGE_OPERATIONS_LITTLE_RENEWAL.md.
Does not change official v2.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math

try:
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_Q, WORK_R, WORK_TAU, core_q
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_Q, WORK_R, WORK_TAU, core_q


def bottleneck_rate(taus: list[float]) -> float:
    """Lemma 1: ν* = 1 / max τ_ℓ."""
    if not taus or min(taus) <= 0.0:
        raise ValueError("latencies must be positive")
    return 1.0 / max(taus)


def little_occupancy(Pi: float) -> float:
    """Theorem 1: L_occ = Π under λ = Π ν*, W = τ*."""
    return float(Pi)


def renewal_lambda_M(M: float, nu_star: float) -> float:
    """Theorem 2: Λ_M = M ν*."""
    return float(M) * float(nu_star)


def renewal_lambda_q(M: float, Pi: float, nu_star: float) -> float:
    """Theorem 2: Λ_q = q ν*."""
    r = nu_star  # ν₀ = 1
    return core_q(M, Pi, r) * float(nu_star)


def usable_lambda(M: float, nu_star: float, u: float) -> float:
    return float(u) * renewal_lambda_M(M, nu_star)


def official_lift(lambda_q: float, nu_star: float) -> float:
    """Theorem 3: Q = ν* Λ_q."""
    return float(nu_star) * float(lambda_q)


def shannon_C(M: float, nu_star: float) -> float:
    """C = ν* log₂(1+M)."""
    if M < 0.0:
        raise ValueError("M must be ≥ 0")
    return float(nu_star) * math.log2(1.0 + float(M))


def stability_margin(Pi: float) -> float:
    """η = 1 − Π. Negative means the utilization reading is unstable."""
    return 1.0 - float(Pi)


def mm1_sojourn(tau_star: float, Pi: float) -> float:
    """W = τ* / (1−Π) for Π < 1, else +∞."""
    if Pi >= 1.0:
        return math.inf
    if Pi < 0.0 or tau_star <= 0.0:
        raise ValueError("need τ* > 0 and Π ≥ 0")
    return float(tau_star) / (1.0 - float(Pi))


def mm1_L_sys(Pi: float) -> float:
    if Pi >= 1.0:
        return math.inf
    return float(Pi) / (1.0 - float(Pi))


def mm1_L_queue(Pi: float) -> float:
    if Pi >= 1.0:
        return math.inf
    return (float(Pi) ** 2) / (1.0 - float(Pi))


def ops_card(M: float, Pi: float, nu_star: float, u: float = 1.0) -> dict[str, float]:
    tau = 1.0 / nu_star
    lam_m = renewal_lambda_M(M, nu_star)
    lam_q = renewal_lambda_q(M, Pi, nu_star)
    return {
        "nu_star": nu_star,
        "Lambda_M": lam_m,
        "Lambda_q": lam_q,
        "Lambda_eff": usable_lambda(M, nu_star, u),
        "C_shannon": shannon_C(M, nu_star),
        "Q_lift": official_lift(lam_q, nu_star),
        "eta": stability_margin(Pi),
        "W_sojourn": mm1_sojourn(tau, Pi),
        "L_occ": little_occupancy(Pi),
        "L_sys": mm1_L_sys(Pi),
        "L_queue": mm1_L_queue(Pi),
    }


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}

    def near(a: float, b: float, tol: float = 1e-9) -> bool:
        return abs(a - b) <= tol

    # Lemma 1
    results["bottleneck_max"] = near(bottleneck_rate([0.12, 0.04, 0.03, 0.02, 0.015]), 1.0 / 0.12)

    # Little occupancy
    results["little_occ"] = near(little_occupancy(WORK_PI), WORK_PI)

    # Renewal rates at the working point
    lam_m = renewal_lambda_M(WORK_M, WORK_R)
    lam_q = renewal_lambda_q(WORK_M, WORK_PI, WORK_R)
    results["lambda_M"] = near(lam_m, WORK_M * WORK_R)
    results["lambda_q_gt_M"] = lam_q > lam_m
    results["lambda_q_near_M"] = abs(lam_q - lam_m) < 0.03

    # Official Q is the lift
    results["Q_is_lift"] = near(official_lift(lam_q, WORK_R), WORK_Q, 5e-3)
    results["Q_over_lambda"] = near(WORK_Q / lam_q, WORK_R, 5e-4)

    # Buckingham classes: Λ ~ Hz, Q ~ Hz²
    results["degree1_scales"] = near(renewal_lambda_M(WORK_M, 2 * WORK_R), 2 * lam_m)
    results["degree2_scales"] = official_lift(renewal_lambda_q(WORK_M, WORK_PI, 2 * WORK_R), 2 * WORK_R) > 3.5 * WORK_Q

    # M/M/1
    eta = stability_margin(WORK_PI)
    W = mm1_sojourn(WORK_TAU, WORK_PI)
    results["margin"] = near(eta, 1.0 - WORK_PI)
    results["sojourn_gt_service"] = W > WORK_TAU
    results["sojourn_formula"] = near(W, WORK_TAU / (1.0 - WORK_PI))
    results["unstable_at_one"] = math.isinf(mm1_sojourn(WORK_TAU, 1.0))
    results["L_sys_formula"] = near(mm1_L_sys(WORK_PI), WORK_PI / (1.0 - WORK_PI))

    # Shannon cousin, same dimension class as Λ
    C = shannon_C(WORK_M, WORK_R)
    results["shannon_rate_class"] = near(shannon_C(WORK_M, 2 * WORK_R), 2 * C)
    results["shannon_positive"] = C > 0.0

    return results


def render_working_point() -> str:
    u = 0.839722
    card = ops_card(WORK_M, WORK_PI, WORK_R, u)
    lines = ["working_point  operations / Little / renewal"]
    for k, v in card.items():
        lines.append(f"{k:<14} {v:.6f}")
    return "\n".join(lines)


if __name__ == "__main__":
    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("ops_checks_passed", len(suite))
    print()
    print(render_working_point())
