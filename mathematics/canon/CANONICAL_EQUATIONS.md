# Canonical Equations

Updated: `2026-04-05`

## Purpose

This file defines the canonical equations of the mathematics packet.

It is derived from:

- `ORGANISMIC_INTELLIGENCE_MATHEMATICAL_BASIS.md`
- `SYMBOLS_AND_NOTATION_GLOSSARY.md`
- `NOTATION_POLICY.md`

Its role is to provide one compact equation set that later documents and implementations can treat as the current canonical system.

## Rule Of Interpretation

These equations are canonical at the basis level.

That means:

- use `𝒪_t` as the full organism object,
- use `Ξ_t` only for the organism-visible core bundle,
- treat older `Ω_t` and `Z_t` forms as historical local shorthands,
- and read all subsystem equations as parts of one coupled organism.

## 1. Basis Object

The organismic basis is:

```text
𝔅_org = (𝒮, 𝓘, 𝓤, 𝓒, 𝓜, 𝓔, 𝓣)
```

with:

```text
𝒮 = 𝒮_D × 𝒮_Ψ × 𝒮_Σ × 𝒮_B
```

## 2. Canonical State Equations

The full organism state is:

```text
𝒪_t = (D_t, Ψ_t, Σ_t, B_t)
```

The differentiable substrate state is:

```text
D_t = (θ_t, alpha_t, χ_t, ω_t)
```

The governance state is:

```text
Ψ_t = (Ξ_t, ρ_t, Λ_t, N_t, m_t, a_t)
```

The organism-visible core bundle is:

```text
Ξ_t = (r_t, x_t, μ_t, G_t, s_t, q_t, u_t, y_t)
```

The nervous-system state is:

```text
Σ_t = (A_t, J_t, K_t, P_t, E_t, M_t, H_t)
```

The blood-system state is:

```text
B_t = (Pl_t, Ma_t, Li_t, De_t, St_t, Cl_t, Hb_t)
```

## 3. Projection And Interface Equations

Projection consistency from substrate to organism-visible state:

```text
r_t = Π_r(D_t)
```

Read-side interface:

```text
c_t = ReadCtx(x_t, G_t, A_t, Pl_t, M_t)
ι_t = InputCompose(y_t, c_t)
```

Write-side interfaces:

```text
ψ_write : (D_t, Ψ_t, Σ_t, B_t) -> Δx_t
ψ_emit  : (D_t, Ψ_t, Σ_t, B_t) -> E_t^act
ψ_bias  : (D_t, Ψ_t, Σ_t, B_t) -> ΔΣ_t
```

Inter-tissue coupling:

```text
TissueCouple : (Ψ_t, Σ_t, B_t) -> (ΔΣ_t, ΔB_t, ΔΨ_t)
```

## 4. Substrate Equations

The fast substrate forward law is:

```text
(alpha_(t+1), χ_(t+1)) = ForwardStep(θ_t, ι_t, χ_t, M_t)
```

The projected organism-visible internal state is then:

```text
r_(t+1) = Π_r(D_(t+1))
```

The organism-facing writes are:

```text
Δx_t    = ψ_write(D_(t+1), Ψ_t, Σ_t, B_t)
E_t^act = ψ_emit(D_(t+1), Ψ_t, Σ_t, B_t)
ΔΣ_t    = ψ_bias(D_(t+1), Ψ_t, Σ_t, B_t)
```

When structural learning is permitted:

```text
(θ_(t+1), ω_(t+1)) = PlasticityUpdate(θ_t, ω_t, 𝒪_t)
```

When plasticity is closed:

```text
θ_(t+1) = θ_t
ω_(t+1) = ω_t
```

## 5. Governance Equations

The governance update is:

```text
Ψ_(t+1) = GovernanceUpdate(Ψ_t, D_t, Σ_t, B_t)
```

The discrete governance action is chosen by:

```text
a_t = Policy_disc(Ξ_t, ρ_t, Λ_t, N_t, m_t)
```

Reserve evolution is governed by:

```text
ρ_(t+1) = R(ρ_t, Ξ_t, Λ_t, u_t, a_t)
```

Lineage evolution is governed by:

```text
Λ_(t+1) = L(Λ_t, N_t, a_t)
```

## 6. Nervous-System Equations

The nervous-system update is:

```text
Σ_(t+1) = NervousUpdate(Σ_t, D_t, Ψ_t, B_t)
```

The typed afferent field is:

```text
A_t = (A_t^exo, A_t^intero, A_t^mem, A_t^err, A_t^gov)
```

Region-local integration state is:

```text
J_t^(r) = (e_r, i_r, c_r, s_r, φ_r)
```

Region-local gate state is:

```text
K_t^(r) = (d_r, θ_r, γ_r, o_r)
```

Local drive law:

```text
d_r = w_e e_r - w_i i_r + w_c c_r + w_s s_r + b_r(M_t)
```

Commitment law:

```text
o_r(t) = 1[d_r > θ_r] 1[γ_r < γ_max]
```

Routing state is:

```text
P_t = (R_t, L_t, T_t, Y_t)
```

Route utility law:

```text
u_e = α_T T_e + α_Y Y_e - α_L L_e + α_M g_e(M_t)
```

Efferent state is:

```text
E_t = (E_t^act, E_t^auto, F_t)
```

Modulator state is:

```text
M_t = [m_nov, m_thr, m_urg, m_foc, m_exp, m_enc]^T
```

Health state is:

```text
H_t = [h_exc, h_noise, h_flood, h_lat, h_route, h_ground]^T
```

## 7. Blood-System Equations

The blood-system update is:

```text
B_(t+1) = BloodUpdate(B_t, D_t, Ψ_t, Σ_t)
```

The plasma and circulation state is:

```text
Pl_t = (Q_t, F_t, U_t, R_t)
```

The marrow state is:

```text
Ma_t = (Tg_t, Bg_t, Dm_t, Sp_t)
```

The lineage state is:

```text
Li_t = [l_rbc, l_plt, l_neu, l_mono, l_mac, l_lym]^T
```

The demand state is:

```text
De_t = (d_ctx, d_health, d_route, d_urg, d_fail)
```

The stabilization state is:

```text
St_t = (b_t, k_t, p_t, iso_t)
```

The clearance state is:

```text
Cl_t = (w_t, q_t, g_t, m_t^clr)
```

The blood-health state is:

```text
Hb_t = [h_flow, h_sludge, h_clot, h_inf, h_clear, h_auto]^T
```

The typed payload packet is:

```text
π_t^(i) = (k_i, p_i, f_i, u_i, g_i, ttl_i)
```

Packet delivery utility is:

```text
v_i = α_f f_i + α_u u_i + α_r reach_i - α_s stale_i
```

Marrow retargeting law:

```text
Ma_(t+1) = MarrowUpdate(Ma_t, ρ_t, Λ_t, N_t, m_t, Σ_t, Hb_t)
```

Lineage update law:

```text
Li_(t+1) = LineageUpdate(Li_t, Ma_t, De_t, St_t, Cl_t, m_t)
```

## 8. Event And Mode Equations

The event policy is:

```text
e_t = EventPolicy(𝒪_t)
```

The event family is:

```text
𝓔 = 𝓔_gov ∪ 𝓔_sig ∪ 𝓔_sup
```

The mode set is:

```text
𝓜 = { homeostasis, adaptive, inflammatory, pathological, regenerative }
```

## 9. Constraint Equations

The organism must remain inside the viability envelope:

```text
𝒪_t ∈ X_safe
```

Projection consistency is:

```text
Π_consistency(D_t, Ξ_t) := r_t - Π_r(D_t) = 0
```

The plasticity gate is:

```text
PlasticityAllowed_t =
1[m_t ∈ {homeostasis, adaptive}]
1[ρ_t > ρ_min]
1[H_t < H_max]
1[Hb_t < Hb_max]
```

The total organism barrier is:

```text
Φ_org(𝒪_t) = Φ_sub(D_t) + Φ_gov(Ψ_t) + Φ_sig(Σ_t) + Φ_sup(B_t)
```

## 10. Coupled Evolution Equations

The coupled organism law is:

```text
D_(t+1) = SubstrateUpdate(D_t, Ψ_t, Σ_t, B_t)
Ψ_(t+1) = GovernanceUpdate(Ψ_t, D_t, Σ_t, B_t)
Σ_(t+1) = NervousUpdate(Σ_t, D_t, Ψ_t, B_t)
B_(t+1) = BloodUpdate(B_t, D_t, Ψ_t, Σ_t)
e_t     = EventPolicy(𝒪_t)
```

This is the minimal canonical hybrid organism law.

## 11. Objective Equation

The canonical organism objective is:

```text
min E [
  L_task(f_(θ_t)(ι_t), target_t)
  + λ_D Φ_sub(D_t)
  + λ_Ψ Φ_gov(Ψ_t)
  + λ_Σ Φ_sig(Σ_t)
  + λ_B Φ_sup(B_t)
]
```

subject to:

```text
𝒪_t ∈ X_safe
Π_consistency(D_t, Ξ_t) = 0
PlasticityAllowed_t = 1 when θ_t is updated
```

## 12. Timescale Equation

The timescale ordering is:

```text
𝓣 = (τ_alpha, τ_sigma, τ_blood, τ_gov, τ_theta)
```

with:

```text
τ_alpha << τ_sigma << τ_blood << τ_gov << τ_theta
```

## 13. Implementation Reading

For implementation purposes, the equations should be read in this order:

1. load `𝒪_t`
2. compute `c_t`
3. compose `ι_t`
4. run `ForwardStep`
5. project `r_t = Π_r(D_t)`
6. build `Δx_t`, `E_t^act`, `ΔΣ_t`
7. update `Ψ_t`, `Σ_t`, `B_t`
8. evaluate `EventPolicy`
9. evaluate `PlasticityAllowed_t`
10. commit structural updates only if the gate is open

## Final Statement

If a later document needs to quote the mathematics packet in one place, it should quote this file together with:

- `SYMBOLS_AND_NOTATION_GLOSSARY.md`
- `NOTATION_POLICY.md`

That gives one canonical system, one canonical symbol set, and one canonical equation family.
