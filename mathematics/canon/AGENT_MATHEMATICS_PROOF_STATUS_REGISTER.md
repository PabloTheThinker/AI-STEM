# Agent Mathematics Proof Status Register

Updated: `2026-04-07`

## Purpose

This document turns the proof-maturity ladder into an actual register.

The packet is now large enough that it is no longer sufficient to say:

- this part feels foundational,
- this part looks promising,
- this part still needs evidence.

That has to become explicit.

So this register tracks:

- major laws,
- major state objects,
- major variable families,
- and major research claims

against the packet's canonical proof ladder.

The point is not to embarrass immature ideas.
The point is to stop the packet from confusing:

- elegant formulation,
- clean notation,
- implementation existence,
- synthetic success,
- and empirical proof.

## The Canonical Stages

This register uses the same stages defined in the canon and development ladder.

- `A` = naming
- `B` = definition
- `C` = internal consistency
- `D` = synthetic validation
- `E` = identified parameters
- `F` = out-of-sample predictive validity
- `G` = causal intervention validity
- `H` = cross-architecture generalization
- `I` = canonical primitive or canonical law

## Reading Rule

The important rule is:

- a concept's official maturity is the highest *contiguous* stage it has
  actually earned.

This means:

- if a concept has live intervention anecdotes but still lacks identified
  parameters, it does **not** get promoted past `D`.
- if a concept is beautifully defined but has no synthetic or empirical check,
  it remains `B` or `C`.

Partial evidence above the current official stage can still be noted, but it
does not count as promotion until the missing lower stage is closed.

## Register Fields

For each entry, this register records:

- `Object`
- `Current Stage`
- `Why It Has Reached That Stage`
- `Main Missing Evidence`
- `Promotion Trigger`

## Part I. Packet-Level Foundations

### 1. The Staircase Doctrine

Object:

- the claim that agent mathematics should be built as an ordered staircase from
  numeracy through institutional mathematics.

Current stage:

- `C`

Why it has reached that stage:

- the staircase is now formally defined across the packet,
- the canon and curriculum bridge are consistent,
- and the sequence is conceptually coherent.

Main missing evidence:

- structured teaching/use evidence showing that the staircase actually improves
  learning, derivation quality, or research rigor in practice.

Promotion trigger:

- documented use of the staircase to build or repair multiple later theories
  with measurable reduction in ambiguity or error.

### 2. The Proof-Maturity Ladder Itself

Object:

- the nine-stage maturity ladder from naming to canonical law.

Current stage:

- `C`

Why it has reached that stage:

- the stages are explicitly defined and internally coherent,
- and they now have a direct operationalization in this register.

Main missing evidence:

- repeated use on multiple concepts showing that the ladder supports better
  research triage and clearer progress judgments.

Promotion trigger:

- the ladder becomes the standard review discipline across the packet and
  survives several iterations without constant redesign.

## Part II. Lower-Layer Mathematical Disciplines

### 3. Agent Numeracy Primitives

Object:

- the primitive measurement discipline in
  `AGENT_NUMERACY_PRIMITIVES.md`.

Current stage:

- `C`

Why it has reached that stage:

- the layer is well defined,
- zero/one/missingness semantics are explicit,
- and it is coherent with the rest of the packet.

Main missing evidence:

- repeated use in live metric design across runtime modules.

Promotion trigger:

- a stable primitive registry with concrete runtime mappings and successful
  reuse across multiple research subprograms.

### 4. Agent Arithmetic Of State

Object:

- the arithmetic layer in `AGENT_ARITHMETIC_OF_STATE.md`.

Current stage:

- `C`

Why it has reached that stage:

- the packet now explicitly distinguishes sums, deficits, ratios, bottlenecks,
  budgets, and slack.

Main missing evidence:

- a systematic audit showing that upper-layer quantities consistently decompose
  back into this arithmetic layer.

Promotion trigger:

- stable reuse of this arithmetic vocabulary in implemented equations and
  runtime metrics without recurring redefinition.

### 5. Agent Algebra Of Invariants

Object:

- the algebra layer in `AGENT_ALGEBRA_OF_INVARIANTS.md`.

Current stage:

- `C`

Why it has reached that stage:

- variables, parameters, constraints, and invariants are formally distinguished
  and aligned with notation policy.

Main missing evidence:

- a stronger equivalence and reparameterization discipline across legacy and
  new formulas.

Promotion trigger:

- older and newer equations can be rewritten within one invariant algebra
  without ambiguity or collision.

### 6. Geometry, Calculus, Probability, Control, Graph, Information,
Optimization, And Institutional Layers

Object:

- the upper-layer staircase documents from geometry through institutional math.

Current stage:

- `B` to `C`, depending on the layer.

