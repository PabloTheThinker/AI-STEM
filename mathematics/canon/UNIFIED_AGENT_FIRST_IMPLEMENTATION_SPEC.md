# Unified Agent Intelligence: First Implementation Spec

Updated: `2026-03-31 03:32 UTC`

## Purpose

This document turns the merged mathematics into a first implementation plan.

It answers four concrete questions:

1. what should count as `r_t` in the first version,
2. where those signals can be collected in the current the cognition engine code,
3. how `q_t` should be computed on each cycle,
4. how the first controller loop should wrap around retrieval, thinking, memory updates, and maintenance.

This is the first implementation layer above theory.

## Design Rule

The first implementation should follow this rule:

```text
instrument with proxies now,
replace with native internal metrics later
```

That means the first version must not wait for perfect transformer introspection.
It should begin with observable inference-path summaries already present in the cognition engine.

## Target Runtime Stack

The future main system should sit above the cognition engine and orchestrate:

```text
request
-> controller pre-state estimate
-> cognition engine retrieval / think path
-> post-think state estimate
-> q_t update
-> control action selection
-> memory / pathway / maintenance decisions
```

This is the first practical form of the multi-scale system.

## Current Hook Points In the cognition engine

The current engine already gives clear hook points.

### Retrieval hooks

From `query()` and `query_multihop()`:

- retrieved result count,
- similarity distribution,
- cross-node retrieval spread,
- retrieval-induced suppression events,
- prediction-error queue insertions,
- helix proofreading / supercoiling maintenance on access.

These are the first retrieval-flow signals.

### Think-path hooks

From `think()`:

- retrieval size per node,
- superposition coherence and entanglement,
- collapse method and dominant strand,
- strand-read volume and average strand weights,
- active-gene count,
- attended result count,
- user-profile load depth and pattern count,
- body-state availability and alert condition.

These are the first internal-computation proxies.

### Weighted-think hooks

From `weighted_think()`:

- domain weights,
- weighted retrieval distribution,
- dominant node,
- weighted similarity ranking.

These expose a first structured policy-bias signal.

### Cognitive-web hooks

From `cognitive_web_tick()` and `latest_cognitive_web_state()`:

- coherence,
- pressure,
- permanence integrity,
- working-memory item count,
- healthy pathway count,
- identity alert count,
- merge confidence,
- minimal-self state.

These are the first organism-state signals.

## First Version Of Internal State `r_t`

In theory, `r_t` is internal transformer state.
In `v1`, it should be an inference-summary vector collected from the think path.

Use:

```text
r_t = [r_ret, r_sup, r_strand, r_attn, r_user, r_body, r_mode]^T
```

### `r_ret` retrieval state

Computed from the retrieval phase:

- total retrieved patterns,
- node distribution entropy,
- mean similarity of top results,
- multihop depth actually used.

Interpretation:

- broad, coherent retrieval means rich context assembly,
- narrow or low-similarity retrieval means weak contextual grounding.

### `r_sup` superposition state

Computed from helix superposition:

- superposition coherence,
- entanglement,
- constructive-theme count,
- destructive-theme count,
- collapse method category.

Interpretation:

- this is the closest current proxy to internal competition and synthesis.

### `r_strand` deep-read state

Computed from strand-read and gene-expression phases:

- strand base-pair count,
- average strand weight,
- supercoiled count,
- telomere count,
- active gene count.

Interpretation:

- this approximates depth and structure of deep memory engagement.

### `r_attn` focus state

In `v1`, there is no true attention-tensor instrumentation.
So use a proxy:

- number of retained items after `attend()`,
- concentration ratio of top retained items,
- dominant node after attention.

Interpretation:

- this approximates narrowing and focus of active inference.

### `r_user` merge-conditioning state

Computed from the user-profile phase:

- loaded pattern count,
- mean confidence,
- profile depth category encoded numerically.

### `r_body` embodied inference state

Computed from the body-state phase:

- available pathway count,
- degraded pathway count,
- down pathway count,
- autonomic alert flag.

### `r_mode` inference-mode state

Computed from model profile:

- reasoning depth rank,
- frame budget,
- convergence mode category.

This matters because inference quality and internal capacity depend on the model sleeve currently attached.

## First Version Of External State `x_t`

`x_t` should remain aligned with the existing cognitive-web blocks:

```text
x_t = [x_id, x_mem, x_aff, x_body, x_merge, x_exec]^T
```

For `v1`, each block should be assembled from current database state.

### `x_id`

Use:

- permanence integrity,
- identity alert count,
- drift magnitude summary,
- resistance log pressure if available.

### `x_mem`

Use:

- total mesh entries,
- cross-link count,
- contradiction pressure,
- retrieval-success summary,
- schema / core-memory counts when available.

### `x_aff`

Use:

- operational valence,
- coherence pressure,
- temporal orientation skew,
- alert-state flags.

### `x_body`

Use:

- healthy ratio,
- recent pathway success ratio,
- degraded/down counts,
- bond-depth weighted pathway availability.

### `x_merge`

Use:

- user-pattern count,
- mean profile confidence,
- merge stage encoding.

### `x_exec`

Use:

- working-memory item count,
- action readiness proxy,
- daemon-event activity,
- current task strain proxy from retrieval + body alert pressure.

## First Version Of Capacity State `q_t`

`q_t` should be computed on every controller cycle:

```text
q_t = [𝓜_t, Π_t, ν*_t, 𝓔₀_t, 𝓠_raw,t, 𝓠_net,t]^T
```

### `𝓜_t`

Use the existing controller-spec formula, but now let it depend on both:

- external permanence/identity/memory signals,
- internal deep-read and superposition stability terms.

