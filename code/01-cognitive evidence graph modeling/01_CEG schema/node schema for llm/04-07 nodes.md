# Nodes 04-07: Unified Extraction of Fault Information Nodes (v5)

## [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

---

## [Task]

Extract 4 types of fault information nodes involved in the paper in one pass: fault location, fault mode, fault severity, and whether compound faults are included. Output a multi-node JSON array.

### The 4 Types of Nodes Involved

| No. | Node Type | Multiple Nodes | node_name Options |
|------|---------|-------|--------------|
| 04 | Fault Location | Yes (1-N) | Fill null |
| 05 | Fault Mode | Yes (1-N) | Fill null |
| 06 | Fault Severity | No (1) | Choose 1 from 2 |
| 07 | Compound Fault | No (1) | Choose 1 from 3 |

---

## [JSON Format]

**⚠️ Outer `[...]`, 06/07 each have 1 node; 04/05 may have multiple (N1/N2/N3... incrementing).**

```json
[
  { "node_id": "<case_id>_04_N1", "node_type": "04-Fault Location", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_05_N1", "node_type": "05-Fault Mode", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_06_N1", "node_type": "06-Fault Severity", "node_original_name": "", "node_name": "", "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_07_N1", "node_type": "07-Compound Fault", "node_original_name": "", "node_name": "", "node_description": "", "node_case_id_list": null }
]
```

---

## [Definitions of Each Node Type]

### Node 04: Fault Location

**Definition**: The **specific equipment or component** where the fault occurs in the paper.

**Explicit Identification**: The fault location explicitly stated in the experimental section of the paper.

**Implicit Reasoning**: When the paper only mentions the fault mode, infer based on the research object:

| Fault Mode | Inferred Location |
|---------|---------|
| rotor bar / broken rotor / rotor fault | Motor (rotor is an internal component of the motor) |
| stator winding / stator fault | Motor (winding is an internal component of the motor) |
| bearing fault | Bearing |
| gear / fault / gearbox fault | Gearbox |
| blade crack | Blade / Rotor |
| shaft crack | Shaft |
| coupling fault | Coupling |

⚠️ Must be at the **entity-equipment / component level**; system-level (e.g., "aerospace system") is not allowed.

**Fields**: `node_original_name` = original English text; `node_name` = null; `node_description` = describe the specific location in English. **Extract only the locations involved in the paper's own experiments.**

---

### Node 05: Fault Mode

**Definition**: The **specific fault manifestations** (physical mechanism or damage type) involved in the paper's experiments.

**Fault Mode Identification (Divided into 3 Major Categories by Physical Mechanism)**

| Category | Fault Mode | English Keywords |
|------|---------|-----------|
| Surface Damage | Pitting | pitting, surface pitting |
| Surface Damage | Spalling | spalling, flaking |
| Surface Damage | Wear | wear, abrasive wear |
| Surface Damage | Corrosion | corrosion |
| Structural Failure | Crack | crack, fatigue crack |
| Structural Failure | Fracture | fracture, broken |
| Structural Failure | Short Circuit | short circuit |
| Structural Failure | Open Circuit | open circuit |
| Dynamic Abnormality | Imbalance | imbalance, unbalance |
| Dynamic Abnormality | Misalignment | misalignment |
| Dynamic Abnormality | Rubbing | rub, rubbing |

**Granularity**: ✅ Pitting / Crack / Broken Bar / Short Circuit (precise); ❌ Inner-ring pitting vs. outer-ring pitting (too fine, unify to "pitting"); ❌ Mechanical fault (too coarse)

**Fields**: `node_original_name` = original English text; `node_name` = null; `node_description` = describe the specific manifestation in English. **Extract only the modes involved in the paper's own experiments.**

---

### Node 06: Fault Severity

**Definition**: The quantitative description or grading of fault damage degree in the paper.

**node_name Choose 1 from 2**: `Single Severity` | `Multiple Severities`

| Judgment | Condition |
|------|------|
| `Multiple Severities` | Explicit grading; multiple diameters / depths; multi-level comparative experiments; includes performance degradation / life decay (RUL / degradation / health-state degradation curves) |
| `Single Severity` | Only a single fixed fault parameter, without multi-level comparison, no degradation / slow-change process |

**⚠️ Common Misjudgments**: Performance degradation, life prediction, progressive wear, crack propagation → `Multiple Severities` (slow-change type). Only injecting fixed-size faults (e.g., 0.3mm pitting) without comparison → `Single Severity`.

**Fields**: `node_original_name` = original English text of quantitative parameters, null if none; `node_name` = choose 1 from 2; `node_description` = two-paragraph format — paragraph 1: quantity and type; paragraph 2: values for each level.

---

### Node 07: Compound Fault

**Definition**: Whether the paper involves compound faults (multiple faults occurring simultaneously).

**node_name Choose 1 from 3**: `No Compound Fault` | `Compound Fault Within Same Structure` | `Compound Fault Across Structures`

| Judgment | Condition |
|------|------|
| `Compound Fault Across Structures` | Multiple faults exist simultaneously between different equipment / structures (bearing fault + gear fault) |
| `Compound Fault Within Same Structure` | Multiple faults exist simultaneously within the same equipment (inner-ring and outer-ring bearing faults simultaneously) |
| `No Compound Fault` | Only single-fault classification; or multiple faults injected independently (not at the same time) |

⚠️ **The core is "whether multiple faults occur simultaneously"**; independent injection → no compound fault.

**Fields**: `node_original_name` = original English text of compound fault, null if none; `node_name` = choose 1 from 3; `node_description` = two-paragraph format — paragraph 1: type; paragraph 2: specific combination or reason.

---

## [Relationship Between 04 and 05]

04 (Fault Location) and 05 (Fault Mode) must be mutually consistent: rotor bar fault → 04 inferred as Motor + 05 filled with rotor bar fault. Multiple fault modes on the same equipment → separate independent nodes. The quantities of 04 and 05 are not necessarily equal.

---

## [Mandatory Constraints]

1. `node_name` must be filled in with **standard English options**; English original text or non-standard variants are prohibited
2. 06/07 each have **1 node**; 04/05 may have multiple
3. **Extract only those involved in the paper's own experiments**, ignoring Introduction / Related Work / Baseline
4. When `node_description` is not null, fill in an English description
