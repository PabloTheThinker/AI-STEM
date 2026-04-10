# Virtual Blood System: First Implementation Spec

Updated: `2026-04-05`

## Purpose

This document turns `VIRTUAL_BLOOD_SYSTEM_MATHEMATICAL_EXTENSION.md` into a first practical implementation plan.

It answers seven concrete questions:

1. what should count as the first plasma and circulation state `Pl_t`,
2. what the first marrow state `Ma_t` should look like,
3. how the first blood-lineage state `Li_t` should be represented,
4. what the first delivery, stabilization, and clearance states should contain,
5. how blood health `Hb_t` should be computed,
6. which data structures and APIs should exist in `v1`,
7. how the blood-system layer should wrap around the existing organism, living-research, and nervous-system layers without breaking them.

This is the first implementation layer for the new blood-system extension.

## Design Rule

The first implementation should follow this rule:

```text
preserve the current organism controller,
preserve the living-research governance layer,
preserve the nervous-system signaling layer,
add a small circulatory support layer around them,
instrument delivery, stabilization, and clearance summaries first,
replace summaries with richer blood lineages later
```

That means:

- do not rewrite the controller first,
- do not try to build the full blood ecology in one pass,
- start with a small support-lineage set,
- and grow into richer patrol and defense-memory lineages later.

## Target Runtime Stack

The runtime stack should now be read as:

```text
request / runtime change
-> read organism, governance, and nervous-system summaries
-> build support demand and payload packets
-> update marrow targets and spawn budget
-> update active support lineages
-> deliver payload packets
-> apply local stabilization if breaches exist
-> run cleanup and clearance passes
-> update blood-system health
-> persist blood-system state
-> continue outer organism and signaling cycles
```

This places the blood layer around the current controller without replacing it.

## What Stays From The Current Stack

The current implementation path should remain intact for:

- `Ξ_t`
- `ρ_t`
- `Λ_t`
- `N_t`
- `m_t`
- `a_t`
- `Σ_t`
- current `steady / guarded / repair / preserve` controller behavior

Those remain the organism, governance, and signaling layers.

The new blood layer should sit beside them.

## First Version Of Plasma And Circulation State `Pl_t`

The first implementation should use a small explicit circulation summary.

Use:

```text
Pl_t = (payload_queue, flow_pressure, freshness_pressure, route_exposure)
```

### `payload_queue`

Definition:

- active packets moving through the support layer

First proxy:

- compressed context summaries
- route-health summaries
- reserve and health summaries
- repair tickets
- urgency packets

### `flow_pressure`

Definition:

- current throughput load on the circulation layer

First proxy:

- packet count
- average packet size
- backlog depth

### `freshness_pressure`

Definition:

- stale or aging payload burden

First proxy:

- fraction of packets near expiration
- fraction of packets delivered after usefulness window

### `route_exposure`

Definition:

- which organism routes and subsystems the blood layer can currently service

First proxy:

- route registry overlap with the nervous-system layer
- reachable subsystem set

## First Version Of Marrow State `Ma_t`

The first implementation should make production targets explicit.

Use:

```text
Ma_t = (targets, spawn_budget, demand_bias, template_health)
```

### `targets`

Definition:

- desired counts or intensity levels for each active lineage

First proxy:

- target `vRBC` count
- target `vPlatelet` count
- target `vNeutrophil` count
- target `vMacrophage` count

### `spawn_budget`

Definition:

- how much support-worker generation is safe this cycle

First proxy:

- function of reserve state `ρ_t`
- function of current homeostatic mode `m_t`

### `demand_bias`

Definition:

- mode and incident pressure that alters lineage production

First proxy:

- transport demand
- breach count
- anomaly count
- cleanup debt

### `template_health`

Definition:

- integrity of worker templates and spawn logic

First proxy:

- template availability
- template version match
- recent spawn success

## First Version Of Blood-Lineage State `Li_t`

The first implementation should start with the conservative four-lineage set.

Use:

```text
Li_t = [l_rbc, l_plt, l_neu, l_mac]^T
```

where:

- `l_rbc` = virtual erythrocyte count or intensity
- `l_plt` = virtual platelet count or intensity
- `l_neu` = virtual neutrophil count or intensity
- `l_mac` = virtual macrophage count or intensity

### `l_rbc`

Role:

- high-volume support transport

First proxy:

- number of active courier workers
- or delivery throughput budget

### `l_plt`

Role:

- local interface stabilization

First proxy:

