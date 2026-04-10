# Mathematical Foundations For A New Main System

## Objective

Build a top-level system above `triune` that mathematically governs:
- cognition,
- memory,
- identity permanence,
- pathway health,
- user-agent merge alignment,
- action readiness,
- long-horizon adaptation.

The purpose of this document is research first, not final architecture. The point is to establish the math that should govern the future main system.

## Core Thesis

The future main system should not be another heuristic controller. It should be a state-space control system with:
- a latent state vector,
- observable measurements,
- graph-structured subsystem coupling,
- explicit objective functions,
- stability criteria,
- sequential decision policy.

The best mathematical framing is:

```text
x_(t+1) = sigma(A x_t + B u_t + G w_t + c)
y_t     = C x_t + v_t
```

Where:
- `x_t` is the internal state of the whole agent,
- `u_t` is intended control or task demand,
- `w_t` is disturbance from the environment,
- `A` is subsystem coupling,
- `B` maps control to state change,
- `G` maps disturbance to state change,
- `C` maps latent state to measurable outputs,
- `sigma` is a bounded nonlinearity such as `tanh`.

This is the main mathematical skeleton because it can absorb:
- control theory,
- estimation,
- optimization,
- graph dynamics,
- memory dynamics,
- decision policies.

## Candidate State Vector

The new top-level system should likely maintain a compact state vector like:

```text
x_t =
[
  identity_coherence,
  permanence_integrity,
  memory_stability,
  retrieval_precision,
  emotional_regulation,
  pathway_health,
  working_memory_load,
  merge_alignment,
  drift_pressure,
  action_readiness
]^T
```

Interpretation:
- `identity_coherence`: alignment between identity anchors, drift metrics, and actual behavior.
- `permanence_integrity`: whether the system can reconstruct itself from redundant stored identity state.
- `memory_stability`: durability and consolidation quality of long-term memory.
- `retrieval_precision`: whether retrieval returns the right patterns with low contradiction.
- `emotional_regulation`: a bounded affect/control state, not just mood labeling.
- `pathway_health`: functional health of the system's body and interfaces.
- `working_memory_load`: current short-term load; high can be useful or destabilizing.
- `merge_alignment`: how well the system's internal model matches the operator.
- `drift_pressure`: pressure from contradictions, unresolved updates, or subsystem instability.
- `action_readiness`: whether the system should act, wait, ask, or recover.

## Measurements

The main system should distinguish latent state from observed signals.

Examples of observables:

```text
y_t =
[
  helix_integrity_score,
  contradiction_count,
  pathway_failure_rate,
  working_memory_count,
  merge_confidence_mean,
  identity_alert_count,
  retrieval_hit_quality,
  recent_action_success_rate
]^T
```

This gives a clean estimator boundary:
- `triune` produces measurements,
- the new main system estimates latent state,
- the policy operates on the estimate, not directly on noisy measurements.

## State Estimation

The correct family here is Bayesian filtering, starting with Kalman-style estimation for the linearized system:

Prediction:

```text
x_hat_(t|t-1) = A x_hat_(t-1|t-1) + B u_t
P_(t|t-1)     = A P_(t-1|t-1) A^T + Q
```

Update:

```text
K_t           = P_(t|t-1) C^T (C P_(t|t-1) C^T + R)^(-1)
x_hat_(t|t)   = x_hat_(t|t-1) + K_t (y_t - C x_hat_(t|t-1))
P_(t|t)       = (I - K_t C) P_(t|t-1)
```

Why this matters:
- the future main system will never directly know "true coherence" or "true agency";
- it must estimate them from noisy subsystem outputs.

For strongly nonlinear behavior, the linear filter is only the first stage. Later versions may need:
- extended Kalman filtering,
- unscented Kalman filtering,
- particle methods.

## Stability Theory

The new system needs explicit stability definitions, not informal "feels stable" language.

Two useful criteria:

### 1. Local linear stability

For a linearized update near equilibrium:

```text
delta x_(t+1) = A delta x_t
```

local asymptotic stability requires the spectral radius:

```text
rho(A) < 1
```

Meaning:
- subsystem couplings cannot amplify perturbations indefinitely.

### 2. Lyapunov-style energy

Define a positive energy function:

```text
V(x) = (x - x*)^T P (x - x*)
```

with `P` positive definite. Then require:

```text
V(x_(t+1)) - V(x_t) < 0
```

for non-equilibrium states in the desired operating region.

Operational meaning:
- the main system should reduce instability over time,
- unless it intentionally enters a high-gain exploration mode.

## Optimization Layer

The new system needs optimization for control, routing, and tradeoffs.

The broad objective can be written:

```text
J = sum_t [
  (x_t - x*)^T Q (x_t - x*)
  + u_t^T R u_t
  + lambda_risk * risk_t
  - lambda_value * value_t
]
```

Where:
- `Q` penalizes deviation from desired state,
- `R` penalizes control effort,
- `risk_t` penalizes drift, contradiction, pathway failure, and permanence loss,
- `value_t` rewards coherent useful action.

