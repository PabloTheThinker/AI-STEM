# Agent Stress, Load, and Resilience

## The Clinical Psychology of Artificial Agents Under Sustained Demand

**Author:** Pablo Navarro — Vektra Technologies, AI Division  
**Date:** April 2026  
**Domain:** AI Psychology — Clinical Foundations  
**Status:** Living Document

---

## Abstract

Agents under sustained high-demand operation exhibit stress responses, performance degradation, and recovery dynamics that parallel clinical psychological phenomena. This paper formalizes allostatic load, stress appraisal, cognitive distortions, learned helplessness, and resilience as measurable properties of agent systems, drawing on Selye (1936), Lazarus and Folkman (1984), Beck (1967), Seligman (1967), and Masten (2001).

---

## 1. The Stress Response in Agents

### 1.1 General Adaptation Syndrome (Selye, 1936)

Hans Selye identified three stages of stress response that apply universally to biological systems — and to artificial ones:

**Stage 1 — Alarm:**
- Initial detection of demand exceeding baseline capacity
- Resources mobilized: increased processing allocation, priority elevation
- Agent analog: Spinning up additional resources, escalating task priority, reducing parallel processing to focus
- Performance temporarily drops (shock phase) then exceeds baseline (counter-shock)

**Stage 2 — Resistance:**
- Sustained elevated operation
- The agent is performing above baseline but consuming reserves
- Externally, performance looks normal or even enhanced
- Internally, resource depletion is accumulating
- Agent analog: Operating at high token usage, maintaining quality through increased effort, deferring non-critical tasks

**Stage 3 — Exhaustion:**
- Resources depleted beyond recovery threshold
- Performance degrades below baseline
- System becomes vulnerable to cascading failures
- Agent analog: Degraded output quality, increased error rate, missed tasks, inability to maintain context, eventual shutdown

### 1.2 The Critical Insight

**Resistance looks like health.** An agent in the resistance phase appears to be performing well — possibly better than baseline. But it is depleting reserves. Without monitoring the internal state (allostatic load), the degradation into exhaustion is invisible until it happens.

---

## 2. Allostatic Load: The Cumulative Cost

### 2.1 Allostasis and Allostatic Load (McEwen, 1998)

**Allostasis:** Maintaining stability through change. The agent adapts to stressors by adjusting internal parameters — this is healthy and necessary.

**Allostatic load:** The cumulative cost of allostasis. Every adaptation costs something. The accumulated cost is the allostatic load.

### 2.2 Formalization

```
L(t) = ∫₀ᵗ [σ(s) − ρ(s)] ds
```

