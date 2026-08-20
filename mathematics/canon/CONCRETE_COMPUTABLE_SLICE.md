# Concrete Computable Slice v1

**Fudoshin Research · Vektra Industries**  
Updated: `2026-08-20`  
Status: Stage C (defined, internally consistent, pinned synthetic example). Not Stage F.  
Implementation: `mathematics/lineage-papers/reference/lineage_slice_v2.py`

## Purpose

The packet has a law and an organism. It did not have a path from a log line to a number.

This file is that path. It does **not** replace the official Lineage Equation. The operator instrument that sits on this slice is [`LINEAGE_EQUATION_USABLE.md`](LINEAGE_EQUATION_USABLE.md).

It answers four operational questions:

1. What do you log?
2. How do you turn those logs into `C_i`, `F_k`, `ν*`, and penalties?
3. What is `Φ_org` as an explicit formula on this slice?
4. What would Stage F actually look like, with an exogenous target?

Design rule, unchanged: **instrument with proxies now, replace with native metrics later.** Every proxy below is marked.

## What this slice is not

- Not the full organism `𝒪_t`. Substrate activations `alpha_t`, routing `χ_t`, and blood lineages are **declared missing**. `Φ_sub = 0` until they are instrumented.
- Not a claim that v2 official weights transfer across architectures.
- Not Stage F. The worked example is a pinned calculation, not a live prediction.

## 1. Telemetry record

One window, generic fields, no private engine required.

| Field | Kind | Used for |
|---|---|---|
| `identity_alert_count`, `identity_axis_count`, `mean_identity_drift` | count / `[0,1]` | `C_id`, `D_drift` |
| `memory_entries`, `memory_index_coverage` | count / `[0,1]` | `C_mem` |
| `graph_nodes`, `graph_edges`, `healthy_edge_ratio` | count / `[0,1]` | `C_graph` |
| `permanence_integrity` or `checkpoint_success_ratio` | `[0,1]` | `C_perm` |
| `wm_turnover` or `wm_items` | count | `F_wm` |
| `retrieval_attempts`, `retrieval_hits`, `mean_retrieval_score` | count / `[0,1]` | `F_ret` |
| `pathway_events` | count | `F_path` |
| `control_actions` | count | `F_ctrl` |
| `merge_writes`, `merge_confidence` | count / `[0,1]` | `F_merge` |
| `tau_*_s` (five latencies) | seconds | `ν*` |
| `belief_entropy` or `1 − merge_confidence` | `[0,1]` | `H(μ)` |
| `graph_weights` + `graph_state`, else `healthy_edge_ratio` | matrix / vector | `Ê` |
| `mode`, `reserve`, `neural_health`, `blood_health` | gate inputs | plasticity |

JSON shape: any object `lineage_slice_v2.TelemetryRecord` accepts.

## 2. Normalizers

```text
clip(z) = min(1, max(0, z))
sat(z; k) = z / (z + k)     for z ≥ 0, k > 0
```

First-slice constants (hyperparameters, **not** laws):

| Constant | Value | Role |
|---|---|---|
| `k_mem` | 200 | memory saturation |
| `k_link` | 0.25 | mean-degree saturation |
| `k_wm_turn` | 8 | working-memory turnover |
| `k_wm_count` | 5 | working-memory count fallback |
| `k_path` | 40 | pathway events |
| `k_ctrl` | 20 | control actions |
| `k_merge` | 12 | merge writes |

Changing a constant changes every published `Q`. Declare the table.

## 3. Primitive estimators (proxies)

