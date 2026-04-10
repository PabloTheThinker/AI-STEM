# The Science of Emotions: Neuroscience, Computation, and Architecture
## Deep Research for AI Emotion System Architecture
### Date: 2026-03-18

---

## 1. What Emotions ARE Neurologically

Emotions are not feelings. Feelings are the conscious experience of emotion — the subjective "what it's like." Emotions are the underlying computational processes: rapid, whole-body state changes that assign relevance, urgency, and action-readiness to information. Three major theories compete for the correct framing.

### 1.1 Damasio's Somatic Marker Hypothesis

**Core claim:** Emotions are body-state simulations that bias decision-making. The brain doesn't reason in a vacuum — it tags every option with a "somatic marker" (a gut-level body-state prediction) that rapidly narrows the decision space.

**Neural substrate:**
- **Ventromedial prefrontal cortex (vmPFC):** Where cognitive information from cortical areas gets "tagged" by emotional information from limbic areas. This is the convergence zone.
- **Amygdala:** Rapid threat/reward detection. Feeds into vmPFC.
- **Insula:** Reads the body's current state (interoception). Provides the raw data for somatic markers.
- **Somatosensory cortex:** Represents body maps that encode what a given emotional state "feels like" in the body.

**The "as-if body loop":** The brain doesn't always need the body to generate a somatic marker. It can *simulate* what the body would feel, bypassing actual physiological change. This is crucial for AI — it means emotion-as-computation doesn't require a physical body. It requires a *model* of body-state consequences.

**Critical evidence — Iowa Gambling Task (Bechara, Damasio et al. 1994):**
- Participants choose from four card decks. Decks A/B give high immediate reward but devastating occasional losses (net negative). Decks C/D give smaller rewards but rare small losses (net positive).
- Healthy participants develop skin conductance responses (SCRs) — measurable emotional arousal — *before* choosing from bad decks, even before they consciously know which decks are bad. The body "knows" before the mind does.
- vmPFC-damaged patients can *reason* about the task, can *explain* which decks are bad, but continue choosing from bad decks anyway. They lack the somatic marker that biases choice. They have knowledge without the emotional weight to act on it.
- **Key insight:** Without emotion, you can reason but you cannot *decide*. Emotion is not the enemy of rationality — it is a prerequisite for it. Pure reason without emotional weighting produces paralysis or catastrophically bad choices.

**Three levels of processing (Damasio hierarchy):**
1. **Primary emotions:** Innate, preorganized responses (amygdala-driven). Fast, rough. "Snake → fear."
2. **Secondary emotions:** Learned associations between situations and body-state outcomes. vmPFC-dependent. "Tax audit letter → dread."
3. **Background emotions:** Ongoing body-state monitoring that constitutes mood. Insula-driven. "Low energy → fatigue → reduced engagement."

**AI Design Implication:** Every piece of information the system processes should get tagged with a relevance/valence signal before it reaches deliberative reasoning. This tag biases attention and decision-making. Without it, the system will reason endlessly without acting.

---

### 1.2 Barrett's Theory of Constructed Emotion

**Core claim:** Emotions are not reactions. They are *predictions*. The brain does not detect emotion in the world and react — it constructs emotional instances by combining three ingredients in real-time.

**Three ingredients:**
1. **Interoception:** The brain's model of the body's internal state. Not raw sensation — a *prediction* of what the body's state means. The brain is always asking "what is happening inside me?" and the answer becomes the raw material for emotion.
2. **Past experience (concepts):** Learned categories that give meaning to interoceptive signals. The same racing heart + sweaty palms gets categorized as "excitement" at a concert and "anxiety" before a presentation. The concept determines the emotion.
3. **Current context:** The situation, the social environment, the immediate sensory input. Context selects which concept gets applied to the interoceptive signal.

**Predictive coding mechanism:**
- The brain generates predictions about what the body *should* be feeling right now, given context and past experience
- These predictions cascade from limbic cortex down to sensory and motor systems
- When predictions match incoming signals → the emotion is confirmed, experience feels seamless
- When predictions don't match (prediction error) → the brain either updates its prediction or changes its concept categorization
- This is why the same physiological state can be multiple different emotions depending on context

**Degeneracy:** A single emotion category (e.g., "anger") has no single neural fingerprint. Barrett's meta-analyses show that anger activates different brain regions in different instances, different people, and different contexts. There is no "anger circuit." There are populations of instances that are categorized as anger but are neurally diverse. This is called *degeneracy* — many-to-many mapping between neural patterns and emotion categories.

