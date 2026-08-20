# Lineage Equation reference (v2)

**Fudoshin Research · Vektra Industries**

Pure-Python official implementation of the Lineage Equation, plus the computable slice.

- Spec: `../LINEAGE_EQUATION_V2_OFFICIAL.md`
- Slice spec: `../../canon/CONCRETE_COMPUTABLE_SLICE.md`
- Law module: `lineage_capacity_v2.py`
- Slice module: `lineage_slice_v2.py`
- Example record: `example_telemetry.json`

```bash
python3 lineage_capacity_v2.py
python3 lineage_slice_v2.py --example
python3 lineage_slice_v2.py --json example_telemetry.json
```

Expect `all_validation_checks_passed 16` and `slice_validation_checks_passed 31`.
