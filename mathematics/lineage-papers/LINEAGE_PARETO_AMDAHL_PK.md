# Pareto SLA, Amdahl Cuts, and Pollaczek–Khinchine

**Fudoshin Research · Vektra Industries**  
**Status:** Research paper (named theorems + checks). Stage C.  
**Date:** 2026-08-20  
**Implementation:** `mathematics/lineage-papers/reference/lineage_qos_v2.py`  
**Depends on:** `LINEAGE_TANDEM_KINGMAN_QOS.md`  
**Does not change:** Official Specification v2.0.

> **Correction (same day).** The numbers below inherit the all-hot reading and
> are the **upper-bound** case. Under the single-stream traffic equations the
> working point is under the mean SLA (`W_net = 0.345 s`, `Π* = 0.568`,
> `δ* = 0`), while the tail conclusion survives (`p_miss = 0.301`; a 10% miss
> budget still allows `Π ≈ 0.010`). Corrected model and simulation:
> `LINEAGE_TRAFFIC_AND_SIMULATION.md`. The wall-invariance, Amdahl, PK, and
> hypoexponential theorems are unchanged as mathematics.

---

## Abstract

The tandem paper said the mind is five waits, not one, and that live `Π` is over a 400 ms mean SLA. It did not say **how much** to shed, **how much** to cut, or whether those two levers are the same thing.

They are the same for responsiveness and different for throughput.

On the delay wall `W_net = W_max`, Little gives `Λ_W,net = M / W_max` — a constant. Shedding `Π` down to `Π*` and cutting total service down to `T* = W_max(1−Π)` land on the same responsiveness. Shed spends delivered jobs. Cut spends the bottleneck clock and official `Q`.

Pollaczek–Khinchine is Kingman with Poisson arrivals (`c_a² = 1`). Amdahl’s serial fraction is `τ*/T = 0.533` at the working point: more than half the wait is the slow pipe, and the needed 12.2 ms cut fits inside the 80 ms slack before the bottleneck moves. Burke plus independent exponential sojourns give an exact tail:

```text
P(W_net > 0.400 s) = 0.439   live
                     0.401   on the mean wall
                     0.098   idle (Π = 0)
```

A 10% miss budget allows `Π ≈ 0.007`. You cannot have a 400 ms deadline, exponential service, `T = 225 ms`, and meaningful flux. A mean cap is not a percentile cap.

Nineteen checks pass. Official `Q` is not replaced.

---

## 1. What was missing

Tandem sojourn `W_net = T/(1−Π)` is a mean. The controller said “shed” because the mean was over. An operator needs three numbers:

```text
δ*     = how much Π to drop
ΔT*    = how much total service to cut
p_miss = chance a tagged job exceeds W_max
```

Those come from Little, Amdahl, Pollaczek–Khinchine, and the hypoexponential tail of a Jackson tandem — not from official `Q`.

---

## 2. Pollaczek–Khinchine is the Poisson case of Kingman

**Theorem 1 (PK / M/G/1).** For Poisson arrivals and general service with SCV `c_s²`,

```text
W = τ ( 1 + κ_PK · Π / (1−Π) )
κ_PK = (1 + c_s²) / 2
```

*Proof.* Pollaczek (1930), Khinchine (1932). Residual service `E[s²]/(2E[s])` plus PASTA (Wolff 1982). □

Kingman (1961) replaces `1` by `c_a²`. Exponential service is `c_s² = 1`, so `κ = 1` and `W = τ/(1−Π)`. Deterministic service is `κ = 1/2`. The instrument’s default `κ = 1` is the PK exponential case, not a guess.

**Lemma (PASTA).** Time-average utilization equals arrival-average utilization for Poisson arrivals. Reading `Π` from a window mean is legal under that arrival law. It is an approximation otherwise; declare `κ` if you log burstiness.

---

## 3. The SLA wall is a level set of responsiveness

**Theorem 2 (wall invariance).** If `W_net = W_max` and `W_max > 0`, then

```text
Λ_W,net = M / W_net = M / W_max
```

independent of how you got there. Shed (`Π ↦ Π*`, `T` held) and cut (`T ↦ T*`, `Π` held) produce the **same** `Λ_W,net`.

*Proof.* Definition of `Λ_W,net`. □

At the working point that common value is `0.72035 / 0.400 = 1.801 Hz`.

They are not the same for jobs or for official `Q`:

```text
Λ_job(Π*) = M Π* ν*     <  Λ_job(Π)     (shed spends throughput)
T* < T  ⇒  ν* may rise                  (cut can raise Q)
```

**Theorem 3 (required levers, κ = 1).**

```text
Π*   = 1 − T / W_max                 (W_max > T)
δ*   = max(0, Π − Π*)
T*   = W_max (1 − Π)
ΔT*  = max(0, T − T*)
```

Working point: `δ* = 0.0306`, `ΔT* = 12.2 ms`.

For general `κ` invert Kingman as in the tandem paper. The wall theorem still holds: any pair with `W_net(κ) = W_max` has the same `Λ_W,net`.

---

## 4. Amdahl: where the cut actually lands

**Theorem 4 (serial fraction).** Write `T = τ* + T_other`. The bottleneck share of service is

```text
s = τ* / T ∈ (0, 1]
```

A cut that only shortens the slowest pipe by `Δ ≤ slack` changes `T` by `Δ` and does not move `ν*`’s argmax, where

```text
slack = τ* − τ_(2)
```

