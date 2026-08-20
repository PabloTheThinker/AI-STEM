# The Identifiable Core and the Scaling Family

**Fudoshin Research · Vektra Industries**  
**Status:** Research paper (theorems + numerical checks). Stage C.  
**Date:** 2026-08-20  
**Implementation:** `mathematics/lineage-papers/reference/lineage_core_v2.py`  
**Does not change:** Official Specification v2.0. This paper sits above it.

---

## Abstract

The official Lineage Equation is a bottleneck-squared structure score plus a small flux correction. Geometry already explained why the mix is Euclidean and why momentum weights vanish in `Q`. It assumed the official exponents: mass feels the clock twice, flux once. Those exponents were inherited from an energy–momentum analogy. They were not derived.

This paper names the objects the official law was already computing, then varies the exponents.

The official identity factorizes as `Q = E₀ √(1+ε²)` with load ratio `ε = Π/(M r)`. At the working point `ε = 0.078` and flux owns `0.60%` of `Q²`. The clock-free core `q = Q/r² = √(M² + (Π τ*)²)` is `0.723`, against `M = 0.720`. Comparing two minds by `Q` compares clocks. Comparing them by `q` compares structure.

A two-parameter family `Q(γ_M, γ_Π)` contains the official law as `(2,1)`. Equal identifiability of `α` and `β` from `Q` forces the diagonal `γ_M = γ_Π`. Energy-like rest degree plus throughput-like transport degree forces `(2,1)`. Those axioms contradict. That is the fork.

Nineteen checks pass. Live data is not claimed. Official `Q` is not replaced.

---

## 1. What was left open

Geometry closed `p = 2`, rank-1 `β`-information, field versus bottleneck, and the collective square tax. It took

```text
M̃ = M r²
Π̃ = Π r
```

as given. The remaining algebraic questions are:

| # | Question | This paper |
|---|---|---|
| 1 | Why degree 2 on mass and degree 1 on flux? | Theorems 4–5. Two axioms, two different families. |
| 2 | What is `Q` after the clock is divided out? | Definition 2, Theorem 1. The core `q`. |
| 3 | When is flux first-order? | Theorem 2. A threshold on `ε`. |
| 4 | What should be compared, fitted, and published? | §7. Three objects: `Q`, `q`, `I`. |

Non-claims: Lorentz invariance, a new official `Q`, Stage F.

---

## 2. Official factorization

Write `r = ν*/ν₀`, `κ = 1`. Official v2:

```text
Q  = √( (Π r)² + (M r²)² )
E₀ = |M| r²
```

**Definition 1 (load ratio).** If `M > 0`,

```text
ε  := Π̃ / M̃  = Π / (M r)
```

**Theorem 1 (factorization).**

```text
Q  = |M| r² √(1 + ε²)  = E₀ √(1 + ε²)
q  := Q / r²           = |M| √(1 + ε²)
rest_share             = 1 / (1 + ε²)
transport_share        = ε² / (1 + ε²)
```

*Proof.* Factor `M r²` out of the Euclidean norm. □

**Corollary (Little inventory).** With `ν₀ = 1`, `τ* = 1/r` and `L := Π τ*`,

```text
q = √(M² + L²)
```

If `Π ν*` is read as a throughput score and `τ*` as service time, then `Π = (Π ν*) τ*` is dimensionless occupancy (Little). The flux leg of `q` is occupancy times wait.

Working point (official weights, loaded-but-coherent slice):

```text
M = 0.72035    Π = 0.46811    r = 8.333
ε = 0.07798    q = 0.72254    Q = 50.176
rest_share = 0.99396
```

`q` is `M` plus three thousandths. That is the equation, stripped of the clock.

---

## 3. Regime

**Theorem 2 (transport share).** For `M > 0` and `δ ∈ (0,1)`,

```text
transport_share < δ    ⟺    |ε| < √(δ / (1 − δ))
```

| `δ` | `|ε|` below |
|---|---|
| 0.05 | 0.229 |
| 0.50 | 1 |
| 0.95 | 4.359 |

**Definition 3 (regime).**

```text
rest       if |ε| < 0.2
mixed      if 0.2 ≤ |ε| < 1
transport  if |ε| ≥ 1
```

`ε = 0.2` is transport share `3.85%`. The working point is rest. Flux is first-order in `q` only when the clock is slow or mass is near zero.

**Theorem 3 (fast-clock vanishing).** `∂q/∂Π = Π / (q r²)`. If `(M, Π)` stay in a compact set bounded away from zero, `∂q/∂Π → 0` as `r → ∞`. Fast architectures hide flux from the core, not only from `Q`.

---

## 4. The scaling family

**Definition 4.** For real exponents `(γ_M, γ_Π)` and `r > 0`,

