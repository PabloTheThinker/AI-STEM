# The Lineage Equation  
## Official Specification v2.0  
### A Nondimensional Capacity Invariant for Cognitive Agent Architectures

**Status:** Canonical (supersedes draft paper `lineage-equation-paper.md` for formal claims)  
**Version:** 2.0.0  
**Date:** 2026-07-15  
**Division:** Fudoshin Research — Vektra Industries  
**Implementation:** `mathematics/lineage-papers/reference/lineage_capacity_v2.py`

---

## Abstract

We specify the **Lineage Equation**: a computable, differentiable capacity invariant for autonomous cognitive agents. The official form is the **nondimensional Minkowski-style identity**

\[
\mathcal{Q}^{2}=\tilde{\Pi}^{2}+\tilde{\mathcal{M}}^{2},
\qquad
\tilde{\mathcal{M}}=\mathcal{M}\!\left(\frac{\nu^{\ast}}{\nu_{0}}\right)^{2},
\qquad
\tilde{\Pi}=\Pi\!\left(\frac{\nu^{\ast}}{\nu_{0}}\right),
\]

where \(\mathcal{M}\) is cognitive mass (structural inertia), \(\Pi\) is cognitive momentum (directed information flux), \(\nu^{\ast}\) is the bottleneck propagation rate, and \(\nu_{0}\) is a fixed reference rate. With capacity unit \(\kappa\ge 0\),

\[
\mathcal{Q}_{\kappa}=\kappa\,\mathcal{Q}.
\]

This document states axioms, definitions, identified weight defaults, exact gradients, a free-energy style conservation budget, Laplacian/Lyapunov coherence energy, a second-order coupling extension, a validation suite, and a falsifiability protocol. The algebraic template is the relativistic energy–momentum relation; the dynamical justification for coherence penalties is the graph-Laplacian quadratic form used as a Lyapunov energy. No claim is made that agents obey special-relativistic physics—only that the same algebraic skeleton yields a useful, homogeneous capacity invariant under explicit scaling assumptions.

---

## 1. Scope and non-claims

### 1.1 What this specification claims

1. **Algebraic well-formedness.** Under the stated domain restrictions, \(\mathcal{Q}\) is finite, nonnegative, and \(C^{\infty}\) on the open set \(\mathcal{Q}>0\).
2. **Rest reduction.** If \(\Pi=0\), then \(\mathcal{Q}_{\kappa}=\kappa\,|\mathcal{M}|\,(\nu^{\ast}/\nu_{0})^{2}\).
3. **Exact gradients.** Partial derivatives of \(\mathcal{Q}_{\kappa}\) with respect to \((\mathcal{M},\Pi,\nu^{\ast})\) admit closed form (Theorem 3).
4. **Coherence energy.** For a symmetric nonnegative weight matrix, \(E_{\mathrm{coh}}(z)=z^{\mathsf T}Lz\ge 0\) with \(L=D-W\) (Laplacian PSD property).
5. **Operational measurability.** Every symbol maps to a pure-Python reference routine without external numeric libraries.

### 1.2 What this specification does **not** claim

- Lorentz invariance of agent state spaces.
- That equal \(\alpha,\beta\) weights are unique or optimal for all architectures.
- That synthetic bootstrap training of any neural sidecar is a substitute for longitudinal live data.
- Cross-architecture universal constants without re-identification of \((\alpha,\beta,\nu_{0},\kappa)\).

Draft v1 (`lineage-equation-paper.md`) remains historical narrative and empirical log. **Normative math lives here.**

---

## 2. Mathematical preliminaries

### 2.1 Energy–momentum relation (algebraic template)

In special relativity, total energy \(E\), rest mass \(m\), and momentum magnitude \(p\) satisfy

\[
E^{2}=(pc)^{2}+(mc^{2})^{2}.
\]

Primary sources: Einstein (1905); standard textbook form of the energy–momentum relation (see `mathematics/canon/SOURCES.md` §§18–19). We use this **only** as a homogeneous quadratic composition of a “rest” term and a “transport” term.

### 2.2 Graph Laplacian quadratic form

For an undirected weighted graph with symmetric \(W\ge 0\) and degree matrix \(D\), the Laplacian \(L=D-W\) is symmetric positive semidefinite and

\[
z^{\mathsf T}Lz=\sum_{(i,j)\in E}w_{ij}(z_i-z_j)^{2}.
\]

