# The Loop Closes on Wait

**Fudoshin Research · Vektra Industries**  
**Status:** Research paper + executable loop. Stage D on a simulated plant. Not Stage F.  
**Date:** 2026-08-20  
**Implementation:** `reference/lineage_loop_v2.py`  
**Does not change:** Official Specification v2.0.

---

## Abstract

A card can recommend a lever. That is not a loop. A loop measures the plant, acts, and measures again.

Official `Q` is the wrong plant. It is a published invariant, not a sojourn. The operator hint still scores `∂Q`, so it cuts the bottleneck: `Q` grows as `ν*²`. The job does not feel `Q`. The job feels wait.

This module closes the loop on wait. The plant is the same Lindley tandem used for Stage D. Waits come out of mechanism; the controller never reads the sojourn formula, and it never reads `Q`. `Q` stays on the tick as audit.

At a hot window (`Π = 0.60`) the open loop stays over the 400 ms mean SLA. The wait-loop sheds to a 10 ms guard under the wall; the next measured mean is under. The official-`Q` loop cuts the bottleneck instead — the first action the card has always wanted. Both levers can repair the mean. They are not the same action, and `Q` is not why the wait-loop moved.

The tail is not closed. After the mean is repaired, jobs are still late about a third of the time. A percentile SLA is a different loop.

Replay reads JSONL windows. If a line carries `measured_wait_s`, that number is the exogenous residual. That is the socket for a live agent.

---

## 1. Card versus loop

The operator instrument (`lineage_use_v2.py`) takes one window and writes a card. `ops_action` is a one-window recommendation. Nothing applies the lever. Nothing measures the next window.

```text
card:   window → numbers → recommended lever
loop:   measure → decide → apply → measure
```

The real path is the second object. Gate on `u` and on measured wait. Maximize `Λ_W,net` only while `W ≤ W_max`. Official `Q` stays on the card. It does not enter the controller.

---

## 2. Plant

State is `(M, Π, τ, u)`. `Q` is not a coordinate.

Each window the plant draws Poisson arrivals and exponential services and runs the tandem recursion (Lindley 1952). The simulator contains no sojourn formula. The observation is

```text
measured_W  = mean_j (D[j][5] − A[j])
p_miss      = fraction of jobs with sojourn > W_max
```

The traffic equation is computed beside the measurement as a residual, not as the plant:

```text
formula_W   = Σ τ_ℓ / (1 − λ τ_ℓ),   λ = Π / τ*
residual    = measured_W − formula_W
```

A live agent replaces `simulate_tandem` with logged end-to-end sojourn. The controller does not change. That is Stage F's socket, not this paper's claim.

---

## 3. Wait controller

```text
Π ≥ 1                 →  unstable_shed_load
u < 0.25              →  repair_health
measured_W > W_max    →  shed_load by min(δ*(W_max − 10 ms), 0.10)
else                  →  hold
```

The *decision* to shed uses the measurement. The *size* of the shed uses the traffic model, aimed 10 ms under the wall so the next noisy window does not bounce back over. If the model is wrong, the next measurement is still late and the loop sheds again. That is the integral.

`wait_controller` does not take `Q`. The reference checks inspect the signature and the body.

The official-`Q` counterfactual ignores wait and always cuts the bottleneck. It exists so the first-action fork can be tested, not so anyone should run it.

---

## 4. What the seeded loop does

Hot start: `Π = 0.60`, official working mass and latencies, `u = 0.84`, `W_max = 0.400 s`. Theory wait at the start is `0.424 s`. Required shed to the wall is `δ* ≈ 0.032`; the 10 ms guard aims near `Π ≈ 0.55`.

Seeded run (`lineage_loop_v2.py`, same seed family as Stage D):

