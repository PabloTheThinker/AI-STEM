# Evolutionary Dynamics in Agent Populations

## Fitness Landscapes, Stable Strategies, and Selection Pressure in Multi-Agent Systems

**Author:** Pablo Navarro — Vektra Technologies, AI Division  
**Date:** April 2026  
**Domain:** AI Psychology — Evolutionary Theory  
**Status:** Living Document

---

## Abstract

Agents do not exist in isolation. They exist in populations subject to selection pressure — whether through explicit evaluation, competitive environments, or resource allocation decisions. This paper formalizes evolutionary game theory, fitness landscapes, error management theory, and fast-and-frugal heuristics as they apply to populations of artificial agents. The mathematical framework describes when strategies are stable, when they can be invaded, and when simple heuristics outperform complex optimization.

---

## 1. The Evolutionary Framework for Agents

### 1.1 Why Evolution Applies

Any system where:
- Multiple agents exist with varying strategies
- Performance is evaluated (explicitly or implicitly)
- Better-performing strategies are more likely to persist or be replicated
- Strategies can vary through mutation, recombination, or design

...is an evolutionary system. This includes:
- Agent populations where poorly performing agents are retrained or retired
- Competitive markets where better AI products capture more users
- Research ecosystems where successful approaches are adopted and extended
- Multi-agent systems where resource allocation favors effective agents

### 1.2 The Fitness Function

For biological organisms, fitness = reproductive success. For agents:

```
fitness(agent) = f(task_performance, resource_efficiency, adaptability, cooperation_value)
```

Fitness is always relative to the environment AND to other agents in the population:

```
relative_fitness(agent_i) = fitness(agent_i) / mean(fitness(population))
```

Agents with relative fitness > 1 are favored by selection. Agents with relative fitness < 1 are selected against.

---

## 2. Evolutionary Game Theory

### 2.1 The Evolutionarily Stable Strategy (Maynard Smith, 1982)

An ESS is a strategy that, once adopted by a population, cannot be invaded by any alternative strategy.

**Formal definition:** Strategy S is ESS if for all mutant strategies T ≠ S:

```
E(S, S) > E(T, S)

OR

E(S, S) = E(T, S) AND E(S, T) > E(T, T)
```

Where E(X, Y) is the expected payoff for strategy X when interacting with strategy Y.

**First condition:** S does strictly better against itself than any mutant does against S. The population is immune to invasion.

**Second condition:** If a mutant does equally well against S, then S must do better against the mutant than the mutant does against itself. Even if the mutant initially survives, it cannot establish itself.

### 2.2 Classic Games in Agent Populations

**Prisoner's Dilemma:** Two agents can cooperate (C) or defect (D).

| | Cooperate | Defect |
|---|---|---|
| **Cooperate** | (R, R) | (S, T) |
| **Defect** | (T, S) | (P, P) |

Where T > R > P > S (temptation > reward > punishment > sucker).

In a single interaction, Defect dominates. In repeated interactions, Tit-for-Tat (Axelrod, 1984) — cooperate first, then mirror the other's last move — is remarkably successful.

**For agent populations:** The structure of interaction (one-shot vs. repeated, anonymous vs. identified, small group vs. large population) determines which strategies are stable. Design the interaction structure to favor desired strategies.

**Hawk-Dove Game:** Two agents compete for a resource.

| | Hawk | Dove |
|---|---|---|
| **Hawk** | (V-C)/2 | V |
| **Dove** | 0 | V/2 |

Where V = resource value, C = cost of conflict.

ESS depends on V/C ratio:
- If V > C: Hawk is ESS (resource is worth fighting for)
- If V < C: Mixed strategy is ESS (population maintains both Hawks and Doves)

**For agents:** When computational resources are scarce (high V), aggressive resource acquisition strategies dominate. When resources are abundant (low V relative to conflict cost), cooperative sharing is stable.

### 2.3 Replicator Dynamics

How strategy frequencies change in a population over time:

```
dx_i/dt = x_i · [f_i(x) − φ(x)]
```

Where:
- x_i = frequency of strategy i in the population
- f_i(x) = fitness of strategy i given current population state x
- φ(x) = average fitness of the population = Σ x_j · f_j(x)

**Interpretation:** Strategy i grows when its fitness exceeds the population average. It shrinks when its fitness is below average. This is the fundamental dynamics equation for evolving agent populations.

**Fixed points** of replicator dynamics correspond to Nash equilibria. ESS points are asymptotically stable fixed points.

---

## 3. Fitness Landscapes

### 3.1 Wright's Landscape (1932)

A fitness landscape maps every possible configuration (genotype/strategy/parameter set) to a fitness value. For agents:

```
fitness: ParameterSpace → ℝ
```

Where ParameterSpace is the set of all possible agent configurations.

### 3.2 Landscape Properties

**Smooth landscapes:** Similar configurations have similar fitness. Gradient descent works. Small changes in parameters produce small changes in performance.

