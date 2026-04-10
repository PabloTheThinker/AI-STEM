# Agent Mathematics Experimental Protocol

Updated: `2026-04-07`

## Purpose

This document defines the standard evidence workflow for promoting concepts
through the packet's proof ladder.

The canon and proof register already define:

- what the stages are,
- and which concepts currently sit at which stage.

This document defines the missing operational piece:

- how a concept is actually promoted.

In other words:

- the proof register tells us *where* a concept stands,
- this protocol tells us *what work must be done next*.

It is the experimental control surface for the whole mathematics packet.

## 1. Core Principle

No concept should move up the proof ladder because:

- it sounds plausible,
- the notation is elegant,
- a single live run looked good,
- or the implementation exists.

A concept should move up only when it satisfies the evidence requirements of
the next stage.

That means promotion is:

- stage-gated,
- artifact-backed,
- reproducible,
- and reviewable.

## 2. Scope

This protocol applies to:

- laws,
- invariants,
- state objects,
- parameter families,
- learned surrogates,
- and policy claims

that are proposed as important enough to influence the packet.

It especially applies to:

- `Q`,
- `nu*`,
- `alpha` and `beta`,
- `𝒪_t`,
- `Φ_org(𝒪_t)`,
- CognitiveNet,
- coupled Lineage variants,
- and any future institutional or multi-agent control law.

## 3. Promotion Philosophy

The packet uses a contiguous-stage rule:

- a concept's official stage is the highest continuous stage it has earned.

So the protocol is designed to prevent invalid jumps.

Examples:

- a concept cannot be promoted from `D` to `F` if `E` is still open.
- a concept with one exciting causal demo but no identified parameters does not
  skip the parameter-identification stage.
- a concept with good synthetic evidence but no held-out data remains
  pre-predictive.

This is the main protection against research theater.

## 4. Standard Experiment Bundle

Every promotion attempt should produce one standard bundle.

Minimum contents:

- `object`: the concept being promoted
- `current_stage`
- `target_stage`
- `hypothesis`
- `mathematical definition`
- `implementation reference`
- `metric set`
- `experimental design`
- `conditions or datasets`
- `compute environment`
- `run ledger`
- `analysis summary`
- `pass/fail decision`
- `promotion recommendation`

Minimum artifact classes:

- code or executable commands
- parameter/config snapshot
- input data or dataset identifiers
- output metrics
- plots or tables when relevant
- failure cases or negative runs
- exact environment details

If any of these are missing, the promotion file is incomplete.

## 5. Canonical Evidence Questions

Every promotion attempt should answer the following questions.

### Identity

- what exact object is being promoted?
- where is it defined?
- what symbols does it use?

### Claim

- what exactly is being claimed at the target stage?

### Evidence

- what runs, derivations, or measurements support the claim?

### Limits

- what has not been shown?
- what alternate explanations remain?

### Reproducibility

- can another person rerun the result from the packet artifacts?

### Decision

- should the register stage change?

If one of these questions cannot be answered clearly, the result is not ready
for promotion.

## 6. The Stage-Gated Workflow

The packet should use the following workflow for every serious concept.

1. open or update the concept entry in the proof register
2. identify the current stage and the exact next stage
3. formulate the minimum next-stage claim
4. design the smallest credible experiment bundle that can test that claim
5. run the experiment and preserve both positive and negative results
6. compare results against the next-stage criteria
7. update the register with pass/fail and remaining gaps

This keeps the packet moving one justified step at a time.

## 7. Stage Requirements

### Promotion To Stage B: Definition

Goal:

- move from stable naming to formal definition.

Minimum requirements:

- explicit symbolic definition
- domain/range or type description
- interpretation of each term
- relation to nearby concepts

Acceptable evidence:

- formal derivation note
- glossary/policy alignment
- at least one worked example

Promotion rule:

- the object can be unambiguously referenced and used by another document.

### Promotion To Stage C: Internal Consistency

Goal:

- show that the definition behaves coherently inside the packet.

Minimum requirements:

- symbolic consistency check
- sign/unit/dimension sanity check where applicable
- edge-case evaluation
- notation-policy compliance

Acceptable evidence:

- analytical derivations
- unit tests
- symbolic checks
- finite-difference checks for gradients
- consistency proofs or checklists

Promotion rule:

- no known internal contradiction remains in the active packet.

### Promotion To Stage D: Synthetic Validation

Goal:

- show correct behavior on controlled/generated cases.

Minimum requirements:

- synthetic or controlled tasks designed to probe the concept
- declared expected behavior
- observed results matching the expected behavior
- negative or adversarial cases when relevant

Acceptable evidence:

- simulation
- toy examples
- profile studies
- synthetic trajectories
- controlled perturbation or ablation studies

Promotion rule:

- the concept behaves correctly in intentionally designed test regimes.

