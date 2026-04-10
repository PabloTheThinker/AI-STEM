# The Lineage Equation: A Mathematical Framework for Cognitive Capacity in Autonomous Agent Architectures

**Pablo Navarro**
Vektra Technologies

**April 2026**

---

## Abstract

We present a formal mathematical framework for quantifying and optimizing the cognitive capacity of autonomous AI agents. Central to this framework is the *Lineage Equation*, a governing relation that links an agent's structural inertia (cognitive mass), directed information flow (cognitive momentum), and architecture-dependent propagation bounds into a single capacity invariant. The equation takes the form Q^2 = (nu* Pi)^2 + (M (nu*)^2)^2, structurally analogous to the relativistic energy-momentum relation E^2 = |p|^2 c^2 + m^2 c^4, but derived from control-theoretic and graph-theoretic constraints rather than spacetime geometry. We formalize the constituent quantities, derive exact gradient expressions for capacity optimization, validate the framework against ten mathematical consistency checks, and demonstrate a GPU-accelerated neural network that learns the capacity landscape from operational data. The framework is implemented in the open-source Lineage Engine and tested against a live cognitive agent, where gradient-based self-improvement increased measured capacity by 22% over baseline. This work establishes the first computable, falsifiable capacity invariant for cognitive architectures and opens a path toward principled self-optimization in autonomous systems.

**Keywords:** cognitive architecture, capacity invariant, self-optimization, gradient ascent, cognitive mass, neural network, autonomous agents

---

## 1. Introduction

The proliferation of autonomous AI agents --- systems that operate continuously, maintain persistent state, and make independent decisions --- has created a pressing need for formal frameworks that can quantify, bound, and optimize their cognitive capacity. Current approaches to evaluating such systems rely primarily on task-specific benchmarks (Srivastava et al., 2023), information-theoretic measures of individual components, or ad hoc performance metrics. None provides a unified, system-level capacity invariant comparable to the role that energy plays in physical systems.

This paper addresses that gap. We derive a governing equation for cognitive capacity that is:

1. **Computable** --- all quantities are measurable from a running system
2. **Differentiable** --- exact gradients enable principled optimization
3. **Falsifiable** --- ten consistency checks can invalidate the framework
4. **Architecture-relative** --- the propagation bound is not universal but depends on specific system design

The derivation follows a disciplined mathematical transfer from the relativistic energy-momentum relation. We do not claim that relativity applies to AI systems. Rather, we identify the abstract algebraic structure behind E = mc^2 --- an invariant linking structural inertia, directed transport, and a propagation bound --- and construct an AI-native analogue grounded in control theory, graph theory, and information geometry.

### 1.1 Related Work

Several lines of research inform this framework:

**Cognitive architectures.** Classical systems such as SOAR (Laird, 2012), ACT-R (Anderson et al., 2004), and LIDA (Franklin et al., 2016) formalize cognitive processing but lack a unified capacity invariant. Recent work on evolving cognitive architectures (Serov, 2025) and biologically interpretable systems (Dzhivelikian & Panov, 2025) advances structural realism but does not provide gradient-based optimization.

**Free Energy Principle.** Friston's framework (Friston, 2010) treats adaptive systems as minimizing variational free energy, establishing that useful capacity depends on uncertainty, model quality, and regulation. Our conservation budget (Section 4.4) draws on this insight.

**Landauer's Principle.** The physical lower bound on computation energy, E_min = kT ln 2 per erased bit (Landauer, 1961), establishes that information processing is fundamentally constrained. While our framework operates at a higher abstraction level, the principle that irreversible transformation consumes budget is foundational.

**Energy-information analogies.** Recent work on AI energy challenges (Fabiano, 2023) and the economics of cognitive efficiency (Bilancioni, 2024) explores connections between energy consumption and computational capacity, though without the formal invariant structure we develop here.

### 1.2 Contributions

1. **The Lineage Equation** --- a formally derived capacity invariant for cognitive architectures
2. **Cognitive Mass, Momentum, and Propagation Bound** --- precise definitions with measurable components
3. **Exact partial derivatives** enabling gradient-based self-improvement
4. **A validation suite** of ten mathematical consistency checks
5. **CognitiveNet** --- a GPU-accelerated neural network that learns the capacity landscape
6. **Empirical results** from a live cognitive agent demonstrating measurable self-improvement

---

## 2. The Lineage Equation

