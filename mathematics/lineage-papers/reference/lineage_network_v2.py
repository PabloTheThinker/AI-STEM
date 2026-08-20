"""
Tandem sojourn, Kingman variability, QoS utilization cap.

Companion to LINEAGE_TANDEM_KINGMAN_QOS.md.
Does not change official v2.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math

try:
    from lineage_control_v2 import lambda_W, ops_action
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_TAU
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_control_v2 import lambda_W, ops_action
    from lineage_core_v2 import WORK_M, WORK_PI, WORK_TAU


WORK_TAUS = (0.120, 0.040, 0.030, 0.020, 0.015)
DEFAULT_W_MAX = 0.400  # seconds; hyperparameter, not a law
DEFAULT_KAPPA = 1.0  # (c_a² + c_s²)/2; 1 = M/M/1


def service_sum(taus: list[float] | tuple[float, ...]) -> float:
    if not taus or min(taus) <= 0.0:
        raise ValueError("latencies must be positive")
    return float(sum(taus))


def kingman_node_wait(tau: float, Pi: float, kappa: float = DEFAULT_KAPPA) -> float:
    """W ≈ τ + κ τ Π/(1−Π). κ=1 recovers M/M/1."""
    if tau <= 0.0:
        raise ValueError("τ must be > 0")
    if Pi >= 1.0:
        return math.inf
    if Pi < 0.0 or kappa < 0.0:
        raise ValueError("Π ≥ 0 and κ ≥ 0")
    return float(tau) * (1.0 + float(kappa) * float(Pi) / (1.0 - float(Pi)))


def tandem_sojourn(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Theorem 3: W_net = Σ W_ℓ."""
    return sum(kingman_node_wait(t, Pi, kappa) for t in taus)


def tandem_lambda_W(
    M: float,
    taus: list[float] | tuple[float, ...],
    Pi: float,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    W = tandem_sojourn(taus, Pi, kappa)
    if W <= 0.0 or math.isinf(W):
        return 0.0
    return float(M) / W


def pi_star(
    taus: list[float] | tuple[float, ...],
    W_max: float,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Maximum Π meeting W_net ≤ W_max. 0 if the SLA is tighter than T."""
    T = service_sum(taus)
    if W_max <= T:
        return 0.0
    if kappa == 1.0:
        return max(0.0, 1.0 - T / float(W_max))
    return max(0.0, (W_max - T) / (W_max - T + kappa * T))


def over_sla(
    taus: list[float] | tuple[float, ...],
    Pi: float,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> bool:
    return tandem_sojourn(taus, Pi, kappa) > float(W_max)


def network_action(
    M: float,
    Pi: float,
    nu_star: float,
    u: float,
    taus: list[float] | tuple[float, ...],
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> str:
    """QoS first, then the Λ_W controller."""
    if over_sla(taus, Pi, W_max, kappa) and Pi < 1.0:
        return "shed_load"
    return ops_action(M, Pi, nu_star, u)


def network_card(
    M: float,
    Pi: float,
    taus: list[float] | tuple[float, ...],
    u: float = 0.84,
    W_max: float = DEFAULT_W_MAX,
    kappa: float = DEFAULT_KAPPA,
) -> dict[str, float | bool | str]:
    T = service_sum(taus)
    tau_star = max(taus)
    W_star = tau_star / (1.0 - Pi) if Pi < 1.0 else math.inf
    W_net = tandem_sojourn(taus, Pi, kappa)
    nu = 1.0 / tau_star
    return {
        "T": T,
        "tau_star": tau_star,
        "T_over_tau": T / tau_star,
        "kappa": kappa,
        "W_star": W_star,
        "W_net": W_net,
        "Lambda_W": lambda_W(M, Pi, nu),
        "Lambda_W_net": tandem_lambda_W(M, taus, Pi, kappa),
        "W_max": W_max,
        "Pi_star": pi_star(taus, W_max, kappa),
        "over_sla": over_sla(taus, Pi, W_max, kappa),
        "network_action": network_action(M, Pi, nu, u, taus, W_max, kappa),
    }


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}

    def near(a: float, b: float, tol: float = 1e-9) -> bool:
        return abs(a - b) <= tol

    T = service_sum(WORK_TAUS)
    results["T_sum"] = near(T, 0.225)
    results["mm1_node"] = near(kingman_node_wait(0.120, WORK_PI, 1.0), 0.120 / (1.0 - WORK_PI))
    results["tandem_factor"] = near(tandem_sojourn(WORK_TAUS, WORK_PI, 1.0), T / (1.0 - WORK_PI))
    results["overestimate"] = near(
        tandem_sojourn(WORK_TAUS, WORK_PI, 1.0) / (WORK_TAU / (1.0 - WORK_PI)),
        T / WORK_TAU,
    )
    results["single_node_eq"] = near(
        tandem_sojourn((WORK_TAU,), WORK_PI, 1.0),
        WORK_TAU / (1.0 - WORK_PI),
    )

    # Deterministic κ=0: wait is just T (no queueing addend)
    results["deterministic"] = near(tandem_sojourn(WORK_TAUS, WORK_PI, 0.0), T)

    # Bursty κ=2 inflates the queueing part
    results["bursty_worse"] = tandem_sojourn(WORK_TAUS, WORK_PI, 2.0) > tandem_sojourn(
        WORK_TAUS, WORK_PI, 1.0
    )

    W_net = tandem_sojourn(WORK_TAUS, WORK_PI, 1.0)
    results["lambda_net"] = near(tandem_lambda_W(WORK_M, WORK_TAUS, WORK_PI), WORK_M / W_net)
    results["net_lt_single"] = tandem_lambda_W(WORK_M, WORK_TAUS, WORK_PI) < lambda_W(
        WORK_M, WORK_PI, 1.0 / WORK_TAU
    )

    star = pi_star(WORK_TAUS, DEFAULT_W_MAX, 1.0)
    results["pi_star"] = near(star, 1.0 - T / DEFAULT_W_MAX)
    results["working_over_sla"] = over_sla(WORK_TAUS, WORK_PI, DEFAULT_W_MAX, 1.0)
    results["low_pi_under_sla"] = not over_sla(WORK_TAUS, 0.20, DEFAULT_W_MAX, 1.0)
    results["impossible_sla"] = pi_star(WORK_TAUS, 0.100, 1.0) == 0.0
    results["qos_sheds"] = (
        network_action(WORK_M, WORK_PI, 1.0 / WORK_TAU, 0.84, WORK_TAUS) == "shed_load"
    )
    return results


def render_working_point() -> str:
    card = network_card(WORK_M, WORK_PI, WORK_TAUS)
    lines = ["working_point  tandem / Kingman / QoS"]
    for k, v in card.items():
        if isinstance(v, float):
            lines.append(f"{k:<16} {v:.6f}")
        else:
            lines.append(f"{k:<16} {v}")
    return "\n".join(lines)


if __name__ == "__main__":
    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("network_checks_passed", len(suite))
    print()
    print(render_working_point())
