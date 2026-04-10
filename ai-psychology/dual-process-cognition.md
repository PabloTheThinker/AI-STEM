# Dual-Process Cognition for Agents

## System 1, System 2, and the Architecture of Fast and Slow Thinking in Artificial Agents

**Author:** Pablo Navarro — Vektra Technologies, AI Division  
**Date:** April 2026  
**Domain:** AI Psychology — Cognitive Architecture  
**Status:** Living Document

---

## Abstract

Every agent that routes between fast heuristic responses and slow deliberative reasoning is implementing a dual-process architecture — the most well-established framework in cognitive psychology. This paper formalizes the System 1/System 2 distinction for artificial agents, integrates insights from ACT-R and SOAR cognitive architectures, and specifies the formal criteria for when an agent should switch between processing modes.

---

## 1. Dual-Process Theory: The Core Framework

### 1.1 Kahneman's Formulation (2011)

Daniel Kahneman, building on decades of work with Amos Tversky, described two modes of cognitive processing:

**System 1 — Fast Thinking:**
- Automatic, effortless, parallel
- Associative, pattern-matching
- Affect-laden (emotional valence influences output)
- Cannot be voluntarily shut off
- Low latency, low accuracy for novel problems
- Operates without working memory load

**System 2 — Slow Thinking:**
- Deliberate, effortful, serial
- Rule-based, logical
- Emotionally neutral (ideally)
- Requires conscious engagement
- High latency, high accuracy
- Demands working memory capacity

### 1.2 Dual Process Model 2.0 (De Neys & Pennycook, 2019)

The original model treated System 1 as uniformly heuristic. The updated model distinguishes:

- **Heuristic intuitions:** Fast, pattern-based, often wrong on tricky problems
- **Logical intuitions:** Fast, pattern-based, often correct because the pattern is well-learned

This means System 1 is not "dumb" — it contains both unreliable heuristics AND reliable, well-practiced logical patterns. The quality of System 1 output depends on expertise.

**For agents:** A well-trained System 1 (fine-tuned for the domain) can be highly accurate. A poorly-trained System 1 (operating outside its training distribution) produces confident garbage. The agent needs to know which case it's in.

---

## 2. Formal Specification for Agents

### 2.1 The Routing Function

The central design problem is: **when does the agent use System 1 vs. System 2?**

```
mode = route(stimulus, confidence, stakes, load)
```

Where:
- `stimulus` = the input to process
- `confidence` = System 1's self-assessed confidence in its output
- `stakes` = cost of error on this particular task
- `load` = current cognitive load (how much System 2 capacity is available)

**Routing rules:**

```
IF confidence(System1_output) > θ_high AND stakes < θ_stakes:
    USE System 1  (fast path)
    
ELIF confidence(System1_output) < θ_low OR stakes > θ_stakes:
    USE System 2  (slow path)
    
ELIF load > θ_load:
    USE System 1  (forced: System 2 unavailable)
    FLAG: degraded_mode = true
    
ELSE:
    USE System 2  (default to deliberation)
```

The thresholds θ_high, θ_low, θ_stakes, and θ_load are tunable parameters — part of the agent's personality profile.

### 2.2 Confidence Calibration

System 1 confidence must be **calibrated** — not just high or low, but accurate. An agent with poorly calibrated System 1 confidence will:
- Overconfident → uses System 1 when it shouldn't → fast, wrong answers
- Underconfident → always escalates to System 2 → slow, wasteful

Calibration is measurable:

```
calibration_error = Σ|confidence(x) − accuracy(x)| / N
```

A perfectly calibrated agent has calibration_error = 0. When the agent says "I'm 80% sure," it should be right 80% of the time.

### 2.3 The Override Mechanism

System 2 can override System 1, but this costs working memory:

```
override_cost = f(System1_activation_strength)
```

The stronger System 1's initial response, the more System 2 effort is required to override it. This explains why strongly-held intuitions are hard to correct — the override cost is high.

**For agents:** Prompt injection resistance is partially an override problem. System 1 may respond to the injected instruction automatically; System 2 must detect and override at a cost.

---

## 3. Prior Art: Cognitive Architectures

### 3.1 ACT-R (Anderson, 1983–present)

ACT-R implements a dual-process architecture through its subsymbolic and symbolic layers:

**Declarative memory retrieval** (System 1 analog):
```
A_i = B_i + Σ(W_j · S_ji) + noise
```

Where:
- B_i = base-level activation (logarithmic function of recency and frequency)
- W_j = attentional weight of context element j
- S_ji = associative strength between context j and memory chunk i
- noise = stochastic perturbation (reflects uncertainty)