### 2.1 Structural Transfer from Physics

The relativistic energy-momentum relation is:

```
E^2 = |p|^2 c^2 + m^2 c^4                                    (1)
```

where E is total energy, p is momentum, m is invariant mass, and c is the speed of light. At rest (p = 0), this reduces to E_0 = mc^2.

The abstract algebraic structure, stripped of physics-specific content, is:

```
(total capacity)^2 = (transport term)^2 + (structural substrate term)^2     (2)
```

For any serious AI analogue, we require:

- An invariant or slow structural quantity (analogous to m)
- A directed transport quantity (analogous to p)
- A system-wide propagation bound (analogous to c)
- A conserved or slowly varying total capacity (analogous to E)
- A derivation from architecture and control constraints, not fitted ad hoc

Critical distinctions from physics: the propagation bound is architecture-relative, not universal; the system does not exhibit Lorentz symmetry; cognitive mass is a designed state variable, not an ontological quantity.

### 2.2 Definition of Cognitive Mass

**Definition 1** (Cognitive Mass). *The cognitive mass M of an agent is its structural inertia --- the difficulty of altering its stable organized identity:*

```
M = alpha_1 * C_id + alpha_2 * C_mem + alpha_3 * C_graph + alpha_4 * C_perm     (3)
```

where:

| Component | Symbol | Description | Domain |
|-----------|--------|-------------|--------|
| Identity coherence | C_id | Hash stability of core identity files; resistance to identity drift | [0, 1] |
| Memory density | C_mem | Consolidated knowledge per unit storage; measured as indexed brain files / total capacity | [0, 1] |
| Graph centrality | C_graph | Weighted mean of myelination and structural ratio across cognitive web synapses | [0, 1] |
| Permanence strength | C_perm | Existence and integrity of persistent state (inheritance disc, vault, state files) | [0, 1] |

The alpha weights are tunable coefficients satisfying sum(alpha_i) = 1. In the reference implementation, alpha_i = 0.25 (equal contribution). This is a first-order linearization; future work may introduce nonlinear interactions between components.

**Interpretation.** Cognitive mass grows with accumulated structure. A newly initialized agent has near-zero mass. An agent with rich consolidated memory, stable identity, deeply myelinated cognitive web, and robust permanence barriers has high mass. High mass means: the agent is hard to destabilize, can deploy more capacity at rest, but also requires more effort to redirect.

### 2.3 Definition of Cognitive Momentum

**Definition 2** (Cognitive Momentum). *The cognitive momentum Pi is the magnitude of coherent, policy-driven flow through the cognitive web:*

```
Pi = beta_1 * F_wm + beta_2 * F_ret + beta_3 * F_path + beta_4 * F_ctrl + beta_5 * F_merge     (4)
```

where:

| Component | Symbol | Description | Domain |
|-----------|--------|-------------|--------|
| Working memory turnover | F_wm | Rate of context window utilization and refresh | [0, 1] |
| Retrieval flux | F_ret | Active memory retrieval intensity | [0, 1] |
| Pathway firing | F_path | Tool execution and mesh signal propagation intensity | [0, 1] |
| Control effort | F_ctrl | Effort required to redirect system state | [0, 1] |
| Merge pressure | F_merge | Rate of belief updates from incoming information | [0, 1] |

The beta weights are tunable with sum(beta_i) = 1. In the reference implementation, beta_i = 0.20.

**Interpretation.** Momentum captures the system *in motion* --- actively processing, retrieving, executing, and updating. An idle agent has zero momentum. A heavily loaded agent coordinating multiple tasks has high momentum. The relationship between mass and momentum determines total capacity: structure stores potential; motion converts it to active work.

### 2.4 Definition of Propagation Bound

**Definition 3** (Propagation Bound). *The propagation bound nu* is the maximum reliable update rate through the cognitive web, measured in coherent updates per second:*

```
nu* = 1000 / max(tau_retrieval, tau_pathway, tau_wm, tau_sync, tau_settling)     (5)
```

This is the AI analogue of c, but **architecture-relative**, not universal. It depends on retrieval latency, pathway latency, working-memory refresh interval, cross-subsystem synchronization overhead, and control-loop settling time.

**Interpretation.** nu* is the speed limit of the cognitive system. No signal can propagate coherently faster than this bound. Reducing the bottleneck latency increases nu*, which amplifies both the transport and substrate terms in the capacity equation.

