# The Lineage Equation, broken down like `1 + 1 = 2`

**Fudoshin Research · Vektra Industries**  
**Equation:** official v2  
**Numbers:** the loaded-but-coherent worked example  
**Printer:** `mathematics/lineage-papers/reference/lineage_breakdown_v2.py`

School arithmetic does not start with “addition is a deep idea.” It writes

```text
1 + 1 = 2
```

and asks three questions: what is each mark, what does the operation do, what is the result. This file does that to the current law. No new equation. No Peano. The official identity only.

---

## 0. The whole equation

```text
Q²  =  Π̃²  +  M̃²
```

with

```text
Π̃  =  Π  ·  r
M̃  =  M  ·  r²
r   =  ν* / ν₀
```

and, if you want a unit on the answer,

```text
Q_κ  =  κ · Q
```

In the example we set `ν₀ = 1` and `κ = 1`, so `r = ν*` and `Q_κ = Q`.

**English:** capacity is the hypotenuse of a right triangle whose legs are scaled flux and scaled structure.

That is the same shape as

```text
c²  =  a²  +  b²
```

`Π̃` is one leg. `M̃` is the other. `Q` is the hypotenuse.

---

## 1. Each mark, one line

| Mark | Name | In this example | What it is |
|---|---|---|---|
| `C_id` | identity density | 0.865 | how stable the self-model is, in `[0,1]` |
| `C_mem` | memory density | 0.4275 | how packed and indexed memory is |
| `C_graph` | graph density | 0.845 | how connected the mesh is |
| `C_perm` | permanence density | 0.820 | how healthy checkpoints are |
| `α` | mass weights | `(0.28, 0.30, 0.22, 0.20)` | how much each `C` counts. They add to `1` |
| `M` | cognitive mass | 0.72035 | the weighted pile of structure |
| `F_wm` … `F_merge` | flux scores | see §3 | how hard each pipe is running, in `[0,1]` |
| `β` | momentum weights | `(0.22, 0.25, 0.20, 0.18, 0.15)` | how much each `F` counts. They add to `1` |
| `Π` | cognitive momentum | 0.46811 | the weighted pile of flux |
| `τ_ℓ` | latencies | 0.120, 0.040, 0.030, 0.020, 0.015 s | how long each step takes |
| `ν*` | propagation bound | 8.333… Hz | `1` over the slowest step |
| `ν₀` | reference rate | 1 Hz | a yardstick, so `r` has no unit |
| `r` | rate ratio | 8.333… | `ν* / ν₀` |
| `Π̃` | scaled flux | 3.901 | flux after the rate is applied once |
| `M̃` | scaled mass | 50.024 | mass after the rate is applied twice |
| `Q` | capacity | 50.176 | the hypotenuse |

If a mark is not in this table, it is not in the current equation.

---

## 2. Build `M` — this is `1 + 1 = 2` for structure

Mass is ordinary weighted addition.

```text
M  =  α_id C_id  +  α_mem C_mem  +  α_graph C_graph  +  α_perm C_perm
```

Plug in official weights and the example densities:

```text
M  =  0.28·0.865  +  0.30·0.4275  +  0.22·0.845  +  0.20·0.820
   =  0.24220     +  0.12825      +  0.18590     +  0.16400
   =  0.72035
```

Four multiplies, then add. Same operations as

```text
2·3 + 4·5
```

The only rule that is not grade-school is: the `α` add to `1`, and each `C` lives in `[0,1]`, so `M` also lives in `[0,1]`.

---

## 3. Build `Π` — the same addition, for flux

```text
Π  =  β_wm F_wm  +  β_ret F_ret  +  β_path F_path  +  β_ctrl F_ctrl  +  β_merge F_merge
```

```text
F_wm    = 0.428571
F_ret   = 0.708000
F_path  = 0.384615
F_ctrl  = 0.285714
F_merge = 0.456471
```

```text
Π  =  0.22·0.428571  +  0.25·0.708000  +  0.20·0.384615
   +  0.18·0.285714  +  0.15·0.456471
   =  0.094286       +  0.177000       +  0.076923
   +  0.051429       +  0.068471
   =  0.46811
```

Again: multiply, then add. `Π ∈ [0,1]`.

---

## 4. Build `ν*` — one divide, after a max

Five waits, in seconds:

```text
τ_retrieval = 0.120
τ_pathway   = 0.040
τ_wm        = 0.030
τ_sync      = 0.020
τ_settling  = 0.015
```

The slowest step wins:

```text
τ*  =  max(0.120, 0.040, 0.030, 0.020, 0.015)  =  0.120
ν*  =  1 / τ*  =  1 / 0.120  =  8.333… Hz
```

