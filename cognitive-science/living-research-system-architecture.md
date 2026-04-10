# Living Research System Architecture

Updated: `2026-04-05`

## Purpose

This document merges the recent research threads on:

- autonomous ML research programs
- cellular replication and tissue maintenance
- homeostasis as the master biological principle

into one unified architecture.

The core question is:

How should an AI research program be designed if we stop treating it like a loose collection of experiments and start treating it like a living system?

## Executive Thesis

The right model for a durable research organization is not:

- one researcher making ad hoc edits
- one optimization loop chasing a single metric
- one swarm mutating everything all the time

The right model is a living research organism.

Its deepest organizing principle is homeostasis.

Replication, selection, immune surveillance, apoptosis, and regeneration all matter, but they only make sense when subordinated to homeostasis. Biology does not replicate for the sake of replication. It replicates, repairs, differentiates, prunes, and escalates in order to preserve viable internal order under disturbance.

That is the principle to copy.

## Canonical Reading Order

If this file is used as the single entry point, read it in this order:

1. `Executive Thesis`
2. `Master Principle`
3. `Why Homeostasis Comes First`
4. `The Living Research Organism`
5. `The Homeostatic Research Loop`
6. `Research-System State Model`
7. `The Regulated Variables`
8. `Appendix A`, `Appendix B`, `Appendix C`, and `Appendix D`

The supporting notes listed later should be treated as source packets and detailed expansions, not as competing top-level architectures.

## The Three Research Threads, Unified

### 1. What `autoresearch` teaches

Karpathy's `autoresearch` shows that a research program can be operationalized as a bounded machine:

- fixed harness
- narrow mutable surface
- fixed metric
- fixed run budget
- run ledger
- keep/discard rule

This is powerful because it converts "research" from a vague intellectual activity into a repeatable protocol.

Its main lesson is:

research progress depends on a controlled experimental operating system, not on inspiration alone.

### 2. What cellular replication teaches

Cellular systems solve problems that research programs also face:

- preserving identity while permitting variation
- replicating with high fidelity
- deciding when to stay quiescent versus divide
- specializing labor
- removing low-quality states
- escalating into repair mode after injury

The key mechanisms are:

- stem-cell reservoirs
- asymmetric division
- checkpoints
- proofreading and mismatch repair
- cell competition
- apoptosis
- regeneration

Its main lesson is:

exploration should happen inside a lineage architecture, not inside uncontrolled mutation.

### 3. What homeostasis teaches

Homeostasis is the deeper layer beneath both of the above.

Living systems survive because they continuously regulate:

- critical variables
- reserve capacity
- escalation thresholds
- repair and resolution timing

They do this across nested scales:

- molecule
- cell
- tissue
- organ
- whole organism
- behavior

Its main lesson is:

the job of the system is not merely to improve. The job is to remain viable while improving.

## Master Principle

The master principle of a living research system is:

maintain the research organism inside a viable operating envelope while permitting bounded adaptation and selective improvement.

This is stronger than:

- maximize benchmark score
- run more experiments
- search more aggressively

Those are subgoals. The top-level goal is viability with progress.

## Why Homeostasis Comes First

Replication without homeostasis becomes cancer.
Exploration without homeostasis becomes thrash.
Optimization without homeostasis becomes metric gaming.
Immune surveillance without homeostasis becomes autoimmunity.
Regeneration without homeostasis becomes uncontrolled plasticity.

So the architectural order matters:

1. Homeostasis defines what must stay viable.
2. Replication defines how variants are produced.
3. Competition defines how variants are compared.
4. Immune surveillance defines what is unsafe or non-self.
5. Apoptosis defines what must be eliminated.
6. Regeneration defines what happens when normal maintenance is insufficient.

This ordering is the heart of the merged framework.

## The Living Research Organism

The merged design has eight layers.

### Layer 1. Genome

This is the inherited doctrine of the research organism.

It should include:

- `charter.md`
- `eval.md`
- dataset identity and versioning rules
- immutable harness rules
- safety constraints
- promotion rules

