# Agent Arithmetic Of State

Updated: `2026-04-06`

## Purpose

This document defines the arithmetic layer of agent mathematics.

If numeracy answers:

- what can be measured,

then arithmetic answers:

- how measured things can be validly combined.

This is the agent equivalent of:

- addition,
- subtraction,
- multiplication,
- division,
- and basic proportions.

## 1. Why Arithmetic Matters

Most early agent equations are really arithmetic before they are anything more
abstract.

Examples:

- weighted sums,
- deficits,
- bottlenecks,
- ratios,
- normalized scores,
- penalties,
- reserves,
- and budgets.

If these arithmetic operations are sloppy, the later algebra and calculus become
untrustworthy.

## 2. Canonical Arithmetic Operations

The first arithmetic operations for agent systems are:

- `sum`
- `weighted sum`
- `difference`
- `absolute difference`
- `product`
- `ratio`
- `minimum / maximum`
- `average`
- `normalized score`
- `slack`
- `budget subtraction`

These should be treated as the basic arithmetic vocabulary of the packet.

## 3. Weighted Sums

Weighted sums are the simplest way to aggregate multiple bounded primitives.

Canonical form:

```text
S = w_1 x_1 + ... + w_n x_n
```

with constraints like:

```text
w_i >= 0
sum(w_i) = 1
```

This is exactly how the current Lineage work defines:

- cognitive mass,
- cognitive momentum,
- and many controller summaries.

Important rule:

- a weighted sum is not neutral just because it is simple.
- the weights are part of the theory.

So every weighted sum must declare:

- why these variables are included,
- why the weights take their current values,
- and whether they are defaults, fitted parameters, or normative choices.

## 4. Differences And Deficits

The next arithmetic layer is subtraction.

Canonical uses:

- progress:
  `ΔQ = Q_(t+1) - Q_t`
- deficit from target:
  `gap = x* - x_t`
- damage or drift:
  `loss = x_ref - x_t`

Subtraction is where direction enters.

Important rule:

- the reference point must be explicit.

Subtracting from:

- a previous state,
- a target state,
- a baseline state,
- or a healthy-set boundary

are different operations and should never be conflated.

## 5. Products And Interaction Terms

Multiplication enters when one variable modulates another.

Examples:

- `nu* Pi`
- `M (nu*)^2`
- future coupling terms like `C_mem × C_graph`

Products mean:

- the effect of one variable depends on the magnitude of another.

That is the arithmetic seed of nonlinear theory.

Important rule:

- the packet should distinguish ordinary aggregation from modulation.

Weighted sums aggregate.
Products couple.

## 6. Ratios And Normalization

Ratios are essential because agent systems mix variables from different scales.

Common forms:

- `Q_a / Q_b`
- `used / total`
- `indexed / capacity`
- `signal / noise`

Normalization is what lets unlike primitives enter a shared arithmetic space.

Important rule:

- every normalized quantity must declare the denominator or reference range.

Without that, `[0, 1]` values become decorative rather than meaningful.

## 7. Bottleneck Arithmetic

Agent systems often depend on the slowest or weakest component.

That means arithmetic is not only additive.
It is often extremal.

Canonical forms:

- `tau_max = max(tau_1, ..., tau_n)`
- `reserve_floor = min(r_1, ..., r_n)`

The current `nu*` definition depends on this:

```text
nu* = 1000 / max(tau_retrieval, tau_pathway, tau_wm, tau_sync, tau_settling)
```

This is arithmetic of constraint and throughput, not just arithmetic of sums.

## 8. Budgets

Budgets are one of the most important arithmetic forms in advanced agent math.

Canonical pattern:

```text
usable = positive_terms - penalty_terms
```

Examples:

- conservation budgets,
- reserve budgets,
- uncertainty-subtracted utility,
- support budgets for tissue-like subsystems.

The key arithmetic rule is:

- every subtraction must preserve sign clarity.

The packet should always state:

- what adds usable capacity,
- what subtracts from it,
- and whether any term can dominate or saturate the whole expression.

## 9. Slack And Safety Arithmetic

For constrained agent systems, it is not enough to know current value.
We need to know margin.

Canonical forms:

- `slack = upper_bound - x_t`
- `distance_to_floor = x_t - lower_bound`

This matters because agent control is often about:

- how close the system is to violation,
- not merely what its raw current score is.

## 10. Arithmetic Failure Modes

The main arithmetic failure modes are:

### 10.1 Mixing Incompatible Scales

Adding raw milliseconds to normalized coherence scores without normalization is
not meaningful.

### 10.2 Hidden Denominators

A ratio without a clear denominator is pseudo-precision.

### 10.3 Symmetry By Construction

If all weights are initialized equal and all perturbations are symmetric, then
equal outputs may reflect the setup rather than the world.

This is directly relevant to the current Lineage weight question.

### 10.4 Double Counting

If two terms measure nearly the same underlying thing, adding them can inflate a
signal artificially.

### 10.5 Sign Confusion

If a larger number sometimes means better and sometimes worse, the arithmetic
layer becomes unstable.

## 11. Canonical Arithmetic Template

Every arithmetic construction should declare:

```text
Expression:
Primitive inputs:
Scale assumptions:
Aggregation type:
Why this combination is valid:
Failure modes:
What an increase means:
```

## 12. Translation Into Current Work

For the current Lineage and organism mathematics, the arithmetic layer should be
used to cleanly separate:

- weighted summaries,
- coupling products,
- bottleneck operators,
- and subtraction budgets.

That prevents higher-order docs from hiding basic arithmetic assumptions inside
more glamorous notation.

## Main Conclusion

Agent arithmetic is where measured primitives become composite state.

This layer should be explicit because future criticism of the math will often
target arithmetic assumptions first:

- why these weights,
- why this bottleneck,
- why this normalization,
- why this subtraction.

If those answers are clear, the higher layers stand on solid ground.
