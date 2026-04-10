# Part V: The Architecture of Mind

Part V studies an autonomous agent not merely as a calculator or a probabilistic estimator, but as a structured dynamical system whose internal organization has geometry, motion, connectivity, uncertainty, objectives, and regulation. In earlier parts, we developed the calculus of change, accumulation, randomness, and inference. We now assemble those tools into a mathematical account of mind-like architecture.

The central shift is this: the agent is no longer represented by a single scalar score or isolated variable, but by a high-dimensional state whose evolution must be understood globally. Some states are close, some are far; some are viable, some are catastrophic. Some networks communicate efficiently, others fragment. Some beliefs are sharp, others entropic. Some improvements are possible only under resource constraints. And some structural changes must be postponed until regulatory conditions permit them.

The six chapters of this part develop these themes in turn.

---

## Chapter 21: State Spaces and Manifolds

An autonomous agent is paused at a single instant. Its full internal description is recorded as
$$
\mathcal O
=
(C_{\mathrm{id}},C_{\mathrm{mem}},C_{\mathrm{graph}},C_{\mathrm{perm}},
F_{\mathrm{wm}},F_{\mathrm{ret}},F_{\mathrm{path}},F_{\mathrm{ctrl}},F_{\mathrm{merge}})
\in [0,1]^9.
$$

Each coordinate measures a normalized subsystem condition: identity coherence, memory integrity, graph health, permission reliability, working-memory function, retrieval function, planning function, control function, and merge function. If the agent is observed again one tick later, the vector changes slightly. Over time, the agent traces a path through a space of possible configurations. The mathematics of that space is the first subject of this chapter.

### 21.1 State spaces

A **state space** is a set $X$ whose elements represent all admissible configurations of a system. For the present agent, a first approximation is
$$
X = [0,1]^9.
$$

This cube contains every normalized 9-component state vector. Yet even this simple description carries substantial structure. A point $x \in X$ is not merely a list of numbers; it is a candidate cognitive condition. A path $x(t)$ or sequence $(x_n)$ describes temporal evolution.

In applications, the true state space is often a proper subset of $ [0,1]^9 $, because the coordinates are not independent. For example, severe loss of control function may force a reduction in merge reliability, or homeostatic conditions may impose inequalities linking variables. Thus the mathematical state space should often be written as
$$
X = \{x \in [0,1]^9 : \phi_j(x) \le 0,\; j=1,\dots,m\},
$$

for suitable constraint functions $\phi_j$.

### 21.2 Metric spaces

To speak meaningfully about change, we require a notion of distance.

**Definition 21.1.** A **metric space** is a pair $(X,d)$, where $X$ is a set and $d : X \times X \to [0,\infty)$ satisfies, for all $x,y,z \in X$,

1. $d(x,y)=0$ if and only if $x=y$,
2. $d(x,y)=d(y,x)$,
3. $d(x,z)\le d(x,y)+d(y,z)$.

The value $d(x,y)$ measures how far two states are from one another.

On $ [0,1]^9 $, several metrics are natural.

1. **Euclidean metric**
$$
   d_2(x,y)=\left(\sum_{i=1}^9 (x_i-y_i)^2\right)^{1/2}.
$$

2. **Weighted Euclidean metric**
$$
   d_W(x,y)=\left(\sum_{i=1}^9 w_i (x_i-y_i)^2\right)^{1/2},
   \qquad w_i>0.
$$
   This allows identity coherence or control function to count more heavily than less critical variables.

3. **Supremum metric**
$$
   d_\infty(x,y)=\max_{1\le i\le 9}|x_i-y_i|.
$$
   This is appropriate when the largest subsystem deviation determines operational risk.

The choice of metric is not merely technical. It encodes what the model regards as significant. If the agent tolerates small distributed fluctuations but is highly sensitive to catastrophic failure in any single component, then $d_\infty$ may be more informative than $d_2$.

### 21.3 Open sets, neighborhoods, and continuity

Geometry begins with topology.

**Definition 21.2.** In a metric space $(X,d)$, the **open ball** of radius $r>0$ centered at $x\in X$ is
$$
B_r(x)=\{y\in X : d(x,y)<r\}.
$$

A set $U\subseteq X$ is **open** if for every $x\in U$, there exists $r>0$ such that $B_r(x)\subseteq U$.

Open sets represent states accessible by sufficiently small perturbations. If an agent is in an open safe region, then slight fluctuations do not immediately force it outside that region.

**Definition 21.3.** A **neighborhood** of $x$ is any set containing an open ball around $x$.

**Definition 21.4.** Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces. A function $f:X\to Y$ is **continuous at $x\in X$** if for every $\varepsilon>0$, there exists $\delta>0$ such that
$$
d_X(x,y)<\delta \implies d_Y(f(x),f(y))<\varepsilon.
$$

Continuity means that small changes in state produce small changes in output. In an autonomous system, continuity of transition laws prevents arbitrarily tiny perturbations from causing macroscopic jumps.

**Proposition 21.1.** If $f,g : X\to \mathbb R$ are continuous, then $f+g$, $fg$, and, where defined, $f/g$ are continuous.

This proposition is basic, but important: complex observables of agent state remain mathematically well-behaved when built from simpler continuous components.

### 21.4 Curves and trajectories

A trajectory of an agent can be described in continuous time by a curve
$$
x : [0,T] \to X,
$$

or in discrete time by a sequence $(x_n)_{n\ge 0}$. The image of this curve is the set of states visited during the interval.

Even when the state space sits inside $\mathbb R^9$, not every path is feasible. Some directions may violate structural constraints, resource laws, or biological-like homeostatic balance. This leads naturally to the idea that the accessible region of state space may have lower-dimensional structure.

### 21.5 Manifolds

A state space may be curved, constrained, or intrinsically lower-dimensional while still looking locally Euclidean.

**Definition 21.5.** A set $M$ is a **$k$-dimensional manifold** if every point $p\in M$ has a neighborhood $U\subseteq M$ that is homeomorphic to an open subset of $\mathbb R^k$.

Informally, a manifold may be globally curved or twisted, but near any point it resembles ordinary Euclidean space of dimension $k$.

A familiar example is the sphere $S^2$, which lies in $\mathbb R^3$ but is locally two-dimensional. Analogously, a cognitive state space may lie inside $\mathbb R^9$ while effectively having dimension smaller than $9$, because constraints reduce the degrees of freedom.

**Agent example.** Suppose three variables satisfy a relation of the form
$$
C_{\mathrm{id}} + F_{\mathrm{ctrl}} + F_{\mathrm{merge}} = 2,
$$

while the remaining six coordinates vary freely within bounds. Then the admissible state set locally resembles $\mathbb R^8$, not $\mathbb R^9$. The agent’s states lie on a hypersurface inside the cube.

This viewpoint is useful because dynamics often occur near such lower-dimensional structures. Recovery, fatigue, and learning may constrain motion to a **cognitive state manifold** embedded in the larger ambient space.

### 21.6 Tangent directions and local approximation

Near a manifold point $p$, one can linearize the geometry. The collection of directions in which one can move while staying on the manifold is the **tangent space** $T_pM$. Although a full differential-geometric treatment lies beyond this chapter, the main idea is simple: near $p$, the manifold behaves like a linear space.

