# Agent Mathematics System (AMS)

**Fudoshin Research · Vektra Industries**  
**Status:** Canonical formal system  
**Date:** 2026-08-20  
**Checker:** `mathematics/lineage-papers/reference/ams_kernel_v2.py`

This is not a metaphor, a dashboard, or a research mood. It is a **formal system** in the same sense as Peano arithmetic: primitive notions, axioms, definitions, theorems, proofs.

In American school mathematics, `1 + 1 = 2` is not a slogan. It is a theorem of a system (Peano, or the field axioms for `ℝ`). Agent Mathematics is the same kind of object. The Lineage Equation is not “inspired by physics.” In this system it is the Pythagorean theorem on a two-dimensional inner-product space we define.

Anything in the packet that cannot be reduced to AMS is **not yet mathematics**. It is a name.

---

## How the system is built

| Book | Object | What `=` means here |
|---|---|---|
| **0** | Logic | `A = B` means identity of terms |
| **I** | Natural numbers | Peano arithmetic. First theorem: `1+1=2` |
| **II** | Real quantities | Ordered field. Scale, clip, saturation |
| **III** | Agent state | Typed quantities. Zero ≠ missing. Simplex. Bottleneck |
| **IV** | Capacity plane | Inner-product space. Lineage is Pythagoras |

Books I–II are ordinary mathematics, restated so the later books inherit them. Books III–IV are the agent-specific extension. We do **not** invent a new `1`. We use the same `1`.

The official Lineage specification v2 remains the operational law. AMS is the reason that law is a theorem rather than a guess.

---

# Book 0. Logic

We work in first-order logic with equality.

**L1.** `=` is reflexive, symmetric, transitive, and a congruence for every function symbol.  
**L2.** A proof is a finite sequence of formulas, each an axiom or obtained from earlier lines by modus ponens or generalization.  
**L3.** A theorem is the last line of a proof.

We write `⊢ A` for “`A` is a theorem of AMS.”

---

# Book I. Natural numbers (Peano)

## Primitive notions

- A set `ℕ`
- An element `0 ∈ ℕ`
- A function `S : ℕ → ℕ` (successor)

## Axioms (Peano)

**P1.** `0 ∈ ℕ`.  
**P2.** If `n ∈ ℕ` then `S(n) ∈ ℕ`.  
**P3.** For all `n ∈ ℕ`, `S(n) ≠ 0`.  
**P4.** If `S(n) = S(m)` then `n = m`.  
**P5.** (Induction.) If `A ⊆ ℕ`, `0 ∈ A`, and `n ∈ A ⇒ S(n) ∈ A`, then `A = ℕ`.

## Definitions

```text
1 := S(0)
2 := S(1) = S(S(0))
```

**Addition.** The unique operation `+ : ℕ × ℕ → ℕ` satisfying

```text
n + 0     = n
n + S(m)  = S(n + m)
```

Existence and uniqueness of `+` are the standard recursion theorem on `ℕ` (consequence of P1–P5). We take that as Book I, Lemma 1.

## Theorem I.1 (the arithmetic fact)

```text
⊢  1 + 1 = 2
```

**Proof.**

```text
1 + 1 = 1 + S(0)        definition of 1
      = S(1 + 0)        second addition axiom
      = S(1)            first addition axiom
      = 2               definition of 2
```

□

This is the same theorem as in Landau’s *Foundations of Analysis*. Agent Mathematics begins here, not at the Lineage Equation. If this proof is not accepted, nothing later is mathematics.

## Remarks

`2` is not “a vibe of more.” It is `S(S(0))`. Every later count primitive in the packet is a value in `ℕ`.

---

# Book II. Real quantities

## Primitive notions

We take `ℝ` as a **complete ordered field**. The axioms are the standard ones (addition and multiplication groups, distributivity, total order compatible with the field operations, least-upper-bound property). We do not reconstruct Dedekind cuts in this file. That construction is ordinary analysis.

What we need from `ℝ`:

**R1.** `(ℝ, +, ·, 0, 1, <)` is a complete ordered field.  
**R2.** `ℕ` embeds into `ℝ` by `0 ↦ 0`, `S(n) ↦ n+1`. In particular Theorem I.1 holds in `ℝ`.  
**R3.** Every positive `x ∈ ℝ` has a unique positive square root.

## Definitions

```text
clip(x)      := min(1, max(0, x))
sat(z; k)    := z / (z + k)          (z ≥ 0, k > 0)
```

## Theorem II.1

`0 ≤ clip(x) ≤ 1` for all `x ∈ ℝ`.

