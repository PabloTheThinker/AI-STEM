# Traffic Equations Correct the Tandem, and a Simulation Says So

**Fudoshin Research · Vektra Industries**  
**Status:** Correction + first exogenous validation. Traffic model Stage C → **Stage D**.  
**Date:** 2026-08-20  
**Implementation:** `reference/lineage_traffic_v2.py`, `reference/lineage_sim_v2.py`  
**Corrects:** `LINEAGE_TANDEM_KINGMAN_QOS.md`, `LINEAGE_PARETO_AMDAHL_PK.md`  
**Does not change:** Official Specification v2.0.

---

## Abstract

The tandem papers put every node at the bottleneck's utilization. That is not what one stream of jobs through five stages does. Jackson's traffic equation gives node ℓ the load `ρ_ℓ = λ τ_ℓ` with `λ = Π ν*`; only the bottleneck sits at `Π`. The four fast pipes are cooler.

The correction changes the operational verdict. Tandem wait at the working point is **0.345 s, not 0.423 s** — the all-hot reading overstated by **22.8%** and wrongly declared the mind over its 400 ms mean SLA. Corrected: under the SLA, `Π* = 0.568` not `0.4375`, `δ* = 0`, and the SLA does not bind throughput (`Λ_job` cap 3.407 Hz against live 2.810 Hz).

One claim survives untouched: **the tail**. `P(W_net > 400 ms) = 0.301` at the working point. The mean is fine and three jobs in ten are still late. A 10% miss budget still allows almost no flux (`Π ≈ 0.010`).

Then the part this program has never had: an **exogenous check**. A seeded discrete-event simulation draws Poisson arrivals and exponential services and runs the tandem recursion `D[j][ℓ] = max(D[j][ℓ−1], D[j−1][ℓ]) + S[j][ℓ]` (Lindley 1952). The simulator does not contain the sojourn formulas. Over 70,000 measured jobs: mean wait 0.3424 s against predicted 0.3446 s (0.6%), miss fraction 0.3001 against predicted 0.3008. The all-hot model misses mechanism by 23% and is rejected. Every previous check in this program tested formulas against themselves; this one tests them against a mechanism.

24 traffic checks and 8 simulation checks pass.

---

## 1. What the audit found

Nine modules, 182 checks — all internal consistency. Nothing had ever been compared to a number the formulas did not produce. And the tandem layer carried a flagged-but-unpriced assumption: *"Π common across nodes is a reading."* Priced, that reading is worth 78 ms of phantom wait and one wrong shed order.

## 2. The traffic equation

**Theorem 1 (single-stream loads).** One stream at rate `λ` visits all five stages. Utilization of node ℓ is

```text
ρ_ℓ = λ τ_ℓ,        λ = Π ν* = Π / τ*
```

so `ρ_bottleneck = Π` exactly and `ρ_ℓ < Π` elsewhere. *Proof.* Jackson (1957): in an open network the flow through a series station equals the external arrival rate; utilization is flow times service time. □

**Theorem 2 (corrected sojourn).** With per-node Kingman factor `κ`,

```text
W_net = Σ_ℓ τ_ℓ ( 1 + κ ρ_ℓ / (1 − ρ_ℓ) )
```

`κ = 1` is the M/M/1 tandem (Burke gives Poisson flow into each stage). `κ = 0` recovers `T`.

**Theorem 3 (all-hot is an upper bound).** For `Π < 1`,

```text
W_net ≤ T / (1 − Π)
```

with equality only in the single-node case. *Proof.* `ρ_ℓ ≤ Π` termwise. □

The old model survives as `W_net_upper`: the exact wait when every stage also carries enough foreign traffic to run at the bottleneck's heat. It is a worst case, not the default.

## 3. Corrected working point

```text
λ = 3.9009 Hz     ρ = (0.468, 0.156, 0.117, 0.078, 0.059)

                    all-hot (old)     traffic (corrected)
W_net               0.423 s           0.345 s
Λ_W,net             1.703 Hz          2.090 Hz
Π* (400 ms mean)    0.4375            0.5675
δ*                  0.0306            0
Λ_job cap           2.626 Hz          3.407 Hz  (does not bind)
verdict             over SLA, shed    under SLA
p_miss (400 ms)     0.439             0.301
Π*_pct (α = 0.10)   0.007             0.010
```

The mean-SLA emergency was an artifact of the reading. The tail problem is real in both models: even under the corrected loads, `P(W_net > W_max) = 0.301`, and a 10% miss budget forces near-zero flux. If the deadline matters per-job, the lever is `T` or `W_max`, not `Π` — that conclusion survives its own correction.

Levers stay exact, now by bisection: at a hot window `Π = 0.60`, `W_net = 0.424 s` is over; shed `δ* = 0.032` or cut the bottleneck 4.0 ms (λ held) and the wall is met either way. The cut got cheaper than the all-hot model claimed for a structural reason: with `λ` held, shortening the bottleneck also lowers the bottleneck's own utilization, so wait falls at rate `1/(1−ρ)²` per millisecond — the all-hot model, holding `Π` fixed everywhere, only credited `1/(1−Π)`.

## 4. The simulation

Protocol (pre-stated in the checks, seeded, pure Python):

1. Draw `A_j − A_{j−1} ~ Exp(λ)` and `S_{j,ℓ} ~ Exp(1/τ_ℓ)` with `random.Random(20260820)`.
2. Tandem recursion, FIFO, infinite buffers: `D[j][ℓ] = max(D[j][ℓ−1], D[j−1][ℓ]) + S[j][ℓ]`.
3. 80,000 jobs, first 10,000 discarded as warmup. Sojourn `W_j = D[j][5] − A_j`.
4. Pass rules: mean within 3% of Theorem 2; miss fraction within 0.02 of the hypoexponential tail; the all-hot prediction must bound mechanism from above; a second load level (`Π = 0.20`) must also match.

Result (seeded run, 70,000 measured jobs):

```text
sim mean W       0.342411 s     theory 0.344606 s     (0.6%)
sim P(W > 0.4)   0.300114       theory 0.300768
all-hot 0.423018 s: off mechanism by 23% — rejected
```

Failure of any rule would have shipped as a miss. It did not fail.

## 5. Stages, honestly

| Object | Before | Now |
|---|---|---|
| Traffic-equation sojourn + tail | — | **D** (mechanism-validated, synthetic) |
| All-hot tandem model | C, presented as default | C, demoted to upper bound |
| Exact SLA levers (`δ*`, cut) | C | **D** via the same mechanism |

Stage D is still synthetic: the simulator is honest about arrivals and services but they are the *assumed* laws (Poisson, exponential). Stage F needs live waits. What changed is that the formulas now survive contact with a process that does not know them.

The next object is a loop, not another formula. Measure that sojourn, act, measure again. Official `Q` stays off the controller. See `LINEAGE_CLOSED_LOOP.md`.

## 6. Reproduce

```bash
python3 mathematics/lineage-papers/reference/lineage_traffic_v2.py
python3 mathematics/lineage-papers/reference/lineage_sim_v2.py
```

Expect `traffic_checks_passed 24` and `sim_checks_passed 8`.
