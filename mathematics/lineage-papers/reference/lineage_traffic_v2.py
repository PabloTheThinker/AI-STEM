"""
Single-stream traffic equations for the five-stage tandem.

Corrects the common-Π reading in lineage_network_v2.py: one stream of
jobs visits every stage, so node ℓ runs at ρ_ℓ = λ τ_ℓ, not at the
bottleneck's utilization. The common-Π model is kept as the all-hot
upper bound.

Companion to LINEAGE_TRAFFIC_AND_SIMULATION.md.
Does not change official v2.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math

try:
    from lineage_control_v2 import ops_action
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_TAU
    from lineage_network_v2 import (
        DEFAULT_KAPPA,
        DEFAULT_W_MAX,
        WORK_TAUS,
        service_sum,
        tandem_sojourn,
    )
    from lineage_qos_v2 import bottleneck_slack, hypoexp_survival, serial_fraction
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_control_v2 import ops_action
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_TAU
    from lineage_network_v2 import (
        DEFAULT_KAPPA,
        DEFAULT_W_MAX,
        WORK_TAUS,
        service_sum,
        tandem_sojourn,
    )
    from lineage_qos_v2 import bottleneck_slack, hypoexp_survival, serial_fraction


def arrival_rate(Pi: float, taus: list[float] | tuple[float, ...]) -> float:
    """λ = Π ν* : bottleneck utilization Π fixes the stream rate."""
    return float(Pi) / max(taus)


def utilizations(
    taus: list[float] | tuple[float, ...], Pi: float
) -> tuple[float, ...]:
    """Traffic equation: ρ_ℓ = λ τ_ℓ. The bottleneck sits at Π exactly."""
    lam = arrival_rate(Pi, taus)
    return tuple(lam * float(t) for t in taus)


def traffic_sojourn(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """W_net = Σ τ_ℓ (1 + κ ρ_ℓ/(1−ρ_ℓ)) with per-node ρ_ℓ = λ τ_ℓ."""
    if Pi < 0.0 or kappa < 0.0:
        raise ValueError("Π ≥ 0 and κ ≥ 0")
    lam = arrival_rate(Pi, taus)
    total = 0.0
    for t in taus:
        rho = lam * float(t)
        if rho >= 1.0:
            return math.inf
        total += float(t) * (1.0 + float(kappa) * rho / (1.0 - rho))
    return total


def traffic_lambda_W(
    M: float,
    taus: list[float] | tuple[float, ...],
    Pi: float,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    W = traffic_sojourn(taus, Pi, kappa)
    if W <= 0.0 or math.isinf(W):
        return 0.0
    return float(M) / W


def pi_star_traffic(
    taus: list[float] | tuple[float, ...],
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Largest Π with W_net ≤ W_max. Bisection; no closed form needed."""
    if W_max <= service_sum(taus):
        return 0.0
    lo, hi = 0.0, 0.999999
    if traffic_sojourn(taus, hi, kappa) <= W_max:
        return hi
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if traffic_sojourn(taus, mid, kappa) <= W_max:
            lo = mid
        else:
            hi = mid
    return lo


