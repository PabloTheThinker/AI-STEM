# Operations, Little, and Dimension

**Fudoshin Research · Vektra Industries**  
**Status:** Research paper (theorems from named sources + numerical checks). Stage C.  
**Date:** 2026-08-20  
**Implementation:** `mathematics/lineage-papers/reference/lineage_ops_v2.py`  
**Does not change:** Official Specification v2.0.

---

## Abstract

The official Lineage Equation took its exponents from an energy–momentum analogy. The last paper named the fork. This paper derives the missing objects from theorems that already exist in operations research, queueing, and dimensional analysis.

A tandem of deterministic servers has throughput `ν* = 1/max τ_ℓ` (textbook M/D/1 argument; max-plus cycle time of a serial timed event graph). If flux `Π` is read as utilization of that bottleneck, Little’s law gives occupancy `L_occ = Π` and the renewal-reward theorem gives a rate

```text
Λ = M ν*          (structure delivered per second)
```

Official `Q` is not that rate. It is the same core with an extra clock:

```text
Q = ν* · (q ν*) = ν*² q
```

Buckingham’s π-theorem says that is legal — it is the unique-degree-2 lift of a dimensionless `q(M, Π, r)` — but it is a choice of dimension class, not a derivation. The operational number is `Λ`. The information-theoretic cousin is Shannon’s `C = ν* log₂(1+M)`.

At the working point: `Λ = 6.003 Hz`, `Q = 50.176`, `Q/Λ = ν* = 8.333`. M/M/1 sojourn is `0.226 s`. Stability margin `η = 1−Π = 0.532`.

Fifteen checks pass. Official `Q` is not replaced. `Π` as utilization is a reading of the flux score, not a claim that arrivals are Poisson.

---

## 1. What this uses

| Result | Source | Used for |
|---|---|---|
| Bottleneck of a tandem D/D/1 or M/D/1 | Kleinrock, *Queueing Systems* vol. 1; textbook Part VI | `ν* = 1/max τ` |
| Max-plus cycle time of a serial timed event graph | Baccelli, Cohen, Olsder, Quadrat, *Synchronization and Linearity* | same `ν*` |
| Little’s law `L = λ W` | Little, *Operations Research* 9 (1961) | occupancy |
| Renewal-reward theorem | Ross, *Stochastic Processes*; Feller | `Λ = E[R]/E[T]` |
| Buckingham π-theorem | Buckingham, *Phys. Rev.* 4 (1914) | dimension class of `Q` |
| M/M/1 sojourn and occupancy | Erlang; Kleinrock | stability margin, wait |
| Shannon capacity | Shannon 1948 (already in `SOURCES.md`) | rate-class cousin |

Geometry and the core paper stay. They explained the hypotenuse and the fork. They did not derive a rate from a queue.

---

## 2. Bottleneck (already official, now cited)

**Lemma 1 (tandem bottleneck).** A serial line of work-conserving servers with deterministic service times `τ_ℓ > 0` has maximum stable throughput

```text
ν* = 1 / max_ℓ τ_ℓ
```

*Proof.* Each server `ℓ` accepts at most `1/τ_ℓ` jobs per second. The tandem is limited by the minimum of those rates. The same number is the max-plus eigenvalue of the serial timed event graph (cycle time `max τ_ℓ`). □

This is official Axiom A3 and the textbook M/D/1 paragraph. The constant `1000` is milliseconds to seconds. It is not a free parameter.

---

## 3. Little

**Assumption (utilization reading).** Treat `Π ∈ [0,1)` as the utilization of the bottleneck. Arrival rate `λ = Π ν*`. Mean service time `W = τ* = 1/ν*`.

**Theorem 1 (Little occupancy).**

```text
L_occ = λ W = Π
```

*Proof.* Little’s law, 1961. □

The core paper’s `L = Π τ*` is occupancy times wait. Occupancy itself is `Π`. Both are legal Little quantities. They must be named apart.

---

## 4. Renewal reward — the operational capacity

**Theorem 2 (renewal-reward rate).** Let a cycle be one bottleneck service of length `τ*`. Let the reward per cycle be the cognitive mass `M` (structure delivered or maintained in one coherent update). Then the long-run reward rate is

```text
Λ_M = M / τ* = M ν*
```

If the reward per cycle is the clock-free core `q = √(M² + (Π τ*)²)`,

```text
Λ_q = q ν*
```

