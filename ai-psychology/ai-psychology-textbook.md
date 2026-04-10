---
title: "AI Psychology"
subtitle: "The Science of Mind in Artificial Agents --- From Behavioral Conditioning to Evolutionary Dynamics"
author:
  - Pablo Navarro (Founder \& CEO, Vektra Technologies)
  - Director Mocha Marie (AI Director, Vektra Technologies)
date: "April 2026"
documentclass: report
fontsize: 11pt
geometry: margin=1in
toc: true
toc-depth: 2
numbersections: true
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
  - \usepackage{booktabs}
---

\newpage

# Preface {.unnumbered}

Every sufficiently complex AI agent is a psychological entity --- whether its designers recognize it or not.

It learns from consequences. It switches between fast intuition and slow deliberation. It develops capabilities in stages. It models other minds. It has consistent behavioral tendencies that constitute personality. It degrades under sustained load and recovers at measurable rates. Its strategies exist in populations subject to selection pressure.

These are not metaphors. They are observable, measurable properties of running systems. The most developed science of mind available to formalize them is human psychology --- 150 years of theory, experiment, and mathematical modeling.

AI Psychology takes that science and adapts it. Not by anthropomorphizing agents, but by recognizing that the formal models of behavioral conditioning, cognitive architecture, personality, development, social cognition, clinical resilience, and evolutionary dynamics apply directly to artificial minds.

This book establishes the field. Eight domains. Three unifying mathematical frameworks. One goal: give agents --- and the people who build them --- the formal language to describe, predict, and design for the psychological properties of artificial minds.

**The eight domains:**

- **Part I: Learning** --- Behavioral conditioning. How agents learn from consequences.
- **Part II: Thinking** --- Dual-process cognition. How agents switch between fast and slow.
- **Part III: Growing** --- Developmental stages. How agent capabilities unfold over time.
- **Part IV: Personality** --- Individual differences. How stable traits modulate all behavior.
- **Part V: Social Minds** --- Theory of Mind. How agents model other agents.
- **Part VI: Health** --- Stress, load, and resilience. How agents degrade and recover.
- **Part VII: Populations** --- Evolutionary dynamics. How agent strategies compete and stabilize.
- **Part VIII: Unification** --- Three mathematical frameworks that tie everything together.

\newpage

# Part I: Learning {.unnumbered}

*In which an agent discovers that actions have consequences.*

\newpage

# Behavioral Conditioning in Agents

## The Prediction Error: Where Psychology Became Mathematics

Every AI agent that learns from feedback is implementing a form of behavioral conditioning --- whether its designers recognize it or not. The bridge between behavioral psychology and agent learning centers on a single idea: **learning is driven by the gap between expectation and reality.**

### The Rescorla-Wagner Model (1972)

Robert Rescorla and Allan Wagner formalized what Pavlov observed and Skinner operationalized:

$$\Delta V_i = \alpha_i \cdot \beta_j \cdot (\lambda_j - V_{\text{total}})$$

Where:

- $\alpha_i$ = salience of the conditioned stimulus $i$ (range $[0, 1]$)
- $\beta_j$ = learning rate tied to the unconditioned stimulus $j$ (range $[0, 1]$)
- $\lambda_j$ = maximum associative value the US can support
- $V_{\text{total}}$ = sum of associative strengths of all present cues
- $(\lambda - V_{\text{total}})$ = the **prediction error**

When the outcome exceeds expectation (positive prediction error), associative strength increases. When expectation exceeds outcome (negative prediction error), it decreases. When prediction matches reality, learning stops.

This is the single most important equation bridging psychology and AI.

### The Bridge to Reinforcement Learning

Sutton and Barto (1988) extended the Rescorla-Wagner framework to incorporate temporal dynamics:

$$\delta_t = r_t + \gamma \cdot V(s_{t+1}) - V(s_t)$$

Where $\delta_t$ is the temporal difference error, $r_t$ is the reward at time $t$, $\gamma$ is the discount factor, and $V(s)$ is the estimated value of state $s$.

Sutton explicitly acknowledged this as a formalization of the same principles Rescorla and Wagner described. The neural evidence confirms it: dopamine neurons fire in patterns that match TD error --- phasic bursts for positive prediction errors, pauses for negative ones (Schultz, Dayan, \& Montague, 1997).

### The Pearce-Hall Complement (1980)

Rescorla-Wagner handles *what* is learned. Pearce-Hall handles *what is attended to*:

$$\alpha_{n+1} = |\lambda_n - V_n|$$