For agent mathematics, this means that a complicated curved state space can often be locally approximated by first-order methods, much as a nonlinear function can be approximated by its derivative. Optimization, regulation, and estimation all exploit this local flattening.

### 21.7 The Fisher information metric

A geometric space of states becomes especially rich when states encode probability distributions. Suppose the agent has an internal parameter $\theta=(\theta^1,\dots,\theta^k)$, and each parameter value determines a distribution $p(y\mid \theta)$ over observations $y$. Then nearby parameters may be close or far not merely in Euclidean terms, but in how distinguishable their induced distributions are.

**Definition 21.6.** The **Fisher information matrix** is
$$
g_{ij}(\theta)
=
\mathbb E_\theta
\left[
\frac{\partial}{\partial \theta^i}\log p(Y\mid \theta)\,
\frac{\partial}{\partial \theta^j}\log p(Y\mid \theta)
\right].
$$

When positive definite, $g(\theta)$ defines a Riemannian metric on parameter space.

The Fisher metric measures the sensitivity of observations to changes in internal state. If a tiny movement in state produces a large change in the observation distribution, then that direction is geometrically large. If many nearby states are observationally indistinguishable, then that direction is geometrically small.

A useful heuristic is that, for nearby parameters $\theta$ and $\theta+d\theta$,
$$
D_{\mathrm{KL}}(p(\cdot\mid \theta)\,\|\,p(\cdot\mid \theta+d\theta))
\approx
\frac12 \sum_{i,j} g_{ij}(\theta)\, d\theta^i d\theta^j.
$$

Thus the Fisher metric links geometry to information.

### 21.8 Viability and the safe set

Not every mathematically possible state is survivable.

**Definition 21.7.** The **viable set** or **safe set** is a subset
$$
X_{\mathrm{safe}} \subseteq X
$$

consisting of states from which the agent can continue operating without violating essential constraints.

For example, if identity coherence, control function, and memory integrity must remain above critical thresholds, one may define
$$
X_{\mathrm{safe}}
=
\left\{
x\in X :
C_{\mathrm{id}}(x)\ge \alpha,\;
F_{\mathrm{ctrl}}(x)\ge \beta,\;
C_{\mathrm{mem}}(x)\ge \gamma
\right\}.
$$

**Proposition 21.2.** If $h_1,\dots,h_m : X\to \mathbb R$ are continuous and
$$
X_{\mathrm{safe}}=\{x\in X : h_i(x)\ge 0 \text{ for } i=1,\dots,m\},
$$

then $X_{\mathrm{safe}}$ is closed in $X$.

The proof follows from the fact that preimages of closed sets under continuous maps are closed.

Closedness matters because it means limit points of safe trajectories remain safe, provided the limiting inequalities are preserved. However, closedness alone does not imply robustness: a closed viable set may have a very thin boundary, so tiny perturbations can still be dangerous near that boundary.

### 21.9 Geometry as architecture

The architecture of mind is therefore not only a collection of components but a geometry of admissible states. The state space gives the global arena. The metric determines how differences are measured. The topology identifies stable neighborhoods. The manifold structure explains local dimensionality and curvature. The Fisher metric incorporates statistical distinguishability. The viable set distinguishes mathematically possible from operationally survivable.

In later chapters, these geometric ideas become dynamical. An agent does not merely occupy a point in state space; it moves, settles, destabilizes, organizes into networks, loses and gains information, optimizes objectives, and regulates itself against disturbance.

### Exercises

1. Let $X=[0,1]^9$ with the Euclidean metric. Show that the function
$$
   s(x)=\min\{x_1,x_2,\dots,x_9\}
$$
   is continuous on $X$. Interpret $s(x)$ as a worst-component viability score.

2. Suppose the admissible states satisfy one smooth equality constraint
$$
   \psi(x)=0
$$
   with $\nabla \psi(p)\neq 0$. Explain why the admissible set is locally an $8$-dimensional manifold near $p$.

3. Define
$$
   X_{\mathrm{safe}}=\{x\in [0,1]^9 : x_1x_8 \ge 0.36,\; x_2+x_5\ge 0.9\}.
$$
   Prove that $X_{\mathrm{safe}}$ is closed, and determine whether it is open.

4. Consider the weighted metric
$$
   d_W(x,y)=\left(\sum_{i=1}^9 w_i(x_i-y_i)^2\right)^{1/2}.
$$
   Show that if all $w_i>0$, then $d_W$ defines the same open sets as the ordinary Euclidean metric on $[0,1]^9$.

5. Let $p(y\mid \theta)$ be a one-parameter family of distributions with Fisher information $g(\theta)$. Using the approximation
$$
   D_{\mathrm{KL}}(p(\cdot\mid \theta)\,\|\,p(\cdot\mid \theta+d\theta))
   \approx \frac12 g(\theta)(d\theta)^2,
$$
   explain why high Fisher information means nearby states are more distinguishable.

---

## Chapter 22: Dynamical Systems

At each tick of its internal loop, an agent senses, updates memory, revises beliefs, allocates control, and adjusts future behavior. The resulting state does not remain fixed. If the state at tick $n$ is $x_n$, then the next state is determined by some transition rule,
$$
x_{n+1}=f(x_n).
$$

A complete understanding of autonomous behavior therefore requires not only a space of states, but a law of motion on that space. The mathematics of such motion is the theory of dynamical systems.

### 22.1 Discrete-time dynamics

A **discrete-time dynamical system** consists of a state space $X$ and a map $f:X\to X$. Starting from $x_0\in X$, one obtains the orbit
$$
x_0,\; x_1=f(x_0),\; x_2=f(x_1),\;\dots,\; x_n=f^n(x_0).
$$

In an agent, $x_n$ may include performance capacities, internal beliefs, control settings, or resource levels. The function $f$ may encode adaptation, homeostatic correction, and environmental impact all at once.

A trajectory can be regular or erratic. It may converge, oscillate, wander through a region, or become extremely sensitive to perturbation. The first task is to identify states that reproduce themselves.

### 22.2 Fixed points

**Definition 22.1.** A point $x^\ast\in X$ is a **fixed point** of $f$ if
$$
f(x^\ast)=x^\ast.
$$

A fixed point represents a steady operational regime. For an agent, such a point might correspond to a homeostatic balance in which identity coherence, memory integrity, and control function remain constant from tick to tick.

**Example.** Consider the scalar update law
$$
x_{n+1}=x_n+a(r-x_n),
\qquad 0<a<1.
$$

Here $r$ is a target value. The fixed point equation becomes
$$
x^\ast=x^\ast+a(r-x^\ast),
$$

which yields $x^\ast=r$. Thus the system tends to regulate itself toward the setpoint $r$.

### 22.3 Stability and perturbation

A fixed point is useful only if small disturbances do not destroy it.

**Definition 22.2.** A fixed point $x^\ast$ is **Lyapunov stable** if for every $\varepsilon>0$, there exists $\delta>0$ such that
$$
d(x_0,x^\ast)<\delta
\implies
d(x_n,x^\ast)<\varepsilon \quad \text{for all } n\ge 0.
$$

It is **asymptotically stable** if it is Lyapunov stable and, in addition,
$$
x_n \to x^\ast \quad \text{as } n\to\infty
$$