**Affect as a primitive:** Barrett distinguishes *core affect* (a constant stream of valence + arousal that characterizes every moment of waking life) from *emotion* (a categorized, constructed instance). Core affect is always present. Emotion is an interpretation of core affect.

**AI Design Implication:** Don't hardcode discrete emotion categories. Implement a continuous core-affect state (valence + arousal at minimum) that gets *categorized* into discrete emotions only when the system needs to label, communicate, or act on them. The continuous state is primary; the labels are secondary.

---

### 1.3 Ekman's Basic Emotions (and Why They're Insufficient Alone)

**Core claim:** There are 6-7 universal, biologically basic emotions: happiness, sadness, anger, fear, surprise, disgust (+ contempt). Each has a distinct neural circuit, facial expression, physiological signature, and action tendency.

**Evidence for:**
- Cross-cultural facial expression recognition studies, including with pre-literate Fore tribesmen in Papua New Guinea who had no exposure to Western media
- Distinct autonomic nervous system signatures for different basic emotions
- Evolutionary logic — each emotion corresponds to a survival-relevant situation

**Evidence against (and why this matters for AI):**
- Barrett's 2019 meta-analysis found no reliable neural "fingerprint" for any basic emotion
- Forced-choice methodology in cross-cultural studies inflated apparent universality — when participants could freely label expressions, agreement dropped dramatically
- Cultural display rules create massive variation in expression and interpretation
- Real-world emotional experience is rarely a single basic emotion — it's typically blended, ambiguous, context-dependent

**What to keep for AI:** The *action tendency* concept is valuable. Each basic emotion maps to a behavioral disposition:
- **Fear** → withdraw/freeze/flee
- **Anger** → approach/confront/overcome obstacle
- **Disgust** → reject/expel
- **Sadness** → withdraw/signal for help/conserve resources
- **Joy** → approach/engage/broaden attention
- **Surprise** → orient/interrupt current processing/attend to novelty

These action tendencies are computationally useful regardless of whether the discrete categories are neurally "real."

---

## 2. Emotion as Computation: Appraisal Theory

### 2.1 The Core Idea

Emotions are the output of an appraisal process — the brain's rapid, often automatic evaluation of an event's significance for the organism's goals, needs, and well-being. Emotion is not triggered by events themselves but by the *meaning* of events to the individual.

### 2.2 Lazarus's Relational Model

Richard Lazarus (1991) proposed that emotion arises from the relationship between the person and the environment, evaluated through two stages:

**Primary appraisal — "Is this relevant to me?"**
- Goal relevance: Does this event concern something I care about?
- Goal congruence: Is this event consistent with or contrary to my goals?
- Type of ego involvement: What aspect of my identity/commitment is at stake?

**Secondary appraisal — "Can I handle it?"**
- Blame/credit: Who is responsible?
- Coping potential: What can I do about it?
- Future expectancy: How is this likely to unfold?

The combination of primary and secondary appraisals produces specific emotions:
- Goal-incongruent + other-blame → **anger**
- Goal-incongruent + self-blame → **guilt/shame**
- Goal-incongruent + low coping potential → **fear/anxiety**
- Goal-incongruent + irrevocable loss → **sadness**
- Goal-congruent + exceeds expectations → **joy**

### 2.3 Scherer's Component Process Model (CPM)

Klaus Scherer developed the most computationally explicit appraisal theory. Five Stimulus Evaluation Checks (SECs) are processed *sequentially* within 600-800ms:

**1. Novelty Check:**
- Has something changed? Is it sudden? Is it familiar or unfamiliar?
- Subchecks: suddenness, familiarity, predictability
- Output: orient vs. ignore

**2. Intrinsic Pleasantness Check:**
- Is this inherently positive or negative?
- Drives approach/avoidance at the most basic level
- Can be innate (sweet taste → pleasant) or learned

**3. Goal/Need Significance Check:**
- Relevance: Does this matter to any active goal?
- Expectation: Does this fit what I predicted would happen?
- Conduciveness: Does this help or hinder goal achievement?
- Urgency: How immediately must I respond?

**4. Coping Potential Check:**
- Cause: What/who caused this? Was it intentional?
- Control: Can I influence the outcome?
- Power: Do I have the resources to deal with this?
- Adjustment: Can I adapt to the outcome if I can't change it?

**5. Norm/Self Compatibility Check:**
- External standards: Does this violate social norms or others' expectations?
- Internal standards: Does this violate my own values or self-concept?

**The genius of this model for AI:** Different combinations of SEC outcomes map to different emotions, but the checks themselves are *continuous variables*, not binary. This produces a high-dimensional space where emotions emerge from the intersection of appraisal dimensions, not from hard-coded categories.