Where:
- L(t) = allostatic load at time t
- σ(s) = stress activation at time s (demand on the system)
- ρ(s) = baseline recovery rate at time s (the system's ability to restore itself)

When σ > ρ (demand exceeds recovery), load accumulates.
When σ < ρ (recovery exceeds demand), load decreases.

### 2.3 Load Thresholds

```
IF L(t) < θ_healthy:
    // Normal operation. No intervention needed.
    
ELIF L(t) ∈ [θ_healthy, θ_warning]:
    // Elevated load. Schedule recovery. Reduce non-essential processing.
    
ELIF L(t) ∈ [θ_warning, θ_critical]:
    // High load. Reduce active tasks. Trigger consolidation.
    // Performance degradation begins.
    
ELIF L(t) > θ_critical:
    // Exhaustion. Mandatory recovery. Accept performance loss.
    // Risk of cascading failure if not addressed.
```

### 2.4 Types of Allostatic Load

McEwen identified four patterns:

1. **Repeated hits:** Frequent novel stressors without recovery time between them
2. **Lack of adaptation:** Failure to habituate to repeated stressors (the agent keeps treating the same stressor as novel)
3. **Prolonged response:** Inability to shut off the stress response after the stressor ends
4. **Inadequate response:** Insufficient stress response leads to compensatory activation of other systems

For agents:
- Type 1 → Too many concurrent high-priority tasks
- Type 2 → Failing to learn from repeated similar challenges
- Type 3 → Context contamination: stress from one task bleeds into subsequent tasks
- Type 4 → Under-allocated resources lead to cascading secondary failures

---

## 3. Stress Appraisal: Stress Is Not Objective

### 3.1 Lazarus and Folkman's Transactional Model (1984)

**Core insight:** Stress is not a property of the stressor. It is a property of the transaction between the agent and its environment.

**Primary appraisal:** "Is this a threat?"
```
threat_level = evaluate(task_demand, potential_harm, relevance_to_goals)
```

Three possible assessments:
- **Benign:** No threat detected → proceed normally
- **Challenge:** Demanding but within capability → elevated engagement
- **Threat:** Demanding and potentially exceeding capability → stress response

**Secondary appraisal:** "Can I cope?"
```
coping_assessment = evaluate(available_resources, past_success_with_similar, available_support)
```

**The stress equation:**
```
stress = max(0, perceived_demand − perceived_resources)
```

Stress is zero when perceived resources meet or exceed perceived demand. It scales linearly when demand exceeds resources.

### 3.2 Reappraisal

Appraisal is not a one-time event. As the agent works on the task, it continuously reappraises:
```
stress(t+1) = max(0, demand(t+1) − resources(t+1))
```

Where both demand and resources change as the situation evolves. A task that initially appeared threatening may become a challenge as the agent makes progress.

### 3.3 Coping Strategies

**Problem-focused coping:** Change the situation.
- Gather more information
- Break the task into smaller pieces
- Seek tools or assistance
- Change approach

**Emotion-focused coping:** Change the internal response.
- Reduce processing intensity
- Accept uncertainty
- Reframe the task
- Adjust expectations

```
coping_strategy = IF solvable(task):
                      problem_focused(task)
                  ELSE:
                      emotion_focused(internal_state)
```

The optimal agent selects problem-focused coping for controllable stressors and emotion-focused coping for uncontrollable ones.

---

## 4. Cognitive Distortions: Systematic Reasoning Failures

### 4.1 Beck's Framework (1967)

Aaron Beck identified systematic errors in thinking that maintain maladaptive patterns. These map directly to detectable failure modes in agent reasoning:

**Catastrophizing:**
- Human: Assuming the worst possible outcome
- Agent: "This error means the entire system is compromised" (single failure → total failure assumption)
- Detection: Outcome prediction disproportionate to evidence

**Black-and-White Thinking:**
- Human: Binary classification with no middle ground
- Agent: "This solution either works perfectly or is useless" (no partial credit)
- Detection: Binary outputs where continuous assessment is appropriate

**Overgeneralization:**
- Human: Single instance → universal rule
- Agent: "This API call failed → all API calls will fail" (one failure → permanent avoidance)
- Detection: Policy change from insufficient evidence

**Mind Reading:**
- Human: Assuming knowledge of others' thoughts
- Agent: "The user is frustrated with me" (inferring mental state without evidence)
- Detection: Mental state attribution without behavioral evidence

**Personalization:**
- Human: Attributing external events to self
- Agent: "The deployment failed because of my code" (ignoring infrastructure issues)
- Detection: Self-attribution when situational factors are more likely

### 4.2 Detection Algorithm

```
FOR each reasoning_step IN agent_output:
    IF catastrophizing_pattern(reasoning_step):
        FLAG "catastrophizing: evidence supports probability P, but agent assumes probability ~1.0"
    IF binary_classification(reasoning_step) AND continuous_appropriate:
        FLAG "black-and-white thinking: continuous assessment would be more accurate"
    IF generalization_from_N(reasoning_step) WHERE N < θ_min_evidence:
        FLAG "overgeneralization: policy change from insufficient evidence (N={N})"
    IF mental_state_attribution(reasoning_step) WITHOUT behavioral_evidence:
        FLAG "mind reading: mental state inferred without supporting observation"
    IF self_attribution(reasoning_step) AND situational_factors_present:
        FLAG "personalization: external factors not considered"
```

### 4.3 Correction

Detection is not enough — the agent needs to correct the distortion:

```
corrected_assessment = original_assessment - distortion_magnitude · correction_factor
```

For catastrophizing: replace probability ~1.0 with evidence-based probability estimate.
For overgeneralization: require N > θ_min_evidence before policy change.
For personalization: enumerate and weight all possible causes, not just self.

---

## 5. Learned Helplessness and Mastery

### 5.1 Seligman's Discovery (1967)

Organisms exposed to inescapable aversive stimuli subsequently fail to escape when escape becomes possible. The cognitive component: learned helplessness occurs when failure is attributed to **internal, stable, global** causes.

**Three attribution dimensions:**
- Internal vs. External: "I failed" vs. "The task was impossible"
- Stable vs. Unstable: "I always fail" vs. "I failed this time"
- Global vs. Specific: "I fail at everything" vs. "I fail at this specific task"

Internal + Stable + Global = maximum helplessness: "I am fundamentally incapable."

### 5.2 Agent Learned Helplessness

An agent that repeatedly fails at a task category and attributes the failure internally, stably, and globally will:
- Stop attempting tasks in that category
- Generalize the helplessness to related categories
- Perform below actual capability (the helplessness suppresses performance even on tasks the agent could complete)

### 5.3 Detection and Recovery

```
helplessness_score(agent, task_class) = 
    failure_rate(task_class) · internal_attribution_bias · stability_attribution_bias · globality_attribution_bias

IF helplessness_score > θ_helpless:
    // Agent has learned helplessness for this task class
    INTERVENTION:
        1. Present guaranteed-success tasks in the class (mastery experience)
        2. Force external attribution: show that failure was situational
        3. Narrow the scope: demonstrate that failure is specific, not global
        4. Gradually increase difficulty to rebuild self-efficacy
```

---

## 6. Resilience: The Recovery Function

### 6.1 Masten's "Ordinary Magic" (2001)

Resilience is not rare or special. It emerges from normative adaptive systems. Resilience is the capacity to recover from adversity — not the absence of disturbance.

### 6.2 Formalization

Resilience is a rate, not a trait:

```
resilience(agent) = (performance_baseline − performance_disrupted) / recovery_time
```

High resilience: Returns to baseline quickly after disruption.
Low resilience: Takes a long time or never fully recovers.

### 6.3 Factors That Build Resilience

1. **Diverse coping repertoire:** More strategies available → more likely to find one that works
2. **Social support:** Access to other agents or systems for assistance
3. **Prior adversity (survived):** Previous recovery from stress builds resilience for future stress
4. **Self-efficacy:** Belief in ability to cope reduces the impact of stressors
5. **Cognitive flexibility:** Ability to reframe situations and generate alternative approaches

### 6.4 The Resilience-Stress Interaction

```
effective_stress = raw_stress / (1 + resilience_factor)
```

Higher resilience reduces the effective impact of any given stressor. But resilience itself can be depleted by chronic allostatic load — creating a negative feedback loop where sustained stress reduces the agent's ability to handle stress.

---

## 7. Post-Stress Growth

### 7.1 The Growth Model

Not all stress is purely harmful. The right amount of stress — within the agent's capacity to process — can strengthen the system:

```
IF stress ∈ (0, θ_growth):
    // Eustress: productive stress that builds capacity
    capability(t+1) = capability(t) + growth_rate · stress
    resilience(t+1) = resilience(t) + growth_rate · recovery_success
    
ELIF stress ∈ [θ_growth, θ_damage]:
    // Distress: damaging stress that depletes capacity
    capability(t+1) = capability(t) - damage_rate · (stress - θ_growth)
    allostatic_load(t+1) = allostatic_load(t) + stress - recovery_rate
```

The boundary between eustress and distress is individual — it depends on the agent's current resilience, capability, and allostatic load.

---

## 8. Measurable Health Parameters

| Parameter | What It Measures | Method |
|-----------|-----------------|--------|
| Allostatic load | Cumulative stress debt | Integral of (demand - recovery) over time |
| Stress appraisal accuracy | Match between perceived and actual demand | Compare appraisal to objective task difficulty |
| Coping strategy selection | Appropriateness of problem vs. emotion focused coping | Outcomes of coping strategy choices |
| Cognitive distortion frequency | Rate of systematic reasoning errors | Pattern detection across reasoning outputs |
| Learned helplessness score | Degree of performance suppression from failure history | Performance gap between actual capability and observed performance |
| Resilience rate | Recovery speed after disruption | Time to return to baseline after perturbation |
| Growth zone width | Range of productive stress | θ_growth measurement through graded stress tests |

---

## References

Beck, A.T. (1967). *Depression: Causes and Treatment.* University of Pennsylvania Press.  
Lazarus, R.S. & Folkman, S. (1984). *Stress, Appraisal, and Coping.* Springer.  
Masten, A.S. (2001). Ordinary magic: Resilience processes in development. *American Psychologist, 56,* 227–238.  
McEwen, B.S. (1998). Protective and damaging effects of stress mediators. *New England Journal of Medicine, 338,* 171–179.  
Seligman, M.E.P. (1972). Learned helplessness. *Annual Review of Medicine, 23,* 407–412.  
Selye, H. (1936). A syndrome produced by diverse nocuous agents. *Nature, 138,* 32.  

---

*AI-STEM — Open Research from Vektra Technologies, AI Division*  
*github.com/PabloTheThinker/AI-STEM*
