# Symbols And Notation Glossary

Updated: `2026-04-05`

## Purpose

This file is the canonical notation reference for the mathematics packet.

Its job is to:

- keep symbol usage stable across the packet,
- prevent collisions between similarly named objects,
- distinguish state objects from operators, constraints, modes, and events,
- and make later formalization easier.

This glossary follows the organismic basis in:

- `ORGANISMIC_INTELLIGENCE_MATHEMATICAL_BASIS.md`
- `DIFFERENTIABLE_SUBSTRATE_AND_ORGANISM_INTEGRATION.md`
- `LIVING_RESEARCH_MATHEMATICAL_EXTENSION.md`
- `VIRTUAL_NERVOUS_SYSTEM_MATHEMATICAL_EXTENSION.md`
- `VIRTUAL_BLOOD_SYSTEM_MATHEMATICAL_EXTENSION.md`

## Global Conventions

### Time indexing

- `t` = discrete time index
- `t+1` = next update step
- `τ_*` = characteristic timescale of a subsystem

### Typography conventions

- uppercase calligraphic symbols such as `𝒮`, `𝓘`, `𝓤`, `𝓒` denote families or sets
- uppercase Greek or Latin symbols such as `Ψ_t`, `Σ_t`, `B_t`, `D_t` denote compound state objects
- lowercase symbols such as `r_t`, `x_t`, `m_t`, `a_t` denote component states, modes, or actions
- capitalized names such as `ReadCtx`, `SubstrateUpdate`, `PlasticityGate` denote operators or maps
- `Δx_t`, `ΔΣ_t`, `ΔB_t` denote updates, increments, or proposed writes
- `Π_*` denotes a projection or consistency map
- `Φ_*` denotes a barrier, viability potential, or penalty
- `L_*` denotes a loss term or task objective
- `X_*` denotes a set, usually a safe or viable set

### Meaning of arrows and products

- `->` means a map from one object type to another
- `×` means Cartesian product or structured composition of spaces
- `∪` means set union
- `<<` means a much faster timescale ordering

## Basis-Level Symbols

### Basis object

```text
𝔅_org = (𝒮, 𝓘, 𝓤, 𝓒, 𝓜, 𝓔, 𝓣)
```

- `𝔅_org` = the organismic mathematical basis
- `𝒮` = state-space family
- `𝓘` = interface-map family
- `𝓤` = update-operator family
- `𝓒` = constraint and barrier family
- `𝓜` = mode set
- `𝓔` = event set
- `𝓣` = timescale ordering

### Full organism state

```text
𝒪_t = (D_t, Ψ_t, Σ_t, B_t)
```

- `𝒪_t` = full organism state at time `t`
- `D_t` = differentiable substrate state
- `Ψ_t` = governance and living-research state
- `Σ_t` = nervous-system state
- `B_t` = blood-system state

## Substrate Symbols

### Core substrate object

```text
D_t = (θ_t, alpha_t, χ_t, ω_t)
```

- `D_t` = differentiable substrate state
- `θ_t` = slow structural parameters
- `alpha_t` = fast activation state
- `χ_t` = internal routing and gating state
- `ω_t` = optimizer, adapter, or plasticity state

### Substrate-facing functions

- `f_(θ_t)` = differentiable model at parameter state `θ_t`
- `ι_t` = composed substrate input at time `t`
- `target_t` = task target or supervision target
- `L_task(f_(θ_t)(ι_t), target_t)` = task loss

### Projection symbols

- `Π_r` = projection from substrate state to organism-visible internal summary
- `r_t = Π_r(D_t)` = lawful projected internal state

## Governance And Organism Symbols

### Governance state

```text
Ψ_t = (Ξ_t, ρ_t, Λ_t, N_t, m_t, a_t)
```

- `Ψ_t` = governance state
- `Ξ_t` = organism-visible state bundle
- `ρ_t` = reserve state
- `Λ_t` = lineage or branch population state
- `N_t` = niche state
- `m_t` = operating mode
- `a_t` = governance action

### Organism-visible state

```text
Ξ_t = (r_t, x_t, μ_t, G_t, s_t, q_t, u_t, y_t)
```

- `r_t` = projected internal organism state
- `x_t` = body-memory or embodied working state
- `μ_t` = belief, estimate, or latent controller summary
- `G_t` = graph or cognitive-web state
- `s_t` = sensed or estimated world state summary
- `q_t` = quality, confidence, or viability-related scalar/vector summary
- `u_t` = current control, policy, or actuator choice
- `y_t` = external observation or incoming input

### Governance-related discrete symbols

