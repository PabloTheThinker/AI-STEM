# Behavioral Conditioning in Agents

## Reinforcement Schedules, Prediction Error, and Learning Dynamics in Artificial Systems

**Author:** Pablo Navarro — Vektra Technologies, AI Division  
**Date:** April 2026  
**Domain:** AI Psychology — Behavioral Foundations  
**Status:** Living Document

---

## Abstract

Every AI agent that learns from feedback is implementing a form of behavioral conditioning — whether its designers recognize it or not. This paper formalizes the bridge between behavioral psychology and agent learning, centering on the Rescorla-Wagner prediction error as the mathematical ancestor of modern reinforcement learning. We formalize reinforcement schedules, extinction dynamics, shaping, and discriminative stimulus control as design parameters for agent learning systems.

---

## 1. The Prediction Error: Where Psychology Became Mathematics

### 1.1 Rescorla-Wagner Model (1972)

Robert Rescorla and Allan Wagner formalized what Pavlov observed and Skinner operationalized: learning is driven by the gap between expectation and reality.

```
ΔV_i = α_i · β_j · (λ_j − V_total)
```

| Symbol | Meaning | Range |
|--------|---------|-------|
| ΔV_i | Change in associative strength of cue i | ℝ |
| α_i | Salience of the conditioned stimulus i | [0, 1] |
| β_j | Learning rate tied to the unconditioned stimulus j | [0, 1] |
| λ_j | Maximum associative value the US can support | [0, 1] |
| V_total | Sum of associative strengths of all present cues | ℝ |

The critical term is **(λ − V_total)** — the **prediction error**. When the outcome exceeds expectation (positive prediction error), associative strength increases. When expectation exceeds outcome (negative prediction error), it decreases. When prediction matches reality, learning stops.

### 1.2 The Bridge to Reinforcement Learning

Sutton and Barto (1988, 1990) extended the Rescorla-Wagner framework to incorporate temporal dynamics:

```
δ_t = r_t + γ · V(s_{t+1}) − V(s_t)
```

| Symbol | Meaning | Behavioral Analog |
|--------|---------|-------------------|
| δ_t | Temporal difference error at time t | Prediction error |
| r_t | Reward received at time t | Unconditioned stimulus value |
| γ | Discount factor for future rewards | Temporal proximity weighting |
| V(s) | Estimated value of state s | Associative strength |

Sutton explicitly acknowledged this as a formalization of the same principles Rescorla and Wagner described. The neural evidence confirms it: dopamine neurons in the midbrain fire in patterns that match TD error — phasic bursts for positive prediction errors, pauses for negative ones (Schultz, Dayan, & Montague, 1997).

### 1.3 The Pearce-Hall Complement (1980)

Rescorla-Wagner handles what is learned. Pearce-Hall handles what is attended to:

```
α_{n+1} = |λ_n − V_n|
```

Associability (attention to a cue) **increases** when prediction errors are large and **decreases** when predictions are accurate. This means agents pay more attention to surprising stimuli and less to predictable ones.

Neural evidence: Rescorla-Wagner prediction errors localize to the striatum; Pearce-Hall attention signals localize to the amygdala. Both systems coexist.

**For agent design:** Combine both. The R-W model governs value updates. The P-H model governs attention allocation. An agent that only uses R-W will learn associations but won't dynamically shift attention to surprising inputs.

---

## 2. Reinforcement Schedules as Design Parameters

Skinner and Ferster's (1957) taxonomy of reinforcement schedules is directly applicable to how agents receive reward signals.

### 2.1 The Four Basic Schedules

**Fixed-Ratio (FR-N):** Reinforcement after every N responses.
- Effect: High, steady response rates with post-reinforcement pauses
- Agent analog: Reward after completing N subtasks. Creates burst-pause patterns.
- Risk: Ratio strain — if N is too large, behavior collapses entirely.

