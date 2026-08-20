# Using the Lineage Equation

**Fudoshin Research · Vektra Industries**  
**Instrument:** `mathematics/lineage-papers/reference/lineage_use_v2.py`  
**Law:** official v2, unchanged  
**Status:** Stage C operator layer. Not Stage F.

This file is how you use the current equation. It does not invent a new one.

## What you get

One telemetry window in. A card out:

| Field | Meaning |
|---|---|
| `Q` | capacity from the law. Dominated by rest. Not a health score. A clock times `q`. |
| `q` | clock-free core `Q/r² ≈ M`. Compare minds across clocks with this. |
| `eps` | load ratio `Π/(M r)`. Flux share of `Q²` is `ε²/(1+ε²)`. |
| `regime` | `rest` / `mixed` / `transport` from `ε` |
| `u` | usable fraction in `[0,1]`. This is the health number. |
| `Q_eff` | `u · Q`. Report this next to `Q`. |
| `zone` | `steady` / `guarded` / `repair` / `critical` from `u` |
| `bottleneck` | slowest latency and its Hz |
| `hint` / `action` | feasible one-tick move |
| `rest_share` | fraction of `Q²` from scaled mass |
| `transport_share` | fraction of `Q²` from scaled flux |
| `weight_table` | `official` (default), `equal`, or `promotion` |

Do not put `Q` on a dashboard without `u` and `weight_table`.

## Run it

```bash
python3 mathematics/lineage-papers/reference/lineage_use_v2.py --example
python3 mathematics/lineage-papers/reference/lineage_use_v2.py mathematics/lineage-papers/reference/example_telemetry.json
python3 mathematics/lineage-papers/reference/lineage_use_v2.py mathematics/lineage-papers/reference/minimal_telemetry.json --json
python3 mathematics/lineage-papers/reference/lineage_use_v2.py --compare \
    mathematics/lineage-papers/reference/example_telemetry.json \
    mathematics/lineage-papers/reference/minimal_telemetry.json
python3 mathematics/lineage-papers/reference/lineage_use_v2.py \
    mathematics/lineage-papers/reference/example_telemetry.json --cut-ms 20
python3 mathematics/lineage-papers/reference/lineage_use_v2.py --self-test
```

`--cut-ms` does not change the log. It answers: if the slowest pipe were that many milliseconds faster, what happens to `Q` and `Q_eff`.

`--batch windows.jsonl` writes one JSON card per line. Bad lines become `{"line": N, "error": "..."}`.

## Smallest window that still computes

`minimal_telemetry.json`:

```json
{
  "memory_entries": 120,
  "graph_nodes": 40,
  "graph_edges": 70,
  "permanence_integrity": 0.82,
  "retrieval_attempts": 20,
  "retrieval_hits": 14,
  "tau_retrieval_s": 0.12
}
```

Missing optional fields are declared on the card. Extra log fields are ignored.

## Why additive `Q_eff` is not the instrument

v2 once wrote `Q_eff = Q − λH − λE − λD`. On a 120 ms bottleneck, `Q ≈ 50` and the penalties are `≈ 0.6`. Subtracting them leaves `Q` almost unchanged. That is a units error.

Operational form, now in the official spec §4.4.1:

```text
u      = clip(1 − 0.25 H − 0.25 Ê − 0.25 D)
Q_eff  = u · Q
```

`LineageEquationV2.usable_capacity(...)` is that form. `effective_capacity(...)` remains the historical additive writing.

## What this does not claim

- The official weights are not claimed true for every machine.
- A green `zone` is not a live prediction. Stage F still needs an exogenous target.
- `--cut-ms` is a first-order preview, not a causal experiment.
