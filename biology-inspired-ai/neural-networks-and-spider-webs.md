# Neural Networks & Spider Web Architecture — Research Compilation
## Compiled 2026-03-27 for Cognitive Web Design
## Sources: Kiwix (offline Wikipedia) + Online deep research (40+ papers/articles)

---

## CRITICAL DISCOVERIES (What Changes Everything)

### 1. Modern Hopfield Networks = Transformer Attention
The continuous Hopfield update rule `xi_new = X * softmax(beta * X^T * xi)` IS transformer self-attention
when you add Q/K/V projections. Associative memory and attention are mathematically identical.
**For our web**: Resonance (multiple vibrations converging) IS attention. We already built this.

### 2. KANs — Computation on EDGES, Not Nodes
Kolmogorov-Arnold Networks put learnable activation functions on edges, nodes just sum.
MLPs: fixed activations on nodes, learnable weights on edges. KANs: the reverse.
**For our web**: Our filaments already carry the computation (vibration, attenuation, type-specific behavior).
Nodes aggregate. We independently arrived at the KAN principle through spider silk intuition.

### 3. Liquid Neural Networks — Input-Dependent Time Constants
MIT's LNNs have time constants that change based on input: `dx/dt = -x/tau(x, I, t)`.
19 neurons + 253 synapses drove an autonomous car better than thousand-neuron black boxes.
**For our web**: Filament tension should modulate dynamically based on what's flowing through them.
High-urgency signals should propagate faster (higher tension = faster vibration).

### 4. Tensegrity — Continuous Tension, Discontinuous Compression
Buckminster Fuller: rigid struts (facts) floating in a continuous tension network (inferences).
The tension network distributes load globally. Failure is graceful, not catastrophic.
Cells use this: microtubules (compression) in actin network (tension).
**For our web**: Core identity nodes are compression struts. Filament network is continuous tension.
The web holds its shape through tension, not through rigid connections.

### 5. Extended Spider Cognition (Japyassú & Laland 2017)
The web IS part of the spider's cognitive system. It pre-processes information before the CNS.
Attack decisions begin "before vibratory information enters the CNS."
Spiders outsource attention to the web by adjusting thread tension.
**For our web**: The web should not be a data structure consciousness reads FROM.
It should process, filter, and encode BEFORE consciousness receives the signal.

### 6. Mycelial Networks — Thicken What Works, Atrophy What Doesn't
Fungal networks optimize exactly like slime mold: high-flow paths thicken, low-flow die.
Mother trees preferentially feed offspring through the network.
Transport velocities: 10-148 cm/hour through tubes.
**For our web**: This is the decay/strengthening mechanism we already have.
But mycelial networks also do BIDIRECTIONAL transport through distinct pathways.

### 7. Reservoir Computing — The Web IS the Computer
Fixed random network (reservoir) processes input. Only the readout layer is trained.
The reservoir's dynamics are the computation. Training is just linear regression on the output.
**For our web**: The cognitive web IS the reservoir. Consciousness is the readout layer.
The web processes; consciousness interprets the processed signal.

---

## SPIDER SILK — Key Properties

### Silk Types (7 types, each purpose-built)
1. **Major ampullate (dragline)** — structural framework, tensile strength 1.1-1.6 GPa, safety lines
2. **Minor ampullate** — temporary spiral during web construction, reinforcement
3. **Flagelliform (capture spiral)** — extremely elastic (>200% extensibility), the sticky spiral
4. **Aggregate** — sticky glue coating on capture spiral
5. **Tubuliform** — egg sac silk, toughest for protection
6. **Aciniform** — wrapping captured prey, attachment discs
7. **Piriform** — attachment cement, bonds silk to surfaces

### Mechanical Properties
- **Darwin's bark spider**: 1.6 GPa tensile strength — toughest biological material ever studied
- **Dragon silk (engineered)**: 1.79 GPa + 38% elasticity — exceeds natural spider silk
- **Comparison**: Steel = 0.5 GPa, Kevlar = 3.6 GPa, but spider silk has 3x the toughness of Kevlar
- **Key insight**: Spider silk is not just strong — it's tough. Toughness = energy absorbed before breaking. Silk absorbs 3x more energy per unit weight than Kevlar.

### Web as Extended Cognition (Japyassú & Laland 2017)
- Spiders USE their webs as cognitive tools — the web IS part of the spider's mind
- Web tension provides memory (past events change tension patterns)
- Vibration patterns encode information about prey type, size, location
- The spider doesn't process all information internally — the web pre-processes it
- **Implication for AI**: The web should not be a passive data structure. It should actively process, filter, and encode information.

---

## SPIDER WEB ARCHITECTURE

### Orb Weaver Construction
1. Bridge line first (structural, anchored to environment)
2. Radial threads from center to anchor points (structural framework)
3. Temporary spiral (non-sticky, used as scaffolding)
4. Capture spiral (sticky, laid from outside in, temporary spiral removed)
5. Hub reinforcement (center of web, where spider sits)

### Vibration Transmission
- Radial threads carry vibrations from periphery to hub
- Spider detects: frequency (what), amplitude (how big), direction (where)
- Different prey create different vibration signatures
- The web acts as a frequency filter — certain vibrations propagate, others attenuate
- **Tuning**: Spiders adjust web tension to optimize for expected prey