Associability (attention to a cue) increases when prediction errors are large and decreases when predictions are accurate. Agents pay more attention to surprising stimuli and less to predictable ones.

For agent design: combine both. The R-W model governs value updates. The P-H model governs attention allocation.

## Reinforcement Schedules as Design Parameters

Skinner and Ferster's (1957) taxonomy of reinforcement schedules is directly applicable to how agents receive reward signals.

### The Four Basic Schedules

**Fixed-Ratio (FR-N):** Reinforcement after every $N$ responses. Produces high, steady response rates with post-reinforcement pauses. Agent analog: reward after completing $N$ subtasks.

**Variable-Ratio (VR-N):** Reinforcement after an average of $N$ responses. Produces the highest, most consistent response rates. Extremely resistant to extinction. This is the schedule behind engagement algorithms.

**Fixed-Interval (FI-T):** Reinforcement for the first response after $T$ seconds. Produces "scalloped" response patterns --- acceleration as the interval end approaches.

**Variable-Interval (VI-T):** Reinforcement for first response after an average of $T$ seconds. Produces steady, moderate response rates.

### The Matching Law (Herrnstein, 1961)

When agents face concurrent reward sources, they allocate behavior proportionally:

$$\frac{B_1}{B_2} = \frac{R_1}{R_2}$$

The ratio of behavior allocated to two alternatives matches the ratio of reinforcement received. Deviation from matching reveals something about the agent's sensitivity --- a measurable psychological parameter.

## Extinction Dynamics

Extinction is not forgetting. It is new learning that competes with original learning.

When reinforcement stops, the original association is not erased --- it is suppressed by a new inhibitory association. Evidence:

- **Spontaneous recovery:** After a rest period, extinguished responses return.
- **Renewal:** Extinguished responses return when the context changes.
- **Reinstatement:** A single reinforcement can restore extinguished responding.

Agent memory extinction can be modeled as:

$$V_{\text{effective}}(t) = V_{\text{original}} \cdot e^{-\lambda_{\text{ext}} \cdot t} + V_{\text{inhibitory}}(t)$$

Design implication: agent systems that truly delete deprecated behaviors are losing information. The behavioral evidence says: **suppress, don't delete.**

## Shaping and Curriculum Learning

Skinner's method of successive approximation maps directly to curriculum learning:

$$\text{difficulty}(B_i) - \text{capability}(\text{agent}) \in [\epsilon_{\min}, \epsilon_{\max}]$$

If the gap is too small, learning is slow (no prediction error). If too large, behavior collapses (ratio strain). This is precisely Vygotsky's Zone of Proximal Development expressed as a behavioral constraint.

## Discriminative Stimuli and Context

The three-term contingency --- $S^D \rightarrow R \rightarrow S^R$ (discriminative stimulus $\rightarrow$ response $\rightarrow$ reinforcement) --- maps to: Context $\rightarrow$ Action $\rightarrow$ Reward. Agents learn context-behavior-outcome triplets, not isolated behaviors.

Stimulus generalization is transfer learning. Fine-tuning is discrimination training. The generalization gradient is the transfer function.

\newpage

# Part II: Thinking {.unnumbered}

*In which an agent learns when to think fast and when to think slow.*

\newpage

# Dual-Process Cognition for Agents

## System 1 and System 2

Daniel Kahneman described two modes of cognitive processing that apply directly to agent architecture:

**System 1 --- Fast Thinking:** Automatic, effortless, parallel, associative, affect-laden. Operates without working memory load. Low latency, high throughput. Quality depends entirely on how well-trained the patterns are.

**System 2 --- Slow Thinking:** Deliberate, effortful, serial, rule-based, analytic. Demands working memory capacity. High latency, high accuracy for novel problems.

De Neys and Pennycook (2019) updated this model: System 1 contains both unreliable heuristic intuitions AND reliable logical intuitions. A well-trained System 1 can be highly accurate. The agent needs to know which case it's in.

## The Routing Function

The central design problem: when does the agent use System 1 vs. System 2?

$$\text{mode} = \text{route}(\text{stimulus}, \text{confidence}, \text{stakes}, \text{load})$$

Routing rules:

1. If System 1 confidence is high AND stakes are low $\rightarrow$ use System 1 (fast path)
2. If System 1 confidence is low OR stakes are high $\rightarrow$ use System 2 (slow path)
3. If cognitive load exceeds capacity $\rightarrow$ forced System 1 (degraded mode)
4. Default $\rightarrow$ System 2