This is the standard spectral-graph energy (Spielman, Spectral Graph Theory; Barabási, Network Science). We adopt \(E_{\mathrm{coh}}(z)=z^{\mathsf T}Lz\) as **coherence energy** of a cognitive-web state \(z\).

### 2.3 Lyapunov energy

A continuously differentiable \(V\) with \(V(x)\ge 0\), \(V(0)=0\), and \(\dot V\le 0\) along closed-loop trajectories certifies stability (Lyapunov). MIT Underactuated Robotics Lyapunov notes and MIT 6.243J materials formalize the technique we invoke when treating \(E_{\mathrm{coh}}\) and capacity losses as decreasing energies under healing policies.

### 2.4 Free-energy / uncertainty budget

Friston’s free-energy principle frames adaptive systems as regulating an upper bound on surprise (information-theoretic free energy). We do **not** re-derive FEP; we adopt the operational budget

\[
\mathcal{Q}_{\mathrm{eff}}=\mathcal{Q}-\lambda_H H(\mu)-\lambda_E E_{\mathrm{graph}}-\lambda_D D_{\mathrm{drift}},
\]

i.e. uncertainty, graph fracture, and identity drift consume usable capacity (Landauer’s principle motivates irreversible cost of information change; Friston 2010 motivates the uncertainty term).

### 2.5 Convex quadratic structure

Boyd & Vandenberghe (Convex Optimization) supply the ambient setting: quadratic forms \(x^{\mathsf T}Mx\) with \(M\succeq 0\), simplex constraints on weights, and gradient methods on smooth objectives.

---

## 3. Axioms

Let an agent at time \(t\) expose measurable structural densities \(C_i(t)\in[0,1]\) and flux scores \(F_k(t)\in[0,1]\), and positive path latencies \(\tau_\ell(t)>0\).

**A1 (Structural mass).** Cognitive mass is a convex combination

\[
\mathcal{M}=\sum_{i\in\mathcal{I}}\alpha_i C_i,\qquad
\alpha_i\ge 0,\ \sum_i\alpha_i=1.
\]

**A2 (Directed momentum).** Cognitive momentum is a convex combination

\[
\Pi=\sum_{k\in\mathcal{K}}\beta_k F_k,\qquad
\beta_k\ge 0,\ \sum_k\beta_k=1.
\]

**A3 (Bottleneck propagation).** There exists a positive bottleneck latency

\[
\tau^{\ast}=\max_{\ell}\tau_\ell,\qquad
\nu^{\ast}=\frac{1}{\tau^{\ast}}\ \ (\mathrm{Hz}).
\]

Optional channel ceiling: \(\nu^{\ast}\leftarrow\min(\nu^{\ast},C_{\mathrm{channel}})\).

**A4 (Homogeneous capacity).** Capacity is nonnegative, zero only when \(\mathcal{M}=\Pi=0\), strictly increasing in \(|\mathcal{M}|\) and \(|\Pi|\) when \(\nu^{\ast},\nu_{0},\kappa\) are fixed and positive, and reduces to a pure rest term when \(\Pi=0\).

**A5 (Quadratic composition).** Capacity is the Euclidean norm of the scaled pair \((\tilde{\Pi},\tilde{\mathcal{M}})\) defined in §4 (Minkowski-style, (+,+) signature on the capacity plane—not spacetime).

**Proposition 1 (Existence).** Axioms A1–A5 admit the unique capacity form of Definition 1 up to the global unit \(\kappa\) and reference rate \(\nu_{0}\).

*Sketch.* A4+A5 force \(\mathcal{Q}=\sqrt{\tilde{\Pi}^{2}+\tilde{\mathcal{M}}^{2}}\). Homogeneity of degree 1 in the scaled coordinates plus rest reduction force \(\tilde{\mathcal{M}}\propto\mathcal{M}r^{2}\) and \(\tilde{\Pi}\propto\Pi r\) with the same \(r=\nu^{\ast}/\nu_{0}\). □

---

## 4. Official definitions

### 4.1 Index sets (canonical)

| Symbol | Meaning | Canonical components |
|--------|---------|----------------------|
| \(C_i\) | Mass densities | \(C_{\mathrm{id}}, C_{\mathrm{mem}}, C_{\mathrm{graph}}, C_{\mathrm{perm}}\) |
| \(F_k\) | Momentum fluxes | \(F_{\mathrm{wm}}, F_{\mathrm{ret}}, F_{\mathrm{path}}, F_{\mathrm{ctrl}}, F_{\mathrm{merge}}\) |
| \(\tau_\ell\) | Latencies (s) | retrieval, pathway, working-memory, sync, settling |

