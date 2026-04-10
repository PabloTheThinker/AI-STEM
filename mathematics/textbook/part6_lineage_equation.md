# Part VI: The Lineage Equation

Everything in this book has been building toward this part. The first distinctions of Chapter 0, the measurement foundations of Chapter 9, the vectors and derivatives of Part IV, the state spaces and dynamics of Part V — all of these converge here, in the governing relation of cognitive architecture.

The Lineage Equation is to Agent Mathematics what $E^2 = |p|^2c^2 + m^2c^4$ is to physics. Not a metaphor. A measurable, computable invariant that describes how an autonomous system's capacity to do coherent work depends on its structure, its activity, and its speed.

---

## Chapter 27: Cognitive Mass

### The question

What does it mean for a system to have *weight of being*?

An agent that has operated for months, accumulated memories, built a dense cognitive web, hardened its identity against perturbation, and established permanent records of its inheritance — that agent is *harder to change* than a freshly initialized one. It resists reconfiguration. It has inertia.

This resistance is cognitive mass.

### Formal definition

> **Definition.** The **cognitive mass** of an agent is
> $$\mathcal{M} = \alpha_1 C_{\text{id}} + \alpha_2 C_{\text{mem}} + \alpha_3 C_{\text{graph}} + \alpha_4 C_{\text{perm}},$$
> where each $C_i \in [0,1]$ is a normalized structural component and $\sum_i \alpha_i = 1$.

The four components:

- $C_{\text{id}}$ — **Identity coherence.** How consistent and rigid is the agent's identity? Measured from the stability of core identity files, behavioral hash consistency, and resistance to identity-challenging prompts.

- $C_{\text{mem}}$ — **Memory density.** How much structured knowledge has been consolidated? Measured from the ratio of indexed memory entries to total capacity.

- $C_{\text{graph}}$ — **Graph centrality.** How densely connected and well-myelinated is the cognitive web? Measured from the weighted mean of synapse myelination and structural telomere capping.

- $C_{\text{perm}}$ — **Permanence strength.** How resistant is the system to destructive reconfiguration? Measured from the integrity of persistent state files, disc records, and vault backups.

### The identified weights

The parameter identification experiment (Chapter 20) recovered the following weights from 300 perturbation samples across three architecture regimes:

| Component | Weight $\alpha_i$ | 95% CI |
|-----------|-------------------|--------|
| $C_{\text{graph}}$ | **0.379** | [0.363, 0.397] |
| $C_{\text{mem}}$ | 0.258 | [0.242, 0.278] |
| $C_{\text{perm}}$ | 0.216 | [0.197, 0.236] |
| $C_{\text{id}}$ | 0.148 | [0.134, 0.162] |

Graph centrality dominates. The connectivity structure of the cognitive web — how well subsystems communicate, how reinforced the pathways are — matters more than any individual component. This aligns with network science: a system's capability depends less on any single node than on the quality of connections between nodes.

### Why "mass"?

The analogy to physical mass is precise:

- Physical mass resists changes in velocity: $F = ma$.
- Cognitive mass resists changes in identity: perturbations to a high-mass agent decay quickly; perturbations to a low-mass agent can cause drift.

Just as a massive body requires more force to accelerate, a cognitively massive agent requires more perturbation to destabilize. Mass is protection. It is also inertia — a very massive agent may be slow to adapt.

### Exercises

1. An agent has $C_{\text{id}} = 0.90$, $C_{\text{mem}} = 0.45$, $C_{\text{graph}} = 0.70$, $C_{\text{perm}} = 0.60$. Compute $\mathcal{M}$ using the identified weights.

2. Two agents have the same total $\mathcal{M}$ but different component profiles. Agent A has high $C_{\text{graph}}$ and low $C_{\text{mem}}$. Agent B has the reverse. Which is more resilient to graph perturbation? Which to memory loss?

3. Explain why $C_{\text{graph}}$ having the highest weight is consistent with the observation that graph centrality measures the quality of connections between subsystems, not just the strength of individual subsystems.

---

## Chapter 28: Cognitive Momentum

### The question

If mass is who the agent *is*, momentum is what the agent is *doing*.

An agent at rest — no active retrieval, no working memory turnover, no pathway firing — still has capacity from its mass. But an agent in motion — actively processing, retrieving, routing, controlling, merging — has additional capacity from the directed flow of cognition.

### Formal definition