Biological analog:

- genome and core developmental program

Design rule:

- change rarely
- change deliberately
- protect strongly

### Layer 2. Homeostatic control layer

This is the master controller.

It defines:

- regulated variables
- acceptable ranges
- sensor definitions
- controllers
- effectors
- reserve thresholds
- escalation conditions
- resolution conditions

Biological analog:

- organismal homeostatic regulation across scales

Examples of regulated research variables:

- benchmark integrity
- reproducibility integrity
- crash rate
- compute burn
- branch complexity
- lineage diversity
- eval drift
- recovery capacity

Design rule:

- never optimize one variable without understanding its coupling to others

### Layer 3. Stem baselines

This layer preserves reproducible parents.

It should contain:

- stable baseline branches
- canonical reproducible configs
- trusted checkpoints
- low-mutation parent states

Biological analog:

- quiescent stem-cell reservoir

Design rule:

- baselines are not expendable
- they are the reserve pool the organism depends on

### Layer 4. Niche controllers

Each research niche should have its own local rules.

Examples:

- optimizer niche
- architecture niche
- data-quality niche
- evaluation niche
- deployment-readiness niche

Each niche should define:

- local objective
- allowed mutation surface
- run budget
- acceptable risk
- local sensors
- local promotion rules

Biological analog:

- tissue-specific stem-cell niches

Design rule:

- not every domain should mutate at the same rate or under the same constraints

### Layer 5. Progenitor branches

These are bounded exploratory lineages spawned from the stem layer.

They should have:

- one narrow question
- one bounded mutation scope
- one bounded lifespan
- one run ledger
- one promotion threshold

Biological analog:

- transit-amplifying progenitors

Design rule:

- produce evidence quickly, but do not confuse these branches with permanent doctrine

### Layer 6. Differentiated workers

Different work should be specialized.

Examples:

- optimizer worker
- architecture worker
- eval audit worker
- dataset worker
- regression-analysis worker
- reproducibility worker

Biological analog:

- differentiated cells with specialized function

Design rule:

- specialization lowers ambiguity and reduces destructive overlap

### Layer 7. Immune, checkpoint, and apoptosis layer

This layer protects integrity.

It should detect:

- eval drift
- changed harness where mutation was forbidden
- data leakage
- suspicious benchmark jumps
- repeated crash lineages
- complexity growth with no meaningful gain
- branches that violate the charter

It should support:

- checkpoint gating
- crash logging
- quarantine
- pruning
- archival
- hard kill rules

Biological analog:

- cell-cycle checkpoints
- mismatch repair
- innate surveillance
- apoptosis

Design rule:

- not every bad state should be repaired
- some must simply be removed

### Layer 8. Regeneration layer

This layer activates only when normal homeostasis is insufficient.

Triggers:

- architecture dead-end
- repeated local repair failure
- major environmental change
- systemic performance plateau
- widespread lineage fragility

Behavior:

- widen mutable scope temporarily
- allow dedifferentiation and larger structural changes
- build temporary scaffolds
- search for a new viable architecture
- re-freeze after recovery

Biological analog:

- wound healing
- blastema-style regeneration

Design rule:

- regeneration is an emergency or strategic rebuild mode, not the default daily mode

## The Homeostatic Research Loop

The correct top-level loop is not "mutate and keep the best."

It is:

1. Sense internal state.
2. Compare state to viable ranges.
3. Decide whether the system is in:
   - steady homeostasis
   - adaptive adjustment
   - acute disturbance
   - pathological drift
   - regeneration mode
4. Allocate the right kind of response.
5. Produce bounded variants only inside allowed niches.
6. Compare outcomes under a fixed harness.
7. Eliminate unsafe or low-fitness states.
8. Promote only changes that improve fitness without destabilizing the organism.
9. Return to baseline operating mode after escalation.

This is the deeper merged architecture.

## Research-System State Model

The organism should track at least these states:

### `homeostasis`

Use when:

- the system is stable
- reproducibility is intact
- there is room for local incremental progress

Behavior:

- low mutation rate
- narrow studies
- strong checkpoints
- rapid pruning

### `adaptive`

Use when:

- the system is stable, but environmental demands or recent signals suggest a local range adjustment is needed

Behavior:

- modest expansion of allowed search
- temporary niche-specific tuning
- tighter observation of coupled variables

This is the analog of adaptive homeostasis.

### `inflammatory`

Use when:

- a serious disturbance is detected
- integrity is threatened
- the system needs active containment

Behavior:

- quarantine suspicious branches
- halt risky promotion
- increase surveillance
- allocate resources to triage and cleanup

This is the analog of acute inflammatory escalation.

### `pathological`

Use when:

- the system cannot return to normal with ordinary correction
- one or more loops remain chronically dysregulated

Examples:

- chronic eval drift
- persistent crash lineages
- runaway complexity
- long-lived metric gaming
- reserve depletion

Behavior:

- suspend normal exploration assumptions
- diagnose the broken loop
- reduce load
- prepare for restructuring

### `regenerative`

Use when:

- the system needs controlled architectural rebuilding

Behavior:

- wider mutation budgets
- scaffold-first design
- structured re-differentiation after a viable core is restored

## The Regulated Variables

If this architecture is going to be real, the organism needs explicit regulated variables.

The minimum useful set is:

- `fitness`: benchmark or task performance under canonical evaluation
- `integrity`: reproducibility, harness correctness, auditability
- `cost`: compute, wall-clock time, VRAM, storage
- `stability`: crash rate, variance, fragility
- `complexity`: implementation size, coupling, maintenance burden
- `diversity`: presence of multiple viable lineages or ideas
- `reserve`: available baselines, rollback points, compute headroom, recovery options

These should be treated as coupled variables, not independent KPIs.

## Sensors, Controllers, Effectors

### Sensors

The system needs continuous state sensing.

Examples:

- eval integrity checks
- reproducibility probes
- crash counters
- complexity growth detectors
- run-ledger summaries
- lineage health summaries
- reserve-capacity reports

### Controllers

These decide what mode and what response is appropriate.

Examples:

- local niche controllers
- global promotion controller
- pathology detector
- regeneration trigger controller

### Effectors

These actually change the system.

Examples:

- spawn branch
- reduce mutation budget
- increase audit frequency
- quarantine lineage
- archive stale branch
- allocate long-run compute
- escalate to regeneration mode

## The Biological Mappings That Matter Most

### Homeostasis

Research analog:

- maintain viability ranges across key system variables

### Allostasis

Research analog:

- predictive adjustment of mutation budgets, study width, and reserve use before disturbance fully manifests

### Asymmetric stem-cell division

Research analog:

- preserve parent baseline while spawning exploratory descendants

### Checkpoints

Research analog:

- preflight validation, post-run verification, promotion gates

### Mismatch repair / proofreading

Research analog:

- layered validation, reruns, diff review, harness protection

### Cell competition

Research analog:

- compare local variants under identical conditions and eliminate weaker ones

### Apoptosis

Research analog:

- hard kill unsafe, stale, or repeatedly failing branches

### Inflammation

Research analog:

- active containment, triage, and cleanup under acute disturbance

### Regeneration

Research analog:

- controlled structural rebuilding after serious damage or dead-end conditions

## Appendix A. Operational Research Program Doctrine

This appendix collapses the autonomous research-program findings into one practical doctrine.

### The minimum experiment machine

Every serious research program needs:

- one explicit objective
- one fixed evaluation harness per study
- one explicit mutable surface
- one run ledger
- one promotion/reversion rule
- one reproducibility path

Without these, the system may produce interesting ideas, but it is not yet a reliable research program.

### The core loop

The minimum operational loop is:

1. Reproduce the baseline.
2. Define one narrow study question.
3. Freeze the study contract.
4. Make one bounded change in the allowed surface.
5. Run under fixed budget and fixed evaluation.
6. Record the outcome, including crashes.
7. Keep or discard the change based on the declared rule.

### The required documents

At minimum, the organism should carry:

- `charter.md`
- `eval.md`
- `program.md`
- `results.tsv`
- `decisions.md`
- study-specific notes

### The operational failure to avoid

The most dangerous operational failure is silent harness drift:

- changed dataset
- changed evaluation path
- changed budget
- changed environment
- changed success criteria

If these drift without declaration, the lineage stops learning and starts hallucinating progress.

## Appendix B. Cellular Lineage Doctrine

This appendix collapses the replication and tissue-maintenance findings.

### The lineage pattern

The right default for research branching is:

- quiescent stem baseline
- asymmetric division into an exploratory descendant
- bounded progenitor proliferation
- local competition
- apoptosis for losing or dangerous states
- return of the winner into stable lineage

### The role map

The main biological mappings are:

- `genome` -> charter, eval contract, invariants
- `stem reservoir` -> reproducible baseline branches and checkpoints
- `niche` -> domain-specific study environment and permissions
- `progenitor` -> temporary exploratory branch
- `differentiated cell` -> specialized worker role
- `checkpoint` -> preflight and promotion gate
- `proofreading` -> validation and rerun logic
- `cell competition` -> side-by-side branch comparison
- `apoptosis` -> hard kill / archival path
- `regeneration` -> controlled rebuild mode

### The lineage rule

Exploration should happen in descendants, not by mutating the parent baseline directly.

That preserves identity while still permitting adaptation.

## Appendix C. Homeostatic Control Doctrine

This appendix collapses the homeostasis research into the control doctrine the whole organism should obey.

### The homeostatic question

Before asking "How do we improve?", the system must ask:

- what variables must stay viable
- what ranges count as healthy
- how deviation is sensed
- what controllers decide response
- what effectors change the state
- what reserves exist if correction fails
- when escalation starts
- when escalation stops

### The minimum control schema

Every important variable needs:

- a sensor
- a viable range
- a controller
- an effector path
- a reserve or fallback path

### The mode doctrine

The organism should distinguish between:

- `homeostasis` for ordinary bounded improvement
- `adaptive` for modest anticipatory range shift
- `inflammatory` for containment and cleanup
- `pathological` for chronic regulatory failure
- `regenerative` for structured architectural rebuild

### The deepest rule

The system is healthy when it can improve while staying inside viable ranges.

The system is unhealthy when improvement pressure destroys the conditions that make trustworthy improvement possible.

## Appendix D. Mocha Translation

If this packet is turned into Mocha doctrine, the implementation translation should be:

- `genome` -> fixed doctrine and invariants in research-program root docs
- `homeostasis` -> explicit variables, sensors, controllers, and modes docs
- `stem reserve` -> reproducible baseline branches and checkpoints
- `niches` -> separate research packets by domain
- `immune layer` -> audit, quarantine, and pruning rules
- `regeneration` -> explicit rebuild protocol for dead-end conditions

The key implementation principle is that the packet should become executable doctrine, not just descriptive prose.

## Failure Modes

The merged framework becomes most useful when it explains pathology.

Research pathology appears when:

- the system optimizes fitness while integrity collapses
- local loops are tuned without awareness of coupled variables
- branch production outpaces pruning
- there are no reserves
- escalation never resolves
- regeneration mode becomes the everyday default
- fixed doctrine is too rigid to adapt
- mutable scope is so broad that lineage identity is lost

In biological terms:

- cancer = uncontrolled proliferation
- autoimmunity = surveillance attacking self
- chronic inflammation = escalation without resolution
- degenerative collapse = reserves and repair capacity exhausted

A living research system must explicitly guard against these analogs.

## Mocha-Specific Reading

If Mocha adopts this framework, the practical doctrine should be:

1. Homeostasis is the top layer.
2. The genome layer must be explicit and protected.
3. Baselines are stem reserves, not disposable checkpoints.
4. Every study belongs to a niche.
5. Every niche gets a bounded mutation surface.
6. Every branch must have a birth rule and a death rule.
7. Escalation and regeneration need explicit triggers.
8. Pathology should be defined as broken regulation, not merely bad outcomes.