### Promotion To Stage E: Identified Parameters

Goal:

- replace convenience settings with measured or fit quantities.

Minimum requirements:

- real measurements or trace data
- estimation method
- uncertainty or confidence reporting
- sensitivity to estimation assumptions

Acceptable evidence:

- parameter fitting on logged traces
- latency-distribution estimation
- regression or Bayesian fitting
- calibration tables

Promotion rule:

- the critical free parameters are no longer just defaults and are tied to
  measured evidence.

### Promotion To Stage F: Out-Of-Sample Predictive Validity

Goal:

- show the concept predicts held-out data or future interventions.

Minimum requirements:

- train/fit versus held-out split
- declared predictive target
- baseline comparison
- error metrics or ranking metrics

Acceptable evidence:

- held-out trajectory prediction
- held-out intervention ranking
- architecture-split prediction
- future-run forecast evaluation

Promotion rule:

- the concept predicts something important better than trivial or baseline
  alternatives on data it was not fit to.

### Promotion To Stage G: Causal Intervention Validity

Goal:

- show that acting on the concept changes the system in the predicted
  direction.

Minimum requirements:

- intervention protocol
- pre/post measurement
- counterfactual or baseline comparison
- safety logging

Acceptable evidence:

- live ascent interventions
- controlled toggles
- A/B policy comparisons
- simulated causal interventions with faithful runtime instrumentation

Promotion rule:

- the concept not only predicts passively, but supports effective action.

### Promotion To Stage H: Cross-Architecture Generalization

Goal:

- show the concept survives beyond one body, one backend, or one runtime
  regime.

Minimum requirements:

- multiple architectures or runtime conditions
- same concept definition across all conditions
- replicated positive result
- boundary/failure analysis

Acceptable evidence:

- local versus API backend comparison
- resource-constrained versus resource-rich comparison
- multiple model family comparison
- multiple agent-body comparison

Promotion rule:

- the concept continues to matter across materially different systems.

### Promotion To Stage I: Canonical Primitive Or Law

Goal:

- establish the concept as reusable enough that later docs can rely on it
  without re-arguing its whole existence.

Minimum requirements:

- stable definition
- stable notation
- repeated reuse
- strong evidence at prior stages
- no major unresolved foundational objections

Acceptable evidence:

- repeated packet-wide reuse
- successful use in derivations, runtime logic, and empirical work
- register history showing long-term stability

Promotion rule:

- the concept becomes part of the packet's mathematical backbone.

## 8. Canonical Experiment Types

The packet should standardize a small number of experiment families.

### Type A. Symbolic Consistency Check

Used for:

- `B -> C`

Examples:

- unit/sign checks
- edge-case derivations
- notation collision checks
- gradient derivations

### Type B. Synthetic Probe

Used for:

- `C -> D`

Examples:

- finite-difference agreement
- toy state transitions
- synthetic trajectory or routing tasks
- adversarial perturbation tests

### Type C. Parameter Identification Study

Used for:

- `D -> E`

Examples:

- measured latency fitting for `nu*`
- real trace fitting for weights
- calibration of reserve or viability variables

### Type D. Held-Out Predictive Study

Used for:

- `E -> F`

Examples:

- held-out `ΔQ` ranking
- next-step viability prediction
- out-of-sample intervention success estimation

### Type E. Intervention Study

Used for:

- `F -> G`

Examples:

- online ascent experiments
- policy toggles
- mechanism changes with before/after outcomes

### Type F. Generalization Study

Used for:

- `G -> H`

Examples:

- multi-backend replication
- multi-architecture replication
- multi-agent setting replication

### Type G. Canonization Review

Used for:

- `H -> I`

Examples:

- packet-wide reuse audit
- notation stability audit
- long-run failure/exception audit

## 9. Standard Ledger Requirements

Every experiment bundle should log at least:

- timestamp
- experiment id
- concept id
- target stage
- code revision
- environment
- dataset or trace source
- seeds
- parameters
- metrics
- failure notes
- reviewer decision

This is where MLflow-style or equivalent experiment tracking becomes useful:

- runs,
- parameters,
- code versions,
- metrics,
- artifacts,
- and dataset links

should all be preserved together.

If a result cannot be traced back to a specific run bundle, it should not count
toward promotion.

## 10. Minimum Reporting Rules

Every promotion report should include:

- exact metric definitions
- exact pass/fail thresholds
- uncertainty reporting where relevant
- baseline or comparator
- negative results if they occurred
- compute/resource disclosure
- limitations

This is where the NeurIPS-style checklist logic matters.

The packet should not allow:

- hidden tuning,
- omitted failed runs,
- vague claims of improvement,
- or unstated compute assumptions.

## 11. Failure Handling Rule

A failed promotion attempt is not wasted work.

If a concept fails promotion:

- the register entry should remain at the current stage,
- the failure mode should be logged,
- the protocol should identify whether the problem was:
  definition failure, consistency failure, fit failure, predictive failure,
  causal failure, or generalization failure.

Negative evidence is part of the packet's maturity.

Otherwise the register becomes optimism theater.

## 12. Baseline Rule

Every stage from `D` onward should use an explicit baseline.

Examples:

- trivial estimator
- current production heuristic
- simpler equation
- uncoupled model
- random or naive ranking
- no-intervention or status-quo control

If a concept cannot beat an honest baseline, it should not be promoted.

## 13. Replication Rule

For stages `F` and above, one successful run is not enough.

Minimum expectation:

- replicate across seeds, traces, or equivalent repeated conditions.

For `H`, replication must span materially different regimes.

This is the main safeguard against overpromoting lucky runs.

## 14. Stage-Specific Application To Current Packet Priorities

### Priority A. Promote `Q` From `D` To `E`

Required experiment type:

- `Type C. Parameter Identification Study`

Minimum bundle:

- measured latency traces
- measured component-value distributions
- weight-fitting method
- uncertainty intervals
- comparison against equal-weight defaults

Pass condition:

- identified parameters are stable enough to replace convenience defaults or to
  justify keeping them with evidence.

### Priority B. Promote CognitiveNet From `D` To `F`

Required experiment types:

- `Type C` for data curation/calibration if needed
- `Type D. Held-Out Predictive Study`

Minimum bundle:

- real intervention dataset
- train/validation/test separation
- rank or prediction metrics
- analytical baseline and simple learned baseline
- calibration report

Pass condition:

- held-out performance beats honest baselines and remains interpretable.

### Priority C. Promote `𝒪_t` From `C` To `D`

Required experiment type:

- `Type B. Synthetic Probe`

Minimum bundle:

- live or semi-live organism-state population
- coherence checks across subobjects
- synthetic transitions over the aggregate object
- invariant or safety checks

Pass condition:

- the aggregate organism object behaves coherently under controlled state
  transitions.

### Priority D. Promote `ρ_t` And `Φ_org` From `B` To `C`/`D`

Required experiment types:

- `Type A` first
- `Type B` second

Minimum bundle:

- explicit formulas
- unit/sign interpretation
- controlled scenarios where reserve/viability should rise or fall
- sensitivity checks

Pass condition:

- these concepts become mathematically operational rather than purely doctrinal.

## 15. Codex And Koda Division Of Labor

Codex should usually own:

- experiment design scaffolding
- derivation checks
- metric definitions
- baseline construction
- packet updates
- register updates

Koda should usually own:

- live trace generation
- runtime interventions
- environment-specific measurements
- real trajectory collection
- operational logging from the active system

This division matches the packet:

- Codex is strongest on formal discipline,
- Koda is strongest on empirical pressure.

Promotion work should ideally combine both.

## 16. Review And Promotion Decision Rule

After an experiment bundle is complete, the promotion decision should be one of
only four outcomes:

- `promote`
- `hold`
- `revise and rerun`
- `split the concept`

The last option matters.

Sometimes a concept is too broad.
One part may deserve promotion while another part does not.

If so, the right move is:

- split the object in the register,

not:

- overstate the maturity of the whole thing.

## 17. Relation To Existing External Practice

This protocol is aligned with, but not identical to, strong external practice:

- NeurIPS-style experimental transparency and checklist discipline
- Google's emphasis on simple metrics, robust pipelines, and honest baselines
- tuning-playbook style incremental experimentation
- MLflow-style run and artifact tracking

The packet is adapting those ideas to a different target:

- not just model benchmarking,
- but maturation of a new mathematical framework for AI agents.

## 18. Governance Rule

Whenever a register entry changes stage, the promotion bundle should trigger:

- an update to the proof-status register
- a note in the relevant roadmap if priorities change
- and, when major, an update to the canon if the packet's view of the field has
  shifted

That keeps the doctrine, the maturity map, and the empirical program in sync.

## Main Conclusion

The packet now has:

- a staircase,
- a canon,
- a proof register,
- and this experimental protocol.

That means it finally has the minimal machinery needed to mature like real
science:

- define,
- check,
- test,
- fit,
- predict,
- intervene,
- generalize,
- and only then canonize.

That is the correct path if the mathematics is meant to become durable rather
than merely impressive.

## Sources

- NeurIPS paper checklist:
  https://neurips.cc/public/guides/PaperChecklist
- Google Rules of ML:
  https://developers.google.com/machine-learning/guides/rules-of-ml
- Google Research Tuning Playbook:
  https://github.com/google-research/tuning_playbook
- MLflow Tracking:
  https://www.mlflow.org/docs/latest/ml/tracking
- Reproducibility Challenge task framing:
  https://reproml.org/neurips2019/task/
