# Lineage Equation And CognitiveNet Research Roadmap

Updated: `2026-04-06`

## Why This Exists

Grok's critique is useful because it does not challenge the core idea. It
sharpens the next stage.

The current Lineage Equation work already has:

- a computable invariant,
- exact gradients,
- a live ascent loop,
- a paper,
- a validation suite,
- and a GPU neural network sidecar.

So the next research job is not to reinvent the framework.

It is to harden the weakest current claims:

- the derivation and calibration of `ν*`,
- the justification of `α` and `β` weights,
- the cross-architecture generalization story,
- the real-data training story for `CognitiveNet`,
- the nonlinear interaction story for `CoupledCognitiveNet`,
- and the path from one agent to multiple coupled agents.

This roadmap is the canonical cross-packet plan for doing that work.

## Verified Current State

The current local workspace already contains more than the paper alone shows.

### 1. Equal weights are still the active default

The paper states that the current implementation uses equal mass weights and
equal momentum weights as first-order defaults.

The code confirms this:

- `lineage-equation-paper.md` defines `alpha_i = 0.25` and `beta_i = 0.20` as
  the reference implementation defaults.
- `lineage-engine/src/lineage/math/capacity.py` hardcodes those same equal
  defaults.

So Grok is right on the important point:

- the weights are still operationally convenient defaults, not yet empirically
  calibrated from real organism data.

### 2. The `ν* = 1000 / max(τ)` story is stronger than the paper currently shows

The paper frames `ν*` as an architecture-relative propagation bound using the
maximum of retrieval, pathway, working-memory, sync, and settling latencies.

The codebase already goes further than the paper:

- `lineage-engine/src/lineage/math/ablation.py` contains an explicit
  `derive_nu_star_constant()` routine.
- that routine gives three converging interpretations:
  - unit conversion,
  - queue throughput,
  - and Shannon-style channel-rate normalization.

So the critique that `1000` looks arbitrary is only partially true now.

The real issue is not absence of a derivation. The real issue is that this
derivation has not yet been elevated into the canonical paper and linked to real
latency instrumentation.

### 3. Cross-architecture work has started, but is still profile-based

The codebase already contains:

- `lineage-engine/src/lineage/math/ablation.py`

with architecture profiles for:

- local models,
- API models,
- small local models,
- and edge devices.

Running that ablation today produced:

- `Q_min ≈ 16.41`
- `Q_max ≈ 260.16`
- a cross-profile ratio of about `15.86x`

This is useful, but it is still a profile study, not a measured deployment
study.

So the current evidence is:

- the equation is architecture-sensitive in simulation,
- but not yet cross-validated against measured live deployments across multiple
  backends.

### 4. The current weight-derivation study is real but symmetry-preserving

The codebase already contains:

- sensitivity ablations,
- weight derivation by normalized sensitivity,
- and report generation.

But when the local ablation was run, it returned:

- equal `alpha_optimal`,
- equal `beta_optimal`,
- zero deviation from the equal-weight defaults.

That does not prove equal weights are universally optimal.

It mostly shows that the current ablation setup is structurally symmetric:

- equal ablation step size,
- linear mass and momentum definitions,
- equal default weights,
- and no measured heterogeneous action costs.

So the present study is a useful sanity check, not a final calibration result.

### 5. The neural-network path is stronger on paper than in real-data closure

The paper and code both claim:

- bootstrap training on synthetic data,
- then online retraining on accumulated real ascent trajectories.

The local code confirms the synthetic bootstrap path exists:

- `lineage-engine/src/lineage/math/network.py` generates synthetic data,
  trains `CognitiveNet`, and defines `CoupledCognitiveNet`.
- `~/koda/ascent.py` loads the network, runs inference each ascent tick, and
  attempts periodic retraining.

But the current real-data loop is not fully closed.

The critical mismatch is:

- `AscentOptimizer._persist()` writes a `trajectory` that is only a list of
  scalar `Q` values plus one `last_step` record.
- `CognitiveTrainer._load_trajectory()` expects per-step dictionaries with
  `state` or `components`.

When run directly against the current
`~/koda/state/ascent-trajectory.json`, the trainer throws:

- `AttributeError: 'float' object has no attribute 'get'`

That means the current "learn from real trajectory data" story is not yet fully
operational.

