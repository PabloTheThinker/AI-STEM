# Living Research: First Implementation Spec

Updated: `2026-04-05`

## Purpose

This document turns `LIVING_RESEARCH_MATHEMATICAL_EXTENSION.md` into a first practical implementation plan.

It answers six concrete questions:

1. what the first implementation should count as reserve state `ρ_t`,
2. what should count as lineage population state `Λ_t`,
3. what the first niche state `N_t` should look like,
4. how the richer homeostatic mode `m_t` should be computed,
5. which discrete governance actions `a_t` should exist in `v1`,
6. how this should wrap around the existing organism controller without breaking it.

This is the first implementation layer above the new extension.

## Design Rule

The first implementation should follow this rule:

```text
preserve the current organism controller,
add population and governance layers around it,
instrument with explicit summaries first,
replace summaries with native lineages and niche services later
```

That means:

- do not rewrite the runtime controller first,
- add a small outer governance layer,
- start with measurable proxies,
- move to richer branch ecology only after the state is visible.

## Target Runtime Stack

The runtime stack should now be read as:

```text
request
-> organism pre-state estimate
-> organism regime / policy selection
-> inference / retrieval / memory path
-> organism post-state estimate
-> reserve update
-> lineage update
-> niche policy update
-> discrete governance action selection
-> maintenance / branch / promotion decisions
-> persist living research state
```

This keeps the existing control loop while placing a research-organism governance layer above it.

## What Stays From The Current Stack

The current implementation path should remain intact for:

- `r_t`
- `x_t`
- `q_t`
- current `steady / guarded / repair / preserve` controller behavior

Those are already useful and should remain the organism controller.

The new layer should sit above them.

## First Version Of Reserve State `ρ_t`

The first version should be explicit and simple.

Use:

```text
ρ_t = [ρ_roll, ρ_base, ρ_comp, ρ_mem, ρ_rec]^T
```

### `ρ_roll` rollback reserve

Definition:

- count and freshness of rollback points available to the current system

First proxy:

- recent control-state snapshots available
- recent known-good checkpoints available

Suggested normalization:

```text
ρ_roll = sat(checkpoint_count_recent; 5)
```

### `ρ_base` baseline reserve

Definition:

- integrity of trusted baselines the organism can return to

First proxy:

- presence of at least one trusted baseline branch or known-good config
- last successful reproduction of the baseline

Suggested first version:

```text
ρ_base = clip(0.6 baseline_exists + 0.4 baseline_repro_success)
```

### `ρ_comp` compute reserve

Definition:

- safe compute headroom available for exploration or recovery

First proxy:

- complement of controller load pressure
- optional wall-clock / queue-pressure metrics once instrumented

Suggested first version:

```text
ρ_comp = clip(1 - normalized_compute_pressure)
```

### `ρ_mem` memory reserve

Definition:

- working-memory and persistence slack before overload

First proxy:

- complement of working-memory saturation
- storage pressure if available

Suggested first version:

```text
ρ_mem = clip(1 - sat(working_memory_items; 8))
```

### `ρ_rec` recovery reserve

Definition:

- capacity for stabilization and rebuild if ordinary operation fails

First proxy:

- blend of `ρ_roll`, `ρ_base`, and `ρ_comp`

Suggested first version:

```text
ρ_rec = clip(0.4 ρ_roll + 0.3 ρ_base + 0.3 ρ_comp)
```

## First Version Of Lineage Population State `Λ_t`

The first implementation does not need a full branch orchestration service.
It needs a durable ledger and a small health model.

Use:

```text
Λ_t = (B_t, A_t, K_t, C_t)
```

where:

- `B_t` = active branch summaries
- `A_t` = archived branch summaries
- `K_t` = branch health summaries
- `C_t` = local comparison state

### Active branch summary

Each branch should minimally store:

```text
b_t^(i) = [branch_id, parent_id, niche, created_at, status]
```

with `status ∈ {active, quarantined, archived, promoted, killed}`.

### Branch health summary

For each branch `i`, compute:

```text
k_t^(i) = [f_i, h_i, c_i, d_i, r_i]^T
```

where:

- `f_i` = fitness score
- `h_i` = harness integrity score
- `c_i` = complexity burden score
- `d_i` = drift / instability score
- `r_i` = reproducibility status

#### `f_i` fitness

Use:

- benchmark delta if branch is experimental
- task success delta if benchmark is unavailable

#### `h_i` harness integrity

Use:

- whether forbidden surfaces changed
- whether required eval path remained fixed
- whether dataset / budget / environment were declared