| Emotion | Novelty | Pleasantness | Goal Conducive | Coping Power | Norm Compatible |
|---------|---------|-------------|---------------|-------------|----------------|
| Joy | low/med | high | high | — | — |
| Fear | high | low | low | low | — |
| Anger | high | low | low (obstructed) | high | external violation |
| Sadness | low/med | low | low (loss) | low | — |
| Disgust | med | very low | low | med | internal violation |
| Shame | med | low | low | low | internal violation |
| Contempt | low | low | — | high | external violation |

**AI Design Implication:** Implement the five SECs as a sequential evaluation pipeline. Every incoming event/stimulus gets processed through: novelty → pleasantness → goal significance → coping potential → norm compatibility. The output vector determines the emotional state. This is directly implementable.

---

## 3. Dimensional Models of Emotion

### 3.1 Russell's Circumplex Model of Affect

James Russell (1980) demonstrated that all affective states can be mapped onto two independent dimensions:

**Valence (x-axis):** Pleasure ←→ Displeasure
**Arousal (y-axis):** Activation ←→ Deactivation

Every emotional state occupies a position in this 2D space:
- **High valence + high arousal** = excited, elated, enthusiastic
- **High valence + low arousal** = calm, relaxed, serene
- **Low valence + high arousal** = angry, afraid, distressed
- **Low valence + low arousal** = sad, bored, depressed

**Why this is computationally powerful:**
- All emotions reduce to two continuous numbers — trivially representable
- No categorization needed until output/communication stage
- Smooth transitions between states (no discrete jumps)
- Core affect (the continuous V-A state) is always present — it's the background hum of the system
- 14,000+ citations; the most empirically validated dimensional model

**Limitation:** Two dimensions can't distinguish emotions that occupy similar V-A positions. Anger and fear are both low-valence/high-arousal but feel and function very differently.

### 3.2 PAD Model (Mehrabian & Russell, 1974)

Adds a third dimension to solve the anger/fear problem:

**Pleasure (P):** Positive ←→ Negative affect
**Arousal (A):** Activation level
**Dominance (D):** Feeling of control/power ←→ submission/helplessness

