# Lineage Equation reference (v2)

**Fudoshin Research · Vektra Industries**

Pure-Python official implementation of the Lineage Equation, plus the computable slice and the operator instrument.

- Spec: `../LINEAGE_EQUATION_V2_OFFICIAL.md`
- Operator manual: `../../canon/LINEAGE_EQUATION_USABLE.md`
- Slice spec: `../../canon/CONCRETE_COMPUTABLE_SLICE.md`
- Law module: `lineage_capacity_v2.py`
- Operator instrument: `lineage_use_v2.py`
- Slice module: `lineage_slice_v2.py`
- Geometry module: `lineage_geometry_v2.py`
- Example records: `example_telemetry.json`, `minimal_telemetry.json`

```bash
python3 lineage_use_v2.py --example
python3 lineage_use_v2.py example_telemetry.json
python3 lineage_use_v2.py example_telemetry.json --cut-ms 20
python3 lineage_use_v2.py --self-test
python3 lineage_capacity_v2.py
python3 lineage_slice_v2.py --example
python3 lineage_geometry_v2.py
```

Expect `use_checks_passed 17`, `all_validation_checks_passed 20`, `slice_validation_checks_passed 31`, and `geometry_validation_checks_passed 17`.
