# Notation Policy

Updated: `2026-04-05`

## Purpose

This file defines the notation policy for the mathematics packet.

It is not a glossary.
It is the rule set that governs how notation must be introduced, reused, extended, and stabilized across the packet.

The policy exists to stop three failure modes:

- symbol collision,
- silent symbol drift,
- and multiple incompatible mathematical dialects for the same organism.

## Scope

This policy applies to:

- basis documents,
- formal extensions,
- implementation specifications,
- compatibility notes,
- and any later mathematics or control research added to this packet.

## Canonical Authority Order

When there is a notation conflict, resolve it in this order:

1. `ORGANISMIC_INTELLIGENCE_MATHEMATICAL_BASIS.md`
2. `SYMBOLS_AND_NOTATION_GLOSSARY.md`
3. the relevant subsystem extension document
4. local document-specific notation

This means:

- the basis defines the primitive categories,
- the glossary defines the canonical symbol meanings,
- subsystem files may refine local structure,
- but local files may not silently redefine canonical symbols.

## Core Principles

### 1. One symbol, one stable meaning

A symbol should have one canonical meaning across the packet.

Examples:

- `D_t` = differentiable substrate state
- `Ψ_t` = governance state
- `Σ_t` = nervous-system state
- `B_t` = blood-system state
- `𝒪_t` = full organism state

### 2. Reuse before inventing

Before creating a new symbol:

- check whether the idea already fits an existing object,
- check whether it is a component, mode, event, or operator of an existing object,
- and prefer subscripts or superscripts over introducing a new top-level state symbol.

### 3. Extension by structure, not by renaming

If a concept is a refinement of an existing state, extend that state structurally instead of renaming the whole object.

Good:

- add `A_t^tool` as a new afferent type under `A_t`
- add `h_mem` as a new health component under `H_t`

Bad:

- invent a new aggregate object when `Σ_t` already holds the concept
- rename `Ψ_t` to a new top-level symbol for the same governance layer

### 4. Basis objects outrank intermediate aggregates

The packet now has a basis-level whole-organism object:

```text
𝒪_t = (D_t, Ψ_t, Σ_t, B_t)
```

Use `𝒪_t` for basis-level writing.

Older aggregate forms such as `Ω_t` or `Z_t` may remain in historical extension documents, but new documents should translate them back to `𝒪_t` unless there is a strong local reason not to.

### 5. Research notation and code notation must be linked

Research documents may use canonical mathematical typography.
Implementation documents should preserve the same meaning while allowing ASCII-safe aliases when needed.

Example:

- research notation: `D_t = (θ_t, alpha_t, χ_t, ω_t)`
- code-facing alias: `D_t = (theta_t, alpha_t, chi_t, omega_t)`

The meaning must stay the same even if the glyphs differ.

## Symbol Classes

The following classes must remain visually and semantically distinct.

### Basis and family symbols

Use calligraphic capitals for families and sets:

- `𝒮` = state-space family
- `𝓘` = interface-map family
- `𝓤` = update-operator family
- `𝓒` = constraint family
- `𝓜` = mode set
- `𝓔` = event set
- `𝓣` = timescale ordering

### Compound state objects

Use uppercase Greek or Latin symbols with time index:

- `D_t`
- `Ξ_t`
- `Ψ_t`
- `Σ_t`
- `B_t`
- `𝒪_t`

### Component states

Use lowercase symbols for component states and scalar or vector members:

- `r_t`, `x_t`, `μ_t`, `m_t`, `a_t`
- `ρ_t`, `Λ_t`, `N_t`
- `A_t`, `J_t`, `K_t`, `P_t`, `E_t`, `M_t`, `H_t`
- `Pl_t`, `Ma_t`, `Li_t`, `De_t`, `St_t`, `Cl_t`, `Hb_t`

### Operators and maps

Use capitalized names or Greek operator symbols:

- `ReadCtx`
- `InputCompose`
- `SubstrateUpdate`
- `GovernanceUpdate`
- `NervousUpdate`
- `BloodUpdate`
- `PlasticityUpdate`
- `Π_r`
- `Π_consistency`
- `ψ_write`, `ψ_emit`, `ψ_bias`

### Constraints, barriers, and losses

Use:

- `X_*` for admissible or viable sets
- `Φ_*` for viability penalties, barriers, or potentials
- `L_*` for optimization losses

### Modes and events

Use plain text names for discrete modes and events:

- modes: `homeostasis`, `adaptive`, `inflammatory`, `pathological`, `regenerative`
- events: `spawn_branch`, `quarantine_branch`, `promote_branch`, `trigger_regeneration`

## Reserved Symbols

These meanings are reserved and must not be reassigned.

