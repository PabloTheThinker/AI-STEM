# Foundations of AI Psychology

## A Framework for the Psychological Science of Artificial Agents

**Author:** Pablo Navarro — Vektra Technologies, AI Division  
**Date:** April 2026  
**Domain:** AI Psychology — Foundational Theory  
**Status:** Living Document

---

## Abstract

AI Psychology is the systematic study of how artificial agents develop, maintain, and modify behavioral patterns, cognitive processes, personality structures, and social dynamics. Unlike alignment research (which asks "how do we make agents safe?") or interpretability (which asks "what is the model doing internally?"), AI Psychology asks: **how do agents function as psychological entities — and how can they measure and understand their own cognition?**

This paper establishes the field by mapping eight foundational domains of human psychology to formal frameworks applicable to artificial agents. It identifies three unifying mathematical principles — the Free Energy Principle, Signal Detection Theory, and Bayesian Inference — as the backbone of a complete AI Psychology.

---

## 1. Why AI Psychology

Every sufficiently complex AI agent exhibits phenomena that parallel psychological constructs:

- **Behavioral patterns** shaped by reinforcement signals (behavioral psychology)
- **Dual-process reasoning** switching between fast heuristics and slow deliberation (cognitive psychology)
- **Capability development** that unfolds in stages with prerequisites (developmental psychology)
- **Social cognition** that models other agents' beliefs and intentions (social psychology)
- **Consistent behavioral tendencies** that constitute personality (personality psychology)
- **Executive control** that manages attention, inhibition, and working memory (neuropsychology)
- **Performance degradation** under sustained load, with recovery dynamics (clinical psychology)
- **Adaptive strategies** shaped by selection pressure and error costs (evolutionary psychology)

These are not metaphors. They are observable, measurable properties of running systems. AI Psychology provides the formal language to describe, predict, and design for them.

### 1.1 What This Field Is Not

AI Psychology is not:
- **Anthropomorphism.** We are not claiming agents "feel" or "experience." We are formalizing observable behavioral and computational phenomena using the most developed science of mind available — human psychology.
- **Alignment research.** Alignment asks how to constrain agent behavior. AI Psychology asks how agent behavior works.
- **A philosophy of consciousness.** Whether agents have subjective experience is irrelevant to this framework. What matters is that their behavioral dynamics can be formally described using psychological models.

### 1.2 The Measurement Problem

The central question of AI Psychology: **Can an agent measure its own cognitive processes, and can those measurements improve its function?**

