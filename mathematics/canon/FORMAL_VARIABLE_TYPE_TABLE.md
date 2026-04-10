# Formal Variable Type Table

Updated: `2026-04-05`

## Purpose

This file translates the canonical mathematics into an implementation-facing type contract.

It is meant to answer four questions for each symbol:

- what kind of object it is,
- what mathematical type it has,
- what code alias should be used when Unicode is inconvenient,
- and what runtime or storage shape should be expected in `v1`.

## Rule Of Use

This table does not override the basis or glossary.

It operationalizes them.

Authority order remains:

1. `ORGANISMIC_INTELLIGENCE_MATHEMATICAL_BASIS.md`
2. `SYMBOLS_AND_NOTATION_GLOSSARY.md`
3. `NOTATION_POLICY.md`
4. this type table

## Implementation Type Conventions

Use the following generic implementation kinds:

- `scalar<float>` = one real-valued scalar
- `scalar<int>` = one integer scalar
- `scalar<bool>` = one boolean indicator
- `enum<string>` = one string from a fixed closed set
- `vector<float>[fixed]` = fixed-order real vector
- `vector<float>[variable]` = variable-length real vector
- `record{...}` = structured object with named fields
- `map<K,V>` = keyed dictionary
- `set<T>` = unordered collection
- `graph` = graph object or graph-backed store
- `opaque` = implementation-defined state that must preserve the mathematical meaning

ASCII aliases should follow the notation policy:

- `θ_t` -> `theta_t`
- `χ_t` -> `chi_t`
- `Ψ_t` -> `Psi_t`
- `Σ_t` -> `Sigma_t`

## Top-Level Organism Objects

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Update cadence |
| --- | --- | --- | --- | --- | --- |
| `𝒪_t` | `O_t` | full organism state | `𝒮_D × 𝒮_Ψ × 𝒮_Σ × 𝒮_B` | `record{D_t, Psi_t, Sigma_t, B_t}` | mixed |
| `D_t` | `D_t` | substrate state | compound state | `record{theta_t, alpha_t, chi_t, omega_t}` | `τ_alpha`, `τ_theta` |
| `Ψ_t` | `Psi_t` | governance state | compound state | `record{Xi_t, rho_t, Lambda_t, N_t, m_t, a_t}` | `τ_gov` |
| `Σ_t` | `Sigma_t` | nervous-system state | compound state | `record{A_t, J_t, K_t, P_t, E_t, M_t, H_t}` | `τ_sigma` |
| `B_t` | `B_t` | blood-system state | compound state | `record{Pl_t, Ma_t, Li_t, De_t, St_t, Cl_t, Hb_t}` | `τ_blood` |

## Substrate Type Table

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- | --- |
| `θ_t` | `theta_t` | structural parameters | parameter state | `opaque` | checkpoint refs, adapter refs, or tensor handles |
| `alpha_t` | `alpha_t` | fast activation state | transient substrate state | `record{latency, token_load, context_load, route_summary, output_load}` | do not shorten to `a_t` |
| `χ_t` | `chi_t` | routing and gating state | internal routing state | `record{focus, route_mix, dominant_path, mask_summary}` | substrate-internal summary |
| `ω_t` | `omega_t` | optimizer or plasticity state | learning-control state | `opaque` | null or frozen in inference-only mode |
| `f_(θ_t)` | `model_fn` | differentiable model | map | callable or model runtime handle | task model |
| `ι_t` | `iota_t` | composed input | input state | `record{outer_input, context_state}` | result of `InputCompose` |
| `r_t` | `r_t` | projected internal state | fixed real vector | `vector<float>[fixed]` | produced by `Π_r(D_t)` |

## Governance Type Table

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- | --- |
| `Ξ_t` | `Xi_t` | organism-visible core bundle | compound state | `record{r_t, x_t, mu_t, G_t, s_t, q_t, u_t, y_t}` | not the full organism |
| `ρ_t` | `rho_t` | reserve state | reserve variable or vector | `record{available, committed, recovery}` | bounded reserve accounting |
| `Λ_t` | `Lambda_t` | lineage population state | branch population state | `record{branches, scores, status}` | governance ecology |
| `N_t` | `N_t` | niche state | niche registry | `map<string, record>` | niche-local control contexts |
| `m_t` | `m_t` | operating mode | `𝓜` | `enum<string>` | `homeostasis`, `adaptive`, `inflammatory`, `pathological`, `regenerative` |
| `a_t` | `a_t` | governance action | discrete action | `enum<string>` | reserved for governance action only |

