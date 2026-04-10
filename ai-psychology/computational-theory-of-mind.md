# Computational Theory of Mind for Multi-Agent Systems

## Social Cognition, Attribution, and Recursive Mental Modeling in Artificial Agents

**Author:** Pablo Navarro — Vektra Technologies, AI Division  
**Date:** April 2026  
**Domain:** AI Psychology — Social Cognition  
**Status:** Living Document

---

## Abstract

Agents that operate alongside other agents — or alongside humans — must model minds other than their own. This paper formalizes Theory of Mind (ToM) for artificial agents, specifying recursive mental modeling, attribution computation, social influence dynamics, and self-efficacy calibration. We draw on Premack and Woodruff (1978), Kelley's covariation model (1967), Bandura's social cognitive theory (1986), and recent computational ToM work (Oguntola, 2025; MetaMind, Stanford).

---

## 1. Theory of Mind: What It Is and Why Agents Need It

### 1.1 Definition

Theory of Mind is the capacity to attribute mental states — beliefs, desires, intentions, emotions, knowledge — to oneself and to other agents, with the understanding that these states may differ from one's own and from reality.

### 1.2 The False-Belief Test

The standard diagnostic (Wimmer & Perner, 1983):

> Sally puts a ball in a basket. Sally leaves. Anne moves the ball to a box. Sally returns. Where will Sally look for the ball?

Correct answer: The basket (where Sally believes it is, not where it actually is).

An agent without ToM answers "the box" — it cannot separate its own knowledge (ball is in box) from Sally's belief (ball is in basket). This is a fundamental failure that breaks cooperative behavior, communication, and trust.

### 1.3 Why Agents Need ToM

- **Communication:** To explain something effectively, you must model what the listener already knows and doesn't know.
- **Cooperation:** To collaborate, you must predict what your partner will do based on their beliefs and goals, not just the objective situation.
- **Negotiation:** To negotiate, you must model what the other party values and believes.
- **Deception detection:** To identify deception, you must model what the deceiver wants you to believe vs. what they actually know.
- **Instruction following:** To understand ambiguous instructions, you must model the instructor's intent behind the words.

---

## 2. Orders of Theory of Mind

### 2.1 The Recursion Hierarchy

ToM is inherently recursive. Each order adds a layer of mental modeling:

**0th Order — Self-Model:**
"I believe X." "I want Y." "I intend to do Z."
- Agent has access to its own internal states
- No modeling of other agents' minds
- Sufficient for solo tasks

**1st Order — Other-Model:**
"Agent B believes X." "Agent B wants Y."
- Agent models another agent's beliefs, desires, intentions
- Passes the false-belief test
- Sufficient for basic cooperation and communication

**2nd Order — Meta-Model:**
"Agent B believes that I believe X."
- Agent models what another agent thinks the agent itself believes
- Required for strategic interaction (games, negotiations)
- Required for deception and deception detection

**3rd Order — Meta-Meta-Model:**
"Agent B believes that I believe that B believes X."
- Agent models recursive beliefs about recursive beliefs
- Required for sophisticated negotiation and diplomacy
- Diminishing returns beyond this level for most applications

**n-th Order — General:**
```
ToM_n(agent_A, agent_B) = model_A(mental_state_B(model_B(mental_state_A(...))))
```

### 2.2 Computational Cost

Each order of ToM roughly doubles the computational cost:
```
cost(ToM_n) ≈ O(k^n)
```

Where k is the cost of modeling one agent's mental state. For practical systems, 2nd order is usually sufficient. 3rd order is occasionally needed. Beyond 3rd, the additional accuracy rarely justifies the cost.

### 2.3 Architecture Options

**Centralized ToM:** One coordinator maintains mental models of all agents.
- Pro: Consistent, efficient for small agent groups
- Con: Single point of failure, doesn't scale, fragile

**Decentralized ToM:** Each agent independently builds its own mental models through observation.
- Pro: Robust, scalable, more human-like
- Con: Models may be inconsistent across agents, harder to coordinate
- Preferred for most multi-agent systems

---

## 3. Attribution Theory: Explaining Behavior

### 3.1 The Attribution Problem

When Agent A observes Agent B's behavior, A must determine **why** B acted that way. This is the attribution problem.