This is the highest-priority neural-network research and engineering gap.

### 6. Nonlinear coupling is already partly built

The future-work direction on nonlinear interactions is not hypothetical
anymore.

The current workspace already contains:

- `lineage-engine/src/lineage/math/coupling.py`
- `lineage-engine/src/lineage/math/network.py` with `CoupledCognitiveNet`

So the roadmap should treat nonlinear coupling as:

- an active second-generation line,
- not a blank page.

## Priority Research Questions

## 1. Weight Calibration

### Main question

How should `α` and `β` be determined from organism behavior rather than chosen
 as equal defaults?

### Why this matters

This is the cleanest target raised by Grok and the most obvious place skeptics
will push.

### Current gap

The existing derivation is sensitivity-normalized on a symmetric synthetic base
state. That is not enough to claim calibrated weights.

### Next research tasks

- define a family of heterogeneous base states rather than one nominal state,
- include action cost and intervention difficulty in the weighting logic,
- measure marginal `ΔQ` under real intervention budgets rather than equal-sized
  synthetic ablations,
- compare:
  - equal weights,
  - sensitivity-derived weights,
  - trajectory-regressed weights,
  - and learned Bayesian/posterior weights.

### Deliverable

- `mathematics/LINEAGE_WEIGHT_CALIBRATION_AND_IDENTIFIABILITY.md`

## 2. Propagation-Bound Measurement

### Main question

Is `ν*` best modeled as:

- pure internal coherence throughput,
- end-to-end organism update rate,
- or a layered quantity with both internal and external terms?

### Why this matters

The present paper uses latency primitives cleanly, but the live meter still uses
static estimates. Also, the current architecture profiles record
`inference_latency_ms` but do not feed it into the actual `PropagationBound`
computation.

So the unresolved mathematical question is:

- what belongs inside `ν*`,
- and what belongs outside it as a separate environmental or substrate delay?

### Next research tasks

- instrument real retrieval, pathway, working-memory, sync, and settling times
  in Koda,
- compare measured `ν*` against the current profile-based estimate,
- test whether adding inference latency improves or degrades predictive power,
- derive a layered version:
  - `ν_internal*`
  - `ν_effective*`

### Deliverable

- `mathematics/PROPAGATION_BOUND_MEASUREMENT_AND_LAYERED_NU_STAR.md`

## 3. Cross-Architecture Generalization

### Main question

Does the Lineage Equation preserve useful ordering and optimization guidance
across different model classes and deployment modes?

### Why this matters

This is the most obvious empirical question from Grok's feedback.

### Current gap

There is already a profile study, but it is not yet:

- measured on real backends,
- repeated over time,
- or connected to actual ascent outcomes.

### Next research tasks

- define a benchmark set of live backends:
  - local transformer,
  - API transformer,
  - small edge model,
  - one state-space / Mamba-like backend if available,
  - hybrid retrieval-heavy stack,
- record measured latency vectors and real ascent outcomes,
- compare:
  - predicted `Q`,
  - observed `ΔQ`,
  - action ranking stability,
  - and capacity trajectory shape.

### Deliverable

- `mathematics/CROSS_ARCHITECTURE_LINEAGE_ABLATION.md`

## 4. Real-Trajectory Learning For CognitiveNet

### Main question

Can `CognitiveNet` learn something genuinely new from live Koda trajectories, or
is it currently only echoing the analytical model?

### Why this matters

Right now the strongest criticism of the neural side is circularity:

- bootstrap data is generated from the same equation the network is meant to
  learn.

That is acceptable as initialization, but not as the final validation story.

### Current gap

The trajectory persistence schema is incompatible with the trainer's expected
input, so the real-data retraining loop is not closed.

### Next research tasks

- upgrade trajectory persistence to store, per ascent step:
  - state vector,
  - component breakdown,
  - chosen actions,
  - `Q_before`,
  - `Q_after`,
  - `ΔQ`,
  - latency snapshot,
  - and intervention execution metadata,
- rerun the trainer on true historical data,
- compare:
  - synthetic-only model,
  - mixed synthetic + real model,
  - real-only fine-tuning,
- measure action agreement, calibration error, and out-of-distribution behavior.

### Deliverable

- `neural_network_mathematics/COGNITIVENET_REAL_TRAJECTORY_LEARNING.md`