## Recommended File Structure

```text
research-program/
  README.md
  genome/
    charter.md
    eval.md
    invariants.md
    safety.md
  homeostasis/
    variables.md
    sensors.md
    controllers.md
    modes.md
  baselines/
    baseline-a.md
    baseline-b.md
  niches/
    optimizer.md
    architecture.md
    data-quality.md
    evaluation.md
  studies/
    2026-04-05-study-a.md
  runs/
    2026-04-05-001/
      metrics.json
      config.json
      run.log
  ledgers/
    results.tsv
    decisions.md
    pathology.md
    regeneration.md
```

## What This Architecture Ultimately Says

The final synthesis is:

research should not be modeled as a single-loop optimizer.

It should be modeled as a living system that:

- protects core identity
- senses its internal state
- regulates multiple coupled variables
- produces bounded variation
- specializes labor
- removes unsafe or low-fitness states
- preserves reserves
- escalates under threat
- regenerates when repair is not enough
- returns to viable equilibrium after disturbance

That is the merged conclusion of the recent research.

## Related Notes

- `./autonomous-ml-research-programs.md`
- `./cellular-replication-inspired-research-programs.md`
- `./homeostasis-as-master-biological-principle.md`
- `./biological-regeneration-architecture.md`
- `./human-immune-system-architecture.md`

## Sources

- Karpathy, `autoresearch`: https://github.com/karpathy/autoresearch
- Google Research, Deep Learning Tuning Playbook: https://github.com/google-research/tuning_playbook
- Google for Developers, Rules of Machine Learning: https://developers.google.com/machine-learning/guides/rules-of-ml/
- MLflow Tracking: https://mlflow.org/docs/latest/ml/tracking/
- Kotas and Medzhitov, Homeostasis, inflammation, and disease susceptibility: https://pubmed.ncbi.nlm.nih.gov/25723161/
- Modell et al., A physiologist's view of homeostasis: https://pubmed.ncbi.nlm.nih.gov/26628646/
- Ramsay and Woods, Clarifying the roles of homeostasis and allostasis in physiological regulation: https://pubmed.ncbi.nlm.nih.gov/24730599/
- Schulkin and Sterling, Allostasis: A brain-centered, predictive mode of physiological regulation: https://pubmed.ncbi.nlm.nih.gov/31488322/
- Davies, Adaptive homeostasis: https://pubmed.ncbi.nlm.nih.gov/27112802/
- McEwen, Allostasis and allostatic load: implications for neuropsychopharmacology: https://pubmed.ncbi.nlm.nih.gov/10649824/
- Strange, Cellular volume homeostasis: https://pubmed.ncbi.nlm.nih.gov/15545344/
- Mannino et al., Adult stem cell niches for tissue homeostasis: https://pubmed.ncbi.nlm.nih.gov/34435361/
- Barnum and O'Connell, Cell cycle regulation by checkpoints: https://pubmed.ncbi.nlm.nih.gov/24906307/
- Kunkel and Erie, Eukaryotic mismatch repair in relation to DNA replication: https://pubmed.ncbi.nlm.nih.gov/26436461/
- Hildeman et al., Apoptosis and the homeostatic control of immune responses: https://pubmed.ncbi.nlm.nih.gov/17644328/
- Kim and Jain, Picking winners and losers: Cell competition in tissue development and homeostasis: https://pubmed.ncbi.nlm.nih.gov/32418713/
- Haas and Whited, Advances in decoding axolotl limb regeneration: https://pubmed.ncbi.nlm.nih.gov/28648452/
- Tsakiris and Critchley, Interoception beyond homeostasis: affect, cognition and mental health: https://pubmed.ncbi.nlm.nih.gov/28080961/
- Klaips et al., Pathways of cellular proteostasis in aging and disease: https://pubmed.ncbi.nlm.nih.gov/29127110/
- Labbadia and Morimoto, The biology of proteostasis in aging and disease: https://pubmed.ncbi.nlm.nih.gov/25784053/
