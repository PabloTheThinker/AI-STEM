# Operational Control on the Capacity Partition

**Fudoshin Research · Vektra Industries**  
**Status:** Research paper + executable policy. Stage C.  
**Date:** 2026-08-20  
**Implementation:** `mathematics/lineage-papers/reference/lineage_control_v2.py`  
**Does not change:** Official Specification v2.0.

---

## Abstract

Official `Q` is a degree-2 lift of the core. The operator hint still scored `∂Q`, so it kept saying “cut latency” — because `Q` grows as `ν*²`. Operations research splits installed capacity into two rates that add:

```text
Λ_job + Λ_W  =  Λ_M
M Π ν*  +  M (1−Π) ν*  =  M ν*
```

`Λ_job` is delivered throughput (Little: jobs completing). `Λ_W` is responsiveness (structure per sojourn). The working controller maximizes `Λ_W` under hard safety on `Π` and `u`.

At the working point the official hint is `cut_bottleneck_latency`. The operational action is `shed_load`. A 0.10 drop in utilization raises `Λ_W` by `0.600 Hz`. A 1 Hz bottleneck cut raises it by `0.383 Hz`. A 0.05 mass raise raises it by `0.221 Hz`.

Twelve checks pass. Official `Q` is not replaced. The old hint stays on the card as `hint`. The working action is `ops_action`.

---

## 1. Three rates

Under the utilization reading `λ = Π ν*`, `W = τ*/(1−Π)` for `Π < 1`.

**Theorem 1 (delivered throughput).** Reward `M` per completed job, completion rate `λ`:

```text
Λ_job = M λ = M Π ν*
```

**Theorem 2 (responsiveness).** A tagged job returns every sojourn `W`. Refresh rate `1/W = ν*(1−Π)`:

```text
Λ_W = M / W = M (1−Π) ν*
```

**Theorem 3 (partition).**

```text
Λ_job + Λ_W = Λ_M = M ν*
```

*Proof.* Factor `M ν*`. □

Official `Q` has no such split. `Q = ν* Λ_q` mixes the clock in twice and never sees `Π → 1`.

Working point:

```text
Λ_M   = 6.003 Hz     installed
Λ_job = 2.810 Hz     delivered
Λ_W   = 3.193 Hz     responsive
```

---

## 2. Why the official hint is the wrong lever

`∂Q/∂ν* ~ r³` at rest. Feasible-step scoring on `Q` therefore prefers cutting the bottleneck. That is correct for the lift, false for a rate.

**Theorem 4 (Λ_W steps).** For feasible one-tick sizes `ΔM = 0.05`, `ΔΠ = −0.10`, `Δν* = +1 Hz`,

```text
ΔΛ_W(raise M)  = ΔM · η · ν*
ΔΛ_W(shed Π)   = M · |ΔΠ| · ν*
ΔΛ_W(cut ν*)   = M · η · Δν*
```

At the working point those are `0.221`, `0.600`, `0.383`. The argmax is shed.

Hard rules sit above the scores:

```text
Π ≥ 1      →  unstable_shed_load
Π ≥ 0.85   →  shed_load
u < 0.25   →  repair_health
else       →  argmax ΔΛ_W
```

Raising flux never wins `Λ_W`. It spends margin.

---

## 3. What-if

`--cut-ms` still recomputes the slice (clock move).  
`--shed-pi` moves utilization only: `Π ↦ Π − δ`, with `M`, `ν*`, `u` held. That is the operations lever.

A 0.10 shed at the working point:

```text
ΔΛ_W   = +0.600 Hz
ΔW     = −0.034 s
ΔQ     = −0.032
```

`Q` barely notices. Wait and responsiveness do. That is the instrument working.

---

## 4. What to run

```bash
python3 mathematics/lineage-papers/reference/lineage_control_v2.py
python3 mathematics/lineage-papers/reference/lineage_use_v2.py --example
python3 mathematics/lineage-papers/reference/lineage_use_v2.py --example --shed-pi 0.10
```

Expect `control_checks_passed 12`. Card field `ops_action` is the working lever. `hint` remains the official-`Q` score for audit.