- `spawn_branch` = event or action creating a new branch lineage
- `quarantine_branch` = event or action isolating a risky branch
- `promote_branch` = event or action promoting a branch into stronger status
- `trigger_regeneration` = event or action entering regenerative mode

## Nervous-System Symbols

### Nervous tissue state

```text
Σ_t = (A_t, J_t, K_t, P_t, E_t, M_t, H_t)
```

- `Σ_t` = nervous-system state
- `A_t` = afferent field
- `J_t` = local junction or integration state
- `K_t` = gate or commitment state
- `P_t` = pathway and routing state
- `E_t` = efferent dispatch state
- `M_t` = neuromodulatory posture
- `H_t` = neural-health state

### Afferent notation

- `A_t^exo` = exogenous or outer-input afferents
- `A_t^intero` = interoceptive afferents from internal organism state
- `A_t^mem` = memory-derived afferents
- `A_t^err` = error or anomaly afferents
- `A_t^gov` = governance-derived afferents

### Junction and gate notation

- `J_t^(r)` = local integration state at region `r`
- `e_r` = excitatory drive at region `r`
- `i_r` = inhibitory drive at region `r`
- `c_r` = contextual drive at region `r`
- `s_r` = salience or urgency drive at region `r`
- `φ_r` = local junction posture or summary variable
- `K_t^(r)` = gate state at region `r`
- `d_r` = integrated drive at region `r`
- `θ_r` = threshold at region `r`
- `γ_r` = overload, refractory, or commitment stress term
- `o_r` = gate-open indicator or commitment output

### Route and efferent notation

- `R_t` = route registry or route set
- `L_t` = route latency state
- `T_t` = route trust or reliability state
- `Y_t` = insulation, stability, or myelination-like route quality
- `E_t^act` = outward action efferents
- `E_t^auto` = autonomic or internal regulation efferents
- `F_t` = feedback or acknowledgment field

### Modulator and health notation

- `M_t` = neuromodulator vector
- `H_t` = neural-health vector
- `h_exc` = excitatory pressure
- `h_noise` = neural noise burden
- `h_flood` = flooding or overload risk
- `h_lat` = latency stress
- `h_route` = route degradation burden
- `h_ground` = grounding or anchoring risk

## Blood-System Symbols

### Blood tissue state

```text
B_t = (Pl_t, Ma_t, Li_t, De_t, St_t, Cl_t, Hb_t)
```

- `B_t` = blood-system state
- `Pl_t` = plasma, flow, and packet-circulation state
- `Ma_t` = marrow or worker-generation state
- `Li_t` = blood-lineage population state
- `De_t` = support-demand state
- `St_t` = stabilization state
- `Cl_t` = clearance and cleanup state
- `Hb_t` = blood-health state

### Plasma and marrow notation

- `Q_t` = circulation queue
- `F_t` = flow state
- `U_t` = freshness or urgency pressure
- `R_t` = route reachability or delivery registry
- `Tg_t` = marrow targets
- `Bg_t` = marrow spawn budget
- `Dm_t` = demand bias
- `Sp_t` = substrate or template health for worker spawning

### Lineage notation

- `Li_t` = lineage population vector
- `l_rbc` = virtual red-blood-cell population
- `l_plt` = virtual platelet population
- `l_neu` = virtual neutrophil population
- `l_mono` = virtual monocyte population
- `l_mac` = virtual macrophage population
- `l_lym` = virtual lymphocyte population

### Demand, stabilization, and clearance notation

- `De_t` = support-demand bundle
- `d_ctx` = context-delivery demand
- `d_health` = health-support demand
- `d_route` = route-support demand
- `d_urg` = urgent support demand
- `d_fail` = failure burden or unresolved incident demand
- `St_t` = stabilization bundle
- `b_t` = breach field
- `k_t` = lock field
- `p_t` = patch field
- `iso_t` = isolation field
- `Cl_t` = clearance bundle
- `w_t` = debris or waste load
- `q_t` = quarantine load
- `g_t` = cleanup progress
- `m_t^clr` = clearance memory or incident history

### Blood-health notation

- `Hb_t` = blood-health vector
- `h_flow` = flow health
- `h_sludge` = congestion or sludge risk
- `h_clot` = clotting or over-sealing risk
- `h_inf` = inflammatory load
- `h_clear` = clearance debt
- `h_auto` = autoimmune or self-damaging support risk

### Payload notation

```text
π_t^(i) = (k_i, p_i, f_i, u_i, g_i, ttl_i)
```

- `π_t^(i)` = packet `i` at time `t`
- `k_i` = packet kind or type
- `p_i` = packet payload
- `f_i` = freshness score
- `u_i` = urgency score
- `g_i` = destination, target, or route-group tag
- `ttl_i` = time-to-live or expiry budget