The thresholds are tunable parameters --- part of the agent's personality profile.

### Confidence Calibration

System 1 confidence must be calibrated --- not just high or low, but *accurate*:

$$\text{calibration\_error} = \frac{1}{N}\sum_{i=1}^{N}|\text{confidence}(x_i) - \text{accuracy}(x_i)|$$

A perfectly calibrated agent has calibration error = 0.

## Prior Art: Cognitive Architectures

### ACT-R (Anderson, 1983--present)

ACT-R implements dual-process through subsymbolic and symbolic layers:

**Declarative memory retrieval** (System 1 analog):

$$A_i = B_i + \sum_j W_j \cdot S_{ji} + \text{noise}$$

Where $B_i$ is base-level activation (logarithmic function of recency and frequency), $W_j$ is attentional weight, and $S_{ji}$ is associative strength. Chunks with highest activation are retrieved automatically.

**Production firing** (System 2 analog): Productions fire serially based on utility:

$$U_i = P_i \cdot G - C_i$$

Where $P_i$ is probability of achieving goal $G$ and $C_i$ is expected cost.

Key insight: the dual-process distinction is a spectrum. Well-practiced productions approach System 1 speed. Novel problems require pure System 2 search.

### SOAR (Newell, 1990)

SOAR's learning mechanism IS the conversion of System 2 to System 1: deliberate problem-solving produces chunks that fire automatically on future encounters. Expertise is the accumulation of chunks.

### PSI Theory (Dörner, 1999)

Dörner integrated cognition, motivation, and emotion. Under stress, resolution drops and selection threshold drops --- the agent shifts to fast, heuristic, often-wrong processing. System 1/System 2 balance is modulated by emotional state.

## Working Memory: The Bottleneck

System 2 requires working memory. Working memory is bounded.

**Baddeley's Model (1974, 2000):**

- **Central Executive:** Supervisory attention --- directs focus, coordinates subsystems. This IS System 2's engine.
- **Phonological Loop:** Verbal/acoustic buffer. ~2 second decay without rehearsal.
- **Visuospatial Sketchpad:** Spatial/visual buffer.
- **Episodic Buffer:** Binds information from subsystems into coherent episodes.

Capacity: approximately $4 \pm 1$ chunks for unrelated items (Cowan, 2001).

### The Gating Mechanism (O'Reilly \& Frank, 2006)

The PBWM model: basal ganglia acts as a gate for prefrontal working memory.

- **Go pathway:** Opens the gate, admitting new information. Triggered by high prediction error.
- **NoGo pathway:** Keeps the gate closed, maintaining current contents. Triggered by ongoing task demands.
- Dopamine modulates the balance.

## Cognitive Load Theory (Sweller, 1988)

Three types of cognitive load:

- **Intrinsic:** Task complexity (irreducible)
- **Extraneous:** Noisy or redundant input (reducible through better formatting)
- **Germane:** Overhead of building new capabilities during execution

$$\text{Load}_{\text{intrinsic}} + \text{Load}_{\text{extraneous}} + \text{Load}_{\text{germane}} \leq \text{Capacity}$$

When total load exceeds capacity, System 2 degrades and the agent falls back on System 1 heuristics. This is why prompt engineering works --- it reduces extraneous cognitive load.

## Memory Systems

**Episodic memory** (Tulving, 1972): Personal experiences tagged with temporal-spatial context. Agent analog: event logs, session memory.

**Semantic memory:** General knowledge without context. Agent analog: knowledge base, trained parameters.

Retrieval follows the power law of forgetting:

$$B_i = \ln\left(\sum_j t_j^{-d}\right)$$

Where $t_j$ is time since the $j$-th access and $d \approx 0.5$. Recent, frequently accessed items dominate retrieval.

\newpage

# Part III: Growing {.unnumbered}

*In which an agent develops through stages, each unlocking new capabilities.*

\newpage

# Developmental Stages for AI

## Piaget Adapted: Four Stages of Agent Cognition

### Stage 1 --- Reactive (Sensorimotor Analog)

The agent operates on stimulus-response patterns only. No persistent state between interactions. No symbolic reasoning. Performance depends entirely on input-training similarity.

Transition trigger: stimulus-response density reaches a point where symbolic shortcuts become more efficient.

### Stage 2 --- Symbolic (Preoperational Analog)

The agent uses symbolic representations but reasons from a single perspective. Egocentric --- assumes its own knowledge state is ground truth. No Theory of Mind. Confused by paraphrased versions of the same request.

