"""
Pareto SLA, Amdahl cuts, Pollaczek–Khinchine, hypoexponential tail.

Companion to LINEAGE_PARETO_AMDAHL_PK.md.
Does not change official v2.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math

try:
    from lineage_control_v2 import lambda_W, lambda_job
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_TAU
    from lineage_network_v2 import (
        DEFAULT_KAPPA,
        DEFAULT_W_MAX,
        WORK_TAUS,
        network_card,
        pi_star,
        service_sum,
        tandem_lambda_W,
    )
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_control_v2 import lambda_W, lambda_job
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_TAU
    from lineage_network_v2 import (
        DEFAULT_KAPPA,
        DEFAULT_W_MAX,
        WORK_TAUS,
        network_card,
        pi_star,
        service_sum,
        tandem_lambda_W,
    )


DEFAULT_ALPHA = 0.10  # percentile SLA; hyperparameter, not a law


def pk_kappa(c_s2: float) -> float:
    """Pollaczek–Khinchine variability: κ = (1 + c_s²)/2. Poisson arrivals."""
    if c_s2 < 0.0:
        raise ValueError("c_s² must be ≥ 0")
    return (1.0 + float(c_s2)) / 2.0


def serial_fraction(taus: list[float] | tuple[float, ...]) -> float:
    T = service_sum(taus)
    return max(taus) / T


def bottleneck_slack(taus: list[float] | tuple[float, ...]) -> float:
    """Seconds you can cut the slowest pipe before the argmax moves."""
    ordered = sorted((float(t) for t in taus), reverse=True)
    if len(ordered) == 1:
        return ordered[0]
    return ordered[0] - ordered[1]


def shed_needed(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    return max(0.0, float(Pi) - pi_star(taus, W_max, kappa))


def cut_T_needed(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Seconds of total service to cut, Π held. 0 if already under SLA."""
    if Pi >= 1.0:
        return math.inf
    T = service_sum(taus)
    if kappa == 1.0:
        T_star = float(W_max) * (1.0 - float(Pi))
    else:
        # Invert W = T (1 + κ Π/(1−Π)) ≤ W_max
        T_star = float(W_max) / (1.0 + float(kappa) * float(Pi) / (1.0 - float(Pi)))
    return max(0.0, T - T_star)


def sla_wall_lambda_W(M: float, W_max: float = DEFAULT_W_MAX) -> float:
    """Theorem 2: on W_net = W_max, Λ_W,net = M / W_max."""
    if W_max <= 0.0:
        return 0.0
    return float(M) / float(W_max)