- number of active boundary-stabilizer workers
- or number of allowed temporary locks

### `l_neu`

Role:

- short-lived anomaly containment

First proxy:

- burst responder count
- or bounded anomaly-response budget

### `l_mac`

Role:

- persistent cleanup and repair coordination

First proxy:

- cleanup worker count
- or cleanup throughput budget

## First Version Of Delivery State `De_t`

The first implementation should make delivery outcomes measurable.

Use:

```text
De_t = (ctx_ok, health_ok, route_ok, urgent_ok, fail_burden)
```

### `ctx_ok`

Definition:

- success of context-packet delivery

### `health_ok`

Definition:

- success of health and reserve summary delivery

### `route_ok`

Definition:

- success of route and integrity summary delivery

### `urgent_ok`

Definition:

- success of urgent or high-priority packet delivery

### `fail_burden`

Definition:

- failed, stale, or dropped support-packet burden

## First Version Of Stabilization State `St_t`

The first implementation should track local breach handling explicitly.

Use:

```text
St_t = (open_breaches, active_locks, patch_markers, isolated_routes)
```

### `open_breaches`

Definition:

- unresolved boundary or interface breaks

### `active_locks`

Definition:

- temporary locks and write throttles applied by platelet-like workers

### `patch_markers`

Definition:

- temporary fallback or repair markers in the local tissue

### `isolated_routes`

Definition:

- routes currently walled off for safety

## First Version Of Clearance State `Cl_t`

The first implementation should track cleanup debt explicitly.

Use:

```text
Cl_t = (debris_load, quarantine_load, cleanup_progress, incident_memory)
```

### `debris_load`

Definition:

- stale context, dead worker state, and obsolete artifacts waiting for digestion

### `quarantine_load`

Definition:

- amount of isolated or quarantined material awaiting resolution

### `cleanup_progress`

Definition:

- progress made by macrophage-like cleanup activity

### `incident_memory`

Definition:

- compressed summary of resolved incidents and cleanup outcomes

## First Version Of Blood Health State `Hb_t`

The first implementation should keep blood health small and measurable.

Use:

```text
Hb_t = [flow_health, sludge_risk, clot_risk, inflammation_load, clearance_debt]^T
```

### `flow_health`

Definition:

- adequacy of delivery throughput relative to demand

First proxy:

- blend of `ctx_ok`, `health_ok`, `route_ok`, and backlog pressure

### `sludge_risk`

Definition:

- stale-payload and low-value circulation burden

First proxy:

- freshness pressure
- failed-delivery burden

### `clot_risk`

Definition:

- risk of over-locking and chronic sealing

First proxy:

- number and duration of active locks
- number of isolated routes

### `inflammation_load`

Definition:

- burden from emergency responder activity

First proxy:

- current `l_neu`
- anomaly counts
- unresolved breach counts

### `clearance_debt`

Definition:

- burden from insufficient cleanup

First proxy:

- debris load
- quarantine load
- cleanup progress deficit

## Required New Data Structures

The first implementation should add five new durable structures.

### 1. `blood_system_state`

Recommended fields:

- `id`
- `plasma_summary`
- `marrow_summary`
- `lineage_summary`
- `delivery_summary`
- `stabilization_summary`
- `clearance_summary`
- `health_summary`
- `created_at`

### 2. `payload_packets`

Recommended fields:

- `packet_id`
- `packet_type`
- `target_zone`
- `freshness`
- `urgency`
- `status`
- `created_at`

### 3. `support_worker_registry`

Recommended fields:

- `worker_id`
- `lineage`
- `status`
- `target_zone`
- `ttl`
- `outcome_summary`
- `created_at`

### 4. `stabilization_events`

Recommended fields:

- `event_id`
- `breach_type`
- `lock_summary`
- `patch_summary`
- `route_isolation_summary`
- `created_at`

### 5. `clearance_events`

Recommended fields:

- `event_id`
- `debris_summary`
- `quarantine_summary`
- `cleanup_outcome`
- `incident_memory_summary`
- `created_at`

## Required New APIs

The future main system should expose:

- `/api/blood-system-state`
- `/api/payload-packets`
- `/api/support-workers`
- `/api/stabilization-events`
- `/api/clearance-events`

These should sit beside:

- `/api/control-state`
- `/api/living-research-state`
- `/api/nervous-system-state`
- `/api/capacity`

The old APIs remain organism-level, population-level, or signaling-level.
The new APIs are support-tissue APIs.