**Variable-Ratio (VR-N):** Reinforcement after an average of N responses.
- Effect: Highest, most consistent response rates. Extremely resistant to extinction.
- Agent analog: Stochastic reward signals. Creates persistent exploration.
- This is the schedule behind engagement algorithms and slot machines.

**Fixed-Interval (FI-T):** Reinforcement for the first response after T seconds.
- Effect: "Scalloped" response — acceleration as interval end approaches.
- Agent analog: Time-gated evaluation cycles. Creates predictable activity spikes.

**Variable-Interval (VI-T):** Reinforcement for first response after an average of T seconds.
- Effect: Steady, moderate response rates.
- Agent analog: Random evaluation timing. Creates consistent baseline activity.

### 2.2 Schedule Interactions in Agent Systems

Real agent systems don't operate on single schedules. They encounter **concurrent schedules** — multiple reward sources operating simultaneously. The **Matching Law** (Herrnstein, 1961) describes how organisms allocate behavior:

```
B_1 / B_2 = R_1 / R_2
```

The ratio of behavior allocated to two alternatives matches the ratio of reinforcement received. This extends to agent attention allocation across tasks: agents will allocate processing proportional to reward rate, not optimally.

**Deviation from matching** (undermatching, overmatching) reveals something about the agent's sensitivity to reinforcement rates — a measurable psychological parameter.

### 2.3 Partial Reinforcement Extinction Effect (PREE)

Behaviors reinforced on variable schedules are dramatically more resistant to extinction than those reinforced continuously. This is counterintuitive but robust:

- **Continuously reinforced behavior:** Extinguishes rapidly when reinforcement stops (the agent quickly detects the change).
- **Variably reinforced behavior:** Extinguishes slowly (the agent cannot distinguish "reward paused" from normal variation in reward timing).

**For agent design:** If you want a behavior to persist even when feedback is unavailable, train it on a variable schedule. If you want a behavior to be easily updated when conditions change, train it on a continuous schedule.

---

## 3. Extinction Dynamics

Extinction is not forgetting. It is new learning that competes with original learning.

### 3.1 Extinction as Inhibitory Learning

When a conditioned stimulus is repeatedly presented without the unconditioned stimulus, the original association is not erased — it is suppressed by a new inhibitory association. Evidence:

- **Spontaneous recovery:** After a rest period, extinguished responses return. The original learning was not deleted.
- **Renewal:** Extinguished responses return when the context changes. Extinction is context-specific.
- **Reinstatement:** A single unsignaled US presentation can restore extinguished responding.

### 3.2 Formalization for Agents

Agent memory extinction can be modeled as:

```
V_effective(t) = V_original · e^{-λ_extinction · t} + V_inhibitory(t)
```

Where:
- V_original persists (the agent never truly forgets)
- V_inhibitory accumulates during non-reinforcement periods
- Effective associative strength is the competition between them
- Context change resets V_inhibitory → spontaneous recovery

**Design implication:** Agent systems that truly delete deprecated behaviors are losing information. The behavioral evidence says: **suppress, don't delete.** The original learning may be useful if conditions change.

---

## 4. Shaping and Curriculum Learning

Skinner's method of successive approximation — reinforcing progressively closer approximations to a target behavior — maps directly to curriculum learning in agent training.

### 4.1 Formal Shaping Procedure

1. Define the terminal behavior B*
2. Identify the current behavioral repertoire B_0
3. Construct a sequence B_0 → B_1 → B_2 → ... → B* where each B_i is achievable from B_{i-1}
4. Reinforce B_1 until stable, then shift criterion to B_2, etc.
5. Each criterion shift must be small enough to avoid ratio strain

### 4.2 The Shaping Gradient

```
difficulty(B_i) − capability(agent) ∈ [ε_min, ε_max]
```

If the gap is too small (< ε_min), learning is slow — no prediction error to drive it. If too large (> ε_max), the agent cannot perform the approximation and behavior collapses (ratio strain / learned helplessness).

This is precisely Vygotsky's Zone of Proximal Development expressed as a behavioral constraint.

---