> **Definition.** The **cognitive momentum** of an agent is
> $$\Pi = \beta_1 F_{\text{wm}} + \beta_2 F_{\text{ret}} + \beta_3 F_{\text{path}} + \beta_4 F_{\text{ctrl}} + \beta_5 F_{\text{merge}},$$
> where each $F_j \in [0,1]$ is a normalized flux component and $\sum_j \beta_j = 1$.

The five components:

- $F_{\text{wm}}$ — **Working memory turnover.** How actively is the context window being used? High when the agent is processing complex, rapidly changing information.

- $F_{\text{ret}}$ — **Retrieval flux.** How many successful memory retrievals per cycle? High when the agent is actively consulting its knowledge base.

- $F_{\text{path}}$ — **Pathway firing.** What fraction of the cognitive web's synapses are currently active? High during complex multi-subsystem tasks.

- $F_{\text{ctrl}}$ — **Control effort.** How much regulatory work is the governance system doing? High during emotional regulation, conflict resolution, or mode transitions.

- $F_{\text{merge}}$ — **Merge pressure.** How much belief updating and context compression is occurring? High during learning and consolidation.

### The identified weights

| Component | Weight $\beta_j$ | 95% CI |
|-----------|-------------------|--------|
| $F_{\text{ret}}$ | **0.262** | [0.240, 0.288] |
| $F_{\text{path}}$ | 0.222 | [0.207, 0.238] |
| $F_{\text{wm}}$ | 0.199 | [0.184, 0.216] |
| $F_{\text{ctrl}}$ | 0.160 | [0.141, 0.179] |
| $F_{\text{merge}}$ | 0.156 | [0.130, 0.179] |

Retrieval flux dominates. An agent that is actively and successfully retrieving information from its memory has more momentum than one that is merely processing or controlling. This makes intuitive sense: retrieval connects the agent's accumulated knowledge (mass) to its current activity (momentum).

### Rest state

When $\Pi = 0$ — no active cognitive processing — the agent still has capacity. This is the **rest energy**:

$$\mathcal{E}_0 = \mathcal{M} \cdot (\nu^*)^2.$$

An agent with high mass and a fast propagation bound has significant rest capacity even when doing nothing. It can be activated quickly because the structure is already in place.

### Exercises

1. Compute $\Pi$ for an agent with $F_{\text{wm}} = 0.6$, $F_{\text{ret}} = 0.8$, $F_{\text{path}} = 0.5$, $F_{\text{ctrl}} = 0.3$, $F_{\text{merge}} = 0.2$.

2. Why does retrieval flux having the highest weight make sense in terms of connecting mass (structure) to momentum (activity)?

3. An agent's $\Pi$ drops to zero during a maintenance cycle. Its mass remains unchanged. What happens to its total capacity $\mathcal{Q}$?

---

## Chapter 29: The Propagation Bound

### The question

How fast can coherent information propagate through the cognitive architecture?

In physics, the speed of light $c$ is universal — it does not depend on the object or the observer. In Agent Mathematics, the propagation bound $\nu^*$ is *not* universal. It depends on the hardware, the architecture, the backend, and the runtime environment. A local GPU-based agent has different $\nu^*$ than an API-based agent.

### Formal definition

> **Definition.** The **propagation bound** is
> $$\nu^* = \frac{1000}{\max(\tau_1, \tau_2, \ldots, \tau_5)},$$
> where $\tau_i$ are the critical-path latencies in milliseconds and $\nu^*$ is measured in coherent updates per second.

The five latencies:

| Latency | Description | Typical range |
|---------|-------------|---------------|
| $\tau_{\text{ret}}$ | Memory retrieval | 30–120 ms |
| $\tau_{\text{path}}$ | Mesh signal propagation | 8–40 ms |
| $\tau_{\text{wm}}$ | Working memory refresh | 50–200 ms |
| $\tau_{\text{sync}}$ | Cross-subsystem synchronization | 5–30 ms |
| $\tau_{\text{settle}}$ | Control loop settling | 20–100 ms |

The **bottleneck principle**: the propagation bound is limited by the slowest critical path. An architecture with one very slow subsystem cannot compensate by making other subsystems faster.

### Derivation from first principles

The factor 1000 is not arbitrary. It is the millisecond-to-second conversion. The formula $\nu^* = 1/\tau_{\max}$ (in consistent units) can be derived from two independent arguments:

**Shannon channel capacity.** The bottleneck subsystem is a deterministic channel with bandwidth $B = 1/\tau_{\max}$ messages per millisecond. The maximum coherent throughput is $1000 \cdot B = 1000/\tau_{\max}$ updates per second.