Recommended first extension:

```text
𝓜_t = 0.30 P_perm + 0.20 P_id + 0.15 P_mem + 0.15 P_graph + 0.20 P_internal
```

where:

```text
P_internal = clip(0.5 superposition_coherence + 0.5 normalized_strand_weight)
```

### `Π_t`

`Π_t` should become the main bridge variable.

Use:

```text
Π_t = 0.25 F_path + 0.15 F_wm + 0.15 F_ctrl + 0.15 F_merge + 0.30 F_infer
```

where:

```text
F_infer = clip(
  0.25 retrieval_flux
  + 0.25 attended_flux
  + 0.25 superposition_activity
  + 0.25 strand_read_activity
)
```

This is the first direct merge of neural inference math into the macro controller.

### `ν*_t`

Use:

```text
ν*_t = 0.35 R_path + 0.20 R_self + 0.20 R_perm + 0.25 R_infer
```

where:

```text
R_infer = clip(
  0.4 superposition_coherence
  + 0.2 (1 - destructive_theme_penalty)
  + 0.2 attended_focus_quality
  + 0.2 model_depth_quality
)
```

This treats internal inferential coherence as part of the propagation bound.

## Required New Data Structures

The first implementation should add one new table above the existing cognitive-web tables:

```text
agent_control_state
```

Recommended columns:

- `id`
- `trigger`
- `r_summary`
- `x_summary`
- `q_summary`
- `control_regime`
- `decision_policy`
- `created_at`

Optional second table:

```text
inference_trace
```

Recommended columns:

- `question_hash`
- `model`
- `retrieval_summary`
- `superposition_summary`
- `strand_summary`
- `attention_summary`
- `body_summary`
- `created_at`

The first table is required.
The second is strongly useful for debugging and research.

## Required New APIs

The future main system should expose at least:

- `/api/control-state`
- `/api/inference-trace/latest`
- `/api/capacity`

These should sit next to the existing:

- `/api/cognitive-web`
- `/api/permanence`
- `/api/helix`

## First Controller Regimes

The controller should classify each cycle into one of four regimes:

```text
steady
guarded
repair
preserve
```

Use the existing `𝓠_net` zones:

- `steady` when `𝓠_net >= 0.70`
- `guarded` when `0.45 <= 𝓠_net < 0.70`
- `repair` when `0.25 <= 𝓠_net < 0.45`
- `preserve` when `𝓠_net < 0.25`

## First Policy Mapping

### `steady`

- allow full retrieval depth,
- allow memory writes,
- allow pathway execution under normal trust gates,
- defer maintenance unless separately scheduled.

### `guarded`

- reduce optional retrieval depth,
- reduce memory-write frequency,
- prefer lower-risk pathways,
- schedule a maintenance tick soon.

### `repair`

- prioritize cognitive-web tick and proprioception,
- restrict nonessential pathway calls,
- write only high-salience memory,
- prefer weighted-think over unconstrained think.

### `preserve`

- force permanence sync,
- force pathway scan,
- minimize working-memory growth,
- disable nonessential writes and risky tool actions,
- prioritize stabilization over throughput.

## First Runtime Sequence

The controller loop should be:

```text
1. Pre-read latest cognitive web state
2. Estimate provisional x_t
3. Estimate provisional q_t from existing summaries
4. Choose pre-inference policy
5. Run think()/weighted_think() under that policy
6. Collect r_t inference summary
7. Recompute x_t from cognitive_web_tick()
8. Recompute q_t from merged r_t and x_t
9. Choose post-inference regime
10. Apply maintenance / write / pathway policy
11. Persist agent_control_state
```

This makes control both:

- predictive before inference,
- corrective after inference.

## Minimal Code Integration Plan

The first code pass should be small.

### Step 1

Add a pure function:

```text
build_inference_summary(...)
```

This should summarize:

- retrieval,
- superposition,
- strand reads,
- attended results,
- user patterns,
- body state,
- model profile.

### Step 2

Add:

```text
compute_capacity_state(r_summary, x_summary)
```

This returns `q_t`.

### Step 3

Add:

```text
choose_control_regime(q_t)
```

and:

```text
choose_decision_policy(regime, model_profile)
```

### Step 4

Persist:

```text
agent_control_state
```

and expose `/api/control-state`.

### Step 5

Wrap `think()` and `weighted_think()` with a top-level orchestrator function in the new main system, not inside raw the cognition engine cognition functions.

## What Stays As V2

The following should not block `v1`, but should be added later:

- true attention entropy,
- residual update norms from model internals,
- token-level activation dispersion,
- solver-style continuous-depth diagnostics,
- belief entropy instead of merge-confidence proxy,
- graph Laplacian from a fully explicit cognitive graph.

These belong to `v2` instrumentation.

## File / Module Recommendation

The future main system should begin with a small module layout:

```text
main_system/
  state_estimator.py
  capacity.py
  policy.py
  orchestrator.py
  adapters/cognition engine_adapter.py
```

Responsibility split:

- `state_estimator.py` builds `r_t` and `x_t`,
- `capacity.py` computes `q_t`,
- `policy.py` selects regime and decision policy,
- `orchestrator.py` sequences the runtime,
- `cognition engine_adapter.py` calls the cognition engine functions and APIs.

## Final Statement

The first implementation should not try to fully solve internal interpretability.
It should:

```text
use the current the cognition engine inference path as a source of structured internal-state proxies,
merge those proxies with cognitive-web state,
compute q_t every cycle,
and let q_t govern retrieval, writing, maintenance, and action risk
```

That is the shortest path from the new mathematics to a working main system.