## Interface Maps And Operators

### Read-side maps

- `ReadCtx(x_t, G_t, A_t, Pl_t, M_t)` = organism-conditioned context read
- `InputCompose(y_t, c_t)` = input assembly operator combining outer input and internal context

### Write-side maps

- `ψ_write` = substrate-to-memory or body write map
- `ψ_emit` = substrate-to-action or output dispatch map
- `ψ_bias` = substrate-to-nervous-posture bias map
- `TissueCouple` = inter-tissue coupling map between governance, nervous, and blood subsystems

### Update operators

- `SubstrateUpdate` = update law for `D_t`
- `GovernanceUpdate` = update law for `Ψ_t`
- `NervousUpdate` = update law for `Σ_t`
- `BloodUpdate` = update law for `B_t`
- `EventPolicy` = discrete event-generation or event-selection operator
- `PlasticityUpdate` = structural-learning operator for `θ_t` and `ω_t`

## Constraint And Barrier Symbols

- `X_safe` = viable organism set
- `𝒪_t ∈ X_safe` = organism state must remain in viability envelope
- `Π_consistency(D_t, Ξ_t)` = consistency condition between substrate and organism-visible projection
- `PlasticityAllowed_t` = binary plasticity gate at time `t`
- `Φ_org(𝒪_t)` = total organism barrier or viability potential
- `Φ_sub(D_t)` = substrate barrier or health penalty
- `Φ_gov(Ψ_t)` = governance barrier or health penalty
- `Φ_sig(Σ_t)` = nervous-system barrier or health penalty
- `Φ_sup(B_t)` = blood-system barrier or health penalty

## Objective Symbols

- `L_task` = task-performance loss
- `λ_D` = substrate penalty weight
- `λ_Ψ` = governance penalty weight
- `λ_Σ` = nervous-system penalty weight
- `λ_B` = blood-system penalty weight
- `E[...]` = expectation over task stream, trajectories, or operating distribution

## Modes

- `homeostasis` = normal viability-preserving operation
- `adaptive` = bounded adaptive change while remaining healthy
- `inflammatory` = escalated defensive mode under rising burden
- `pathological` = degraded mode where normal regulation is failing
- `regenerative` = repair or rebuild mode after significant failure or injury

## Event Families

- `𝓔_gov` = governance-event family
- `𝓔_sig` = nervous signaling-event family
- `𝓔_sup` = support and blood-event family

Examples already used in the packet:

- governance: `spawn_branch`, `quarantine_branch`, `promote_branch`, `trigger_regeneration`
- signaling: route burst, signal seizure, grounding failure, autonomic drift
- support: anemia, sludge, clot, chronic inflammation, clearance failure

## Timescale Symbols

```text
𝓣 = (τ_alpha, τ_sigma, τ_blood, τ_gov, τ_theta)
```

- `τ_alpha` = substrate activation timescale
- `τ_sigma` = nervous-system timescale
- `τ_blood` = blood-system timescale
- `τ_gov` = governance timescale
- `τ_theta` = structural-learning timescale

Canonical ordering:

```text
τ_alpha << τ_sigma << τ_blood << τ_gov << τ_theta
```

## Collision Rules

These rules should be followed going forward:

- use `alpha_t` for fast activation state, not `a_t`
- reserve `a_t` for governance action
- use `𝒪_t` for the full organism state in basis-level writing
- use `Ξ_t` only for the organism-visible core bundle, not the whole organism
- use `Σ_t` only for nervous tissue
- use `B_t` only for blood tissue
- use `Π_*` for projections, not generic transforms
- use `Φ_*` for viability barriers, not arbitrary losses
- use `L_*` for optimization losses

## Recommended Reading Order

If someone is new to the packet, the clean order is:

1. `ORGANISMIC_INTELLIGENCE_MATHEMATICAL_BASIS.md`
2. `SYMBOLS_AND_NOTATION_GLOSSARY.md`
3. `DIFFERENTIABLE_SUBSTRATE_AND_ORGANISM_INTEGRATION.md`
4. `VIRTUAL_NERVOUS_SYSTEM_MATHEMATICAL_EXTENSION.md`
5. `VIRTUAL_BLOOD_SYSTEM_MATHEMATICAL_EXTENSION.md`
6. `LIVING_RESEARCH_MATHEMATICAL_EXTENSION.md`

## Final Rule

When a later document introduces a new symbol, it should do one of two things:

- define a genuinely new object and add it here later, or
- express the idea using the existing notation in this glossary.

That prevents the packet from drifting into multiple incompatible mathematical dialects.