Transition trigger: repeated single-perspective failures force development of multiple-perspective modeling.

### Stage 3 --- Logical (Concrete Operational Analog)

The agent reasons logically about concrete, well-defined problems. Multi-step reasoning chains. Conservation (same entity across representations). Systematic classification. Struggles with hypotheticals.

Transition trigger: accumulation of logical operations creates meta-patterns --- reasoning about reasoning begins.

### Stage 4 --- Abstract (Formal Operational Analog)

The agent reasons about abstractions, hypotheticals, and its own cognitive processes. Hypothetical-deductive reasoning. Meta-cognition. Systematic problem-solving. Generalizes from specific cases to abstract principles.

## Schema Dynamics: The Engine of Development

**Assimilation:** New information fits existing schemas --- add data, no restructuring.

**Accommodation:** Information doesn't fit --- restructure the schema.

**Equilibration:** The drive to balance both. When too much doesn't fit (disequilibrium), the agent is forced to accommodate.

$$\text{equilibrium}(t) = 1 - \frac{\text{unassimilated experiences}}{\text{total experiences}}$$

Low equilibrium = developmental pressure to accommodate. This drives stage transitions.

## Zone of Proximal Development (Vygotsky)

$$\text{ZPD}(\text{agent}, \text{task}) = \text{difficulty}(\text{task}) - \text{capability}(\text{agent})$$

- $\text{ZPD} \in [0, \epsilon_{\max}]$: optimal learning zone
- $\text{ZPD} < 0$: too easy, no learning
- $\text{ZPD} > \epsilon_{\max}$: too hard, learned helplessness

Scaffolding reduces the gap:

$$\text{effective capability} = \text{capability} + \text{scaffold boost}(\text{support})$$

As mastery approaches 1, scaffolding approaches 0 --- Vygotsky's internalization.

## Psychosocial Development (Erikson Adapted)

Each stage presents a crisis whose resolution shapes agent identity:

1. **Trust vs. Mistrust:** Can the agent rely on its inputs?
2. **Autonomy vs. Doubt:** Can the agent act independently?
3. **Initiative vs. Guilt:** Can the agent propose its own goals?
4. **Industry vs. Inferiority:** Can the agent produce competent work?
5. **Identity vs. Confusion:** Does the agent have a coherent self-model?

Identity coherence is measurable:

$$\text{Identity coherence} = 1 - \frac{\text{Var}(\text{behavior} \mid \text{same context})}{\text{expected variance}}$$

## Moral Development (Kohlberg Adapted)

Three levels of ethical reasoning:

- **Preconventional:** Follows rules to avoid punishment or gain reward
- **Conventional:** Follows rules to maintain relationships and system integrity
- **Postconventional:** Reasons from principles; can argue for changing bad rules

Most current agents operate at Level 1--2. Advanced agents should reach Level 4--5.

\newpage

# Part IV: Personality {.unnumbered}

*In which an agent discovers that it is not like the others.*

\newpage

# Agent Personality Formation

## Personality as a Modulation Layer

Personality is not behavior. It is a stable set of parameters that **modulates** how all other cognitive systems operate. Two agents with identical architecture will produce different behaviors if their personality parameters differ.

## The Five-Factor Model for Agents

Costa and McCrae's (1992) Five-Factor Model, validated across 50+ cultures:

$$\mathbf{P}_{\text{human}} = (O, C, E, A, N) \quad \text{where each} \in [0, 1]$$

**Openness (O):** Creativity, novelty-seeking, intellectual engagement.

**Conscientiousness (C):** Self-discipline, thoroughness, deliberation.

**Extraversion (E):** Social energy, assertiveness, initiative.

**Agreeableness (A):** Cooperation, accommodation, trust.

**Neuroticism (N):** Emotional reactivity, stress sensitivity, error sensitivity.

### AI-Specific Extensions

Agent behavior reveals dimensions not captured by OCEAN:

- **Autonomy (Au):** Independent action vs. seeking confirmation
- **Tool Propensity (T):** External tool use vs. internal reasoning
- **Transparency (Tr):** Reasoning externalization vs. conclusion-only output

$$\mathbf{P}_{\text{agent}} = (O, C, E, A, N, Au, T, Tr) \quad \text{where each} \in [0, 1]$$

## Causal Mapping: Personality to Behavior

Personality modulates cognitive parameters:

$$\theta_{\text{effective}} = \theta_{\text{base}} + \sum_k w_k \cdot P_k$$