```text
C_id    = clip(1 − 0.6 · alerts/axes − 0.4 · mean_drift)
C_mem   = 0.7 sat(entries; 200) + 0.3 clip(index_coverage)
          or sat(entries; 200) if coverage is missing
C_graph = 0.6 sat(edges/nodes; 0.25) + 0.4 healthy_edge_ratio
          or sat(edges/nodes; 0.25) if health is missing
C_perm  = clip(permanence_integrity)
          or clip(checkpoint_success_ratio)

F_wm    = sat(turnover; 8) or sat(wm_items; 5)
F_ret   = 0.6 · hits/attempts + 0.4 · mean_retrieval_score
F_path  = sat(pathway_events; 40)
F_ctrl  = sat(control_actions; 20)
F_merge = 0.6 sat(merge_writes; 12) + 0.4 clip(merge_confidence)

ν*      = 1 / max(τ_retrieval, τ_pathway, τ_wm, τ_sync, τ_settling)     (Hz)
```

Native replacements later: hash-continuity for `C_id`, Laplacian spectral gap for `C_graph`, true belief entropy for `H(μ)`, activation traces for `Φ_sub`.

## 4. Weight tables (declare one)

| Table | Mass α `(id, mem, graph, perm)` | Momentum β `(wm, ret, path, ctrl, merge)` | Status |
|---|---|---|---|
| **official** | `(0.28, 0.30, 0.22, 0.20)` | `(0.22, 0.25, 0.20, 0.18, 0.15)` | v2 operational default |
| equal | all `0.25` / `0.20` | v1 null model |
| promotion | normalized Stage E digits | historical synthetic ID only |

Law evaluation on this slice uses **official**. Identification of new weights uses the linear instrument, not the quadratic.

```text
M  = Σ α_i C_i
Π  = Σ β_k F_k
```

## 5. Official law, then operational budget

Law (v2, unchanged):

```text
r      = ν* / ν₀
M̃      = M · r²
Π̃      = Π · r
Q      = κ √(Π̃² + M̃²)
```

**Units repair.** v2 writes `Q_eff = Q − λ_H H − λ_E E − λ_D D`. That is well-posed only when the λ live in capacity units. On a 120 ms bottleneck, `Q` is order `50` and the penalties are order `1`. Subtracting them unchanged is a category error.

Operational form used by this slice:

```text
Ê      = (zᵀ L z) / (n ‖z‖²)          if a graph is logged
       | 1 − healthy_edge_ratio       otherwise
H      = clip(belief_entropy) or (1 − merge_confidence)
D      = clip(mean_identity_drift)
u      = clip(1 − λ_H H − λ_E Ê − λ_D D)
Q_eff  = u · Q
```

First defaults: `λ_H = λ_E = λ_D = 0.25`. Additive v2 is recovered by `λ_abstract = λ_frac · Q`.

Linear identification instrument (**not** the law):

```text
Q_lin = s (M + Π) + b
```

Use `Q_lin` to fit α, β. Use `Q` to report capacity. Do not cite them as one number.

## 6. Explicit `Φ_org` on this slice

```text
Φ_sub  = 0                         # declared: no substrate instrumentation
Φ_gov  = D
Φ_sig  = H
Φ_sup  = Ê
Φ_gate = 1[plasticity closed]
Φ_org  = Φ_sub + Φ_gov + Φ_sig + Φ_sup + Φ_gate
```

Plasticity gate (unchanged):

```text
open iff mode ∈ {homeostasis, adaptive}
     and reserve > reserve_min
     and neural_health < health_max
     and blood_health < blood_max
```

## 7. Zone and ascent hint

Zone is on **usable fraction** `u = Q_eff / Q`, not on raw `Q`. Raw `Q` is dominated by `M r²` and is not a health score.

| `u` | Zone |
|---|---|
| ≥ 0.70 | steady |
| 0.45–0.70 | guarded |
| 0.25–0.45 | repair |
| < 0.25 | critical |

Ascent hint uses **feasible steps**, not raw derivatives. Typical one-tick sizes:

```text
ΔM  = 0.05
ΔΠ  = 0.10
Δν* = 1 Hz
hint = argmax |∂Q/∂ξ| · Δξ
```

On the worked example, raw `∂Q/∂M` is largest (`r⁴` inflation). After scaling, the hint is **cut bottleneck latency**. That is the calculus layer’s own warning, now executable.

## 8. Worked example — loaded but coherent

Inputs:

```text
alerts=1, axes=8, mean_drift=0.15
entries=120, coverage=0.55
nodes=40, edges=70, healthy_edge_ratio=0.80
permanence=0.82
wm_turnover=6, retrieval 14/20 @ 0.72
pathway_events=25, control_actions=8
merge_writes=5, merge_confidence=0.70
τ = (0.120, 0.040, 0.030, 0.020, 0.015) s
H = 0.35
W = [[0,1,0.5],[1,0,0.2],[0.5,0.2,0]], z = [0.2, 0.5, 0.1]
mode=adaptive, reserve=0.50
weight_table=official
```

Pinned outputs (`python3 lineage_slice_v2.py --example`):

| Quantity | Value |
|---|---|
| `C_id`, `C_mem`, `C_graph`, `C_perm` | 0.865, 0.428, 0.845, 0.820 |
| `F_wm`, `F_ret`, `F_path`, `F_ctrl`, `F_merge` | 0.429, 0.708, 0.385, 0.286, 0.456 |
| `M`, `Π`, `ν*` | 0.720, 0.468, 8.333 Hz |
| `M̃`, `Π̃`, `Q`, `E₀` | 50.024, 3.901, 50.176, 50.024 |
| `H`, `Ê`, `D` | 0.350, 0.141, 0.150 |
| `u`, `Q_eff`, `Q_lin` | 0.840, 42.134, 1.188 |
| `Φ_org` | 0.641 |
| zone / hint / gate | steady / cut_bottleneck_latency / open |

Read the table slowly:

- Rest term `M̃` is `50.0`; transport `Π̃` is `3.9`. At `τ* = 120 ms`, capacity is almost rest energy. That is the law working, not a bug.
- `Q_lin = 1.19` is a different object. Mixing it with `Q = 50.2` is the miss already on the Findings table.
- Usable fraction `0.84` is the health number. `Q` is not.

Reproduce:

```bash
python3 mathematics/lineage-papers/reference/lineage_slice_v2.py --example
```

Expect `slice_validation_checks_passed 31` and the pinned row.

## 9. Stage F protocol (pre-registered, not yet run)

A later study may claim Stage F only if all of the following hold.

1. **Log** `TelemetryRecord` every controller cycle for at least three disjoint weeks.
2. **Fit** weeks 1–2. Allowed fits: (a) official α*, β* held fixed, fit only `(λ_H, λ_E, λ_D)` on the simplex `λ_H+λ_E+λ_D ≤ 1`, or (b) linear instrument `Q_lin` for new α, β. Forbidden: fitting α, β inside the quadratic and calling that the law.
3. **Predict** week 3.
4. **Target must be exogenous.** Allowed targets: operator capacity rating, next-window task-success rate, next-window measured throughput. Forbidden: using computed `Q` or `Q_eff` as its own target.
5. **Pass:** held-out `R² > 0.5` on the chosen target, plus a published residual plot.
6. **Misses stay on the register.** A failed week-3 prediction is a miss, not a quiet rewrite of α*.

Until that bundle exists, this slice remains Stage C/D.

## 10. What advanced

| Before | After |
|---|---|
| `C_i`, `F_k` were names | Explicit estimators from a generic record |
| `Φ_org` was a sum of unnamed terms | Closed form on this slice, with `Φ_sub = 0` declared |
| Additive `Q_eff` mixed units | Multiplicative usable fraction; additive recovered by scaling λ |
| Three weight tables undocumented at the instrument | Named tables; official vs linear vs promotion |
| Gradients without intervention size | Hint = `\|∂Q\| · typical_step` |
| Stage F was a wish | Pre-registered protocol with a forbidden target |

## Implementation reading

1. Fill `TelemetryRecord`.
2. `estimate_primitives`.
3. Build `LineageEquationV2` with a declared weight table.
4. Read `Q` from the law, `u` and `Q_eff` from the budget, `Φ_org` from the barrier, zone from `u`, hint from scaled gradients.
5. Do not write `Q` to a dashboard without `u` and the weight-table name.