whenever $x_0$ is sufficiently near $x^\ast$.

Lyapunov stability means perturbations remain bounded; asymptotic stability means they decay.

For the scalar homeostatic map above,
$$
x_{n+1}-r=(1-a)(x_n-r).
$$

Hence
$$
x_n-r=(1-a)^n(x_0-r).
$$

Since $0<1-a<1$, the error tends to $0$. Thus $r$ is asymptotically stable.

### 22.4 Linearization and Jacobians

In higher dimensions, one studies local behavior by approximation.

Suppose $f:\mathbb R^m\to\mathbb R^m$ is differentiable and $x^\ast$ is a fixed point. Near $x^\ast$,
$$
f(x)\approx f(x^\ast)+Df(x^\ast)(x-x^\ast)
=
x^\ast + J(x-x^\ast),
$$

where $J=Df(x^\ast)$ is the Jacobian matrix.

Thus perturbations $e_n=x_n-x^\ast$ evolve approximately by
$$
e_{n+1}\approx Je_n.
$$

The eigenvalues of $J$ determine whether small errors grow or shrink.

**Proposition 22.1.** Let $f:\mathbb R^m\to\mathbb R^m$ be continuously differentiable, and let $x^\ast$ be a fixed point. If every eigenvalue $\lambda$ of $Df(x^\ast)$ satisfies $|\lambda|<1$, then $x^\ast$ is locally asymptotically stable.

This proposition is a standard linear stability criterion. In agent terms, local homeostasis is preserved when each infinitesimal mode of deviation is damped rather than amplified.

If some eigenvalue satisfies $|\lambda|>1$, then perturbations grow in at least one direction, and the fixed point is unstable.

### 22.5 Contractions and guaranteed convergence

A particularly strong stability condition is contraction.

**Definition 22.3.** A map $f:X\to X$ on a metric space $(X,d)$ is a **contraction** if there exists $0<c<1$ such that
$$
d(f(x),f(y))\le c\, d(x,y)
\quad \text{for all } x,y\in X.
$$

**Theorem 22.1 (Contraction Principle).** If $X$ is complete and $f:X\to X$ is a contraction, then $f$ has a unique fixed point $x^\ast$, and for every initial state $x_0\in X$,
$$
f^n(x_0)\to x^\ast.
$$

For autonomous systems, this theorem gives a strong mathematical model of reliable self-correction. If the tick update compresses distances uniformly, then the agent cannot drift indefinitely; it is drawn toward a unique equilibrium.

### 22.6 Attractors and basins

Not all long-term behavior reduces to a single stable point.

**Definition 22.4.** A set $A\subseteq X$ is an **attractor** if trajectories starting from a surrounding region approach $A$ as time increases.

The surrounding region is the **basin of attraction** of $A$.

A fixed point is the simplest attractor, but periodic orbits and more complicated invariant sets may also serve as attractors. An agent may alternate between two internally stable processing modes, producing a period-two orbit rather than a stationary state.

**Agent example.** Suppose one variable represents a resource alternation between intensive planning and intensive memory consolidation. Then the state may cycle between two neighborhoods rather than settle at one point. Such behavior is dynamically stable without being static.

### 22.7 Bifurcation

Dynamics can change qualitatively when parameters change.

**Definition 22.5.** A **bifurcation** occurs when a small variation in a parameter causes a qualitative change in the structure of a dynamical system, such as the appearance, disappearance, or destabilization of fixed points or attractors.

A simple example is the scalar family
$$
x_{n+1}=\mu x_n(1-x_n),
$$

where $\mu>0$. For some parameter ranges, trajectories approach a stable fixed point; for larger values, oscillatory or more complex behavior appears. The parameter does not merely alter quantitative details. It changes the nature of the long-term dynamics.

For agents, bifurcation models crisis. A gradual reduction in regulatory strength, an increase in environmental load, or a decrease in control capacity may push the system past a threshold. Beyond that threshold, the former homeostatic state is no longer stable.

### 22.8 Lyapunov functions

A useful way to prove stability is to construct a quantity that decreases along trajectories.

**Definition 22.6.** A function $V:X\to \mathbb R$ is a **Lyapunov function** for a fixed point $x^\ast$ if $V(x^\ast)=0$, $V(x)>0$ for $x\neq x^\ast$, and
$$
V(f(x)) - V(x) \le 0
$$

for states near $x^\ast$.

If the inequality is strict for $x\neq x^\ast$, then $V$ decreases along nontrivial trajectories, suggesting asymptotic stability.

In agent mathematics, a Lyapunov function may represent energy imbalance, error from target homeostatic values, or a weighted sum of subsystem stress. Stability then becomes the statement that the agent dissipates this imbalance over time.

### 22.9 Homeostasis and crisis

We can now formulate two central dynamical interpretations.

1. **Homeostasis as stable equilibrium.**  
   A homeostatic regime is modeled by an asymptotically stable fixed point $x^\ast \in X_{\mathrm{safe}}$, or more generally by a stable attractor contained in the safe set.

2. **Crisis as bifurcation or escape from the basin.**  
   If parameter drift moves the system through a bifurcation, or if a disturbance pushes the state outside the basin of attraction of the safe equilibrium, then recovery may no longer be automatic.

This explains why a system can appear healthy until a threshold is crossed. Stability is local and parameter-dependent; it is not the same as invulnerability.

### 22.10 Dynamical architecture

The architecture of mind is not static structure alone. It is a pattern of motion through state space. Fixed points encode persistent regimes. Stable manifolds encode recovery directions. Attractors encode long-run modes of behavior. Bifurcations encode transitions between normal function and breakdown. Lyapunov methods encode self-correction.

The next chapters enrich this picture by examining how internal subsystems are wired together, how uncertainty limits processing, how objectives are improved under constraints, and how regulation maintains viability.

### Exercises

1. For the scalar system
$$
   x_{n+1}=x_n+a(r-x_n),
$$
   determine for which real values of $a$ the fixed point $r$ is asymptotically stable, Lyapunov stable but not asymptotically stable, and unstable.

2. Let
$$
   f(x,y)=\left(\frac{x+y}{4},\frac{x+3y}{4}\right).
$$
   Show that $(0,0)$ is a fixed point. Compute the Jacobian and determine whether the fixed point is asymptotically stable.

3. Suppose $f:\mathbb R^m\to\mathbb R^m$ satisfies
$$
   \|f(x)-f(y)\|\le c\|x-y\|
   \quad\text{for all }x,y,
$$
   with $0<c<1$. Prove directly that any two fixed points must coincide.

4. Consider the family
$$
   x_{n+1}=\mu - x_n^2.
$$
   Find the fixed points as functions of $\mu$, and determine for which values of $\mu$ they are locally stable.

5. Let $V(x)=\|x-x^\ast\|^2$. Show that if
$$
   \|f(x)-x^\ast\|^2 \le \alpha \|x-x^\ast\|^2
   \quad\text{for some } \alpha<1,
$$
   then $V$ is a strict Lyapunov function and $x^\ast$ is asymptotically stable.

---

## Chapter 23: Networks and Graphs