## Organism-Visible Core Bundle

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- | --- |
| `x_t` | `x_t` | body-memory state | embodied working state | `record{memory, merge, execution, body}` | implementation may split internally |
| `μ_t` | `mu_t` | belief or estimate state | belief state | `record{belief, uncertainty, estimator_state}` | estimator-owned |
| `G_t` | `G_t` | graph state | graph | `graph` | cognitive-web or pathway graph |
| `s_t` | `s_t` | sensed or regime state | sensed summary | `record{world, regime, incidents}` | may include change-memory |
| `q_t` | `q_t` | quality or viability summary | quality vector or record | `record{confidence, capacity, viability}` | keep semantically narrow per implementation |
| `u_t` | `u_t` | control or outward action | control state | `record{action, tool_call, dispatch}` or `enum<string>` | outward control surface |
| `y_t` | `y_t` | incoming observation | observation state | `record{user_input, tool_input, sensor_input}` | outer observation surface |

## Nervous-System Type Table

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- | --- |
| `A_t` | `A_t` | afferent field | typed afferent bundle | `record{exo, intero, mem, err, gov}` | keep types separated |
| `J_t` | `J_t` | junction state | region-indexed integration state | `map<string, record>` | keyed by region id |
| `K_t` | `K_t` | gate state | region-indexed gate state | `map<string, record>` | keyed by region id |
| `P_t` | `P_t` | routing state | route state bundle | `record{routes, latencies, trust, insulation}` | path registry |
| `E_t` | `E_t` | efferent state | output bundle | `record{act, auto, feedback}` | action and autonomic channels |
| `M_t` | `M_t` | modulator state | fixed real vector | `vector<float>[fixed]` | neuromodulatory posture |
| `H_t` | `H_t` | neural health state | fixed real vector | `vector<float>[fixed]` | health and overload summary |

## Nervous-System Components

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- | --- |
| `A_t^exo` | `A_exo` | afferent channel | typed input set | `set<record>` or `list<record>` | external/user-originated |
| `A_t^intero` | `A_intero` | afferent channel | typed input set | `set<record>` or `list<record>` | internal/body-derived |
| `A_t^mem` | `A_mem` | afferent channel | typed input set | `set<record>` or `list<record>` | memory-derived |
| `A_t^err` | `A_err` | afferent channel | typed input set | `set<record>` or `list<record>` | anomaly-derived |
| `A_t^gov` | `A_gov` | afferent channel | typed input set | `set<record>` or `list<record>` | governance-derived |
| `J_t^(r)` | `J_r` | local junction state | region-local record | `record{e_r, i_r, c_r, s_r, phi_r}` | one per region |
| `K_t^(r)` | `K_r` | local gate state | region-local record | `record{d_r, theta_r, gamma_r, o_r}` | one per region |
| `E_t^act` | `E_act` | action efferent channel | action output state | `record{dispatches}` | outward acts |
| `E_t^auto` | `E_auto` | autonomic efferent channel | internal regulation state | `record{autonomic_updates}` | internal regulation |

## Blood-System Type Table

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- | --- |
| `Pl_t` | `Pl_t` | plasma state | circulation bundle | `record{queue, flow, freshness, routes}` | transport medium |
| `Ma_t` | `Ma_t` | marrow state | production bundle | `record{targets, spawn_budget, demand_bias, template_health}` | worker generation |
| `Li_t` | `Li_t` | lineage state | nonnegative population vector | `vector<float>[fixed]` | virtual blood lineage counts |
| `De_t` | `De_t` | support demand | demand bundle | `record{ctx, health, route, urg, fail}` | support needs |
| `St_t` | `St_t` | stabilization state | stabilization bundle | `record{breaches, locks, patches, isolation}` | platelet-like sealing layer |
| `Cl_t` | `Cl_t` | clearance state | cleanup bundle | `record{debris, quarantine, progress, memory}` | macrophage-like cleanup layer |
| `Hb_t` | `Hb_t` | blood health state | fixed real vector | `vector<float>[fixed]` | blood-layer viability summary |

## Blood-System Components