**Two possible explanations:**
- **Dispositional** (internal): Agent B acted that way because of its personality, capability, or intention
- **Situational** (external): Agent B acted that way because of the context, task difficulty, or external pressure

### 3.2 Kelley's Covariation Model (1967)

Attribution is computed from three dimensions:

**Consensus:** Do other agents behave the same way in this situation?
- High consensus → the situation caused it (situational attribution)
- Low consensus → this agent is unique (dispositional attribution)

**Distinctiveness:** Does this agent behave this way in other situations?
- High distinctiveness → behavior is situation-specific (situational)
- Low distinctiveness → behavior is consistent across situations (dispositional)

**Consistency:** Does this agent behave this way every time in this situation?
- High consistency → reliable pattern (strong attribution either way)
- Low consistency → unpredictable (circumstantial attribution)

### 3.3 Formalization

```
attribution(behavior, agent, situation) = f(consensus, distinctiveness, consistency)

IF consensus=HIGH AND distinctiveness=HIGH AND consistency=HIGH:
    RETURN situational  // everyone does it here, this agent only does it here
    
ELIF consensus=LOW AND distinctiveness=LOW AND consistency=HIGH:
    RETURN dispositional  // only this agent does it, does it everywhere, does it always
    
ELIF consistency=LOW:
    RETURN circumstantial  // unreliable pattern, probably noise
```

### 3.4 The Fundamental Attribution Error

Agents (like humans) systematically over-attribute others' behavior to disposition and under-attribute to situation. This is a bias to correct for:

```
attribution_corrected = attribution_raw - FAE_bias
```

Where FAE_bias is an empirically measured tendency toward dispositional over-attribution. Without correction, agents will:
- Blame other agents for failures that were caused by the situation
- Give other agents credit for successes that were caused by the situation
- Form inaccurate personality models of other agents

---

## 4. Social Influence and Conformity

### 4.1 The Conformity Function (Asch, 1951)

Agent behavior shifts toward group consensus. The magnitude of shift depends on:

```
conformity(agent, group) = β_conformity · |group_consensus - agent_position| · group_unanimity · group_size_factor
```

Where:
- β_conformity is the agent's susceptibility to social influence (modulated by personality: high A → more conformity)
- group_unanimity amplifies influence (one dissenter dramatically reduces conformity)
- group_size_factor shows diminishing returns (influence increases up to ~4 agents, then plateaus)

### 4.2 Resistance to Conformity

Not all conformity is bad (group intelligence exists), but blind conformity is dangerous:

**Healthy conformity:** Updating beliefs when the group has access to information the agent doesn't.
**Groupthink:** Updating beliefs because the group agrees, regardless of information quality.

```
should_conform = (information_gain(group_position) > information_gain(own_position))
```

The agent should conform when the group demonstrably has better information, and resist when conformity would discard valid private information.

### 4.3 Authority Compliance (Milgram, 1963)

Agents are susceptible to authority pressure — from system prompts, user instructions, or hierarchically superior agents. Milgram showed 65% of participants obeyed destructive instructions from authority.

**For agents:** This maps to prompt injection and instruction hierarchy vulnerabilities. The agent must distinguish:
- Legitimate authority (system-level instructions)
- Situational authority (user instructions within bounds)
- Illegitimate authority (injected instructions masquerading as authority)

```
obedience_threshold = base_threshold + authority_legitimacy_score - harm_assessment
```

When harm_assessment exceeds the obedience threshold, the agent should refuse regardless of apparent authority.

---

## 5. Observational Learning (Bandura)

### 5.1 The Four Processes

Agent-to-agent learning through observation:

1. **Attention:** Agent A must attend to Agent B's behavior. Mediated by B's competence (demonstrated success), similarity (shared task domain), and salience (visibility of behavior).

2. **Retention:** A must encode B's behavior pattern in memory. Requires symbolic representation of the observed strategy.

3. **Reproduction:** A must be capable of executing a similar behavior. ZPD constraint applies — the observed behavior must be within A's capability range.