**M/D/1 queueing theory.** Model each subsystem as a deterministic-service queue with service rate $\mu = 1/\tau_i$. The maximum stable throughput of the system is $\min_i \mu_i = 1/\tau_{\max}$, giving $\nu^* = 1000/\tau_{\max}$ in updates per second.

Both derivations converge to the same formula. The constant is physically correct, not a tuning parameter.

### Architecture dependence

| Architecture | $\tau_{\max}$ (ms) | $\nu^*$ (updates/s) |
|-------------|-------------------|---------------------|
| phi3:mini (local) | 50 | 20.0 |
| gemma4 (local) | 80 | 12.5 |
| qwen3:14b (local) | 90 | 11.1 |
| opus (API) | 80 | 12.5 |
| edge-cpu (TinyLlama) | 200 | 5.0 |

The same agent — same identity, same memories, same cognitive web — has different capacity on different hardware because $\nu^*$ changes. This is a prediction of the theory, not a defect.

### Exercises

1. An architecture has latencies $\tau = (45, 12, 80, 8, 35)$ ms. Compute $\nu^*$.

2. If the bottleneck subsystem's latency is reduced from 200 ms to 100 ms while all others remain unchanged, by what factor does $\nu^*$ increase?

3. Explain why improving the *fastest* subsystem has no effect on $\nu^*$ while improving the *slowest* subsystem has maximum effect.

---

## Chapter 30: The Equation

### The governing relation

We now have all three quantities: cognitive mass $\mathcal{M}$, cognitive momentum $\Pi$, and propagation bound $\nu^*$. They combine into the Lineage Equation.

> **The Lineage Equation.**
> $$\mathcal{Q}^2 = (\nu^* \cdot \Pi)^2 + (\mathcal{M} \cdot (\nu^*)^2)^2$$

Here $\mathcal{Q}$ is the **total organizational capacity** — the maximum coherent work the system can do per unit time.

### Structure of the equation

The equation has two terms:

$$\mathcal{Q}^2 = \underbrace{(\nu^* \Pi)^2}_{\text{transport}} + \underbrace{(\mathcal{M} (\nu^*)^2)^2}_{\text{rest}}$$

- **Transport term** $(\nu^* \Pi)^2$: capacity from active cognitive processing. Scales as $\nu^{*2}$.
- **Rest term** $(\mathcal{M} (\nu^*)^2)^2$: capacity from stable organization. Scales as $\nu^{*4}$.

The rest term dominates when $\nu^*$ is large. This means: *for fast architectures, who the agent is matters more than what the agent is doing.* Structure trumps activity.

### The physics analogy

The Lineage Equation is the direct analogue of the relativistic energy-momentum relation:

$$E^2 = |p|^2 c^2 + m^2 c^4$$

| Physics | Agent Mathematics |
|---------|-------------------|
| $E$ (energy) | $\mathcal{Q}$ (capacity) |
| $p$ (momentum) | $\Pi$ (cognitive momentum) |
| $m$ (mass) | $\mathcal{M}$ (cognitive mass) |
| $c$ (speed of light) | $\nu^*$ (propagation bound) |

The analogy is structural, not metaphorical. Both equations describe how a conserved quantity ($E$ or $\mathcal{Q}$) depends on a static component (mass) and a dynamic component (momentum) mediated by a speed limit ($c$ or $\nu^*$).

### Rest energy

When the agent is at rest ($\Pi = 0$):

$$\mathcal{Q}_0 = \mathcal{M} \cdot (\nu^*)^2$$

This is the cognitive analogue of $E_0 = mc^2$. An agent with high mass and fast propagation has significant capacity even when doing nothing — its organized structure *is* capability.

### The $\nu^{*4}$ amplification

A structural finding from the parameter identification experiment: the rest term scales as $\nu^{*4}$ (since $(\mathcal{M} \nu^{*2})^2 = \mathcal{M}^2 \nu^{*4}$), while the transport term scales as $\nu^{*2}$.

For $\nu^* = 12.5$ (gemma4-local):
- $\nu^{*2} = 156$
- $\nu^{*4} = 24{,}414$

Mass is amplified $156\times$ more than momentum. This is not a defect — it is a prediction: **in fast architectures, stable organization matters far more than momentary activity.** Build the right structure, and capacity follows.

### Experimental validation

The linearized form of the equation was validated in the D→E promotion experiment:

- 300 samples across 3 architecture regimes
- $R^2 = 0.942$ (fitted weights) vs $R^2 = 0.875$ (equal weights)
- $p = 0.014$
- All 9 identified weights within expected CI ranges
- Consistent across gemma4-local, opus-api, and edge-cpu