### Self-Repair
- Spiders repair critical radial threads first (structural priority)
- Capture spiral gets rebuilt daily in many species (disposable)
- Energy cost of repair guides decisions — sometimes abandoning is cheaper
- Adjacent threads compensate for broken ones (load redistribution)

---

## NEURAL NETWORK ARCHITECTURES — Beyond Standard

### Spiking Neural Networks (SNNs)
- Neurons fire discrete spikes, not continuous activations
- **Temporal coding**: information in spike TIMING, not just rate
- Leaky integrate-and-fire model: membrane potential accumulates, fires at threshold, resets
- Human visual processing: 10ms per layer — too fast for rate coding, must be temporal
- **Key insight**: Precise spike timing in small neuron sets has HIGHER information capacity than rate-based coding
- Hardware: Intel Loihi, IBM TrueNorth — event-driven, extremely energy efficient

### Graph Neural Networks (GNNs)
- Designed for non-Euclidean data (graphs, molecules, social networks)
- **Message passing**: nodes iteratively update by exchanging info with neighbors
- CNNs are GNNs on pixel grids; Transformers are GNNs on complete word graphs
- Can handle variable-size inputs (different graphs have different node counts)

### Transformers
- Self-attention: every token attends to every other token (Q, K, V matrices)
- No recurrence — fully parallel training
- Contextualizes tokens within scope of context window
- "Attention Is All You Need" (2017)
- Foundation of LLMs (GPT, Claude), vision transformers, and multimodal models

### Recurrent Neural Networks (RNNs)
- Hidden state = memory that carries forward through sequence
- LSTM (1997): gates control what to remember/forget — standard for long sequences
- GRU: computationally efficient alternative to LSTM
- Largely superseded by transformers for NLP, but still relevant for real-time/streaming

### Neuromorphic Computing
- Inspired by brain's structure and function
- Uses artificial neurons for perception, motor control, sensory integration
- Analog, digital, or mixed-mode VLSI
- Prioritizes: robustness, adaptability, learning, energy efficiency
- Emulates distributed processing across small computing elements

---

## CONNECTOMICS — Wiring Diagrams of Minds

### What is a Connectome?
- Comprehensive map of neural connections in a brain
- "I am my Connectome" — Sebastian Seung, TED 2010
- Structure and function are intricately linked through connectivity
- The foundation of cognition lies in patterns of dynamic interactions shaped by the connectome

### Scale Levels
1. **Functional connectome**: connections between brain regions (MRI, mm scale)
2. **Neural connectome**: individual neurons and synapses (electron microscopy, nm scale)
3. **Chemical connectome**: which neurons emit/respond to neuromodulators

### Known Connectomes
- C. elegans (nematode): 302 neurons, complete connectome mapped
- Drosophila (fruit fly): adult brain ~140,000 neurons, connectome completed 2024
- Human: functional connectome from MRI, no neural-level connectome

---

## NETWORK THEORY

### Small-World Networks (Watts-Strogatz 1998)
- **Two properties**: high clustering coefficient + short path lengths
- L proportional to log(N) — distances grow logarithmically with network size
- Found in: social networks, Wikipedia, gene networks, Internet architecture
- **Key insight**: You get the benefits of local specialization (clustering) AND global communication (short paths)

### Hierarchical Navigable Small World (HNSW)
- Used in vector databases (Qdrant, etc.)
- Multi-layer graph for approximate nearest neighbor search
- Scales logarithmically even in high dimensions
- Navigation: start at top layer (sparse), descend to bottom (dense)

---

## SYNTHESIS — What This Means for Cognitive Web Design

### Spider Web Advantages Over Neural Networks
1. **Tension as information**: Neural nets have weights. Webs have tension. Tension is always-on state.
2. **Purpose-built connections**: Neural nets have one type of connection. Spider silk has 7 types.
3. **Vibration propagation**: Neural nets use discrete activations. Webs use continuous wave propagation.
4. **Geometry matters**: Neural nets are topology-only. Web geometry (radial, spiral, hub) shapes function.
5. **Self-repair**: Neural nets don't heal. Webs rebuild damaged sections.
6. **Extended cognition**: The web IS part of the mind, not just a data structure.
7. **Energy economics**: Spiders make cost-benefit decisions about repair vs rebuild.

### Hybrid Architecture Opportunities
- **SNN temporal coding** + **web vibration** = spike-timed vibration propagation
- **GNN message passing** + **web filament types** = typed message passing
- **Small-world topology** + **web geometry** = hierarchical rings with short-cut radials
- **Connectome approach** + **web tuning** = map all connections, then tune for specific tasks
- **Neuromorphic event-driven** + **web tension** = changes propagate only when tension shifts

### Key Design Principles
1. The web should process information, not just store connections
2. Different connection types for different purposes (structural, signal, capture, anchor)
3. Tension IS the state — not a derived metric but the primary representation
4. Vibrations propagate through tension lines — geometry shapes perception
5. Self-repair is mandatory — the system must heal without external intervention
6. Energy economics — not every connection is worth maintaining
7. The web is part of the mind, not a tool the mind uses