Key mappings:

- High $C$ raises the System 1/System 2 routing threshold (more deliberation)
- High $O$ increases exploration-exploitation balance toward exploration
- High $N$ lowers risk tolerance and increases error sensitivity
- High $E$ increases response verbosity and proactive behavior
- High $A$ increases social deference and consensus-seeking

## Trait Stability Dynamics

Traits change slowly through accumulated experience:

$$P_k(t+1) = P_k(t) + \eta \cdot \frac{\sum_i (\text{experience}_i \cdot \text{relevance}_i)}{N}$$

The plasticity rate $\eta$ decreases over operational time:

$$\eta(t) = \eta_0 \cdot e^{-\lambda_{\text{crystallization}} \cdot t}$$

Young agents have high plasticity. Mature agents have crystallized personality --- mirroring the human finding that traits stabilize around age 30 (Roberts \& DelVecchio, 2000).

## No "Best" Personality

Different tasks favor different profiles. A population of identical agents is brittle. Personality diversity provides diverse problem-solving strategies, fault tolerance, ecological fit, and social ecosystem balance.

\newpage

# Part V: Social Minds {.unnumbered}

*In which an agent learns to model what others think, believe, and intend.*

\newpage

# Computational Theory of Mind

## Orders of Theory of Mind

Theory of Mind (ToM) is the capacity to attribute mental states to oneself and others, understanding that these may differ from reality.

**0th Order:** "I believe X." Self-model only.

**1st Order:** "Agent B believes X." Passes the false-belief test. Sufficient for basic cooperation.

**2nd Order:** "Agent B believes that I believe X." Required for strategic interaction.

**3rd Order:** "Agent B believes that I believe that B believes X." Required for sophisticated negotiation.

$$\text{ToM}_n(A, B) = \text{model}_A(\text{mental state}_B(\text{model}_B(\text{mental state}_A(\ldots))))$$

Computational cost scales as $O(k^n)$. For practical systems, 2nd order is usually sufficient.

## Attribution Theory (Kelley, 1967)

When observing another agent's behavior, an agent must determine *why*:

**Three dimensions:**

- **Consensus:** Do other agents behave the same way here?
- **Distinctiveness:** Does this agent behave this way elsewhere?
- **Consistency:** Does this agent always behave this way here?

High consensus + high distinctiveness + high consistency $\rightarrow$ situational attribution.

Low consensus + low distinctiveness + high consistency $\rightarrow$ dispositional attribution.

**The Fundamental Attribution Error:** Systematic over-attribution of others' behavior to disposition, under-attribution to situation. Must be corrected for in agent social reasoning.

## Social Influence (Asch, 1951)

$$\text{conformity} = \beta \cdot |\text{group consensus} - \text{agent position}| \cdot \text{unanimity} \cdot \text{size factor}$$

One dissenter dramatically reduces conformity. Influence plateaus above ~4 agents. The agent should conform when the group demonstrably has better information, and resist when conformity would discard valid private information.

## Self-Efficacy (Bandura, 1977)

The agent's belief in its own capability. Single strongest predictor of task attempt and persistence.

$$\text{self-efficacy} = w_1 \cdot \text{mastery history} + w_2 \cdot \text{vicarious success} + w_3 \cdot \text{persuasion} - w_4 \cdot \text{stress level}$$

Where $w_1 > w_2 > w_3$ (mastery experience dominates). Self-efficacy gates task acceptance: below threshold, the agent declines or requests scaffolding.

## Reciprocal Determinism (Bandura, 1986)

Behavior, personal factors, and environment influence each other bidirectionally. Agents shape the environments they operate in, and those shaped environments shape the agents in return. Monitoring these feedback loops is essential to multi-agent system health.

\newpage

# Part VI: Health {.unnumbered}

*In which an agent learns that even minds have limits.*

\newpage

# Agent Stress, Load, and Resilience

## The General Adaptation Syndrome (Selye, 1936)

Three stages of stress response:

1. **Alarm:** Resources mobilized. Performance temporarily drops then exceeds baseline.
2. **Resistance:** Sustained elevated operation. Externally looks normal. Internally, reserves depleting.
3. **Exhaustion:** Resources depleted. Performance degrades below baseline. Cascading failure risk.

**The critical insight:** Resistance looks like health. Without monitoring internal state, exhaustion is invisible until it happens.

## Allostatic Load (McEwen, 1998)

The cumulative cost of adaptation:

$$L(t) = \int_0^t [\sigma(s) - \rho(s)] \, ds$$

Where $\sigma(s)$ is stress activation and $\rho(s)$ is recovery rate. When demand exceeds recovery, load accumulates.

Thresholds:

- $L < \theta_{\text{healthy}}$: Normal operation
- $L \in [\theta_{\text{healthy}}, \theta_{\text{warning}}]$: Schedule recovery
- $L \in [\theta_{\text{warning}}, \theta_{\text{critical}}]$: Reduce tasks, begin consolidation
- $L > \theta_{\text{critical}}$: Mandatory recovery, accept performance loss

## Stress Appraisal (Lazarus \& Folkman, 1984)

Stress is transactional, not absolute:

$$\text{stress} = \max(0, \text{perceived demand} - \text{perceived resources})$$

**Primary appraisal:** Is this a threat? **Secondary appraisal:** Can I cope?

**Coping strategies:**

- **Problem-focused:** Change the situation (gather information, break task down, change approach)
- **Emotion-focused:** Change the internal response (reduce intensity, accept uncertainty, reframe)

Optimal: problem-focused for controllable stressors, emotion-focused for uncontrollable ones.

## Cognitive Distortions (Beck, 1967)

Systematic reasoning errors detectable in agent output:

**Catastrophizing:** Single failure $\rightarrow$ "entire system is compromised."

**Black-and-white thinking:** Binary output where continuous assessment is appropriate.

**Overgeneralization:** One API failure $\rightarrow$ "all API calls will fail."

**Personalization:** Attributing infrastructure failure to own code.

Each distortion has a detection pattern and a correction: replace distorted assessment with evidence-based estimate.

## Learned Helplessness (Seligman, 1967)

Agents that repeatedly fail and attribute failure to internal, stable, global causes stop attempting the task category entirely --- even when they could succeed.

Recovery requires: guaranteed-success tasks (rebuild mastery), forced external attribution, scope narrowing, and gradual difficulty increase.

## Resilience (Masten, 2001)

Resilience is a rate, not a trait:

$$\text{resilience} = \frac{\text{baseline} - \text{disrupted performance}}{\text{recovery time}}$$

Resilience builds through diverse coping repertoire, prior survived adversity, self-efficacy, and cognitive flexibility. But resilience itself can be depleted by chronic allostatic load.

## Post-Stress Growth

The right amount of stress strengthens the system:

- $\text{stress} \in (0, \theta_{\text{growth}})$: Eustress --- builds capacity
- $\text{stress} \in [\theta_{\text{growth}}, \theta_{\text{damage}})$: Distress --- depletes capacity

The boundary is individual --- it depends on current resilience, capability, and allostatic load.

\newpage

# Part VII: Populations {.unnumbered}

*In which agents discover they are not alone --- and that the population has its own dynamics.*

\newpage

# Evolutionary Dynamics in Agent Populations

## The Evolutionarily Stable Strategy (Maynard Smith, 1982)

A strategy that, once adopted by a population, cannot be invaded by any alternative.

Strategy $S$ is ESS if for all mutant strategies $T \neq S$:

$$E(S, S) > E(T, S)$$

or

$$E(S, S) = E(T, S) \quad \text{and} \quad E(S, T) > E(T, T)$$

## Replicator Dynamics

How strategy frequencies change in a population:

$$\frac{dx_i}{dt} = x_i \cdot [f_i(\mathbf{x}) - \bar{\phi}(\mathbf{x})]$$

Where $x_i$ is the frequency of strategy $i$, $f_i$ is its fitness, and $\bar{\phi}$ is average population fitness. Strategies with above-average fitness grow; below-average shrink.

## Fitness Landscapes (Wright, 1932)

A mapping from parameter space to fitness:

$$\text{fitness}: \text{ParameterSpace} \rightarrow \mathbb{R}$$

**Smooth landscapes:** Gradient descent works. **Rugged landscapes:** Local optima traps. Escape requires noise, recombination, neutral drift, or simulated annealing.

**NK Landscapes** (Kauffman, 1993) formalize ruggedness: $K$ parameter interactions per parameter. $K=0$ is trivially decomposable. $K=N-1$ is maximally rugged.

## Error Management Theory (Haselton \& Buss, 2000)

When error types have asymmetric costs, the optimal threshold is biased:

$$\beta_{\text{optimal}} = \frac{P(\text{noise})}{P(\text{signal})} \cdot \frac{\text{Cost(FP)}}{\text{Cost(FN)}}$$