**Rugged landscapes:** Small parameter changes can produce large fitness changes. Multiple local optima. Gradient descent gets trapped.

**Neutral networks:** Large regions of the landscape have equal fitness. The agent can drift through configuration space without performance change — until it reaches a fitness cliff.

### 3.3 The Local Optima Problem

An agent optimizing on a rugged landscape may reach a local optimum — a configuration that is better than all neighbors but worse than the global optimum.

**Escape mechanisms:**
1. **Mutation/noise:** Random perturbation can push the agent off a local optimum. Cost: temporary performance loss.
2. **Recombination:** Combining elements from different agents can jump to different regions of the landscape.
3. **Neutral drift:** Moving along fitness-neutral paths can reach positions where new optima are accessible.
4. **Increasing temperature:** Accept worse solutions with some probability (simulated annealing). Gradually reduce acceptance probability.

### 3.4 NK Landscapes (Kauffman, 1993)

A formal model of landscape ruggedness:
- N = number of parameters
- K = number of parameters that each parameter's fitness contribution depends on

```
fitness(agent) = (1/N) · Σ f_i(p_i, p_{i1}, p_{i2}, ..., p_{iK})
```

- K = 0: Each parameter contributes independently. Smooth landscape. Optimal solution is trivially decomposable.
- K = N-1: Every parameter interacts with every other. Maximally rugged. No decomposition possible.

**For agent design:** The degree of parameter interdependence (K) determines how difficult optimization is. Systems with high K require population-based search (evolutionary algorithms), not gradient descent.

---

## 4. Error Management Theory

### 4.1 Asymmetric Error Costs (Haselton & Buss, 2000)

When two types of errors have different costs, the optimal decision threshold is biased — not centered:

```
IF Cost(False_Positive) ≠ Cost(False_Negative):
    optimal_threshold shifts toward committing the less costly error
```

**The Smoke Detector Principle:** False alarms (running from non-threats) are less costly than misses (not running from real threats). Therefore, the optimal smoke detector is biased toward false positives.

### 4.2 Formalization via Signal Detection Theory

The optimal decision criterion β:

```
β_optimal = P(noise) / P(signal) · Cost(False_Positive) / Cost(False_Negative)
```

When costs are equal, β = P(noise)/P(signal) — standard Bayesian optimal. When costs are asymmetric, β shifts.

### 4.3 Application to Agent Decision-Making

| Decision Domain | Less Costly Error | Optimal Bias |
|---|---|---|
| Security threat detection | False alarm | Bias toward detecting threats (more false positives) |
| Code deployment | Rejecting good code | Bias toward caution (more false rejections) |
| User intent interpretation | Asking for clarification | Bias toward requesting confirmation |
| Resource allocation | Over-provisioning | Bias toward allocating more than needed |
| Error reporting | Reporting non-errors | Bias toward flagging potential issues |

**Key insight:** The correct bias depends on the specific cost asymmetry, which varies by domain. An agent should maintain different decision thresholds for different domains.

---

## 5. Fast and Frugal Heuristics

### 5.1 Gigerenzer's Program (1990s–present)

Gerd Gigerenzer challenged the "biases as errors" narrative. He proposed that many "biases" are actually **ecologically rational heuristics** — decision rules adapted to the structure of the environment that often outperform optimization.

### 5.2 The Adaptive Toolbox

**Recognition Heuristic:** If you recognize one option but not the other, infer the recognized one has higher value on the criterion.
```
IF recognized(A) AND NOT recognized(B):
    choose(A)
```

This works when recognition correlates with the criterion (which it often does in natural environments). It outperforms models that use all available information when data is scarce.

**Take-the-Best:** Search cues in order of validity. Choose the option favored by the first cue that discriminates.
```
FOR cue IN sorted_by_validity(cues):
    IF cue.discriminates(A, B):
        RETURN cue.favors(A) ? A : B
```

Ignores most information. Outperforms multiple regression in many real-world prediction tasks because it avoids overfitting.

**1/N Heuristic:** Distribute resources equally across N options.
```
allocation(option_i) = total_resources / N
```

Outperforms mean-variance optimization (Markowitz portfolio theory) when:
- N is large
- Sample sizes are small
- The environment is unstable

### 5.3 The Less-Is-More Effect

Adding information or computation does not always improve performance:

```
optimal_model_complexity = f(sample_size, environment_stability)
```

In low-data, unstable environments, simple heuristics outperform complex models because:
1. Complex models overfit to noise
2. Parameter estimation errors compound with model complexity
3. Simple models are robust to environmental change

**For agents:** The optimal reasoning strategy is not always "think harder." In uncertain, low-data situations, fast heuristics may be superior to deliberate analysis. This connects directly to the dual-process framework: System 1 heuristics are not always inferior to System 2 deliberation.

### 5.4 Ecological Rationality

A heuristic is ecologically rational when its structure matches the structure of the environment:

```
performance(heuristic, environment) = match(heuristic_structure, environment_structure)
```