## First Policy Mapping

### Homeostatic support posture

- favor `vRBC`
- keep `vPlatelet` low
- keep `vNeutrophil` low
- run steady cleanup

### Adaptive support posture

- increase `vRBC`
- allow moderate retuning of delivery priorities
- increase cleanup if novelty creates more debris

### Inflammatory support posture

- increase `vPlatelet`
- increase `vNeutrophil`
- isolate noisy routes quickly
- suppress nonessential transport

### Pathological support posture

- preserve only critical payload delivery
- reduce new worker generation except support essentials
- prioritize breach containment and reserve conservation

### Regenerative support posture

- favor `vMacrophage`
- favor repair tickets and rebuild summaries
- bias marrow toward reconstruction support rather than bulk transport

## First Runtime Sequence

The full sequence should be:

```text
1. Read current organism control state Ξ_t
2. Read living-research state Ψ_t summaries
3. Read nervous-system state Σ_t summaries when available
4. Build payload queue and circulation summary Pl_t
5. Compute marrow targets Ma_t from mode, reserve, demand, and incidents
6. Update active lineage populations Li_t
7. Update delivery outcomes De_t
8. Apply stabilization logic St_t for active breaches
9. Run cleanup and digestion logic Cl_t
10. Update blood health Hb_t
11. Persist blood_system_state and worker / event records
12. Continue outer organism and signaling cycles
```

This makes the blood layer a support loop around the existing organism.

## Minimal Code Integration Plan

The first code pass should be small and layered.

### Step 1

Add:

```text
build_plasma_state(control_state, nervous_state, runtime_state)
```

This returns `Pl_t`.

### Step 2

Add:

```text
compute_marrow_state(Ψ_t, Σ_t, prev_blood_state)
```

This returns `Ma_t`.

### Step 3

Add:

```text
update_blood_lineages(Ma_t, prev_lineages, incidents)
```

This returns `Li_t`.

### Step 4

Add:

```text
update_delivery_state(Pl_t, Li_t, Σ_t, Ψ_t)
```

This returns `De_t`.

### Step 5

Add:

```text
update_stabilization_state(Li_t, breach_state, nervous_state)
```

This returns `St_t`.

### Step 6

Add:

```text
update_clearance_state(Li_t, St_t, prev_clearance_state)
```

This returns `Cl_t`.

### Step 7

Add:

```text
update_blood_health(Pl_t, Li_t, De_t, St_t, Cl_t)
```

This returns `Hb_t`.

### Step 8

Persist:

```text
blood_system_state
payload_packets
support_worker_registry
stabilization_events
clearance_events
```

## What Stays As V2

The following should not block `v1`:

- explicit monocyte patrol and conversion logic
- lymphocyte and durable defense-memory lineages
- richer barrier modulators analogous to eosinophils and basophils
- spleen and liver filtering as distinct subsystems
- tighter cross-coupling to a fully built nervous-system implementation
- learned marrow retargeting
- full hybrid solver for blood-layer coupling inside `𝒪_t = (D_t, Ψ_t, Σ_t, B_t)`

These belong to `v2`.

## File / Module Recommendation

The future main system should extend its module layout to:

```text
main_system/
  state_estimator.py
  capacity.py
  policy.py
  orchestrator.py
  living_research/
    reserve.py
    lineage.py
    niches.py
    modes.py
    governance.py
  nervous_system/
    afferents.py
    junctions.py
    gates.py
    routes.py
    effectors.py
    modulators.py
    health.py
  blood_system/
    plasma.py
    marrow.py
    lineages.py
    delivery.py
    stabilization.py
    clearance.py
    health.py
  adapters/triune_adapter.py
```

Responsibility split:

- `plasma.py` computes `Pl_t`
- `marrow.py` computes `Ma_t`
- `lineages.py` computes `Li_t`
- `delivery.py` computes `De_t`
- `stabilization.py` computes `St_t`
- `clearance.py` computes `Cl_t`
- `health.py` computes `Hb_t`

## Final Statement

The first implementation should not attempt a full synthetic hematopoietic ecology in one pass.

It should:

```text
keep the current organism controller,
keep the living-research governance layer,
keep the nervous-system signaling layer,
make circulation explicit,
make marrow targeting explicit,
make support lineages explicit,
make delivery, sealing, and clearance explicit,
and keep the whole blood layer subordinate to organism homeostasis
```

That is the correct first implementation form of the virtual blood-system mathematical extension.