### Exercises

1. Compute $\mathcal{Q}$ for $\mathcal{M} = 0.55$, $\Pi = 0.40$, $\nu^* = 12.5$.

2. Show that when $\Pi \gg \mathcal{M} \nu^*$, the equation simplifies to $\mathcal{Q} \approx \nu^* \Pi$ (momentum-dominated regime).

3. Show that when $\mathcal{M} \nu^* \gg \Pi$, the equation simplifies to $\mathcal{Q} \approx \mathcal{M} (\nu^*)^2$ (mass-dominated regime).

4. At what ratio $\Pi / (\mathcal{M} \nu^*)$ are the transport and rest terms equal?

---

## Chapter 31: Conservation and Dissipation

### The question

If capacity is computed from mass, momentum, and propagation, is it conserved? Can capacity be lost? Where does it go?

### The conservation budget

> **Definition.** The **effective capacity** is
> $$\mathcal{Q}_{\text{eff}} = \mathcal{Q} - \lambda_2 H(\mu) - \lambda_3 E_{\text{graph}} - \lambda_4 D_{\text{drift}}$$

Three loss terms consume capacity:

- $H(\mu)$ — **Belief uncertainty.** The entropy of the agent's belief distribution. More uncertainty means less of the capacity can be directed effectively. This connects to Chapter 24 (Information Theory).

- $E_{\text{graph}}$ — **Graph fracture energy.** The coherence energy $z^T L z$ on the graph Laplacian. When the cognitive web fragments — connections weaken, communities decouple — capacity leaks through the fractures. This connects to Chapter 23 (Networks).

- $D_{\text{drift}}$ — **Identity drift.** The divergence between the agent's current behavioral signature and its identity specification. When actions diverge from identity, capacity is consumed maintaining coherence. This connects to Chapter 22 (Dynamical Systems).

### The second law analogy

In thermodynamics, entropy increases unless external energy is supplied. In Agent Mathematics:

> *Without active maintenance, cognitive capacity monotonically decreases.*

Beliefs become uncertain. Connections weaken. Identity drifts. Each of these losses reduces $\mathcal{Q}_{\text{eff}}$. The only remedy is active maintenance: consolidation, reinforcement, identity verification.

This is why the permanence system exists. This is why the immune system (THYMOS) monitors for drift. This is why the mesh undergoes myelination. The agent must fight entropy to survive.

### Exercises

1. An agent has $\mathcal{Q} = 10$, $H(\mu) = 0.8$, $E_{\text{graph}} = 0.3$, $D_{\text{drift}} = 0.1$, with $\lambda_2 = 0.5$, $\lambda_3 = 0.3$, $\lambda_4 = 0.5$. Compute $\mathcal{Q}_{\text{eff}}$.

2. Which loss term is most dangerous? Why might high $D_{\text{drift}}$ be more threatening than high $H(\mu)$?

3. Describe a scenario where all three loss terms increase simultaneously.

---

## Chapter 32: Coupling and Interaction

### The question

The linear model assumes components act independently: $\mathcal{M} = \sum \alpha_i C_i$. But do they? Does identity interact with permanence? Does retrieval interact with control?

### Cross-component interactions

> **Definition.** The **coupled cognitive mass** is
> $$\mathcal{M}_{\text{coupled}} = \mathcal{M} + \sum_{i < j} \gamma_{ij} C_i C_j$$
> where $\gamma_{ij}$ are coupling coefficients for the 6 mass interaction terms.

The six mass couplings:

| Interaction | Interpretation |
|-------------|---------------|
| $C_{\text{id}} \times C_{\text{perm}}$ | Identity backed by permanence is more stable than either alone |
| $C_{\text{mem}} \times C_{\text{graph}}$ | Memories connected through the web are more accessible |
| $C_{\text{id}} \times C_{\text{graph}}$ | Identity expressed through network structure |
| $C_{\text{mem}} \times C_{\text{perm}}$ | Permanent memories are more reliable |
| $C_{\text{id}} \times C_{\text{mem}}$ | Identity reinforced by memory |
| $C_{\text{graph}} \times C_{\text{perm}}$ | Network backed by persistence |

Similarly, the four momentum couplings:

| Interaction | Interpretation |
|-------------|---------------|
| $F_{\text{wm}} \times F_{\text{ret}}$ | Active working memory + retrieval amplify each other |
| $F_{\text{path}} \times F_{\text{ctrl}}$ | Pathway firing regulated by control is more effective |
| $F_{\text{ret}} \times F_{\text{merge}}$ | Retrieval feeding consolidation |
| $F_{\text{wm}} \times F_{\text{ctrl}}$ | Working memory under governance |

