# Nodes 10-14: Unified Extraction of Data and Resource Nodes (v5)

## [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

---

## [Task]

Extract 5 types of data and resource nodes involved in the paper in one pass: dataset, sensor information, available training data volume, noise level, and computational resource. Output a multi-node JSON array.

### The 5 Types of Nodes Involved

| No. | Node Type | Multiple Nodes | node_name Options |
|------|---------|-------|--------------|
| 10 | Dataset | Yes (1-N) | Fill null |
| 11 | Sensor Information | Yes (1-N) | Fill null |
| 12 | Training Data Availability | No (1) | Choose 1 from 3 |
| 13 | Noise Level | No (1) | Choose 1 from 2 |
| 14 | Computational Resource | No (1) | Choose 1 from 3 |

---

## [JSON Format]

**⚠️ Outer `[...]`, 12/13/14 each have 1 node; 10/11 may have multiple (N1/N2/N3... incrementing).**

```json
[
  { "node_id": "<case_id>_10_N1", "node_type": "10-Dataset", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_11_N1", "node_type": "11-Sensor Information", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_12_N1", "node_type": "12-Training Data Availability", "node_original_name": "", "node_name": "", "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_13_N1", "node_type": "13-Noise Level", "node_original_name": "", "node_name": "", "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_14_N1", "node_type": "14-Computational Resource", "node_original_name": "", "node_name": "", "node_description": "", "node_case_id_list": null }
]
```

---

## [Definitions of Each Node Type]

### Node 10: Dataset

**Definition**: The data source **used by the paper's authors in their own experiments**.

| Dataset Category | Description | Example |
|-----------|------|------|
| Public Dataset | Freely downloadable from the internet | CWRU, PU, XJTU-SY, NASA Battery, C-MAPSS, MFPT, IMS |
| Private Dataset (Self-collected) | Authors built their own testbed for collection | Self-collected: |
| Private Dataset (Simulation) | Authors generated via simulation | Simulation: |

**Fields**: `node_original_name` = original English text; `node_name` = null; `node_description` = format as `<Category> + <Description>`, where the category is "Public Dataset" or "Private Dataset" (with spaces before and after +), e.g., `Public Dataset + CWRU Case Western Reserve University bearing dataset, vibration signals`.

Multiple datasets → multiple nodes. **Extract only those used in the paper's own experiments.**

---

### Node 11: Sensor Information

**Definition**: The data acquisition sensors used in the paper's experiments.

**Classify nodes by the sensed physical quantity category**, not by quantity or installation location.

| Sensor Category | English Keywords | Sensed Physical Quantity |
|-----------|-----------|-----------|
| Accelerometer | accelerometer, vibration sensor | Vibration acceleration |
| Acoustic Emission Sensor | acoustic emission sensor | Acoustic emission waves |
| Current Sensor | current sensor | Current signal |
| Voltage Sensor | voltage sensor | Voltage signal |
| Torque Sensor | torque sensor | Torque |
| Temperature Sensor | temperature sensor, thermocouple | Temperature |
| Speed Sensor | speed sensor, tachometer | Rotational speed |

Merging Principle: Drive-end + fan-end accelerometers → merge (both are vibration); accelerometer + vibration sensor → merge (same function).

**Fields**: `node_original_name` = original English text; `node_name` = null; `node_description` = describe the type, installation location, etc. in English. **Extract only those used in the paper's own experiments.**

---

### Node 12: Training Data Availability

**Definition**: The sufficiency of fault samples in the training set.

**node_name Choose 1 from 3**: `Zero-Sample` | `Scarce` | `Sufficient`

| Judgment | Condition |
|------|------|
| `Zero-Sample` | Number of samples per fault class = 0 (a certain fault is completely unseen), or the paper explicitly mentions zero-sample or similar descriptions when describing the paper's own training data |
| `Scarce` | Number of samples per class > 0 and < 40, or explicitly mentions scarcity / insufficiency, etc. |
| `Sufficient` | Number of samples per class ≥ 40, or no explicit mention of data scarcity or few-shot, etc. |

Completely unable to determine → default to `Sufficient`.

**Fields**: `node_original_name` = original English text; `node_name` = choose 1 from 3; `node_description` = describe the specific sample size and judgment basis.

---

### Node 13: Noise Level

**Definition**: Whether the paper treats noise as a research challenge.

**node_name Choose 1 from 2**: `High Noise` | `Normal`

| Judgment | Condition |
|------|------|
| `High Noise` | The authors mention noise, disturbance, etc. when describing data / signals |
| `Normal` | The authors do not explicitly mention noise, disturbance, etc. when describing data / signals |

⚠️ Only when the paper explicitly mentions that the data / signals in this paper's own method involve noise, disturbance, etc., it counts as high noise; if noise is mentioned in non-this-paper methods, it does not belong to high noise.

**Fields**: `node_original_name` = original English text; `node_name` = choose 1 from 2; `node_description` = describe the noise level information.

---

### Node 14: Computational Resource

**Definition**: Whether the paper treats computational efficiency / resource consumption as a research dimension.

**node_name Choose 1 from 3**: `Low Resource Consumption` | `Not Mentioned` | `High Resource Consumption`

| Judgment | Condition |
|------|------|
| `Low Resource Consumption` | Explicitly mentions lightweight / online deployment / embedded / comparison of parameter count FLOPs |
| `High Resource Consumption` | Explicitly mentions high computational resource consumption / high complexity |
| `Not Mentioned` | Not explicitly mentioned |

**Fields**: `node_original_name` = original English text; `node_name` = choose 1 from 3; `node_description` = describe the specific resource consumption.

---

## [Mandatory Constraints]

1. `node_name` must be filled in with **standard English options**; English original text or non-standard variants are prohibited
2. 12/13/14 each have **1 node**; 10/11 may have multiple
3. **Extract only those involved in the paper's own experiments**, ignoring Introduction / Baseline
4. When `node_description` is not null, fill in an English description