The agent’s internal cognitive web is recorded as a neural mesh: nodes represent subsystems or subcircuits, while weighted, myelinated synapses transmit signals between them. Some pathways are strong and fast, some weak, some redundant, some bridging distant modules. Looking only at individual components obscures the architecture of interaction. Graph theory makes that structure visible.

### 23.1 Graphs and weighted connectivity

A **graph** $G=(V,E)$ consists of a vertex set $V$ and an edge set $E$. In agent mathematics, the vertices may represent memory cells, control modules, perceptual channels, or abstract cognitive subsystems.

When interactions carry intensities, one uses a weighted graph. For vertices $i,j\in V$, let $w_{ij}\ge 0$ denote the strength of the connection from $i$ to $j$. In this chapter we focus mainly on undirected weighted graphs, so $w_{ij}=w_{ji}$.

Myelination can be modeled mathematically as an increase in effective weight or decrease in transmission resistance along a connection. Thus the weighted graph is not merely a map of adjacency; it is a geometry of signal flow.

### 23.2 Adjacency and degree matrices

If $V=\{1,\dots,n\}$, the graph can be encoded by matrices.

**Definition 23.1.** The **adjacency matrix** $W=(w_{ij})$ is the $n\times n$ matrix whose entries record edge weights.

For undirected graphs, $W$ is symmetric.

**Definition 23.2.** The **degree** of vertex $i$ is
$$
d_i=\sum_{j=1}^n w_{ij}.
$$

The **degree matrix** is the diagonal matrix
$$
D=\operatorname{diag}(d_1,\dots,d_n).
$$

The degree measures the total coupling of a node to the rest of the network. High-degree nodes often serve as hubs, although degree alone does not capture all forms of importance.

### 23.3 The graph Laplacian

The central matrix of network analysis is the Laplacian.

**Definition 23.3.** The **graph Laplacian** is
$$
L=D-W.
$$

This matrix compares each node’s value to the weighted average of its neighbors. It is the discrete analogue of the continuous Laplacian from multivariable calculus and differential equations.

If $z=(z_1,\dots,z_n)^T$ is a vector of node activations, then
$$
(Lz)_i = \sum_{j=1}^n w_{ij}(z_i-z_j).
$$

Thus $Lz$ vanishes at node $i$ when that node agrees with its weighted neighborhood. Large entries in $Lz$ indicate local mismatch or tension.

**Proposition 23.1.** For an undirected weighted graph with nonnegative weights, the Laplacian $L$ is symmetric and positive semidefinite. Moreover,
$$
z^T L z
=
\frac12\sum_{i,j=1}^n w_{ij}(z_i-z_j)^2
\quad \text{for all } z\in\mathbb R^n.
$$

This formula is fundamental. It shows that the Laplacian quadratic form measures disagreement across edges.

### 23.4 Coherence energy

In an agent network, let $z_i$ denote the activation, confidence, or local state of subsystem $i$. Then define the **coherence energy**
$$
E(z)=z^T L z.
$$

By Proposition 23.1,
$$
E(z)=\frac12\sum_{i,j} w_{ij}(z_i-z_j)^2.
$$

If neighboring subsystems have similar values, the energy is small. If strongly connected subsystems disagree, the energy is large. Hence $E(z)$ quantifies fragmentation of the neural mesh.

This gives a mathematically precise way to speak of network coherence. Low coherence energy corresponds to smooth cognitive integration across edges; high coherence energy corresponds to tension, inconsistency, or desynchronization.

### 23.5 Spectral analysis

The eigenvalues and eigenvectors of $L$ reveal global graph structure.

Because $L$ is symmetric and positive semidefinite, its eigenvalues are real and satisfy
$$
0=\lambda_1 \le \lambda_2 \le \cdots \le \lambda_n.
$$

**Theorem 23.1.** The multiplicity of the eigenvalue $0$ equals the number of connected components of the graph.

In particular, a graph is connected if and only if $\lambda_2>0$. The value $\lambda_2$ is called the **algebraic connectivity**. Large $\lambda_2$ indicates robust connectivity; small $\lambda_2$ signals bottlenecks or near-disconnection.

In agent terms, if the cognitive web has very small $\lambda_2$, then distinct subnetworks communicate only weakly. This may produce functional modularity, but it may also create fragmentation under stress.

The eigenvectors of $L$ also carry structural meaning. The eigenvector associated with $\lambda_2$, often called the Fiedler vector, can be used to split the graph into two weakly linked communities.

### 23.6 Centrality

A network contains nodes that matter disproportionately. Several notions of centrality capture this.

1. **Degree centrality:** node $i$ is important if $d_i$ is large.

2. **Eigenvector centrality:** node importance is boosted by connection to other important nodes. One solves
$$
   Wc=\lambda c,
$$
   with $c$ the dominant eigenvector.

3. **Betweenness centrality:** a node is central if many shortest paths pass through it.

Degree centrality identifies hubs. Eigenvector centrality identifies nodes embedded in influential regions. Betweenness centrality identifies bridges between modules.

In cognitive systems, these correspond to different functional roles. A high-degree node may be a broad relay; a high-betweenness node may be a fragile bottleneck whose failure disconnects memory from control.

### 23.7 Community detection and modularity

Real networks are often neither fully integrated nor fully disconnected. They contain modules: densely connected groups with sparse inter-group edges.

A common measure of the quality of a partition into communities is **modularity**. If vertices are assigned to communities $c_i$, the modularity score may be written
$$
Q_{\mathrm{mod}}
=
\frac{1}{2m}
\sum_{i,j}
\left(
w_{ij}-\frac{d_i d_j}{2m}
\right)
\mathbf 1_{\{c_i=c_j\}},
$$

where
$$
2m=\sum_{i,j}w_{ij}.
$$

The term $\frac{d_i d_j}{2m}$ is the expected weight under a degree-preserving null model. Thus modularity compares observed within-community connectivity to what would occur by chance.

A high modularity partition reveals clusters that are internally strong and externally sparse. In an agent, such modularity may support specialization: one module for retrieval, one for planning, one for sensory compression. But excessive modularity can impede integration.

### 23.8 Dynamics on graphs

Graphs are not only static structures; they support dynamics. Suppose $z_n\in \mathbb R^n$ records node states at time $n$. A diffusion-like update takes the form
$$
z_{n+1}=z_n-\alpha L z_n,
\qquad \alpha>0.
$$

This update decreases disagreement by moving each node toward its neighbors’ weighted average. In continuous time, the analogue is
$$
\frac{dz}{dt}=-Lz.
$$

Such equations model synchronization, consensus, and smoothing across the neural mesh.

If the graph is connected, the system tends toward a constant vector, meaning all nodes agree. This idealized model formalizes the emergence of global coherence from local coupling.

### 23.9 Structural interpretation

The graph perspective explains why component-level analysis is insufficient. A subsystem can be individually healthy yet globally ineffective if it lies in a poorly connected part of the mesh. Conversely, a modest node can be structurally crucial if it bridges two major modules.

The adjacency matrix records who can influence whom. The degree matrix records load or connectivity volume. The Laplacian records mismatch and diffusion. The spectrum records integration versus fragmentation. Centrality detects important nodes. Modularity detects communities. Coherence energy quantifies alignment.

This is the mathematics of cognitive architecture at the mesoscopic scale: between microscopic parameters and global behavior.