def shed_star(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    return max(0.0, float(Pi) - pi_star_traffic(taus, W_max, kappa))


def cut_star_ms(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """
    Milliseconds to cut from the current bottleneck, λ held, so the
    mean SLA holds. The general per-node formula keeps working if the
    cut moves the bottleneck. 0 if already under. inf if impossible.
    """
    if traffic_sojourn(taus, Pi, kappa) <= float(W_max):
        return 0.0
    lam = arrival_rate(Pi, taus)
    idx = max(range(len(taus)), key=lambda i: taus[i])
    tau_b = float(taus[idx])

    def wait_with_cut(cut_s: float) -> float:
        total = 0.0
        for i, t in enumerate(taus):
            tt = tau_b - cut_s if i == idx else float(t)
            rho = lam * tt
            if rho >= 1.0:
                return math.inf
            total += tt * (1.0 + float(kappa) * rho / (1.0 - rho))
        return total

    hi = tau_b - 1e-9
    if wait_with_cut(hi) > float(W_max):
        return math.inf
    lo = 0.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if wait_with_cut(mid) > float(W_max):
            lo = mid
        else:
            hi = mid
    return hi * 1000.0


def sojourn_rates_traffic(
    taus: list[float] | tuple[float, ...], Pi: float
) -> tuple[float, ...]:
    """Node ℓ sojourn ~ Exp(1/τ_ℓ − λ) in the M/M/1 tandem (Burke/Reich)."""
    lam = arrival_rate(Pi, taus)
    return tuple(1.0 / float(t) - lam for t in taus)


def miss_probability(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> float | None:
    """P(W_net > W_max). Exact for κ = 1; withheld otherwise."""
    if kappa != 1.0:
        return None
    rates = sojourn_rates_traffic(taus, Pi)
    if any(r <= 0.0 for r in rates):
        return 1.0
    try:
        return hypoexp_survival(rates, float(W_max))
    except ValueError:
        return None


def pi_star_percentile_traffic(
    taus: list[float] | tuple[float, ...],
    W_max: float,
    alpha: float,
) -> float:
    """Largest Π with miss probability ≤ α. κ = 1 only."""
    if alpha <= 0.0:
        return 0.0
    p0 = miss_probability(taus, 0.0, W_max)
    if p0 is None or p0 > alpha:
        return 0.0
    lo, hi = 0.0, 0.999
    for _ in range(48):
        mid = 0.5 * (lo + hi)
        p = miss_probability(taus, mid, W_max)
        if p is None or p > alpha:
            hi = mid
        else:
            lo = mid
    return lo


def traffic_action(
    M: float,
    Pi: float,
    nu_star: float,
    u: float,
    taus: list[float] | tuple[float, ...],
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> str:
    if Pi < 1.0 and traffic_sojourn(taus, Pi, kappa) > float(W_max):
        return "shed_load"
    return ops_action(M, Pi, nu_star, u)


def traffic_card(
    M: float,
    Pi: float,
    taus: list[float] | tuple[float, ...],
    u: float = 0.84,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
    alpha: float | None = None,
) -> dict[str, float | bool | str | None]:
    T = service_sum(taus)
    tau_star = max(taus)
    nu = 1.0 / tau_star
    W_net = traffic_sojourn(taus, Pi, kappa)
    W_upper = tandem_sojourn(taus, Pi, kappa)
    star = pi_star_traffic(taus, W_max, kappa)
    shed = shed_star(taus, Pi, W_max, kappa)
    cut_ms = cut_star_ms(taus, Pi, W_max, kappa)
    slack = bottleneck_slack(taus)
    out: dict[str, float | bool | str | None] = {
        "T": T,
        "tau_star": tau_star,
        "kappa": kappa,
        "W_net": W_net,
        "W_net_upper": W_upper,
        "Lambda_W_net": traffic_lambda_W(M, taus, Pi, kappa),
        "W_max": W_max,
        "Pi_star": star,
        "shed_needed": shed,
        "cut_T_ms": cut_ms,
        "over_sla": W_net > float(W_max),
        "p_over_sla": miss_probability(taus, Pi, W_max, kappa),
        "serial_fraction": serial_fraction(taus),
        "fits_bottleneck": bool(
            math.isfinite(cut_ms) and cut_ms / 1000.0 <= slack + 1e-12
        ),
        "Lambda_job_cap": M * star * nu,
        "network_action": traffic_action(M, Pi, nu, u, taus, W_max, kappa),
    }
    if alpha is not None and kappa == 1.0:
        out["Pi_star_pct"] = pi_star_percentile_traffic(taus, W_max, alpha)
        out["alpha"] = float(alpha)
    return out


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}

    def near(a: float, b: float, tol: float = 1e-9) -> bool:
        return abs(a - b) <= tol

    lam = arrival_rate(WORK_PI, WORK_TAUS)
    results["lambda_stream"] = near(lam, WORK_PI / WORK_TAU)
    rho = utilizations(WORK_TAUS, WORK_PI)
    results["bottleneck_rho_is_Pi"] = near(rho[0], WORK_PI)
    results["others_cooler"] = all(r < WORK_PI for r in rho[1:])

    W = traffic_sojourn(WORK_TAUS, WORK_PI, 1.0)
    manual = sum(t / (1.0 - lam * t) for t in WORK_TAUS)
    results["sojourn_formula"] = near(W, manual)
    W_upper = tandem_sojourn(WORK_TAUS, WORK_PI, 1.0)
    results["allhot_is_upper_bound"] = W < W_upper
    results["overstatement_working"] = 1.22 < W_upper / W < 1.24

    results["single_node_agrees"] = near(
        traffic_sojourn((WORK_TAU,), WORK_PI, 1.0), WORK_TAU / (1.0 - WORK_PI)
    )
    results["deterministic_is_T"] = near(
        traffic_sojourn(WORK_TAUS, WORK_PI, 0.0), service_sum(WORK_TAUS)
    )
    results["unstable_inf"] = math.isinf(traffic_sojourn(WORK_TAUS, 1.0, 1.0))

    # The corrected working point is UNDER the 400 ms mean SLA.
    results["working_under_sla"] = W < DEFAULT_W_MAX
    star = pi_star_traffic(WORK_TAUS, DEFAULT_W_MAX, 1.0)
    results["pi_star_hits_wall"] = near(
        traffic_sojourn(WORK_TAUS, star, 1.0), DEFAULT_W_MAX, 1e-6
    )
    results["cap_looser_than_allhot"] = star > 1.0 - service_sum(WORK_TAUS) / DEFAULT_W_MAX
    results["shed_zero_at_working"] = shed_star(WORK_TAUS, WORK_PI) == 0.0
    results["cut_zero_at_working"] = cut_star_ms(WORK_TAUS, WORK_PI) == 0.0

    # Hot window Π = 0.60 is over the SLA; both levers report amounts.
    results["hot_over_sla"] = traffic_sojourn(WORK_TAUS, 0.60, 1.0) > DEFAULT_W_MAX
    results["hot_shed_positive"] = shed_star(WORK_TAUS, 0.60) > 0.0
    hot_cut = cut_star_ms(WORK_TAUS, 0.60)
    results["hot_cut_positive"] = 0.0 < hot_cut < 120.0
    results["hot_levers_agree"] = near(
        traffic_sojourn(WORK_TAUS, 0.60 - shed_star(WORK_TAUS, 0.60), 1.0),
        DEFAULT_W_MAX,
        1e-6,
    )

    p = miss_probability(WORK_TAUS, WORK_PI)
    results["tail_survives_correction"] = p is not None and 0.28 < p < 0.32
    p_idle = miss_probability(WORK_TAUS, 0.0)
    results["idle_tail_lower"] = p_idle is not None and p_idle < p
    results["pct_cap_still_tiny"] = (
        pi_star_percentile_traffic(WORK_TAUS, DEFAULT_W_MAX, 0.10) < 0.05
    )
    results["withheld_if_bursty"] = miss_probability(WORK_TAUS, WORK_PI, kappa=2.0) is None

    results["working_action_is_ops"] = (
        traffic_action(WORK_M, WORK_PI, 1.0 / WORK_TAU, 0.84, WORK_TAUS)
        == ops_action(WORK_M, WORK_PI, 1.0 / WORK_TAU, 0.84)
    )
    results["hot_action_sheds"] = (
        traffic_action(WORK_M, 0.60, 1.0 / WORK_TAU, 0.84, WORK_TAUS) == "shed_load"
    )
    return results


def render_working_point() -> str:
    card = traffic_card(WORK_M, WORK_PI, WORK_TAUS, alpha=0.10)
    lines = ["working_point  single-stream traffic equations"]
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
    print("traffic_checks_passed", len(suite))
    print()
    print(render_working_point())
