# Tandem Sojourn, Kingman Variability, and a QoS Cap

**Fudoshin Research · Vektra Industries**  
**Status:** Research paper (named theorems + checks). Stage C.  
**Date:** 2026-08-20  
**Implementation:** `mathematics/lineage-papers/reference/lineage_network_v2.py`  
**Does not change:** Official Specification v2.0.

> **Correction (same day).** This paper loads every node at the bottleneck's
> utilization. A single stream through five stages actually gives `ρ_ℓ = λ τ_ℓ`
> (Jackson traffic equation), which makes this model an **upper bound** that
> overstates the working-point wait by 22.8% and wrongly declares it over the
> mean SLA. The corrected default, validated by discrete-event simulation, is
> `LINEAGE_TRAFFIC_AND_SIMULATION.md`. The theorems below are kept as the exact
> all-hot worst case (`W_net_upper` on the operator card).

---

## Abstract

The last paper treated the mind as one M/M/1 at the bottleneck. The packet already logs five latencies. Responsiveness is not `τ*/(1−Π)`. It is the sum of the waits.

A Jackson tandem of M/M/1 nodes with common utilization `Π` has sojourn `W_net = (Σ τ_ℓ)/(1−Π)`. Kingman’s G/G/1 approximation inserts a variability factor `κ = (c_a² + c_s²)/2`. A delay SLA `W_net ≤ W_max` caps utilization at `Π* = 1 − T/W_max` (Poisson case).

At the working point `T = 0.225 s`. Single-server sojourn was `0.226 s`. Tandem sojourn is `0.423 s`. Responsiveness drops from `Λ_W = 3.19 Hz` to `Λ_W,net = 1.70 Hz`. The one-node model overestimated by `1.875×` — exactly `T/τ*`. Against a 400 ms SLA, `Π* = 0.437` and live `Π = 0.468` is over cap. The working action is still shed, now for a delay budget, not only for `ΔΛ_W`.

Fourteen checks pass. Official `Q` is not replaced. `Π` common across nodes is a reading.

---

## 1. Why one server was not enough

Official A3 and the textbook M/D/1 paragraph set throughput by the slowest pipe. That is correct for **rate**. It is false for **wait**. A job crosses retrieval, pathway, working memory, sync, and settling. Little still holds at each node. The tagged job’s time in system is the sum.

Sources: Jackson (1957) on networks of waiting lines; Burke (1956) — the output of a stable M/M/1 is Poisson at the arrival rate, which is why a tandem of M/M/1 nodes stays product-form; Reich (1957) on tandem waits; Kleinrock vol. 1; Kingman (1961) on the heavy-traffic G/G/1 wait; Bertsekas–Gallager, *Data Networks*, on delay constraints.

`Π` common across nodes is a reading, not a Jackson traffic-equation solution. Distinct service times are logged; a common utilization is the coarsest consistent use of the official flux scalar.

---

## 2. Tandem sojourn

**Assumption.** Five work-conserving nodes in series, service times `τ_ℓ`, common utilization `Π ∈ [0,1)`. Throughput remains `ν* = 1/max τ_ℓ` (stability of the slowest).

**Theorem 1 (Jackson tandem, Poisson).** If each node is M/M/1 with load `Π`,

```text
W_ℓ     = τ_ℓ / (1 − Π)
W_net   = Σ W_ℓ = T / (1 − Π)
T       := Σ τ_ℓ
Λ_W,net = M / W_net = M (1 − Π) / T
```

*Proof.* Independent geometric sojourns in a Jackson tandem; add means. □

**Corollary (overestimate).** The one-node model used `W* = τ*/(1−Π)`. Then

```text
W_net / W* = T / τ* ≥ 1
```

with equality only when every non-bottleneck latency is zero. At the working point `T/τ* = 1.875`.

Throughput `Λ_job = M Π ν*` does not change. Only responsiveness does.

---

## 3. Kingman variability

**Theorem 2 (Kingman G/G/1, 1961).** For a G/G/1 node with SCVs `c_a², c_s²` and `κ = (c_a² + c_s²)/2`,

```text
W_ℓ ≈ τ_ℓ + κ · τ_ℓ · Π / (1 − Π) = τ_ℓ ( 1 + κ Π/(1−Π) )
```

`κ = 1` recovers M/M/1. `κ = 0` is deterministic (M/D/1 queueing part vanishes). `κ = 2` is a bursty tax: the queueing addend doubles.

**Theorem 3 (tandem Kingman).** Under a common `κ` and `Π`,

```text
W_net(κ) = T ( 1 + κ Π/(1−Π) )
```

The **variability tax** on wait is `W_net(κ)/W_net(1) = (1−Π + κ Π)/(1−Π+Π) = 1 − Π + κ Π`.

At the working point, `κ = 2` makes `W_net = 0.621 s` against `0.423 s` Poisson.

Default in the instrument is `κ = 1` (Poisson). Declare `κ` if you log burstiness.

---

## 4. QoS cap

**Theorem 4 (delay SLA).** Require `W_net ≤ W_max` with `κ = 1` and `W_max > T`. Then

```text
Π* = 1 − T / W_max
```

is the maximum legal utilization. If `Π > Π*`, no amount of mass or official `Q` meets the SLA. Shed until `Π ≤ Π*`, or cut `T`.

*Proof.* Invert Theorem 1. □

Default SLA in the instrument: `W_max = 0.400 s` (hyperparameter, not a law). Working `T = 0.225` gives `Π* = 0.437`. Live `Π = 0.468` is over.

For general `κ`, invert Theorem 3:

```text
Π* = (W_max − T) / (W_max − T + κ T)     (W_max > T)
```

---

## 5. What this does to the controller

`Λ_W,net = M(1−Π)/T` still rises fastest by shedding `Π` at the working point. The new fact is the SLA: shed is required, not only preferred.

Official `Q` and single-node `W*` both miss this. `Q` does not see `T`. `W*` pretends the other four pipes are free.

---

## 6. Working point

```text
τ = (0.120, 0.040, 0.030, 0.020, 0.015) s
T = 0.225 s     τ* = 0.120 s     T/τ* = 1.875
Π = 0.468       κ = 1            W_max = 0.400 s
W*     = 0.226 s     Λ_W     = 3.193 Hz
W_net  = 0.423 s     Λ_W,net = 1.703 Hz
Π*     = 0.437       over_sla = true
```

---

## 7. Reproduce

```bash
python3 mathematics/lineage-papers/reference/lineage_network_v2.py
```

Expect `network_checks_passed 14`.

Required shed `δ*`, Amdahl cut, and the Jackson miss tail: `LINEAGE_PARETO_AMDAHL_PK.md`.
