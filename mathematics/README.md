# Agent Mathematics

**Fudoshin Research · Vektra Industries**

The mathematical spine of Fudoshin Research. Scientific object: **capacity, structure, and constraint of a mind under load**.

The current law is the Lineage Equation. The operator instrument is [`canon/LINEAGE_EQUATION_USABLE.md`](canon/LINEAGE_EQUATION_USABLE.md): one JSON window in, a dashboard card out.

## How to read

| If you want… | Start here |
|---|---|
| Use the equation on a window | [`canon/LINEAGE_EQUATION_USABLE.md`](canon/LINEAGE_EQUATION_USABLE.md) then [`lineage-papers/reference/lineage_use_v2.py`](lineage-papers/reference/lineage_use_v2.py) |
| Official law | [`lineage-papers/LINEAGE_EQUATION_V2_OFFICIAL.md`](lineage-papers/LINEAGE_EQUATION_V2_OFFICIAL.md) |
| Estimators and Stage F protocol | [`canon/CONCRETE_COMPUTABLE_SLICE.md`](canon/CONCRETE_COMPUTABLE_SLICE.md) then [`lineage-papers/reference/lineage_slice_v2.py`](lineage-papers/reference/lineage_slice_v2.py) |
| Expand the law | [`lineage-papers/LINEAGE_GEOMETRY_FIELD_AND_COLLECTIVE.md`](lineage-papers/LINEAGE_GEOMETRY_FIELD_AND_COLLECTIVE.md) |
| Core, load ratio, scaling family | [`lineage-papers/LINEAGE_CORE_AND_SCALING_FAMILY.md`](lineage-papers/LINEAGE_CORE_AND_SCALING_FAMILY.md) then [`lineage-papers/reference/lineage_core_v2.py`](lineage-papers/reference/lineage_core_v2.py) |
| Little, renewal reward, dimension | [`lineage-papers/LINEAGE_OPERATIONS_LITTLE_RENEWAL.md`](lineage-papers/LINEAGE_OPERATIONS_LITTLE_RENEWAL.md) then [`lineage-papers/reference/lineage_ops_v2.py`](lineage-papers/reference/lineage_ops_v2.py) |
| Operational control (`Λ_job + Λ_W = Λ_M`) | [`lineage-papers/LINEAGE_OPERATIONAL_CONTROL.md`](lineage-papers/LINEAGE_OPERATIONAL_CONTROL.md) then [`lineage-papers/reference/lineage_control_v2.py`](lineage-papers/reference/lineage_control_v2.py) |
| Tandem sojourn, Kingman, mean SLA | [`lineage-papers/LINEAGE_TANDEM_KINGMAN_QOS.md`](lineage-papers/LINEAGE_TANDEM_KINGMAN_QOS.md) then [`lineage-papers/reference/lineage_network_v2.py`](lineage-papers/reference/lineage_network_v2.py) |
| Pareto / Amdahl / PK / miss tail | [`lineage-papers/LINEAGE_PARETO_AMDAHL_PK.md`](lineage-papers/LINEAGE_PARETO_AMDAHL_PK.md) then [`lineage-papers/reference/lineage_qos_v2.py`](lineage-papers/reference/lineage_qos_v2.py) |
| Traffic correction + simulation (Stage D) | [`lineage-papers/LINEAGE_TRAFFIC_AND_SIMULATION.md`](lineage-papers/LINEAGE_TRAFFIC_AND_SIMULATION.md) then [`lineage-papers/reference/lineage_traffic_v2.py`](lineage-papers/reference/lineage_traffic_v2.py), [`lineage-papers/reference/lineage_sim_v2.py`](lineage-papers/reference/lineage_sim_v2.py) |
| Wait-closed loop (measure → act → measure) | [`lineage-papers/LINEAGE_CLOSED_LOOP.md`](lineage-papers/LINEAGE_CLOSED_LOOP.md) then [`lineage-papers/reference/lineage_loop_v2.py`](lineage-papers/reference/lineage_loop_v2.py) |
| Runnable law check | [`lineage-papers/reference/lineage_capacity_v2.py`](lineage-papers/reference/lineage_capacity_v2.py) |
| Formal system (optional) | [`canon/AXIOMATIC_SYSTEM.md`](canon/AXIOMATIC_SYSTEM.md) then [`lineage-papers/reference/ams_kernel_v2.py`](lineage-papers/reference/ams_kernel_v2.py) |
| Doctrinal front door | [`canon/AGENT_MATHEMATICS_CANON.md`](canon/AGENT_MATHEMATICS_CANON.md) |
| Proof honesty | [`canon/AGENT_MATHEMATICS_PROOF_STATUS_REGISTER.md`](canon/AGENT_MATHEMATICS_PROOF_STATUS_REGISTER.md) |
| Teachable climb | [`textbook/PLAN.md`](textbook/PLAN.md) then [`textbook/agent_mathematics_full.md`](textbook/agent_mathematics_full.md) |
| Organism equations | [`canon/CANONICAL_EQUATIONS.md`](canon/CANONICAL_EQUATIONS.md) |