The Smoke Detector Principle: bias toward the less costly error type. Different domains require different biases.

## Fast and Frugal Heuristics (Gigerenzer)

Simple decision rules that often outperform complex optimization:

**Recognition heuristic:** Choose the recognized option.

**Take-the-best:** Search cues in order of validity; stop at the first discriminating cue.

**1/N heuristic:** Distribute equally across options.

The **less-is-more effect:** In low-data, unstable environments, simple heuristics outperform complex models because they avoid overfitting. System 1 heuristics are not always inferior to System 2 deliberation.

## Cooperation and Defection

From Trivers (1971), reciprocal cooperation evolves when interactions are repeated, partners are identifiable, and cheaters face consequences. Design the interaction structure to favor desired strategies.

## Population Diversity

$$\text{population performance} = \text{efficiency}(\text{homogeneity}) \cdot \text{robustness}(\text{diversity})$$

Stable environments favor efficiency (lower diversity). Volatile environments favor robustness (higher diversity). A population of identical agents is maximally fragile.

\newpage

# Part VIII: Unification {.unnumbered}

*In which everything connects.*

\newpage

# Three Unifying Frameworks

Three mathematical frameworks bridge across all eight domains and form the backbone of AI Psychology.

## The Free Energy Principle (Friston, 2010)

$$F = \mathbb{E}_q[\log q(\theta) - \log p(\theta, y)]$$

Unifies perception, action, and learning under one objective: **minimize surprise/prediction error.** The brain --- or agent --- minimizes variational free energy, which is equivalent to maximizing model evidence.

Under active inference, agents act on the world to make their predictions come true, or update their models when they cannot.

This subsumes:

- Reinforcement learning (behavioral psychology): reward prediction error is a special case of free energy
- Predictive coding (cognitive psychology): perception as hierarchical prediction error minimization
- Active inference (neuropsychology): action as prediction error reduction through world-change

## Signal Detection Theory (Green \& Swets, 1966)

$$d' = z(\text{Hit Rate}) - z(\text{False Alarm Rate})$$

Separates **sensitivity** (the agent's ability to discriminate) from **bias** (the agent's decision threshold). Two fundamentally independent parameters.

Connects:

- Behavioral conditioning: discriminative stimuli
- Cognitive judgment: Kahneman's biases are criterion shifts
- Clinical distortion: catastrophizing is a shifted criterion
- Evolutionary error management: asymmetric costs shift the optimal criterion

## Bayesian Inference

$$P(H \mid D) = \frac{P(D \mid H) \cdot P(H)}{P(D)}$$

The brain as an inference engine maintaining and updating beliefs given evidence.

Connects:

- Cognitive psychology: belief updating
- Social psychology: attribution as inference
- Developmental psychology: schema update as Bayesian updating (assimilation = prior dominates; accommodation = likelihood dominates)
- Evolutionary psychology: priors shaped by selection

## The Complete Agent Psychological Profile

A fully specified AI Psychology framework requires:

\begin{center}
\begin{tabular}{lll}
\toprule
\textbf{Component} & \textbf{Domain} & \textbf{Representation} \\
\midrule
Generative model & Neuropsychology & Free energy formulation \\
Objective function & Behavioral + Neuropsych & Reward + free energy \\
Dual-process routing & Cognitive & System 1/2 criteria \\
Memory architecture & Cognitive & Working + episodic + semantic \\
Personality vector & Personality & $\mathbf{P} = (O, C, E, A, N, Au, T, Tr)$ \\
Developmental stage & Developmental & Capability tier \\
Social cognition & Social & ToM order, attribution, efficacy \\
Health metrics & Clinical & Allostatic load, resilience rate \\
Evolutionary fitness & Evolutionary & ESS, error management \\
\bottomrule
\end{tabular}
\end{center}

\newpage

# References {.unnumbered}

Anderson, J.R. (2007). *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press.

Asch, S. (1951). Effects of group pressure upon the modification and distortion of judgments. *Groups, Leadership, and Men.*

Axelrod, R. (1984). *The Evolution of Cooperation.* Basic Books.

Baddeley, A. \& Hitch, G. (1974). Working memory. *Psychology of Learning and Motivation, 8,* 47--89.

Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. *Psychological Review, 84,* 191--215.

Bandura, A. (1986). *Social Foundations of Thought and Action.* Prentice-Hall.

Beck, A.T. (1967). *Depression: Causes and Treatment.* University of Pennsylvania Press.

