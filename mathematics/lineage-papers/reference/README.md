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
- Core / scaling-family module: `lineage_core_v2.py`
- Operations / Little / renewal module: `lineage_ops_v2.py`
- Operational control module: `lineage_control_v2.py`
- Tandem / Kingman / SLA module: `lineage_network_v2.py`
- Pareto / Amdahl / PK / tail module: `lineage_qos_v2.py`
- Traffic-equation module (corrected default): `lineage_traffic_v2.py`
- Discrete-event simulation (Stage D): `lineage_sim_v2.py`
- Example records: `example_telemetry.json`, `minimal_telemetry.json`
- Core paper: `../LINEAGE_CORE_AND_SCALING_FAMILY.md`
- Tandem paper (all-hot upper bound): `../LINEAGE_TANDEM_KINGMAN_QOS.md`
- QoS paper (upper-bound numbers): `../LINEAGE_PARETO_AMDAHL_PK.md`
- Correction + simulation paper: `../LINEAGE_TRAFFIC_AND_SIMULATION.md`

```bash
python3 lineage_use_v2.py --example
python3 lineage_use_v2.py example_telemetry.json
python3 lineage_use_v2.py example_telemetry.json --cut-ms 20
python3 lineage_use_v2.py --self-test
python3 lineage_core_v2.py
python3 lineage_ops_v2.py
python3 lineage_control_v2.py
python3 lineage_network_v2.py
python3 lineage_qos_v2.py
python3 lineage_traffic_v2.py
python3 lineage_sim_v2.py
python3 lineage_capacity_v2.py
python3 lineage_slice_v2.py --example
python3 lineage_geometry_v2.py
```

Expect `use_checks_passed 34`, `core_checks_passed 19`, `ops_checks_passed 16`, `control_checks_passed 12`, `network_checks_passed 14`, `qos_checks_passed 19`, `traffic_checks_passed 24`, `sim_checks_passed 8`, `all_validation_checks_passed 20`, `slice_validation_checks_passed 31`, and `geometry_validation_checks_passed 17`.