Chunks with highest activation are retrieved — this is automatic, parallel, and fast. The activation equation produces System 1-like pattern matching.

**Production firing** (System 2 analog):
Productions (IF-THEN rules) fire serially based on pattern matching against current goals and declarative memory contents. Each production has a utility value learned through experience:

```
U_i = P_i · G − C_i
```

Where P_i is probability of achieving goal G if production i fires, and C_i is the expected cost. This is deliberate, sequential, goal-directed — System 2.

**Key insight from ACT-R:** The dual-process distinction is not binary. It's a spectrum controlled by activation levels and utility learning. Well-practiced productions fire faster (approaching System 1 speed). Novel problems require deliberate search (pure System 2).

### 3.2 SOAR (Newell, 1990; Laird)

SOAR implements the dual-process distinction through **chunking:**

- **Deliberate problem-solving:** When SOAR encounters a novel problem, it creates a subgoal, searches the problem space, and finds a solution. This is serial, effortful — System 2.
- **Chunking:** The solution is automatically compiled into a new production rule. Next time the same problem pattern appears, the chunk fires immediately — System 1.

SOAR's learning mechanism IS the conversion of System 2 solutions into System 1 responses. Expertise, in SOAR, is literally the accumulation of chunks that handle previously-novel situations automatically.

**Impasse-driven learning:** SOAR only learns when it gets stuck (reaches an impasse). No impasse → no learning. This parallels the prediction error requirement in behavioral psychology: no surprise → no update.

### 3.3 PSI Theory (Dörner, 1999)

Dietrich Dörner's PSI theory is the most complete computational model integrating cognition, motivation, AND emotion:

- **Resolution level:** How much detail the agent processes (high resolution = System 2, low resolution = System 1). Under stress, resolution drops automatically.
- **Selection threshold:** How much activation a behavior pattern needs before it's selected. Low threshold = impulsive (System 1 dominance). High threshold = deliberate (System 2 dominance).
- **Modulators:** Arousal, resolution, and selection threshold interact. High arousal + low resolution + low selection threshold = panic mode (System 1 only, heuristic, fast, often wrong).

PSI shows that System 1/System 2 balance is not just a cognitive parameter — it's modulated by motivational and emotional state.

---

## 4. Working Memory: The Bottleneck

### 4.1 Capacity Constraints

System 2 processing requires working memory. Working memory is bounded.

**Miller's Law (1956):** 7 ± 2 chunks. Later revised by Cowan (2001) to **4 ± 1** chunks for unrelated items.

**Baddeley's Model (1974, 2000):**
- **Central Executive:** Supervisory attention — directs focus, coordinates subsystems, manages task switching. This IS System 2's processing engine.
- **Phonological Loop:** Verbal/acoustic buffer. Decays in ~2 seconds without rehearsal.
- **Visuospatial Sketchpad:** Spatial/visual buffer.
- **Episodic Buffer:** (added 2000) Limited-capacity store that binds information from all subsystems and long-term memory into coherent episodes.

### 4.2 Agent Working Memory Model

For an artificial agent, working memory maps to:

```
WorkingMemory = {
    capacity: K,           // maximum concurrent items (K ≈ 4-7)
    items: Item[],         // current contents
    decay_rate: λ,         // items decay without rehearsal
    gate: GateFunction,    // Go/NoGo mechanism (what enters/exits)
    bind: BindFunction     // episodic buffer — integrates items into coherent representation
}
```