#### `c_i` complexity burden

Use first proxies:

- changed-file count
- diff-size count
- new coupling or dependency flags if available

#### `d_i` drift

Use:

- deviation from parent baseline behavior
- failure / contradiction / instability pressure

#### `r_i` reproducibility

Boolean or score:

- exact run config captured
- exact command captured
- rerun success available

### Competition state `C_t`

The first version can be minimal:

```text
C_t = { comparison_groups, current_winners }
```

where a comparison group contains branches that share:

- same niche
- same baseline parent
- same evaluation harness

That is enough for `v1`.

## First Version Of Niche State `N_t`

The first implementation should use a small fixed niche registry.

Use:

```text
N_t = { optimizer, architecture, data_quality, evaluation, deployment }
```

Each niche should carry:

```text
N_t^(k) = (χ_k, U_k, β_k, θ_k, risk_k)
```

where:

- `χ_k` = local objective
- `U_k` = allowed mutation / action surface
- `β_k` = budget profile
- `θ_k` = promotion threshold
- `risk_k` = risk class

### First niche definitions

#### `optimizer`

- objective: improve fitness under fixed architecture
- allowed surface: optimizer, scheduler, numeric hyperparameters
- risk: low-medium

#### `architecture`

- objective: improve structure or representational capacity
- allowed surface: architecture and control interfaces only
- risk: high

#### `data_quality`

- objective: improve data integrity and fit
- allowed surface: data-processing and dataset-selection layers
- risk: medium

#### `evaluation`

- objective: improve measurement quality
- allowed surface: evaluation tooling only, with stronger review
- risk: very high because of metric gaming risk

#### `deployment`

- objective: improve robustness and runtime fit
- allowed surface: deployment and integration layers
- risk: medium-high

## First Version Of Homeostatic Mode `m_t`

The first implementation should explicitly track:

```text
m_t ∈ { homeostasis, adaptive, inflammatory, pathological, regenerative }
```

This should sit above the current runtime regimes.

### Mapping from current controller regimes

The first bridging map should be:

- `steady` -> `homeostasis`
- `guarded` -> `adaptive`
- `repair` -> `inflammatory`
- `preserve` -> `pathological`

`regenerative` should be added only at the outer governance layer.

### First mode logic

Use organism health, reserve, and lineage health together.

Suggested first rule:

#### `homeostasis`

when:

- organism regime is `steady`
- reserve is healthy
- no serious lineage pathology is present

#### `adaptive`

when:

- organism regime is `guarded`
- reserve remains healthy enough for local exploration
- no quarantine condition is active

#### `inflammatory`

when:

- organism regime is `repair`
- or a branch-integrity threat requires containment

#### `pathological`

when:

- organism regime is `preserve`
- or branch ecology remains unhealthy across repeated cycles
- or reserve drops below safety threshold

#### `regenerative`

when:

- `pathological` persists,
- local repair repeatedly fails,
- and `ρ_rec` remains above minimum rebuild threshold

## First Version Of Discrete Governance Action `a_t`

The first implementation should define a small real action set:

```text
a_t ∈
{
  noop,
  spawn_branch,
  quarantine_branch,
  archive_branch,
  kill_branch,
  promote_branch,
  trigger_regeneration
}
```

`restore_homeostasis` does not need to be a first-class action in `v1`.
It can be represented by returning to `noop` under normal mode.

### `spawn_branch`

Allow only if:

- current mode is `homeostasis` or `adaptive`
- `ρ_comp` is healthy
- `ρ_base` is healthy
- branch count is below limit

### `quarantine_branch`

Use when:

- branch harness integrity falls below threshold
- metric jump is suspicious
- forbidden surfaces changed
- reproducibility metadata is missing

### `archive_branch`

Use when:

- branch is no longer active
- branch is not dangerous
- branch should be kept as lineage memory but removed from active load

### `kill_branch`

Use when:

- repeated failure continues
- harness integrity remains broken
- drift / complexity burden exceeds limits with no gain

### `promote_branch`

Use only if:

- branch fitness exceeds threshold
- branch integrity is preserved
- reproducibility passes
- promotion does not violate organism viability

### `trigger_regeneration`

Use only if:

- mode is `pathological`
- repeated local repair attempts failed
- no promotable branch exists
- `ρ_rec` is above rebuild threshold

## Required New Data Structures

The first implementation should add four new durable structures.

### 1. `living_research_state`

This is the top-level governance snapshot.

Recommended fields:

- `id`
- `mode`
- `reserve_summary`
- `lineage_summary`
- `niche_summary`
- `governance_action`
- `created_at`

### 2. `branch_registry`

Recommended fields:

- `branch_id`
- `parent_branch_id`
- `niche`
- `status`
- `fitness_summary`
- `integrity_summary`
- `complexity_summary`
- `drift_summary`
- `repro_summary`
- `created_at`
- `updated_at`

### 3. `branch_comparisons`

Recommended fields:

- `comparison_group_id`
- `niche`
- `baseline_ref`
- `candidate_branch_ids`
- `winner_branch_id`
- `decision_summary`
- `created_at`

### 4. `regeneration_events`

Recommended fields:

- `event_id`
- `trigger_reason`
- `pre_state_summary`
- `action_summary`
- `outcome_summary`
- `created_at`

## Required New APIs

The future main system should expose:

- `/api/living-research-state`
- `/api/branches`
- `/api/branches/:id`
- `/api/branch-comparisons`
- `/api/regeneration-events`

These should sit above the current:

- `/api/control-state`
- `/api/inference-trace/latest`
- `/api/capacity`

The old APIs remain organism-level.
The new APIs are population-level.

## First Policy Mapping

### `homeostasis`

- allow low-risk branch spawning inside safe niches
- allow ordinary memory writes and runtime operation
- keep audit frequency normal
- prefer incremental local studies

### `adaptive`

- narrow active mutation surfaces
- reduce branch count ceiling
- increase audit frequency
- prefer optimizer and data-quality niches over architecture niche

### `inflammatory`

- pause risky promotions
- quarantine suspicious branches aggressively
- restrict new branch spawning
- prioritize evaluation integrity and cleanup

### `pathological`

- disable new branch spawning except emergency repair branches
- reduce active branch count
- archive nonessential branches
- preserve baselines and reserves first

### `regenerative`

- temporarily widen allowed architectural search
- allow scaffold branches
- treat branch creation as rebuild work, not open-ended exploration
- re-tighten back to `adaptive` or `homeostasis` after stabilization

## First Runtime Sequence

The full sequence should be:

```text
1. Read current organism control state
2. Estimate current reserve state ρ_t
3. Read branch registry and derive Λ_t
4. Read niche registry and derive N_t
5. Map current organism regime into candidate homeostatic mode
6. Update mode m_t using reserve and lineage health
7. Choose discrete governance action a_t
8. Apply governance decision:
   - spawn
   - quarantine
   - archive
   - kill
   - promote
   - regenerate
   - noop
9. Run or continue organism-level inference/control cycle
10. Persist living_research_state
11. Persist any branch-registry or regeneration-event changes
```

This makes governance sit around the organism controller without replacing it.

## Minimal Code Integration Plan

The first code pass should be small and layered.

### Step 1

Add:

```text
compute_reserve_state(control_state, runtime_state)
```

This returns `ρ_t`.

### Step 2

Add:

```text
build_lineage_summary(branch_registry)
```

This returns `Λ_t`.

### Step 3

Add:

```text
build_niche_registry()
```

This returns `N_t`.

### Step 4

Add:

```text
choose_homeostatic_mode(control_regime, ρ_t, Λ_t)
```

This returns `m_t`.

### Step 5

Add:

```text
choose_governance_action(m_t, ρ_t, Λ_t, N_t)
```

This returns `a_t`.

### Step 6

Persist:

```text
living_research_state
branch_registry
branch_comparisons
regeneration_events
```

### Step 7

Expose:

```text
/api/living-research-state
/api/branches
/api/branch-comparisons
/api/regeneration-events
```

## What Stays As V2

The following should not block `v1`:

- full lineage DAG analytics
- true viable-set geometry instead of thresholded summaries
- learned or adaptive niche controllers
- explicit branch rollback orchestration
- formal hybrid solver for continuous + discrete updates
- regeneration scaffolds with automatic re-differentiation

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
  adapters/cognition engine_adapter.py
```

Responsibility split:

- `reserve.py` computes `ρ_t`
- `lineage.py` computes `Λ_t` and branch health
- `niches.py` defines `N_t`
- `modes.py` computes `m_t`
- `governance.py` chooses and applies `a_t`

## Final Statement

The first implementation should not attempt a full autonomous research ecology in one pass.

It should:

```text
keep the current organism controller,
make reserve explicit,
make branch health explicit,
make modes explicit,
make governance actions explicit,
and let regeneration remain a tightly gated outer-layer capability
```

That is the correct first implementation form of the living research mathematical extension.
