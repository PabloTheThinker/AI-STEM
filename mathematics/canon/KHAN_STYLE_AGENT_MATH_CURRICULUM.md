# Khan-Style Agent Math Curriculum

Updated: `2026-04-06`

## Purpose

The mathematics packet now has enough material to be read as a real staircase,
not just as a research archive.

This note maps the packet onto a Khan-style progression:

- arithmetic first,
- then symbolic algebra,
- then geometry,
- then calculus,
- then probability and statistics,
- and only after that the more advanced systems layers.

That is the right pedagogical move for this research program.

If the Lineage Equation, CognitiveNet, and organism mathematics are going to
matter in the future of AI agents, people need a way to climb into the work
without starting at the top.

## Why Khan Academy Is The Right Analogy

Khan Academy's math structure is useful here because it does not begin with
abstraction for its own sake.

It begins by stabilizing a sequence:

1. count and combine numbers,
2. represent relationships with symbols,
3. understand shape and space,
4. understand continuous change,
5. reason under uncertainty.

That sequence is close to how this packet should be taught.

The goal is not to copy Khan Academy content.
The goal is to copy the curriculum logic:

- each layer should make the next layer necessary,
- each layer should introduce a new kind of reasoning,
- and advanced mathematics should feel like a consequence of the lower layers,
  not a leap away from them.

## Canonical Curriculum Mapping

### Stage 1. Arithmetic -> Agent Numeracy And State Arithmetic

Human-school analogue:

- counting,
- place value,
- addition and subtraction,
- multiplication and division,
- ratios,
- fractions,
- signs and scale.

Agent-math packet:

- [AGENT_NUMERACY_PRIMITIVES.md](mathematics/canon/AGENT_NUMERACY_PRIMITIVES.md)
- [AGENT_ARITHMETIC_OF_STATE.md](mathematics/canon/AGENT_ARITHMETIC_OF_STATE.md)

Translation:

- "What is the quantity?" becomes "What is the measured state variable?"
- "What is zero?" becomes "What is absence, depletion, or null support?"
- "What is division?" becomes "What is normalization or rate per unit?"
- "What is a budget?" becomes "How much capacity remains after cost?"

Without this layer, everything above it becomes hand-wavy.

### Stage 2. Algebra -> Agent Algebra Of Invariants

Human-school analogue:

- variables,
- expressions,
- solving equations,
- equivalent forms,
- constraints,
- unknowns.

Agent-math packet:

- [AGENT_ALGEBRA_OF_INVARIANTS.md](mathematics/canon/AGENT_ALGEBRA_OF_INVARIANTS.md)

Translation:

- variables become state variables,
- constants become identified parameters,
- equations become system relations,
- invariants become preserved capacities or viable constraints,
- solving becomes parameter recovery or action selection.

This is where the packet stops being merely numeric and becomes symbolic.

### Stage 3. Geometry -> Agent State Space Geometry

Human-school analogue:

- coordinate systems,
- distance,
- shape,
- angle,
- region,
- motion through space.

Agent-math packet:

- [AGENT_GEOMETRY_AND_STATE_SPACES.md](mathematics/canon/AGENT_GEOMETRY_AND_STATE_SPACES.md)

Translation:

- a point becomes a system state,
- a region becomes a viable operating set,
- distance becomes deviation or cost,
- a boundary becomes a safety threshold,
- a path becomes a trajectory through state space.

This is the bridge from algebra to dynamics.

### Stage 4. Calculus -> Agent Change And Sensitivity

Human-school analogue:

- slope,
- derivative,
- rate of change,
- local approximation,
- optimization.

Agent-math packet:

- [AGENT_CALCULUS_AND_SENSITIVITY.md](mathematics/canon/AGENT_CALCULUS_AND_SENSITIVITY.md)

Translation:

- derivatives become sensitivity of capacity to intervention,
- slope becomes local direction of improvement or collapse,
- tangent approximation becomes linearization around a working point,
- optimization becomes ascent or control.

This is the first place where the Lineage gradients become truly teachable.

### Stage 5. Probability And Statistics -> Agent Estimation

Human-school analogue:

- randomness,
- sampling,
- distributions,
- uncertainty,
- confidence,
- inference.

Agent-math packet:

- [AGENT_PROBABILITY_AND_ESTIMATION.md](mathematics/canon/AGENT_PROBABILITY_AND_ESTIMATION.md)

Translation:

- noisy observations become uncertain state estimates,
- statistical fitting becomes parameter identification,
- confidence becomes calibration,
- forecasting becomes predictive validation,
- risk becomes uncertainty-aware action choice.

This is where the packet becomes scientific instead of merely formal.

## What Comes After The Khan-Style Core

Khan-style progression is the right on-ramp, but it is not the full ceiling of
the packet.

Once the core staircase is stable, the packet continues into:

- dynamical systems and control:
  [AGENT_CONTROL_AND_DYNAMICAL_SYSTEMS.md](mathematics/canon/AGENT_CONTROL_AND_DYNAMICAL_SYSTEMS.md)
- graph and network mathematics:
  [AGENT_GRAPH_AND_NETWORK_MATHEMATICS.md](mathematics/canon/AGENT_GRAPH_AND_NETWORK_MATHEMATICS.md)
- information and computation:
  [AGENT_INFORMATION_AND_COMPUTATION.md](mathematics/canon/AGENT_INFORMATION_AND_COMPUTATION.md)