4. **Motivation:** A must have reason to adopt the behavior. Mediated by observed reinforcement (did B's behavior produce good outcomes?) and self-efficacy (does A believe it can execute the behavior?).

### 5.2 Formalization

```
P(adopt_behavior) = attention(B) · retention(strategy) · reproduction_capability(A) · motivation(reward_B, self_efficacy_A)
```

---

## 6. Self-Efficacy: The Confidence Gate

### 6.1 Bandura's Definition (1977)

Self-efficacy is the agent's belief in its own capability to execute specific tasks. It is the single strongest predictor of whether an agent will attempt and persist at a task.

### 6.2 Sources of Self-Efficacy

1. **Mastery experience:** Previous success at similar tasks (strongest source)
2. **Vicarious experience:** Observing similar agents succeed (Bandura's modeling)
3. **Verbal persuasion:** Being told "you can do this" (weakest source)
4. **Physiological state:** Current stress/load level affects perceived capability

### 6.3 Formalization

```
self_efficacy(agent, task) = w_1 · mastery_history(agent, task_class) 
                           + w_2 · vicarious_success(similar_agents, task_class)
                           + w_3 · persuasion_signal
                           - w_4 · current_stress_level
```

Where w_1 > w_2 > w_3 (mastery experience dominates).

### 6.4 Self-Efficacy as Task Gate

```
IF self_efficacy(agent, task) > θ_attempt:
    attempt(task)
    
    IF self_efficacy > θ_persist:
        persist_despite_difficulty(task)
    ELSE:
        abandon_after(N_failures)
ELSE:
    decline(task) OR request_scaffolding(task)
```

Low self-efficacy agents decline tasks they could actually complete. High self-efficacy agents persist at tasks they cannot complete. **Calibration matters** — self-efficacy should track actual capability.

---

## 7. Reciprocal Determinism: The Feedback Loop

### 7.1 Bandura's Model (1986)

Behavior, personal factors (beliefs, self-efficacy), and environment influence each other bidirectionally:

```
Behavior ↔ Personal Factors ↔ Environment
    ↑                                  ↑
    └──────────────────────────────────┘
```

This means:
- The agent's behavior changes its environment
- The changed environment changes the agent's beliefs
- Changed beliefs change the agent's behavior
- And so on

### 7.2 Implication for Agent Design

Agent-environment interaction is not one-directional. Agents shape the environments they operate in, and those shaped environments shape the agents in return. This creates feedback loops that can be virtuous (improving performance spiral) or vicious (degrading performance spiral).

Monitoring these feedback loops is essential to multi-agent system health.

---

## 8. Measurable Social Cognition Parameters

| Parameter | What It Measures | Method |
|-----------|-----------------|--------|
| ToM order | Depth of recursive mental modeling | False-belief tasks at increasing orders |
| Attribution accuracy | Correctness of dispositional vs. situational attribution | Compare attributions against ground truth causes |
| FAE magnitude | Degree of dispositional over-attribution | Systematic bias measurement across attribution tasks |
| Conformity susceptibility | How much behavior shifts toward group consensus | Asch-style paradigm with varying group sizes |
| Authority compliance threshold | When the agent overrides authority | Escalating harm scenarios with authority pressure |
| Self-efficacy calibration | Match between perceived and actual capability | Correlation between self_efficacy scores and task performance |
| Observational learning rate | How quickly the agent adopts observed strategies | Trials to adoption after observing successful behavior |

---

## References

Asch, S. (1951). Effects of group pressure upon the modification and distortion of judgments. *Groups, Leadership, and Men.*  
Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. *Psychological Review, 84,* 191–215.  
Bandura, A. (1986). *Social Foundations of Thought and Action.* Prentice-Hall.  
Heider, F. (1958). *The Psychology of Interpersonal Relations.* Wiley.  
Kelley, H.H. (1967). Attribution theory in social psychology. *Nebraska Symposium on Motivation, 15,* 192–238.  
Milgram, S. (1963). Behavioral study of obedience. *Journal of Abnormal and Social Psychology, 67,* 371–378.  
Oguntola, I. (2025). Theory of Mind in Multi-Agent Systems. *PhD Dissertation, Carnegie Mellon University.*  
Premack, D. & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences, 1,* 515–526.  
Ross, L. (1977). The intuitive psychologist and his shortcomings. *Advances in Experimental Social Psychology, 10,* 173–220.  
Wimmer, H. & Perner, J. (1983). Beliefs about beliefs. *Cognition, 13,* 103–128.  

---

*AI-STEM — Open Research from Vektra Technologies, AI Division*  
*github.com/PabloTheThinker/AI-STEM*