and `τ_(2)` is the second-slowest latency.

Working point: `s = 0.533`, `slack = 80 ms`, `ΔT* = 12.2 ms`. The mean SLA is reachable by a bottleneck-only cut. Official `hint` (“cut retrieval”) is therefore a *legal* SLA repair here — just not the cheapest responsiveness repair, and it still leaves the percentile hole in §6.

If `ΔT* > slack`, a retrieval-only cut moves the bottleneck. The remainder must come from the new slowest pipe, or from shed.

Amdahl (1967) is the same bookkeeping: you cannot speed up more than the serial piece allows. Here the serial piece is the logged bottleneck, and the “parallel” piece is the other four latencies you already pay.

---

## 5. Pareto box

Hold `M, T, ν*` and require

```text
W_net ≤ W_max
Λ_job ≥ Λ_min          (optional throughput floor)
```

**Theorem 5 (feasible utilization).** For `κ = 1`,

```text
Π_min = Λ_min / (M ν*)
Π*    = 1 − T / W_max
feasible  ⇔  0 ≤ Π_min ≤ Π* < 1
```

On that interval `Λ_W,net` is decreasing in `Π` and `Λ_job` is increasing. The Pareto front of `(Λ_job, Λ_W,net)` is the interval itself.

- Max responsiveness under a job floor: operate at `Π_min`.
- Max throughput under the SLA: operate at `Π*`, with `Λ_job^cap = M Π* ν*`.
- No job floor (default instrument): if over SLA, shed to `Π*`.

This is Boyd-style constrained optimization on a 1-dimensional convex set. There is no interior stationary point.

Working `Λ_job^cap = 2.626 Hz` against live `2.810 Hz`. Meeting the mean SLA costs `0.184 Hz` of delivered structure if you shed, or nothing delivered if you cut 12.2 ms and keep `Π`.

---

## 6. The mean SLA is not a percentile SLA

Burke (1956): each stable M/M/1 has exponential sojourn, and the departure process is Poisson, so the next node sees Poisson arrivals. Under the common-`Π` reading, node `ℓ` has sojourn `~ Exp(μ_ℓ)` with `μ_ℓ = (1−Π)/τ_ℓ`, independent.

**Theorem 6 (hypoexponential tail).** `W_net = Σ W_ℓ` is hypoexponential with those rates (distinct). For distinct `μ_j`,

```text
P(W_net > t) = Σ_j  e^{−μ_j t}  Π_{k≠j} μ_k / (μ_k − μ_j)
```

Pinned:

```text
P(W_net > 0.400) = 0.439   at live Π
                 = 0.401   at Π* (mean wall)
                 = 0.098   at Π = 0
```

Idle is already a 10% miss. The bottleneck sojourn alone is `P(W_* > 0.400) = e^{-0.400/0.120} = 0.036`; the other four waits push idle to `0.098`. A single exponential on the mean wall would miss `e^{-1} ≈ 0.368`. Five distinct rates miss `0.401`.

**Corollary.** A controller that only meets `E[W_net] ≤ W_max` late-delivers about two jobs in five. A percentile SLA `P(W_net > W_max) ≤ 0.10` forces `Π ≈ 0.007` — empty. Meaningful flux at a 10% miss budget needs a smaller `T` or a larger `W_max`, not a smaller official `Q`.

Percentile caps that still allow work:

```text
α = 0.20  →  Π*_pct = 0.218
α = 0.30  →  Π*_pct = 0.344
α = 0.37  →  Π*_pct = 0.411   (near the mean wall)
```

The instrument reports `p_over_sla`. It does **not** switch the working action to the percentile cap unless you pass `--alpha`. Default action remains the mean SLA. Percentile is the honest number next to it.

`κ ≠ 1` has no closed tail here. Then `p_over_sla` is withheld.

---

## 7. What this does to the controller

```text
if Π ≥ 1:           unstable_shed_load
if W_net > W_max:   shed_load          (δ* reported; ΔT* reported)
else:               ops_action on Λ_W  (single-node partition, still true)
```

`Λ_job + Λ_W = Λ_M` remains the **single-node** identity. Tandem responsiveness does not sit on that sum:

```text
Λ_W / Λ_W,net = T / τ* = 1.875
```

Keep both on the card. Do not add `Λ_W,net` to `Λ_job` and call it installed capacity.

`--meet-sla` sheds exactly `δ*`. `--cut-ms` remains the clock lever. They meet the same `Λ_W,net` and different `Λ_job`.

---

## 8. Working point

```text
T = 0.225 s     τ* = 0.120 s     s = 0.533     slack = 80 ms
Π = 0.468       Π* = 0.4375      δ* = 0.0306
W_max = 0.400 s
W_net = 0.423 s                  over_sla = true
ΔT* = 12.2 ms                    fits_bottleneck = true
Λ_W,net live = 1.703 Hz
Λ_W,net wall = 1.801 Hz
Λ_job live   = 2.810 Hz
Λ_job cap    = 2.626 Hz
p_over_sla   = 0.439
Π*_pct(0.10) = 0.007
```

---

## 9. Reproduce

```bash
python3 mathematics/lineage-papers/reference/lineage_qos_v2.py
python3 mathematics/lineage-papers/reference/lineage_use_v2.py --example
python3 mathematics/lineage-papers/reference/lineage_use_v2.py --example --meet-sla
```

Expect `qos_checks_passed 19`.