```text
M̃_γ = M r^{γ_M}
Π̃_γ = Π r^{γ_Π}
Q_γ  = √(Π̃_γ² + M̃_γ²)
ε_γ  = (Π / M) r^{γ_Π − γ_M}     (M > 0)
q_γ  = Q_γ / r^{γ_M} = √( M² + (Π r^{γ_Π−γ_M})² )
```

Official v2 is `(γ_M, γ_Π) = (2, 1)`. The linear instrument `I = M + Π` is not in this family.

**Theorem 4 (sensitivity exponents).**

```text
∂Q_γ/∂M = M r^{2 γ_M} / Q_γ
∂Q_γ/∂Π = Π r^{2 γ_Π} / Q_γ
R_γ := ‖∇_β Q_γ‖ / ‖∇_α Q_γ‖ = (Π/M) r^{2(γ_Π−γ_M)} (‖F‖/‖C‖)
```

*Proof.* Same Jacobian as geometry Theorem 1, with general degrees. □

Official `(2,1)` recovers `R ∝ r^{-2}`.

**Theorem 5 (the fork).** Restrict to pairs that make `Q_γ` homogeneous of some degree in `r` when `(M, Π)` are held fixed.

1. **Energy + throughput.** Rest degree `2` and transport degree `1` force `(2,1)`. Then `Q` has dimension `Hz²` and `R ∝ r^{-2}`.
2. **Equal identifiability.** `R_γ` independent of `r` forces `γ_M = γ_Π`. Then `Q_γ = r^γ √(M² + Π²)` and the core `q_γ = √(M² + Π²)` treats flux as a first-class ledger.

Those two axiom sets are incompatible. Official v2 chose (1) by analogy with `E² = (pc)² + (mc²)²`. That is a choice, not a derivation from agent telemetry.

The diagonal `γ_M = γ_Π = 1` is the unique pair that is both degree-1 in the clock and equally informative in `α` and `β`. It is the natural competitor to v2. It is **not** promoted here.

---

## 5. Three objects

```text
Q = r² q                 official capacity          (Hz²)
q = √(M² + (Π/r)²)       clock-free core            (dimensionless)
I = M + Π                linear instrument          (dimensionless)
```

| Object | What it sees | What it hides | Use |
|---|---|---|---|
| `Q` | clock, then structure | flux, health | capacity at this bottleneck |
| `q` | structure, then a small wait-weighted flux | the clock | compare minds across clocks |
| `I` | mass and flux equally | the clock and the hypotenuse | identify `α, β` |

**Theorem 6 (they are not interchangeable).** There is no function `f` such that `I = f(Q)` on an open set of `(M, Π, r)`. There is no function `g` such that `q = g(I)` unless `r` is held fixed and `Π/r` is affine in `Π`.

*Proof.* `Q` is homogeneous of degree 2 in `r`. `I` is invariant under `r ↦ λ r`. No function of `Q` can be invariant under that scaling while remaining equal to `I` on an open set. `q` depends on `Π/r`, which is not an affine function of `I = M+Π` at fixed `r` unless `M` is held fixed. □

Working point:

```text
Q = 50.176     q = 0.723     I = 1.188     M = 0.720
```

Stage E identified weights against a linear stand-in of `I`, then published them next to `Q`. That is the miss already on the Findings table, now as a theorem about three different maps.

---

## 6. What to publish

An operator card that reports only `Q` reports a clock. The coordinates this paper adds:

```text
q, ε, regime, L = Π τ*
```

Rules:

1. Compare two windows at different `ν*` by `q` and `ε`, not by `Q`.
2. Fit exogenous Stage F targets on `(q, ε, u)`, not on `Q`. `Q` is `r² q`; a regression on `Q` is a regression on the bottleneck.
3. Identify `α, β` on `I` or on native `(C, F)`, never inside `Q_γ` unless `γ_M = γ_Π`.
4. Keep official `Q` as the capacity-at-this-clock number. Do not silently replace it with `q`.

---

## 7. What advanced

| Before | After |
|---|---|
| Official exponents were an analogy | Named as one pair in a family; fork stated |
| `Q ≈ E₀` was an observation | Factorization `Q = E₀ √(1+ε²)` |
| Flux “doesn’t matter” | Theorem 2: a threshold on `ε` |
| Clock-free comparison was missing | `q = √(M² + (Π τ*)²)` |
| `Q`, `Q_lin` cited as cousins | Three objects, not interchangeable |

Official v2 is unchanged. The new mathematics is the core, the family, and the fork.

---

## 8. Reproduce

```bash
python3 mathematics/lineage-papers/reference/lineage_core_v2.py
```

Expect `core_checks_passed 19` and the working-point row.