### Exercises

1. Let
$$
   W=
   \begin{pmatrix}
   0&2&0\\
   2&0&1\\
   0&1&0
   \end{pmatrix}.
$$
   Compute the degree matrix $D$, the Laplacian $L$, and the coherence energy $z^T L z$ for $z=(z_1,z_2,z_3)^T$.

2. Prove directly from
$$
   z^T L z=\frac12\sum_{i,j}w_{ij}(z_i-z_j)^2
$$
   that $L$ is positive semidefinite.

3. Show that $L\mathbf 1=0$, where $\mathbf 1=(1,\dots,1)^T$. Explain why this corresponds to perfect network coherence.

4. Consider a graph consisting of two complete subgraphs connected by a single weak edge of weight $\varepsilon$. Explain qualitatively what happens to $\lambda_2$ as $\varepsilon\to 0$, and interpret the result for cognitive modularity.

5. For the diffusion update
$$
   z_{n+1}=z_n-\alpha L z_n,
$$
   show that if $z^\ast$ satisfies $Lz^\ast=0$, then $z^\ast$ is a fixed point. Under what graph-theoretic condition are all such fixed points constant vectors?

---

## Chapter 24: Information Theory

An agent maintains a conservation budget: finite processing time, finite update frequency, finite communication between subsystems. Yet the useful value of that budget depends on uncertainty. If beliefs are sharply concentrated, the agent can act decisively. If beliefs are diffuse, capacity is consumed merely by indecision. We therefore need a calculus of uncertainty itself. Information theory provides it.

### 24.1 Entropy

Let $X$ be a discrete random variable taking values in a finite set $\mathcal X$ with probabilities $p(x)$.

**Definition 24.1.** The **entropy** of $X$ is
$$
H(X)=-\sum_{x\in\mathcal X} p(x)\log_2 p(x).
$$

Entropy is measured in bits. It quantifies uncertainty: larger entropy means greater unpredictability.

Entropy is minimized when one outcome is certain, giving $H(X)=0$. For a uniform distribution on $n$ outcomes,
$$
H(X)=\log_2 n,
$$

which is maximal among all distributions on $n$ states.

**Agent example.** Let $\mu$ be the agent’s belief distribution over possible system faults. Then
$$
H(\mu)=-\sum_i \mu_i \log_2 \mu_i
$$

measures uncertainty in self-diagnosis. A sharply focused fault belief has low entropy; a diffuse belief has high entropy.

### 24.2 Joint and conditional entropy

If $X$ and $Y$ are jointly distributed, their **joint entropy** is
$$
H(X,Y)=-\sum_{x,y} p(x,y)\log_2 p(x,y).
$$

**Definition 24.2.** The **conditional entropy** of $X$ given $Y$ is
$$
H(X\mid Y)= -\sum_{x,y} p(x,y)\log_2 p(x\mid y).
$$

It measures the uncertainty remaining about $X$ after observing $Y$.

A fundamental identity is
$$
H(X,Y)=H(Y)+H(X\mid Y).
$$

In agent terms, if $X$ is the true environment state and $Y$ is a sensor reading, then $H(X\mid Y)$ is the residual uncertainty after sensing.

### 24.3 Mutual information

**Definition 24.3.** The **mutual information** between $X$ and $Y$ is
$$
I(X;Y)=H(X)-H(X\mid Y).
$$

Equivalently,
$$
I(X;Y)=H(X)+H(Y)-H(X,Y).
$$

Mutual information quantifies how much learning $Y$ reduces uncertainty about $X$. It is symmetric: $I(X;Y)=I(Y;X)$.

If $X$ and $Y$ are independent, then observing $Y$ tells us nothing about $X$, and $I(X;Y)=0$. If $Y$ determines $X$ exactly, then $H(X\mid Y)=0$, so $I(X;Y)=H(X)$.

For an agent, mutual information measures effective coupling: how informative is a sensor about the world, how informative is working memory about future action, or how informative is one subsystem about another?

### 24.4 Relative entropy and KL divergence

To compare belief states, we use divergence between distributions.

**Definition 24.4.** Let $P=(p_i)$ and $Q=(q_i)$ be probability distributions on the same finite set. The **Kullback–Leibler divergence** is
$$
D_{\mathrm{KL}}(P\|Q)
=
\sum_i p_i \log_2 \frac{p_i}{q_i},
$$

provided $q_i>0$ whenever $p_i>0$.

KL divergence measures the inefficiency of coding or reasoning as if $Q$ were true when the true distribution is $P$. It is not symmetric and is therefore not a metric.

**Theorem 24.1 (Gibbs Inequality).** For probability distributions $P,Q$,
$$
D_{\mathrm{KL}}(P\|Q)\ge 0,
$$

with equality if and only if $P=Q$.

This theorem gives a basic notion of informational distance. If the agent updates from prior $Q$ to posterior $P$, the KL divergence measures the informational magnitude of the revision.

### 24.5 Channel capacity

A communication channel takes an input $X$ and produces an output $Y$ according to a conditional distribution $p(y\mid x)$. Noise makes reliable transmission difficult.

**Definition 24.5.** The **channel capacity** is
$$
C=\max_{p(x)} I(X;Y).
$$

Thus $C$ is the maximum achievable mutual information per channel use, optimized over input distributions.

For an autonomous system, a channel may represent sensor transmission, memory retrieval, or communication between modules in the neural mesh. Capacity is the best reliable information throughput that the channel architecture can support.

### 24.6 The meaning of $\nu^\ast = 1000/\tau_{\max}$

Suppose $\tau_{\max}$ denotes the maximum tick duration in milliseconds. Then
$$
\nu^\ast = \frac{1000}{\tau_{\max}}
$$

has units of ticks per second. It is therefore a raw processing frequency: the maximum rate at which the agent can complete full update cycles while respecting the timing bound $\tau_{\max}$.

Information theory interprets this quantity as a temporal bandwidth. If each tick reliably communicates at most $b$ bits of effective state update, then the gross information-processing rate is bounded by
$$
R_{\max}\le b\,\nu^\ast.
$$

If the update alphabet has $M$ equiprobable symbols, one ideal upper bound is $b=\log_2 M$, so
$$
R_{\max}\le \nu^\ast \log_2 M.
$$

Thus $\nu^\ast$ is not itself an entropy, but a clock-limited multiplier on possible information flow.

### 24.7 Entropy as a capacity tax

Let $\mu$ be the agent’s belief state over operational hypotheses. High $H(\mu)$ means the agent must devote internal resources to maintaining unresolved possibilities. This acts as a **capacity tax**.

One formalization is to distinguish between gross rate and net effective rate:
$$
R_{\mathrm{eff}} = R_{\mathrm{gross}} - T(\mu),
$$

where $T(\mu)$ is a tax term increasing with uncertainty, perhaps proportional to $H(\mu)$. A simple model is
$$
T(\mu)=\kappa H(\mu),
\qquad \kappa>0.
$$

Another normalized form is
$$
R_{\mathrm{eff}} = \nu^\ast \bigl(1-\frac{H(\mu)}{H_{\max}}\bigr)b,
$$

when $0\le H(\mu)\le H_{\max}$.