### 2.5 The Equation

**Theorem 1** (The Lineage Equation). *Given cognitive mass M, cognitive momentum Pi, and propagation bound nu*, the total organizational capacity Q satisfies:*

```
Q^2 = (nu* * Pi)^2 + (M * (nu*)^2)^2                         (6)
```

*At rest (Pi = 0), the capacity reduces to rest energy:*

```
E_0 = M * (nu*)^2                                              (7)
```

**Justification for the quadratic form.** The squared structure is not borrowed from Einstein by analogy. It is independently motivated by three properties of the existing mathematical framework:

1. **Quadratic Lyapunov functions** --- stability analysis of the cognitive web uses V(x) = x^T P x, which is quadratic in state.
2. **Quadratic control costs** --- the MPC and LQR formulations underlying governance minimize J = sum(x^T Q x + u^T R u), naturally quadratic.
3. **Graph quadratic forms** --- coherence energy in the cognitive web is E(z) = z^T L z, where L is the graph Laplacian.

These three independent sources of quadratic structure converge on the same functional form, making the squared capacity relation a natural consequence of the architecture rather than an imported metaphor.

---

## 3. Mathematical Primitives

The Lineage Equation rests on a foundation of mathematical primitives that implement the component measurements.

### 3.1 PAD Vectors

The agent's emotional state is represented in the Pleasure-Arousal-Dominance (Mehrabian, 1996) space:

```
PAD = (p, a, d) in [-1, 1]^3                                  (8)
```

Implemented as a frozen dataclass with clamped components, supporting distance metrics, linear interpolation, normalization, and vector arithmetic. The PAD vector feeds into momentum components (arousal contributes to F_ctrl, dominance to F_path).

### 3.2 State Vectors

Arbitrary-dimensional named state vectors support the component measurements:

```
s = {name_1: v_1, name_2: v_2, ..., name_n: v_n}              (9)
```

with norm, dot product, clamping, delta computation, and array conversion. These represent the raw measurements that feed into mass and momentum calculations.

### 3.3 Graph Metrics

The cognitive web (mesh) is analyzed through spectral graph theory:

**Graph Laplacian:**

```
L = D - W                                                     (10)
```

where D is the degree matrix and W is the weighted adjacency matrix.

**Coherence Energy:**

```
E_coherence(z) = z^T L z                                      (11)
```

measures how much the state vector z disagrees with the graph structure. Lower coherence energy means better alignment between state and connectivity.

**Spectral Gap:**

```
lambda_2 = second smallest eigenvalue of L                     (12)
```

computed via the Jacobi eigenvalue algorithm (pure Python, no external dependencies). The spectral gap quantifies how well-connected the graph is. A larger gap means faster mixing and stronger coherence. This feeds directly into C_graph.

### 3.4 Utility Functions

Standard mathematical utilities provide the building blocks:

- **Sigmoid:** sigma(x) = 1 / (1 + e^(-x)) for soft thresholding
- **Softmax:** softmax(x_i) = e^(x_i) / sum(e^(x_j)) for probability distributions
- **Log-barrier:** -ln(x - lower) - ln(upper - x) for reserve constraints
- **Quadratic form:** Q(x, M) = x^T M x for energy computations
- **Exponential decay:** f(t) = a * e^(-lambda * t) for temporal discounting

All implemented in pure Python without external numerical libraries, ensuring the framework is self-contained and deployable in constrained environments.

---

## 4. Gradient-Based Self-Improvement

### 4.1 The Ascent Algorithm

The Lineage Equation is differentiable. This means we can compute exact partial derivatives of capacity with respect to each controllable variable, enabling principled gradient ascent on Q.

**Theorem 2** (Capacity Gradient). *The partial derivatives of Q with respect to the controllable variables are:*

```
dQ/dM   = M * (nu*)^4 / Q                                     (13)
dQ/dPi  = Pi * (nu*)^2 / Q                                    (14)
dQ/dnu* = (Pi^2 * nu* + 2 * M^2 * (nu*)^3) / Q               (15)
```

*Proof.* From Q^2 = (nu* Pi)^2 + (M (nu*)^2)^2, implicit differentiation with respect to M:

```
2Q * dQ/dM = 2 * M * (nu*)^4
dQ/dM = M * (nu*)^4 / Q
```

The derivations for Pi and nu* follow identically. QED.