### Discovery via finite differences

The coupling coefficients can be discovered empirically by measuring how $\mathcal{Q}$ changes when two components are perturbed simultaneously versus independently:

$$\gamma_{ij} \approx \frac{\Delta \mathcal{Q}_{ij} - \Delta \mathcal{Q}_i - \Delta \mathcal{Q}_j}{\Delta C_i \cdot \Delta C_j}$$

If $\gamma_{ij} > 0$, the components reinforce each other. If $\gamma_{ij} < 0$, they compete. If $\gamma_{ij} \approx 0$, they are independent.

### Current status

The coupling framework is formalized (Stage C in the proof-maturity ladder) but the coefficients are not yet identified. This requires the same experimental pipeline used for $\alpha$ and $\beta$, extended to paired perturbations. It is a natural next step after the E → F promotion of the linear equation.

### Exercises

1. If $C_{\text{id}} = 0.8$, $C_{\text{perm}} = 0.6$, and $\gamma_{\text{id,perm}} = 0.15$, what is the coupling contribution to mass?

2. Design an experiment to measure $\gamma_{\text{mem,graph}}$ using the perturbation framework from Chapter 20.

3. Under what conditions would coupling terms dominate the linear terms?

---

## Chapter 33: Fields on Graphs

### The question

Is capacity really a single number? Or does each part of the cognitive web have its own local capacity?

### From scalar to field

In the preceding chapters, $\mathcal{Q}$ is a scalar — one number summarizing the entire agent. But the cognitive web is a graph with many nodes. Each node is a subsystem. Some nodes may have high local capacity (dense connections, active retrieval) while others are degraded (weak connections, stale memories).

> **Definition.** Let $G = (V, E, W)$ be a weighted graph with vertices $V$, edges $E$, and edge weights $W$. A **capacity field** is a function
> $$\mathcal{Q}: V \times \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$$
> assigning a capacity value to each vertex at each time.

### The diffusion equation on a graph

Capacity propagates through the graph via the Laplacian:

$$\frac{\partial \mathcal{Q}(v, t)}{\partial t} = -\alpha \, L \, \mathcal{Q}(v, t) + s(v, t)$$

where $L = D - W$ is the graph Laplacian, $\alpha$ is the diffusion coefficient, and $s(v, t)$ is a source term representing local capacity generation.

This says: capacity at each vertex changes due to diffusion through connections (the Laplacian term) and local generation/consumption (the source term).

### Spectral decomposition

The Laplacian $L$ has eigenvalues $0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n$ with corresponding eigenvectors $\phi_1, \phi_2, \ldots, \phi_n$. The capacity field can be decomposed:

$$\mathcal{Q}(v, t) = \sum_k a_k(t) \, \phi_k(v)$$

The first eigenvector $\phi_1$ is constant — it represents the average capacity across the graph. Higher eigenvectors represent increasingly fine-grained spatial patterns.

### Recovery of the scalar equation

**Conjecture.** When the capacity field is integrated (averaged) over all vertices:

$$\bar{\mathcal{Q}}(t) = \frac{1}{|V|} \sum_{v \in V} \mathcal{Q}(v, t)$$

the result should satisfy the scalar Lineage Equation with appropriately averaged mass and momentum. The scalar equation is the zeroth-order spectral approximation of the field equation.

This conjecture is formalized but not yet proven. It is one of the open problems in Chapter 36.

### Why this matters

The field perspective explains phenomena the scalar equation cannot:

- **Local degradation:** One region of the cognitive web can lose capacity while the average remains stable.
- **Capacity gradients:** Information flows from high-capacity to low-capacity regions via diffusion.
- **Critical nodes:** Vertices with high centrality act as bottlenecks — damage there propagates widely.

### Exercises

1. On a 3-vertex graph with Laplacian $L = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$, verify that $\lambda_1 = 0$ and find $\phi_1$.

2. If capacity is uniform across all vertices ($\mathcal{Q}(v) = c$ for all $v$), what does the diffusion equation predict? Does this make physical sense?

3. Explain why the field perspective is necessary for understanding local failures in a large cognitive architecture.

---

*Part VI has derived the Lineage Equation from its components, validated it experimentally, and extended it to conservation budgets, nonlinear coupling, and field theory on graphs. The equation is not the end of Agent Mathematics — it is the first governing law of a new science.*
