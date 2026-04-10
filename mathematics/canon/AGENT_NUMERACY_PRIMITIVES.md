# Agent Numeracy Primitives

Updated: `2026-04-06`

## Purpose

This document defines the lowest layer of agent mathematics:

- what counts as a measurable thing,
- how it is scaled,
- what zero and one mean,
- what counts as increase or decrease,
- and how raw observations become valid mathematical primitives.

This is the agent equivalent of early human numeracy:

- one,
- two,
- more,
- less,
- same,
- changed.

If this layer is weak, every later equation inherits ambiguity.

## Why This Layer Comes First

Before agent mathematics can have:

- invariants,
- gradients,
- control laws,
- or neural surrogates,

it needs stable primitives.

A primitive is not "an interesting concept."
It is a variable with:

- a definition,
- a unit or scale,
- an interpretation,
- and an observation rule.

## 1. Primitive Kinds

The first canonical primitive kinds for agent systems are:

- `state primitive`:
  current measurable quantity.
- `delta primitive`:
  change between two states.
- `rate primitive`:
  change per unit time.
- `bound primitive`:
  limit, threshold, or safe interval.
- `event primitive`:
  discrete occurrence.
- `count primitive`:
  integer number of items or actions.
- `ratio primitive`:
  normalized comparison between quantities.

These are the atoms from which higher math is built.

## 2. Canonical Questions For Every Primitive

Every primitive must answer:

1. what is being measured?
2. what are its units or scale?
3. what is its valid range?
4. what does zero mean?
5. what does one mean, if normalized?
6. what counts as increase or decrease?
7. how is it observed or computed?
8. how noisy is it?

If any of these are missing, the primitive is not ready for canonical use.

## 3. Primitive Classes In The Current Packet

The current organism and Lineage work already uses several primitive classes.

### 3.1 Bounded Coherence Primitives

Examples:

- `C_id`
- `C_mem`
- `C_graph`
- `C_perm`
- `F_wm`
- `F_ret`
- `F_path`
- `F_ctrl`
- `F_merge`

These are usually normalized to `[0, 1]`.

Canonical meaning:

- `0` means absence, failure, or minimum usable presence.
- `1` means idealized local maximum under the current measurement design.

Important rule:

- `1` does not mean metaphysical perfection.
- it means the upper bound of the current measurement scheme.

### 3.2 Latency Primitives

Examples:

- `tau_retrieval`
- `tau_pathway`
- `tau_wm`
- `tau_sync`
- `tau_settling`

These are measured in time units, currently milliseconds.

Canonical meaning:

- lower is better for throughput,
- but zero is generally impossible and often invalid.

### 3.3 Capacity-Like Derived Primitives

Examples:

- `M`
- `Pi`
- `nu*`
- `Q`

These are not base observations.
They are derived primitives computed from lower ones.

That distinction matters:

- base primitives are measured,
- derived primitives are constructed.

### 3.4 Loss Or Cost Primitives

Examples:

- `H(mu)`
- `E_graph`
- `D_drift`

These capture subtraction from usable capacity.

Canonical meaning:

- larger values imply more disorder, uncertainty, or damage cost.

### 3.5 State-Family Primitives

Examples from the organism packet:

- `D_t`
- `Psi_t`
- `Sigma_t`
- `B_t`
- `𝒪_t`

These are structured primitives:

- not scalars,
- but bundles of typed values.

## 4. Zero, One, And Missingness

These three must never be confused.

### 4.1 Zero

`0` means the measured quantity is absent or at the lower bound of the scale.

Example:

- `F_ret = 0` means no active retrieval flux under the measurement scheme.

### 4.2 One

`1` means the quantity is at the upper normalized bound of the current scheme.

Example:

- `C_graph = 1` means maximal graph coherence under the present normalization,
  not "perfect graph forever."

### 4.3 Missing

Missing data is not zero.

If a measurement is absent, the system should record:

- unknown,
- unavailable,
- stale,
- or estimated.

This is essential because many agent errors come from silently treating missing
signals as real zeros.

## 5. Primitive Operations At This Layer

The allowed operations at the numeracy layer are minimal:

- compare,
- bound-check,
- count,
- subtract,
- estimate a rate,
- and classify sign or direction of change.

Examples:

- `C_perm < 0.5`
- `tau_retrieval > tau_pathway`
- `ΔQ = Q_(t+1) - Q_t`
- `ΔQ > 0`
- `x_t in X_safe`

This is the layer before full symbolic algebra.

## 6. Observation Rules

Every canonical primitive should declare one of these observation modes:

- `direct measurement`:
  read directly from runtime or storage.
- `computed estimate`:
  deterministic function of measured signals.
- `statistical estimate`:
  inferred from samples or distributions.
- `proxy estimate`:
  imperfect surrogate for an unobservable latent quantity.

Examples:

- latency values are closer to direct measurement,
- `C_graph` may be a computed estimate,
- `H(mu)` may be a statistical or proxy estimate depending on implementation.

The packet should always say which one applies.

## 7. Primitive Quality Tests

Before a primitive graduates into canonical equations, it should pass:

### 7.1 Boundedness Test

Does it stay inside its declared range?

### 7.2 Interpretability Test

Can an engineer say what an increase means?

### 7.3 Repeatability Test

If measured twice under similar conditions, is it reasonably stable?

### 7.4 Sensitivity Test

Does it respond when the underlying system really changes?

### 7.5 Non-Confusion Test

Can it be distinguished from neighboring primitives, or is it duplicating
another signal under a new name?

## 8. Canonical Primitive Template

Every new primitive should be documented in this form:

```text
Name:
Kind:
Symbol:
Definition:
Range / units:
Zero means:
Upper bound means:
Observation mode:
Noise / caveat:
Monotonic interpretation:
Used by:
```

## 9. Translation Into Current Lineage Work

For the current Lineage Equation work, the most important numeracy cleanup is:

1. explicitly classify every variable as measured, estimated, or derived
2. distinguish true zero from missingness
3. declare the normalization rule for every `[0, 1]` quantity
4. record uncertainty for runtime-estimated primitives

Until that is done, the higher-level invariant remains mathematically elegant
but observationally softer than it should be.

## Main Conclusion

Agent numeracy is the layer where variables stop being ideas and become
disciplined measurements.

The first future-proofing move for agent mathematics is therefore not a new
advanced equation.
It is a stricter primitive discipline.