Component semantics (operational):

- \(C_{\mathrm{id}}\): identity stability / hash-continuity of self-model  
- \(C_{\mathrm{mem}}\): memory density and index coverage  
- \(C_{\mathrm{graph}}\): mesh connectivity / myelination of the cognitive web  
- \(C_{\mathrm{perm}}\): durable persistence / checkpoint health  
- \(F_{\mathrm{wm}}\): working-memory throughput  
- \(F_{\mathrm{ret}}\): retrieval hit rate / quality  
- \(F_{\mathrm{path}}\): pathway firing activity  
- \(F_{\mathrm{ctrl}}\): control / executive flux  
- \(F_{\mathrm{merge}}\): integrate / write-back flux  

### 4.2 Definition 1 (Lineage Equation, official)

Fix \(\nu_{0}>0\) and \(\kappa\ge 0\). Set \(r=\nu^{\ast}/\nu_{0}\). Then

\begin{align}
\tilde{\mathcal{M}}&=\mathcal{M}\,r^{2},\\
\tilde{\Pi}&=\Pi\,r,\\
\mathcal{Q}&=\sqrt{\tilde{\Pi}^{2}+\tilde{\mathcal{M}}^{2}},\\
\mathcal{Q}_{\kappa}&=\kappa\,\mathcal{Q}.
\end{align}

**Rest energy**

\[
\mathcal{E}_{0}=\kappa\,|\mathcal{M}|\,r^{2}.
\]

**Transport term** \(\kappa|\tilde{\Pi}|\); **rest term** \(\kappa|\tilde{\mathcal{M}}|\).

### 4.3 Relation to draft v1

Draft v1 wrote \(\mathcal{Q}^{2}=(\nu^{\ast}\Pi)^{2}+(\mathcal{M}(\nu^{\ast})^{2})^{2}\) with \(\nu^{\ast}=1000/\max\tau_{\mathrm{ms}}\).  

Under \(\nu_{0}=1\,\mathrm{Hz}\), \(\kappa=1\), and \(\tau\) expressed in seconds so that \(\nu^{\ast}=1/\tau^{\ast}_{\mathrm{s}}=1000/\tau^{\ast}_{\mathrm{ms}}\), **the numerical value of \(\mathcal{Q}\) is identical** to v1. v2 makes the scaling **explicit** (homogeneous, unit-aware) and prefers SI seconds.

### 4.4 Official weight defaults (identified)

Equal weights remain a **null model**. The **official operational defaults** for the reference architecture are the identified simplex (parameter-ID bootstrap, \(R^{2}\approx 0.94\) on synthetic+trajectory fits; re-fit required per architecture class):

\[
\begin{aligned}
\alpha^{\star}&=(0.28,\ 0.30,\ 0.22,\ 0.20)
&&\text{for }(C_{\mathrm{id}},C_{\mathrm{mem}},C_{\mathrm{graph}},C_{\mathrm{perm}}),\\
\beta^{\star}&=(0.22,\ 0.25,\ 0.20,\ 0.18,\ 0.15)
&&\text{for }(F_{\mathrm{wm}},F_{\mathrm{ret}},F_{\mathrm{path}},F_{\mathrm{ctrl}},F_{\mathrm{merge}}).
\end{aligned}
\]

**Requirement:** any published capacity number must declare whether it used \(\alpha^{\star},\beta^{\star}\) or equal weights.

### 4.5 Propagation bound derivation (three equivalent views)

Let \(\tau^{\ast}=\max_\ell\tau_\ell\) in seconds.

1. **Unit conversion / reciprocal latency.** \(\nu^{\ast}=1/\tau^{\ast}\).  
2. **Single-server queue.** For a saturated node with service time \(\tau^{\ast}\), mean throughput upper-bounds by \(1/\tau^{\ast}\).  
3. **Channel-rate normalization.** If a measured Shannon-style capacity \(C_{\mathrm{channel}}\) (messages/s) is available, \(\nu^{\ast}_{\mathrm{eff}}=\min(1/\tau^{\ast},C_{\mathrm{channel}})\).