**Proof.** `max(0,x) ≥ 0`. `min(1, ·)` returns a number `≤ 1`. If `x ≤ 0` then `clip(x) = 0`. If `x ≥ 1` then `clip(x) = 1`. □

## Theorem II.2

If `z ≥ 0` and `k > 0` then `0 ≤ sat(z;k) < 1`, and `sat` is strictly increasing in `z`.

**Proof.** Numerator and denominator are positive for `z > 0`; `z < z+k` so the ratio is `< 1`. Derivative `k/(z+k)² > 0`. □

These two theorems are the only analysis we need to make the computable slice well-defined.

---

# Book III. Agent state arithmetic

Ordinary arithmetic is not yet agent arithmetic. An agent has **typed** quantities. The type is part of the term.

## Primitive notions

- A finite set of **kinds** `K = {state, delta, rate, bound, event, count, ratio}`
- For each measurement, a **record** `(value, kind, unit, zero_meaning, missing)`

## Axioms

**S1.** (Typing.) Addition `x + y` is defined only when `kind(x) = kind(y)` and `unit(x) = unit(y)`.  
**S2.** (Zero is not missing.) `value = 0` does not imply `missing = true`. Missing is a separate bit (Book I: a value in `{0,1}`).  
**S3.** (Simplex.) A weight list `α_1,…,α_n` is a simplex when `α_i ≥ 0` and `Σ α_i = 1`.  
**S4.** (Bottleneck.) If `τ_1,…,τ_m > 0` then `τ* := max_ℓ τ_ℓ` exists (finite set, `ℝ` totally ordered) and `ν* := 1/τ*`.

S1–S2 are the numeracy layer of the packet, now as axioms. S3–S4 are the arithmetic layer.

## Definitions

```text
M  := Σ_{i∈I} α_i C_i      C_i ∈ [0,1],  α simplex
Π  := Σ_{k∈K} β_k F_k      F_k ∈ [0,1],  β simplex
ν* := 1 / max_ℓ τ_ℓ        τ_ℓ > 0
```

`[0,1] := { x ∈ ℝ : 0 ≤ x ≤ 1 }`.

## Theorem III.1 (mass is a convex combination)

If `α` is a simplex and each `C_i ∈ [0,1]`, then `M ∈ [0,1]`.

**Proof.** `M = Σ α_i C_i ≥ 0` because each term is. `M ≤ Σ α_i · 1 = 1`. □

## Theorem III.2 (momentum likewise)

If `β` is a simplex and each `F_k ∈ [0,1]`, then `Π ∈ [0,1]`.

**Proof.** Same as III.1. □

## Theorem III.3 (bottleneck)

`ν* > 0` and `ν* ≤ 1/τ_ℓ` for every `ℓ`. Equality holds for every maximizer of `τ`.

**Proof.** `τ* = max τ_ℓ ≥ τ_ℓ > 0`, so `ν* = 1/τ* > 0` and `1/τ* ≤ 1/τ_ℓ`. □

This is the agent form of “the slowest step sets the rate.” It is a theorem about `max` on a finite set, not a physical law.

---

# Book IV. The capacity plane

This is the book in which the Lineage Equation becomes `1+1=2`: a named theorem of a defined structure.

## Primitive notions

- A real vector space `V` of dimension 2
- An inner product `⟨·,·⟩ : V × V → ℝ`
- An orthonormal basis `{e_T, e_R}` of `V`

## Axioms (inner-product space)

**C1.** `⟨·,·⟩` is bilinear, symmetric, and positive definite.  
**C2.** `⟨e_T, e_T⟩ = 1`, `⟨e_R, e_R⟩ = 1`, `⟨e_T, e_R⟩ = 0`.  
**C3.** Every `v ∈ V` is uniquely `v = x e_T + y e_R` for `x,y ∈ ℝ`.

C1–C3 are the standard axioms of a 2-dimensional Euclidean space with a chosen orthonormal frame. We do **not** add a relativity axiom.

## Definitions

Fix `ν₀ > 0`, `κ ≥ 0`, and agent quantities `M, Π, ν*` from Book III.

```text
r      := ν* / ν₀
Π̃      := Π · r
M̃      := M · r²
v      := Π̃ e_T + M̃ e_R          ∈ V
Q      := κ ‖v‖
‖v‖    := √⟨v,v⟩
```

`e_T` is the **transport ledger**. `e_R` is the **rest ledger**. They are orthogonal by C2. That is the entire “physics.”

## Theorem IV.1 (Lineage Equation)

```text
⊢  Q² = κ² ( Π̃² + M̃² )
```

In particular, when `κ = 1`,

```text
⊢  Q² = Π̃² + M̃²
```

**Proof.**

