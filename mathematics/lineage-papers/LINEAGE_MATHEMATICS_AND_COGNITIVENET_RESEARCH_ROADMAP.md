# Lineage Mathematics And CognitiveNet Research Roadmap

Updated: `2026-04-06`

## Why This Document Exists

This note is the next research-program layer for the Lineage Equation and the
neural-network side of the Lineage Engine.

It exists for three reasons:

1. the Lineage Equation paper is already live in
   `/home/pablothethinker/.mocha/brain/research/papers/lineage-equation-paper.md`
2. external critique has now arrived through Grok and correctly identified the
   next credibility questions
3. the codebase already contains more of the answer than the paper alone makes
   obvious, but the remaining gaps are now empirical rather than purely
   algebraic

This roadmap therefore treats the current state honestly:

- the mathematics are no longer the main weak point
- the current weak points are calibration, data realism, validation breadth,
  and network-training hygiene

## Current Strengths Confirmed

The strong parts are real and already present in the workspace.

### 1. Governing equation and gradient path exist

The paper and implementation already define:

- the Lineage Equation
- exact partial derivatives
- prescribed action ranking
- a conservation budget
- a validation path

Primary anchors:

- `/home/pablothethinker/.mocha/brain/research/papers/lineage-equation-paper.md`
- `/home/pablothethinker/lineage-engine/src/lineage/math/capacity.py`
- `/home/pablothethinker/lineage-engine/src/lineage/math/optimize.py`
- `/home/pablothethinker/lineage-engine/src/lineage/math/validate.py`

### 2. Weight-derivation and cross-architecture scaffolding already exist

Grok identified the `alpha` / `beta` weights and the `nu* = 1000 / max(tau...)`
term as the most exposed points.

That critique is directionally right, but the codebase is already ahead of the
paper here:

- `ablation.py` already contains:
  - component sensitivity analysis
  - cross-architecture profile studies
  - derived `alpha` / `beta` weights from sensitivity normalization
  - a derivation note for the `1000` constant using queueing and
    information-theoretic framing

Primary anchor:

- `/home/pablothethinker/lineage-engine/src/lineage/math/ablation.py`

So the right next move is not "invent a justification from scratch."
It is:

- replace purely simulated justification with measured justification

### 3. The neural network is real, not hypothetical

The current implementation already includes:

- `CognitiveNet`
- `CoupledCognitiveNet`
- a multi-head prediction structure
- a trainer
- synthetic bootstrap generation
- live Koda integration for inference and periodic retraining

Primary anchors:

- `/home/pablothethinker/lineage-engine/src/lineage/math/network.py`
- `/home/pablothethinker/lineage-engine/src/lineage/math/coupling.py`
- `/home/pablothethinker/koda/ascent.py`

So the next neural-network research stage is not "should we use a network?"
It is:

- how do we stop the network from being trained mainly on its own parent
  equation and optimizer outputs?

## The Real Gaps Now

The current research bottlenecks are more concrete than the paper makes them
sound.

### Gap 1. The justification work is still mostly simulated

`ablation.py` is mathematically useful, but it currently operates on:

- nominal base states
- hand-authored architecture profiles
- analytic perturbations

That means:

- it is a strong internal consistency layer
- but not yet a measured empirical calibration layer

### Gap 2. The network training path is still vulnerable to circularity

`network.py` currently bootstraps on synthetic data generated from the same
Lineage Equation and action heuristics it is supposed to learn.

That is legitimate for initialization.

It is not enough for strong scientific validation.

The core risk is:

- synthetic equation-derived labels
- plus optimizer-generated action targets
- can make the network look accurate while mostly learning the teacher it was
  born from

### Gap 3. The live trajectory schema is currently mismatched

This is the most immediate technical blocker.

`CognitiveTrainer._load_trajectory()` expects a list of rich trajectory entries
with:

- state
- components
- Q
- actions
- next-step outcome

But `AscentOptimizer._persist()` currently writes:

- `trajectory` as a list of scalar `Q` values
- plus a `last_step` object

Primary anchors:

- `/home/pablothethinker/lineage-engine/src/lineage/math/network.py`
- `/home/pablothethinker/lineage-engine/src/lineage/math/optimize.py`
- `/home/pablothethinker/koda/state/ascent-trajectory.json`