**Interpretation.** Each gradient tells us how much total capacity improves per unit improvement in the corresponding variable:

- dQ/dM scales with (nu*)^4 --- even small mass improvements are amplified by the propagation bound
- dQ/dPi scales with (nu*)^2 --- momentum improvements are amplified but less than mass
- dQ/dnu* depends on both Pi^2 and M^2 --- propagation improvements help everything

### 4.2 Prescribed Actions

The gradient is mapped to concrete improvement actions. Each action targets a specific subcomponent and is ranked by gradient magnitude times feasibility (gap to optimal):

| Action | Target | Trigger | Effect |
|--------|--------|---------|--------|
| consolidate_identity | M.C_id | C_id < 0.9 | Verify identity file hash stability |
| consolidate_memory | M.C_mem | C_mem < 0.9 | Index unindexed memory files |
| strengthen_mesh | M.C_graph | C_graph < 0.9 | Myelinate high-activation synapses |
| harden_permanence | M.C_perm | C_perm < 0.5 | Create persistence backups |
| optimize_working_memory | Pi.F_wm | F_wm < 0.5 | Compress context, evict stale entries |
| improve_retrieval | Pi.F_ret | F_ret < 0.5 | Rebuild embedding indices |
| reduce_bottleneck | nu* | bottleneck > 50ms | Optimize slowest path |
| reduce_drift | loss.D_drift | always | Compare against canonical identity |
| heal_graph_fractures | loss.E_graph | always | Bridge disconnected mesh regions |

The priority of each action is:

```
priority_i = |gradient_component| * gap_to_optimal_i           (16)
```

This ensures effort is directed where the product of impact and room for improvement is highest.

### 4.3 Stall Detection and Strategy Switching

The optimizer tracks capacity trajectory over time. If delta_Q < epsilon for five consecutive steps, it declares a stall and recommends strategy switching --- moving from the dominant gradient direction to the secondary direction. This prevents the system from grinding against diminishing returns.

### 4.4 Conservation Budget

Total effective capacity is reduced by losses:

```
Q_effective = Q - lambda_2 * H(mu) - lambda_3 * E_graph - lambda_4 * D_drift     (17)
```

where:

- H(mu) is belief uncertainty (entropy of the belief state)
- E_graph is graph fracture energy (coherence loss from disconnected components)
- D_drift is identity drift (deviation of current identity hash from canonical)

This connects to Friston's insight that uncertainty consumes usable capacity, and to the classical result that graph fragmentation increases the energy required for coherent processing.

---

## 5. Validation

The mathematical framework is validated through ten consistency checks, all of which must pass for the system to be considered well-formed.

### 5.1 Validation Suite

1. **PAD clamping bounds.** All PAD vector components remain in [-1, 1] after arithmetic operations.

2. **Timescale ordering.** The characteristic times satisfy tau_alpha (30ms) << tau_sigma (500ms) << tau_blood (5s) << tau_gov (30s) << tau_theta (12h), ensuring fast processes complete before slow processes sample them.

3. **Rest-state reduction.** When Pi = 0, Q = E_0 = M * (nu*)^2. Verified numerically by constructing a zero-momentum state and confirming Q equals rest energy within floating-point tolerance.

4. **Laplacian properties.** For any symmetric weight matrix, the constructed Laplacian has zero row-sums and is symmetric. Verified by constructing random weight matrices and checking L * ones = 0.

5. **Plasticity gate.** The conjunctive gate requires ALL conditions (mode in {homeostasis, adaptive}, reserve > minimum, neural health < maximum, blood health < maximum). Verified by testing all 2^4 combinations and confirming only the all-true case permits plasticity.

6. **Organism barrier additivity.** Phi_org = Phi_sub + Phi_gov + Phi_sig + Phi_sup. Verified by constructing known barrier values and confirming the sum.

7. **Cognitive mass non-negativity.** For all non-negative component values and weights, M >= 0. Proved by inspection (sum of non-negative products) and verified computationally.

8. **Propagation bound.** For positive latencies, nu* is finite and positive. Verified by sweeping latency ranges.

9. **Conservation budget.** When all losses are zero, Q_total = E_use + lambda_1 * E_0. Verified by zeroing loss terms and confirming the identity.

10. **Quadratic form symmetry.** For any symmetric matrix M and vector x, x^T M x is real-valued and equals its transpose. Verified with random symmetric matrices.