That is “how many full updates per second the slowest pipe allows.”  
`1000` in the old v1 form was only milliseconds-to-seconds. It is not a magic constant.

Yardstick:

```text
ν₀  =  1 Hz
r   =  ν* / ν₀  =  8.333… / 1  =  8.333…
```

---

## 5. Scale the two piles — multiply

Flux feels the rate **once**:

```text
Π̃  =  Π · r  =  0.46811 · 8.333…  =  3.90090
```

Mass feels the rate **twice**:

```text
M̃  =  M · r²  =  0.72035 · (8.333…)²
               =  0.72035 · 69.444…
               =  50.02431
```

Why twice? Because the official rest term is `M (ν*)²`, the same way rest energy is `m c²`. After you divide by the yardstick `ν₀`, that is `M r²`.

This is the only non-grade-school choice in the equation: mass is scaled by `r²`, flux by `r`. Everything after this is `a² + b²`.

---

## 6. Square — same as the `²` in `c² = a² + b²`

```text
Π̃²  =  (3.90090)²  =  15.217
M̃²  =  (50.02431)² =  2502.431
```

Squaring does three things, all ordinary:

1. Sign disappears. Capacity is not negative.
2. The larger leg dominates. `50²` dwarfs `3.9²`.
3. The two legs become **the same kind of thing** (squared scaled scores) so they may be added.

---

## 7. Add — this is the `+` in `1 + 1 = 2`

```text
Π̃² + M̃²  =  15.217 + 2502.431  =  2517.648
```

You are not adding mass to flux. You already scaled them. You are adding two squared legs of one triangle.

---

## 8. Square root — undo the `²` on `Q`

```text
Q  =  √(Π̃² + M̃²)  =  √2517.648  =  50.176
```

Check against the triangle:

```text
Q²  =?  Π̃² + M̃²
50.176²  =  2517.65
15.217 + 2502.431  =  2517.65
```

That is the whole law.

---

## 9. The same arithmetic as v1

Old writing:

```text
Q²  =  (ν* · Π)²  +  (M · (ν*)²)²
```

With `ν₀ = 1`, `ν* = r`, this is identical:

```text
ν* · Π      =  8.333… · 0.46811  =  3.90090  =  Π̃
M · (ν*)²   =  0.72035 · 69.444  =  50.02431 =  M̃
```

v2 did not change the number. It named the two legs.

---

## 10. Two special cases, still the same equation

**No flux** (`Π = 0`):

```text
Q  =  |M̃|  =  |M| r²  =  0.72035 · 69.444  =  50.024
```

That is `E₀` in the papers. In the example, live `Q = 50.176` is almost this. Flux added `0.152`.

**No mass** (`M = 0`):

```text
Q  =  |Π̃|  =  |Π| r
```

A system with no structure and only flux has capacity equal to scaled flux. The official example is the other extreme.

---

## 11. What you may add after `Q` (not inside it)

The current equation **stops at `Q`**. These are extra, and they must be named:

```text
u      =  clip(1 − 0.25 H − 0.25 Ê − 0.25 D)
Q_eff  =  u · Q
```

In the example, `u = 0.840`, so `Q_eff = 42.134`. That is a **budget**, not a change to `Q² = Π̃² + M̃²`.

---

## 12. One-line worksheet

```text
C  = (0.865, 0.4275, 0.845, 0.820)
α  = (0.28,  0.30,   0.22,  0.20)
M  = 0.28·0.865 + 0.30·0.4275 + 0.22·0.845 + 0.20·0.820  = 0.72035

F  = (0.428571, 0.708, 0.384615, 0.285714, 0.456471)
β  = (0.22, 0.25, 0.20, 0.18, 0.15)
Π  = 0.22·0.428571 + 0.25·0.708 + 0.20·0.384615
   + 0.18·0.285714 + 0.15·0.456471                        = 0.46811

τ* = 0.120 s
ν* = 1/0.120 = 8.333 Hz
r  = 8.333

Π̃ = 0.46811 · 8.333 = 3.901
M̃ = 0.72035 · 69.444 = 50.024

Q² = 3.901² + 50.024² = 15.22 + 2502.43 = 2517.65
Q  = √2517.65 = 50.176
```

Print the same steps:

```bash
python3 mathematics/lineage-papers/reference/lineage_breakdown_v2.py
```

---

## 13. What this is not

- It is not a new law.
- It is not Peano arithmetic. `1+1=2` is the **method** (name each mark, do the operations, check the result), not a new foundation.
- It does not say the weights are true for every machine. It says: **given these weights and these scores, this is the arithmetic.**