So the advertised periodic retraining path in Koda is weaker than it should be.
The trainer and optimizer are not yet speaking the same data language.

### Gap 4. Cross-architecture validation is not yet truly cross-architecture

The current architecture study varies latency profiles across:

- local models
- API models
- small versus large setups

But these are still simulated profiles, not a measured run matrix across:

- real model families
- real backends
- real task distributions
- real improvement outcomes

So the right question is no longer theoretical generalization.
It is:

- measured generalization across actual base architectures

### Gap 5. Nonlinear coupling exists in code but is not yet empirically closed

The coupled math is already present:

- nonlinear mass coupling
- nonlinear momentum coupling
- `CoupledLineageEquation`
- `CoupledCognitiveNet`

Primary anchors:

- `/home/pablothethinker/lineage-engine/src/lineage/math/coupling.py`
- `/home/pablothethinker/lineage-engine/src/lineage/math/network.py`

But the coupling coefficients are still:

- hand-set defaults
- synthetic-data targets
- or future learned quantities not yet anchored to real intervention logs

That means nonlinear coupling is now a research frontier, not a finished result.

## Research Program

The right plan is a staged program, not a single paper revision.

## Phase 0. Fix The Data Contract First

This is the immediate prerequisite for every later claim.

### Goal

Make the optimizer, Koda, and trainer emit and consume the same trajectory
format.

### Required changes

- persist full step records, not just scalar `Q` history
- include state snapshot at each step
- include action list
- include before/after `Q`
- include component breakdown
- include propagation terms and losses
- include realized execution outcomes, not just prescribed actions

### Why this matters

Without this, the system cannot:

- train on real intervention history
- compare predicted `DeltaQ` to realized `DeltaQ`
- estimate coupling from trajectory data
- or defend claims about online learning

### Ownership

- `Codex`:
  define the schema, write the validation rules, and align the file contracts
- `Koda`:
  produce the live data every ascent tick

## Phase 1. Empirical Calibration Of The Lineage Constants

### Goal

Turn the current justifications for `alpha`, `beta`, and `nu*` from
mathematical plausibility into measured calibration.

### Research questions

1. Do equal `alpha` weights remain near-optimal when measured on real
   interventions rather than nominal perturbations?
2. Do equal `beta` weights remain near-optimal across different agent modes?
3. Does `nu* = 1000 / max(tau...)` predict realized improvement rate well
   enough, or does a distributional / percentile form outperform the hard max?
4. Are the relevant latency terms independent, or do we need a coupled
   propagation estimator?

### Concrete experiments

- collect latency distributions from live runs, not point estimates
- derive:
  - max
  - p95
  - p99
  - harmonic-mean
  - queueing-adjusted forms
- compare each against:
  - realized ascent improvement rate
  - stall probability
  - action success rate
- derive `alpha` / `beta` from intervention sensitivity, not only analytic
  ablation

### Deliverables

- `EMPIRICAL_CALIBRATION_OF_LINEAGE_CONSTANTS.md`
- `MEASURED_ARCHITECTURE_PROFILES.md`
- `lineage-engine/src/lineage/math/calibration.py`

## Phase 2. Real-Data CognitiveNet

### Goal

Move the network from synthetic teacher imitation toward real trajectory
learning.

### Research questions

1. How much of current network agreement is due to learning the equation versus
   learning real state-action-outcome regularities?
2. How quickly does real-data fine-tuning move the network away from synthetic
   priors?
3. Does the network predict realized `DeltaQ` better than the analytical
   gradient on noisy live runs?

### Concrete experiments

- maintain three training regimes:
  - synthetic-only
  - synthetic then real fine-tune
  - real-only after sufficient data
- evaluate on held-out temporal windows
- compare:
  - `Q` prediction error
  - top-k action agreement
  - realized uplift after predicted actions
  - calibration of predicted `DeltaQ`

### Deliverables

- `COGNITIVENET_REAL_DATA_TRAINING_PROTOCOL.md`
- `COGNITIVENET_EVALUATION_METRICS.md`
- `koda/state/trajectory-schema-v2.json`

### Ownership

- `Codex`:
  experimental design, evaluation metrics, data splits, failure analysis