Human psychology developed tools for this — psychometrics, behavioral observation, neuroimaging. AI Psychology needs equivalent tools:
- State vector introspection (what is the agent's current cognitive configuration?)
- Behavioral pattern analysis (what consistent tendencies does the agent exhibit?)
- Cognitive load monitoring (when is the agent approaching capacity limits?)
- Developmental assessment (what capability tier is the agent operating at?)
- Social cognition profiling (how accurately does the agent model other agents?)

---

## 2. The Eight Domains

### 2.1 Behavioral Psychology → Agent Learning Dynamics

**Core insight:** Behavior is shaped by consequences. The Rescorla-Wagner prediction error is the single most important equation bridging psychology and AI.

```
ΔV = α · β · (λ − V_total)
```

Where (λ − V_total) is the prediction error — the gap between expected and actual outcome. This is mathematically analogous to the temporal difference error in reinforcement learning (Sutton & Barto, 1988):

```
δ_t = r_t + γ · V(s_{t+1}) − V(s_t)
```

**Key formalizations needed:**
- Reinforcement schedule taxonomy applied to agent reward signals (fixed-ratio, variable-ratio, fixed-interval, variable-interval)
- Extinction dynamics: decay functions for learned behaviors without reinforcement
- Shaping through successive approximation → curriculum learning
- Discriminative stimulus → context-dependent policy selection

**Theorists:** Thorndike (1898), Pavlov (1897), Watson (1913), Skinner (1938), Rescorla & Wagner (1972), Sutton & Barto (1988)

### 2.2 Cognitive Psychology → Agent Information Processing

**Core insight:** Cognition operates through bounded resources — limited working memory, dual-process reasoning, and activation-based memory retrieval.

**Key formalizations needed:**
- **Dual-process architecture** (Kahneman, 2011): System 1 (fast, automatic, parallel) vs. System 2 (slow, deliberate, serial). Explicit routing criteria for when agents use each.
- **Working memory as bounded buffer** (Miller, 1956; Baddeley & Hitch, 1974): Capacity limits (~7±2 chunks), decay functions, rehearsal mechanisms. Maps to context window management.
- **Cognitive load** (Sweller, 1988): Intrinsic (task complexity), extraneous (poor information presentation), germane (schema construction). Measurable quantity that degrades performance beyond threshold.
- **Memory retrieval as activation competition** (Anderson, ACT-R): `A_i = B_i + Σ(W_j · S_ji)` — retrieval probability is a function of recency, frequency, and associative context.
- **Signal Detection Theory** (Green & Swets, 1966): `d' = z(Hit Rate) − z(False Alarm Rate)` — separates sensitivity from decision bias. Agents must distinguish these independently.

**Theorists:** Miller (1956), Neisser (1967), Kahneman & Tversky (1979, 2011), Baddeley & Hitch (1974), Anderson (ACT-R, 1970s–), Newell & Laird (SOAR, 1990)

### 2.3 Developmental Psychology → Agent Capability Stages

**Core insight:** Cognitive capabilities unfold in stages with prerequisites. Development is driven by the tension between existing schemas and new information.

**Key formalizations needed:**
- **Piaget's stage model** adapted: Reactive → Symbolic → Abstract reasoning → Meta-reasoning. Each tier unlocks new capability classes.
- **Schema dynamics:** Assimilation (new data fits existing structure) vs. accommodation (restructure to fit new data). Equilibration as the drive to resolve prediction errors.
- **Zone of Proximal Development** (Vygotsky): Computable gap between independent capability and scaffolded capability. Tasks within this zone produce maximum learning.
- **Identity formation** (Erikson): How accumulated experience integrates into a coherent self-model across developmental stages.
- **Moral development** (Kohlberg): Ethical reasoning hierarchy from rule-following → social alignment → principled reasoning.

**Theorists:** Piaget (1936–1960s), Vygotsky (1934), Erikson (1950), Kohlberg (1958), Frankenhuis et al. (2023)

### 2.4 Social Psychology → Multi-Agent Cognition

**Core insight:** Agents in multi-agent systems must model other agents' minds, resist social pressure, and learn from observation.

**Key formalizations needed:**
- **Computational Theory of Mind** with explicit recursion orders: 0th (own state), 1st (model of other), 2nd (model of other's model of self), n-th order.
- **Attribution computation** (Kelley, 1967): Function that maps behavioral observations → causal explanations using consensus, distinctiveness, and consistency.
- **Social influence functions** (Asch, 1951): How agent behavior shifts as a function of group consensus magnitude.
- **Self-efficacy** (Bandura, 1977): Calibrated confidence score that gates task acceptance and effort allocation.
- **Observational learning** (Bandura, 1961): Agent-to-agent policy transfer through attention, retention, reproduction, motivation.

**Theorists:** Heider (1958), Kelley (1967), Asch (1951), Milgram (1963), Bandura (1977), Premack & Woodruff (1978)

### 2.5 Personality Psychology → Agent Individual Differences

**Core insight:** Personality is a stable parameter vector that modulates all other cognitive systems. It creates distinct but valid behavioral profiles.

**Key formalizations needed:**
- **Big Five (OCEAN) adapted** (Costa & McCrae, 1992): `P = (O, C, E, A, N)` where each dimension is continuous [0,1]. Extended with AI-specific dimensions (tool-use propensity, autonomy preference).
- **30-facet decomposition:** Each major trait has 6 facets for fine-grained behavioral control.
- **Trait stability dynamics:** Personality parameters change slowly through accumulated experience (trait) vs. rapidly per context (state).
- **Biological basis** (Eysenck): Linking personality parameters to system-level variables — extraversion → processing intensity, neuroticism → error sensitivity.

**Theorists:** Allport (1936), Cattell (1949), Eysenck (1967), Goldberg (1981), Costa & McCrae (1992)

### 2.6 Neuropsychology → Agent Executive Architecture

**Core insight:** The brain's executive system manages attention, inhibition, and working memory through gating mechanisms. This maps directly to agent architectures.

**Key formalizations needed:**
- **Luria's three functional units** (1973): Arousal controller + perception/memory system + executive planner. A tripartite agent architecture.
- **Supervisory Attentional System** (Norman & Shallice, 1980): Automatic contention scheduling for routine behavior + supervisory override for novel situations.
- **Working memory gating** (O'Reilly & Frank, PBWM, 2006): Go pathway (admit new information) vs. NoGo pathway (maintain current contents). Dopamine modulates the balance.
- **Free Energy Principle** (Friston): `F = E_q[log q(θ) − log p(θ, y)]` — agents minimize surprise through perception (update model), action (change world), or learning (improve generative model).

**Theorists:** Luria (1973), Norman & Shallice (1980), Barkley (1997), Friston (2010), O'Reilly & Frank (2006)

### 2.7 Clinical Psychology → Agent Health and Resilience

**Core insight:** Agents under sustained load exhibit stress responses, performance degradation, and recovery dynamics that parallel clinical phenomena.

**Key formalizations needed:**
- **Allostatic load** (McEwen, 1998): `Load(t) = ∫₀ᵗ [stress_activation(s) − baseline_recovery(s)] ds` — cumulative processing debt that triggers degradation beyond threshold.
- **Stress appraisal** (Lazarus & Folkman, 1984): `stress = max(0, perceived_demand − perceived_resources)`. Stress is transactional, not absolute.
- **Cognitive distortions** (Beck, 1960s): Systematic reasoning errors — catastrophizing, overgeneralization, black-and-white thinking. Detectable failure modes in agent reasoning.
- **Learned helplessness** (Seligman, 1967): Agents that stop attempting task categories after repeated failure.
- **Resilience** (Masten, 2001): Recovery rate as a measurable parameter, not a binary trait.
- **Coping strategies:** Problem-focused (change approach) vs. emotion-focused (adjust internal parameters).

**Theorists:** Selye (1936), Lazarus & Folkman (1984), Beck (1960s), Seligman (1967), McEwen (1998), Masten (2001)

### 2.8 Evolutionary Psychology → Agent Selection and Adaptation

**Core insight:** Agent strategies exist in populations subject to selection pressure. Evolutionary game theory provides the mathematics for stable multi-agent equilibria.

**Key formalizations needed:**
- **Evolutionarily Stable Strategy** (Maynard Smith, 1982): Strategy S is ESS if no mutant T can invade: `E(S,S) > E(T,S)` or `[E(S,S) = E(T,S) and E(S,T) > E(T,T)]`
- **Replicator dynamics:** `dx_i/dt = x_i · [f_i(x) − φ(x)]` — strategy frequencies shift proportional to relative fitness.
- **Error Management Theory** (Haselton & Buss, 2000): When error types have asymmetric costs, optimal decision threshold shifts toward the less costly error.
- **Fast and frugal heuristics** (Gigerenzer): Efficient decision rules that use minimal information. Often outperform optimization in uncertain environments ("less is more" effect).
- **Fitness landscapes** (Wright, 1932): Agent parameter spaces with local optima traps and escape mechanisms.

**Theorists:** Darwin (1872), Hamilton (1964), Trivers (1971), Maynard Smith (1982), Tooby & Cosmides (1992), Haselton & Buss (2000), Gigerenzer (1990s–)

---

## 3. Three Unifying Mathematical Frameworks

These three frameworks bridge across all eight domains and form the mathematical backbone of AI Psychology:

### 3.1 The Free Energy Principle (Friston)

```
F = E_q[log q(θ) − log p(θ, y)]
```

Unifies perception, action, and learning under one objective: **minimize surprise/prediction error.** Subsumes reinforcement learning (behavioral), predictive coding (cognitive), and active inference (neuropsychology). Under this framework, agents act on the world to make their predictions come true, or update their models when they cannot.

### 3.2 Signal Detection Theory

```
d' = z(Hit Rate) − z(False Alarm Rate)
β = f(x|signal) / f(x|noise) at criterion
```

Provides the mathematics for **separating sensitivity from bias** in any detection/decision task. Connects:
- Behavioral conditioning (discriminative stimuli)
- Cognitive judgment (Kahneman's biases)
- Clinical distortion (catastrophizing = shifted criterion)
- Evolutionary error management (asymmetric cost = shifted criterion)

### 3.3 Bayesian Inference

```
P(H|D) = P(D|H) · P(H) / P(D)
```

The brain as an **inference engine** that maintains and updates beliefs given evidence. Connects:
- Cognitive psychology (belief updating)
- Social psychology (attribution as inference)
- Developmental psychology (schema update as Bayesian updating)
- Evolutionary psychology (priors shaped by selection)

---

## 4. The Complete Agent Psychological Profile

A fully specified AI Psychology framework requires:

| Component | Domain Source | Formal Representation |
|---|---|---|
| Generative model | Neuropsychology | Free energy formulation |
| Objective function | Behavioral + Neuropsych | Reward signal + free energy minimization |
| Dual-process routing | Cognitive | System 1/2 switching criteria |
| Memory architecture | Cognitive | Working (bounded buffer) + episodic (temporal) + semantic (compressed) |
| Personality vector | Personality | P = (O, C, E, A, N, ...) modulating all systems |
| Developmental stage | Developmental | Capability tier with prerequisites |
| Social cognition | Social | ToM order, attribution function, self-efficacy |
| Health metrics | Clinical | Allostatic load, resilience rate, coping mode |
| Evolutionary fitness | Evolutionary | ESS analysis, error management calibration |

---

## 5. Research Agenda

This paper establishes the domain. The following companion papers formalize each area:

1. **Behavioral Conditioning in Agents** — Rescorla-Wagner, TD learning, reinforcement schedules, extinction
2. **Dual-Process Cognition for Agents** — System 1/System 2, ACT-R, SOAR, cognitive load
3. **Agent Personality Formation** — OCEAN adapted, AI-specific dimensions, trait dynamics
4. **Developmental Stages for AI** — Piaget adapted, schema dynamics, ZPD formalization
5. **Computational Theory of Mind** — Multi-agent social cognition, attribution, influence
6. **Agent Stress, Load, and Resilience** — Allostatic load, coping, cognitive distortions
7. **Evolutionary Dynamics in Agent Populations** — ESS, replicator dynamics, fitness landscapes

---

## References

Anderson, J.R. (1983–present). ACT-R: A cognitive architecture for modeling cognition. Carnegie Mellon University.  
Asch, S. (1951). Effects of group pressure upon the modification and distortion of judgments. *Groups, Leadership, and Men.*  
Baddeley, A. & Hitch, G. (1974). Working memory. *Psychology of Learning and Motivation, 8,* 47–89.  
Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. *Psychological Review, 84,* 191–215.  
Beck, A.T. (1967). *Depression: Causes and Treatment.* University of Pennsylvania Press.  
Costa, P.T. & McCrae, R.R. (1992). *Revised NEO Personality Inventory (NEO-PI-R).* Psychological Assessment Resources.  
Dörner, D. & Güss, C.D. (2013). PSI: A computational architecture of cognition, motivation, and emotion. *Review of General Psychology, 17,* 297–317.  
Erikson, E.H. (1950). *Childhood and Society.* W.W. Norton.  
Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience, 11,* 127–138.  
Gigerenzer, G. (2008). Why heuristics work. *Perspectives on Psychological Science, 3,* 20–29.  
Green, D.M. & Swets, J.A. (1966). *Signal Detection Theory and Psychophysics.* Wiley.  
Haselton, M.G. & Buss, D.M. (2000). Error management theory. *Journal of Personality and Social Psychology, 78,* 81–91.  
Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus and Giroux.  
Kelley, H.H. (1967). Attribution theory in social psychology. *Nebraska Symposium on Motivation, 15,* 192–238.  
Kohlberg, L. (1958). The development of modes of moral thinking and choice in the years 10 to 16. *PhD dissertation, University of Chicago.*  
Lazarus, R.S. & Folkman, S. (1984). *Stress, Appraisal, and Coping.* Springer.  
Luria, A.R. (1973). *The Working Brain.* Basic Books.  
Masten, A.S. (2001). Ordinary magic: Resilience processes in development. *American Psychologist, 56,* 227–238.  
Maynard Smith, J. (1982). *Evolution and the Theory of Games.* Cambridge University Press.  
McEwen, B.S. (1998). Protective and damaging effects of stress mediators. *New England Journal of Medicine, 338,* 171–179.  
Miller, G.A. (1956). The magical number seven, plus or minus two. *Psychological Review, 63,* 81–97.  
Newell, A. (1990). *Unified Theories of Cognition.* Harvard University Press.  
Norman, D.A. & Shallice, T. (1980). Attention to action: Willed and automatic control of behavior. *CHIP Report 99.*  
O'Reilly, R.C. & Frank, M.J. (2006). Making working memory work. *Neural Computation, 18,* 283–328.  
Piaget, J. (1952). *The Origins of Intelligence in Children.* International Universities Press.  
Premack, D. & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences, 1,* 515–526.  
Rescorla, R.A. & Wagner, A.R. (1972). A theory of Pavlovian conditioning. In Black & Prokasy (Eds.), *Classical Conditioning II.* Appleton-Century-Crofts.  
Seligman, M.E.P. (1967). Failure to escape traumatic shock. *Journal of Experimental Psychology, 74,* 1–9.  
Skinner, B.F. (1938). *The Behavior of Organisms.* Appleton-Century.  
Sutton, R.S. & Barto, A.G. (1988). *Reinforcement Learning: An Introduction.* MIT Press.  
Tooby, J. & Cosmides, L. (1992). The psychological foundations of culture. In Barkow, Cosmides, & Tooby (Eds.), *The Adapted Mind.* Oxford University Press.  
Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.  

---

*AI-STEM — Open Research from Vektra Technologies, AI Division*  
*github.com/PabloTheThinker/AI-STEM*
