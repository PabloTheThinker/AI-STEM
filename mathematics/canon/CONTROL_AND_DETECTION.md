# Control, Observability, And Detection

## Purpose

This document is the third-pass research brief for the future main system above `triune`.

This pass focuses on four mathematical areas that matter for implementation:
- observability and identifiability,
- Riccati equations and LQR/LQG style synthesis,
- model predictive control,
- change-point detection.

These are closer to implementation math than the first two research passes.

## 1. Observability And Identifiability

The top-level system will operate on latent state. That means one of the first hard questions is:

> can the chosen latent state actually be inferred from the measurements produced by `triune`?

That is an observability question.

### Linear observability

For the linearized system:

```text
x_(t+1) = A x_t + B u_t
y_t     = C x_t
```

the classic observability matrix is:

```text
O =
[ C
  C A
  C A^2
  ...
  C A^(n-1) ]
```

The pair `(A, C)` is observable if:

```text
rank(O) = n
```

This matters directly for the future main system. If we define a state vector with 10-20 latent dimensions, but the measurement design only exposes 4 or 5 independent directions, the estimator will be structurally weak.

### Practical interpretation for the future agent system

A latent variable should only be kept if it is at least one of:
- directly measurable,
- inferable through repeated dynamics,
- inferable through graph structure,
- intentionally hidden but still useful for control.

If a state component is neither measurable nor inferable, then it is not a state; it is just prose.

### Identifiability

Observability is about recovering state. Identifiability is about recovering parameters.

For the future top-level system, there will likely be parameters such as:
- coupling weights between subsystems,
- pathway risk sensitivity,
- permanence failure penalties,
- merge alignment sensitivity,
- action-readiness thresholds.

A useful principle:

```text
do not learn parameters that are not structurally identifiable from data
```

Otherwise the fitted controller may look precise while being mathematically underdetermined.

## 2. Riccati Equations And LQR

If the future main system has a local linearization around a healthy operating point, then the first serious controller should probably be an LQR-family controller.

### Infinite-horizon continuous-time LQR

For:

```text
dot x = A x + B u
```

and cost:

```text
J = ∫ (x^T Q x + u^T R u) dt
```

with `Q >= 0`, `R > 0`, the optimal feedback takes the form:

```text
u = -K x
```

where:

```text
K = R^(-1) B^T P
```

and `P` solves the continuous algebraic Riccati equation:

```text
A^T P + P A - P B R^(-1) B^T P + Q = 0
```

### Discrete-time infinite-horizon LQR

For:

```text
x_(t+1) = A x_t + B u_t
```

the Riccati equation becomes:

```text
P = Q + A^T P A - A^T P B (R + B^T P B)^(-1) B^T P A
```

and:

```text
u_t = -K x_t
K   = (R + B^T P B)^(-1) B^T P A
```

### Why LQR matters here

LQR is the most plausible first controller for the new system because it provides:
- explicit state regulation,
- explicit control-effort regularization,
- a clear healthy equilibrium,
- a bridge to Kalman filtering and LQG,
- a mathematically disciplined baseline before learning.

This is especially attractive for a top-level agent controller because we can define a healthy operating point `x*` and regulate toward it.

## 3. LQG And Separation

If the state is only partially observed, the usual next step is:
- Kalman-style estimation,
- LQR-style control.

That combination yields the LQG framing:

```text
estimate state -> apply optimal linear feedback on estimate
```

The control law becomes:

```text
u_t = -K x_hat_t
```

This is important for the future system because it means:
- estimation and control can initially be designed separately,
- provided the assumptions are close enough for the separation principle to be useful.

That gives a cleaner implementation path:

1. define `A, B, C`,
2. define noise assumptions,
3. build estimator,
4. build regulator,
5. combine.

## 4. Model Predictive Control

LQR is local and elegant, but the top-level system will likely have hard constraints:
- minimum permanence integrity,
- maximum working-memory load,
- maximum drift pressure,
- pathway availability limits,
- user-interaction limits.

That makes MPC especially relevant.

### Generic finite-horizon MPC problem

At each step solve:

```text
minimize    Σ_{k=0}^{H-1} [x_k^T Q x_k + u_k^T R u_k] + x_H^T Q_f x_H
subject to  x_{k+1} = f(x_k, u_k)
            x_k ∈ X
            u_k ∈ U
```