The constant “1000” in v1 is **not fundamental**—it is ms→s conversion.

---

## 5. Theorems

### Theorem 1 (Rest-state reduction)

If \(\Pi=0\) and \(\kappa,\nu_{0},\nu^{\ast}\) are finite with \(\nu_{0}>0\), then \(\mathcal{Q}_{\kappa}=\mathcal{E}_{0}=\kappa\,|\mathcal{M}|\,(\nu^{\ast}/\nu_{0})^{2}\).

*Proof.* Immediate from Definition 1. □

### Theorem 2 (Monotonicity)

Fix \(\nu^{\ast},\nu_{0},\kappa>0\). Then \(\mathcal{Q}_{\kappa}\) is nondecreasing in \(\mathcal{M}\) for \(\mathcal{M}\ge 0\) and nondecreasing in \(\Pi\) for \(\Pi\ge 0\).

*Proof.* \(\partial\mathcal{Q}/\partial\mathcal{M}=(\mathcal{M} r^{4})/\mathcal{Q}\ge 0\) when \(\mathcal{M}\ge 0\), \(\mathcal{Q}>0\); similarly \(\partial\mathcal{Q}/\partial\Pi=(\Pi r^{2})/\mathcal{Q}\ge 0\). □

### Theorem 3 (Capacity gradients)

Let \(r=\nu^{\ast}/\nu_{0}\) and \(\mathcal{Q}_{\kappa}=\kappa\sqrt{(\Pi r)^{2}+(\mathcal{M} r^{2})^{2}}>0\). Then

\begin{align}
\frac{\partial\mathcal{Q}_{\kappa}}{\partial\mathcal{M}}
&=\kappa\frac{\mathcal{M}\,r^{4}}{\mathcal{Q}},\\[4pt]
\frac{\partial\mathcal{Q}_{\kappa}}{\partial\Pi}
&=\kappa\frac{\Pi\,r^{2}}{\mathcal{Q}},\\[4pt]
\frac{\partial\mathcal{Q}_{\kappa}}{\partial\nu^{\ast}}
&=\kappa\frac{\Pi^{2} r/\nu_{0}+2\mathcal{M}^{2} r^{3}/\nu_{0}}{\mathcal{Q}},
\end{align}

where \(\mathcal{Q}=\mathcal{Q}_{\kappa}/\kappa\).

*Proof.* Implicit differentiation of \(\mathcal{Q}^{2}=\Pi^{2}r^{2}+\mathcal{M}^{2}r^{4}\). □

### Theorem 4 (Laplacian PSD / coherence)

For symmetric \(W\) with nonnegative off-diagonals and zero diagonal, \(L=D-W\succeq 0\) and \(E_{\mathrm{coh}}(z)=z^{\mathsf T}Lz\ge 0\). Moreover \(L\mathbf{1}=0\).

*Proof.* Standard spectral graph theory (quadratic form identity). □

### Theorem 5 (Effective capacity floor)

If \(\lambda_H,\lambda_E,\lambda_D\ge 0\) and penalty terms are nonnegative, then \(\mathcal{Q}_{\mathrm{eff}}^{\downarrow}=\max(0,\mathcal{Q}-\lambda_H H-\lambda_E E_{\mathrm{graph}}-\lambda_D D_{\mathrm{drift}})\) is a well-defined usable budget.

---

## 6. Second-order coupling (official extension)

Linear mass/momentum ignore synergistic interactions. Official **Coupled Lineage Equation**:

\begin{align}
\mathcal{M}_{\mathrm{c}}&=\mathcal{M}+\sum_{i<j}\gamma_{ij}C_i C_j,\\
\Pi_{\mathrm{c}}&=\Pi+\sum_{k<\ell}\delta_{k\ell}F_k F_\ell,\\
\mathcal{Q}_{\mathrm{c}}&=\kappa\sqrt{(\Pi_{\mathrm{c}} r)^{2}+(\mathcal{M}_{\mathrm{c}} r^{2})^{2}}.
\end{align}

Default nonnegative \(\gamma,\delta\) (reference implementation) guarantee \(\mathcal{Q}_{\mathrm{c}}\ge\mathcal{Q}\) on the unit hypercube. Coefficients are **hyperparameters** subject to identification; they are not universal constants.

Canonical mass interactions: identity×permanence, memory×graph, identity×graph, memory×permanence, identity×memory, graph×permanence.  
Canonical momentum interactions: wm×retrieval, path×control, retrieval×merge, wm×control.

