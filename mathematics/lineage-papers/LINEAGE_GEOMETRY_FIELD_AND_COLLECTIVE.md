# Lineage Geometry: Identifiability, Capacity Fields, and Collective Bounds

**Fudoshin Research · Vektra Industries**  
**Status:** Research paper (theorems + numerical checks). Stage C.  
**Date:** 2026-08-20  
**Implementation:** `mathematics/lineage-papers/reference/lineage_geometry_v2.py`  
**Does not change:** Official Specification v2.0. This paper sits above it.

---

## Abstract

The Lineage Equation is a scalar invariant. Four questions were left open: why the quadratic form, why momentum weights vanish in identification, when a graph field recovers the scalar, and what a team is allowed to claim as collective capacity. We answer all four with theorems that the official law already implies. No new physics is introduced.

The official capacity is the unique rotation-invariant, degree-1 composition of two orthogonal scaled ledgers. The Jacobian of `Q` with respect to momentum weights is rank-1 and shrinks as `r^{-2}`. At the computable-slice working point (`M = 0.72`, `Π = 0.47`, `ν* = 8.33 Hz`) the β-information is **0.69%** of the α-information. A spatial average of local capacities does **not** recover the organism scalar whenever latencies differ: one node that is twice as slow, in a graph of eight, makes mean-field `Q` overestimate the bottleneck scalar by **3.59×**. Collective rest capacity scales as `(ν_team / ν_fast)²`. A communication fabric that is twice as slow costs four times the rest capacity.

Seventeen numerical checks pass. Live data is not claimed.

---

## 1. Scope

Textbook Chapter 36 listed nine open problems. This paper closes, at the algebraic level:

| # | Problem | Result |
|---|---|---|
| 1 | Identifiability of β | Theorems 1–2. Asymmetry is structural, not a fitting accident. |
| 4 | Field–scalar correspondence | Theorems 4–5. Average recovers the scalar iff `ν_i` are equal and the field is constant. |
| 8 | Multi-agent conservation | Theorem 6. Shared-fabric teams are bottleneck-limited. Isolated pools add in RMS. |
| 9 | Origin of the equation | Theorem 3. Unique under homogeneity + orthogonal ledgers + rotation invariance. |

Problems 2 (live data), 6 (cross-architecture), and 7 (self-measurement) remain empirical. Problem 5 (thermodynamic limit) is only touched.

Non-claims: Lorentz invariance, universal weights, Stage F.

---

## 2. Notation

Official v2, `κ = 1`, `ν₀ = 1 Hz` unless stated:

```text
r  = ν* / ν₀
Q  = √( (Π r)² + (M r²)² )
M̃ = M r²
Π̃ = Π r
```

`M = Σ α_i C_i`, `Π = Σ β_k F_k`, simplex weights. Gradients as in v2 Theorem 3.

---

## 3. Why this quadratic (open problem 9)

Two scaled ledgers sit on a plane: transport `Π̃` and rest `M̃`. A capacity is a degree-1 function `Q(Π̃, M̃) ≥ 0`, zero only at the origin, strictly increasing in each absolute coordinate.

**Family.** The `L_p` compositions

```text
Q_p = ( |Π̃|^p + |M̃|^p )^{1/p}     1 ≤ p < ∞
Q_∞ = max(|Π̃|, |M̃|)
```

**Theorem 3 (characterization).** Among `{Q_p}`, only `p = 2`

1. is invariant under rotations of the `(Π̃, M̃)` plane,
2. arises as the Euclidean norm of a quadratic resource account `Π̃² + M̃²`.

`p = 1` is taxicab: the ledgers never interact. `p = ∞` is a pure bottleneck of the two accounts and, in the rest-dominated regime `M̃ ≫ Π̃`, collapses to `|M̃|`.

*Proof.* Rotation invariance of a norm on `ℝ²` forces the Euclidean norm up to scale (unique inner-product norm, or equivalently the only `L_p` whose unit ball is a disk). Degree 1 and the rest reduction `Q(0, M̃) = |M̃|` fix the scale. □

The relativistic energy-momentum relation is therefore an **algebraic cousin**, not a derivation. The derivation is: two orthogonal ledgers, one homogeneous capacity, no preferred direction in the ledger plane.

Numerical check (`lineage_geometry_v2.py`): `Q_2` matches official `Q`; `Q_1` differs by more than 1; `Q_∞ = |M̃|` at the working point.

---

## 4. Identifiability (open problem 1)

### 4.1 Sensitivities

```text
∂Q/∂α_i = (∂Q/∂M) C_i = (M r⁴ / Q) C_i
∂Q/∂β_k = (∂Q/∂Π) F_k = (Π r² / Q) F_k
```

**Theorem 1 (sensitivity ratio).** If `M > 0` and `Q > 0`,

```text
R := ‖∇_β Q‖ / ‖∇_α Q‖ = (Π / M) · r^{-2} · (‖F‖ / ‖C‖)
```