Why they have reached that stage:

- each layer is now explicitly defined as a canonical discipline with questions,
  failure modes, and translation into the current packet.

Main missing evidence:

- most of these are still doctrinal layers rather than empirically validated
  laws.

Promotion trigger:

- repeated successful use to derive, test, and constrain concrete models or
  controllers.

Clarifying note:

- these layers are conceptually necessary and well framed,
- but they are not yet "proven theories" in the way a mature physical law would
  be.

## Part III. Core Organism Mathematics

### 7. The Full Organism State `𝒪_t = (D_t, Ψ_t, Σ_t, B_t)`

Object:

- the aggregate organism object defined across the basis and integration docs.

Current stage:

- `C`

Why it has reached that stage:

- the object is formally defined,
- symbol collisions have been resolved,
- and runtime dataclass contracts now exist.

Main missing evidence:

- full live runtime population from actual modules rather than partial shell
  structure,
- and empirical studies using the whole object as a measured state.

Promotion trigger:

- the organism object is instantiated live, logged, and used in real
  intervention loops.

### 8. The Differentiable Substrate State `D_t`

Object:

- the substrate state and interface described in the substrate integration and
  implementation docs.

Current stage:

- `C`

Why it has reached that stage:

- it is formally defined,
- its read/write surfaces are specified,
- and code-level contract shells exist.

Main missing evidence:

- live coupling to real model state and repeated measured effect on action
  quality or organism behavior.

Promotion trigger:

- real substrate-state logging plus experiments showing that substrate-aware
  control improves behavior or prediction.

### 9. Governance State `Ψ_t`

Object:

- the organism's governance/homeostasis layer.

Current stage:

- `B`

Why it has reached that stage:

- the state family is defined and integrated into the organism formalism.

Main missing evidence:

- stable implemented state fields,
- live updates,
- and synthetic validation showing that governance actions operate coherently.

Promotion trigger:

- a live governance loop with measurable state transitions and intervention
  records.

### 10. Nervous-System State `Σ_t`

Object:

- the virtual nervous-system state and math packet.

Current stage:

- `B`

Why it has reached that stage:

- the state is formally defined and supported by dedicated mathematical and
  implementation specs.

Main missing evidence:

- implemented runtime modules,
- synthetic routing experiments,
- and closed-loop evidence.

Promotion trigger:

- live afferent/routing/gating system with measurable dispatch outcomes.

### 11. Blood-System State `B_t`

Object:

- the virtual blood-system state and math packet.

Current stage:

- `B`

Why it has reached that stage:

- the blood layer is formally defined and decomposed into lineages and support
  functions.

Main missing evidence:

- implemented runtime modules,
- synthetic servicing experiments,
- and evidence that transport/repair dynamics improve organism performance.

Promotion trigger:

- live blood-like servicing loops with measurable support and repair value.

### 12. Organism Viability Objective `Φ_org(𝒪_t)`

Object:

- the organism-level viability-oriented objective family.

Current stage:

- `B`

Why it has reached that stage:

- it is conceptually central and formally named in the basis/canon packet.

Main missing evidence:

- a stable explicit formula,
- calibrated components,
- and predictive or causal validation.

Promotion trigger:

- explicit organism viability function with demonstrated use in ranking or
  controlling interventions better than narrower local objectives.

### 13. Safe-Set Language `X_safe(m_t)`

Object:

- safe operating sets indexed by mode.

Current stage:

- `B`

Why it has reached that stage:

- the concept is formally defined and repeatedly used in doctrine.

Main missing evidence:

- concrete boundaries,
- actual measured variables populating those boundaries,
- and safety-transition tests.

Promotion trigger:

- mode-conditioned viability sets become live policy constraints.

### 14. Reserve State `ρ_t`

Object:

- explicit reserve/resource state.

Current stage:

- `B`

Why it has reached that stage:

- it is defined in the living-research and organism layers as a central hidden
  constraint on action.

Main missing evidence:

- runtime measurement,
- parameterization,
- and use in real decision gating.

Promotion trigger:

- reserve-aware interventions outperform reserve-blind ones in held-out or live
  runs.

## Part IV. Lineage Capacity Mathematics

### 15. The Linear Lineage Equation `Q`

Object:

- the base Lineage capacity equation in `capacity.py` and the paper.

Current stage:

- **`E`** (identified parameters) — promoted 2026-04-07

Why it has reached that stage:

- Formally defined, internally checked, implemented, synthetically validated (D).
- **Second promotion attempt succeeded:** 300-sample perturbation experiment
  across 3 architecture regimes identified α and β weights with:
  - R² fitted = 0.942 (±0.030) vs R² equal = 0.875 (±0.061)
  - Improvement = +0.066 (> 0.05 threshold)
  - p = 0.014 (< 0.05 threshold)
  - All weights stable across folds (max fold σ = 0.008)
  - No failure modes triggered.