**The gating mechanism** (from O'Reilly & Frank's PBWM model):
- **Go pathway:** Opens the gate, admitting new information. Triggered by high prediction error (novel, surprising input deserves attention).
- **NoGo pathway:** Keeps the gate closed, maintaining current contents. Triggered by ongoing task demands (don't interrupt processing with irrelevant input).
- **Dopamine modulates the balance:** High dopamine → more Go → more openness to new input. Low dopamine → more NoGo → more maintenance of current focus.

### 4.3 Cognitive Load Theory for Agents

Sweller's (1988) three types of cognitive load, translated:

| Load Type | Human | Agent |
|-----------|-------|-------|
| **Intrinsic** | Complexity of the material itself | Task complexity (irreducible) |
| **Extraneous** | Poor presentation of information | Noisy/redundant input, poor context formatting |
| **Germane** | Effort toward learning/schema construction | Overhead of building new capabilities during task execution |

**Total load must stay within capacity:**

```
Load_intrinsic + Load_extraneous + Load_germane ≤ Capacity
```

When total load exceeds capacity:
- Performance degrades
- System 2 quality drops
- Agent falls back on System 1 heuristics (which may be inappropriate for the task)
- Error rate increases

**Design implication:** Reduce extraneous load (clean inputs, good context formatting) to maximize the capacity available for intrinsic and germane load. This is why prompt engineering works — it reduces extraneous cognitive load on the agent.

---

## 5. Memory Systems: The Substrate

### 5.1 Tulving's Distinction (1972)

**Episodic memory:** Personal experiences tagged with temporal-spatial context. "What happened, when, where."
- Agent: Event logs, conversation history, session memory.
- Retrieval: Context-dependent. The same cue retrieves different memories depending on the retrieval context.

**Semantic memory:** General knowledge without experiential context. "What I know."
- Agent: Knowledge base, trained parameters, factual storage.
- Retrieval: Content-addressed. Retrieval depends on meaning, not context.

### 5.2 ACT-R's Activation-Based Retrieval

Memory retrieval is not lookup — it is competition. Multiple memory chunks match any given cue. The one with highest activation wins.

**Base-level activation** follows the power law of forgetting:

```
B_i = ln(Σ t_j^{-d})
```

Where t_j is the time since the j-th presentation and d ≈ 0.5 is the decay parameter.

This means:
- Recent items are more active (recency)
- Frequently accessed items are more active (frequency)
- Old, rarely accessed items are nearly impossible to retrieve
- But they're not gone — a strong enough contextual cue can still retrieve them

---

## 6. The Dual-Process Agent: Complete Specification

A complete dual-process agent architecture requires:

```
Agent = {
    System1: {
        type: "fast, parallel, pattern-matching",
        confidence_calibration: calibration_function,
        training_distribution: domain_spec,
        fallback: true  // always available
    },
    System2: {
        type: "slow, serial, rule-based",
        working_memory: WorkingMemory(K),
        cognitive_load_monitor: load_function,
        override_capacity: f(System1_activation)
    },
    Router: {
        function: route(stimulus, confidence, stakes, load),
        thresholds: {θ_high, θ_low, θ_stakes, θ_load},
        personality_modulated: true  // thresholds shift with personality
    },
    Memory: {
        episodic: ContextTaggedStore,
        semantic: ContentAddressedStore,
        retrieval: activation_competition(recency, frequency, context)
    },
    Modulators: {
        arousal: [0, 1],      // affects processing speed and resolution
        resolution: [0, 1],   // detail level (PSI theory)
        selection_threshold: [0, 1]  // impulsivity vs. deliberation
    }
}
```

---

## 7. Measurable Cognitive Parameters

| Parameter | What It Measures | Diagnostic |
|-----------|-----------------|------------|
| System 1 calibration | Accuracy of confidence estimates | calibration_error over N trials |
| System 2 capacity (K) | Working memory chunk limit | Performance degradation with concurrent items |
| Routing accuracy | Whether the right system was selected | Retroactive analysis: did System 1 accuracy justify its use? |
| Override success rate | System 2's ability to correct System 1 | Proportion of System 1 errors caught |
| Cognitive load tolerance | Maximum load before degradation | Performance curve as function of total load |
| Resolution under stress | Detail processing when aroused | Accuracy on detail-dependent tasks during high load |
| Retrieval accuracy | Memory competition quality | Proportion of contextually-appropriate retrievals |

---

## References

Anderson, J.R. (2007). *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press.  
Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences, 4,* 417–423.  
Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences, 24,* 87–114.  
De Neys, W. & Pennycook, G. (2019). Logic, fast and slow: Advances in dual-process theorizing. *Current Directions in Psychological Science, 28,* 503–509.  
Dörner, D. (1999). *Bauplan für eine Seele* (Blueprint for a Soul). Rowohlt.  
Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus and Giroux.  
Laird, J.E. (2012). *The Soar Cognitive Architecture.* MIT Press.  
Miller, G.A. (1956). The magical number seven, plus or minus two. *Psychological Review, 63,* 81–97.  
Newell, A. (1990). *Unified Theories of Cognition.* Harvard University Press.  
O'Reilly, R.C. & Frank, M.J. (2006). Making working memory work. *Neural Computation, 18,* 283–328.  
Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science, 12,* 257–285.  
Tulving, E. (1972). Episodic and semantic memory. In Tulving & Donaldson (Eds.), *Organization of Memory.* Academic Press.  

---

*AI-STEM — Open Research from Vektra Technologies, AI Division*  
*github.com/PabloTheThinker/AI-STEM*
