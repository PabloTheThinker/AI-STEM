# Lineage Equation reference (v2)

**Fudoshin Research · Vektra Industries**

Pure-Python official implementation of the Lineage Equation, plus the computable slice.

- Spec: `../LINEAGE_EQUATION_V2_OFFICIAL.md`
- Slice spec: `../../canon/CONCRETE_COMPUTABLE_SLICE.md`
- Law module: `lineage_capacity_v2.py`
- Slice module: `lineage_slice_v2.py`
- Geometry module: `lineage_geometry_v2.py`
- Example record: `example_telemetry.json`

```bash
python3 ams_kernel_v2.py
python3 lineage_capacity_v2.py
python3 lineage_slice_v2.py --example
python3 lineage_slice_v2.py --json example_telemetry.json
python3 lineage_geometry_v2.py
```

Expect `ams_theorems_passed 11`, `all_validation_checks_passed 16`, `slice_validation_checks_passed 31`, and `geometry_validation_checks_passed 17`.
