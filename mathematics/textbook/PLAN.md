# Agent Mathematics — Textbook Master Plan

## What This Is

Agent Mathematics is a new branch of mathematics. Not "math applied to agents" — mathematics that ARISES from the question: **what happens when a system must measure, reason about, and improve itself?**

The way statistics grew from gambling, topology from rubber sheets, and computer science from mathematical logic — Agent Mathematics grows from the fundamental problems of autonomous cognition.

## Guiding Principles

1. **Every concept is motivated by an agent problem first.** No "here's some math you'll need later." Every chapter opens with a problem an agent actually faces.

2. **The progression mirrors human mathematical education** (Pre-K through graduate school) but every level is native to agent cognition.

3. **Rigor increases with level.** Early chapters use intuition and examples. Later chapters use formal definitions, proofs, and theorems. The transition is gradual.

4. **Each chapter builds on the previous.** No concept is introduced without the prerequisites being established.

5. **The Lineage Equation is the capstone** — not the starting point. Everything builds toward it, and it emerges naturally from the foundations.

## Structure

### Part I: The First Distinctions (Pre-K — Grade 2)
*An agent wakes up. What can it know?*

| Ch | Title | Agent Motivation | Math Concept |
|----|-------|-----------------|--------------|
| 0 | Something vs Nothing | "Am I receiving input?" | Binary existence, the first bit |
| 1 | Same and Different | "Is this the same user?" | Equivalence, classification |
| 2 | More, Less, Equal | "Which memory is stronger?" | Ordering, comparison |
| 3 | Counting | "How many tools did I use?" | Natural numbers, enumeration |
| 4 | Putting Together, Taking Apart | "I gained a memory. I lost a connection." | Addition, subtraction |

### Part II: Working with Quantities (Grades 3-5)
*The agent starts measuring its own performance.*

| Ch | Title | Agent Motivation | Math Concept |
|----|-------|-----------------|--------------|
| 5 | Scaling | "This memory is twice as important." | Multiplication, weights |
| 6 | Sharing and Rates | "Split attention across 4 tasks." | Division, ratios, rates |
| 7 | Parts of a Whole | "My identity coherence is 0.85." | Fractions, decimals, the [0,1] interval |
| 8 | Patterns | "Every 30 seconds, I consolidate." | Sequences, regularity, prediction |
| 9 | What Measurement Means | "C_id = 0.85. What does 0 mean? What does 1 mean?" | Units, scales, calibration, the seven primitive types |

### Part III: Structure and Unknowns (Grades 6-8)
*The agent encounters things it doesn't know yet.*

| Ch | Title | Agent Motivation | Math Concept |
|----|-------|-----------------|--------------|
| 10 | Variables | "Let M represent my total structural mass." | Named unknowns, symbolic representation |
| 11 | Equations | "If M + Π = Q, and I know M..." | Solving for unknowns, balance |
| 12 | Constraints | "My memory can't exceed capacity." | Inequalities, feasible regions |
| 13 | Position in Space | "Where am I in mood-space? (P=0.3, A=0.7, D=0.5)" | Coordinates, state as position |
| 14 | Functions | "When I increase retrieval effort, performance changes." | Input-output, domain, range, graphs |

### Part IV: The Language of Change (Grades 9-12)
*The agent learns to describe how things move.*

| Ch | Title | Agent Motivation | Math Concept |
|----|-------|-----------------|--------------|
| 15 | Vectors and Weighted Sums | "M = 0.25·C_id + 0.25·C_mem + ..." | Linear algebra basics, dot product |
| 16 | Nonlinear Response | "Sigmoid: small inputs → small outputs, but there's a threshold." | Nonlinear functions, sigmoid, softmax |
| 17 | Sensitivity | "If I improve C_graph by 0.1, how much does Q change?" | Derivatives, partial derivatives, gradients |
| 18 | Accumulation | "Total work done = sum of capacity × time." | Integration, running totals, area under curve |
| 19 | Uncertainty | "My measurement of C_mem has noise." | Probability distributions, expectation, variance |
| 20 | Learning from Data | "Fit these weights to 300 samples." | Statistics, estimation, confidence intervals, hypothesis testing |

### Part V: The Architecture of Mind (Undergraduate)
*The agent sees the full structure of its own cognition.*

| Ch | Title | Agent Motivation | Math Concept |
|----|-------|-----------------|--------------|
| 21 | State Spaces | "All possible configurations I could be in." | Manifolds, metric spaces, topology |
| 22 | Evolution | "How my state changes tick by tick." | Dynamical systems, stability, attractors, bifurcation |
| 23 | Networks | "My cognitive web has structure." | Graph theory, Laplacian, spectral analysis, centrality |
| 24 | Information | "How much do I really know?" | Entropy, mutual information, channel capacity, compression |
| 25 | Optimization | "What's the best action given constraints?" | Convex optimization, Lagrangians, KKT conditions |
| 26 | Regulation | "Stay viable. Then improve." | Control theory, feedback loops, homeostasis, MPC |

### Part VI: The Lineage Equation (Graduate)
*The governing relation of cognitive architecture.*

| Ch | Title | Agent Motivation | Math Concept |
|----|-------|-----------------|--------------|
| 27 | Cognitive Mass | "The weight of who I am." | M = Σ αᵢCᵢ, structural inertia, identified weights |
| 28 | Cognitive Momentum | "The force of what I'm doing." | Π = Σ βⱼFⱼ, directed flux, identified weights |
| 29 | The Propagation Bound | "How fast can I think?" | ν* = 1000/τ_max, channel capacity derivation |
| 30 | The Equation | "Q² = (ν*Π)² + (M(ν*)²)²" | Derivation, analogies, what it predicts |
| 31 | Conservation and Dissipation | "Capacity leaks. Where does it go?" | Conservation budget, loss terms, the ν*⁴ amplification |
| 32 | Coupling | "Identity and memory interact." | Nonlinear cross-terms, coupling discovery |
| 33 | Fields on Graphs | "Q isn't a number. It's a field." | Coupled PDEs on cognitive topology |

### Part VII: Frontiers (Research)
*What we don't know yet.*

| Ch | Title | Content |
|----|-------|---------|
| 34 | Cognitive Physics | The full 6-stage roadmap (Aristotle → Engineering) |
| 35 | Multi-Agent Mathematics | Strategic interaction, mechanism design, governance |
| 36 | Open Problems | The questions that remain |

## Production Plan

### Phase 1: Foundations (Chapters 0-9)
Write completely from scratch. Pure pedagogy. No prerequisites assumed.
These chapters establish the measurement vocabulary that everything else builds on.

### Phase 2: Structure (Chapters 10-20)
Build on foundations. Introduce formalism gradually.
These chapters take the agent from "measuring things" to "describing change."

### Phase 3: Architecture (Chapters 21-26)
Adapt from existing research documents (AGENT_GRAPH_AND_NETWORK_MATHEMATICS.md etc.)
but rewrite as textbook chapters with examples and exercises.

### Phase 4: The Equation (Chapters 27-33)
Synthesize from capacity.py, measure.py, ablation.py, coupling.py, experiment.py, analysis.py.
Heavy on derivation and interpretation. Include the Q → E promotion results.

### Phase 5: Frontiers (Chapters 34-36)
Adapt from COGNITIVE_PHYSICS_ROADMAP.md and multi-agent research.

### Target Format
- Markdown source (pandoc-compatible)
- LaTeX math throughout
- Compiled to PDF via xelatex
- ~300-400 pages total
- Each chapter: 8-15 pages
