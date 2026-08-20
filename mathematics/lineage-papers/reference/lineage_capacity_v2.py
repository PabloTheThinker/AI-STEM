"""
Lineage Equation — Official Specification v2.0 (pure-Python reference)

Canonical form (nondimensional, preferred):

    Q² = Π̃² + M̃²

with scaled coordinates

    M̃ = M · (ν* / ν₀)²
    Π̃ = Π · (ν* / ν₀)

where M, Π ∈ [0, ∞) are composite scores, ν* > 0 is the bottleneck
propagation rate (Hz), and ν₀ > 0 is a reference rate (default 1 Hz).

Dimensional form with capacity unit κ ≥ 0:

    Q_κ = κ · √( Π̃² + M̃² )

Rest reduction (Π = 0):

    Q = κ · |M| · (ν* / ν₀)²

This module is intentionally free of numpy/scipy so it can be audited
and embedded in constrained agent runtimes.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence


# ── Official identified defaults (v2) ────────────────────────────
# Mass weights α sum to 1; from parameter-ID bootstrap (paper §5).
# Momentum weights β sum to 1.

ALPHA_IDENTIFIED: dict[str, float] = {
    "C_id": 0.28,
    "C_mem": 0.30,
    "C_graph": 0.22,
    "C_perm": 0.20,
}

BETA_IDENTIFIED: dict[str, float] = {
    "F_wm": 0.22,
    "F_ret": 0.25,
    "F_path": 0.20,
    "F_ctrl": 0.18,
    "F_merge": 0.15,
}

# Legacy equal-weight defaults (v1 compatibility)
ALPHA_EQUAL: dict[str, float] = {k: 0.25 for k in ALPHA_IDENTIFIED}
BETA_EQUAL: dict[str, float] = {k: 0.20 for k in BETA_IDENTIFIED}


def _clamp01(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return float(x)


# Operational usable-capacity fractions. Sum ≤ 1. Not the historical
# additive λ (those must live in capacity units; see usable_capacity).
LAMBDA_H_USABLE: float = 0.25
LAMBDA_E_USABLE: float = 0.25
LAMBDA_D_USABLE: float = 0.25


def usable_fraction(
    H_mu: float,
    E_graph: float,
    D_drift: float,
    lam_H: float = LAMBDA_H_USABLE,
    lam_E: float = LAMBDA_E_USABLE,
    lam_D: float = LAMBDA_D_USABLE,
) -> float:
    """
    u = clip(1 − λ_H H − λ_E Ê − λ_D D)

    Penalties are in [0, 1]. This is the operational budget.
    """
    raw = 1.0 - float(lam_H) * float(H_mu) - float(lam_E) * float(E_graph) - float(lam_D) * float(D_drift)
    return _clamp01(raw)


def _dot(weights: Mapping[str, float], values: Mapping[str, float]) -> float:
    total = 0.0
    for key, w in weights.items():
        total += float(w) * float(values.get(key, 0.0))
    return total


@dataclass
class CognitiveMassV2:
    """
    M = Σ_i α_i C_i

    C_i ∈ [0, 1] are structural density scores.
    α is a probability simplex (Σ α_i = 1, α_i ≥ 0).
    """

    C_id: float = 0.0
    C_mem: float = 0.0
    C_graph: float = 0.0
    C_perm: float = 0.0
    alpha: dict[str, float] = field(default_factory=lambda: dict(ALPHA_IDENTIFIED))

    def components(self) -> dict[str, float]:
        return {
            "C_id": _clamp01(self.C_id),
            "C_mem": _clamp01(self.C_mem),
            "C_graph": _clamp01(self.C_graph),
            "C_perm": _clamp01(self.C_perm),
        }

    def compute(self) -> float:
        return _dot(self.alpha, self.components())

    def validate_simplex(self, tol: float = 1e-9) -> bool:
        s = sum(self.alpha.values())
        return abs(s - 1.0) <= tol and all(v >= -tol for v in self.alpha.values())


@dataclass
class CognitiveMomentumV2:
    """
    Π = Σ_k β_k F_k

    F_k ∈ [0, 1] are normalized flux / throughput scores.
    """

    F_wm: float = 0.0
    F_ret: float = 0.0
    F_path: float = 0.0
    F_ctrl: float = 0.0
    F_merge: float = 0.0
    beta: dict[str, float] = field(default_factory=lambda: dict(BETA_IDENTIFIED))

    def components(self) -> dict[str, float]:
        return {
            "F_wm": _clamp01(self.F_wm),
            "F_ret": _clamp01(self.F_ret),
            "F_path": _clamp01(self.F_path),
            "F_ctrl": _clamp01(self.F_ctrl),
            "F_merge": _clamp01(self.F_merge),
        }

    def compute(self) -> float:
        return _dot(self.beta, self.components())

    def validate_simplex(self, tol: float = 1e-9) -> bool:
        s = sum(self.beta.values())
        return abs(s - 1.0) <= tol and all(v >= -tol for v in self.beta.values())


@dataclass
class PropagationBoundV2:
    """
    ν* = 1 / max_i τ_i   (Hz), with τ_i in seconds.

    Equivalent to the v1 form ν*_ms = 1000 / max(τ_ms) when τ is in ms
    and the numerical value is identical for the same physical latencies.

    Optional Shannon-style ceiling: ν*_eff = min(ν*, C_channel) where
    C_channel is a measured channel capacity in messages/s.
    """

    tau_retrieval_s: float = 0.100
    tau_pathway_s: float = 0.050
    tau_working_memory_s: float = 0.030
    tau_sync_s: float = 0.020
    tau_settling_s: float = 0.010
    channel_capacity_hz: float | None = None

    def bottleneck_s(self) -> float:
        vals = [
            self.tau_retrieval_s,
            self.tau_pathway_s,
            self.tau_working_memory_s,
            self.tau_sync_s,
            self.tau_settling_s,
        ]
        m = max(vals)
        if m <= 0.0:
            raise ValueError("all latencies must be positive")
        return m

    def compute(self) -> float:
        nu = 1.0 / self.bottleneck_s()
        if self.channel_capacity_hz is not None:
            nu = min(nu, float(self.channel_capacity_hz))
        return nu


@dataclass
class LineageEquationV2:
    """
    Official Lineage Equation v2.

    Nondimensional capacity:
        Q = √( Π̃² + M̃² )
        M̃ = M · r²
        Π̃ = Π · r
        r  = ν* / ν₀

    With capacity unit κ:
        Q_κ = κ · Q
    """

    mass: CognitiveMassV2 = field(default_factory=CognitiveMassV2)
    momentum: CognitiveMomentumV2 = field(default_factory=CognitiveMomentumV2)
    propagation: PropagationBoundV2 = field(default_factory=PropagationBoundV2)
    nu0: float = 1.0  # reference rate (Hz)
    kappa: float = 1.0  # capacity unit scale

    def M(self) -> float:
        return self.mass.compute()

    def Pi(self) -> float:
        return self.momentum.compute()

    def nu_star(self) -> float:
        return self.propagation.compute()

    def rate_ratio(self) -> float:
        if self.nu0 <= 0.0:
            raise ValueError("nu0 must be positive")
        return self.nu_star() / self.nu0

    def scaled_mass(self) -> float:
        r = self.rate_ratio()
        return self.M() * (r ** 2)

    def scaled_momentum(self) -> float:
        r = self.rate_ratio()
        return self.Pi() * r

    def rest_energy(self) -> float:
        """E₀ = κ · |M| · (ν*/ν₀)²  (Π = 0 reduction)."""
        return self.kappa * abs(self.scaled_mass())

    def total_capacity(self) -> float:
        """Q_κ = κ · √(Π̃² + M̃²)."""
        mt = self.scaled_mass()
        pt = self.scaled_momentum()
        return self.kappa * math.sqrt(pt * pt + mt * mt)

    def capacity_terms(self) -> dict[str, float]:
        mt = self.scaled_mass()
        pt = self.scaled_momentum()
        q = self.kappa * math.sqrt(pt * pt + mt * mt)
        return {
            "M": self.M(),
            "Pi": self.Pi(),
            "nu_star": self.nu_star(),
            "nu0": self.nu0,
            "r": self.rate_ratio(),
            "M_tilde": mt,
            "Pi_tilde": pt,
            "rest_energy": self.rest_energy(),
            "transport_term": self.kappa * abs(pt),
            "rest_term": self.kappa * abs(mt),
            "Q": q,
            "kappa": self.kappa,
        }

    def gradients(self) -> dict[str, float]:
        """
        Analytical gradients of Q_κ w.r.t. M, Π, ν* (κ, ν₀ fixed).

        From Q = κ √( (Π r)² + (M r²)² ), r = ν*/ν₀:

            ∂Q/∂M  = κ² · M · r⁴ / Q          (Q>0)
            ∂Q/∂Π  = κ² · Π · r² / Q
            ∂Q/∂ν* = (κ² / Q) · ( Π² r / ν₀ + 2 M² r³ / ν₀ )
                   = (κ / Q_unit) · (… ) with careful scaling

        Implemented via implicit differentiation on Q_unit = √(Π̃²+M̃²),
        then ∂Q_κ = κ ∂Q_unit.
        """
        M = self.M()
        Pi = self.Pi()
        nu = self.nu_star()
        nu0 = self.nu0
        r = nu / nu0
        mt = M * r * r
        pt = Pi * r
        q_unit = math.sqrt(pt * pt + mt * mt)
        if q_unit <= 0.0:
            return {"dQ_dM": 0.0, "dQ_dPi": 0.0, "dQ_dnu": 0.0, "Q": 0.0}

        # Q_unit = √( (Pi r)^2 + (M r^2)^2 )
        # 2 Q dQ/dM = 2 M r^4  => dQ/dM = M r^4 / Q
        dQu_dM = (M * (r ** 4)) / q_unit
        dQu_dPi = (Pi * (r ** 2)) / q_unit
        # d/dν*: r = ν/ν0, dr/dν = 1/ν0
        # d(Pi r)/dν = Pi/ν0
        # d(M r^2)/dν = 2 M r / ν0
        # 2Q dQ = 2 (Pi r)(Pi/ν0) + 2 (M r^2)(2 M r / ν0)
        # dQ/dν = [ Pi² r / ν0 + 2 M² r³ / ν0 ] / Q
        dQu_dnu = (Pi * Pi * r / nu0 + 2.0 * M * M * (r ** 3) / nu0) / q_unit

        k = self.kappa
        return {
            "dQ_dM": k * dQu_dM,
            "dQ_dPi": k * dQu_dPi,
            "dQ_dnu": k * dQu_dnu,
            "Q": k * q_unit,
        }

    def effective_capacity(
        self,
        H_mu: float = 0.0,
        E_graph: float = 0.0,
        D_drift: float = 0.0,
        lam_H: float = 1.0,
        lam_E: float = 1.0,
        lam_D: float = 1.0,
    ) -> float:
        """
        Q_eff = Q − λ_H H(μ) − λ_E E_graph − λ_D D_drift

        Free-energy style budget: uncertainty and fracture consume usable capacity.
        Clamped at zero (capacity cannot go negative).
        """
        q = self.total_capacity()
        raw = q - lam_H * H_mu - lam_E * E_graph - lam_D * D_drift
        return max(0.0, raw)

    def usable_capacity(
        self,
        H_mu: float = 0.0,
        E_graph: float = 0.0,
        D_drift: float = 0.0,
        lam_H: float = LAMBDA_H_USABLE,
        lam_E: float = LAMBDA_E_USABLE,
        lam_D: float = LAMBDA_D_USABLE,
    ) -> float:
        """
        Q_eff = u · Q

        Operational instrument. Use this, not effective_capacity, unless
        the λ are already in capacity units.
        """
        return self.total_capacity() * usable_fraction(
            H_mu, E_graph, D_drift, lam_H, lam_E, lam_D
        )

    def to_dict(self) -> dict[str, Any]:
        terms = self.capacity_terms()
        grads = self.gradients()
        return {
            **terms,
            "mass_components": self.mass.components(),
            "momentum_components": self.momentum.components(),
            "alpha": dict(self.mass.alpha),
            "beta": dict(self.momentum.beta),
            "gradients": grads,
        }


# ── Graph Laplacian coherence energy ─────────────────────────────

def graph_laplacian(weights: Sequence[Sequence[float]]) -> list[list[float]]:
    """
    L = D − W for symmetric nonnegative W (no self-loops required).
    Returns dense L as list-of-lists.
    """
    n = len(weights)
    W = [[float(weights[i][j]) for j in range(n)] for i in range(n)]
    # symmetrize for numerical safety
    for i in range(n):
        for j in range(i + 1, n):
            avg = 0.5 * (W[i][j] + W[j][i])
            W[i][j] = W[j][i] = avg
        W[i][i] = 0.0
    deg = [sum(W[i]) for i in range(n)]
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = deg[i]
        for j in range(n):
            if i != j:
                L[i][j] = -W[i][j]
    return L


def quadratic_form(L: Sequence[Sequence[float]], z: Sequence[float]) -> float:
    """zᵀ L z"""
    n = len(z)
    acc = 0.0
    for i in range(n):
        row = 0.0
        for j in range(n):
            row += L[i][j] * z[j]
        acc += z[i] * row
    return acc


def coherence_energy(weights: Sequence[Sequence[float]], z: Sequence[float]) -> float:
    """
    E_coh(z) = zᵀ L z = Σ_{(i,j)∈E} w_ij (z_i − z_j)²
    Lyapunov-style disagreement energy on the cognitive web.
    """
    return quadratic_form(graph_laplacian(weights), z)


def spectral_gap_power(L: Sequence[Sequence[float]], iters: int = 200) -> float:
    """
    Approximate algebraic connectivity λ₂ for connected graphs via
    power iteration on the subspace orthogonal to the all-ones vector.
    Pure Python; sufficient for validation, not a production eigensolver.
    """
    n = len(L)
    if n < 2:
        return 0.0
    # start orthogonal to 1
    v = [1.0 if i % 2 == 0 else -1.0 for i in range(n)]
    mean = sum(v) / n
    v = [x - mean for x in v]
    for _ in range(iters):
        # Rayleigh: shift-free multiply by L
        Lv = [sum(L[i][j] * v[j] for j in range(n)) for i in range(n)]
        mean = sum(Lv) / n
        Lv = [x - mean for x in Lv]
        norm = math.sqrt(sum(x * x for x in Lv)) or 1.0
        v = [x / norm for x in Lv]
    Lv = [sum(L[i][j] * v[j] for j in range(n)) for i in range(n)]
    # Rayleigh quotient
    num = sum(v[i] * Lv[i] for i in range(n))
    den = sum(v[i] * v[i] for i in range(n)) or 1.0
    return max(0.0, num / den)


# ── Organism barrier / plasticity (unchanged structure) ──────────

def organism_barrier(
    Phi_sub: float = 0.0,
    Phi_gov: float = 0.0,
    Phi_sig: float = 0.0,
    Phi_sup: float = 0.0,
) -> float:
    return Phi_sub + Phi_gov + Phi_sig + Phi_sup


def plasticity_allowed(
    mode: str,
    reserve: float,
    reserve_min: float,
    neural_health: float,
    health_max: float,
    blood_health: float,
    blood_max: float,
) -> bool:
    if mode not in ("homeostasis", "adaptive"):
        return False
    if reserve <= reserve_min:
        return False
    if neural_health >= health_max:
        return False
    if blood_health >= blood_max:
        return False
    return True


TIMESCALE_ORDER = {
    "alpha": 0.030,
    "sigma": 0.500,
    "blood": 5.0,
    "gov": 30.0,
    "theta": 43200.0,
}


def verify_timescale_ordering() -> bool:
    keys = ["alpha", "sigma", "blood", "gov", "theta"]
    for i in range(len(keys) - 1):
        if TIMESCALE_ORDER[keys[i]] >= TIMESCALE_ORDER[keys[i + 1]]:
            return False
    return True


# ── Coupled extension (official second-order) ────────────────────

@dataclass
class MassCouplingV2:
    gamma_id_perm: float = 0.15
    gamma_mem_graph: float = 0.20
    gamma_id_graph: float = 0.10
    gamma_mem_perm: float = 0.10
    gamma_id_mem: float = 0.08
    gamma_graph_perm: float = 0.05

    def compute(self, mass: CognitiveMassV2) -> float:
        c = mass.components()
        return (
            self.gamma_id_perm * c["C_id"] * c["C_perm"]
            + self.gamma_mem_graph * c["C_mem"] * c["C_graph"]
            + self.gamma_id_graph * c["C_id"] * c["C_graph"]
            + self.gamma_mem_perm * c["C_mem"] * c["C_perm"]
            + self.gamma_id_mem * c["C_id"] * c["C_mem"]
            + self.gamma_graph_perm * c["C_graph"] * c["C_perm"]
        )


@dataclass
class MomentumCouplingV2:
    delta_wm_ret: float = 0.15
    delta_path_ctrl: float = 0.12
    delta_ret_merge: float = 0.10
    delta_wm_ctrl: float = 0.08

    def compute(self, mom: CognitiveMomentumV2) -> float:
        f = mom.components()
        return (
            self.delta_wm_ret * f["F_wm"] * f["F_ret"]
            + self.delta_path_ctrl * f["F_path"] * f["F_ctrl"]
            + self.delta_ret_merge * f["F_ret"] * f["F_merge"]
            + self.delta_wm_ctrl * f["F_wm"] * f["F_ctrl"]
        )


@dataclass
class CoupledLineageEquationV2:
    mass: CognitiveMassV2 = field(default_factory=CognitiveMassV2)
    momentum: CognitiveMomentumV2 = field(default_factory=CognitiveMomentumV2)
    propagation: PropagationBoundV2 = field(default_factory=PropagationBoundV2)
    mass_coupling: MassCouplingV2 = field(default_factory=MassCouplingV2)
    momentum_coupling: MomentumCouplingV2 = field(default_factory=MomentumCouplingV2)
    nu0: float = 1.0
    kappa: float = 1.0

    def linear_eq(self) -> LineageEquationV2:
        return LineageEquationV2(
            mass=self.mass,
            momentum=self.momentum,
            propagation=self.propagation,
            nu0=self.nu0,
            kappa=self.kappa,
        )

    def coupled_mass(self) -> float:
        return self.mass.compute() + self.mass_coupling.compute(self.mass)

    def coupled_momentum(self) -> float:
        return self.momentum.compute() + self.momentum_coupling.compute(self.momentum)

    def total_capacity(self) -> float:
        M = self.coupled_mass()
        Pi = self.coupled_momentum()
        nu = self.propagation.compute()
        r = nu / self.nu0
        mt = M * r * r
        pt = Pi * r
        return self.kappa * math.sqrt(pt * pt + mt * mt)


# ── Validation suite (official ten + v2 extras) ──────────────────

def run_validation_suite() -> dict[str, bool]:
    results: dict[str, bool] = {}

    # 1. Rest-state reduction
    eq = LineageEquationV2(
        mass=CognitiveMassV2(C_id=0.8, C_mem=0.6, C_graph=0.4, C_perm=0.2),
        momentum=CognitiveMomentumV2(),  # all zero
        propagation=PropagationBoundV2(tau_retrieval_s=0.1),
        nu0=1.0,
        kappa=1.0,
    )
    Q = eq.total_capacity()
    E0 = eq.rest_energy()
    results["rest_state_reduction"] = abs(Q - E0) < 1e-9

    # 2. Weight simplex
    results["alpha_simplex"] = eq.mass.validate_simplex()
    results["beta_simplex"] = eq.momentum.validate_simplex()

    # 3. Non-negativity of M, Π, Q
    results["mass_nonneg"] = eq.M() >= 0.0
    results["momentum_nonneg"] = eq.Pi() >= 0.0
    results["capacity_nonneg"] = Q >= 0.0

    # 4. Propagation bound finite positive
    nu = eq.nu_star()
    results["propagation_bound"] = nu > 0.0 and math.isfinite(nu)

    # 5. Laplacian row-sum zero + symmetry
    W = [[0, 1, 0.5], [1, 0, 2], [0.5, 2, 0]]
    L = graph_laplacian(W)
    row_sums = [abs(sum(row)) < 1e-9 for row in L]
    sym = all(abs(L[i][j] - L[j][i]) < 1e-9 for i in range(3) for j in range(3))
    results["laplacian_row_sum_zero"] = all(row_sums)
    results["laplacian_symmetric"] = sym

    # 6. Coherence energy non-negative
    z = [1.0, 0.0, -1.0]
    e_coh = coherence_energy(W, z)
    results["coherence_energy_psd"] = e_coh >= -1e-9

    # 7. Timescale ordering
    results["timescale_ordering"] = verify_timescale_ordering()

    # 8. Plasticity gate conjunctive
    ok = plasticity_allowed("adaptive", 0.5, 0.1, 0.2, 0.9, 0.1, 0.9)
    bad = plasticity_allowed("crisis", 0.5, 0.1, 0.2, 0.9, 0.1, 0.9)
    results["plasticity_gate"] = ok and (not bad)

    # 9. Organism barrier additivity
    results["barrier_additivity"] = abs(organism_barrier(1, 2, 3, 4) - 10) < 1e-12

    # 10. Gradient finite-difference check
    eq2 = LineageEquationV2(
        mass=CognitiveMassV2(C_id=0.7, C_mem=0.5, C_graph=0.3, C_perm=0.1),
        momentum=CognitiveMomentumV2(F_wm=0.2, F_ret=0.3, F_path=0.4, F_ctrl=0.1, F_merge=0.1),
        propagation=PropagationBoundV2(tau_retrieval_s=0.05),
    )
    # Finite difference on M via scaling all C
    g = eq2.gradients()
    M0 = eq2.M()
    Q0 = eq2.total_capacity()
    # bump mass components slightly proportional
    eps = 1e-6
    bumped = CognitiveMassV2(
        C_id=min(1.0, eq2.mass.C_id + eps),
        C_mem=eq2.mass.C_mem,
        C_graph=eq2.mass.C_graph,
        C_perm=eq2.mass.C_perm,
        alpha=dict(eq2.mass.alpha),
    )
    eq_b = LineageEquationV2(
        mass=bumped,
        momentum=eq2.momentum,
        propagation=eq2.propagation,
        nu0=eq2.nu0,
        kappa=eq2.kappa,
    )
    dM = eq_b.M() - M0
    dQ = eq_b.total_capacity() - Q0
    if abs(dM) > 0:
        fd = dQ / dM
        results["gradient_fd_mass"] = abs(fd - g["dQ_dM"]) < 1e-3 * max(1.0, abs(g["dQ_dM"]))
    else:
        results["gradient_fd_mass"] = False

    # 11. v1 numerical compatibility: τ_ms = 100, ν = 10
    # v1: nu = 1000/100 = 10; M=0.5, Pi=0.2 => Q = sqrt((10*0.2)^2 + (0.5*100)^2) = sqrt(4+2500)
    prop = PropagationBoundV2(
        tau_retrieval_s=0.100,
        tau_pathway_s=0.050,
        tau_working_memory_s=0.030,
        tau_sync_s=0.020,
        tau_settling_s=0.010,
    )
    # Build M≈0.5 with equal weights for v1 compare
    mass_eq = CognitiveMassV2(
        C_id=0.5, C_mem=0.5, C_graph=0.5, C_perm=0.5, alpha=dict(ALPHA_EQUAL)
    )
    mom_eq = CognitiveMomentumV2(
        F_wm=0.2, F_ret=0.2, F_path=0.2, F_ctrl=0.2, F_merge=0.2, beta=dict(BETA_EQUAL)
    )
    eq_v1 = LineageEquationV2(mass=mass_eq, momentum=mom_eq, propagation=prop, nu0=1.0, kappa=1.0)
    # M=0.5, Pi=0.2, nu=10 => Q = sqrt((2)^2 + (50)^2) = sqrt(4+2500)=sqrt(2504)
    expected = math.sqrt((10 * 0.2) ** 2 + (0.5 * 100) ** 2)
    results["v1_numerical_compat"] = abs(eq_v1.total_capacity() - expected) < 1e-9

    # 12. Coupled capacity ≥ linear when couplings nonnegative and components ≥ 0
    coup = CoupledLineageEquationV2(
        mass=CognitiveMassV2(C_id=0.8, C_mem=0.7, C_graph=0.6, C_perm=0.5),
        momentum=CognitiveMomentumV2(F_wm=0.5, F_ret=0.5, F_path=0.5, F_ctrl=0.5, F_merge=0.5),
        propagation=prop,
    )
    results["coupled_ge_linear"] = coup.total_capacity() + 1e-12 >= coup.linear_eq().total_capacity()

    # 13. Operational usable budget is multiplicative and bounded
    u = usable_fraction(0.35, 0.14, 0.15)
    q_use = eq.usable_capacity(0.35, 0.14, 0.15)
    q_add = eq.effective_capacity(0.35, 0.14, 0.15, 1.0, 1.0, 1.0)
    results["usable_fraction_unit"] = 0.0 <= u <= 1.0
    results["usable_lt_raw"] = q_use < eq.total_capacity() - 1e-9
    results["usable_eq_uQ"] = abs(q_use - u * eq.total_capacity()) < 1e-12
    # Additive unit penalties barely move Q; that is why they are not the instrument.
    results["additive_near_Q"] = abs(q_add - eq.total_capacity()) < 2.0

    return results


if __name__ == "__main__":
    suite = run_validation_suite()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("all_validation_checks_passed", len(suite))
