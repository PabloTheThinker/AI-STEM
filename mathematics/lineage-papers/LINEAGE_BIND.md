# The Bind Is a Process

**Fudoshin Research · Vektra Industries**  
**Status:** First real plant. Stage D on measured service, not drawn exponentials. Not Stage F.  
**Date:** 2026-08-20  
**Implementation:** `reference/lineage_bind_v2.py`  
**Does not change:** Official Specification v2.0.

---

## Abstract

The wait-loop was real as a controller and fake as a plant. `simulate_tandem` drew `Exp(1/τ)`. Apply rewrote `Π` on a dataclass. Nothing retrieved. Nothing was dropped.

This module is the bind table from `LINEAGE_CLOSED_LOOP.md` §5, executed.

```text
shed_load                 →  drop low-priority jobs
cut_bottleneck_latency    →  turn on the retrieval cache
repair_health             →  freeze writes
hold                      →  keep the window
```

Five stages run: retrieval over a corpus, a graph walk, a working-memory ring, a sync hash, a settle/write. A clock measures each service. Lindley advances with that measurement. `τ` is an outcome. `Π` is busy time over the window. `W` is sojourn. Official `Q` is computed from the same window as audit. It does not choose the lever.

The mean SLA is calibrated to this plant (`W_max = 1.35 ×` idle sojourn). The 400 ms number in the tandem papers is for a different body. A setpoint is a hyperparameter.

A live agent does not need this corpus. It needs `--decide`: one JSON window in, including `measured_wait_s`, a bind out.

---

## 1. What "real" means here

Not a live product agent. Not three weeks of logs. Three things that were not true yesterday:

1. **Service is work.** Retrieval scans documents. Pathway walks edges. Those functions run. `time.perf_counter` is the sojourn formula.
2. **Apply changes the next window.** Shed lowers `admit_low`. The same offered stream loses its low-priority jobs. Queueing falls because fewer jobs enter, not because a field named `Π` was decremented.
3. **The window is a slice.** Each tick writes a `TelemetryRecord` the operator card already accepts, plus `measured_wait_s`. `lineage_use_v2.py --batch` and `lineage_loop_v2.py --replay` read it.

The waiting room is still Lindley. That is honest: we do not spend wall-clock sleeping between arrivals. The *services* are not a draw from the traffic equation.

---

## 2. The socket

```bash
python3 mathematics/lineage-papers/reference/lineage_bind_v2.py --decide window.json
```

`window.json` is a telemetry record, or `{M, Pi, taus, u}`, plus `measured_wait_s` when the agent has it. The reply names the lever:

```json
{
  "action": "shed_load",
  "bind": {
    "lever": "drop_low_priority",
    "do": "Drop low-priority retrievals, tool calls, or speculative branches.",
    "admit_low": 0.5
  },
  "scored_q": false
}
```

That is the integration. Wire `measured_wait_s` from the job log. Apply `bind.lever` in the orchestrator. Measure the next window. Official `Q` may be printed. It must not be the setpoint.

---

## 3. What this is not

- Not Stage F. The corpus and graph are synthetic. The arrivals are still Poisson.
- Not Stage G. No external agent has been intervened on.
- Not the official 400 ms SLA transplanted onto a millisecond plant.
- Not a training loss. `Q` stays off the controller.

The miss that remains: a percentile loop. Mean repair still leaves late jobs.

On this plant the bottleneck is a few milliseconds, so official `Q` prints in the tens of thousands (`Q ~ M r²`). That is the law working, and the reason `Q` is the wrong plant. Compare clocks with `q`. Control wait.

Seeded wait-bind (same offer stream, policy changes after each tick):

```text
t      Pi    meas_W    jobs  action       lever
0   0.708  0.0115 s     90  shed_load    drop_low_priority
1   0.596  0.0102 s     75  shed_load    drop_low_priority
2   0.367  0.0096 s     45  shed_load    drop_low_priority
end 0.369  0.0096 s     45  —            admit_low = 0
```

Idle sojourn was `6.3 ms`. The open loop stays over the calibrated wall. The wait-loop drops the low-priority half of the stream. Jobs in the window fall from 90 to 45. Wait falls. `Q` is still huge, and still not why it moved.

---

## 4. Reproduce

```bash
python3 mathematics/lineage-papers/reference/lineage_bind_v2.py
python3 mathematics/lineage-papers/reference/lineage_bind_v2.py --run --ticks 5
python3 mathematics/lineage-papers/reference/lineage_bind_v2.py --compare --ticks 4
python3 mathematics/lineage-papers/reference/lineage_bind_v2.py \
    --decide mathematics/lineage-papers/reference/example_telemetry.json
```

Expect `bind_checks_passed 25`.
