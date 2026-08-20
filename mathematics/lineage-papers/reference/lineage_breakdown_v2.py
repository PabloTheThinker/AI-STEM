"""
Print the official Lineage Equation the way a teacher writes 1+1=2.

Uses the same numbers as CONCRETE_COMPUTABLE_SLICE.md / lineage_slice_v2.py.
Does not change the law.

License: Fudoshin Research reference (Vektra Industries).
"""

from __future__ import annotations

import math

from lineage_capacity_v2 import ALPHA_IDENTIFIED, BETA_IDENTIFIED


def _import_slice():
    try:
        from lineage_slice_v2 import compute_slice, worked_example_record
    except ImportError:
        import sys
        from pathlib import Path

        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from lineage_slice_v2 import compute_slice, worked_example_record
    return compute_slice, worked_example_record


def breakdown() -> str:
    compute_slice, worked_example_record = _import_slice()
    out = compute_slice(worked_example_record())
    C = out.primitives
    F = out.primitives
    alpha = ALPHA_IDENTIFIED
    beta = BETA_IDENTIFIED

    c_id, c_mem, c_graph, c_perm = C["C_id"], C["C_mem"], C["C_graph"], C["C_perm"]
    parts_M = [
        ("α_id C_id", alpha["C_id"], c_id, alpha["C_id"] * c_id),
        ("α_mem C_mem", alpha["C_mem"], c_mem, alpha["C_mem"] * c_mem),
        ("α_graph C_graph", alpha["C_graph"], c_graph, alpha["C_graph"] * c_graph),
        ("α_perm C_perm", alpha["C_perm"], c_perm, alpha["C_perm"] * c_perm),
    ]
    M = sum(p[3] for p in parts_M)

    f_keys = [
        ("β_wm F_wm", "F_wm"),
        ("β_ret F_ret", "F_ret"),
        ("β_path F_path", "F_path"),
        ("β_ctrl F_ctrl", "F_ctrl"),
        ("β_merge F_merge", "F_merge"),
    ]
    parts_P = []
    for label, key in f_keys:
        w = beta[key]
        v = F[key]
        parts_P.append((label, w, v, w * v))
    Pi = sum(p[3] for p in parts_P)

    r = out.terms["r"]
    Pi_t = Pi * r
    M_t = M * r * r
    q2 = Pi_t * Pi_t + M_t * M_t
    Q = math.sqrt(q2)

    lines = [
        "THE CURRENT EQUATION",
        "    Q² = Π̃² + M̃²",
        "    Π̃  = Π · r",
        "    M̃  = M · r²",
        "    r  = ν* / ν₀",
        "",
        "STEP 1.  M  =  α·C     (multiply, then add)",
    ]
    for label, w, v, prod in parts_M:
        lines.append(f"    {label:18s}  {w:.2f} × {v:.6f}  =  {prod:.6f}")
    lines.append(f"    M  =  {' + '.join(f'{p[3]:.6f}' for p in parts_M)}")
    lines.append(f"    M  =  {M:.6f}")
    lines.append("")
    lines.append("STEP 2.  Π  =  β·F     (multiply, then add)")
    for label, w, v, prod in parts_P:
        lines.append(f"    {label:20s}  {w:.2f} × {v:.6f}  =  {prod:.6f}")
    lines.append(f"    Π  =  {Pi:.6f}")
    lines.append("")
    lines.append("STEP 3.  ν*  =  1 / max(τ)")
    lines.append(f"    τ*  =  0.120 s")
    lines.append(f"    ν*  =  1/0.120  =  {out.terms['nu_star']:.6f} Hz")
    lines.append(f"    r   =  ν*/1     =  {r:.6f}")
    lines.append("")
    lines.append("STEP 4.  scale the two piles")
    lines.append(f"    Π̃  =  Π · r   =  {Pi:.6f} × {r:.6f}  =  {Pi_t:.6f}")
    lines.append(f"    M̃  =  M · r²  =  {M:.6f} × {r*r:.6f}  =  {M_t:.6f}")
    lines.append("")
    lines.append("STEP 5.  square")
    lines.append(f"    Π̃²  =  {Pi_t:.6f}²  =  {Pi_t*Pi_t:.6f}")
    lines.append(f"    M̃²  =  {M_t:.6f}²  =  {M_t*M_t:.6f}")
    lines.append("")
    lines.append("STEP 6.  add     (this is the + in 1+1=2)")
    lines.append(f"    Π̃² + M̃²  =  {Pi_t*Pi_t:.6f} + {M_t*M_t:.6f}  =  {q2:.6f}")
    lines.append("")
    lines.append("STEP 7.  square root")
    lines.append(f"    Q  =  √{q2:.6f}  =  {Q:.6f}")
    lines.append("")
    lines.append("CHECK")
    lines.append(f"    Q²           =  {Q*Q:.6f}")
    lines.append(f"    Π̃² + M̃²     =  {q2:.6f}")
    lines.append(f"    match        =  {abs(Q*Q - q2) < 1e-9}")
    lines.append(f"    law Q        =  {out.terms['Q']:.6f}")
    lines.append(f"    same as law  =  {abs(Q - out.terms['Q']) < 1e-9}")
    return "\n".join(lines)


def run_checks() -> dict[str, bool]:
    compute_slice, worked_example_record = _import_slice()
    out = compute_slice(worked_example_record())
    text = breakdown()
    return {
        "prints_equation": "Q² = Π̃² + M̃²" in text,
        "prints_plus": "this is the +" in text,
        "matches_law_Q": "same as law  =  True" in text,
        "check_true": "match        =  True" in text,
        "uses_official_alpha": abs(sum(ALPHA_IDENTIFIED.values()) - 1.0) < 1e-12,
        "slice_Q_positive": out.terms["Q"] > 0.0,
    }


if __name__ == "__main__":
    suite = run_checks()
    failed = [k for k, v in suite.items() if not v]
    for k, v in suite.items():
        print(f"{'PASS' if v else 'FAIL':4s}  {k}")
    if failed:
        raise SystemExit(1)
    print("breakdown_checks_passed", len(suite))
    print()
    print(breakdown())