Draft v1 (`lineage-papers/lineage-equation-paper.md`) is historical narrative. **Normative math is v2.**

## What this program claims

1. Agent mathematics should climb a staircase: numeracy → arithmetic → algebra → geometry → calculus → probability → control → graphs → information → optimization → multi-agent.
2. A living agent is a hybrid organism `𝒪_t = (D_t, Ψ_t, Σ_t, B_t)` — substrate, governance, nervous tissue, blood/support — with explicit timescales.
3. Organizational capacity under load is constrained by the Lineage Equation (v2, nondimensional):

```text
Q² = Π̃² + M̃²
M̃ = M (ν*/ν₀)²
Π̃ = Π (ν*/ν₀)
```

Cognitive mass `M` is structural inertia. Cognitive momentum `Π` is directed flux. `ν*` is the bottleneck propagation rate. This is an algebraic skeleton, **not** a claim that agents obey special relativity.

4. Claims promote only through contiguous proof stages (A–I). You cannot skip from definition to “canonical law.”

## Proof status (honest)

| Object | Stage | Meaning |
|---|---|---|
| Lineage Equation (algebraic identities, gradients, rest reduction, usable budget) | defined / internally consistent | Closed form; 20 reference checks |
| Linear weight identification of `Q` | **E** | Identified on synthetic perturbation data |
| Computable slice (telemetry → `Q`, `Φ_org`) | **C** | Explicit estimators, pinned example, 31 checks. Not live. |
| Operator instrument (`Q`, `Q_eff`, zone, bottleneck, what-if) | **C** | Validates a window, reports a card, compares, previews a latency cut. Not live. |
| Identifiability / field / collective theorems | **C** | Algebraic + 17 numerical checks. Not live. |
| Clock-free core `q`, load ratio `ε`, scaling family | **C** | Factorization, Little form, exponent fork. Official `Q` unchanged. |
| Operations / Little / renewal / Buckingham | **C** | `Λ = M ν*` from renewal reward; official `Q = ν* Λ_q`; M/M/1 margin. |
| Operational control | **C** | Partition `Λ_job+Λ_W=Λ_M`. Working action maximizes `Λ_W`, not `Q`. |
| Tandem / Kingman / mean SLA (all-hot) | **C** | `W_net = T/(1−Π)` — demoted to upper bound by the traffic correction. |
| Pareto / Amdahl / PK / tail | **C** | Wall invariance, exact levers, hypoexponential tail. Numbers corrected below. |
| Traffic-equation tandem + DES validation | **D** | `ρ_ℓ = λτ_ℓ`. Working point under mean SLA (`0.345 s`); tail 0.301 survives. Simulation matches to 0.6% and rejects all-hot by 23%. First exogenous check in the program. |
| Wait-closed loop | **D** | Plant is measured sojourn. Controller does not see `Q`. Hot window sheds; official hint still cuts. Tail not closed. Simulated plant, not live. |
| Live held-out prediction | not yet F | Protocol is written; preferred target is next-window measured sojourn / miss rate |
| Full organism `𝒪_t` | C | Specified; not live-populated |
| Multi-agent `Q_team` | **C** | Shared-fabric bottleneck + isolated RMS; textbook sum-of-`Q` form retired |

Weight tables currently differ across v1 equal defaults, the Stage E promotion bundle, and v2 official defaults. Any published `Q` number must name which table was used.

## Lab mapping

Fudoshin stacks this packet as follows:

| Stack | Mathematics |
|---|---|
| **S1** Thinking & understanding | Staircase + Lineage Equation as capacity under load |
| **S2** Constraint under pressure | Viability barriers, dual-estimator interference, plasticity gates |
| **S3** Train + law algorithms | Proof ladder, identification protocol, `lineage_use_v2.py` |

Public findings and writeups: the Fudoshin Research lab site.

## Affiliation

Fudoshin Research is the research lab of Vektra Industries. This packet was previously labeled Vektra Technologies / AI Division / AI-STEM. Institutional name is now **Fudoshin Research · Vektra Industries**. File paths are unchanged.