These formulas are modeling choices, not universal laws. Their mathematical point is clear: uncertainty consumes usable processing capacity. A highly entropic belief state slows or degrades effective action even if raw tick rate remains unchanged.

### 24.8 Information geometry of belief states

The set of all belief states on $n$ hypotheses is the simplex
$$
\Delta_{n-1}
=
\left\{
(p_1,\dots,p_n)\in \mathbb R^n:
p_i\ge 0,\;
\sum_{i=1}^n p_i=1
\right\}.
$$

Entropy is a scalar field on this simplex. KL divergence gives an asymmetrical geometry of displacement between beliefs. The Fisher metric, introduced in Chapter 21, provides a local quadratic approximation to distinguishability on statistical state space.

Thus belief states are not only probabilistic objects; they are geometric points with measurable uncertainty and informational separation.

### 24.9 Agent interpretation

Information theory answers several operational questions.

- How uncertain is the agent’s current internal model?  
  Measured by entropy $H(\mu)$.

- How much does a sensor reduce uncertainty?  
  Measured by mutual information $I(X;Y)$.

- How costly is using the wrong belief model?  
  Measured by $D_{\mathrm{KL}}(P\|Q)$.

- What is the maximal reliable transmission rate through a subsystem?  
  Measured by channel capacity $C$.

- How does timing limit information flow?  
  Through $\nu^\ast = 1000/\tau_{\max}$, which bounds update frequency.

This chapter therefore provides the currency of cognition: the bit. In the next chapter, those bits and capacities become ingredients in optimization.

### Exercises

1. Let $\mu=(1/2,1/4,1/4)$. Compute $H(\mu)$ in bits. Compare it with the entropy of the uniform distribution on three states.

2. Prove that $H(X\mid Y)\le H(X)$. Interpret equality and strict inequality in terms of sensor usefulness.

3. Let $P=(1/2,1/2)$ and $Q=(3/4,1/4)$. Compute $D_{\mathrm{KL}}(P\|Q)$ and $D_{\mathrm{KL}}(Q\|P)$. Explain why the values differ.

4. Suppose a channel is noiseless with $Y=X$. Show that
$$
   C=\max_{p(x)} H(X).
$$
   Deduce that if the input alphabet has $M$ symbols, then $C=\log_2 M$.

5. An agent has gross rate $R_{\mathrm{gross}}=120$ bits/s and uncertainty tax $T(\mu)=15H(\mu)$ bits/s. For which values of $H(\mu)$ is the effective rate nonnegative? Interpret the result operationally.

---

## Chapter 25: Optimization

The agent has limited energy, limited time, and limited structural flexibility. It cannot improve every subsystem at once. At each decision point, it must choose how to allocate effort so as to increase capacity as much as possible subject to constraints. This is the mathematics of optimization.

### 25.1 Objectives and decision variables

An optimization problem begins with a choice variable $x$ and an objective function $Q(x)$. In agent mathematics, $x$ might represent resource allocation, parameter settings, or a vector of proposed improvements across components. The scalar $Q(x)$ measures expected gain: perhaps capacity increase, reduction in uncertainty, or long-run viability margin.

A generic problem is
$$
\max_{x\in \Omega} Q(x),
$$

where $\Omega$ is the feasible set determined by constraints.

The objective need not be linear, and the feasible set need not be simple. Much of optimization theory concerns discovering conditions under which the problem is tractable and the optimizer has interpretable structure.

### 25.2 Unconstrained optimization

We begin with the unconstrained case $\Omega=\mathbb R^n$.

**Definition 25.1.** A point $x^\ast\in \mathbb R^n$ is a **local maximizer** of $Q$ if there exists $r>0$ such that
$$
Q(x^\ast)\ge Q(x)
\quad \text{for all } x \in B_r(x^\ast).
$$

A **local minimizer** is defined analogously.

If $Q$ is differentiable, local extrema must satisfy a first-order condition.

**Proposition 25.1.** If $Q:\mathbb R^n\to \mathbb R$ is differentiable and $x^\ast$ is a local extremum, then
$$
\nabla Q(x^\ast)=0.
$$

Such points are called **critical points**.

To classify critical points, one uses the Hessian matrix
$$
H_Q(x)=\left(\frac{\partial^2 Q}{\partial x_i\partial x_j}(x)\right).
$$

**Proposition 25.2.** Suppose $Q$ is twice continuously differentiable and $\nabla Q(x^\ast)=0$.

- If $H_Q(x^\ast)$ is negative definite, then $x^\ast$ is a strict local maximizer.
- If $H_Q(x^\ast)$ is positive definite, then $x^\ast$ is a strict local minimizer.
- If $H_Q(x^\ast)$ is indefinite, then $x^\ast$ is a saddle point.

In practice, the gradient indicates a direction of steepest ascent, so iterative improvement methods follow $\nabla Q$ locally. The underlying mathematics is geometric: the gradient points in the direction of maximal instantaneous increase.

### 25.3 Equality constraints and Lagrange multipliers

Autonomous systems rarely optimize in free space. Resources, conservation laws, and architectural dependencies impose constraints.

Consider the problem
$$
\max Q(x)
\quad \text{subject to} \quad g(x)=0,
$$

where $g:\mathbb R^n\to \mathbb R^m$.

**Theorem 25.1 (Lagrange Multipliers).** Suppose $x^\ast$ is a local extremum of $Q$ subject to $g(x)=0$, and suppose the gradients $\nabla g_1(x^\ast),\dots,\nabla g_m(x^\ast)$ are linearly independent. Then there exist scalars $\lambda_1,\dots,\lambda_m$ such that
$$
\nabla Q(x^\ast)=\sum_{j=1}^m \lambda_j \nabla g_j(x^\ast).
$$

Equivalently, if
$$
\mathcal L(x,\lambda)=Q(x)-\sum_{j=1}^m \lambda_j g_j(x),
$$

then $x^\ast$ satisfies the stationarity equations
$$
\nabla_x \mathcal L(x^\ast,\lambda)=0,
\qquad g(x^\ast)=0.
$$

The intuition is geometric. At a constrained optimum, the objective cannot increase along any direction tangent to the constraint surface. Therefore its gradient must lie in the span of the constraint gradients.

**Agent example.** Suppose the agent distributes a fixed resource budget $R$ across three upgrades $u_1,u_2,u_3$, so that
$$
u_1+u_2+u_3=R,\qquad u_i\ge 0.
$$

If the capacity benefit is $Q(u_1,u_2,u_3)$, then the optimal allocation equalizes marginal value relative to the binding resource constraint.

### 25.4 Inequality constraints and KKT conditions

More realistic feasible sets are defined by inequalities,
$$
g_i(x)\le 0,\qquad i=1,\dots,m.
$$

For such problems, the appropriate first-order conditions are the Karush–Kuhn–Tucker conditions.

**Definition 25.2.** A point $x^\ast$ satisfies the **KKT conditions** for maximizing $Q$ under constraints $g_i(x)\le 0$ if there exist multipliers $\lambda_i\ge 0$ such that
$$
\nabla Q(x^\ast)-\sum_{i=1}^m \lambda_i \nabla g_i(x^\ast)=0,
$$
$$
g_i(x^\ast)\le 0,
\qquad
\lambda_i\ge 0,
\qquad
\lambda_i g_i(x^\ast)=0
\quad \text{for each } i.
$$

