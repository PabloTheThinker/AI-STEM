"""
Discrete-event simulation of the five-stage tandem.

This is the first exogenous check in the program. The simulator knows
nothing about the sojourn formulas: it draws Poisson arrivals and
exponential services and runs the tandem recursion

    D[j][0]  = A[j]
    D[j][l]  = max(D[j][l-1], D[j-1][l]) + S[j][l]

(Lindley 1952; FIFO, infinite buffers). Waits come out of mechanism.
Theory is then compared to mechanism. Agreement is Stage D evidence;
disagreement would have been a recorded miss.

Companion to LINEAGE_TRAFFIC_AND_SIMULATION.md.
Does not change official v2.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import random

try:
    from lineage_core_v2 import WORK_PI
    from lineage_network_v2 import DEFAULT_W_MAX, WORK_TAUS, tandem_sojourn
    from lineage_traffic_v2 import (
        arrival_rate,
        miss_probability,
        traffic_sojourn,
    )
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_core_v2 import WORK_PI
    from lineage_network_v2 import DEFAULT_W_MAX, WORK_TAUS, tandem_sojourn
    from lineage_traffic_v2 import (
        arrival_rate,
        miss_probability,
        traffic_sojourn,
    )


SEED = 20260820
N_JOBS = 80_000
WARMUP = 10_000


def simulate_tandem(
    lam: float,
    taus: list[float] | tuple[float, ...],
    n_jobs: int = N_JOBS,
    warmup: int = WARMUP,
    seed: int = SEED,
) -> dict[str, float]:
    """One seeded run. Returns mean sojourn and the 400 ms miss fraction."""
    if lam <= 0.0 or min(taus) <= 0.0:
        raise ValueError("need λ > 0 and τ > 0")
    rng = random.Random(seed)
    last_dep = [0.0] * len(taus)
    t_arr = 0.0
    total = 0.0
    late = 0
    kept = 0
    for j in range(n_jobs):
        t_arr += rng.expovariate(lam)
        t = t_arr
        for i, tau in enumerate(taus):
            start = t if t > last_dep[i] else last_dep[i]
            t = start + rng.expovariate(1.0 / tau)
            last_dep[i] = t
        if j >= warmup:
            w = t - t_arr
            total += w
            kept += 1
            if w > DEFAULT_W_MAX:
                late += 1
    return {
        "mean_W": total / kept,
        "p_miss": late / kept,
        "jobs": float(kept),
    }


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}
    taus = WORK_TAUS

    # Working point: mechanism vs theory.
    lam = arrival_rate(WORK_PI, taus)
    sim = simulate_tandem(lam, taus)
    theory_W = traffic_sojourn(taus, WORK_PI, 1.0)
    theory_p = miss_probability(taus, WORK_PI, DEFAULT_W_MAX)
    results["mean_matches_traffic_eq"] = abs(sim["mean_W"] - theory_W) / theory_W < 0.03
    results["tail_matches_hypoexp"] = (
        theory_p is not None and abs(sim["p_miss"] - theory_p) < 0.02
    )
    results["allhot_bounds_mechanism"] = sim["mean_W"] < tandem_sojourn(taus, WORK_PI, 1.0)
    results["mechanism_above_raw_service"] = sim["mean_W"] > sum(taus)

    # Light load: theory must track mechanism away from the pinned point too.
    lam_light = arrival_rate(0.20, taus)
    sim_light = simulate_tandem(lam_light, taus, seed=SEED + 1)
    theory_light = traffic_sojourn(taus, 0.20, 1.0)
    results["light_load_matches"] = (
        abs(sim_light["mean_W"] - theory_light) / theory_light < 0.03
    )
    results["load_monotone"] = sim_light["mean_W"] < sim["mean_W"]

    # Determinism: same seed, same numbers.
    a = simulate_tandem(lam, taus, n_jobs=5_000, warmup=1_000, seed=7)
    b = simulate_tandem(lam, taus, n_jobs=5_000, warmup=1_000, seed=7)
    results["seeded_reproducible"] = a == b

    # The old common-Π prediction misses mechanism by ~23%; the traffic
    # equation does not. This is the correction, measured.
    allhot = tandem_sojourn(taus, WORK_PI, 1.0)
    results["allhot_rejected"] = abs(sim["mean_W"] - allhot) / allhot > 0.15
    return results


def render_working_point() -> str:
    lam = arrival_rate(WORK_PI, WORK_TAUS)
    sim = simulate_tandem(lam, WORK_TAUS)
    theory_W = traffic_sojourn(WORK_TAUS, WORK_PI, 1.0)
    theory_p = miss_probability(WORK_TAUS, WORK_PI, DEFAULT_W_MAX)
    allhot = tandem_sojourn(WORK_TAUS, WORK_PI, 1.0)
    lines = [
        "working_point  mechanism vs theory (seeded run)",
        f"jobs_measured      {sim['jobs']:.0f}",
        f"sim_mean_W         {sim['mean_W']:.6f} s",
        f"theory_W_traffic   {theory_W:.6f} s",
        f"theory_W_allhot    {allhot:.6f} s  (rejected by mechanism)",
        f"sim_p_miss_400ms   {sim['p_miss']:.6f}",
        f"theory_p_miss      {theory_p:.6f}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("sim_checks_passed", len(suite))
    print()
    print(render_working_point())