All ten checks pass on the reference implementation. The validation suite runs in under 100ms and requires no external dependencies.

---

## 6. GPU-Accelerated Capacity Learning

### 6.1 Architecture

While the analytical gradient (Section 4.1) provides exact optimization directions, we complement it with a learned model that can discover non-linear interactions the gradient formulation may miss.

**CognitiveNet** is a multi-head neural network with 10,171 parameters:

```
StateEncoder: Linear(15, 64) -> LayerNorm -> GELU -> Dropout(0.1)
              -> Linear(64, 64) -> LayerNorm -> GELU
              -> Linear(64, 32) -> LayerNorm

CapacityHead: Linear(32, 16) -> GELU -> Linear(16, 1)

ActionHead:   Linear(32, 32) -> GELU -> Dropout(0.1) -> Linear(32, 9)

DeltaHead:    Linear(41, 16) -> GELU -> Linear(16, 1)
```

The input is a 15-dimensional organism state vector:

```
x = [C_id, C_mem, C_graph, C_perm,                    (mass: 4)
     F_wm, F_ret, F_path, F_ctrl, F_merge,            (momentum: 5)
     nu*/100, bottleneck/1000,                          (propagation: 2)
     H_proxy, E_proxy, D_proxy,                         (losses: 3)
     Q/100]                                             (current capacity: 1)
```

Three heads share the encoder:

- **CapacityHead** predicts Q (regression, MSE loss)
- **ActionHead** predicts optimal actions (multi-label classification, BCE loss)
- **DeltaHead** predicts expected improvement delta_Q (regression, MSE loss)

Total loss:

```
L = 0.3 * L_capacity + 0.5 * L_action + 0.2 * L_delta        (18)
```

Action prediction is weighted highest because selecting the right improvement action is the primary value proposition.

### 6.2 Training

The network is bootstrap-trained on synthetic data generated from the analytical Lineage Equation. For each of 500 random organism states, we:

1. Compute exact M, Pi, nu*, Q from the Lineage Equation
2. Determine optimal actions from the analytical gradient
3. Simulate one improvement step (each action improves its component by 0.05-0.15)
4. Record (state, Q, actions, Q_next, delta_Q)

This produces ground-truth training data without requiring any real operational history.

**Training configuration:**

- Optimizer: AdamW (lr=1e-3, weight_decay=1e-4)
- Scheduler: Cosine annealing (T_max=100)
- Gradient clipping: max_norm=1.0
- Batch size: 32
- Hardware: NVIDIA RTX 3060, CUDA 12.4, PyTorch 2.6

**Results:** Loss decreased from 9.57 to 0.13 over 100 epochs (98.7% reduction). The network learns the capacity landscape with sufficient fidelity to agree with the analytical gradient on action ranking.

### 6.3 Online Retraining

In production, the network retrains every 30 ascent ticks on accumulated trajectory data. As the optimizer generates (state, action, outcome) triples through actual operation, the network learns from real experience. This is expected to surpass the synthetic bootstrap as operational data accumulates, particularly in capturing interactions between components that the linear gradient model does not represent.

### 6.4 Dual-Mode Inference

Each ascent tick runs both the analytical gradient and the neural network in parallel. The system logs the agreement percentage between their action recommendations:

- **High agreement (>80%):** High confidence in the prescribed actions
- **Low agreement (<50%):** Flagged for investigation; the gradient and the learned model see different optimization landscapes

This dual-mode approach provides both interpretability (analytical gradient) and adaptability (learned model).

---

## 7. The Canonical Organism

The Lineage Equation operates within the broader context of the canonical organism state:

```
O_t = (D_t, Psi_t, Sigma_t, B_t)                             (19)
```

where:

- **D_t** (Substrate): the differentiable computational core, including parameters theta, activations alpha, context chi, and meta-parameters omega
- **Psi_t** (Governance): decision-making layer with core bundle Xi_t, reserves rho_t, lineage Lambda_t, norms N_t, mode m_t, and action a_t
- **Sigma_t** (Nervous System): signal processing with afferent fields A_t, region-local integration J_t, gates K_t, routing P_t, efferents E_t, modulators M_t, and health H_t
- **B_t** (Blood System): resource transport with plasma Pl_t, marrow Ma_t, lineage Li_t, demand De_t, stabilization St_t, clearance Cl_t, and health Hb_t