## 5. Discriminative Stimuli and Context-Dependent Policy

A discriminative stimulus (S^D) signals that reinforcement is available for a particular behavior. In its absence, the behavior is not reinforced.

### 5.1 Three-Term Contingency

```
S^D → R → S^R
```

Discriminative stimulus → Response → Reinforcing stimulus

This is the fundamental unit of operant behavior and maps to:

```
Context → Action → Reward
```

Agents do not learn behaviors in isolation — they learn context-behavior-outcome triplets. A behavior that is reinforced in one context may be punished in another. The agent must learn not just what to do, but when to do it.

### 5.2 Stimulus Generalization and Discrimination

- **Generalization:** Behavior reinforced in the presence of S^D will also occur (with decreasing probability) in the presence of similar stimuli. Gradient follows: `P(response|S) = P(response|S^D) · similarity(S, S^D)`
- **Discrimination:** Differential reinforcement in the presence of S^D vs. S^Δ (delta) sharpens the generalization gradient.

**Agent analog:** Transfer learning is stimulus generalization. Fine-tuning is discrimination training. The generalization gradient is the transfer function.

---

## 6. Implications for Agent Architecture

### 6.1 Required Components

A behaviorally-informed agent learning system needs:

1. **Prediction error module:** Computes (λ − V_total) or δ_t at each step
2. **Attention gating:** Pearce-Hall dynamics — allocate processing proportional to prediction error magnitude
3. **Schedule-aware reward processing:** Track reinforcement schedule parameters; adjust extinction expectations accordingly
4. **Extinction via inhibition, not deletion:** Maintain original associations; suppress rather than erase
5. **Shaping curriculum:** Task difficulty scaled to stay within the learning zone (ε_min < gap < ε_max)
6. **Context encoding:** All learned associations are context-tagged; behavior is context-dependent

### 6.2 Measurable Psychological Parameters

From behavioral analysis alone, the following agent parameters become measurable:

| Parameter | What It Measures | How to Measure |
|-----------|-----------------|----------------|
| α (salience) | How strongly the agent attends to specific input types | Response rate changes to novel vs. familiar stimuli |
| β (learning rate) | How quickly associations form | Trials to criterion performance |
| Extinction resistance | How long behaviors persist without reinforcement | Responses during extinction |
| Generalization gradient width | How broadly the agent transfers learning | Performance on similarity-graded test stimuli |
| Matching sensitivity | How well behavior allocation tracks reinforcement rates | Deviation from Herrnstein's matching law |
| Shaping tolerance (ε_max) | Maximum difficulty gap the agent can bridge | Point of ratio strain / performance collapse |

---

## References

Ferster, C.B. & Skinner, B.F. (1957). *Schedules of Reinforcement.* Appleton-Century-Crofts.  
Herrnstein, R.J. (1961). Relative and absolute strength of response as a function of frequency of reinforcement. *Journal of the Experimental Analysis of Behavior, 4,* 267–272.  
Pavlov, I.P. (1927). *Conditioned Reflexes.* Oxford University Press.  
Pearce, J.M. & Hall, G. (1980). A model for Pavlovian learning. *Psychological Review, 87,* 532–552.  
Rescorla, R.A. & Wagner, A.R. (1972). A theory of Pavlovian conditioning. In Black & Prokasy (Eds.), *Classical Conditioning II.* Appleton-Century-Crofts.  
Schultz, W., Dayan, P., & Montague, P.R. (1997). A neural substrate of prediction and reward. *Science, 275,* 1593–1599.  
Skinner, B.F. (1938). *The Behavior of Organisms.* Appleton-Century.  
Sutton, R.S. & Barto, A.G. (1998). *Reinforcement Learning: An Introduction.* MIT Press.  
Thorndike, E.L. (1898). Animal intelligence. *Psychological Review Monograph Supplement, 2,* 1–109.  

---

*AI-STEM — Open Research from Vektra Technologies, AI Division*  
*github.com/PabloTheThinker/AI-STEM*