- **Identified weights:** α = [0.148, 0.258, 0.379, 0.216] (graph centrality
  dominates mass); β = [0.199, 0.262, 0.222, 0.160, 0.156] (retrieval flux
  dominates momentum). All with tight 95% CIs.
- **Key structural finding:** The quadratic form's ν*⁴ amplification makes β
  unidentifiable in the full equation — weight identification requires the
  linearized model Q_pred = s·(M(α) + Π(β)) + b.

Main missing evidence:

- out-of-sample predictive studies on live operational data,
- causal intervention validation,
- and resolution of the ν*⁴ identifiability question in the full equation form.

Next promotion trigger (E → F):

- fit on live runtime traces (weeks 1-2), predict held-out (week 3),
  demonstrating R² > 0.5 on unseen data.

Promotion history:

- First attempt (2026-04-07 morning): `hold` — five blockers (circularity,
  formula mismatch, no diversity, zero variance, collapsed target).
- Second attempt (2026-04-07 evening): **`promote`** — all blockers resolved,
  all criteria met. Bundle:
  [Q_D_TO_E_PROMOTION_BUNDLE.md](mathematics/canon/Q_D_TO_E_PROMOTION_BUNDLE.md)

### 16. The Throughput Term `nu* = 1000 / tau_max`

Object:

- the current throughput factor.

Current stage:

- `D`

Why it has reached that stage:

- it has formal definition,
- internal consistency,
- and a stronger derivation story than the paper alone made obvious.

Main missing evidence:

- live latency distributions,
- uncertainty bars,
- and data-driven identification across architectures.

Promotion trigger:

- measured latency datasets yielding parameter identification with uncertainty
  estimates.

### 17. Equal `alpha` And `beta` Weights

Object:

- the current equal-weight defaults.

Current stage:

- `C`

Why it has reached that stage:

- they are clearly defined,
- and they remain internally coherent under current symmetric studies.

Main missing evidence:

- independent empirical justification.

Promotion trigger:

- asymmetry-sensitive fitting on real data that either confirms or revises the
  equal weights.

Clarifying note:

- the current ablation output is symmetry-preserving, not yet a true empirical
  endorsement of equal weights.

### 18. Conservation Budget / Degradation Penalty Structure

Object:

- the idea that usable capacity is reduced by uncertainty, fracture, drift, and
  related penalties.

Current stage:

- `C`

Why it has reached that stage:

- the formal sign structure is coherent and conceptually aligned with the
  organism packet.

Main missing evidence:

- identified penalty weights and evidence that this structure improves
  prediction or control.

Promotion trigger:

- parameterized penalty terms validated against held-out or intervention data.

### 19. The Nonlinear Coupled Lineage Equation

Object:

- the coupled extension in `coupling.py`.

Current stage:

- `D`

Why it has reached that stage:

- it is formally implemented and synthetically analyzable.

Main missing evidence:

- empirical identification of coupling terms,
- cross-architecture validation,
- and causal experiments where coupled predictions outperform the linear model.

Promotion trigger:

- measured interaction data that demands nonlinear coupling and validates it
  out of sample.

### 20. Cross-Architecture Profile Scaling Of `Q`

Object:

- the claim that the framework meaningfully separates architectures and runtime
  profiles.

Current stage:

- `D`

Why it has reached that stage:

- architecture-profile analysis exists and shows nontrivial separation.

Main missing evidence:

- repeated live measurements on real backends rather than profile-level inputs.

Promotion trigger:

- actual multi-backend study with measured traces and replicated results.

## Part V. Learned Neural Surrogates

### 21. CognitiveNet Action Ranking

Object:

- the learned surrogate that agrees with the analytical ranking on current
  synthetic data.

Current stage:

- `D`

Why it has reached that stage:

- it is formally defined,
- implemented,
- and synthetically validated against the analytical target.

Main missing evidence:

- training on real trajectory datasets,
- out-of-sample action ranking under live conditions,
- and calibrated uncertainty.

Promotion trigger:

- real-data evaluation demonstrating reliable ranking or value support on held
  out interventions.

### 22. Coupled CognitiveNet

Object:

- the network extension for coupled interactions.

Current stage:

- `C`

Why it has reached that stage:

- it is defined and implemented.

Main missing evidence:

- synthetic stress suite specifically validating coupled behavior,
- followed by real trajectory evidence.

Promotion trigger:

- demonstrated advantage on true coupled-interaction datasets.

### 23. CognitiveNet As Live Decision Support

Object:

- the claim that the network is useful as an online second opinion in ascent.