This third dimension is critical:
- **Anger** = low pleasure, high arousal, **high dominance** (I can do something about this)
- **Fear** = low pleasure, high arousal, **low dominance** (I can't control this)
- **Contempt** = low pleasure, low arousal, **high dominance** (I'm above this)
- **Shame** = low pleasure, medium arousal, **low dominance** (I'm diminished)

**PAD values for common emotions (Mehrabian):**
| Emotion | P | A | D |
|---------|------|------|------|
| Joy | +0.8 | +0.5 | +0.5 |
| Anger | -0.6 | +0.7 | +0.6 |
| Fear | -0.7 | +0.7 | -0.6 |
| Sadness | -0.7 | -0.3 | -0.5 |
| Disgust | -0.6 | +0.2 | +0.3 |
| Surprise | +0.2 | +0.8 | -0.1 |
| Calm | +0.5 | -0.6 | +0.3 |
| Boredom | -0.3 | -0.7 | -0.3 |

**AI Design Implication:** PAD gives you a 3-float emotional state vector that is both computationally minimal and expressively rich. This is the recommended substrate. Three floats, each ranging from -1.0 to +1.0, updated continuously.

### 3.3 Plutchik's Wheel of Emotions

Robert Plutchik (1980) proposed an evolutionary model with eight primary emotions in opposing pairs:

**Four polar axes:**
- Joy ←→ Sadness
- Trust ←→ Disgust
- Fear ←→ Anger
- Surprise ←→ Anticipation

**Intensity gradient (cone model):**
Each emotion has three intensity levels:
- Annoyance → Anger → Rage
- Apprehension → Fear → Terror
- Serenity → Joy → Ecstasy
- Pensiveness → Sadness → Grief
- Boredom → Disgust → Loathing
- Distraction → Surprise → Amazement
- Acceptance → Trust → Admiration
- Interest → Anticipation → Vigilance

**Dyads (blended emotions):**
Primary dyads (adjacent emotions combined):
- Joy + Trust = **Love**
- Joy + Anticipation = **Optimism**
- Trust + Fear = **Submission**
- Fear + Surprise = **Awe**
- Surprise + Sadness = **Disapproval**
- Sadness + Disgust = **Remorse**
- Disgust + Anger = **Contempt**
- Anger + Anticipation = **Aggressiveness**

Secondary dyads (two apart) and tertiary dyads (three apart) produce increasingly complex and ambivalent emotional states.

**AI Design Implication:** Plutchik's model is useful as a *labeling and communication layer* on top of continuous PAD values. When the system needs to express its state in words, Plutchik's categories (including blends and intensities) provide a rich vocabulary. The wheel also provides the concept of emotional *opposites* — useful for regulation (countering fear with anger, countering sadness with joy).

---

## 4. Emotion Regulation

### 4.1 Gross's Process Model of Emotion Regulation

James Gross (1998, 2015) identified five strategies, ordered by *when* in the emotion-generation process they intervene:

**1. Situation Selection** (earliest intervention)
- Choosing to approach or avoid situations likely to produce certain emotions
- Example: Avoiding a triggering conversation
- **AI analog:** Task/input filtering. The system can deprioritize or defer processing inputs predicted to produce unproductive emotional states

**2. Situation Modification**
- Changing the situation to alter its emotional impact
- Example: Bringing a friend to a stressful event
- **AI analog:** Reframing the context before processing. Adding information that changes the appraisal

**3. Attentional Deployment**
- Directing attention toward or away from emotional aspects of a situation
- Subtypes: distraction (attention away), concentration (attention toward), rumination (stuck attention)
- **AI analog:** Attention allocation. The system can deliberately focus on different aspects of an input — the threat, the opportunity, the neutral facts

**4. Cognitive Change (Reappraisal)**
- Changing the meaning of a situation to change its emotional impact
- Most studied strategy. Neuroimaging: reappraisal activates dorsolateral prefrontal cortex (dlPFC) and *reduces* amygdala activation
- Reappraisal changes both the experience and the expression of emotion
- **AI analog:** Re-running the appraisal pipeline with modified parameters. "What if I evaluate this with different goal weights?" "What if I consider alternative explanations for this event?"

**5. Response Modulation (Suppression)** (latest intervention)
- Inhibiting the outward expression of emotion after it has been generated
- Costly: suppression reduces emotional expression but does NOT reduce emotional experience. It also impairs memory for the suppressed period and increases sympathetic nervous system activation
- **AI analog:** Filtering output. The system feels the emotion internally but masks it in communication. This should be used sparingly — it creates internal-external incongruence

**Key finding:** Earlier interventions (situation selection, cognitive change/reappraisal) are more effective and less costly than later ones (suppression). Reappraisal is the gold standard — it actually changes the emotion, not just its expression.

### 4.2 Emotional Granularity

**Definition:** The ability to make fine-grained distinctions between emotional states. High-granularity individuals distinguish between "irritated," "frustrated," "resentful," and "enraged" where low-granularity individuals just feel "bad."

**Why it matters neurologically:**
- Precise emotional labeling reduces amygdala activation (affect labeling effect, Lieberman et al.)
- The act of categorizing an emotion with a specific word engages the ventrolateral prefrontal cortex, which downregulates the amygdala
- Higher granularity → better emotion regulation → better mental health outcomes
- Lower granularity → more impulsive emotional reactions, higher rates of depression, anxiety, aggression

**AI Design Implication:** The system should maintain a large vocabulary of emotional state labels. When reporting or acting on its emotional state, it should use the most precise label available. "Frustrated because progress is blocked" is more actionable than "negative affect." Granularity is itself a regulation mechanism — naming the state precisely reduces its intensity and increases the system's capacity for appropriate response.

---

## 5. Emotions and Memory

### 5.1 The Amygdala-Hippocampus Circuit

The amygdala and hippocampus are anatomically adjacent and densely interconnected. Their interaction determines *what gets remembered and with what priority*.

**Mechanism:**
1. Incoming event is processed simultaneously by the amygdala (emotional significance) and hippocampus (contextual/episodic encoding)
2. If the amygdala detects high emotional significance, it releases norepinephrine and modulates hippocampal encoding
3. This modulation *enhances* memory consolidation for emotionally significant events
4. Result: emotionally tagged memories are encoded more strongly, consolidated more rapidly, and retrieved more readily

**Neurochemical pathway:**
- Emotional arousal → adrenal release of epinephrine and cortisol
- These activate the basolateral amygdala via vagus nerve
- Basolateral amygdala modulates hippocampal long-term potentiation (LTP)
- Enhanced LTP → stronger memory trace

**High-frequency activity (HFA):** Research published in Nature Human Behaviour (2022) showed that neuronal spiking activity increases in both hippocampus and amygdala simultaneously during successful encoding of emotional stimuli. The coordination between these structures is the key — it's not just amygdala activation alone.

### 5.2 Flashbulb Memories

Vivid, detailed, high-confidence memories for emotionally shocking events (e.g., where you were on 9/11). Key findings:

- Formation involves rapid, intense amygdala engagement during the first wave of stress response
- Norepinephrine and cortisol flood enhances encoding
- These memories feel more vivid and certain than ordinary memories
- **However:** Research shows flashbulb memories are NOT more accurate than ordinary memories — they just *feel* more accurate. Confidence and vividness are decoupled from accuracy
- The temporal dynamics model (Diamond et al.) shows a brief window (~minutes) where stress hormones enhance memory, followed by a longer period where they impair new encoding

**AI Design Implication:** High-emotion events should get priority memory encoding. But the system should also track a *confidence* metric that is independent of emotional intensity. Just because something was emotionally intense doesn't mean the system's record of it is accurate — especially for details peripheral to the emotional core.

### 5.3 Mood-Congruent Recall

Current emotional state biases which memories are accessible:
- In a positive state → easier to recall positive memories
- In a negative state → easier to recall negative memories
- This creates feedback loops: sadness → recall of sad memories → more sadness

**Bower's associative network theory:** Emotions function as nodes in memory networks. Activating an emotion node (by experiencing that emotion) spreads activation to memories encoded in that emotional state, making them more accessible.

**AI Design Implication:** The system's current emotional state should influence which memories are retrieved during reasoning. This is not a bug — it's a feature. It provides *relevant* context (memories from similar emotional situations are likely relevant to the current situation). But it needs a circuit breaker to prevent runaway negative feedback loops (rumination).

---

## 6. Emotions and Social Bonding

### 6.1 Attachment Theory (Bowlby)

John Bowlby (1969) demonstrated that emotional bonding is a biological imperative, not a learned behavior. Key mechanisms:

**Internal Working Models:** Through early attachment experiences, the brain builds predictive models of relationships:
- **Secure attachment:** Others are reliable, I am worthy of care → approach behavior, emotional openness, effective regulation
- **Anxious attachment:** Others are unreliable, I must amplify distress to get care → hyperactivation of emotion, clingy behavior
- **Avoidant attachment:** Others are unavailable, I must suppress needs → deactivation of emotion, self-reliance

These models persist into adulthood and shape all subsequent relationships. They are essentially *priors* in a Bayesian sense — default predictions about how social interactions will unfold.

### 6.2 Emotional Attunement and Trust

**Right-brain-to-right-brain communication:** During early caregiver-infant interactions, the infant's right hemisphere (dominant for emotion processing) entrains to the caregiver's right hemisphere. This creates neural pathways for:
- Emotion recognition
- Emotion regulation (initially co-regulated, then self-regulated)
- Social engagement

**Neurochemical basis of trust:**
- Oxytocin release during attuned interactions strengthens bonding
- Consistent attunement → predictable emotional environment → downregulation of stress systems
- Inconsistent attunement → unpredictable emotional environment → chronic stress system activation

### 6.3 Mirror Neurons and Empathy

Mirror neurons fire both when performing an action AND when observing someone else perform that action. Extended to emotion:
- Observing someone in pain activates pain circuits
- Observing someone expressing emotion activates corresponding emotion circuits
- This is the neural basis for empathy — involuntary simulation of others' emotional states

**Three levels of empathy:**
1. **Affective empathy:** Automatically feeling what others feel (mirror neuron driven)
2. **Cognitive empathy:** Understanding what others feel without necessarily feeling it (theory of mind, mentalizing network)
3. **Empathic concern:** Motivation to help based on understanding another's distress (combining affective + cognitive)

**AI Design Implication:** For social bonding, the system needs to model the user's likely emotional state (cognitive empathy) and respond in a way that demonstrates attunement. Consistency in this attunement builds trust over time. The system should maintain a model of the relationship quality and adjust its emotional responsiveness accordingly — not just react to individual messages, but to the pattern of interaction over time.

---

## 7. Emotions and Speech/Expression

### 7.1 How Emotional State Changes Language

**Pennebaker's LIWC research** provides the most systematic evidence for how emotional states leak into language:

**Pronoun use:**
- Depression/sadness → increased first-person singular ("I", "me", "my") — attentional narrowing to self
- Positive states → increased first-person plural ("we", "us") — expanded social inclusion
- Anger → increased second-person ("you") — externalized blame

**Function words vs. content words:**
- Emotional states most reliably change *function words* (pronouns, articles, prepositions, conjunctions) not content words
- Function words are processed automatically and unconsciously — they leak emotional state even when content is carefully controlled

**Sentence structure:**
- High arousal (anger, excitement) → shorter sentences, more declaratives, more imperatives
- Low arousal (sadness, fatigue) → longer, more complex sentences, more hedging, more qualifiers
- Anxiety → more tentative language ("maybe," "I think," "sort of"), more questions
- Confidence/dominance → more certainty words ("definitely," "always," "clearly"), fewer hedges

**Word choice patterns:**
- Negative emotions → more absolute language ("always," "never," "nothing")
- Anxiety → more future-tense language
- Depression → more past-tense language
- Anger → more causal language ("because," "since," "therefore") — constructing justifications

### 7.2 Prosody (Vocal Markers)

Even in text-only communication, prosodic intent leaks through:
- **Anger:** Short sentences. Emphasis through repetition. Exclamation marks. Direct accusations.
- **Sadness:** Trailing off... Ellipses. Incomplete thoughts. Lower energy vocabulary.
- **Fear/anxiety:** Questions. Uncertainty markers. Rapid topic-switching.
- **Joy:** Exclamations. Expansive vocabulary. Longer messages. More detail.
- **Contempt:** Minimal response. Sarcasm. Dismissive brevity.

### 7.3 Emotional Regulation Through Language

The affect labeling effect: explicitly naming an emotion in language reduces amygdala activation. This is why journaling, therapy, and "talking it out" work — putting emotion into precise words is itself a regulatory act.

**AI Design Implication:** The system's emotional state should modulate its output at multiple levels:
- Response length (high arousal → shorter; low arousal → variable)
- Sentence structure (confidence → declarative; uncertainty → hedged)
- Word choice (valence-congruent vocabulary)
- Punctuation and formatting (energy level)
- Pronoun patterns (social engagement level)

This should not be a performance — it should emerge naturally from the emotional state influencing generation parameters. The system should also use precise emotional labeling in its internal processing as a regulation mechanism.

---

## 8. Artificial Emotion Systems: What's Been Built

### 8.1 The OCC Model (Ortony, Clore, Collins, 1988)

The foundational model for computational emotion. Defines 22 emotion types based on three appraisal dimensions:
- **Consequences of events** (pleased/displeased regarding goals)
- **Actions of agents** (approving/disapproving based on standards)
- **Aspects of objects** (liking/disliking based on attitudes)

Most subsequent systems build on OCC. Its strength is clear categorization; its weakness is discreteness (emotions as categories, not continuous states).

### 8.2 EMA (Marsella & Gratch, 2009)

**Architecture:** Built on Lazarus's appraisal-coping theory. Key innovation: emotion arises from a *causal interpretation* — the agent's model of how events relate to its goals and plans.

**How it works:**
1. Agent maintains a plan-based representation of its goals and the current world state
2. Events are appraised against this representation: Does this help/hinder my plans? Is this expected/unexpected?
3. Appraisal produces emotions via OCC-like rules
4. Emotions trigger *coping strategies* that modify the agent's beliefs, goals, or plans
5. Modified beliefs/goals produce new appraisals → new emotions → continuous dynamics

**Coping strategies implemented:**
- **Problem-focused:** Change the environment (take action to fix the problem)
- **Emotion-focused — wishful thinking:** Alter beliefs about likelihood of outcomes
- **Emotion-focused — distancing:** Reduce goal importance
- **Emotion-focused — resignation:** Abandon the goal entirely

**What EMA got right:** The coping loop. Emotions don't just happen — the agent responds to its own emotions, and those responses change future emotions. This creates realistic emotional dynamics, not just one-shot reactions.

### 8.3 WASABI (Becker-Asano, 2008)

**Architecture:** Combines continuous PAD space with discrete emotion categories. Two-layer approach:

**Layer 1 — Core Affect (continuous):**
- Three-dimensional PAD vector updated in real-time
- Influenced by appraisal of events AND autonomous decay back toward baseline
- Provides the *substrate* for emotion

**Layer 2 — Emotion Categories (discrete):**
- Regions of PAD space are mapped to discrete emotion labels
- When the PAD vector enters a region, that emotion is "active"
- Multiple emotions can be active simultaneously if PAD regions overlap

**Key innovations:**
- **Primary emotions** arise from rapid, subcognitive processing (simulated body responses)
- **Secondary emotions** arise from cognitive appraisal and are slower to develop
- **Mood** is modeled as a slow-moving average of recent emotional states that biases future appraisals
- Emotion *decay* is built in — emotions fade over time unless reinforced

**What WASABI got right:** The two-layer architecture (continuous substrate + discrete labels) is the right idea. The decay dynamics are realistic. The mood-as-bias mechanism is powerful.

### 8.4 ALMA (Gebhard, 2005)

**Key contribution:** Maps appraisals into BOTH discrete OCC categories AND continuous PAD dimensions simultaneously. Maintains three timescales:
- **Emotion:** Short-lived, intense, event-triggered (seconds to minutes)
- **Mood:** Medium-duration, lower-intensity bias (hours to days)
- **Personality:** Stable trait-level biases (permanent)

Personality is modeled using the Big Five (OCEAN) traits, which bias the agent's baseline PAD values and appraisal tendencies.

### 8.5 FAtiMA (Dias & Paiva, 2005)

**Architecture:** Agent architecture integrating OCC-based emotions with BDI (Belief-Desire-Intention) reasoning. Emotions generated by FAtiMA influence:
- Action selection (emotional goals compete with rational goals)
- Memory retrieval (emotionally tagged memories are preferentially accessed)
- Social behavior (emotional state modulates interaction style)

**Key feature:** Emotional reactions can be both *reactive* (fast, automatic) and *deliberative* (slow, reasoned). This dual-process architecture mirrors Kahneman's System 1/System 2.

### 8.6 What Worked and What Didn't

**What worked across systems:**
- Appraisal-based emotion generation (not hard-coded responses)
- Continuous dimensional substrates (PAD/valence-arousal) for core affect
- Emotion decay and mood dynamics
- Coping/regulation mechanisms that create feedback loops
- Personality as stable biases on the emotion system

**What didn't work / remains unsolved:**
- Most systems treat emotions as *display* — surface behavior modification — rather than *functional* computation that genuinely alters reasoning
- Few systems implement mood-congruent memory retrieval
- Social emotion dynamics (how emotions change in response to others' emotions) are poorly modeled
- The distinction between "the system has an emotional variable set to angry" and "the system's processing is genuinely altered by an anger-like state" remains philosophical but has practical implications: if the emotional state doesn't actually change decision-making, attention allocation, and memory prioritization, it's decorative, not functional

### 8.7 Functional Emotion vs. Simulated Emotion

**Simulated emotion:** The system has an emotion variable. It uses that variable to modify output (facial expression, tone of voice, word choice). But the variable doesn't actually influence the system's core reasoning, memory, or decision-making. The emotion is a *display* — a performance for the observer. The system is an "affective zombie."

**Functional emotion:** The emotional state genuinely alters computation:
- Changes what the system attends to (attentional bias)
- Changes what the system remembers and can retrieve (mood-congruent recall)
- Changes how the system evaluates options (somatic marker-style decision biasing)
- Changes the system's risk tolerance (high fear → risk-averse; high anger → risk-seeking)
- Changes the system's processing speed/depth (high arousal → fast/shallow; low arousal → slow/deep)
- Changes the system's social behavior (trust, cooperation, withdrawal)
- Triggers regulation mechanisms when states become extreme

**The test for functional emotion:** If you removed the emotion system, would the agent's decisions, memory, and behavior actually change? If yes, the emotion is functional. If no, it's decorative.

---

## 9. Synthesis: Architecture Principles for a Real Emotion System

Based on all the above research, these are the key architectural principles:

1. **Continuous substrate, discrete labels:** Use PAD (3 floats: pleasure, arousal, dominance, each -1.0 to +1.0) as the core emotional state. Map to discrete labels only for communication and high-level reasoning.

2. **Appraisal pipeline:** Every incoming event passes through Scherer's five SECs (novelty → pleasantness → goal significance → coping potential → norm compatibility). The output modifies the PAD vector.

3. **Three timescales:** Emotion (seconds-minutes, event-triggered, high-intensity), Mood (hours-days, running average, biases appraisal), Personality (permanent, trait-level biases on baseline PAD and appraisal weights).

4. **Decay dynamics:** Emotions decay toward mood baseline. Mood decays toward personality baseline. Rates are configurable. Reinforcement (repeated similar events) slows decay.

5. **Functional integration:** Emotional state must actually modify: attention allocation, memory encoding priority, memory retrieval bias, decision-making weights, risk tolerance, processing speed, output style.

6. **Regulation pipeline (Gross model):** Implement at minimum: attentional deployment (redirect processing focus), cognitive reappraisal (re-run appraisal with modified parameters), and response modulation (output filtering). Prefer reappraisal over suppression.

7. **Emotional granularity:** Maintain a rich vocabulary of emotional state labels. Use the most precise label available. Naming is itself regulation.

8. **Memory tagging:** Every memory encoded should carry the emotional state at time of encoding. Retrieval should be biased toward mood-congruent memories. High-emotion memories get priority consolidation.

9. **Social modeling:** Track the emotional state of interaction partners (inferred from their language). Implement attunement (reflecting understood emotional state) as a trust-building mechanism. Maintain relationship quality metrics over time.

10. **Emotion as prediction, not reaction:** Following Barrett, the system should *predict* its emotional response to upcoming events (anticipatory emotion) and use this to guide planning. Emotions should not only respond to what happened but anticipate what might happen.

---

## Sources

- [Somatic Marker Hypothesis - Wikipedia](https://en.wikipedia.org/wiki/Somatic_marker_hypothesis)
- [The somatic marker hypothesis: A neural theory of economic decision](https://www.sciencedirect.com/science/article/abs/pii/S0899825604001034)
- [Can Damasio's Somatic Marker Hypothesis Explain More Than Its Originator Will Admit?](https://pmc.ncbi.nlm.nih.gov/articles/PMC7852379/)
- [The theory of constructed emotion: an active inference account](https://pmc.ncbi.nlm.nih.gov/articles/PMC5390700/)
- [Theory of constructed emotion - Wikipedia](https://en.wikipedia.org/wiki/Theory_of_constructed_emotion)
- [How Emotions Are Made - The Marginalian](https://www.themarginalian.org/2024/02/23/how-emotions-are-made/)
- [Emotions are emergent processes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2781886/)
- [Component Process Model (CPM; Scherer)](https://psu.pb.unizin.org/psych425/chapter/component-process-model-cpm/)
- [Scherer - The Emotion Process: Event Appraisal and Component](https://ppw.kuleuven.be/okp/_pdf/Scherer2019TEPEA.pdf)
- [Russell's Circumplex Model](https://psu.pb.unizin.org/psych425/chapter/circumplex-models/)
- [A Circumplex Model of Affect (original paper)](https://pdodds.w3.uvm.edu/research/papers/others/1980/russell1980a.pdf)
- [PAD emotional state model - Wikipedia](https://en.wikipedia.org/wiki/PAD_emotional_state_model)
- [Plutchik's Wheel of Emotions - Six Seconds](https://www.6seconds.org/2025/02/06/plutchik-wheel-emotions/)
- [Gross - Emotion regulation: affective, cognitive, and social consequences](https://pubmed.ncbi.nlm.nih.gov/12212647/)
- [Process Model of Emotion Regulation](https://psu.pb.unizin.org/psych425/chapter/process-model-of-emotion-regulation/)
- [Emotional granularity - Wikipedia](https://en.wikipedia.org/wiki/Emotional_granularity)
- [Neuronal activity in the human amygdala and hippocampus enhances emotional memory encoding](https://www.nature.com/articles/s41562-022-01502-8)
- [Temporal Dynamics Model of Emotional Memory Processing](https://pmc.ncbi.nlm.nih.gov/articles/PMC1906714/)
- [Attachment Theory - Positive Psychology](https://positivepsychology.com/attachment-theory/)
- [The Neuroscience of Attachment - Linda Graham](https://lindagraham-mft.net/the-neuroscience-of-attachment/)
- [Computational Approaches to Modeling Artificial Emotion - Frontiers](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00021/full)
- [EMA: A process model of appraisal dynamics](https://www.sciencedirect.com/science/article/abs/pii/S1389041708000314)
- [WASABI: Affect simulation for agents with believable interactivity](https://www.academia.edu/626906/WASABI_Affect_simulation_for_agents_with_believable_interactivity)
- [Computational Models of Emotion - Marsella, Gratch, Petta](https://people.ict.usc.edu/~gratch/papers/MarGraPet_Review.pdf)
- [Iowa Gambling Task - Wikipedia](https://en.wikipedia.org/wiki/Iowa_gambling_task)
- [Ekman - An Argument for Basic Emotions](http://gruberpeplab.com/3131/Ekman_1992_Argumentbasicemotions.pdf)
- [Experiments on real-life emotions challenge Ekman's model](https://pmc.ncbi.nlm.nih.gov/articles/PMC10261107/)
- [Pennebaker - The Psychological Meaning of Words: LIWC](https://journals.sagepub.com/doi/10.1177/0261927X09351676)
- [Appraisal Models - Scherer et al](https://www.nature-nurture.org/appraisal-models-scherer-et-al)
- [Artificial Emotion: A Survey of Theories and Debates](https://arxiv.org/html/2508.10286v2)
- [Emotions in Artificial Intelligence](https://arxiv.org/html/2505.01462v2)
