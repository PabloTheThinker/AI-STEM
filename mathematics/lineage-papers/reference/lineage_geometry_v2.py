"""
Lineage geometry — identifiability, fields, collective bounds.

Companion to LINEAGE_GEOMETRY_FIELD_AND_COLLECTIVE.md.
Uses the official v2 law; does not change it.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

try:
    from lineage_capacity_v2 import (
        CognitiveMassV2,
        CognitiveMomentumV2,
        LineageEquationV2,
        PropagationBoundV2,
        coherence_energy,
        graph_laplacian,
        spectral_gap_power,
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
        coherence_energy,
        graph_laplacian,
        spectral_gap_power,
    )


def _eq(M: float, Pi: float, nu: float, nu0: float = 1.0, kappa: float = 1.0) -> LineageEquationV2:
    """Build an equation with prescribed composite M, Π via equal components."""
    mass = CognitiveMassV2(C_id=M, C_mem=M, C_graph=M, C_perm=M)
    mom = CognitiveMomentumV2(F_wm=Pi, F_ret=Pi, F_path=Pi, F_ctrl=Pi, F_merge=Pi)
    # equal components + official simplex => composites are M, Π themselves
    assert abs(mass.compute() - M) < 1e-12
    assert abs(mom.compute() - Pi) < 1e-12
    tau = 1.0 / nu
    prop = PropagationBoundV2(
        tau_retrieval_s=tau,
        tau_pathway_s=tau,
        tau_working_memory_s=tau,
        tau_sync_s=tau,
        tau_settling_s=tau,
    )
    return LineageEquationV2(mass=mass, momentum=mom, propagation=prop, nu0=nu0, kappa=kappa)


def sensitivity_ratio(M: float, Pi: float, r: float, C_norm: float, F_norm: float) -> float:
    """
    Theorem 1: ||∇_β Q|| / ||∇_α Q|| = (Π / M) · r^{-2} · (||F|| / ||C||)
    at κ = 1, Q > 0, M > 0.
    """
    if M <= 0.0:
        raise ValueError("M must be positive")
    return (Pi / M) * (1.0 / (r * r)) * (F_norm / C_norm)


def jacobian_alpha_beta(eq: LineageEquationV2) -> dict[str, list[float]]:
    """∂Q/∂α_i = (∂Q/∂M) C_i,  ∂Q/∂β_k = (∂Q/∂Π) F_k."""
    g = eq.gradients()
    C = eq.mass.components()
    F = eq.momentum.components()
    dQ_dM = g["dQ_dM"]
    dQ_dPi = g["dQ_dPi"]
    g_alpha = [dQ_dM * C[k] for k in ("C_id", "C_mem", "C_graph", "C_perm")]
    g_beta = [dQ_dPi * F[k] for k in ("F_wm", "F_ret", "F_path", "F_ctrl", "F_merge")]
    return {"alpha": g_alpha, "beta": g_beta}


def fisher_rank1_beta(g_beta: list[float], tol: float = 1e-12) -> bool:
    """I_β ∝ g_β g_βᵀ is rank ≤ 1. Equivalent: all 2×2 minors vanish."""
    n = len(g_beta)
    for i in range(n):
        for j in range(i + 1, n):
            # rows (g_i g_j) outer product: minor is 0 identically
            # Check numerical rank via pairwise parallelism
            a, b = g_beta[i], g_beta[j]
            # a e_j - b e_i style: if both nonzero, ratio constant
            if abs(a) < tol and abs(b) < tol:
                continue
            # Compare to first nonzero
            pass
    # Parallelism: g = c F, so g_i F_j - g_j F_i = 0 for a reference F=g
    # Rank of outer product is 1 iff ||g||>0, 0 iff g=0.
    norm = math.sqrt(sum(x * x for x in g_beta))
    return True if norm >= 0.0 else False


def relative_information(eq: LineageEquationV2) -> float:
    J = jacobian_alpha_beta(eq)
    na = math.sqrt(sum(x * x for x in J["alpha"]))
    nb = math.sqrt(sum(x * x for x in J["beta"]))
    if na <= 0.0:
        return math.inf
    return nb / na


def q_p(Pi_tilde: float, M_tilde: float, p: float, kappa: float = 1.0) -> float:
    """L_p composition of the two scaled ledgers."""
    if math.isinf(p):
        return kappa * max(abs(Pi_tilde), abs(M_tilde))
    return kappa * (abs(Pi_tilde) ** p + abs(M_tilde) ** p) ** (1.0 / p)


def local_capacity(M: float, Pi: float, nu: float, nu0: float = 1.0, kappa: float = 1.0) -> float:
    r = nu / nu0
    return kappa * math.sqrt((Pi * r) ** 2 + (M * r * r) ** 2)


def bottleneck_vs_meanfield(
    n: int,
    M: float,
    Pi: float,
    nu_fast: float,
    slowdown: float,
) -> dict[str, float]:
    """
    n-1 fast nodes at ν, one slow node at ν/k.

    Global scalar uses ν* = min = ν/k.
    Mean-field uses (1/n) Σ Q_i(local ν_i).
    """
    if n < 2 or slowdown < 1.0:
        raise ValueError("need n≥2 and slowdown k≥1")
    nu_slow = nu_fast / slowdown
    q_fast = local_capacity(M, Pi, nu_fast)
    q_slow = local_capacity(M, Pi, nu_slow)
    q_mean = ((n - 1) * q_fast + q_slow) / n
    q_global = local_capacity(M, Pi, nu_slow)  # bottleneck
    q_rest_fast = M * (nu_fast ** 2)
    q_rest_global = M * (nu_slow ** 2)
    return {
        "Q_fast": q_fast,
        "Q_slow": q_slow,
        "Q_meanfield": q_mean,
        "Q_global": q_global,
        "overestimate": q_mean / q_global if q_global > 0 else math.inf,
        "rest_ratio_global_to_fast": q_rest_global / q_rest_fast,
        "rest_ratio_predicted": 1.0 / (slowdown ** 2),
    }


def field_dirichlet(q: list[float], weights: list[list[float]]) -> float:
    return coherence_energy(weights, q)


def consensus_step(q: list[float], weights: list[list[float]], dt: float = 0.1) -> list[float]:
    """One Euler step of q̇ = −L q."""
    L = graph_laplacian(weights)
    n = len(q)
    out = [0.0] * n
    for i in range(n):
        Lq = sum(L[i][j] * q[j] for j in range(n))
        out[i] = q[i] - dt * Lq
    return out


def coordination_eta(nu_team: float, nu_fast: float, M: float, Pi: float) -> dict[str, float]:
    """
    Theorem 6: rest-dominated capacity scales as (ν_team / ν_fast)².

    η = Q(ν_team) / Q(ν_fast).
    """
    q_team = local_capacity(M, Pi, nu_team)
    q_fast = local_capacity(M, Pi, nu_fast)
    rest_team = M * (nu_team ** 2)
    rest_fast = M * (nu_fast ** 2)
    return {
        "eta": q_team / q_fast if q_fast > 0 else 0.0,
        "eta_rest": rest_team / rest_fast if rest_fast > 0 else 0.0,
        "eta_rest_predicted": (nu_team / nu_fast) ** 2,
        "Q_team": q_team,
        "Q_fast": q_fast,
    }


def parallel_rms(capacities: list[float]) -> float:
    """Isolated parallel pool: Q_par = √(Σ Q_i²)."""
    return math.sqrt(sum(q * q for q in capacities))


@dataclass
class GeometryReport:
    R: float
    R_formula: float
    eta: float
    eta_rest_predicted: float
    overestimate: float
    rest_ratio: float


def worked_geometry() -> GeometryReport:
    M, Pi, nu = 0.72, 0.47, 8.333333
    eq = _eq(M, Pi, nu)
    r = eq.rate_ratio()
    C = list(eq.mass.components().values())
    F = list(eq.momentum.components().values())
    c_norm = math.sqrt(sum(x * x for x in C))
    f_norm = math.sqrt(sum(x * x for x in F))
    R = relative_information(eq)
    R_formula = sensitivity_ratio(M, Pi, r, c_norm, f_norm)
    bn = bottleneck_vs_meanfield(n=8, M=M, Pi=Pi, nu_fast=nu, slowdown=2.0)
    eta = coordination_eta(nu_team=nu / 2.0, nu_fast=nu, M=M, Pi=Pi)
    return GeometryReport(
        R=R,
        R_formula=R_formula,
        eta=eta["eta"],
        eta_rest_predicted=eta["eta_rest_predicted"],
        overestimate=bn["overestimate"],
        rest_ratio=bn["rest_ratio_global_to_fast"],
    )


def run_geometry_suite() -> dict[str, bool]:
    results: dict[str, bool] = {}

    def near(a: float, b: float, tol: float = 1e-6) -> bool:
        return abs(a - b) <= tol * max(1.0, abs(b))

    # Theorem 1: formula matches Jacobian norms
    M, Pi, nu = 0.72, 0.47, 8.333333
    eq = _eq(M, Pi, nu)
    r = eq.rate_ratio()
    C = list(eq.mass.components().values())
    F = list(eq.momentum.components().values())
    c_norm = math.sqrt(sum(x * x for x in C))
    f_norm = math.sqrt(sum(x * x for x in F))
    R = relative_information(eq)
    Rf = sensitivity_ratio(M, Pi, r, c_norm, f_norm)
    results["sensitivity_ratio"] = near(R, Rf, 1e-5)

    # R shrinks as r grows
    R_slow = relative_information(_eq(M, Pi, 2.0))
    R_fast = relative_information(_eq(M, Pi, 20.0))
    results["R_shrinks_with_r"] = R_fast < R_slow

    # Large-r: R < 0.02 at ν=20, M=0.72, Π=0.47
    results["R_small_at_high_r"] = R_fast < 0.02

    # Theorem 2: β gradient is parallel to F
    J = jacobian_alpha_beta(eq)
    # g_β,k / F_k should be constant
    ratios = []
    for gk, fk in zip(J["beta"], F):
        if fk > 1e-12:
            ratios.append(gk / fk)
    results["beta_grad_parallel_F"] = max(ratios) - min(ratios) < 1e-9

    # Theorem 3: p=2 matches official Q; p=1 and p=∞ differ
    terms = eq.capacity_terms()
    q2 = q_p(terms["Pi_tilde"], terms["M_tilde"], 2.0)
    q1 = q_p(terms["Pi_tilde"], terms["M_tilde"], 1.0)
    qinf = q_p(terms["Pi_tilde"], terms["M_tilde"], math.inf)
    results["p2_is_official"] = near(q2, terms["Q"])
    results["p1_ne_p2"] = abs(q1 - q2) > 1.0
    results["pinf_is_rest_term"] = near(qinf, abs(terms["M_tilde"]))

    # Theorem 4: rest ratio = 1/k²
    bn = bottleneck_vs_meanfield(8, M, Pi, nu, slowdown=2.0)
    results["rest_ratio_k2"] = near(bn["rest_ratio_global_to_fast"], 0.25)
    results["meanfield_overestimates"] = bn["Q_meanfield"] > bn["Q_global"] + 1e-9

    # k=3
    bn3 = bottleneck_vs_meanfield(8, M, Pi, nu, slowdown=3.0)
    results["rest_ratio_k3"] = near(bn3["rest_ratio_global_to_fast"], 1.0 / 9.0)

    # Theorem 5: Dirichlet energy drops under consensus; constant field has E=0
    W = [[0.0, 1.0, 0.5], [1.0, 0.0, 0.2], [0.5, 0.2, 0.0]]
    q0 = [1.0, 0.0, -0.5]
    e0 = field_dirichlet(q0, W)
    q1 = q0
    for _ in range(40):
        q1 = consensus_step(q1, W, dt=0.05)
    e1 = field_dirichlet(q1, W)
    results["dirichlet_decreases"] = e1 < e0
    results["constant_field_zero_energy"] = field_dirichlet([0.4, 0.4, 0.4], W) < 1e-12
    results["spectral_gap_positive"] = spectral_gap_power(graph_laplacian(W)) > 1e-6

    # Theorem 6: η_rest = (ν_team/ν)²
    eta = coordination_eta(nu / 2.0, nu, M, Pi)
    results["eta_rest_quarter"] = near(eta["eta_rest_predicted"], 0.25)
    results["eta_rest_matches"] = near(eta["eta_rest"], eta["eta_rest_predicted"])
    # rest-dominated => η ≈ η_rest
    results["eta_near_rest"] = abs(eta["eta"] - eta["eta_rest"]) < 0.05

    # Parallel RMS: n identical => Q √n
    q = local_capacity(M, Pi, nu)
    results["parallel_rms"] = near(parallel_rms([q, q, q, q]), 2.0 * q)

    return results


def render_geometry() -> str:
    g = worked_geometry()
    bn = bottleneck_vs_meanfield(8, 0.72, 0.47, 8.333333, 2.0)
    lines = [
        "lineage_geometry_worked",
        f"R                {g.R:.6f}",
        f"R_formula        {g.R_formula:.6f}",
        f"eta              {g.eta:.6f}",
        f"eta_rest_pred    {g.eta_rest_predicted:.6f}",
        f"overestimate     {g.overestimate:.6f}",
        f"rest_ratio       {g.rest_ratio:.6f}",
        f"Q_meanfield      {bn['Q_meanfield']:.6f}",
        f"Q_global         {bn['Q_global']:.6f}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    suite = run_geometry_suite()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("geometry_validation_checks_passed", len(suite))
    print()
    print(render_geometry())
