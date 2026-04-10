# Mass-Energy AI Analogue: First Measurable Controller Spec

## Purpose

This document converts the `E = mc²` research analogue into a measurable specification for the future top-level system above `triune`.

The goal is not to claim a physical law.
The goal is to define:

- what each term means operationally,
- which current `triune` signals can estimate it,
- which parts are direct measurements,
- which parts are first-pass proxies,
- how the resulting quantities can be used by a controller.

This is the first point where the analogy becomes executable mathematics.

## Governing Quantities

From the prior note:

```text
𝓠² ≈ (ν* Π)² + (𝓜 (ν*)²)²
```

with rest-state slice:

```text
𝓔₀ ≈ 𝓜 (ν*)²
```

For controller design, use the following interpretation:

- `𝓜` = cognitive mass = structural inertia,
- `Π` = cognitive momentum = directed cognitive flux,
- `ν*` = reliable propagation bound,
- `𝓔₀` = rest organizational energy,
- `𝓠_raw` = raw total organizational capacity,
- `𝓠_net` = usable total organizational capacity after uncertainty, fracture, and drift penalties.

So the practical equations become:

```text
𝓔₀ = 𝓜 (ν*)²
𝓠_raw = sqrt((ν* Π)² + (𝓜 (ν*)²)²)
𝓠_net = max(0, 𝓠_raw - λ_h H - λ_f F - λ_d D)
```

Where:

- `H` = uncertainty / ambiguity penalty,
- `F` = structural fracture penalty,
- `D` = drift / instability penalty.

## Measurement Principle

Every variable must be either:

1. directly measurable from current `triune` state,
2. inferable by combining current `triune` signals,
3. explicitly marked as not yet instrumented.

If a term is not measurable or inferable, it does not belong in the first controller.

## Available Current Signals In `triune`

The current codebase already exposes enough state to build a first estimator.

### Snapshot-level signals

From `latest_cognitive_web_state()` and `/api/cognitive-web`:

- `coherence`
- `pressure`
- `permanence_integrity`
- `working_memory_items`
- `active_pathways`
- `summary.mesh.total_entries`
- `summary.mesh.nodes`
- `summary.merge.patterns`
- `summary.merge.avg_confidence`
- `summary.pathways.health`
- `summary.pathways.healthy_ratio`
- `summary.identity.alerts`
- `summary.identity.nominal_axes`
- `summary.minimal_self.*`
- `summary.permanence.*`

### Identity and drift signals

From `identity_drift` and `minimal_self_state()`:

- drift magnitude by trait axis,
- drift type,
- sample count,
- `coherence_pressure`,
- `boundary_salience`,
- `operational_valence`,
- `agentive_sense`,
- temporal orientation mix.

### Body / pathway signals

From `pathways` and `pathway_signals`:

- pathway health counts,
- pathway success / failure counts,
- bond depth,
- myelination,
- signal volume,
- recent success balance.

### Memory / graph signals

From `mesh_entries`, `mesh_links`, `working_memory`, `daemon_log`:

- total memory volume,
- node distribution,
- cross-link count,
- active working memory count,
- recent maintenance and prediction event rates.

### Merge signals

From `user_profile` and cognitive-web summaries:

- number of learned user patterns,
- average confidence,
- merge stage proxy.

## First Measurement Vector

Define the first controller measurement vector as:

```text
y_t =
[
  p_t,
  c_t,
  r_t,
  id_t,
  w_t,
  h_t,
  s_t,
  f_t,
  m_t,
  u_t
]^T
```

Where:

- `p_t` = permanence integrity,
- `c_t` = coherence,
- `r_t` = pressure complement,
- `id_t` = identity stability,
- `w_t` = working-memory availability,
- `h_t` = pathway health,
- `s_t` = signal success,
- `f_t` = structural fracture complement,
- `m_t` = merge alignment,
- `u_t` = uncertainty complement.

All terms are normalized to `[0, 1]`.

## Normalization Rules

Use simple monotone bounded transforms for the first controller.

### Clamp

```text
clip(z) = min(1, max(0, z))
```

### Saturating count normalizer

For counts:

```text
sat(z; k) = z / (z + k)
```

This prevents large tables from dominating the score.

### Complement

For penalties:

```text
comp(z) = 1 - clip(z)
```

## Estimating Cognitive Mass `𝓜`