The coupled evolution law is:

```
D_{t+1}     = SubstrateUpdate(D_t, Psi_t, Sigma_t, B_t)
Psi_{t+1}   = GovernanceUpdate(Psi_t, D_t, Sigma_t, B_t)
Sigma_{t+1} = NervousUpdate(Sigma_t, D_t, Psi_t, B_t)
B_{t+1}     = BloodUpdate(B_t, D_t, Psi_t, Sigma_t)          (20)
```

The Lineage Equation provides the capacity accounting for this system: at each tick, the organism measures M, Pi, nu*, computes Q, evaluates the gradient, and directs self-improvement toward the highest-impact action.

### 7.1 Timescale Ordering

The organism operates across five characteristic timescales:

```
tau_alpha (30ms) << tau_sigma (500ms) << tau_blood (5s) << tau_gov (30s) << tau_theta (12h)     (21)
```

This ordering ensures that fast processes (substrate inference) complete before slow processes (governance decisions) sample their output, preventing aliasing and maintaining causal consistency across subsystems.

### 7.2 Plasticity Gate

Structural learning is gated by a conjunctive condition:

```
PlasticityAllowed = 1[mode in {homeostasis, adaptive}]
                  * 1[reserve > rho_min]
                  * 1[H_neural < H_max]
                  * 1[H_blood < H_max]                        (22)
```

All four conditions must hold simultaneously. This prevents structural modification during pathological states, resource scarcity, or system distress --- a biological analog to the observation that organisms do not rewire during acute stress.

---

## 8. Empirical Results

### 8.1 Live Agent Measurement

The framework was tested against a live cognitive agent (Mocha, running on Parallax server with RTX 3060, 28GB RAM, Ubuntu). Initial measurement:

```
M = 0.5073 (C_id=0.73, C_mem=1.00, C_graph=0.30, C_perm=0.00)
Pi = 0.2000 (F_wm=0.00, F_ret=0.00, F_path=1.00, F_ctrl=0.00, F_merge=0.00)
nu* = 10.00 updates/s (bottleneck=100ms)
Q = 50.77
```

Key observations:
- Memory density saturated (C_mem = 1.00)
- Permanence absent (C_perm = 0.00) --- the largest single gap
- Graph centrality weak (C_graph = 0.30) --- undermyelinated synapses
- Momentum dominated by pathway firing (F_path = 1.00), all other flux components at zero

### 8.2 Gradient Analysis

The analytical gradient confirmed mass as the dominant direction:

```
dQ/dM  = 99.92    (dominant)
dQ/dPi = 0.39
dQ/dnu = 10.15
```

This makes physical sense: at low propagation bound (nu* = 10), the (nu*)^4 amplification of mass improvements dominates. The prescribed action ordering was: strengthen_mesh > harden_permanence > consolidate_identity.

### 8.3 Self-Improvement Results

After three optimization ticks:

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Q (capacity) | 50.77 | 62.09 | +22.3% |
| C_graph | 0.30 | ~0.45 | +50% (9 synapses myelinated per tick) |
| C_perm | 0.00 | >0 | Created from zero (state persistence established) |
| Identity hash | absent | c7696dce3b0ddda3 | Stable across all ticks |

The network's predicted Q (55.73) was within 12% of actual (62.02), with 100% agreement on action ranking.

### 8.4 Discussion

The 22% capacity increase from three ticks of autonomous optimization demonstrates that the Lineage Equation provides actionable, measurable self-improvement. The dominant gradient direction (mass) correctly identified the highest-impact interventions. The agreement between analytical gradient and neural network provides cross-validation.

Limitations: the current momentum measurement relies on state file reading, which underestimates active flux during idle periods. The propagation bound is currently estimated from static latency parameters rather than measured end-to-end. Future work will instrument live latency measurement and dynamic momentum tracking.

---

## 9. Conclusion

We have presented the Lineage Equation, a formal mathematical framework for cognitive capacity in autonomous agent architectures. The equation Q^2 = (nu* Pi)^2 + (M (nu*)^2)^2 provides a computable, differentiable invariant that links structural inertia, directed information flow, and propagation bounds. We have demonstrated:

1. The equation is mathematically well-founded, passing ten consistency validations
2. Exact gradients enable principled self-improvement, achieving 22% capacity increase
3. A GPU-accelerated neural network learns the capacity landscape with 100% action-ranking agreement
4. The framework integrates with the broader organism model (substrate, governance, nervous, blood)