- `𝒪_t` = full organism state
- `D_t` = differentiable substrate
- `Ξ_t` = organism-visible core bundle
- `Ψ_t` = governance state
- `Σ_t` = nervous-system state
- `B_t` = blood-system state
- `a_t` = governance action
- `m_t` = operating mode
- `alpha_t` = fast activation state
- `Π_*` = projection or consistency maps
- `Φ_*` = viability penalties or barriers
- `L_*` = losses
- `τ_*` = subsystem timescales

## Collision Rules

The following rules are mandatory.

### `a_t` versus `alpha_t`

- use `a_t` only for governance action
- use `alpha_t` for fast activation state
- do not shorten `alpha_t` to `a_t`

### `𝒪_t` versus `Ξ_t`

- use `𝒪_t` for the full organism
- use `Ξ_t` only for the organism-visible core bundle
- do not use `Ξ_t` to mean the whole organism

### `Σ_t` versus generic signaling state

- use `Σ_t` only for the nervous-system aggregate
- if a local signaling component is needed, make it a member of `Σ_t`

### `B_t` versus generic support state

- use `B_t` only for the blood-system aggregate
- if a local support concept is needed, make it a member of `B_t`

### `Φ_*` versus `L_*`

- `Φ_*` means viability pressure, safety barrier, or health penalty
- `L_*` means optimization or fitting loss
- do not use `Φ_*` and `L_*` interchangeably

## Rules For Introducing New Symbols

Every new symbol must pass this test.

### Step 1. Check whether the symbol is actually needed

A new symbol is allowed only if:

- an existing symbol cannot express the idea cleanly,
- the new object has stable meaning across more than one equation,
- or the object is structurally important enough to deserve its own name.

### Step 2. Define type and role at first use

At first introduction, define:

- what the symbol means,
- whether it is a state, operator, constraint, mode, or event,
- its domain and codomain if it is a map,
- its timescale if relevant,
- and its relation to the basis objects.

### Step 3. Prefer local refinement before top-level expansion

Prefer:

- `A_t^tool`
- `H_t^mem`
- `ΔΣ_t`

before inventing:

- a new top-level state object
- a new whole-organism aggregate
- or a renamed basis object

### Step 4. Add stable symbols to the glossary

If the symbol is expected to recur across documents, add it to:

- `SYMBOLS_AND_NOTATION_GLOSSARY.md`

If it is only local, define it clearly in the local file and keep it local.

## Required Definition Format

When introducing a nontrivial new symbol, use a local definition block with:

1. compact equation form
2. one-line semantic meaning
3. component meanings if it is compound
4. relation to parent objects

Example:

```text
Q_t = (q_load, q_age, q_priority)
```

- `Q_t` = queue-state bundle
- `q_load` = current queue load
- `q_age` = age pressure
- `q_priority` = priority distribution

## Subscripts And Superscripts Policy

Use indices consistently.

### Subscripts

- `_t` = time index
- `_r` = region-specific scalar or component
- `_i` = item, route, or packet index

### Superscripts

- `^act` = action channel
- `^auto` = autonomic channel
- `^exo` = exogenous input
- `^intero` = interoceptive input
- `^mem` = memory-derived signal
- `^err` = error or anomaly channel
- `^gov` = governance-derived channel

Do not overload superscripts for unrelated meanings inside the same document.

## Local Alias Policy

Aliases are allowed only when they improve code-facing readability or avoid glyph friction.

Allowed examples:

- `theta_t` as ASCII alias for `θ_t`
- `chi_t` as ASCII alias for `χ_t`
- `Psi_t` as ASCII alias for `Ψ_t` in code comments or implementation notes

Not allowed:

- changing the semantic meaning of the symbol
- inventing aliases that hide the connection to the canonical object

If an alias is used, define it once and keep it consistent.

## Document Structure Policy

A formal math document should usually contain:

1. purpose
2. object definition
3. component definitions
4. operator definitions
5. constraints
6. objective or control law
7. interpretation

This is not a cosmetic rule.
It makes symbol meaning recoverable without guessing.

## Migration Policy For Older Documents

Older documents in the packet may contain intermediate notations such as:

- `Ω_t`
- `Z_t`

These should be treated as historical local aggregates, not new basis objects.

When referencing those files in new work:

- map them back to `𝒪_t` where possible,
- preserve the historical symbol only when quoting or discussing that file locally,
- and avoid reintroducing those aggregates into new top-level documents.

## Review Policy

Before a new mathematics file is treated as canonical, it should be checked for:

- collision with reserved symbols
- untyped new objects
- missing domain or role definitions
- inconsistent use of `Φ_*` versus `L_*`
- inconsistent use of `a_t` versus `alpha_t`
- aggregate drift away from `𝒪_t`

## Final Rule

The packet should behave like one mathematical language with many modules, not many local dialects with shallow bridges.

If a new file cannot be read consistently through:

- `ORGANISMIC_INTELLIGENCE_MATHEMATICAL_BASIS.md`
- `SYMBOLS_AND_NOTATION_GLOSSARY.md`
- and this policy

then the notation should be revised before the file becomes canonical.
