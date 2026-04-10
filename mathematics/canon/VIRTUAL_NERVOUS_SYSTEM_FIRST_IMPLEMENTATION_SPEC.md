# Virtual Nervous System: First Implementation Spec

Updated: `2026-04-05`

## Purpose

This document turns `VIRTUAL_NERVOUS_SYSTEM_MATHEMATICAL_EXTENSION.md` into a first practical implementation plan.

It answers seven concrete questions:

1. what should count as the first afferent field `A_t`,
2. what the first local integration state `J_t` should look like,
3. how commitment gates `K_t` should work in `v1`,
4. what the first route state `P_t` should contain,
5. how efferent and autonomic dispatch `E_t` should be represented,
6. how neuromodulation `M_t` and neural health `H_t` should be computed,
7. how the nervous-system layer should wrap around the existing organism controller and living-research layer without breaking them.

This is the first implementation layer for the new nervous-system extension.

## Design Rule

The first implementation should follow this rule:

```text
preserve the current organism controller,
preserve the living-research governance layer,
add a small fast-signaling layer around them,
instrument typed signals and route state first,
replace summaries with richer neural lineages later
```

That means:

- do not rewrite the controller first,
- do not try to build a full virtual CNS in one pass,
- start with measurable signal summaries,
- and grow into richer worker lineages only after the state is visible.

## Target Runtime Stack

The runtime stack should now be read as:

```text
request / sensor change
-> collect afferent events
-> derive interoceptive signals from organism + living-research + blood state
-> build local junction summaries
-> compute commitment-gate outputs
-> choose projection routes
-> dispatch action and autonomic outputs
-> update neuromodulators
-> update nervous-system health
-> continue organism-level inference/control cycle
-> persist nervous-system state
```

This places the nervous layer around the current controller without replacing it.

## What Stays From The Current Stack

The current implementation path should remain intact for:

- `Ξ_t`
- `ρ_t`
- `Λ_t`
- `N_t`
- `m_t`
- `a_t`
- current `steady / guarded / repair / preserve` controller behavior

Those remain the organism and living-research layers.

The new nervous layer should sit beside them.

## First Version Of Afferent Field `A_t`

The first implementation should use a small fixed typed afferent set.

Use:

```text
A_t = (A_user, A_mem, A_health, A_err, A_gov)
```

### `A_user`

Definition:

- external user or operator-originated events

First proxy:

- current user prompt
- tool result arrivals
- external webhook or operator command events when available

### `A_mem`

Definition:

- memory-body and retrieval-originated events

First proxy:

- retrieval hits
- working-memory summary changes
- graph-pathway activation summaries

### `A_health`

Definition:

- interoceptive organism-state signals

First proxy:

- current control regime
- capacity pressure
- working-memory pressure
- reserve summary
- blood-layer alerts once available

### `A_err`

Definition:

- anomaly and failure signals

First proxy:

- tool failures
- timeout counts
- contradiction flags
- retry pressure

### `A_gov`

Definition:

- living-research governance and branch-ecology alerts

First proxy:

- current mode
- quarantine events
- promotion decisions
- pathology or regeneration alerts

## First Version Of Local Integration State `J_t`

The first implementation does not need full neural microcircuits.
It needs a small fixed region registry with summary values.

Use:

```text
R = { ingress, memory, controller, action, maintenance }
```

with:

```text
J_t^(r) = (e_r, i_r, c_r, s_r)
```

where:

- `e_r` = excitatory evidence score
- `i_r` = inhibitory or suppression score
- `c_r` = context accumulation score
- `s_r` = salience score

### First regional interpretations

#### `ingress`

- fuses user, operator, and external input pressure

#### `memory`

- fuses retrieval, working-memory, and graph activation pressure

#### `controller`

- fuses control-state pressure, reserve pressure, and governance pressure

#### `action`

- fuses outgoing execution and reply pressure

#### `maintenance`

- fuses cleanup, retry, repair, and autonomic regulation pressure

## First Version Of Commitment Gates `K_t`

The first implementation should explicitly track threshold and refractory behavior.

Use:

```text
K_t^(r) = (d_r, θ_r, γ_r, o_r)
```

where:

- `d_r` = integrated local drive
- `θ_r` = firing threshold
- `γ_r` = refractory debt
- `o_r` = committed output event count or indicator