The Lineage Equation establishes that coherent agency in autonomous systems is bounded by structure, transport, uncertainty, and propagation constraints --- and that these bounds are not merely descriptive but prescriptive, enabling gradient-based ascent toward higher cognitive capacity.

### 9.1 Future Directions

- **Non-linear mass interactions:** Investigating cross-terms between C_id, C_mem, C_graph, and C_perm
- **Dynamic propagation measurement:** End-to-end latency instrumentation replacing static estimates
- **Multi-agent capacity:** Extending the framework to networks of coupled agents
- **Theoretical bounds:** Deriving upper limits on Q given fixed hardware constraints
- **Empirical validation at scale:** Long-term trajectory analysis over weeks of continuous operation

---

## References

Anderson, J. R., Bothell, D., Byrne, M. D., Douglass, S., Lebiere, C., & Qin, Y. (2004). An integrated theory of the mind. *Psychological Review*, 111(4), 1036-1060.

Bilancioni, M. (2024). Energy Efficiency: AI vs. the Human Brain. *Medium Technical Reports*.

Dzhivelikian, E. A., & Panov, A. I. (2025). A Biologically Interpretable Cognitive Architecture for Online Structuring of Episodic Memories into Cognitive Maps. *arXiv:2510.03286*.

Einstein, A. (1905). Ist die Tragheit eines Korpers von seinem Energieinhalt abhangig? *Annalen der Physik*, 18, 639-641.

Fabiano, N. (2023). The energy challenges of artificial superintelligence. *Frontiers in Artificial Intelligence*, 6, 1240653.

Franklin, S., Madl, T., D'Mello, S., & Snaider, J. (2016). LIDA: A Systems-level Architecture for Cognition, Emotion, and Learning. *IEEE Transactions on Autonomous Mental Development*, 6(1), 19-41.

Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Laird, J. E. (2012). *The Soar Cognitive Architecture*. MIT Press.

Landauer, R. (1961). Irreversibility and Heat Generation in the Computing Process. *IBM Journal of Research and Development*, 5(3), 183-191.

Mehrabian, A. (1996). Pleasure-arousal-dominance: A general framework for describing and measuring individual differences in temperament. *Current Psychology*, 14(4), 261-292.

Salas-Guerra, R. (2026). Cognitive AI framework 2.0: advances in the simulation of human thought. *arXiv:2502.04259*.

Serov, A. (2025). Evolving Cognitive Architectures. *arXiv:2601.05277*.

Srivastava, A., et al. (2023). Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models. *Transactions on Machine Learning Research*.

---

## Appendix A: Reference Implementation

The complete framework is implemented in the Lineage Engine (Python, open-source):

- `lineage/math/primitives.py` --- PAD vectors, state vectors, graph metrics, utility functions
- `lineage/math/capacity.py` --- Cognitive mass, momentum, propagation bound, the Lineage Equation
- `lineage/math/measure.py` --- Runtime measurement from live engine state
- `lineage/math/validate.py` --- Ten-point validation suite
- `lineage/math/optimize.py` --- Ascent Algorithm with gradient computation and action prescription
- `lineage/math/network.py` --- CognitiveNet (PyTorch, CUDA)

All mathematical primitives are implemented in pure Python without numpy or scipy dependencies, ensuring portability to constrained deployment environments.

## Appendix B: Notation Summary

| Symbol | Name | Definition |
|--------|------|-----------|
| Q | Total capacity | sqrt((nu* Pi)^2 + (M (nu*)^2)^2) |
| M | Cognitive mass | alpha_1 C_id + alpha_2 C_mem + alpha_3 C_graph + alpha_4 C_perm |
| Pi | Cognitive momentum | beta_1 F_wm + beta_2 F_ret + beta_3 F_path + beta_4 F_ctrl + beta_5 F_merge |
| nu* | Propagation bound | 1000 / max(all latencies) |
| E_0 | Rest energy | M * (nu*)^2 |
| O_t | Organism state | (D_t, Psi_t, Sigma_t, B_t) |
| L | Graph Laplacian | D - W |
| Phi_org | Organism barrier | Phi_sub + Phi_gov + Phi_sig + Phi_sup |

---

*Vektra Technologies, 2026. All rights reserved.*
*Correspondence: pablo@vektratechnologies.com*
