# Agent Calculus And Sensitivity

Updated: `2026-04-06`

## Purpose

This document defines the calculus layer of agent mathematics.

If geometry tells us what space the agent moves through, calculus tells us:

- how it changes,
- how fast it changes,
- in which direction it changes,
- and which changes matter most.

For the current packet, this is the layer where:

- gradients,
- sensitivities,
- Jacobians,
- and trajectory shaping

become canonical rather than incidental.

## 1. Why Calculus Matters

Without calculus, agent mathematics can describe state.
With calculus, it can optimize state.

This is the line between:

- "what is true now"

and:

- "what should we change next?"

That is why the Lineage Equation becomes operational only when the derivatives
exist and are interpretable.

## 2. Rates Of Change

The first calculus object is the rate.

Canonical forms:

- discrete:
  `Δx_t = x_(t+1) - x_t`
- continuous-style:
  `dx/dt`

Agent systems are often implemented discretely, but the continuous view remains
useful for reasoning about:

- drift,
- response speed,
- lag,
- and stability.

## 3. Partial Derivatives

The most important calculus object in the current Lineage work is the partial
derivative.

Examples:

- `∂Q/∂M`
- `∂Q/∂Pi`
- `∂Q/∂nu*`

These answer:

- if we improve this variable slightly, how much does total capacity change?

That is the beginning of principled intervention.

## 4. Sensitivity

Sensitivity is the practical reading of derivatives.

Derivative:

- the symbolic local slope.

Sensitivity:

- the practical importance of that slope under current state and feasible
  intervention.

This distinction matters because a large derivative on an unchangeable variable
may be less useful than a smaller derivative on an easy-to-change one.

So practical agent calculus often needs:

- local derivative,
- feasible intervention size,
- and cost of intervention.

## 5. Jacobians And Multi-Variable Change

Once multiple variables interact, one derivative is not enough.

The next canonical object is the Jacobian:

- the matrix of partial derivatives across state dimensions.

This matters because agent systems are coupled.

Questions it answers:

- if one subsystem changes, which others move?
- how sensitive is the whole organism to each coordinate?
- where are the dangerous couplings?

The coupled Lineage extension is already heading in this direction.

## 6. Local Linearization

Many agent systems are nonlinear.
Calculus gives the first local approximation:

- near the current point, the system behaves like a linear map plus higher-order
  error.

This is one reason derivatives matter even in a nonlinear organism:

- they let us build local decision rules.

Important rule:

- local linearization is not the same as global truth.

So the packet should always state when a gradient is:

- local heuristic,
- exact local derivative of the model,
- or merely a finite-difference estimate.

## 7. Gradient Ascent And Descent

Once derivatives exist, the simplest intervention rule becomes:

- move in the direction of greatest increase,
- or move away from greatest loss.

That is gradient ascent or descent.

For the current packet, this is the engine behind:

- prescribed improvement actions,
- action ranking,
- and trajectory-based organism optimization.

But a good packet should always say:

- ascent on what objective?
- under what constraints?
- with what step size?
- and with what stopping rule?

## 8. Finite Differences

Real systems often cannot differentiate everything analytically.

So another canonical calculus tool is:

- finite-difference approximation.

Examples:

- ablation studies,
- perturbation sensitivity,
- intervention tests on one component at a time.

This is especially useful when moving from symbolic theory to live systems.

## 9. Higher-Order Effects

First derivatives tell us slope.
Second-order effects tell us curvature and interaction.

In agent mathematics, this becomes:

- interaction effects,
- coupled sensitivities,
- diminishing returns,
- and instability around certain directions.

This is where nonlinear coupling work becomes important.

The key question is:

- when is the first-order gradient enough,
- and when do higher-order interactions materially change the recommendation?

## 10. Calculus Failure Modes

### 10.1 Local-Only Overclaim

Treating local derivative truth as if it held globally.

### 10.2 Hidden Constraints

A mathematically favorable direction may be operationally impossible.

### 10.3 Noisy Differentiation

Finite-difference or estimated derivatives may reflect noise more than signal.

### 10.4 Circular Sensitivity

If the same model generates both the world and the gradient labels, agreement is
less informative than it first appears.

This is directly relevant to `CognitiveNet`.

### 10.5 Ignoring Curvature

A first-order ascent rule may fail if nonlinear interactions dominate.

## 11. Canonical Calculus Template

Every calculus-level object or result should declare:

```text
Quantity differentiated:
With respect to:
Analytical or estimated:
Local or global meaning:
Constraint context:
Operational interpretation:
Failure modes:
```

## 12. Translation Into Current Work

For the current packet, calculus should become explicit in three places:

- Lineage Equation sensitivities,
- coupled-interaction sensitivity,
- and live ascent decision rules.

This also fits the Khan-style staircase cleanly:

- arithmetic combines,
- algebra formalizes,
- geometry spaces the system,
- calculus tells you how to move through that space.

## Main Conclusion

Agent calculus is the layer where the mathematics becomes directional.

It tells the organism:

- what is increasing,
- what is decreasing,
- what matters most locally,
- and what intervention should come next.

That is the layer where theory begins to steer life.