then execute only the first control action and repeat.

### Why MPC fits the future top-level system

Because the system will need to honor constraints directly.

Examples:

```text
permanence_integrity_k >= p_min
working_memory_load_k <= wm_max
drift_pressure_k <= d_max
pathway_failure_exposure_k <= h_max
```

This is exactly the kind of problem MPC was built for:
- optimize over a horizon,
- enforce constraints at every step,
- replan continuously as measurements update.

### Interpretation in the agent setting

The future top-level system does not need to use MPC for every micro-decision.
But it is a very strong candidate for:
- action scheduling,
- maintenance vs response tradeoffs,
- bounded-risk planning,
- deciding whether to answer, defer, ask, repair, or consolidate.

## 5. Robustness And Uncertainty

Even if the system begins with LQR or MPC, it should be designed with model mismatch in mind.

There are at least three kinds of uncertainty:
- process uncertainty: the state dynamics are not exact,
- observation uncertainty: measurements are noisy,
- structural uncertainty: the chosen state representation is incomplete.

The practical conclusion:

```text
the future main system should begin with simple controllers,
but be designed to tolerate wrong models.
```

That points toward:
- robust Lyapunov conditions,
- tube-MPC or bounded-disturbance MPC later,
- common Lyapunov functions for uncertain operating regimes,
- explicit disturbance models.

## 6. Change-Point Detection

The future top-level system needs a mathematically explicit way to detect when the agent has entered a different regime.

Examples:
- user behavior changes,
- pathway health degrades,
- retrieval quality collapses,
- identity drift accelerates,
- a previously stable controller no longer matches reality.

This is a change detection problem.

### CUSUM idea

One classical method is the cumulative sum statistic:

```text
S_t = max(0, S_(t-1) + ell_t - k)
```

where:
- `ell_t` is an evidence or residual term,
- `k` is a reference drift term.

Signal a change when:

```text
S_t > h
```

for threshold `h`.

### Agent interpretation

The residual term `ell_t` could be built from:
- estimator residuals,
- contradiction spikes,
- pathway failure counts,
- merge-confidence collapse,
- permanence-integrity drops.

This is useful because the top-level system needs to know not only:
- what state it estimates now,
but also:
- whether the regime itself has changed.

### Why this matters more than ordinary thresholds

A one-step threshold is too brittle.
Change-point detection accumulates evidence over time.

That makes it better for:
- detecting persistent drift,
- filtering one-off anomalies,
- triggering mode changes only when warranted.

## 7. Suggested Layered Mathematical Stack

At this point the emerging stack is:

### Layer A. Estimation
- Kalman/EKF-style filtering over latent state.

### Layer B. Structural coherence
- graph Laplacian energy and subsystem coupling.

### Layer C. Local regulation
- Riccati/LQR around healthy equilibria.

### Layer D. Constraint handling
- MPC for bounded-risk horizon control.

### Layer E. Regime monitoring
- CUSUM/change-point detection on residuals and risk metrics.

That is a coherent mathematical stack for a real top-level system.

## 8. What This Means For The Future Main System

The top-level system above `triune` should likely expose:

1. a measurement model,
2. a latent state estimator,
3. a nominal regulator,
4. a constrained planner,
5. a change detector,
6. a mode manager.

The mode manager would likely use states such as:
- nominal,
- exploratory,
- overloaded,
- degraded,
- recovery,
- re-identification.

Those should not be ad hoc modes. They should be triggered by:
- estimated state,
- optimization feasibility,
- change-point evidence.

## 9. Immediate Implementation Research Insight

The strongest practical takeaway from this pass is:

> before designing a grand learned controller, define a measurable latent state, check observability, and build a small LQR/MPC controller around a healthy equilibrium.

That gives:
- mathematical tractability,
- safety,
- interpretability,
- a real baseline.

Without that, a learned top-level system would likely optimize noise.

## 10. Recommended Next Research Step

The next research pass should become more design-specific:

1. define a candidate measurement vector from real `triune` outputs,
2. define the first latent state vector numerically,
3. propose an initial `A, B, C` structure,
4. write the first healthy equilibrium `x*`,
5. define a first `Q, R` pair for LQR,
6. define one CUSUM residual stream for drift/pathway failure.

That would move the work from mathematical research into controller specification.