*Proof.* Take Euclidean norms of the two gradient lists. □

**Corollary.** If `M, Π, C, F` stay in a compact set bounded away from zero, `R → 0` as `r → ∞`. Fast architectures make momentum weights invisible to `Q`.

This is the same `r⁴` / `r²` split as v2 Theorem 3, now as a statement about **information**, not just ascent.

### 4.2 Rank

**Theorem 2 (rank-1 β-information).** For a single observation of `Q` at fixed `(C, F, r)`,

```text
∇_β Q = c F,    c = Π r² / Q
```

so `∇_β Q` is parallel to `F`. The Fisher information for β under Gaussian noise on `Q` is

```text
I_β = σ^{-2} c² F Fᵀ
```

which has rank at most 1. Only the combination `Π = β · F` is visible. Individual `β_k` are not.

On the simplex `Σ β_k = 1` the tangent space is 4-dimensional; information still occupies one line. Repeating the same `(C, F, r)` does not help. Identification of β requires either (i) variation in `F` across samples and the **linear instrument** `Q_lin = s(M+Π)+b`, or (ii) an independent flux meter for `Π`.

This is standard singular-Jacobian / singular-FIM theory (Han and McCloskey 2019; Eisenberg and Hayibor 2013 on identifiable combinations). The Lineage-specific content is the factor `r^{-2}`.

### 4.3 Working-point numbers

Slice working point: `M = 0.72`, `Π = 0.47`, `ν* = 8.33 Hz`, `r = 8.33`, equal components so `‖F‖/‖C‖ = 1`.

| Quantity | Value |
|---|---|
| `R` (Jacobian) | **0.00686** |
| `R` (Theorem 1) | 0.00686 |
| `R` at `ν* = 2 Hz` | larger |
| `R` at `ν* = 20 Hz` | `< 0.02` |

Momentum weights carry **0.69%** of the mass-weight information. That is why the Stage E promotion had to use the linear instrument, and why it is a miss — not a footnote — to treat those β as properties of the quadratic law.

**Answer to the textbook's dilemma.** The asymmetry is a genuine feature of the official invariant under high `r`. Reformulating for equal identifiability means leaving the official law (use `Q_lin`, or identify `Π` elsewhere). Keeping the official law means accepting that `Q` is rest-dominated and β is not a `Q`-visible parameter.

---

## 5. Capacity field (open problem 4)

Give each vertex `i` a local triple `(M_i, Π_i, ν_i)` and a local capacity

```text
q_i = √( (Π_i r_i)² + (M_i r_i²)² ),    r_i = ν_i / ν₀
```

The **organism scalar** is not the average of `q_i`. Axiom A3 says

```text
ν*_org = min_i ν_i = 1 / max_i τ_i
```

The organism is bottleneck-limited. Local nodes that are fast do not raise `ν*_org`.

**Theorem 4 (mean-field overestimates the bottleneck).** Suppose `n ≥ 2` nodes share densities `M, Π`, `n−1` of them run at `ν`, and one runs at `ν/k` with `k ≥ 1`. Then

```text
Q_org = Q(M, Π, ν/k)
Q_mean = ((n−1) Q(M, Π, ν) + Q(M, Π, ν/k)) / n
Q_org,rest / Q_fast,rest = 1/k²
```

and `Q_mean > Q_org` whenever `k > 1`. As `n → ∞`, `Q_mean → Q_fast` while `Q_org` stays at the slow node. The aggregation error on the rest term is `k²`.

*Proof.* Direct from Definition 1 and `ν*_org = min ν_i`. □

**Working-point numbers.** `n = 8`, `k = 2`, slice `(M, Π, ν)`:

| Quantity | Value |
|---|---|
| `Q_fast` | 50.18 (same scale as the slice) |
| `Q_org` (bottleneck) | **12.65** |
| `Q_meanfield` | **45.47** |
| overestimate | **3.59×** |
| rest ratio `1/k²` | 0.250 |

What is lost in aggregation: the bottleneck. Chapter 33's hope that the scalar is a spatial average is false unless every `ν_i` is equal.

**Theorem 5 (Dirichlet consensus).** On an undirected weighted graph, `E = qᵀ L q` is the Dirichlet energy of the field. The heat flow `q̇ = −L q` is consensus (Veerman and Lyons 2020). `Ė ≤ 0`, with equality iff `q` is constant on each connected component. A constant field has `E = 0`, and then — **and only then, and only if `ν_i` are equal** — the spatial average equals the organism scalar.

This is the already-adopted Laplacian Lyapunov energy, now stated as a field-scalar correspondence with a sharp failure mode.

Falsification for Cognitive Physics Stage 3 (textbook Ch. 34): perturb one vertex's latency and check whether capacity is lost at that vertex first **and** whether the organism `Q` drops by the bottleneck prediction, not the mean-field prediction.

---