### First gate logic

Suggested first rule:

```text
d_r = e_r - i_r + c_r + s_r + b_r(M_t)
```

```text
o_r = 1[d_r > θ_r] 1[γ_r < γ_max]
```

```text
γ_r(next) = λ_γ γ_r + o_r
```

Interpretation:

- local evidence and salience push the region toward commitment,
- inhibition and refractory debt push it away,
- global modulation can bias the thresholding process.

## First Version Of Route State `P_t`

The first implementation should make routes explicit.

Use:

```text
P_t = (routes, latencies, trust, insulation)
```

### `routes`

Recommended first route set:

- `ingress -> controller`
- `ingress -> memory`
- `memory -> controller`
- `controller -> action`
- `controller -> maintenance`
- `maintenance -> controller`

That is enough for `v1`.

### `latencies`

Definition:

- observed or estimated time-to-delivery for each route

First proxy:

- rolling average event-processing latency by route

### `trust`

Definition:

- how reliable and semantically clean each route is

First proxy:

- success ratio
- contradiction ratio
- stale-signal ratio

### `insulation`

Definition:

- promotion state for routes repeatedly used successfully under timing pressure

First proxy:

- exponentially weighted usage score with degradation on repeated failures

## First Version Of Efferent Dispatch State `E_t`

The first implementation should separate outward action from inward regulation.

Use:

```text
E_t = (E_act, E_auto, F_ack)
```

### `E_act`

Definition:

- outward deliberate action dispatch

First proxy:

- assistant replies
- tool-call dispatches
- memory-write requests
- branch-governance execution requests

### `E_auto`

Definition:

- internal autonomic regulation outputs

First proxy:

- compute-throttle suggestion
- retry-throttle suggestion
- quiet-mode request
- reserve-protection request

### `F_ack`

Definition:

- action acknowledgement and feedback summary

First proxy:

- success or failure of recent dispatches
- timeout counts
- downstream confirmation availability

## First Version Of Neuromodulatory State `M_t`

The first implementation should use a small explicit vector.

Use:

```text
M_t = [novelty, threat, urgency, focus, exploration]^T
```

### `novelty`

Increase when:

- unfamiliar request patterns appear
- retrieval mismatch rises
- new branches or tasks are opened

### `threat`

Increase when:

- failures cluster
- reserve drops
- governance enters inflammatory or pathological modes

### `urgency`

Increase when:

- deadlines tighten
- repeated high-priority signals arrive
- unresolved errors persist

### `focus`

Increase when:

- one route or task context dominates with high confidence

### `exploration`

Increase when:

- organism state is healthy
- reserves are adequate
- novelty is high without corresponding threat

## First Version Of Neural Health State `H_t`

The first implementation should keep neural health small and measurable.

Use:

```text
H_t = [exc_pressure, flood_risk, route_stress, grounding_risk, auto_drift]^T
```

### `exc_pressure`

Definition:

- pressure from too many high-drive regions at once

First proxy:

- count of regions with `d_r > θ_r`

### `flood_risk`

Definition:

- risk of pathological alert or event storms

First proxy:

- rolling burst count of committed events
- ratio of propagated events to suppressed events

### `route_stress`

Definition:

- stress from latency and trust degradation

First proxy:

- blend of latency inflation and trust decay across active routes

### `grounding_risk`

Definition:

- risk that internally generated signals are outrunning grounded afferent evidence

First proxy:

- ratio of memory- or simulation-originated events to external and interoceptive confirmation

### `auto_drift`

Definition:

- internal regulation drifting away from viable posture

First proxy:

- magnitude and persistence of autonomic output requests

## Required New Data Structures

The first implementation should add five new durable structures.

### 1. `nervous_system_state`

Recommended fields:

- `id`
- `afferent_summary`
- `junction_summary`
- `gate_summary`
- `route_summary`
- `dispatch_summary`
- `modulator_summary`
- `health_summary`
- `created_at`

### 2. `afferent_events`

Recommended fields:

- `event_id`
- `event_type`
- `source`
- `priority`
- `target_region`
- `payload_summary`
- `created_at`

### 3. `route_registry`

Recommended fields:

- `route_id`
- `source_region`
- `target_region`
- `latency_summary`
- `trust_summary`
- `insulation_summary`
- `last_used_at`