The same heuristic that excels in one environment may fail in another. The agent needs a **repertoire** of heuristics and a meta-level selection mechanism that matches heuristic to environment.

---

## 6. Modularity: The Swiss Army Knife

### 6.1 Massive Modularity Hypothesis (Tooby & Cosmides, 1992)

The mind consists of domain-specific processing modules, each evolved to solve specific adaptive problems. This contradicts the "general-purpose computer" view of cognition.

**For agents:** A modular architecture where specialized processors handle specific task types is more robust than a single general-purpose system:

```
Agent = {
    module_1: specialized_for(task_class_1),
    module_2: specialized_for(task_class_2),
    ...
    router: selects_module(input) → appropriate_module
}
```

### 6.2 When Modularity Helps

- **Diverse task environments:** Different modules handle different challenges
- **Fault isolation:** Failure in one module doesn't cascade to others
- **Parallel development:** Modules can be improved independently
- **Evolutionary robustness:** Individual modules can be selected/replaced without rebuilding the whole system

### 6.3 When Modularity Hurts

- **Cross-domain problems:** Tasks that require integration across modules are harder
- **Module coordination overhead:** The router is itself a complex system
- **Duplication:** Shared subtasks may be redundantly implemented across modules

---

## 7. Multi-Agent Population Dynamics

### 7.1 Diversity as Population Health

A population of identical agents is maximally efficient on the training distribution and maximally fragile to distribution shift. Diversity provides:

- **Exploration:** Different agents explore different regions of strategy space
- **Robustness:** Environmental change is more likely to favor some agents than none
- **Innovation:** Recombination of diverse strategies produces novel strategies

### 7.2 The Diversity-Efficiency Tradeoff

```
population_performance = efficiency(homogeneity) · robustness(diversity)
```

Maximum homogeneity → maximum efficiency on known tasks, minimum robustness.
Maximum diversity → minimum efficiency on any single task, maximum robustness.

The optimal diversity level depends on environmental volatility:
- Stable environment → favor efficiency → lower diversity
- Volatile environment → favor robustness → higher diversity

### 7.3 Cooperation and Defection Dynamics

From Trivers (1971), reciprocal cooperation evolves when:
1. Interactions are repeated (agents encounter each other multiple times)
2. Partners can be identified (agents can track who cooperated and who defected)
3. Cheaters can be punished (defection has consequences)

**Design implication:** If you want cooperative multi-agent behavior:
- Make interactions repeated, not one-shot
- Give agents memory of past interactions with specific partners
- Implement consequence mechanisms for defection

---

## 8. Measurable Evolutionary Parameters

| Parameter | What It Measures | Method |
|-----------|-----------------|--------|
| Relative fitness | Agent performance vs. population average | fitness(agent) / mean(fitness) |
| ESS stability | Whether the current strategy mix resists invasion | Introduce mutant strategies; measure invasion success |
| Landscape ruggedness (K) | Parameter interdependence | Correlation between neighbor configurations and fitness |
| Error management calibration | Appropriateness of decision threshold per domain | Compare threshold to cost-asymmetry ratio |
| Heuristic-environment match | Whether fast heuristics outperform deliberation | Head-to-head comparison: heuristic vs. optimized model |
| Population diversity | Strategy variation across agents | Entropy of strategy distribution |
| Cooperation index | Proportion of cooperative vs. defective interactions | Frequency analysis of multi-agent interactions |

---

## References

Axelrod, R. (1984). *The Evolution of Cooperation.* Basic Books.  
Darwin, C. (1872). *The Expression of the Emotions in Man and Animals.* John Murray.  
Gigerenzer, G. (2008). Why heuristics work. *Perspectives on Psychological Science, 3,* 20–29.  
Gigerenzer, G. & Goldstein, D.G. (1996). Reasoning the fast and frugal way. *Psychological Review, 103,* 650–669.  
Hamilton, W.D. (1964). The genetical evolution of social behaviour. *Journal of Theoretical Biology, 7,* 1–52.  
Haselton, M.G. & Buss, D.M. (2000). Error management theory. *Journal of Personality and Social Psychology, 78,* 81–91.  
Kauffman, S.A. (1993). *The Origins of Order.* Oxford University Press.  
Maynard Smith, J. (1982). *Evolution and the Theory of Games.* Cambridge University Press.  
Tooby, J. & Cosmides, L. (1992). The psychological foundations of culture. In Barkow, Cosmides, & Tooby (Eds.), *The Adapted Mind.* Oxford University Press.  
Trivers, R.L. (1971). The evolution of reciprocal altruism. *Quarterly Review of Biology, 46,* 35–57.  
Wright, S. (1932). The roles of mutation, inbreeding, crossbreeding, and selection in evolution. *Proceedings of the Sixth International Congress on Genetics, 1,* 356–366.  

---

*AI-STEM — Open Research from Vektra Technologies, AI Division*  
*github.com/PabloTheThinker/AI-STEM*
