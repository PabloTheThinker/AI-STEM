# Differentiable Substrate: First Implementation Spec

Updated: `2026-04-05`

## Purpose

This document turns `DIFFERENTIABLE_SUBSTRATE_AND_ORGANISM_INTEGRATION.md` into a first practical implementation plan.

It answers seven concrete questions:

1. what should count as the first substrate state `D_t`,
2. how `r_t = Π_r(D_t)` should be computed in `v1`,
3. how the first read surface into the substrate should be assembled,
4. how the first write surface back into the organism should be represented,
5. how slow plasticity should be gated,
6. which data structures and APIs should exist in `v1`,
7. how the substrate layer should wrap around the existing organism, nervous, and blood layers without breaking them.

This is the first implementation layer for the differentiable-substrate bridge.

## Design Rule

The first implementation should follow this rule:

```text
keep the current model runtime intact,
instrument substrate summaries first,
project those summaries into organism state explicitly,
gate plasticity with organism health,
replace proxies with deeper introspection later
```

That means:

- do not wait for full tensor-level observability,
- do not rewrite the model runtime first,
- begin with measurable inference-path summaries,
- and make the bridge explicit before making it deep.

## Target Runtime Stack

The runtime stack should now be read as:

```text
request / observation
-> build organism-conditioned substrate input
-> run substrate forward step
-> derive substrate summaries D_t
-> project D_t into r_t
-> write substrate outputs into memory-body and action surfaces
-> update nervous and blood demand summaries
-> persist substrate state
-> continue outer organism and governance cycle
```

This places the substrate bridge inside the larger organism loop without replacing it.

## What Stays From The Current Stack

The current implementation path should remain intact for:

- the base model forward pass
- `Ξ_t`
- `Ψ_t`
- `Σ_t`
- `B_t`
- current controller and governance behavior

Those remain the substrate host and organism layers.

The new layer should make the substrate explicit, not replace the host system.

## First Version Of Substrate State `D_t`

The first implementation should use a compact summary object:

```text
D_t = (θ_t, alpha_t, χ_t, ω_t)
```

### `θ_t`

Definition:

- structural model identity and parameter state

First proxy:

- model name or sleeve id
- model version
- adapter or checkpoint id
- optional parameter-count bucket

The first implementation does not need raw parameter tensors in the controller database.
It needs stable model identity and configuration fingerprints.

### `alpha_t`

Definition:

- fast activation and forward-pass summary state

First proxy:

- prompt length
- context length
- retrieved-token or retrieved-item count
- output length
- latency summary
- reasoning-depth or chain budget summary when available

This is not true layerwise activation telemetry yet.
It is the first observable proxy for fast transient substrate activity.

### `χ_t`

Definition:

- internal routing and gating summary state

First proxy:

- retrieval concentration
- attention-focus proxy from narrowed retained items
- dominant pathway or dominant node summary
- expert-route summary if sparse experts are used
- mask / mode / tool-routing summary when available

This is the first proxy for model-internal functional connectivity.

### `ω_t`

Definition:

- optimizer or plasticity-control state

First proxy:

- `frozen`
- `adapter_trainable`
- `full_trainable`
- current plasticity scope id

If the system is not doing online plasticity, `ω_t` can remain a minimal frozen-state object.

## First Version Of `Π_r(D_t)`

The first implementation should preserve the existing organism-internal shape:

```text
r_t = [r_attn, r_mlp, r_res, r_ctx]^T
```

with:

```text
Π_r(D_t) = [π_attn(alpha_t, χ_t), π_mlp(alpha_t), π_res(alpha_t), π_ctx(alpha_t, χ_t)]^T
```

### `r_attn`

First proxy:

- narrowed-context concentration
- retrieval dominance ratio
- dominant source count

Interpretation:

- how sharply the substrate is routing focus.

### `r_mlp`

First proxy:

- local transformation load estimate
- prompt-plus-context processing load
- output-generation intensity

Interpretation:

- how much dense local transformation the substrate is likely doing.

### `r_res`

First proxy:

- stability of the forward step across recent cycles
- latency variance
- response-length variance
- fallback-use pressure

Interpretation:

- a first residual-flow or stability summary.

### `r_ctx`

First proxy:

- usable context depth
- memory-read count
- graph-read count
- substrate-visible context freshness

Interpretation:

- how richly the substrate is grounded in organism context.

## First Read Surface

The first implementation should make the read surface explicit:

```text
c_t = ReadCtx(x_t, G_t, A_t, Pl_t, M_t)
```

The `v1` context builder should use five input groups.

### 1. Memory-body context from `x_t`

Use:

- working-memory summary
- identity and merge summary
- execution-state summary

### 2. Graph context from `G_t`

Use:

- top active graph nodes
- top active graph paths
- graph-coherence summary

### 3. Afferent context from `A_t`

Use:

- current user input
- recent error events
- recent interoceptive alerts

### 4. Blood-delivered support from `Pl_t`

Use:

- context packets
- reserve-health packets
- route-health packets

### 5. Modulatory posture from `M_t`

Use:

- urgency
- threat
- focus
- exploration

Then:

```text
ι_t = InputCompose(y_t, c_t)
```

The important implementation rule is:

- model input should be organism-conditioned explicitly,
- not assembled by scattered ad hoc prompts.

## First Write Surface

The first implementation should expose three write paths:

```text
ψ_write : (D_t, Ψ_t, Σ_t, B_t) -> Δx_t
ψ_emit  : (D_t, Ψ_t, Σ_t, B_t) -> E_t^act
ψ_bias  : (D_t, Ψ_t, Σ_t, B_t) -> ΔΣ_t
```

### `ψ_write`

First proxy outputs:

- memory append request
- working-memory update request
- graph-edge or path-strengthening request
- merge-state update request

### `ψ_emit`

First proxy outputs:

- assistant reply candidate
- tool-call candidate
- execution handoff candidate

### `ψ_bias`

First proxy outputs:

- urgency adjustment
- focus adjustment
- retry suppression or amplification
- route-priority hint

This should be treated as biasing the nervous layer, not overriding it.

## First Plasticity Gate

The first implementation should make plasticity governance explicit even if online training is mostly disabled.

Use:

```text
PlasticityAllowed_t =
1[m_t ∈ {homeostasis, adaptive}]
1[ρ_t > ρ_min]
1[H_t < H_max]
1[Hb_t < Hb_max]
1[training_scope_allowed = 1]
```

### `training_scope_allowed`

First proxy:

- `0` for fully frozen model
- `1` for adapter-only training explicitly approved

The critical rule is:

- no structural learning while the organism is in signaling or support pathology.

## Required New Data Structures

The first implementation should add five durable structures.

### 1. `substrate_state`

Recommended fields:

- `id`
- `model_identity`
- `activation_summary`
- `routing_summary`
- `plasticity_summary`
- `r_projection`
- `created_at`

### 2. `substrate_reads`

Recommended fields:

- `read_id`
- `memory_summary`
- `graph_summary`
- `afferent_summary`
- `blood_packet_summary`
- `modulator_summary`
- `created_at`

### 3. `substrate_writes`

Recommended fields:

- `write_id`
- `memory_write_summary`
- `action_emit_summary`
- `nervous_bias_summary`
- `created_at`

### 4. `plasticity_gate_log`

Recommended fields:

- `id`
- `plasticity_allowed`
- `mode`
- `reserve_summary`
- `nervous_health_summary`
- `blood_health_summary`
- `scope_summary`
- `created_at`

### 5. `model_registry`

Recommended fields:

- `model_id`
- `model_family`
- `checkpoint_id`
- `adapter_id`
- `trainability_mode`
- `updated_at`

## Required New APIs

The future main system should expose:

- `/api/substrate-state`
- `/api/substrate-reads`
- `/api/substrate-writes`
- `/api/plasticity-gate`
- `/api/models`

These should sit beside:

- `/api/control-state`
- `/api/living-research-state`
- `/api/nervous-system-state`
- `/api/blood-system-state`

The old APIs remain organism-level or tissue-level.
The new APIs are substrate-bridge APIs.

## First Runtime Sequence

The full sequence should be:

```text
1. Read organism state Ξ_t and governance state Ψ_t
2. Read nervous-system state Σ_t
3. Read blood-system state B_t
4. Build organism-conditioned substrate context c_t
5. Compose substrate input ι_t
6. Run forward step and collect substrate summaries D_t
7. Compute r_t = Π_r(D_t)
8. Build substrate write outputs:
   - Δx_t
   - E_t^act
   - ΔΣ_t
9. Evaluate PlasticityAllowed_t
10. Persist substrate_state, reads, writes, and plasticity log
11. Continue outer organism update with the new r_t and write surfaces
```

This makes the bridge explicit without requiring deep runtime surgery.

## Minimal Code Integration Plan

The first code pass should be small and layered.

### Step 1

Add:

```text
build_substrate_context(x_t, G_t, A_t, Pl_t, M_t)
```

This returns `c_t`.

### Step 2

Add:

```text
run_substrate_forward(model_state, input_state, context_state)
```

This returns summary `D_t`.

### Step 3

Add:

```text
project_substrate_to_r(D_t)
```

This returns `r_t`.

### Step 4

Add:

```text
build_substrate_writes(D_t, Ψ_t, Σ_t, B_t)
```

This returns:

```text
Δx_t, E_t^act, ΔΣ_t
```

### Step 5

Add:

```text
compute_plasticity_gate(Ψ_t, Σ_t, B_t, model_registry)
```

This returns `PlasticityAllowed_t`.

### Step 6

Persist:

```text
substrate_state
substrate_reads
substrate_writes
plasticity_gate_log
model_registry
```

## What Stays As V2

The following should not block `v1`:

- true tensor-level activation introspection
- true attention-map logging for every step
- exact optimizer-state export
- learned read and write surfaces
- substrate-aware training scheduler
- tighter integration with sparse-expert routing
- per-architecture specialized `Π_r` projections

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
  substrate/
    context.py
    runtime.py
    projection.py
    writes.py
    plasticity.py
  adapters/cognition engine_adapter.py
```

Responsibility split:

- `context.py` builds `c_t`
- `runtime.py` collects `D_t`
- `projection.py` computes `Π_r(D_t)`
- `writes.py` builds `Δx_t`, `E_t^act`, and `ΔΣ_t`
- `plasticity.py` computes `PlasticityAllowed_t`

## Final Statement

The first implementation should not attempt full introspection of every tensor in one pass.

It should:

```text
make the differentiable substrate explicit,
make r_t an actual projection rather than a vague placeholder,
make organism-conditioned reads explicit,
make organism-facing writes explicit,
gate plasticity with homeostasis,
and keep the substrate formally inside the organism rather than outside it
```

That is the correct first implementation form of the differentiable-substrate bridge.