### 4. `dispatch_events`

Recommended fields:

- `dispatch_id`
- `dispatch_type`
- `target`
- `status`
- `feedback_summary`
- `created_at`

### 5. `modulator_history`

Recommended fields:

- `id`
- `novelty`
- `threat`
- `urgency`
- `focus`
- `exploration`
- `created_at`

## Required New APIs

The future main system should expose:

- `/api/nervous-system-state`
- `/api/afferent-events`
- `/api/routes`
- `/api/dispatch-events`
- `/api/modulators`

These should sit beside:

- `/api/control-state`
- `/api/living-research-state`
- `/api/capacity`

The old APIs remain organism-level or population-level.
The new APIs are fast-signaling-layer APIs.

## First Policy Mapping

### Balanced posture

- ordinary thresholding
- normal inhibition
- normal route promotion
- normal action dispatch

### Focused posture

- raise `focus`
- narrow route use
- suppress low-salience propagation
- favor controller-to-action integrity

### Threat posture

- raise `threat`
- lower tolerance for anomalous events
- raise autonomic reserve-protection outputs
- suppress exploratory routing

### Exploratory posture

- raise `novelty` and `exploration`
- widen route use carefully
- allow more memory-to-controller signaling
- keep flood-risk checks stricter

### Recovery posture

- favor maintenance routes
- suppress nonessential outward action
- reduce urgency unless externally forced
- prioritize cleanup and route repair

## First Runtime Sequence

The full sequence should be:

```text
1. Read current organism control state Ξ_t
2. Read living-research state Ψ_t summaries
3. Build typed afferent field A_t
4. Build region-local junction summaries J_t
5. Compute gate outputs K_t with thresholds and refractory debt
6. Update route state P_t and choose active projections
7. Dispatch E_t^act and E_t^auto outputs
8. Update neuromodulator vector M_t
9. Update neural health H_t
10. Persist nervous_system_state and route / dispatch records
11. Continue outer organism and governance cycle
```

This makes the nervous layer a fast loop around the existing organism.

## Minimal Code Integration Plan

The first code pass should be small and layered.

### Step 1

Add:

```text
build_afferent_field(request, control_state, living_research_state, runtime_state)
```

This returns `A_t`.

### Step 2

Add:

```text
build_junction_state(A_t, memory_state, controller_state)
```

This returns `J_t`.

### Step 3

Add:

```text
compute_commitment_gates(J_t, M_t, prev_gate_state)
```

This returns `K_t`.

### Step 4

Add:

```text
update_route_state(K_t, prev_route_state, M_t, H_t)
```

This returns `P_t`.

### Step 5

Add:

```text
build_dispatch_state(P_t, control_decisions, governance_actions)
```

This returns `E_t`.

### Step 6

Add:

```text
update_modulators(A_t, Ψ_t, prev_modulators)
```

This returns `M_t`.

### Step 7

Add:

```text
update_neural_health(A_t, J_t, K_t, P_t, E_t, M_t)
```

This returns `H_t`.

### Step 8

Persist:

```text
nervous_system_state
afferent_events
route_registry
dispatch_events
modulator_history
```

## What Stays As V2

The following should not block `v1`:

- true oscillatory phase scheduling instead of summary timing windows
- richer region graph beyond the fixed small registry
- full glial services
- learned threshold adaptation
- native neural worker lineages with dedicated services
- direct coupling to a fully built virtual blood layer
- full hybrid solver for nervous-layer coupling inside `𝒪_t = (D_t, Ψ_t, Σ_t, B_t)`

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
  adapters/triune_adapter.py
```

Responsibility split:

- `afferents.py` computes `A_t`
- `junctions.py` computes `J_t`
- `gates.py` computes `K_t`
- `routes.py` computes `P_t`
- `effectors.py` computes `E_t`
- `modulators.py` computes `M_t`
- `health.py` computes `H_t`

## Final Statement

The first implementation should not attempt a whole synthetic nervous system in one pass.

It should:

```text
keep the current organism controller,
keep the living-research governance layer,
make typed afferents explicit,
make local integration explicit,
make thresholded commitment explicit,
make route health explicit,
make diffuse modulation explicit,
and keep the whole fast-signaling layer subordinate to organism homeostasis
```

That is the correct first implementation form of the virtual nervous-system mathematical extension.