---

## 7. Optimization and prescribed actions

Priority of improvement action \(a\) targeting component \(x_a\):

\[
\mathrm{priority}(a)=\left|\frac{\partial\mathcal{Q}_{\kappa}}{\partial x_a}\right|\cdot\mathrm{gap}(x_a),
\]

with \(\mathrm{gap}(x)=\max(0,x^{\star}-x)\) relative to a design target. Stall rule: if \(\Delta\mathcal{Q}<\varepsilon\) for \(N\) consecutive ticks, switch to the second-ranked gradient direction.

Plasticity remains gated (conjunctive):

\[
\mathbf{1}[m\in\{\mathrm{homeostasis},\mathrm{adaptive}\}]
\cdot\mathbf{1}[\rho>\rho_{\min}]
\cdot\mathbf{1}[H_{\mathrm{neural}}<H_{\max}]
\cdot\mathbf{1}[H_{\mathrm{blood}}<H_{\max}].
\]

Timescale ordering (canonical):

\[
\tau_{\alpha}\ll\tau_{\sigma}\ll\tau_{\mathrm{blood}}\ll\tau_{\mathrm{gov}}\ll\tau_{\theta}
\]

with reference values \(30\,\mathrm{ms}\ll 500\,\mathrm{ms}\ll 5\,\mathrm{s}\ll 30\,\mathrm{s}\ll 12\,\mathrm{h}\).

---

## 8. Validation suite (normative)

The reference module `lineage_capacity_v2.py` implements and must pass:

| ID | Check |
|----|--------|
| V1 | Rest-state reduction \(\Pi=0\Rightarrow\mathcal{Q}=\mathcal{E}_0\) |
| V2 | \(\alpha,\beta\) are simplices |
| V3 | \(\mathcal{M},\Pi,\mathcal{Q}\ge 0\) on the unit hypercube |
| V4 | \(\nu^{\ast}\) finite and positive for \(\tau>0\) |
| V5 | Laplacian row-sum zero + symmetry |
| V6 | Coherence energy PSD (\(E_{\mathrm{coh}}\ge 0\)) |
| V7 | Timescale ordering |
| V8 | Plasticity gate conjunctive |
| V9 | Organism barrier additivity |
| V10 | Analytical \(\partial\mathcal{Q}/\partial\mathcal{M}\) matches finite differences |
| V11 | Numerical compatibility with v1 under SI conversion |
| V12 | Coupled capacity \(\ge\) linear capacity for default \(\gamma,\delta\ge 0\) |

Run:

```bash
python3 mathematics/lineage-papers/reference/lineage_capacity_v2.py
```

---

## 9. Falsifiability protocol

A deployment **falsifies** the operational theory (not the algebra) if any of the following hold under agreed instrumentation:

1. **Gradient non-predictivity.** Actions ranked by Theorem 3 gradients do not improve measured \(\mathcal{Q}\) more than random actions of equal cost over \(N\ge 30\) ticks (\(p>0.05\), pre-registered test).  
2. **Weight instability.** Re-identified \((\alpha,\beta)\) on held-out weeks leave the 95% bootstrap intervals of \(\alpha^{\star},\beta^{\star}\) with total-variation distance \(>0.25\) without architectural change.  
3. **Propagation non-bottleneck.** End-to-end throughput remains \(>2\times\nu^{\ast}\) while all component latencies stay at the measured \(\tau^{\ast}\) (instrumentation contradiction).  
4. **Coherence mismatch.** Reducing \(E_{\mathrm{coh}}\) by mesh repair does not reduce task error rates or effective capacity penalties on fracture-sensitive workloads.

Algebraic identities (Theorems 1–4) are not empirical claims; they are checked by the validation suite.

---

## 10. Measurement recipe (architecture-agnostic)

1. Map agent telemetry → \((C_i),(F_k),(\tau_\ell)\) with documented sensors.  
2. Choose weight mode: `identified` or `equal`; record choice.  
3. Choose \(\nu_{0}\) (default \(1\,\mathrm{Hz}\)) and \(\kappa\) (default \(1\)).  
4. Compute \(\mathcal{M},\Pi,\nu^{\ast},\mathcal{Q}_{\kappa}\) via reference code.  
5. Log gradients and top-3 actions.  
6. Optionally compute \(E_{\mathrm{coh}}\) on the live mesh Laplacian.  
7. Publish series with schema version `lineage-eq/2.0`.

