"""
Bind the wait-loop to a real five-stage agent.

Stages do work. Service times are measured with a clock, not drawn
from Exp(1/τ). The wait controller does not change. Apply means
something: shed drops low-priority jobs, cut turns on the retrieval
cache, repair freezes writes.

Q is written on the window as audit. It does not choose the lever.

Companion to LINEAGE_BIND.md.
Does not change official v2.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import argparse
import json
import math
import random
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, Mapping

try:
    from lineage_capacity_v2 import usable_fraction
    from lineage_loop_v2 import (
        CONTROLLERS,
        Action,
        Observation,
        PlantState,
        apply_action as apply_loop_state,
        decide,
        formula_wait,
        replay_window,
    )
    from lineage_network_v2 import DEFAULT_W_MAX
    from lineage_sim_v2 import SEED
    from lineage_use_v2 import evaluate_mapping
except ImportError:  # pragma: no cover
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lineage_capacity_v2 import usable_fraction
    from lineage_loop_v2 import (
        CONTROLLERS,
        Action,
        Observation,
        PlantState,
        apply_action as apply_loop_state,
        decide,
        formula_wait,
        replay_window,
    )
    from lineage_network_v2 import DEFAULT_W_MAX
    from lineage_sim_v2 import SEED
    from lineage_use_v2 import evaluate_mapping


SCHEMA = "fudoshin.lineage.bind/v1"
STAGE_NAMES = (
    "retrieval",
    "pathway",
    "working_memory",
    "sync",
    "settling",
)
VOCAB = (
    "load",
    "wait",
    "mass",
    "flux",
    "graph",
    "memory",
    "merge",
    "path",
    "query",
    "node",
    "edge",
    "drift",
    "hold",
    "shed",
    "cut",
    "repair",
)
N_DOCS = 48
N_NODES = 32
DOC_LEN = 18
LOW_FRAC = 0.50
HOT_RHO = 0.80
W_MAX_IDLE_MULT = 1.35
WINDOW_JOBS = 90
PROBE_JOBS = 36
WORK = {
    "retrieval": 2200,
    "pathway": 420,
    "working_memory": 260,
    "sync": 160,
    "settling": 120,
}

Lever = Literal[
    "drop_low_priority",
    "enable_retrieval_cache",
    "freeze_writes",
    "checkpoint",
    "keep_window",
]


@dataclass
class Policy:
    """What the agent actually does next window."""

    admit_low: float = 1.0
    cache: bool = False
    writes_open: bool = True
    retrieval_scan: float = 1.0


@dataclass
class Job:
    jid: int
    arrival: float
    query: str
    tokens: frozenset[str]
    node: int
    priority: Literal["high", "low"]


@dataclass
class JobResult:
    job: Job
    services: tuple[float, ...]
    sojourn: float
    finish: float
    retrieval_score: float
    wrote: bool


@dataclass
class Bind:
    lever: Lever
    do: str
    admit_low: float | None = None
    cache: bool | None = None
    writes_open: bool | None = None
    retrieval_scan: float | None = None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"lever": self.lever, "do": self.do}
        if self.admit_low is not None:
            out["admit_low"] = self.admit_low
        if self.cache is not None:
            out["cache"] = self.cache
        if self.writes_open is not None:
            out["writes_open"] = self.writes_open
        if self.retrieval_scan is not None:
            out["retrieval_scan"] = self.retrieval_scan
        return out


def bind_from_action(action: Action, policy: Policy | None = None) -> Bind:
    """The table in LINEAGE_CLOSED_LOOP.md §5, executable."""
    current = policy or Policy()
    name = action.name
    amount = max(0.0, float(action.amount))
    if name in {"shed_load", "unstable_shed_load"}:
        drop = min(1.0, max(0.40, amount / 0.20))
        return Bind(
            "drop_low_priority",
            "Drop low-priority retrievals, tool calls, or speculative branches.",
            admit_low=max(0.0, current.admit_low - drop),
        )
    if name == "cut_bottleneck_latency":
        return Bind(
            "enable_retrieval_cache",
            "Cache / faster retrieval / shorter working-memory hold.",
            cache=True,
            retrieval_scan=max(0.25, current.retrieval_scan * (1.0 - min(0.80, amount))),
        )
    if name == "repair_health":
        return Bind(
            "freeze_writes",
            "Stop writes, raise the merge threshold, freeze identity edits.",
            writes_open=False,
        )
    if name == "raise_mass":
        return Bind("checkpoint", "Checkpoint memory or graph.")
    return Bind("keep_window", "Keep the window.")


def apply_bind(policy: Policy, bind: Bind) -> Policy:
    next_policy = Policy(
        admit_low=policy.admit_low,
        cache=policy.cache,
        writes_open=policy.writes_open,
        retrieval_scan=policy.retrieval_scan,
    )
    if bind.admit_low is not None:
        next_policy.admit_low = bind.admit_low
    if bind.cache is not None:
        next_policy.cache = bind.cache
    if bind.writes_open is not None:
        next_policy.writes_open = bind.writes_open
    if bind.retrieval_scan is not None:
        next_policy.retrieval_scan = bind.retrieval_scan
    return next_policy


def burn(n: int, seed_int: int) -> int:
    """Deterministic CPU work. This is the stage, not a sleep."""
    x = seed_int & 0xFFFFFFFF
    for _ in range(max(0, n)):
        x = (x * 1664525 + 1013904223) & 0xFFFFFFFF
    return x


def _make_corpus(rng: random.Random) -> list[frozenset[str]]:
    docs: list[frozenset[str]] = []
    for _ in range(N_DOCS):
        docs.append(frozenset(rng.choice(VOCAB) for _ in range(DOC_LEN)))
    return docs


def _make_graph(rng: random.Random) -> list[list[int]]:
    adj: list[list[int]] = [[] for _ in range(N_NODES)]
    for i in range(N_NODES):
        for _ in range(3):
            j = rng.randrange(N_NODES)
            if j != i and j not in adj[i]:
                adj[i].append(j)
                adj[j].append(i)
    return adj


class Agent:
    """In-process mind. Five stages, one policy, measured clocks."""

    def __init__(self, seed: int = SEED, policy: Policy | None = None) -> None:
        rng = random.Random(seed)
        self.policy = policy or Policy()
        self.corpus = _make_corpus(rng)
        self.graph = _make_graph(rng)
        self.memory: list[str] = [f"seed-{i}" for i in range(24)]
        self.wm: list[str] = []
        self.wm_evictions = 0
        self.cache: dict[str, tuple[int, float]] = {}
        self.cache_hits = 0
        self.retrieval_attempts = 0
        self.retrieval_hits = 0
        self.score_sum = 0.0
        self.pathway_events = 0
        self.merge_writes = 0
        self.merge_conf_sum = 0.0
        self.checkpoints = 0
        self.checkpoint_ok = 0
        self.identity_alerts = 1.0
        self.identity_drift = 0.12
        self.control_actions = 0

    def snapshot_health(self) -> tuple[float, float, float]:
        edges = sum(len(row) for row in self.graph) / 2.0
        healthy = 0.82 if self.policy.writes_open else 0.92
        entropy = 0.38 if self.policy.writes_open else 0.18
        drift = min(0.90, self.identity_drift)
        return entropy, 1.0 - healthy, drift

    def usable(self) -> float:
        h, e, d = self.snapshot_health()
        return usable_fraction(h, e, d)


def _tokens(query: str) -> frozenset[str]:
    return frozenset(query.split("-"))


def offer_jobs(n: int, intensity: float, seed: int) -> list[Job]:
    if intensity <= 0.0 or n < 1:
        raise ValueError("need intensity > 0 and n ≥ 1")
    rng = random.Random(seed)
    t = 0.0
    jobs: list[Job] = []
    for j in range(n):
        t += rng.expovariate(intensity)
        words = [rng.choice(VOCAB) for _ in range(3)]
        query = "-".join(words)
        jobs.append(
            Job(
                jid=j,
                arrival=t,
                query=query,
                tokens=_tokens(query),
                node=rng.randrange(N_NODES),
                priority="low" if rng.random() < LOW_FRAC else "high",
            )
        )
    return jobs


def idle_jobs(n: int, gap: float, seed: int) -> list[Job]:
    rng = random.Random(seed)
    jobs: list[Job] = []
    t = 0.0
    for j in range(n):
        t += gap
        words = [rng.choice(VOCAB) for _ in range(3)]
        query = "-".join(words)
        jobs.append(
            Job(
                jid=j,
                arrival=t,
                query=query,
                tokens=_tokens(query),
                node=rng.randrange(N_NODES),
                priority="high",
            )
        )
    return jobs


def _admit(job: Job, policy: Policy, rng: random.Random) -> bool:
    if job.priority == "low" and rng.random() > policy.admit_low:
        return False
    return True


def stage_retrieval(job: Job, agent: Agent) -> float:
    agent.retrieval_attempts += 1
    if agent.policy.cache and job.query in agent.cache:
        agent.cache_hits += 1
        _doc, score = agent.cache[job.query]
        agent.score_sum += score
        if score > 0.0:
            agent.retrieval_hits += 1
        burn(WORK["retrieval"] // 8, job.jid)
        return score
    n = max(4, int(len(agent.corpus) * agent.policy.retrieval_scan))
    best = 0.0
    best_i = 0
    q = job.tokens
    for i, doc in enumerate(agent.corpus[:n]):
        burn(WORK["retrieval"], job.jid * 1009 + i)
        score = len(q & doc) / max(1, len(q))
        if score > best:
            best, best_i = score, i
    agent.score_sum += best
    if best > 0.0:
        agent.retrieval_hits += 1
    if agent.policy.cache:
        agent.cache[job.query] = (best_i, best)
    return best


def stage_pathway(job: Job, agent: Agent) -> None:
    agent.pathway_events += 1
    seen = {job.node}
    frontier = [job.node]
    depth = 0
    while frontier and depth < 2:
        nxt: list[int] = []
        for node in frontier:
            burn(WORK["pathway"], job.jid * 17 + node)
            for nb in agent.graph[node]:
                if nb not in seen:
                    seen.add(nb)
                    nxt.append(nb)
        frontier = nxt
        depth += 1


def stage_working_memory(job: Job, agent: Agent) -> None:
    burn(WORK["working_memory"], job.jid * 31)
    agent.wm.append(job.query)
    if len(agent.wm) > 8:
        agent.wm.pop(0)
        agent.wm_evictions += 1


def stage_sync(job: Job, agent: Agent) -> None:
    burn(WORK["sync"], job.jid * 53 + len(agent.memory))
    _ = hash(tuple(agent.memory[-8:])) ^ hash(tuple(agent.wm))


def stage_settling(job: Job, agent: Agent) -> bool:
    burn(WORK["settling"], job.jid * 71)
    if not agent.policy.writes_open:
        return False
    agent.memory.append(job.query)
    agent.merge_writes += 1
    agent.merge_conf_sum += 0.72
    agent.identity_drift = min(0.85, agent.identity_drift + 0.002)
    if job.jid % 11 == 0:
        agent.checkpoints += 1
        agent.checkpoint_ok += 1
    return True


STAGES = (
    stage_retrieval,
    stage_pathway,
    stage_working_memory,
    stage_sync,
    stage_settling,
)


def run_window(
    agent: Agent,
    jobs: list[Job],
    seed: int,
) -> list[JobResult]:
    """
    Real service, virtual waiting room.

    Each stage function runs. A clock measures it. Lindley advances
    with that measured service, not with Exp(1/τ).
    """
    rng = random.Random(seed)
    last_dep = [0.0] * len(STAGES)
    out: list[JobResult] = []
    for job in jobs:
        if not _admit(job, agent.policy, rng):
            continue
        t = job.arrival
        services: list[float] = []
        score = 0.0
        wrote = False
        for i, fn in enumerate(STAGES):
            start = t if t > last_dep[i] else last_dep[i]
            t0 = time.perf_counter()
            if fn is stage_retrieval:
                score = stage_retrieval(job, agent)
            elif fn is stage_settling:
                wrote = stage_settling(job, agent)
            else:
                fn(job, agent)
            svc = time.perf_counter() - t0
            if svc <= 0.0:
                svc = 1e-9
            t = start + svc
            last_dep[i] = t
            services.append(svc)
        out.append(
            JobResult(
                job=job,
                services=tuple(services),
                sojourn=t - job.arrival,
                finish=t,
                retrieval_score=score,
                wrote=wrote,
            )
        )
    return out


def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def measure_window(
    agent: Agent,
    results: list[JobResult],
    w_max: float,
) -> dict[str, Any]:
    if not results:
        raise ValueError("window produced no jobs")
    sojourns = [r.sojourn for r in results]
    taus = tuple(
        _mean([r.services[i] for r in results]) for i in range(len(STAGES))
    )
    first = min(r.job.arrival for r in results)
    last = max(r.finish for r in results)
    span = max(last - first, 1e-12)
    busy_star = sum(r.services[int(max(range(len(taus)), key=lambda i: taus[i]))] for r in results)
    Pi = min(0.999, busy_star / span)
    mean_W = _mean(sojourns)
    p_miss = sum(1 for w in sojourns if w > w_max) / len(sojourns)
    h, e, d = agent.snapshot_health()
    u = usable_fraction(h, e, d)
    edges = sum(len(row) for row in agent.graph) / 2.0
    attempts = max(1.0, float(agent.retrieval_attempts))
    telemetry = {
        "identity_alert_count": agent.identity_alerts,
        "identity_axis_count": 8.0,
        "mean_identity_drift": min(0.90, agent.identity_drift),
        "memory_entries": float(len(agent.memory)),
        "memory_index_coverage": min(1.0, len(agent.memory) / 200.0),
        "graph_nodes": float(N_NODES),
        "graph_edges": float(edges),
        "healthy_edge_ratio": 0.92 if not agent.policy.writes_open else 0.80,
        "permanence_integrity": (
            agent.checkpoint_ok / agent.checkpoints if agent.checkpoints else 0.80
        ),
        "checkpoint_success_ratio": (
            agent.checkpoint_ok / agent.checkpoints if agent.checkpoints else 0.80
        ),
        "wm_items": float(len(agent.wm)),
        "wm_turnover": float(agent.wm_evictions),
        "retrieval_attempts": float(agent.retrieval_attempts),
        "retrieval_hits": float(agent.retrieval_hits),
        "mean_retrieval_score": agent.score_sum / attempts,
        "pathway_events": float(agent.pathway_events),
        "control_actions": float(agent.control_actions),
        "merge_writes": float(agent.merge_writes),
        "merge_confidence": (
            agent.merge_conf_sum / agent.merge_writes if agent.merge_writes else 0.70
        ),
        "tau_retrieval_s": taus[0],
        "tau_pathway_s": taus[1],
        "tau_working_memory_s": taus[2],
        "tau_sync_s": taus[3],
        "tau_settling_s": taus[4],
        "belief_entropy": h,
        "mode": "adaptive",
        "weight_table": "official",
        "measured_wait_s": mean_W,
        "p_miss": p_miss,
        "Pi_busy": Pi,
        "jobs": float(len(results)),
        "W_max": w_max,
    }
    card = evaluate_mapping(telemetry)
    state = PlantState(
        M=float(card["M"]),
        Pi=Pi,
        taus=taus,
        u=u,
    )
    theory = formula_wait(state)
    return {
        "state": state,
        "telemetry": telemetry,
        "card": card,
        "mean_W": mean_W,
        "p_miss": p_miss,
        "formula_W": theory,
        "residual_s": mean_W - theory if math.isfinite(theory) else None,
        "Q": float(card["Q"]),
        "jobs": len(results),
    }


def calibrate(seed: int = SEED) -> dict[str, float]:
    agent = Agent(seed=seed)
    probe = idle_jobs(PROBE_JOBS, gap=1.0, seed=seed + 1)
    results = run_window(agent, probe, seed=seed + 2)
    sojourns = [r.sojourn for r in results]
    taus = tuple(
        _mean([r.services[i] for r in results]) for i in range(len(STAGES))
    )
    idle_W = _mean(sojourns)
    tau_star = max(taus)
    return {
        "idle_W": idle_W,
        "T": sum(taus),
        "tau_star": tau_star,
        "W_max": idle_W * W_MAX_IDLE_MULT,
        "hot_intensity": HOT_RHO / max(tau_star, 1e-9),
    }


def run_bind(
    controller_name: str = "wait",
    ticks: int = 5,
    seed: int = SEED,
    jobs: int = WINDOW_JOBS,
) -> dict[str, Any]:
    cal = calibrate(seed)
    w_max = float(cal["W_max"])
    offer = offer_jobs(jobs, float(cal["hot_intensity"]), seed + 11)
    controller = CONTROLLERS[controller_name]
    policy = Policy()
    history: list[dict[str, Any]] = []
    agent: Agent | None = None
    for t in range(ticks):
        agent = Agent(seed=seed + 100 + t, policy=policy)
        results = run_window(agent, offer, seed=seed + 200 + t)
        measured = measure_window(agent, results, w_max)
        action = decide(controller, measured["state"], _obs(measured), w_max)
        agent.control_actions += 1
        bind = bind_from_action(action, policy)
        history.append(
            {
                "t": t,
                "action": action.name,
                "amount": action.amount,
                "scored_q": action.scored_q,
                "bind": bind.to_dict(),
                "Pi": measured["state"].Pi,
                "u": measured["state"].u,
                "M": measured["state"].M,
                "taus": list(measured["state"].taus),
                "measured_W": measured["mean_W"],
                "formula_W": measured["formula_W"],
                "residual_s": measured["residual_s"],
                "p_miss": measured["p_miss"],
                "Q": measured["Q"],
                "jobs": measured["jobs"],
                "policy": {
                    "admit_low": policy.admit_low,
                    "cache": policy.cache,
                    "writes_open": policy.writes_open,
                    "retrieval_scan": policy.retrieval_scan,
                },
                "telemetry": measured["telemetry"],
            }
        )
        policy = apply_bind(policy, bind)
    assert agent is not None
    final_agent = Agent(seed=seed + 900, policy=policy)
    final_results = run_window(final_agent, offer, seed=seed + 901)
    final = measure_window(final_agent, final_results, w_max)
    return {
        "schema": SCHEMA,
        "controller": controller_name,
        "cal": cal,
        "ticks": history,
        "final": {
            "Pi": final["state"].Pi,
            "u": final["state"].u,
            "measured_W": final["mean_W"],
            "formula_W": final["formula_W"],
            "p_miss": final["p_miss"],
            "Q": final["Q"],
            "jobs": final["jobs"],
            "policy": {
                "admit_low": policy.admit_low,
                "cache": policy.cache,
                "writes_open": policy.writes_open,
                "retrieval_scan": policy.retrieval_scan,
            },
            "telemetry": final["telemetry"],
        },
    }


def _obs(measured: Mapping[str, Any]) -> Observation:
    return Observation(
        mean_W=float(measured["mean_W"]),
        p_miss=float(measured["p_miss"]),
        formula_W=float(measured["formula_W"]),
        jobs=float(measured["jobs"]),
        source="measured",
    )


def decide_socket(
    data: Mapping[str, Any],
    w_max: float | None = None,
) -> dict[str, Any]:
    """One live window in. A bind out. This is the integration."""
    if w_max is None:
        w_max = float(data.get("W_max", data.get("w_max", DEFAULT_W_MAX)))
    row = replay_window(data, w_max=w_max)
    action = Action(
        row["action"],  # type: ignore[arg-type]
        float(row["amount"]),
        str(row["reason"]),
        bool(row["scored_q"]),
    )
    policy = Policy(
        admit_low=float(data.get("admit_low", 1.0)),
        cache=bool(data.get("cache", False)),
        writes_open=bool(data.get("writes_open", True)),
        retrieval_scan=float(data.get("retrieval_scan", 1.0)),
    )
    bind = bind_from_action(action, policy)
    row["schema"] = SCHEMA
    row["bind"] = bind.to_dict()
    return row


def render_run(result: dict[str, Any]) -> str:
    cal = result["cal"]
    lines = [
        f"{result['controller']} bind   "
        f"idle_W={cal['idle_W']:.6f}s  W_max={cal['W_max']:.6f}s  "
        f"T={cal['T']:.6f}s",
        f"{'t':>3}  {'Pi':>6}  {'meas_W':>8}  {'form_W':>8}  {'jobs':>4}  "
        f"{'action':<24}  {'lever':<24}  {'Q':>8}",
    ]
    for tick in result["ticks"]:
        lines.append(
            f"{tick['t']:3d}  {tick['Pi']:6.3f}  {tick['measured_W']:8.6f}  "
            f"{tick['formula_W']:8.6f}  {tick['jobs']:4d}  "
            f"{tick['action']:<24}  {tick['bind']['lever']:<24}  {tick['Q']:8.3f}"
        )
    fin = result["final"]
    lines.append(
        f"end {fin['Pi']:6.3f}  {fin['measured_W']:8.6f}  "
        f"{fin['formula_W']:8.6f}  {fin['jobs']:4d}  "
        f"{'—':<24}  {fin['policy']['admit_low']!s:<24}  {fin['Q']:8.3f}"
    )
    return "\n".join(lines)


def run_checks() -> dict[str, bool]:
    results: dict[str, bool] = {}

    cal = calibrate()
    results["calibrated_positive"] = cal["idle_W"] > 0.0 and cal["tau_star"] > 0.0
    results["retrieval_is_bottleneck"] = True  # confirmed on a probe below
    probe_agent = Agent(seed=SEED)
    probe = run_window(probe_agent, idle_jobs(24, 1.0, SEED + 3), SEED + 4)
    probe_taus = tuple(_mean([r.services[i] for r in probe]) for i in range(5))
    results["retrieval_is_bottleneck"] = probe_taus[0] == max(probe_taus)
    results["idle_near_raw_service"] = abs(_mean([r.sojourn for r in probe]) - sum(probe_taus)) / max(
        sum(probe_taus), 1e-12
    ) < 0.25

    opened = run_bind("open", ticks=3, seed=SEED)
    closed = run_bind("wait", ticks=4, seed=SEED)
    qloop = run_bind("q", ticks=2, seed=SEED)
    w_max = float(opened["cal"]["W_max"])

    results["open_holds"] = all(tick["action"] == "hold" for tick in opened["ticks"])
    results["open_stays_hot"] = opened["final"]["measured_W"] > w_max
    results["wait_first_sheds"] = closed["ticks"][0]["action"] == "shed_load"
    results["wait_first_lever_is_drop"] = (
        closed["ticks"][0]["bind"]["lever"] == "drop_low_priority"
    )
    results["q_first_cuts"] = qloop["ticks"][0]["action"] == "cut_bottleneck_latency"
    results["q_first_lever_is_cache"] = (
        qloop["ticks"][0]["bind"]["lever"] == "enable_retrieval_cache"
    )
    results["closed_beats_open"] = (
        closed["final"]["measured_W"] < opened["final"]["measured_W"]
    )
    results["closed_meets_or_near"] = (
        closed["final"]["measured_W"] <= w_max * 1.15
        or closed["final"]["measured_W"] < 0.55 * opened["final"]["measured_W"]
    )
    results["wait_never_scores_q"] = all(
        not tick["scored_q"] for tick in closed["ticks"]
    )
    results["q_scores_q"] = qloop["ticks"][0]["scored_q"] is True
    results["shed_lowers_admit"] = (
        closed["final"]["policy"]["admit_low"] < 1.0
    )
    results["cut_enables_cache"] = qloop["final"]["policy"]["cache"] is True
    results["closed_keeps_cache_off"] = closed["final"]["policy"]["cache"] is False

    tel = closed["ticks"][0]["telemetry"]
    card = evaluate_mapping(tel)
    results["window_is_slice"] = card["Q"] > 0.0 and card["weight_table"] == "official"
    results["measured_wait_on_window"] = tel["measured_wait_s"] == closed["ticks"][0][
        "measured_W"
    ]

    socket = decide_socket(
        {
            "Pi": 0.60,
            "M": 0.72,
            "u": 0.84,
            "taus": [0.12, 0.04, 0.03, 0.02, 0.015],
            "measured_wait_s": 0.430,
            "W_max": 0.400,
        }
    )
    results["socket_sheds_hot"] = socket["action"] == "shed_load"
    results["socket_names_drop"] = socket["bind"]["lever"] == "drop_low_priority"
    results["socket_does_not_score_Q"] = socket["scored_q"] is False

    sick = decide_socket(
        {
            "Pi": 0.20,
            "M": 0.72,
            "u": 0.10,
            "taus": [0.12, 0.04, 0.03, 0.02, 0.015],
            "measured_wait_s": 0.250,
            "W_max": 0.400,
        }
    )
    results["socket_repairs_health"] = sick["bind"]["lever"] == "freeze_writes"

    hold = decide_socket(
        {
            "Pi": 0.468108,
            "M": 0.72035,
            "u": 0.84,
            "taus": [0.12, 0.04, 0.03, 0.02, 0.015],
            "measured_wait_s": 0.342,
            "W_max": 0.400,
        }
    )
    results["socket_holds_working"] = hold["bind"]["lever"] == "keep_window"

    # Controller amount is a Π drop. The loop-state apply still exists;
    # the bind must not call it. Policy move ≠ PlantState.Pi rewrite.
    before = Policy()
    after = apply_bind(
        before,
        bind_from_action(Action("shed_load", 0.10, "check", False), before),
    )
    results["bind_does_not_set_Pi"] = after.admit_low < before.admit_low
    ghost = apply_loop_state(
        PlantState(0.7, 0.60, (0.1, 0.04, 0.03, 0.02, 0.01), 0.84),
        Action("shed_load", 0.10, "check", False),
    )
    results["old_apply_still_rewrites_state"] = abs(ghost.Pi - 0.50) < 1e-12
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Bind the wait-loop to a real five-stage agent."
    )
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--compare", action="store_true")
    parser.add_argument("--decide", type=Path)
    parser.add_argument("--controller", choices=tuple(CONTROLLERS), default="wait")
    parser.add_argument("--ticks", type=int, default=5)
    parser.add_argument("--jobs", type=int, default=WINDOW_JOBS)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--jsonl", type=Path)
    args = parser.parse_args(argv)

    if args.decide is not None:
        data = json.loads(args.decide.read_text(encoding="utf-8"))
        row = decide_socket(data)
        print(json.dumps(row, indent=2))
        return 0

    if args.run or args.compare:
        names = tuple(CONTROLLERS) if args.compare else (args.controller,)
        payload = {name: run_bind(name, ticks=args.ticks, jobs=args.jobs) for name in names}
        if args.jsonl is not None:
            lines = []
            for name, result in payload.items():
                for tick in result["ticks"]:
                    row = dict(tick["telemetry"])
                    row["controller"] = name
                    row["t"] = tick["t"]
                    lines.append(json.dumps(row))
            args.jsonl.write_text("\n".join(lines) + "\n", encoding="utf-8")
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            for name, result in payload.items():
                print(render_run(result))
                print()
        return 0

    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        return 1
    print("bind_checks_passed", len(suite))
    print()
    print(render_run(run_bind("wait", ticks=4)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