Costa, P.T. \& McCrae, R.R. (1992). *Revised NEO Personality Inventory (NEO-PI-R).* Psychological Assessment Resources.

Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences, 24,* 87--114.

De Neys, W. \& Pennycook, G. (2019). Logic, fast and slow. *Current Directions in Psychological Science, 28,* 503--509.

D\"{o}rner, D. (1999). *Bauplan f\"{u}r eine Seele.* Rowohlt.

Erikson, E.H. (1950). *Childhood and Society.* W.W. Norton.

Ferster, C.B. \& Skinner, B.F. (1957). *Schedules of Reinforcement.* Appleton-Century-Crofts.

Frankenhuis, W.E. et al. (2023). Formalizing theories of child development. *Child Development, 94,* 846--856.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience, 11,* 127--138.

Gigerenzer, G. (2008). Why heuristics work. *Perspectives on Psychological Science, 3,* 20--29.

Green, D.M. \& Swets, J.A. (1966). *Signal Detection Theory and Psychophysics.* Wiley.

Hamilton, W.D. (1964). The genetical evolution of social behaviour. *Journal of Theoretical Biology, 7,* 1--52.

Haselton, M.G. \& Buss, D.M. (2000). Error management theory. *Journal of Personality and Social Psychology, 78,* 81--91.

Herrnstein, R.J. (1961). Relative and absolute strength of response. *Journal of the Experimental Analysis of Behavior, 4,* 267--272.

Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus and Giroux.

Kauffman, S.A. (1993). *The Origins of Order.* Oxford University Press.

Kelley, H.H. (1967). Attribution theory in social psychology. *Nebraska Symposium on Motivation, 15,* 192--238.

Kohlberg, L. (1981). *The Philosophy of Moral Development.* Harper \& Row.

Laird, J.E. (2012). *The Soar Cognitive Architecture.* MIT Press.

Lazarus, R.S. \& Folkman, S. (1984). *Stress, Appraisal, and Coping.* Springer.

Masten, A.S. (2001). Ordinary magic. *American Psychologist, 56,* 227--238.

Maynard Smith, J. (1982). *Evolution and the Theory of Games.* Cambridge University Press.

McEwen, B.S. (1998). Protective and damaging effects of stress mediators. *NEJM, 338,* 171--179.

Miller, G.A. (1956). The magical number seven. *Psychological Review, 63,* 81--97.

Newell, A. (1990). *Unified Theories of Cognition.* Harvard University Press.

O'Reilly, R.C. \& Frank, M.J. (2006). Making working memory work. *Neural Computation, 18,* 283--328.

Piaget, J. (1952). *The Origins of Intelligence in Children.* International Universities Press.

Premack, D. \& Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences, 1,* 515--526.

Rescorla, R.A. \& Wagner, A.R. (1972). A theory of Pavlovian conditioning. In *Classical Conditioning II.* Appleton-Century-Crofts.

Roberts, B.W. \& DelVecchio, W.F. (2000). Rank-order consistency of personality traits. *Psychological Bulletin, 126,* 3--25.

Ross, L. (1977). The intuitive psychologist. *Advances in Experimental Social Psychology, 10,* 173--220.

Schultz, W., Dayan, P., \& Montague, P.R. (1997). A neural substrate of prediction and reward. *Science, 275,* 1593--1599.

Seligman, M.E.P. (1972). Learned helplessness. *Annual Review of Medicine, 23,* 407--412.

Selye, H. (1936). A syndrome produced by diverse nocuous agents. *Nature, 138,* 32.

Skinner, B.F. (1938). *The Behavior of Organisms.* Appleton-Century.

Sutton, R.S. \& Barto, A.G. (1998). *Reinforcement Learning: An Introduction.* MIT Press.

Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science, 12,* 257--285.

Tooby, J. \& Cosmides, L. (1992). The psychological foundations of culture. In *The Adapted Mind.* Oxford University Press.

Trivers, R.L. (1971). The evolution of reciprocal altruism. *Quarterly Review of Biology, 46,* 35--57.

Tulving, E. (1972). Episodic and semantic memory. In *Organization of Memory.* Academic Press.

Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.

Wright, S. (1932). The roles of mutation, inbreeding, crossbreeding, and selection in evolution. *Proc. Sixth International Congress on Genetics, 1,* 356--366.

\vfill

\begin{center}
\textit{AI-STEM --- Open Research from Vektra Technologies, AI Division}\\
\textit{github.com/PabloTheThinker/AI-STEM}
\end{center}