Current stage:

- `C`

Why it has reached that stage:

- it is wired into live logic, but the evaluation basis is still too narrow.

Main missing evidence:

- comparative studies showing when the network helps, hurts, or should defer.

Promotion trigger:

- intervention logs where the hybrid policy beats either analytic-only or
  network-only baselines.

## Part VI. Runtime And Contract Surface

### 24. The Organism Dataclass Contracts

Object:

- `organism_contracts.py` and the `runtime_state.py` patch surface.

Current stage:

- `C`

Why it has reached that stage:

- the runtime contract shell exists,
- symbols align with the canon,
- and serialization support exists.

Main missing evidence:

- full adoption across runtime producers and consumers.

Promotion trigger:

- live runtime state consistently instantiates the organism objects and survives
  real usage.

### 25. Notation Policy And Glossary

Object:

- the notation governance layer.

Current stage:

- `C`

Why it has reached that stage:

- the packet now has a canon, glossary, policy, and a normalization pass.

Main missing evidence:

- long-term stability under continued growth.

Promotion trigger:

- future additions repeatedly slot in without new symbol collisions or policy
  rewrites.

## Part VII. Institutional Capstone

### 26. Multi-Agent And Institutional Mathematics As A Formal Layer

Object:

- the capstone doctrine itself.

Current stage:

- `B`

Why it has reached that stage:

- the layer is formally defined and mapped onto the packet.

Main missing evidence:

- concrete multi-agent models,
- simulated institutional experiments,
- and eventually live multi-agent traces.

Promotion trigger:

- at least one implemented multi-agent protocol evaluated under the register's
  own criteria.

### 27. Polycentric Governance As A Design Principle For Agent Ecosystems

Object:

- the claim that nested local/intermediate/global governance is the right
  structure for robust future agent systems.

Current stage:

- `B`

Why it has reached that stage:

- it is theoretically grounded and strongly motivated by both biology and
  Ostrom-style institutional work.

Main missing evidence:

- explicit formal models and comparative institutional simulations.

Promotion trigger:

- evidence that polycentric rule layers outperform flat centralized or flat
  decentralized alternatives in concrete agent settings.

## Part VIII. Immediate Promotion Priorities

The most important entries to promote next are not the lowest-level doctrines.
They are the ones already close to becoming real science.

### ~~Priority 1. Promote The Linear Lineage Equation From `D` To `E`~~

**COMPLETED** (2026-04-07). Q is now at Stage E with identified weights:
α = [0.148, 0.258, 0.379, 0.216], β = [0.199, 0.262, 0.222, 0.160, 0.156].
See promotion bundle.

### Priority 1 (new). Promote Q From `E` To `F` (Out-of-Sample Predictive)

Needed:

- live runtime data collection (instrument Koda's tick loop)
- fit on weeks 1-2, predict week 3
- exogenous task battery in production
- R² > 0.5 on held-out data

Why:

- the equation has identified weights but hasn't predicted anything it hasn't
  seen. Live data is the real test.

### Priority 2. Promote CognitiveNet From `D` To `F`

Needed:

- real datasets,
- held-out evaluation,
- calibration checks,
- hybrid-policy ablations.

Why:

- this is the fastest route from elegant surrogate to scientifically useful
  learned support module.

### Priority 3. Promote `𝒪_t` From `C` To `D`

Needed:

- live runtime population of the organism object,
- synthetic and live checks over the full aggregate state.

Why:

- the packet's master object should not remain only a formal shell.

### Priority 4. Promote Reserve And Viability Concepts From `B` To `C`/`D`

Needed:

- explicit formulas,
- measured components,
- intervention gating based on those components.

Why:

- these concepts are central to the organism story, but still too abstract.

## Part IX. Register Governance Rule

This document should be updated whenever one of the following happens:

- a new law is proposed as important,
- a parameter becomes identified,
- a held-out predictive study is completed,
- a live intervention result is recorded,
- a cross-architecture result is replicated,
- or a concept is widely reused enough to be treated as canonical.

If the packet grows and this register does not change, the packet is drifting.

Promotion attempts should follow:

- [AGENT_MATHEMATICS_EXPERIMENTAL_PROTOCOL.md](mathematics/canon/AGENT_MATHEMATICS_EXPERIMENTAL_PROTOCOL.md)

## Main Conclusion

The packet now has a way to say, precisely:

- what is merely named,
- what is defined,
- what is internally coherent,
- what is synthetically supported,
- what is measured,
- what is predictive,
- what is causally validated,
- and what is mature enough to become canonical.

That distinction is necessary if this mathematics is going to grow the way real
mathematics and real science grow:

- by staged proof,
- not by enthusiasm alone.