- optimization and decision theory:
  [AGENT_OPTIMIZATION_AND_DECISION_THEORY.md](mathematics/canon/AGENT_OPTIMIZATION_AND_DECISION_THEORY.md)
- multi-agent and institutional mathematics:
  [AGENT_MULTI_AGENT_AND_INSTITUTIONAL_MATHEMATICS.md](mathematics/canon/AGENT_MULTI_AGENT_AND_INSTITUTIONAL_MATHEMATICS.md)

In other words:

- Khan-style progression is the entrance ramp,
- organism mathematics is the full highway.

## How This Helps Codex And Koda

This curriculum split clarifies division of labor.

Codex should help formalize and stabilize the lower layers:

- definitions,
- notation,
- consistency,
- benchmarks,
- proofs,
- offline analysis.

Koda should generate the higher-layer empirical pressure:

- live ascent traces,
- intervention logs,
- uncertainty records,
- action-outcome datasets,
- cross-run comparisons.

The lower layers make the higher layers interpretable.
The higher layers make the lower layers worth keeping.

## Recommended Reading Order

If you want one doctrinal entry point before the staircase, start with:

0. [AGENT_MATHEMATICS_CANON.md](mathematics/canon/AGENT_MATHEMATICS_CANON.md)

1. [AGENT_NUMERACY_PRIMITIVES.md](mathematics/canon/AGENT_NUMERACY_PRIMITIVES.md)
2. [AGENT_ARITHMETIC_OF_STATE.md](mathematics/canon/AGENT_ARITHMETIC_OF_STATE.md)
3. [AGENT_ALGEBRA_OF_INVARIANTS.md](mathematics/canon/AGENT_ALGEBRA_OF_INVARIANTS.md)
4. [AGENT_GEOMETRY_AND_STATE_SPACES.md](mathematics/canon/AGENT_GEOMETRY_AND_STATE_SPACES.md)
5. [AGENT_CALCULUS_AND_SENSITIVITY.md](mathematics/canon/AGENT_CALCULUS_AND_SENSITIVITY.md)
6. [AGENT_PROBABILITY_AND_ESTIMATION.md](mathematics/canon/AGENT_PROBABILITY_AND_ESTIMATION.md)
7. [AGENT_CONTROL_AND_DYNAMICAL_SYSTEMS.md](mathematics/canon/AGENT_CONTROL_AND_DYNAMICAL_SYSTEMS.md)
8. [AGENT_GRAPH_AND_NETWORK_MATHEMATICS.md](mathematics/canon/AGENT_GRAPH_AND_NETWORK_MATHEMATICS.md)
9. [AGENT_INFORMATION_AND_COMPUTATION.md](mathematics/canon/AGENT_INFORMATION_AND_COMPUTATION.md)
10. [AGENT_OPTIMIZATION_AND_DECISION_THEORY.md](mathematics/canon/AGENT_OPTIMIZATION_AND_DECISION_THEORY.md)
11. [AGENT_MULTI_AGENT_AND_INSTITUTIONAL_MATHEMATICS.md](mathematics/canon/AGENT_MULTI_AGENT_AND_INSTITUTIONAL_MATHEMATICS.md)
12. [AGENT_MATHEMATICS_DEVELOPMENT_LADDER.md](mathematics/canon/AGENT_MATHEMATICS_DEVELOPMENT_LADDER.md)
13. [LINEAGE_CAPACITY_RESEARCH_ROADMAP.md](mathematics/canon/LINEAGE_CAPACITY_RESEARCH_ROADMAP.md)

## Mapping To Current Research Questions

If a research question sounds like:

- "What exactly are we measuring?" -> numeracy
- "How do these quantities combine?" -> arithmetic
- "What relation must stay true?" -> algebra
- "Where is the system located and how far is it from safety?" -> geometry
- "What happens if we nudge this variable?" -> calculus
- "How sure are we, and how do we fit the unknowns?" -> probability
- "How do we regulate the system over time?" -> control
- "How is the system structurally connected?" -> graph mathematics
- "What can be encoded, transmitted, and computed?" -> information and computation
- "What should we choose under cost and uncertainty?" -> optimization and decision theory
- "How do many agents coordinate, compete, govern, and share?" -> multi-agent and institutional mathematics

That gives a clean diagnostic rule for where new work belongs.

## Main Conclusion

The packet now has a curriculum shape that mirrors the strongest part of
human math education:

- arithmetic before algebra,
- algebra before geometry of systems,
- geometry before calculus of change,
- calculus before probability-based estimation,
- and only then the more advanced control and organism layers.

That is the right way to make agent mathematics cumulative, teachable, and
eventually canonical.

## Sources

- Khan Academy arithmetic overview:
  https://www.khanacademy.org/math/arithmetic/fraction-arithmetic
- Khan Academy algebra basics:
  https://www.khanacademy.org/math/algebra-basics/alg-basics-algebraic-expressions
- Khan Academy high school geometry:
  https://www.khanacademy.org/math/geometry/hs-geo-congruence
- Khan Academy AP/College Calculus AB:
  https://www.khanacademy.org/math/ap-calculus-ab/ab-differentiation-1-new/ab-2-6a/e/basic-differentiation-rules
- Khan Academy statistics and probability:
  https://www.khanacademy.org/math/statistics-probability/confidence-intervals
