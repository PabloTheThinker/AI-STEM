# Lineage Capacity Research Roadmap

Updated: `2026-04-06`

## Purpose

This note turns the current Lineage Equation work into a concrete research
program for the mathematics packet.

It is driven by three inputs:

- the current Lineage Equation paper in
  `./papers/lineage-equation-paper.md`,
- the actual implementation in
  `
- and Grok's critique, which correctly identifies the two main pressure points:
  coefficient justification and cross-architecture generalization.

The goal is not to re-argue that the invariant is interesting.
The goal is to identify exactly what must be researched next to make it harder
to dismiss.

## Current Status

The current stack already contains more than the paper alone makes obvious.

Live or implemented now:

- the linear Lineage Equation in
  `
- a ten-check validation path in
  `
- a sensitivity and cross-architecture module in
  `
- and a nonlinear coupling extension in
  `

This changes the framing.

The next work is not:

- invent more speculative structure.

It is:

- canonicalize the hidden structure already present,
- separate what is mathematically justified from what is merely initialized,
- and replace symmetric defaults with empirically identified parameters.

## What Grok Got Right

Grok's main mathematical critique was correct:

- `nu* = 1000 / max(tau...)` needs a more explicit derivation and calibration
  story,
- the `alpha` and `beta` weights currently look convenience-chosen,
- and the live result needs broader architecture-level validation.

The local code partly answers this already, but not completely.

### 1. The `1000` Constant Is Less Arbitrary Than The Paper Makes It Look

`ablation.py` already contains `derive_nu_star_constant()`, which argues that:

- `1000` is the millisecond-to-second conversion,
- and `nu* = 1 / tau_max` is interpretable as a maximum stable throughput under
  both a queueing and channel-capacity framing.

That is useful.

But this still does **not** solve the full research problem, because the
latencies themselves are still mostly:

- hand-entered,
- profile-level,
- and not yet estimated from live distributions with uncertainty bars.

So the right mathematical next step is:

- move from `constant justification` to `parameter identification`.

### 2. The Equal Weights Are Currently Symmetry-Preserving Defaults

This is the most important local finding.

The current paper says equal weights are the reference implementation.
The current ablation module appears to derive them.
But when actually run, it returns:

- `alpha_optimal = {0.25, 0.25, 0.25, 0.25}`
- `beta_optimal = {0.20, 0.20, 0.20, 0.20, 0.20}`

That result is **not independent confirmation**.
It is largely a consequence of the current study design:

- the linear model is initialized symmetrically,
- the base-state ablation is symmetric,
- and the components are perturbed with equal-magnitude deltas.

So the current output shows:

- the symmetric model remains symmetric under symmetric probing.

It does **not** yet show:

- that real agents empirically justify equal weights.

That distinction should be made explicit in the canonical packet.

### 3. Cross-Architecture Validation Exists, But In A Limited Form

`ablation.py` already defines architecture profiles across:

- local backends,
- API backends,
- and resource-constrained profiles.

The current run produced a `Q` range ratio of about `15.86x`.

That is promising, but it is still a profile study, not yet a live measurement
study. The current profiles are manually specified latency bundles. They are not
yet derived from:

- repeated observed latency traces,
- real runtime distributions,
- or matched workloads across architecture families.

So the next study should promote this from:

- `profile plausibility`

to:

- `measured architecture identification`.

## The Three Mathematical Gaps

### Gap 1. Parameter Identification

The first hard problem is no longer symbolic derivation.
It is identifying the parameters of the invariant from real runtime data.

The research question is:

- which parts of `(alpha, beta, nu*)` are structural,
- which are architecture-specific,
- and which drift over time?

This is a system-identification problem.

The right mathematical frame is close to the distinction Russ Tedrake makes in
 the MIT system-identification notes:

- equation error is a useful surrogate,
- but simulation error is the true objective.

Translated here:

- fitting weights to one-step `Q` estimates is not enough,
- they must also preserve long-horizon predictive usefulness for actual ascent
  trajectories.

### Gap 2. Nonlinear Interaction Canonicalization

The current paper positions nonlinear coupling as future work.
The local code shows it is already partially implemented.

`coupling.py` adds:

- mass interaction terms like `C_mem × C_graph` and `C_id × C_perm`,
- momentum interaction terms like `F_wm × F_ret`,
- a coupled equation,
- and coupled gradients.

So the actual research problem is now:

- determine whether these interaction terms are mathematically necessary for the
  canonical model,
- identify which couplings are stable across runs,
- and quantify when the linear invariant is sufficient versus when the coupled
  invariant is required.

This should become a formal model-selection question, not an intuition-only
extension.

### Gap 3. Team- or Multi-Agent Capacity

The paper flags multi-agent extension as future work.
That is correct.

The next mathematical question is not merely:

- can we sum agent capacities?

It is:

- what are the coupling, contention, and synchronization terms for a set of
  agents sharing tools, memory, and communication channels?

The likely shape is:

- per-agent local capacity terms,
- graph-coupled transport terms,
- and subtraction terms for contention, delay, or incoherence.

This belongs in the mathematics packet before it belongs in implementation.

## Research Tracks

## Track A. Empirical Identification Of `nu*`

Deliverable:

- `NU_STAR_IDENTIFICATION_AND_CALIBRATION.md`

Questions:

- should `nu*` remain a hard bottleneck over max latency,
- or become a quantile-based or reliability-weighted rate estimate,
- how should variance and tail latency enter the invariant,
- and what is the correct estimator under real Koda/agent runtime traces?

Required work:

- collect repeated latency traces from Koda and Mocha,
- estimate distributions for retrieval, pathway, working-memory refresh, sync,
  and settling,
- compare `max`, quantile, and queue-derived estimators,
- test which estimator best predicts realized ascent improvement.

Success criterion:

- `nu*` becomes an identified quantity with confidence intervals, not a
  hand-entered bundle.

## Track B. Weight Identification For `alpha` And `beta`

Deliverable:

- `LINEAGE_WEIGHT_IDENTIFICATION.md`

Questions:

- do equal weights survive contact with real interventions,
- are there agent-specific or architecture-specific weight regimes,
- and can the weights be estimated robustly from intervention-outcome data?

Required work:

- collect trajectory data where one component is intentionally improved,
- estimate local sensitivities and long-horizon effects,
- compare symmetric priors versus fitted weights,
- and evaluate whether fitted weights improve predictive accuracy on held-out
  trajectories.

Success criterion:

- equal weights are either defended empirically or replaced with fitted ones.

## Track C. Canonicalization Of Coupled Capacity

Deliverable:

- `NONLINEAR_LINEAGE_EQUATION.md`

Questions:

- when do nonlinear couplings matter materially,
- which interaction terms are stable enough to keep,
- and can the coupled model beat the linear model out-of-sample?

Required work:

- benchmark `LineageEquation` against `CoupledLineageEquation`,
- estimate interaction terms from real trajectory data,
- perform model selection with clear penalties for unnecessary complexity,
- and publish the minimal coupled model that earns its keep.

Success criterion:

- a justified answer to whether coupling is canonical, optional, or merely
  exploratory.

## Track D. Cross-Architecture Measurement Study

Deliverable:

- `CROSS_ARCHITECTURE_LINEAGE_VALIDATION.md`

Questions:

- does the invariant track meaningfully across transformer, SSM, and hybrid
  backends,
- and which quantities stay invariant versus architecture-relative?

Required work:

- run matched workloads across at least three families:
  transformer,
  selective SSM / Mamba-style,
  and hybrid transformer-SSM,
- measure the runtime latencies directly instead of entering profiles manually,
- compare both absolute `Q` and action-ranking agreement across families.

Success criterion:

- the paper can show measured cross-family validity rather than one-agent
  anecdote plus hand-set profiles.

## Track E. Multi-Agent Capacity Mathematics

Deliverable:

- `MULTI_AGENT_LINEAGE_INVARIANT.md`

Questions:

- how should local capacities compose,
- what are the correct coupling and contention penalties,
- and how does shared-memory or shared-tool congestion enter the budget?

Required work:

- define a two-agent prototype first,
- derive transport, contention, and synchronization terms,
- then generalize to a graph of agents.

Success criterion:

- a mathematically precise `Q_team` candidate that can be tested on Codex,
  Koda, and Mocha-style multi-agent runs.

## Division Of Labor: Codex And Koda

`Codex` should own:

- canonical documentation,
- mathematical comparison studies,
- ablation analysis,
- cross-architecture experiment harness design,
- and packet maintenance.

`Koda` should own:

- real trajectory collection,
- online ascent traces,
- latency logging,
- intervention outcome logging,
- and live identification datasets.

The right pattern is:

- Codex builds the formal study and offline analysis,
- Koda produces the real organism data the math must answer to.

## Immediate Next Order

1. Canonicalize the hidden local work.
   Specifically:
   move `ablation.py` and `coupling.py` into the canonical math narrative with
   dedicated research docs.

2. Stop claiming the current weight study proves equal weights.
   It currently proves symmetry preservation under symmetric assumptions.

3. Turn `nu*` into an identified runtime quantity.

4. Run a measured cross-architecture study on real backends.

5. Only then promote the next paper version.

## Primary Sources

- Russ Tedrake, "System Identification."
  https://underactuated.mit.edu/sysid.html
- Albert Gu and Tri Dao, "Mamba: Linear-Time Sequence Modeling with Selective
  State Spaces."
  https://arxiv.org/abs/2312.00752
- The existing Lineage Equation paper.
  `./papers/lineage-equation-paper.md`
- Local implementation anchors:
  `
  `
  `