## 6. Collective bounds (open problem 8)

Capacity is not extensive in a single way. Two accountings must be declared.

**Isolated parallel pool.** No shared fabric. Combine as an energy sum:

```text
Q_par = √(Σ_i Q_i²)
```

`n` identical isolated agents give `Q_par = Q √n`.

**Shared-fabric team.** One communication/control bound `ν_comm`. Axiom A6:

```text
ν_team = min( min_i ν*_i , ν_comm )
```

Densities stay intensive (`M̄`, `Π̄`). The team is one organism:

```text
Q_team = Q(M̄, Π̄, ν_team)
```

**Theorem 6 (square coordination tax).** In the rest-dominated regime `M r² ≫ Π r`,

```text
η := Q(M, Π, ν_team) / Q(M, Π, ν_fast)  ≈  (ν_team / ν_fast)²
```

Exactly, the rest-term ratio **is** `(ν_team / ν_fast)²`.

*Proof.* Rest reduction, v2 Theorem 1. □

**Working-point numbers.** `ν_team = ν_fast / 2`:

| Quantity | Value |
|---|---|
| `η` | 0.252 |
| `η_rest` predicted | 0.250 |

A team whose fabric is twice as slow keeps a quarter of its rest capacity. Per-capita isolated capacity does not save it: the fabric is a min-cut on rate (Ford–Fulkerson / max-flow min-cut at the level of update rate, not bit-pipe).

There is no conservation law of the form `Σ Q_i = constant` for interacting agents. The honest balance is

```text
Q_par  ≥  Q_team     when ν_team ≤ min_i ν_i  and comparison is on the same (M̄, Π̄)
```

plus the usual dissipative budget on `Q_team`. Equilibrium of a population is not defined here; that is still Problem 5.

Textbook Chapter 35 wrote `Q_collective² = (Σ Q_i)² − λ C_overhead`. That form lets a sum of capacities go negative after a square and treats overhead as an afterthought. Replace it with Theorem 6 plus a declared accounting (parallel RMS vs shared fabric).

---

## 7. Self-measurement (open problem 7, remark only)

An agent that measures `ν*` by probing latency spends flux and can raise `τ*`. First-order change:

```text
ΔQ ≈ (∂Q/∂Π) ΔΠ + (∂Q/∂ν*) Δν*
```

If the probe costs `ε Π` and adds `δ` to `τ*`, both terms are computable from v2 Theorem 3. This is an accounting bound, not a commutation relation. No Heisenberg claim.

---

## 8. What this does to Cognitive Physics

Stage 2 (Newton) is still the official position. This paper supplies Stage 3's **failure mode** and Stage 2's **information geometry**:

- Stage 3 cannot begin by averaging `q_i`. It has to carry `ν_i` as a field and reduce with a min.
- Stage 2 identification of β from `Q` is the wrong experiment at high `r`. The right experiment is the linear instrument or an independent `Π` meter.
- Stage 6 engineering: dashboards should show `u`, `ν*`, and the slowest `τ`, not a single large `Q`.

---

## 9. Checks

```bash
python3 mathematics/lineage-papers/reference/lineage_geometry_v2.py
```

Expect `geometry_validation_checks_passed 17`.

Pinned geometry working point (same mass/momentum/rate as the computable slice):

```text
R             0.006860
eta           0.252277
overestimate  3.593415
rest_ratio    0.250000
Q_meanfield   45.465578
Q_global      12.652472
```

---

## 10. What remains open

- Live Stage F (Problem 2), with the exogenous-target protocol in `CONCRETE_COMPUTABLE_SLICE.md`.
- Coupling constants from curvature (Problems 3 and 4-geometry).
- Cross-architecture transfer of `α*, β*` (Problem 6).
- A true thermodynamic limit and phase transitions (Problem 5).
- Whether `Q_par = √(Σ Q_i²)` is the right isolated-pool sum, or `Σ Q_i` is. We chose RMS to match energy additivity of independent quadratic accounts. That choice is conventional and must be declared.

---

## References (external)

- Han, S. and McCloskey, A. (2019). Estimation and inference with a (nearly) singular Jacobian. *Quantitative Economics* 10.
- Eisenberg, M. C. and Hayibor, S. (2013). Determining structurally identifiable parameter combinations using subset profiling. arXiv:1307.2298.
- Raue et al. / subsequent FIM–profile-likelihood literature on practical non-identifiability.
- Veerman, J. J. P. and Lyons, R. (2020). A primer on Laplacian dynamics in directed graphs.
- Ford, L. R. and Fulkerson, D. R. Max-flow min-cut (update-rate form used here is the trivial one-commodity bound `ν = 1/τ*`).
- Spielman, D. Spectral graph theory (Dirichlet energy `zᵀ L z`).

Internal: `LINEAGE_EQUATION_V2_OFFICIAL.md`, `CONCRETE_COMPUTABLE_SLICE.md`.