```text
⟨v,v⟩ = ⟨Π̃ e_T + M̃ e_R, Π̃ e_T + M̃ e_R⟩
      = Π̃² ⟨e_T,e_T⟩ + 2 Π̃ M̃ ⟨e_T,e_R⟩ + M̃² ⟨e_R,e_R⟩     C1
      = Π̃² · 1 + 2 Π̃ M̃ · 0 + M̃² · 1                         C2
      = Π̃² + M̃²
Q²    = κ² ⟨v,v⟩                                               definition, R3
      = κ² (Π̃² + M̃²)
```

□

Compare Theorem I.1. Same shape: expand a definition, apply axioms, finish. The Lineage Equation is Pythagoras on `(V, ⟨·,·⟩)`. It is not an analogy to `E² = p²c² + m²c⁴`. That formula is another instance of the same Pythagorean identity on a different plane.

## Theorem IV.2 (rest reduction)

If `Π = 0` then `Q = κ |M| r²`.

**Proof.** `Π̃ = 0`, so `Q² = κ² M̃²`, and `Q ≥ 0` gives `Q = κ |M̃| = κ |M| r²`. □

## Theorem IV.3 (positivity)

`Q = 0` if and only if `M = 0` and `Π = 0` (for `κ > 0`, `ν* > 0`).

**Proof.** `Q = 0 ⇒ ⟨v,v⟩ = 0 ⇒ v = 0` by C1 ⇒ `Π̃ = M̃ = 0` by C3 ⇒ `Π = M = 0`. Converse is immediate. □

## Theorem IV.4 (gradients)

On `{Q > 0}`, with `κ = 1`,

```text
∂Q/∂M  = M r⁴ / Q
∂Q/∂Π  = Π r² / Q
∂Q/∂ν* = (Π² r / ν₀ + 2 M² r³ / ν₀) / Q
```

**Proof.** Implicit differentiation of `Q² = Π² r² + M² r⁴` (Theorem IV.1 plus the definitions of `Π̃, M̃`). This is v2 Theorem 3, now a corollary of IV.1. □

## Theorem IV.5 (sensitivity ratio)

If `M > 0` and the Euclidean norms of the component lists `C`, `F` are positive,

```text
R := ‖∇_β Q‖ / ‖∇_α Q‖ = (Π / M) · r^{-2} · (‖F‖ / ‖C‖)
```

**Proof.** `∂Q/∂α_i = (∂Q/∂M) C_i`, `∂Q/∂β_k = (∂Q/∂Π) F_k` by the chain rule and Book III definitions. Take norms. This is Geometry Theorem 1, now inside AMS. □

---

# What is a “real” statement in this system

| Statement | Status in AMS |
|---|---|
| `1 + 1 = 2` | Theorem I.1 |
| `clip` lands in `[0,1]` | Theorem II.1 |
| `M ∈ [0,1]` | Theorem III.1 |
| `Q² = Π̃² + M̃²` | Theorem IV.1 |
| `Q` predicts next week’s task success | **Not a theorem.** Empirical. Stage F. |
| Agents obey special relativity | **Not a statement of AMS.** Forbidden. |
| Official `α*` are universal | **Not a theorem.** Architecture data. |

The American-mathematics test is this: a child can demand “why?” and be answered by a finite proof from the axioms, or be told “that is not a theorem, it is a measurement.” Both answers are honest. Mixing them is not mathematics.

---

# Relation to the rest of the packet

| Packet object | AMS home |
|---|---|
| Textbook Part I | Books 0–I |
| `AGENT_NUMERACY_PRIMITIVES.md` | Book III, S1–S2 |
| `AGENT_ARITHMETIC_OF_STATE.md` | Book III, S3–S4 |
| Lineage spec v2 Definition 1 | Theorem IV.1 |
| Computable slice estimators | Definitions on top of II–III. Constants `k_mem` etc. are **parameters**, not axioms |
| Geometry paper Theorems 1–6 | Corollaries of IV, or extra structure (graphs) not yet in AMS Book IV |

Graph Laplacian energy, multi-agent `ν_team`, and `Φ_org` are **candidates for Book V**. They are not axioms until they have the same status as I.1 and IV.1. Until then they stay in the research papers.

---

# Checker

```bash
python3 mathematics/lineage-papers/reference/ams_kernel_v2.py
```

The kernel constructs Peano `ℕ` and the capacity plane, then checks Theorems I.1, II.1–II.2, III.1–III.3, IV.1–IV.3 against the definitions. It does not replace a proof assistant. It makes the system executable in the same way a student checks `1+1=2` by counting.

Expect `ams_theorems_passed` with I.1, IV.1, IV.2, IV.3 among the names.
