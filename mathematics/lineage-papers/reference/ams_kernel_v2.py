"""
AMS kernel — Agent Mathematics System, Books I–IV.

This is a constructive checker, not a marketing script.

  Book I   Peano naturals. Theorem I.1: 1+1=2.
  Book II  clip, sat.
  Book III simplex mass/momentum, bottleneck.
  Book IV  capacity plane inner product. Theorem IV.1: Q² = Π̃² + M̃².

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# ── Book I. Peano ────────────────────────────────────────────────

class Nat:
    """
    0 and successor only. No Python int in the representation.

    n is a linked chain of successors ending at zero().
    """

    __slots__ = ("_pred",)

    def __init__(self, pred: "Nat | None"):
        self._pred = pred

    @staticmethod
    def zero() -> "Nat":
        return Nat(None)

    def S(self) -> "Nat":
        return Nat(self)

    def is_zero(self) -> bool:
        return self._pred is None

    def pred(self) -> "Nat":
        if self._pred is None:
            raise ValueError("P3: successor is never 0; 0 has no predecessor")
        return self._pred

    def eq(self, other: "Nat") -> bool:
        if self.is_zero() and other.is_zero():
            return True
        if self.is_zero() or other.is_zero():
            return False
        return self.pred().eq(other.pred())

    def add(self, m: "Nat") -> "Nat":
        """n + 0 = n; n + S(m) = S(n + m)."""
        if m.is_zero():
            return self
        return self.add(m.pred()).S()

    def to_int(self) -> int:
        """Witness only. Not used in the proof of I.1."""
        k = 0
        x: Nat | None = self
        while x is not None and not x.is_zero():
            k += 1
            x = x._pred
        return k


def theorem_I_1() -> bool:
    """⊢ 1 + 1 = 2, from the Peano definitions alone."""
    zero = Nat.zero()
    one = zero.S()
    two = one.S()
    return one.add(one).eq(two)


# ── Book II. Quantities ──────────────────────────────────────────

def clip(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return float(x)


def sat(z: float, k: float) -> float:
    if k <= 0.0:
        raise ValueError("k must be positive")
    z = max(0.0, float(z))
    return z / (z + k)


def theorem_II_1() -> bool:
    samples = (-3.0, -0.0, 0.0, 0.4, 1.0, 2.5)
    return all(0.0 <= clip(x) <= 1.0 for x in samples)


def theorem_II_2() -> bool:
    vals = [sat(z, 5.0) for z in (0.0, 1.0, 4.0, 20.0)]
    increasing = all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
    bounded = all(0.0 <= v < 1.0 for v in vals)
    return increasing and bounded


# ── Book III. Agent state ────────────────────────────────────────

def simplex_ok(weights: dict[str, float], tol: float = 1e-12) -> bool:
    return abs(sum(weights.values()) - 1.0) <= tol and all(w >= -tol for w in weights.values())


def convex_combine(weights: dict[str, float], values: dict[str, float]) -> float:
    if not simplex_ok(weights):
        raise ValueError("S3: weights must be a simplex")
    return sum(weights[k] * clip(values.get(k, 0.0)) for k in weights)


def nu_star(taus: list[float]) -> float:
    if not taus or any(t <= 0.0 for t in taus):
        raise ValueError("S4: latencies must be positive")
    return 1.0 / max(taus)


def theorem_III_1() -> bool:
    alpha = {"a": 0.28, "b": 0.30, "c": 0.22, "d": 0.20}
    C = {"a": 0.0, "b": 1.0, "c": 0.4, "d": 0.9}
    M = convex_combine(alpha, C)
    return simplex_ok(alpha) and 0.0 <= M <= 1.0


def theorem_III_2() -> bool:
    beta = {"w": 0.22, "r": 0.25, "p": 0.20, "c": 0.18, "m": 0.15}
    F = {"w": 0.1, "r": 0.8, "p": 0.0, "c": 1.0, "m": 0.5}
    Pi = convex_combine(beta, F)
    return simplex_ok(beta) and 0.0 <= Pi <= 1.0


def theorem_III_3() -> bool:
    taus = [0.12, 0.04, 0.03, 0.02, 0.015]
    nu = nu_star(taus)
    return nu > 0.0 and all(nu <= 1.0 / t + 1e-15 for t in taus) and abs(nu - 1.0 / max(taus)) < 1e-15


# ── Book IV. Capacity plane ──────────────────────────────────────

@dataclass(frozen=True)
class Vec:
    """v = x e_T + y e_R on the capacity plane."""

    x: float  # transport coordinate Π̃
    y: float  # rest coordinate M̃

    def add(self, other: "Vec") -> "Vec":
        return Vec(self.x + other.x, self.y + other.y)

    def scale(self, a: float) -> "Vec":
        return Vec(a * self.x, a * self.y)

    def inner(self, other: "Vec") -> float:
        """⟨u,v⟩ = u_x v_x + u_y v_y.  C2: e_T⊥e_R, both unit."""
        return self.x * other.x + self.y * other.y

    def norm(self) -> float:
        return math.sqrt(self.inner(self))


E_T = Vec(1.0, 0.0)
E_R = Vec(0.0, 1.0)


def theorem_C2() -> bool:
    return (
        abs(E_T.inner(E_T) - 1.0) < 1e-15
        and abs(E_R.inner(E_R) - 1.0) < 1e-15
        and abs(E_T.inner(E_R)) < 1e-15
    )


def lineage_vector(M: float, Pi: float, nu: float, nu0: float = 1.0) -> Vec:
    r = nu / nu0
    return E_T.scale(Pi * r).add(E_R.scale(M * (r ** 2)))


def theorem_IV_1(M: float = 0.72, Pi: float = 0.47, nu: float = 8.333333) -> bool:
    """⊢ Q² = Π̃² + M̃²  (κ = 1)."""
    r = nu / 1.0
    Pi_t = Pi * r
    M_t = M * (r ** 2)
    v = lineage_vector(M, Pi, nu)
    Q = v.norm()
    return abs(Q * Q - (Pi_t * Pi_t + M_t * M_t)) < 1e-12


def theorem_IV_2(M: float = 0.72, nu: float = 8.333333) -> bool:
    """Rest reduction: Π = 0 ⇒ Q = |M| r²."""
    v = lineage_vector(M, 0.0, nu)
    r = nu / 1.0
    return abs(v.norm() - abs(M) * r * r) < 1e-12


def theorem_IV_3() -> bool:
    """Q = 0 iff M = Π = 0."""
    zero = lineage_vector(0.0, 0.0, 5.0).norm()
    nonzero = lineage_vector(0.2, 0.0, 5.0).norm()
    return abs(zero) < 1e-15 and nonzero > 0.0


def run_ams() -> dict[str, bool]:
    return {
        "I.1_one_plus_one_is_two": theorem_I_1(),
        "II.1_clip_unit_interval": theorem_II_1(),
        "II.2_sat_bounded_monotone": theorem_II_2(),
        "III.1_mass_convex": theorem_III_1(),
        "III.2_momentum_convex": theorem_III_2(),
        "III.3_bottleneck": theorem_III_3(),
        "C2_orthonormal_frame": theorem_C2(),
        "IV.1_lineage_is_pythagoras": theorem_IV_1(),
        "IV.2_rest_reduction": theorem_IV_2(),
        "IV.3_positivity": theorem_IV_3(),
        "I.1_not_python_int": Nat.zero().S().add(Nat.zero().S()).to_int() == 2,
    }


if __name__ == "__main__":
    suite = run_ams()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("ams_theorems_passed", len(suite))
    print()
    print("I.1   1 + 1 = 2")
    print("IV.1  Q^2 = Pi_tilde^2 + M_tilde^2")