def job_cap(
    M: float,
    taus: list[float] | tuple[float, ...],
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Max Λ_job that still meets the mean SLA."""
    tau_star = max(taus)
    return float(M) * pi_star(taus, W_max, kappa) / tau_star


def pi_min(M: float, nu_star: float, lambda_min: float) -> float:
    if M <= 0.0 or nu_star <= 0.0:
        return 1.0
    return max(0.0, float(lambda_min) / (float(M) * float(nu_star)))


def pareto_feasible(
    M: float,
    taus: list[float] | tuple[float, ...],
    lambda_min: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> bool:
    star = pi_star(taus, W_max, kappa)
    return 0.0 <= pi_min(M, 1.0 / max(taus), lambda_min) <= star < 1.0


def sojourn_rates(
    taus: list[float] | tuple[float, ...],
    Pi: float,
) -> tuple[float, ...]:
    """μ_ℓ = (1−Π)/τ_ℓ for Jackson-exponential sojourns."""
    if Pi >= 1.0:
        return tuple(0.0 for _ in taus)
    eta = 1.0 - float(Pi)
    return tuple(eta / float(t) for t in taus)


def hypoexp_survival(rates: list[float] | tuple[float, ...], t: float) -> float:
    """
    P(S > t) for a sum of independent Exp(μ_j) with distinct positive rates.
    """
    if t <= 0.0:
        return 1.0
    mus = [float(m) for m in rates]
    if any(m <= 0.0 for m in mus):
        return 1.0
    if len(set(round(m, 12) for m in mus)) != len(mus):
        raise ValueError("hypoexp_survival needs distinct rates")
    total = 0.0
    for j, muj in enumerate(mus):
        coeff = 1.0
        for k, muk in enumerate(mus):
            if k == j:
                continue
            coeff *= muk / (muk - muj)
        total += coeff * math.exp(-muj * t)
    return max(0.0, min(1.0, total))


def violation_prob(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float | None:
    """Exact Jackson-exponential tail. None if κ ≠ 1 or rates collide."""
    if kappa != 1.0:
        return None
    try:
        return hypoexp_survival(sojourn_rates(taus, Pi), W_max)
    except ValueError:
        return None


def pi_star_percentile(
    taus: list[float] | tuple[float, ...],
    W_max: float,
    alpha: float = DEFAULT_ALPHA,
    lo: float = 0.0,
    hi: float = 0.999,
) -> float:
    """Largest Π with P(W_net > W_max) ≤ α. κ = 1. Bisection."""
    if alpha <= 0.0:
        return 0.0
    if violation_prob(taus, lo, W_max, 1.0) is None:
        return 0.0
    if (violation_prob(taus, lo, W_max, 1.0) or 1.0) > alpha:
        return 0.0
    for _ in range(48):
        mid = 0.5 * (lo + hi)
        p = violation_prob(taus, mid, W_max, 1.0)
        if p is None or p > alpha:
            hi = mid
        else:
            lo = mid
    return lo


def qos_action_text(
    action: str,
    Pi: float,
    W_net: float,
    W_max: float,
    shed: float,
    cut_ms: float,
    tau_star: float,
    over: bool,
) -> str:
    if action == "unstable_shed_load":
        return "Π ≥ 1. Utilization reading is unstable. Shed load."
    if over:
        return (
            f"Over delay SLA. W_net {W_net:.3f} s > {W_max:.3f} s. "
            f"Shed Π by {shed:.3f} or cut total service by {cut_ms:.1f} ms."
        )
    if action == "shed_load":
        return (
            f"Shed flux. Margin {1.0 - Pi:.3f}, tandem sojourn {W_net:.3f} s "
            f"against bottleneck service {tau_star:.3f} s."
        )
    if action == "repair_health":
        return "Usable fraction is critical. Repair uncertainty, fracture, or drift before ascent."
    if action == "raise_mass":
        return "Raise structural mass. Responsiveness is limited by M, not the clock."
    return "Cut the slowest pipe. Responsiveness is limited by ν*."


def qos_card(
    M: float,
    Pi: float,
    taus: list[float] | tuple[float, ...],
    u: float = 0.84,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
    alpha: float | None = None,
) -> dict[str, float | bool | str | None]:
    net = network_card(M, Pi, taus, u, W_max, kappa)
    T = float(net["T"])
    tau_star = float(net["tau_star"])
    W_net = float(net["W_net"])
    shed = shed_needed(taus, Pi, W_max, kappa)
    cut_s = cut_T_needed(taus, Pi, W_max, kappa)
    slack = bottleneck_slack(taus)
    p = violation_prob(taus, Pi, W_max, kappa)
    out: dict[str, float | bool | str | None] = {
        **net,
        "shed_needed": shed,
        "cut_T_s": cut_s,
        "cut_T_ms": cut_s * 1000.0 if math.isfinite(cut_s) else math.inf,
        "serial_fraction": serial_fraction(taus),
        "bottleneck_slack_s": slack,
        "fits_bottleneck": bool(math.isfinite(cut_s) and cut_s <= slack + 1e-12),
        "Lambda_W_wall": sla_wall_lambda_W(M, W_max),
        "Lambda_job": lambda_job(M, Pi, 1.0 / tau_star),
        "Lambda_job_cap": job_cap(M, taus, W_max, kappa),
        "p_over_sla": p,
        "T": T,
        "W_net": W_net,
    }
    if alpha is not None and kappa == 1.0:
        out["Pi_star_pct"] = pi_star_percentile(taus, W_max, alpha)
        out["alpha"] = float(alpha)
    return out


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}

    def near(a: float, b: float, tol: float = 1e-9) -> bool:
        return abs(a - b) <= tol

    results["pk_exp_is_one"] = near(pk_kappa(1.0), 1.0)
    results["pk_det_is_half"] = near(pk_kappa(0.0), 0.5)
    results["serial"] = near(serial_fraction(WORK_TAUS), WORK_TAU / 0.225)
    results["slack"] = near(bottleneck_slack(WORK_TAUS), 0.080)

    star = pi_star(WORK_TAUS, DEFAULT_W_MAX, 1.0)
    results["shed_needed"] = near(shed_needed(WORK_TAUS, WORK_PI), WORK_PI - star)
    cut = cut_T_needed(WORK_TAUS, WORK_PI)
    results["cut_T"] = near(cut, 0.225 - DEFAULT_W_MAX * (1.0 - WORK_PI))
    results["cut_fits"] = cut <= bottleneck_slack(WORK_TAUS)

    wall = sla_wall_lambda_W(WORK_M, DEFAULT_W_MAX)
    results["wall_formula"] = near(wall, WORK_M / DEFAULT_W_MAX)
    # Shed to Π* and cut to T* hit the same Λ_W,net.
    lam_shed = tandem_lambda_W(WORK_M, WORK_TAUS, star, 1.0)
    # Cut the bottleneck only by `cut` (fits slack).
    taus_bn = (WORK_TAUS[0] - cut, *WORK_TAUS[1:])
    lam_cut = tandem_lambda_W(WORK_M, taus_bn, WORK_PI, 1.0)
    results["wall_shed"] = near(lam_shed, wall, 1e-6)
    results["wall_cut"] = near(lam_cut, wall, 1e-6)
    results["single_to_net"] = near(
        lambda_W(WORK_M, WORK_PI, 1.0 / WORK_TAU)
        / tandem_lambda_W(WORK_M, WORK_TAUS, WORK_PI),
        0.225 / WORK_TAU,
    )

    results["job_cap_lt_live"] = job_cap(WORK_M, WORK_TAUS) < lambda_job(
        WORK_M, WORK_PI, 1.0 / WORK_TAU
    )
    results["pareto_live_infeasible_high_floor"] = not pareto_feasible(
        WORK_M, WORK_TAUS, lambda_min=10.0
    )
    results["pareto_zero_floor"] = pareto_feasible(WORK_M, WORK_TAUS, 0.0)

    # Two-stage closed form: Exp(2)+Exp(5) at t=1.
    closed = (5.0 / 3.0) * math.exp(-2.0) + (2.0 / -3.0) * math.exp(-5.0)
    results["hypo_two_stage"] = near(hypoexp_survival((2.0, 5.0), 1.0), closed, 1e-12)

    p = violation_prob(WORK_TAUS, WORK_PI)
    results["p_over_reported"] = p is not None and 0.30 < p < 0.50
    # Mean wall still late-delivers ~ e^{-1} of jobs.
    p_wall = violation_prob(WORK_TAUS, star)
    results["p_wall_near_e"] = p_wall is not None and abs(p_wall - math.exp(-1.0)) < 0.05
    results["pct_tighter"] = pi_star_percentile(WORK_TAUS, DEFAULT_W_MAX, 0.10) < star
    results["withheld_if_bursty"] = violation_prob(WORK_TAUS, WORK_PI, kappa=2.0) is None
    return results


def render_working_point() -> str:
    card = qos_card(WORK_M, WORK_PI, WORK_TAUS, alpha=DEFAULT_ALPHA)
    lines = ["working_point  Pareto / Amdahl / PK / tail"]
    for k, v in card.items():
        if isinstance(v, float):
            lines.append(f"{k:<20} {v:.6f}")
        else:
            lines.append(f"{k:<20} {v}")
    return "\n".join(lines)


if __name__ == "__main__":
    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("qos_checks_passed", len(suite))
    print()
    print(render_working_point())