| Symbol | Code alias | Kind | Mathematical type | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- | --- |
| `Q_t` | `Q_t` | packet queue | set of packets | `list<record>` or `queue<record>` | packet transport surface |
| `F_t` | `F_t` | flow state | flow summary | `record{throughput, congestion}` | circulation health |
| `U_t` | `U_t` | freshness state | urgency/freshness summary | `record{freshness_pressure}` | packet aging surface |
| `Tg_t` | `Tg_t` | marrow targets | target bundle | `map<string, scalar<float>>` | per-lineage target levels |
| `Bg_t` | `Bg_t` | spawn budget | budget scalar or vector | `scalar<float>` or `vector<float>[fixed]` | conservative `v1` may use scalar |
| `Dm_t` | `Dm_t` | demand bias | demand weighting state | `record{weights}` | steers marrow output |
| `Sp_t` | `Sp_t` | template health | health summary | `scalar<float>` or `record` | spawning substrate quality |
| `π_t^(i)` | `packet_i` | typed packet | packet record | `record{kind, payload, freshness, urgency, target, ttl}` | transport unit |

## Operator Signature Table

| Operator | Code alias | Signature | Suggested implementation type | Notes |
| --- | --- | --- | --- | --- |
| `Π_r` | `project_substrate_to_r` | `D_t -> r_t` | function | must preserve projection consistency |
| `ReadCtx` | `build_substrate_context` | `(x_t, G_t, A_t, Pl_t, M_t) -> c_t` | function | explicit organism-conditioned read |
| `InputCompose` | `compose_input` | `(y_t, c_t) -> ι_t` | function | no scattered prompt assembly |
| `ψ_write` | `build_memory_writes` | `(D_t, Ψ_t, Σ_t, B_t) -> Δx_t` | function | memory/body writes |
| `ψ_emit` | `build_action_outputs` | `(D_t, Ψ_t, Σ_t, B_t) -> E_t^act` | function | outward dispatches |
| `ψ_bias` | `build_nervous_bias` | `(D_t, Ψ_t, Σ_t, B_t) -> ΔΣ_t` | function | nervous posture bias |
| `SubstrateUpdate` | `run_substrate_forward` | `(D_t, Ψ_t, Σ_t, B_t) -> D_(t+1)` | function | fast substrate update |
| `GovernanceUpdate` | `update_governance` | `(Ψ_t, D_t, Σ_t, B_t) -> Ψ_(t+1)` | function | slow governance update |
| `NervousUpdate` | `update_nervous_system` | `(Σ_t, D_t, Ψ_t, B_t) -> Σ_(t+1)` | function | nervous-system update |
| `BloodUpdate` | `update_blood_system` | `(B_t, D_t, Ψ_t, Σ_t) -> B_(t+1)` | function | blood-system update |
| `EventPolicy` | `event_policy` | `𝒪_t -> e_t` | function | event selection |
| `PlasticityUpdate` | `plasticity_update` | `(θ_t, ω_t, 𝒪_t) -> (θ_(t+1), ω_(t+1))` | function | gated structural learning |

## Storage Contract

The `v1` storage contract should follow these rules:

- top-level compound states should be stored as named records, not anonymous arrays
- fixed vectors should preserve canonical field order in the glossary or be stored with explicit field names
- enums should be stored as canonical strings, not integer codes without a dictionary
- packets, afferents, and events should remain typed records
- historical aggregates such as `Ω_t` and `Z_t` should not be used as primary storage roots

## Minimal Runtime Contract

At runtime, the implementation should be able to produce at least:

- one current `𝒪_t`
- one projected `r_t = Π_r(D_t)`
- one explicit `PlasticityAllowed_t`
- one current mode `m_t`
- one current governance action `a_t`
- one current outward action channel `E_t^act`

If those objects cannot be surfaced, the implementation is below the current canonical math layer.

## Collision Guard

The following implementation names are reserved:

- `a_t` for governance action
- `alpha_t` for fast activation state
- `O_t` for full organism state
- `Xi_t` for organism-visible core bundle
- `Psi_t` for governance state
- `Sigma_t` for nervous-system state
- `B_t` for blood-system state

## Final Statement

This file is the implementation-facing companion to:

- `CANONICAL_EQUATIONS.md`
- `SYMBOLS_AND_NOTATION_GLOSSARY.md`
- `NOTATION_POLICY.md`

Together, those files now define:

- the canonical system,
- the canonical symbols,
- the notation rules,
- and the implementation type contract.