---

## 11. Neural sidecars (informative, non-normative)

`CognitiveNet` / `CoupledCognitiveNet` may approximate \(\mathcal{Q}\) and action ranks. Normative optimization uses Theorem 3. Neural agreement rate is a **diagnostic**, not a correctness criterion. Training on synthetic trajectories is bootstrap only; production claims require live trajectories.

---

## 12. Versioning

| Version | Change |
|---------|--------|
| 1.x | Draft paper; equal weights default; \(\nu^{\ast}=1000/\tau_{\mathrm{ms}}\) |
| **2.0** | **Official nondimensional form; SI \(\nu^{\ast}\); identified \(\alpha^{\star},\beta^{\star}\); Laplacian/Lyapunov/FEP budget formalized; pure reference module; falsifiability protocol** |

---

## 13. Notation summary

| Symbol | Name | Definition |
|--------|------|------------|
| \(\mathcal{M}\) | Cognitive mass | \(\sum\alpha_i C_i\) |
| \(\Pi\) | Cognitive momentum | \(\sum\beta_k F_k\) |
| \(\nu^{\ast}\) | Propagation bound | \(1/\max\tau_\ell\) (Hz) |
| \(\nu_{0}\) | Reference rate | default \(1\,\mathrm{Hz}\) |
| \(r\) | Rate ratio | \(\nu^{\ast}/\nu_{0}\) |
| \(\tilde{\mathcal{M}}\) | Scaled mass | \(\mathcal{M} r^{2}\) |
| \(\tilde{\Pi}\) | Scaled momentum | \(\Pi r\) |
| \(\mathcal{Q}\) | Nondim. capacity | \(\sqrt{\tilde{\Pi}^{2}+\tilde{\mathcal{M}}^{2}}\) |
| \(\kappa\) | Capacity unit | \(\mathcal{Q}_{\kappa}=\kappa\mathcal{Q}\) |
| \(\mathcal{E}_{0}\) | Rest energy | \(\kappa|\mathcal{M}|r^{2}\) |
| \(L\) | Graph Laplacian | \(D-W\) |
| \(E_{\mathrm{coh}}\) | Coherence energy | \(z^{\mathsf T}Lz\) |
| \(\mathcal{Q}_{\mathrm{eff}}\) | Effective capacity | budget after losses |

---

## 14. References (selected; full packet in SOURCES.md)

1. Einstein, A. (1905). *Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?* Annalen der Physik.  
2. Energy–momentum relation (standard form); MIT 8.033 lecture notes.  
3. Spielman, D. *Spectral Graph Theory* (Yale).  
4. Barabási, A.-L. *Network Science*.  
5. Boyd, S. & Vandenberghe, L. *Convex Optimization*.  
6. MIT Underactuated Robotics — Lyapunov analysis.  
7. MIT OCW 6.243J — Dynamics of Nonlinear Systems (Lyapunov).  
8. Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*.  
9. Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.*  
10. Shannon, C. (1948). A mathematical theory of communication.  
11. Draft v1: `lineage-equation-paper.md` (historical).  
12. Research roadmap: `LINEAGE_EQUATION_AND_COGNITIVENET_RESEARCH_ROADMAP.md`.

---

## 15. Reference implementation map

| Artifact | Path |
|----------|------|
| Official spec (this document) | `mathematics/lineage-papers/LINEAGE_EQUATION_V2_OFFICIAL.md` |
| Pure Python reference | `mathematics/lineage-papers/reference/lineage_capacity_v2.py` |
| Validation entrypoint | `python3 …/lineage_capacity_v2.py` |
| Engine implementation (product) | external `lineage-engine` (`capacity.py`, `coupling.py`) — should converge to v2 defaults |
| Draft narrative paper | `lineage-equation-paper.md` |

---

## 16. Change control

Material changes to Definition 1, Theorems 1–5, or official \((\alpha^{\star},\beta^{\star})\) require:

1. Bump of `2.x` minor or major version in this file.  
2. Updated validation suite.  
3. Note in the research roadmap.  
4. Explicit migration note for telemetry schema `lineage-eq/*`.

---

*Fudoshin Research — Vektra Industries · Lineage Equation Official Specification v2.0*  
*Correspondence: research@vektraindustries.com / Pablo Navarro*