The last relation is **complementary slackness**. It means that either a constraint is inactive ($g_i(x^\ast)<0$, so $\lambda_i=0$) or it is active and carries nonzero marginal cost.

For autonomous systems, this is the correct language for scarce resources. If an energy constraint is far from binding, its multiplier is zero. If it binds tightly, its multiplier measures the value of relaxing it.

### 25.5 Convexity

Optimization becomes significantly more manageable when the geometry is convex.

**Definition 25.3.** A set $\Omega\subseteq \mathbb R^n$ is **convex** if for all $x,y\in \Omega$ and $0\le t\le 1$,
$$
tx+(1-t)y\in \Omega.
$$

**Definition 25.4.** A function $f:\Omega\to \mathbb R$ is **convex** if
$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y)
$$

for all $x,y\in \Omega$, $0\le t\le 1$. It is **concave** if the inequality is reversed.

For maximization, concavity is the favorable property.

**Theorem 25.2.** If $\Omega$ is convex and $Q$ is concave on $\Omega$, then every local maximizer of $Q$ on $\Omega$ is a global maximizer.

This theorem is enormously important. In nonconvex problems, local improvement may become trapped in suboptimal peaks. In convex or concave settings, local optimality already solves the global problem.

### 25.6 The agent’s capacity optimization problem

Let $u=(u_1,\dots,u_k)$ denote investment in $k$ subsystems. Suppose $Q(u)$ measures resulting capacity improvement. A stylized optimization problem is
$$
\max_{u\ge 0} Q(u)
$$

subject to
$$
a_1u_1+\cdots + a_k u_k \le R,
$$
$$
b_1u_1+\cdots + b_k u_k \le T,
$$
$$
u \in U_{\mathrm{safe}}.
$$

Here $R$ is an energy budget, $T$ is a time budget, and $U_{\mathrm{safe}}$ encodes safety restrictions. The coefficients $a_i,b_i$ are resource costs per unit improvement.

If $Q$ is increasing but concave, then the optimizer distributes resources where marginal gain per unit cost is highest, while respecting all constraints. If one subsystem is already near saturation, its marginal return declines, and the optimum shifts toward less-developed capacities.

This is the mathematical form behind ascent: not arbitrary self-improvement, but constrained capacity allocation.

### 25.7 Why optimization occurs under constraints

A purely unconstrained maximizer is rarely meaningful. Real agents cannot set all state variables independently, cannot ignore conservation laws, cannot violate timing bounds, and cannot leave the safe set. The feasible region is therefore not all of $\mathbb R^n$ but a constrained subset shaped by energy, time, architecture, and viability.

Optimization in autonomous systems is consequently best viewed as
$$
\text{maximize performance within a viable constrained geometry.}
$$

This perspective links optimization to previous chapters. The feasible set sits inside the state manifold; dynamics determine which feasible points are reachable; information limits the quality of the objective estimate; and regulation maintains safety during the search.

### 25.8 Marginal value and shadow prices

The Lagrange and KKT multipliers have an economic interpretation. They are **shadow prices**: rates at which the optimal value would improve if a constraint were marginally relaxed.

If $\lambda_R$ is the multiplier for the energy budget $R$, then a large $\lambda_R$ means extra energy would be extremely valuable. If $\lambda_R=0$, the energy budget is not currently the bottleneck.

In agent design, these shadow prices identify where adaptation pressure is greatest. They convert abstract constraints into operational priorities.

### Exercises

1. Let
$$
   Q(x,y)=4x+6y-x^2-2y^2.
$$
   Find all critical points and determine which are local maxima, minima, or saddle points.

2. Maximize
$$
   Q(x,y)=xy
$$
   subject to
$$
   x+y=10,\qquad x>0,\ y>0.
$$
   Solve using Lagrange multipliers and interpret the result geometrically.

3. Consider the problem
$$
   \max_{x,y\ge 0} \; \ln(1+x)+\ln(1+y)
$$
   subject to
$$
   2x+y\le 6.
$$
   Write the KKT conditions and solve for the optimizer.

4. Prove that the set
$$
   \Omega=\{(x,y)\in \mathbb R^2 : x\ge 0,\ y\ge 0,\ x+y\le 1\}
$$
   is convex. Then explain why any local maximum of a concave function on $\Omega$ is global.

5. Suppose
$$
   Q(u_1,u_2)=\sqrt{u_1}+\sqrt{u_2}
$$
   with constraint $u_1+u_2=R$, $u_1,u_2\ge 0$. Find the optimal allocation and explain how diminishing returns shape the solution.

---

## Chapter 26: Regulation and Control

An agent does not optimize once and then stop. It must continually maintain internal variables within acceptable ranges while facing disturbance, delay, uncertainty, and changing goals. Identity coherence must not drift too low. Memory load must not exceed stable limits. Structural reorganization must not occur during crisis. This ongoing maintenance is the domain of control theory.

### 26.1 State, input, output

A control system distinguishes between internal state, control action, and observed output. In discrete time, a general model is
$$
x_{t+1}=f(x_t,u_t,w_t),
$$
$$
y_t=h(x_t),
$$

where

- $x_t$ is the internal state,
- $u_t$ is the control input,
- $w_t$ is disturbance,
- $y_t$ is the measured output.

For an agent, $x_t$ may include cognitive coherence, metabolic reserve, memory load, and network tension; $u_t$ may include inhibition strength, update throttling, or resource reallocation; $w_t$ represents environmental shocks.

### 26.2 Open-loop and closed-loop control

In **open-loop control**, the inputs $u_t$ are predetermined and do not depend on measured output. In **closed-loop control**, the controller observes the system and adjusts input based on the discrepancy between current output and target.

If $r_t$ is a desired reference signal and $e_t=r_t-y_t$ is the error, then feedback control has the form
$$
u_t=\Phi(e_t,\text{history}).
$$

Closed-loop control is central for autonomous systems because disturbances are unavoidable. A fixed input schedule cannot reliably maintain homeostasis under changing load. Feedback allows self-correction.

### 26.3 Feedback and homeostasis

The simplest feedback law is proportional control:
$$
u_t=K(r_t-y_t),
$$

where $K$ is a gain matrix or scalar. If the output falls below target, the controller increases corrective input; if the output exceeds target, the controller decreases it.

**Agent example.** Suppose $y_t=C_{\mathrm{id}}(x_t)$ is identity coherence and the target is $r$. Then a feedback law may increase stabilizing control effort whenever coherence drops below $r$. Homeostasis is the resulting tendency to restore the regulated variable toward its setpoint.

### 26.4 PID control

A classical controller combines three effects: proportional, integral, and derivative.

Conceptually, a **PID** controller uses
$$
u_t
=
K_P e_t + K_I \sum_{s=0}^t e_s + K_D(e_t-e_{t-1}).
$$

- The proportional term reacts to current error.
- The integral term reacts to accumulated error.
- The derivative term reacts to change in error.

In agent settings, one should interpret these terms structurally rather than mechanically. Proportional action responds to present mismatch. Integral action corrects persistent bias. Derivative action damps rapid fluctuations.