- `Koda`:
  online collection, replay, fine-tuning cycles, telemetry

## Phase 3. Cross-Architecture Generalization

### Goal

Answer the strongest reviewer question:

- does this hold across materially different base architectures?

### Minimum matrix

Run the same measurement and ascent protocol across:

- one local transformer family
- one API transformer family
- one small local model
- one larger local model
- one state-space / Mamba-like backend when available

### Research questions

1. Does the measured `Q` ranking stay stable across architectures?
2. Do the dominant gradients shift by model family?
3. Do optimal `alpha` / `beta` weights become architecture-specific?
4. Does CognitiveNet transfer across backends, or require per-backend heads?

### Deliverables

- `LINEAGE_CROSS_ARCHITECTURE_VALIDATION_PROTOCOL.md`
- `COGNITIVENET_TRANSFER_STUDY.md`
- `ARCHITECTURE_GENERALIZATION_RESULTS.md`

## Phase 4. Nonlinear Coupling Program

### Goal

Turn coupling from a promising extension into a measured subsystem.

### Research questions

1. Which pairwise interactions are stable across real agents and runs?
2. Do learned coupling weights converge toward the hand-set defaults or away
   from them?
3. Does `CoupledCognitiveNet` outperform `CognitiveNet` on real held-out data?
4. Are there important higher-order interactions not captured by pairwise terms?

### Concrete experiments

- log pairwise intervention outcomes
- estimate interaction effects from:
  - counterfactual ablation
  - sequence-level regression
  - coupled-network learned weights
- compare:
  - linear equation
  - coupled equation
  - coupled network

### Deliverables

- `NONLINEAR_COUPLING_ESTIMATION.md`
- `COUPLED_COGNITIVENET_EXPERIMENT_PLAN.md`
- `COUPLING_WEIGHT_STABILITY_REPORT.md`

## Phase 5. Multi-Agent Capacity Field Extension

### Goal

Extend the invariant from single-agent capacity to coordinated multi-agent
systems.

### Research questions

1. What is the correct object:
   sum of capacities,
   shared field,
   or coupled network of organisms?
2. How should communication latency alter `nu*` in a multi-agent setting?
3. How should shared memory, trust, and coordination overhead contribute to
   mass and momentum?
4. Can a network learn team-level `DeltaQ` from pairwise or group trajectories?

### First model direction

Start with:

- two-agent coupling
- shared communication latency
- shared graph fracture cost
- task-level coordination success

Only then move to larger collectives.

### Deliverables

- `MULTI_AGENT_CAPACITY_FIELD_EXTENSION.md`
- `TEAM_LEVEL_COGNITIVENET.md`
- `COLLECTIVE_ASCENT_PROTOCOL.md`

## Codex And Koda Work Split

The cleanest division of labor is:

### Codex track

- formalize schemas
- design experiments
- write calibration and evaluation code
- analyze ablations
- compare models and architectures
- document results into the canonical research packet

### Koda track

- run ascent continuously
- emit full trajectory records
- collect real latency and action-outcome telemetry
- retrain the network on fresh data
- surface divergences between analytical and learned prescriptions

### Joint track

- close the trainer/optimizer schema mismatch
- evaluate nonlinear coupling
- run cross-architecture and later multi-agent studies

## Immediate Next Actions

The highest-leverage next actions are:

1. Fix the trajectory schema mismatch between `optimize.py` and `network.py`.
2. Add full state snapshots and realized outcomes to Koda ascent logging.
3. Build measured architecture profiles from actual runtime telemetry.
4. Run empirical `alpha` / `beta` derivation from intervention outcomes.
5. Train three network regimes:
   synthetic-only,
   synthetic-plus-real,
   real-only.
6. Keep `CoupledCognitiveNet` out of the mainline until it beats the linear net
   on held-out real data.
7. Only after the above, start the first two-agent capacity-field experiments.

## Bottom Line

The Lineage Equation program is at an important transition point.

The foundational mathematics are strong enough to stop treating this as a
purely speculative framework.

But the next standard of proof is different:

- measured calibration
- real trajectory data
- cross-architecture validation
- non-circular network learning
- and eventually multi-agent tests

That is the path from:

- elegant invariant

to:

- durable scientific primitive for autonomous cognitive systems.