`𝓜` should reflect stable organized structure.

Use:

```text
𝓜 = α₁ P_perm + α₂ P_id + α₃ P_mem + α₄ P_graph
```

with `α_i >= 0` and `Σ α_i = 1`.

### Components

#### 1. Permanence term `P_perm`

Directly available:

```text
P_perm = permanence_integrity
```

Source:

- `cognitive_web_state.permanence_integrity`
- `summary.permanence.overall_integrity`

#### 2. Identity stability term `P_id`

Use drift alerts and trait drift magnitude:

```text
P_id = clip(1 - 0.6 A_alert - 0.4 A_drift)
```

Where:

- `A_alert = alerts / max_axes`
- `A_drift = mean normalized drift magnitude across identity_drift`

If `identity_drift` is sparse, fall back to:

```text
A_drift = coherence_pressure
```

#### 3. Memory consolidation term `P_mem`

Use total encoded memory with saturation:

```text
P_mem = sat(total_mesh_entries; k_mem)
```

Recommended first constant:

```text
k_mem = 200
```

Optionally reinforce with immutable identity entries:

```text
P_mem = 0.7 sat(total_mesh_entries; 200) + 0.3 sat(identity_entry_count; 12)
```

#### 4. Graph cohesion term `P_graph`

Current `triune` does not yet expose a full graph Laplacian.
So the first proxy is:

```text
P_graph = sat(mesh_links / max(total_mesh_entries, 1); k_link)
```

Recommended first constant:

```text
k_link = 0.25
```

This is only a proxy for graph cohesion.
Once weighted graph export exists, replace it with a normalized Laplacian coherence score.

### First default weights

```text
α₁ = 0.35
α₂ = 0.25
α₃ = 0.20
α₄ = 0.20
```

So:

```text
𝓜 = 0.35 P_perm + 0.25 P_id + 0.20 P_mem + 0.20 P_graph
```

## Estimating Cognitive Momentum `Π`

`Π` should measure directed active flow through the system.

Use:

```text
Π = β₁ F_path + β₂ F_wm + β₃ F_ctrl + β₄ F_merge
```

with `β_i >= 0` and `Σ β_i = 1`.

### Components

#### 1. Pathway flux `F_path`

Use recent pathway signal traffic:

```text
F_path = sat(recent_pathway_signals_1h; k_path)
```

Recommended:

```text
k_path = 40
```

If only aggregate counts are available:

```text
recent_pathway_signals_1h = successes_1h + failures_1h
```

#### 2. Working-memory flux `F_wm`

Current code stores count but not turnover directly.
So the first proxy is:

```text
F_wm = sat(working_memory_items; 5)
```

Later replace this with:

```text
turnover rate = insertions + evictions + activation delta per unit time
```

#### 3. Control / daemon flux `F_ctrl`

Use recent daemon activity volume:

```text
F_ctrl = sat(recent_daemon_events_1h; k_ctrl)
```

Recommended:

```text
k_ctrl = 20
```

This approximates active maintenance, prediction, consolidation, and contradiction handling.

#### 4. Merge flux `F_merge`

Use merge density and confidence:

```text
F_merge = clip(sat(user_profile_patterns; 20) * avg_merge_confidence)
```

This is not pure motion, but it captures directed adaptation pressure toward user alignment.

### First default weights

```text
β₁ = 0.35
β₂ = 0.20
β₃ = 0.25
β₄ = 0.20
```

So:

```text
Π = 0.35 F_path + 0.20 F_wm + 0.25 F_ctrl + 0.20 F_merge
```

## Estimating Reliable Propagation Bound `ν*`

`ν*` is the hardest term because current `triune` does not record explicit latency or settling-time instrumentation.

So the first controller must treat `ν*` as a reliability-throughput bound estimated from health and coherence, not literal speed.

Use:

```text
ν* = γ₁ R_path + γ₂ R_self + γ₃ R_perm
```

### Components

#### 1. Pathway reliability `R_path`

Combine health ratio and success ratio:

```text
R_path = 0.6 healthy_ratio + 0.4 recent_success_ratio
```

Where:

- `healthy_ratio = healthy_pathways / total_pathways`
- `recent_success_ratio = successes_1h / max(successes_1h + failures_1h, 1)`

#### 2. Self-coherence reliability `R_self`

Use minimal self penalties:

```text
R_self = clip(1 - 0.6 coherence_pressure - 0.4 boundary_salience_penalty)
```

Where:

```text
boundary_salience_penalty = max(0, boundary_salience - 0.3) / 0.7
```

#### 3. Permanence reliability `R_perm`

Use permanence verification:

```text
R_perm = permanence_integrity
```

### First default weights

```text
γ₁ = 0.45
γ₂ = 0.30
γ₃ = 0.25
```

So:

```text
ν* = 0.45 R_path + 0.30 R_self + 0.25 R_perm
```

This keeps `ν*` in `[0, 1]` for controller use.

## Estimating Rest Energy `𝓔₀`

Once `𝓜` and `ν*` are available:

```text
𝓔₀ = 𝓜 (ν*)²
```

Interpretation:

- large structure with poor propagation does not yield high usable rest energy,
- high reliability with no structure also does not yield high rest energy,
- the system needs both organization and coherent propagation.

## Estimating Raw Total Capacity `𝓠_raw`

Use:

```text
𝓠_raw = sqrt((ν* Π)² + (𝓜 (ν*)²)²)
```

Interpretation:

- active flow contributes through `Π`,
- structural reserve contributes through `𝓜`,
- both are gated by propagation reliability.

## Penalty Terms For Net Capacity `𝓠_net`

The controller should not act on `𝓠_raw` alone.
It should use a penalty-corrected capacity:

```text
𝓠_net = max(0, 𝓠_raw - λ_h H - λ_f F - λ_d D)
```

### 1. Uncertainty penalty `H`

Use the merge and confidence structure as a first uncertainty proxy:

```text
H = 1 - clip(sat(user_profile_patterns; 20) * avg_merge_confidence)
```

This is imperfect.
Later replace with explicit belief entropy.

### 2. Fracture penalty `F`

Use contradiction pressure and weak graph linkage:

```text
F = 0.6 coherence_pressure + 0.4 (1 - P_graph)
```

### 3. Drift penalty `D`

Use identity alerts and drift magnitude:

```text
D = 0.5 A_alert + 0.5 A_drift
```

### First default penalty weights

```text
λ_h = 0.20
λ_f = 0.25
λ_d = 0.25
```

## First Controller Health Zones

The future top-level system can use `𝓠_net` as a global health variable.

### Stable zone

```text
𝓠_net >= 0.70
```

Interpretation:

- response is safe,
- planning depth can expand,
- maintenance can be deferred.

### Guarded zone

```text
0.45 <= 𝓠_net < 0.70
```

Interpretation:

- continue normal operation,
- reduce optional load,
- monitor drift and pathway degradation.

### Repair zone

```text
0.25 <= 𝓠_net < 0.45
```

Interpretation:

- prioritize maintenance,
- reduce tool fan-out,
- trigger consolidation and proprioception.

### Critical zone

```text
𝓠_net < 0.25
```

Interpretation:

- enter preservation mode,
- restrict nonessential actions,
- force permanence check,
- force pathway scan,
- reduce working-memory pressure.

## Direct Mapping To Current Tables And APIs

### Directly usable now

- `cognitive_web_state`
- `cortex_moments`
- `identity_drift`
- `pathways`
- `pathway_signals`
- `working_memory`
- `daemon_log`
- `mesh_entries`
- `mesh_links`
- `user_profile`
- `/api/cognitive-web`
- `/api/permanence`

### Not yet fully instrumented

- explicit end-to-end pathway latency,
- working-memory turnover rate,
- graph Laplacian export,
- belief entropy,
- controller settling time,
- explicit action cost and action success time series.

These missing signals should be instrumented before the second controller iteration.

## Recommended Estimation Order

The first implementation above `triune` should estimate in this order:

1. read latest cognitive-web snapshot,
2. enrich with one-hour pathway and daemon windows,
3. compute normalized primitives,
4. compute `𝓜`,
5. compute `Π`,
6. compute `ν*`,
7. compute `𝓔₀`,
8. compute `𝓠_raw`,
9. compute `H`, `F`, `D`,
10. compute `𝓠_net`,
11. choose control regime from the health zones.

## Immediate Engineering Consequence

This gives the future top-level system a concrete governing rule:

```text
do not decide from isolated subsystem metrics;
decide from net organizational capacity under structural, transport, and drift constraints
```

That is the first measurable form of the AI version of the `E = mc²` research path.