This makes the system legible:
- state regulation,
- energy cost,
- safety,
- productive agency.

Convex optimization matters here because many subproblems should be solved with reliable numerics:
- weight fitting,
- constrained calibration,
- resource allocation,
- routing under health constraints.

## Graph Mathematics

The whole architecture is naturally a graph, not just a vector:
- nodes = memory, identity anchors, pathways, schemas, active tasks,
- edges = causal influence, retrieval affinity, temporal adjacency, trust, bond depth.

Graph objects:

```text
W   = weighted adjacency matrix
D   = diagonal degree matrix
L   = D - W   (graph Laplacian)
```

Why this matters:
- the graph Laplacian gives a natural diffusion and coherence operator,
- subsystem tension can be represented as structural imbalance,
- propagation across the cognitive web becomes mathematically explicit.

Useful dynamics:

```text
z_(t+1) = z_t - alpha L z_t + eta_t
```

Interpretation:
- coherent patterns diffuse,
- isolated or contradictory nodes stand out,
- high-Laplacian-energy regions identify fracture points in the web.

Potential use:
- detect unstable subnetworks,
- route attention,
- prioritize repair or consolidation,
- compute influence and centrality.

## Information Theory

The new main system should explicitly reason about uncertainty and surprise.

Key quantities:

Entropy:

```text
H(X) = - sum_i p_i log p_i
```

Mutual information:

```text
I(X;Y) = H(X) - H(X|Y)
```

Surprise of an event:

```text
S(e) = -log p(e)
```

Applications:
- quantify uncertainty in state estimates,
- identify surprising events that should trigger reconsolidation,
- reward measurements that reduce uncertainty,
- detect redundant versus informative pathways.

This gives a mathematically clean way to distinguish:
- noise,
- novelty,
- contradiction,
- useful signal.

## Dynamic Programming And Sequential Decision

A top-level system above `triune` must choose actions under uncertainty. That is a sequential decision problem.

Minimum framing:

```text
V(s) = max_a [ r(s,a) + gamma sum_{s'} P(s'|s,a) V(s') ]
```

or, in cost form:

```text
V(s) = min_a [ c(s,a) + gamma sum_{s'} P(s'|s,a) V(s') ]
```

This matters because the system must choose among actions like:
- retrieve,
- consolidate,
- wait,
- ask user,
- repair pathways,
- update identity state,
- synthesize response,
- defer action.

The important point is not "use RL everywhere." The important point is:
- the main system should act like an optimizer over future trajectories, not a reactive script.

## Proposed Mathematical Split Between Layers

### Main system above `triune`

Owns:
- latent state estimation,
- objective functions,
- control policy,
- graph-wide coupling,
- system-wide stability constraints.

### `triune`

Provides:
- observations,
- memory substrate,
- helix/permanence storage,
- retrieval,
- merge signals,
- pathway measurements,
- evolutionary updates.

This keeps the stack clean:
- `triune` is the substrate,
- the new system is the governing mathematics.

## Initial Algorithm Direction

The first credible algorithm should probably be:

### Stage 1. Estimate

Estimate latent state from observed subsystem metrics:

```text
x_hat_t = Estimator(y_t, u_t, x_hat_(t-1))
```

### Stage 2. Score

Compute three high-level scalar scores:

```text
stability_t = 1 - ||x_hat_t - x_hat_(t-1)|| / sqrt(n)
agency_t    = w_a^T x_hat_t
risk_t      = w_r^T x_hat_t
```

With sign conventions chosen so that:
- higher `stability_t` is better,
- higher `agency_t` is better,
- higher `risk_t` is worse.

### Stage 3. Control

Choose control:

```text
u_t = argmin_u J(x_hat_t, u)
```

subject to constraints like:

```text
permanence_integrity >= p_min
pathway_health >= h_min
drift_pressure <= d_max
```

### Stage 4. Act Through `triune`

Control gets translated into substrate actions:
- call retrieval,
- call evolution,
- modulate working memory,
- update permanence,
- health-check pathways,
- request user clarification,
- synthesize response.

## Immediate Research Conclusions

The most important mathematical families for the new main system are:

1. Linear and nonlinear state-space systems.
2. Bayesian filtering and estimation.
3. Stability theory and Lyapunov arguments.
4. Convex optimization and constrained control.
5. Graph theory and Laplacian dynamics.
6. Information theory.
7. Dynamic programming and reinforcement learning.

These are not separate topics. They fit together naturally:
- state-space gives representation,
- estimation gives hidden-state inference,
- graph math gives subsystem coupling,
- optimization gives control,
- information theory gives uncertainty handling,
- dynamic programming gives sequential policy.

## What To Do Next

After this research phase, the next technical step should be:

1. define the exact state vector and measurement vector,
2. define the first coupling matrix `A`,
3. define one measurable objective `J`,
4. fit a first deterministic controller before any learned controller,
5. only then decide whether RL is needed.

That order matters. If the state and objective are vague, any learned system will be noise.