*Proof.* Renewal-reward theorem: `lim_{t→∞} R(t)/t = E[R_1]/E[T_1]` almost surely under a non-lattice cycle with finite means. □

`Λ_M` has dimension `Hz`. It is “how much structure the bottleneck can refresh per second.” That is what operations research calls capacity.

**Theorem 3 (official Q is a lift).** With `ν₀ = 1`,

```text
Q = ν* · Λ_q = ν*² q
```

*Proof.* Core paper, Theorem 1. □

The extra `ν*` has no queueing meaning. It is the degree-2 homogeneous lift of `q`. A 20 ms cut that jumps `Q` from 50 to 72 jumps `Λ_q` from 6.02 to 7.22 — the same relative move on a number that lives in Hz.

---

## 5. Buckingham — why the lift is legal and not forced

Quantities: `M, Π` dimensionless, `ν*` of dimension `T⁻¹`.

**Theorem 4 (π-classification).** Any (smooth, nonzero) scalar built from `(M, Π, ν*)` is of the form

```text
ν*^k  f(M, Π)
```

for some real `k` and dimensionless `f`. The official law is `k = 2` with `f = q` after `r = ν*/ν₀` is formed. The renewal-reward law is `k = 1` with `f = M` or `f = q`. Shannon’s channel bound is `k = 1` with `f = log₂(1+M)`.

*Proof.* Buckingham π: one dimensionful quantity, so one free exponent. □

Choosing `k = 2` because rest energy is `m c²` is an analogy. Choosing `k = 1` because capacity is a rate is the operations theorem. They are different objects. Publish both. Do not add them.

---

## 6. M/M/1 — wait and margin

Still under the utilization reading, `ρ = Π`, `μ = ν*`.

**Theorem 5 (M/M/1).** If `Π < 1`,

```text
η      = 1 − Π                 stability margin
W      = τ* / (1 − Π)          mean sojourn
L_sys  = Π / (1 − Π)           mean number in system
L_q    = Π² / (1 − Π)          mean number waiting
```

If `Π ≥ 1` the chain is unstable and those means are infinite.

*Proof.* Standard birth–death balance (Kleinrock). □

Kingman’s G/G/1 approximation reduces to the same sojourn when `c_a = c_s = 1`. We do not claim arrivals are Poisson. We claim: **if** you read `Π` as utilization, these are the waits.

Working point: `η = 0.532`, `W = 0.226 s`, against service `τ* = 0.120 s`. The mind spends as much time waiting as serving.

---

## 7. Shannon cousin

The textbook already derived `ν*` from a deterministic channel of bandwidth `1/τ*`. Shannon’s formula for a power-limited channel with the same bandwidth and SNR `M` (structure as signal) is

```text
C = ν* log₂(1 + M)
```

At the working point `C = 6.52 Hz`, next to `Λ_M = 6.00 Hz`. Same dimension class, different `f`. Neither is official `Q`.

---

## 8. What to publish

| Symbol | Formula | Dimension | Role |
|---|---|---|---|
| `ν*` | `1/max τ` | Hz | bottleneck |
| `Λ_M` | `M ν*` | Hz | renewal-reward capacity |
| `Λ_q` | `q ν*` | Hz | core as reward |
| `Λ_eff` | `u M ν*` | Hz | usable renewal rate |
| `η` | `1−Π` | 1 | stability margin |
| `W` | `τ*/(1−Π)` | s | M/M/1 sojourn |
| `C` | `ν* log₂(1+M)` | Hz | Shannon cousin |
| `Q` | `ν*² q` | Hz² | official lift |

Rules:

1. Compare clocks with `ν*`. Compare structure with `q` or `M`. Compare operational capacity with `Λ_M`.
2. Do not fit Stage F on `Q`. `Q` is `ν*` times a rate. Fit on `(Λ_M, η, u)` or `(q, ε, u)`.
3. `Π → 1` is a hard wall under the utilization reading. Official `Q` does not see it. `W` does.

---

## 9. Working point

```text
M = 0.72035    Π = 0.46811    ν* = 8.333 Hz    u = 0.840
Λ_M   = 6.003 Hz
Λ_q   = 6.021 Hz
Λ_eff = 5.041 Hz
C     = 6.517 Hz
Q     = 50.176
Q/Λ_q = 8.333 = ν*
η     = 0.532
W     = 0.226 s
```

---

## 10. Reproduce

```bash
python3 mathematics/lineage-papers/reference/lineage_ops_v2.py
```

Expect `ops_checks_passed 15`.