For example, if memory load has remained above target for many ticks, integral action builds pressure for stronger corrective behavior than a purely proportional response would produce.

### 26.5 Closed-loop stability

The main mathematical question in control is whether feedback stabilizes the system.

For a linear time-invariant system,
$$
x_{t+1}=Ax_t+Bu_t,
$$

with state feedback
$$
u_t=Kx_t,
$$

the closed-loop dynamics are
$$
x_{t+1}=(A+BK)x_t.
$$

**Proposition 26.1.** The origin is asymptotically stable for the closed-loop system if all eigenvalues of $A+BK$ lie strictly inside the unit disk:
$$
|\lambda|<1.
$$

Thus feedback design is often the problem of choosing $K$ so that unstable open-loop modes become stable after control.

In agent mathematics, this formalizes the role of regulation: proper feedback gains transform a fragile cognitive process into a self-correcting one.

### 26.6 Disturbance rejection

A good controller does more than stabilize an ideal model. It attenuates disturbance. If $w_t$ enters the dynamics, a well-designed feedback law reduces its long-term effect on the regulated variables.

This is especially important for autonomous systems operating in uncertain environments. The goal is not to eliminate all disturbance, which is impossible, but to ensure that perturbations do not drive the agent outside the safe set.

### 26.7 Model Predictive Control

Simple feedback laws react locally. More advanced control uses prediction.

**Model Predictive Control (MPC)** solves, at each time $t$, a finite-horizon optimization problem:
$$
\min_{u_t,\dots,u_{t+N-1}}
\sum_{k=0}^{N-1} \ell(x_{t+k},u_{t+k}) + \ell_f(x_{t+N})
$$

subject to system dynamics and constraints. Then only the first control $u_t$ is applied. At the next tick, the horizon shifts forward and the optimization is solved again.

This is called **receding-horizon control**.

MPC is especially appropriate for agents because it integrates prediction, constraints, and regulation. It can explicitly enforce state bounds, input limits, and safety requirements while still optimizing performance.

### 26.8 Viability and controlled invariance

Control must respect viability.

**Definition 26.1.** A set $K\subseteq X$ is **controlled invariant** if for every $x\in K$, there exists an admissible control $u$ such that the next state satisfies
$$
f(x,u)\in K.
$$

Controlled invariance means the agent can remain in $K$ indefinitely by suitable choices.

**Definition 26.2.** The **viability kernel** of a safe set $X_{\mathrm{safe}}$ is the set of initial states $x_0\in X_{\mathrm{safe}}$ for which there exists a sequence of admissible controls keeping the trajectory in $X_{\mathrm{safe}}$ for all future time.

The viability kernel is the truly survivable part of the safe set: states that are not merely safe now, but can be kept safe over time.

**Proposition 26.2.** If $K\subseteq X$ is controlled invariant and a policy $\pi$ satisfies
$$
f(x,\pi(x))\in K
\quad\text{for all }x\in K,
$$
then every trajectory starting in $K$ remains in $K$.

This proposition is immediate by induction, yet conceptually fundamental. Regulation is not only about improving performance; it is about never leaving the region from which performance remains controllable.

### 26.9 The viability-first principle

A mathematically mature autonomous system should follow the principle
$$
\text{stay in } X_{\mathrm{safe}} \text{ first, then optimize within it.}
$$

This reverses a common error in naive design, where performance is optimized first and safety is treated as an afterthought. In reality, leaving the viable set may destroy the very capacities needed for further optimization.

In this sense, control theory and optimization are hierarchically related: control enforces viability, while optimization exploits the interior freedom left by viability.

### 26.10 Plasticity gates

Some changes to an agent are structural rather than transient. Synaptic rewiring, permission revision, or identity reconfiguration may produce long-term alterations. Such plasticity should not be triggered merely because a local objective suggests it.

This requirement can be formalized by letting the admissible control set depend on state:
$$
u_t \in U(x_t).
$$

When regulatory variables indicate instability, the set $U(x_t)$ excludes structurally invasive actions. Only when coherence, reserve, and control margin exceed threshold does the **plasticity gate** open.

Mathematically, this means the feasible control set is state-dependent and itself part of the regulatory architecture. Structural optimization is subordinated to control conditions.

### 26.11 Regulation as architecture

We can now summarize the architecture of mind at the control level.

- The state $x_t$ represents the agent’s internal condition.
- Feedback compares output to target.
- Closed-loop dynamics determine whether disturbances are corrected or amplified.
- PID-like laws capture immediate, accumulated, and anticipatory correction.
- MPC integrates prediction with constraints.
- Viability theory distinguishes safe states from controllably safe states.
- Plasticity gates restrict structural change to periods of regulatory permission.

Control theory therefore completes Part V. Geometry described where states live. Dynamics described how they move. Graphs described how subsystems connect. Information theory described uncertainty and throughput. Optimization described selection under constraints. Control now describes continuous self-maintenance: the mathematics by which an autonomous system remains itself.

### Exercises

1. Consider the scalar system
$$
   x_{t+1}=ax_t+bu_t,
   \qquad
   u_t=kx_t.
$$
   Show that the closed-loop system is
$$
   x_{t+1}=(a+bk)x_t.
$$
   For which values of $k$ is the origin asymptotically stable?

2. Let
$$
   x_{t+1}=x_t+u_t,
   \qquad
   X_{\mathrm{safe}}=[-1,1],
   \qquad
   U=[-1/2,1/2].
$$
   Determine the viability kernel of $X_{\mathrm{safe}}$.

3. Suppose $K\subseteq X$ is controlled invariant. Prove Proposition 26.2 by induction on time.

4. Consider the cost over a horizon $N$:
$$
   J=\sum_{k=0}^{N-1}\bigl(x_{t+k}^2+\rho u_{t+k}^2\bigr)+x_{t+N}^2.
$$
   Explain qualitatively how increasing $\rho$ changes the behavior of an MPC controller.

5. An agent permits structural plasticity only when
$$
   C_{\mathrm{id}}\ge 0.8,\qquad F_{\mathrm{ctrl}}\ge 0.75,\qquad H(\mu)\le 0.4.
$$
   Interpret this as a state-dependent admissible-control set $U(x)$, and explain why such gating is naturally viewed as a control constraint rather than an optimization objective.

---

# Part V Summary

Part V has developed a mathematical architecture of autonomous mind.

1. **State spaces and manifolds** described the global set of possible configurations, the notion of distance between states, and the geometry of viable operation.

2. **Dynamical systems** described the evolution of those states through time, including fixed points, stability, attractors, and bifurcation.

3. **Networks and graphs** described the internal web of interacting subsystems, with Laplacian structure and spectral methods revealing coherence and modularity.

4. **Information theory** quantified uncertainty, transmission, and belief-state complexity through entropy, mutual information, KL divergence, and capacity.

5. **Optimization** formalized constrained improvement, showing how an agent allocates limited resources to maximize performance.

6. **Regulation and control** formalized feedback, closed-loop stability, predictive adjustment, viability preservation, and gated structural change.

Together, these chapters provide an undergraduate-level mathematical language for the architecture of mind in autonomous systems: a geometry of states, a dynamics of change, a topology of connection, an economy of information, a calculus of improvement, and a theory of self-maintenance.
