"""
Identifiable core and scaling family of the Lineage Equation.

Companion to LINEAGE_CORE_AND_SCALING_FAMILY.md.
Uses official v2 as the (2, 1) member of the family. Does not change the law.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math
from typing import Literal

try:
    from lineage_capacity_v2 import (
        CognitiveMassV2,
        CognitiveMomentumV2,
        LineageEquationV2,
        PropagationBoundV2,
    )
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_capacity_v2 import (
        CognitiveMassV2,
        CognitiveMomentumV2,
        LineageEquationV2,
        PropagationBoundV2,
    )


# Pinned loaded-but-coherent working point (official weights).
WORK_M = 0.720350
WORK_PI = 0.468108
WORK_R = 8.333333333333334
WORK_Q = 50.176171
WORK_TAU = 0.120

Regime = Literal["rest", "mixed", "transport"]
EPS_REST = 0.2
EPS_TRANSPORT = 1.0


def load_ratio(M: float, Pi: float, r: float, gamma_M: float = 2.0, gamma_Pi: float = 1.0) -> float:
    """ε_γ = (Π/M) r^{γ_Π − γ_M}. Official: Π/(M r)."""
    if M == 0.0:
        raise ValueError("load ratio requires M ≠ 0")
    return (Pi / M) * (r ** (gamma_Pi - gamma_M))


def family_Q(M: float, Pi: float, r: float, gamma_M: float = 2.0, gamma_Pi: float = 1.0) -> float:
    """Q_γ = √( (Π r^{γ_Π})² + (M r^{γ_M})² )."""
    m_t = M * (r ** gamma_M)
    p_t = Pi * (r ** gamma_Pi)
    return math.hypot(p_t, m_t)


def core_q(M: float, Pi: float, r: float, gamma_M: float = 2.0, gamma_Pi: float = 1.0) -> float:
    """q_γ = Q_γ / r^{γ_M} = √( M² + (Π r^{γ_Π−γ_M})² )."""
    if r <= 0.0:
        raise ValueError("r must be positive")
    return family_Q(M, Pi, r, gamma_M, gamma_Pi) / (r ** gamma_M)


def little_L(Pi: float, tau_star: float) -> float:
    """L = Π τ*. Official flux leg of q when ν₀ = 1."""
    return Pi * tau_star


def rest_energy(M: float, r: float, gamma_M: float = 2.0) -> float:
    return abs(M) * (r ** gamma_M)


def shares(eps: float) -> tuple[float, float]:
    """(rest_share, transport_share) = (1, ε²) / (1+ε²)."""
    d = 1.0 + eps * eps
    return 1.0 / d, (eps * eps) / d


def regime(eps: float) -> Regime:
    a = abs(eps)
    if a < EPS_REST:
        return "rest"
    if a < EPS_TRANSPORT:
        return "mixed"
    return "transport"


def transport_share_threshold(delta: float) -> float:
    """|ε| below which transport_share < δ. Theorem 2."""
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must be in (0, 1)")
    return math.sqrt(delta / (1.0 - delta))


def sensitivity_R(
    M: float,
    Pi: float,
    r: float,
    C_norm: float,
    F_norm: float,
    gamma_M: float = 2.0,
    gamma_Pi: float = 1.0,
) -> float:
    """Theorem 4: R_γ = (Π/M) r^{2(γ_Π−γ_M)} (‖F‖/‖C‖)."""
    if M <= 0.0 or C_norm <= 0.0:
        raise ValueError("M and ‖C‖ must be positive")
    return (Pi / M) * (r ** (2.0 * (gamma_Pi - gamma_M))) * (F_norm / C_norm)


def linear_instrument(M: float, Pi: float) -> float:
    return M + Pi


def official_from_slice() -> LineageEquationV2:
    mass = CognitiveMassV2(C_id=WORK_M, C_mem=WORK_M, C_graph=WORK_M, C_perm=WORK_M)
    mom = CognitiveMomentumV2(
        F_wm=WORK_PI, F_ret=WORK_PI, F_path=WORK_PI, F_ctrl=WORK_PI, F_merge=WORK_PI
    )
    tau = 1.0 / WORK_R
    return LineageEquationV2(
        mass=mass,
        momentum=mom,
        propagation=PropagationBoundV2(
            tau_retrieval_s=tau,
            tau_pathway_s=tau,
            tau_working_memory_s=tau,
            tau_sync_s=tau,
            tau_settling_s=tau,
        ),
    )


def core_card(M: float, Pi: float, r: float) -> dict[str, float | str]:
    """Official (2, 1) coordinates this paper adds."""
    eps = load_ratio(M, Pi, r)
    q = core_q(M, Pi, r)
    Q = family_Q(M, Pi, r)
    rest, tr = shares(eps)
    tau = 1.0 / r
    return {
        "M": M,
        "Pi": Pi,
        "r": r,
        "Q": Q,
        "q": q,
        "eps": eps,
        "E0": rest_energy(M, r),
        "L": little_L(Pi, tau),
        "I": linear_instrument(M, Pi),
        "rest_share": rest,
        "transport_share": tr,
        "regime": regime(eps),
    }


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}

    def near(a: float, b: float, tol: float = 1e-9) -> bool:
        return abs(a - b) <= tol

    # 1. Official family member matches the law module.
    eq = official_from_slice()
    results["family_matches_law"] = near(family_Q(WORK_M, WORK_PI, WORK_R), eq.total_capacity())

    # 2. Factorization Q = E0 √(1+ε²)
    eps = load_ratio(WORK_M, WORK_PI, WORK_R)
    e0 = rest_energy(WORK_M, WORK_R)
    Q = family_Q(WORK_M, WORK_PI, WORK_R)
    results["factorization"] = near(Q, e0 * math.sqrt(1.0 + eps * eps))

    # 3. Core q = Q / r²
    q = core_q(WORK_M, WORK_PI, WORK_R)
    results["core_is_Q_over_r2"] = near(q, Q / (WORK_R ** 2))

    # 4. Little form q = √(M² + L²)
    L = little_L(WORK_PI, WORK_TAU)
    results["little_form"] = near(q, math.hypot(WORK_M, L))

    # 5. Shares from ε
    rest, tr = shares(eps)
    results["shares_sum"] = near(rest + tr, 1.0)
    results["rest_share_from_eps"] = near(rest, 1.0 / (1.0 + eps * eps))

    # 6. Working-point numbers
    results["work_eps"] = near(eps, WORK_PI / (WORK_M * WORK_R), 1e-12)
    results["work_q_near_M"] = abs(q - WORK_M) < 0.01
    results["work_regime_rest"] = regime(eps) == "rest"
    results["work_Q"] = near(Q, WORK_Q, 5e-3)

    # 7. Theorem 2 threshold
    results["threshold_half"] = near(transport_share_threshold(0.5), 1.0)
    results["threshold_implies_share"] = tr < 0.05 and abs(eps) < transport_share_threshold(0.05)

    # 8. Equal-identifiability diagonal: R independent of r
    C_n, F_n = 1.0, 1.0
    r1, r2 = 4.0, 16.0
    R_diag_1 = sensitivity_R(WORK_M, WORK_PI, r1, C_n, F_n, 1.0, 1.0)
    R_diag_2 = sensitivity_R(WORK_M, WORK_PI, r2, C_n, F_n, 1.0, 1.0)
    results["diagonal_R_flat"] = near(R_diag_1, R_diag_2)
    R_off_1 = sensitivity_R(WORK_M, WORK_PI, r1, C_n, F_n, 2.0, 1.0)
    R_off_2 = sensitivity_R(WORK_M, WORK_PI, r2, C_n, F_n, 2.0, 1.0)
    results["official_R_shrinks"] = R_off_2 < R_off_1 / 10.0  # (16/4)^2 = 16, actually /16

    # 9. Official R matches geometry r^{-2}
    results["official_R_r2"] = near(
        R_off_1,
        (WORK_PI / WORK_M) * (r1 ** -2) * (F_n / C_n),
    )

    # 10. Three objects are numerically distinct at the working point
    I = linear_instrument(WORK_M, WORK_PI)
    results["three_objects_split"] = abs(Q - q) > 10.0 and abs(q - I) > 0.2 and abs(Q - I) > 10.0

    # 11. Fast-clock vanishing of ∂q/∂Π: finite difference shrinks
    def dq_dPi(r: float) -> float:
        h = 1e-6
        return (core_q(WORK_M, WORK_PI + h, r) - core_q(WORK_M, WORK_PI, r)) / h

    results["flux_sens_shrinks"] = abs(dq_dPi(20.0)) < abs(dq_dPi(5.0)) / 10.0

    # 12. I is invariant under r; Q is not
    results["I_clock_free"] = near(linear_instrument(WORK_M, WORK_PI), I)
    results["Q_clock_tied"] = family_Q(WORK_M, WORK_PI, 2 * WORK_R) > 3.0 * Q

    return results


def render_working_point() -> str:
    card = core_card(WORK_M, WORK_PI, WORK_R)
    lines = ["working_point  official (2, 1)"]
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
    print("core_checks_passed", len(suite))
    print()
    print(render_working_point())