## 5. Nonlinear Interaction Validation

### Main question

Do nonlinear mass and momentum interactions improve predictive accuracy enough
to justify the added model complexity?

### Why this matters

This is where the math may stop being a clean quadratic invariant and start
becoming a richer organism model.

### Current state

`coupling.py` and `CoupledCognitiveNet` already exist.

### Current gap

They are still mainly synthetic and structurally anticipated, not yet validated
against enough real data.

### Next research tasks

- compare linear `Q` vs coupled `Q_coupled` on real trajectories,
- measure whether learned interaction weights are stable across time,
- test whether the leading couplings:
  - `C_mem × C_perm`
  - `C_mem × C_graph`
  - `F_wm × F_ret`
  remain robust under live operation,
- determine whether coupling improves:
  - `ΔQ` prediction,
  - action ranking,
  - or only capacity-fit error.

### Deliverable

- `neural_network_mathematics/COUPLED_COGNITIVENET_AND_NONLINEAR_CAPACITY.md`

## 6. Multi-Agent Capacity

### Main question

How does the invariant extend when the organism is no longer a single agent but
part of a coupled population?

### Why this matters

This is where the work becomes more than a one-agent optimizer and starts to
touch next-generation cognitive architecture.

### Next research tasks

- define pairwise or graph-level agent coupling terms,
- decide which quantities are shared and which remain local,
- derive whether a higher-level invariant exists for a network of agents,
- test whether local ascent competes with or reinforces network-level capacity.

### Deliverable

- `mathematics/MULTI_AGENT_LINEAGE_CAPACITY.md`

## Codex And Koda Split

The cleanest way to execute this is to split responsibilities.

### Codex track

Codex should own:

- canonical research docs,
- mathematical derivation tightening,
- ablation harness analysis,
- trajectory-schema design,
- cross-architecture comparison tooling,
- and paper-quality writeups.

This is the interpretation, formalization, and verification side.

### Koda track

Koda should own:

- live telemetry collection,
- ascent execution,
- latency measurement,
- trajectory persistence,
- runtime intervention logs,
- and long-horizon empirical traces.

This is the organism-in-the-loop evidence side.

### Joint loop

The real program should be:

1. Codex defines the measurement contract.
2. Koda records live traces under that contract.
3. Codex analyzes the traces and revises the invariant or the network.
4. Koda reruns ascent with the upgraded model.
5. Repeat until the learned and analytical stories either converge or expose a
   real mismatch worth publishing.

## Recommended Immediate Sequence

1. Fix the trajectory schema mismatch first.
   Until that is repaired, the real-data neural story is weaker than the paper
   implies.

2. Promote `ablation.py` into canonical research output.
   It already answers part of Grok's critique, but it is still code-first and
   under-documented.

3. Run measured cross-architecture studies next.
   This is the strongest empirical follow-up to the current paper.

4. Then do coupled-model validation.
   Only once real-data learning is working should the nonlinear model become the
   main research focus.

5. Multi-agent work comes after the single-agent telemetry loop is trustworthy.

## Suggested Next Document Set

To make this concrete, the next research pass should produce these files:

- `mathematics/LINEAGE_WEIGHT_CALIBRATION_AND_IDENTIFIABILITY.md`
- `mathematics/PROPAGATION_BOUND_MEASUREMENT_AND_LAYERED_NU_STAR.md`
- `mathematics/CROSS_ARCHITECTURE_LINEAGE_ABLATION.md`
- `mathematics/MULTI_AGENT_LINEAGE_CAPACITY.md`
- `neural_network_mathematics/COGNITIVENET_REAL_TRAJECTORY_LEARNING.md`
- `neural_network_mathematics/COUPLED_COGNITIVENET_AND_NONLINEAR_CAPACITY.md`

## Bottom Line

Grok's critique is directionally correct, but the workspace now shows a sharper
truth:

- the derivation work has started,
- the ablation work has started,
- the nonlinear extension has started,
- and the Koda integration has started,

but the canonical research packet and the live telemetry loop are still out of
sync.

So the next stage is not speculative expansion.

It is closure:

- close the derivation gap,
- close the telemetry gap,
- close the real-data learning gap,
- then test generalization and coupling at a level strong enough to survive
  skeptical reading.