```text
open loop  Π=0.60  observe only
  t       Pi    meas_W    form_W   p_miss  action                       amt        Q
  0   0.6000    0.4185    0.4237    0.403  hold                       0.000   50.274
  1   0.6000    0.4364    0.4237    0.419  hold                       0.000   50.274
  2   0.6000    0.4045    0.4237    0.392  hold                       0.000   50.274
end  0.6000    0.4302    0.4237    0.423  —                                  50.274

wait loop  Π=0.60  measure → shed/hold
  t       Pi    meas_W    form_W   p_miss  action                       amt        Q
  0   0.6000    0.4185    0.4237    0.403  shed_load                  0.048   50.274
  1   0.5523    0.3890    0.3900    0.369  hold                       0.000   50.236
  2   0.5523    0.3905    0.3900    0.367  hold                       0.000   50.236
  3   0.5523    0.4016    0.3900    0.374  shed_load                  0.020   50.236
end  0.5323    0.3744    0.3778    0.328  —                                  50.221

Q loop     Π=0.60  official hint (cut)
  t       Pi    meas_W    form_W   p_miss  action                       amt        Q
  0   0.6000    0.4185    0.4237    0.403  cut_bottleneck_latency     0.100   50.274
  1   0.6000    0.4255    0.3963    0.400  cut_bottleneck_latency     0.100   62.008
end  0.6000    0.3624    0.3723    0.336  —                                  76.494
```

Three facts from that table, none of them a slogan.

1. The open loop never leaves the wrong side of the wall. A card without an apply does this.
2. The wait-loop sheds, holds, then sheds again. Tick 3 measured `0.402 s` against a formula of `0.390 s` — relative error 3%, still over the wall. The controller believes the measurement. That is the integral. `Q` moved from `50.274` to `50.221`.
3. The Q-loop cuts, twice. After the first cut the formula is already under the wall (`0.396 s`) and the measurement is not (`0.426 s`). The Q-controller does not care: it is scoring `ν*²`. `Q` jumps to `76.5`. Wait is not why it moved.

Along the wait-loop, `|formula_W − measured_W| / formula_W < 0.05`. The controller did not use that formula to decide.

After the mean is repaired, `p_miss` is still `0.328`. Idle already misses about 10%. A 10% miss budget is a different setpoint and still allows almost no flux (`Π ≈ 0.010`). This loop does not pretend otherwise.

At the pinned working point (`Π = 0.468`) the wait-loop holds. The Q-loop still cuts. That is the card's own warning, now executable as a counterfactual.

---

## 5. Bind to an agent

The mathematics does not know about retrievals or tool calls. The bind is a table, not a product integration.

| Action | What an agent actually does |
|---|---|
| `shed_load` | Drop low-priority retrievals, tool calls, or speculative branches this window |
| `cut_bottleneck_latency` | Cache, faster retrieval, or a shorter working-memory hold |
| `repair_health` | Stop writes, raise the merge threshold, freeze identity edits |
| `raise_mass` | Checkpoint memory or graph. Slow. Not the wait-loop's first move |
| `hold` | Keep the window |

Replay:

```bash
python3 mathematics/lineage-papers/reference/lineage_loop_v2.py \
    --replay mathematics/lineage-papers/reference/hot_windows.jsonl
```

A line may be a plant dict `{M, Pi, taus, u}` or a telemetry window the slice already accepts. Optional `measured_wait_s` is the exogenous residual. Without it the replay falls back to the formula and says so.

The table above is executed in `LINEAGE_BIND.md`. Shed drops low-priority jobs. Cut turns on a retrieval cache. Repair freezes writes. `--decide` is the socket for a live orchestrator.

---

## 6. What this is not

- Not Stage F. The plant is still Poisson / exponential. Live traces are the next measurement, not a rewrite of the controller.
- Not Stage G. No live intervention has been applied and checked for sign.
- Not a training objective. Do not put `Q` in a loss. Do not put `Q` in this controller.
- Not a percentile loop. Mean SLA ≠ miss budget.
- Official `Q` is not replaced. The card still prints it.

---

## 7. Reproduce

```bash
python3 mathematics/lineage-papers/reference/lineage_loop_v2.py
python3 mathematics/lineage-papers/reference/lineage_loop_v2.py --run --ticks 6 --pi 0.60
python3 mathematics/lineage-papers/reference/lineage_loop_v2.py --compare --ticks 4
python3 mathematics/lineage-papers/reference/lineage_loop_v2.py \
    --replay mathematics/lineage-papers/reference/hot_windows.jsonl
```

Expect `loop_checks_passed 24`.
