# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：U8MIA6IP
- **Paper Title**：Spectral negentropy based sidebands and demodulation analysis for planet bearing fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `U8MIA6IP`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "U8AGEI3J_E077", "edge_description": "odometers is collected on wheel"},
    {"edge_id": "U8AGEI3J_E078", "edge_description": "Inertial Measurement Unit (IMU) is collected on wheel"},
    {"edge_id": "U8AGEI3J_E079", "edge_description": "GPS is collected on wheel"},
    {"edge_id": "U8AGEI3J_E080", "edge_description": "odometers can obviously reflect wheel block"},
    {"edge_id": "U8AGEI3J_E081", "edge_description": "Inertial Measurement Unit (IMU) can obviously reflect wheel block"},
    {"edge_id": "U8AGEI3J_E082", "edge_description": "GPS can obviously reflect wheel block"},
    {"edge_id": "U8AGEI3J_E083", "edge_description": "Gazebo simulation data can be used for Fault Detection and Isolation (FDI)"},
    {"edge_id": "U8AGEI3J_E084", "edge_description": "Real robot experimental data can be used for Fault Detection and Isolation (FDI)"},
    {"edge_id": "U8AGEI3J_E091", "edge_description": "wheeled mobile robot induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E092", "edge_description": "wheeled mobile robot induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8AGEI3J_E093", "edge_description": "low-speed controls and high-speed controls induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E094", "edge_description": "low-speed controls and high-speed controls induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8AGEI3J_E095", "edge_description": "permitted rotation angle of a wheel to 0 induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E096", "edge_description": "permitted rotation angle of a wheel to 0 induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8AGEI3J_E097", "edge_description": "No Compound Fault induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E098", "edge_description": "No Compound Fault induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8AGEI3J_E099", "edge_description": "Fault Detection and Isolation (FDI) induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E100", "edge_description": "Fault Detection and Isolation (FDI) induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8AGEI3J_E101", "edge_description": "approximately 6000 points for each mode induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E102", "edge_description": "approximately 6000 points for each mode induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8AGEI3J_E103", "edge_description": "additive centered Gaussian noise (sigma = 0.005) induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E104", "edge_description": "additive centered Gaussian noise (sigma = 0.005) induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8AGEI3J_E105", "edge_description": "Computational Time Per Cycle (TPC) induces_problem noise robustness and false alarms"},
    {"edge_id": "U8AGEI3J_E106", "edge_description": "Computational Time Per Cycle (TPC) induces_problem computational complexity and real-time constraints of PF"},
    {"edge_id": "U8HVITYL_E056", "edge_description": "rolling bearing induces_problem difference among feature distribution of the measured signals under different speed conditions"},
    {"edge_id": "U8HVITYL_E057", "edge_description": "four different speed conditions (1725/1750/1772/1796 rpm) induces_problem difference among feature distribution of the measured signals under different speed conditions"},
    {"edge_id": "U8HVITYL_E058", "edge_description": "0.007, 0.014, 0.021 inches induces_problem difference among feature distribution of the measured signals under different speed conditions"},
    {"edge_id": "U8HVITYL_E059", "edge_description": "No Compound Fault induces_problem difference among feature distribution of the measured signals under different speed conditions"},
    {"edge_id": "U8HVITYL_E060", "edge_description": "fault classification induces_problem difference among feature distribution of the measured signals under different speed conditions"},
    {"edge_id": "U8HVITYL_E061", "edge_description": "For each health conditions under different speed, 100 samples (60 for training and 40 for testing) were built induces_problem difference among feature distribution of the measured signals under different speed conditions"}
]
```

### 3.2 Field Description

| Field | Description | Data Type |
|------|------|---------|
| `edge_id` | Unique identifier of the candidate edge, obtained from the candidate edge list below | String, must be exactly the same as the input |
| `edge_description` | Description text of the edge, formatted as: `<source_node> <edge_type> <target_node>` | String, format fixed as "Node A relation type Node B" |

### 3.3 Mandatory Constraints

1. **`edge_id` must be a string**, and its value must be exactly the same as the `edge_id` in the input candidate edge list; do not generate or modify it yourself.
2. **`edge_description` must be a string**, with the format fixed as `"<source_node> <edge_type> <target_node>"` (each part separated by a space); do not add, delete or modify any characters.
3. **Only output candidate edges judged as "existing"**; if a candidate edge is judged as not existing, **skip it directly and do not write it anywhere in the JSON array**.
4. The number of records in the final output JSON array may be less than the total number of edges to be judged; this is normal behavior.
5. If all candidate edges are judged as not existing, output the empty array `[]`.

---

## IV. Instructions for the LLM to Execute

Please judge each candidate edge in the table below:

| No. | edge_id | edge_type | source_type | source_node | source_description | target_type | target_node | target_description |
|------|---------|-----------|------------|------------|------------------|------------|------------|-------------------|
| 1 | `U8AGEI3J_E077` | `is collected on` | 11-Sensor Information | odometers |  | 04-Fault Location | wheel |  |
| 2 | `U8AGEI3J_E078` | `is collected on` | 11-Sensor Information | Inertial Measurement Unit (IMU) |  | 04-Fault Location | wheel |  |
| 3 | `U8AGEI3J_E079` | `is collected on` | 11-Sensor Information | GPS |  | 04-Fault Location | wheel |  |
| 4 | `U8AGEI3J_E080` | `can obviously reflect` | 11-Sensor Information | odometers |  | 05-Fault Mode | wheel block |  |
| 5 | `U8AGEI3J_E081` | `can obviously reflect` | 11-Sensor Information | Inertial Measurement Unit (IMU) |  | 05-Fault Mode | wheel block |  |
| 6 | `U8AGEI3J_E082` | `can obviously reflect` | 11-Sensor Information | GPS |  | 05-Fault Mode | wheel block |  |
| 7 | `U8AGEI3J_E083` | `can be used for` | 10-Dataset | Gazebo simulation data |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 8 | `U8AGEI3J_E084` | `can be used for` | 10-Dataset | Real robot experimental data |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 9 | `U8AGEI3J_E091` | `induces_problem` | 02-Object Type | wheeled mobile robot |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 10 | `U8AGEI3J_E092` | `induces_problem` | 02-Object Type | wheeled mobile robot |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 11 | `U8AGEI3J_E093` | `induces_problem` | 03-Operating Conditions | low-speed controls and high-speed controls(Multiple Conditions) |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 12 | `U8AGEI3J_E094` | `induces_problem` | 03-Operating Conditions | low-speed controls and high-speed controls(Multiple Conditions) |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 13 | `U8AGEI3J_E095` | `induces_problem` | 06-Fault Severity | permitted rotation angle of a wheel to 0(Single Severity) |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 14 | `U8AGEI3J_E096` | `induces_problem` | 06-Fault Severity | permitted rotation angle of a wheel to 0(Single Severity) |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 15 | `U8AGEI3J_E097` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 16 | `U8AGEI3J_E098` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 17 | `U8AGEI3J_E099` | `induces_problem` | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 18 | `U8AGEI3J_E100` | `induces_problem` | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 19 | `U8AGEI3J_E101` | `induces_problem` | 12-Training Data Availability | approximately 6000 points for each mode(Sufficient) |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 20 | `U8AGEI3J_E102` | `induces_problem` | 12-Training Data Availability | approximately 6000 points for each mode(Sufficient) |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 21 | `U8AGEI3J_E103` | `induces_problem` | 13-Noise Level | additive centered Gaussian noise (sigma = 0.005)(High Noise) |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 22 | `U8AGEI3J_E104` | `induces_problem` | 13-Noise Level | additive centered Gaussian noise (sigma = 0.005)(High Noise) |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 23 | `U8AGEI3J_E105` | `induces_problem` | 14-Computational Resource | Computational Time Per Cycle (TPC)(Low Resource Consumption) |  | 09-Problem Scenario | noise robustness and false alarms(Uncertainty) |  |
| 24 | `U8AGEI3J_E106` | `induces_problem` | 14-Computational Resource | Computational Time Per Cycle (TPC)(Low Resource Consumption) |  | 09-Problem Scenario | computational complexity and real-time constraints of PF(Other) |  |
| 25 | `U8HVITYL_E056` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) |  |
| 26 | `U8HVITYL_E057` | `induces_problem` | 03-Operating Conditions | four different speed conditions (1725/1750/1772/1796 rpm)(Multiple Conditions) |  | 09-Problem Scenario | difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) |  |
| 27 | `U8HVITYL_E058` | `induces_problem` | 06-Fault Severity | 0.007, 0.014, 0.021 inches(Multiple Severities) |  | 09-Problem Scenario | difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) |  |
| 28 | `U8HVITYL_E059` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) |  |
| 29 | `U8HVITYL_E060` | `induces_problem` | 08-PHM Task | fault classification(Diagnosis Task) |  | 09-Problem Scenario | difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) |  |
| 30 | `U8HVITYL_E061` | `induces_problem` | 12-Training Data Availability | For each health conditions under different speed, 100 samples (60 for training and 40 for testing) were built(Sufficient) |  | 09-Problem Scenario | difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) |  |

> **Auxiliary Note**: When judging candidate edges, the information in each column of the table should be used comprehensively — `source_node` / `target_node` are node names; `source_description` / `target_description` are the original text descriptions extracted from the paper (highly valuable reference); `edge_type` is the relation semantics. **Prioritize using node names, and make a comprehensive judgment combining the original text descriptions and the edge_type semantics**.

### 4.1 Judgment Criteria for `induces_problem` Candidate Edges

Judge one by one **whether there exists a causal relation between source_node and target_node as described by `induces_problem`**.

When judging, the information in each column of the table should be used comprehensively:
- **source_node / target_node**: Node names; prioritize using the original names as the judgment basis
- **source_description / target_description**: The original text descriptions when extracting these nodes from the paper, providing context for judging causal relations
- **edge_type**: The semantics of `induces_problem` is "source causes/induces the target problem scenario"

**General Principle**: Encourage retaining but do not retain incorrect candidate edges. Specifically:
- **Retainable**: The paper **directly mentions** this causal relation; or although not directly mentioned, it is **very likely to indirectly exist** when combining context/domain knowledge
- **Not Retainable**: The paper **does not mention it at all**, and it is **impossible to indirectly infer** this causal relation from the text content or domain knowledge

**Judgment Method**: Requires full-text understanding, considering the following aspects:
- Whether the paper implies, when describing problem scenarios or method design, that source (operating conditions / fault severity / compound fault / PHM task / data amount / noise / computational resource) causes or exacerbates the occurrence of target (problem scenario)
- Whether the authors implicitly include this causal logic in their experimental motivation or analysis
- Even if the paper does not use words like `induces`, as long as there is room for causal inference in the context, it can be retained

**Trap to Watch Out For**: Merely because source and target each appear in the paper does not mean the `induces_problem` relation exists — there must be a causal chain between them.

### 4.2 Judgment Criteria for Other edge_type Candidate Edges

Judge one by one whether there exists a causal relation between source_node and target_node as described by `edge_type`.

When judging, the information in each column of the table should be used comprehensively:
- **source_node / target_node**: Node names; prioritize using the original names as the judgment basis
- **source_description / target_description**: The original text descriptions when extracting these nodes from the paper, providing context for judging relations
- **edge_type**: Semantics need to be understood in the context of the full text, rather than literal retrieval

**General Principle**: The relation can only be retained if it is **directly mentioned** in the paper; "directly mentioned" means that the paper explicitly expresses that the semantic relation exists between source and target, **rather than exact string matching**.

**Judgment Basis**: Should be based on semantic understanding (full-text level), examining whether method/experiment descriptions, figure/table evidence, and author narratives support the existence of this relation.

---

## V. [Key Constraints] Strict Judgment Criteria for Specific edge_type

### ▶ For `induces_problem` (X type → 09-Problem Scenario type)

**Retention Principle**: Encourage retaining but do not retain incorrect candidate edges. Specifically:
- **Retainable**: The paper **directly mentions** that source induces/causes the target problem scenario; or although not directly mentioned, it is **very likely to indirectly exist** when combining context/domain knowledge
- **Not Retainable**: The paper **does not mention it at all**, and it is **impossible to indirectly infer** this causal relation from the text content or domain knowledge(such edges will pollute the graph and must be deleted)
**Judgment Basis**: Comprehensively understand the full text, examining whether the problem description, experimental motivation, method design, etc., imply the source→target causal logic.

### ▶ For `can obviously reflect` (Sensor Information type → Fault Mode type)

**Very High Standard**: All of the following **conditions must be met** to be judged as "existing":
1. The paper explicitly states that the sensor **collects** data of this fault mode (i.e., the sensor appears in the fault data acquisition scenario)
2. The paper explicitly states that the sensor can **directly reflect/characterize** the physical features of this fault
3. The mere appearance of the sensor and fault mode in the dataset description is **insufficient** for judgment — the sensor must play an active role in the research method
**Trap to Watch Out For**: The mere appearance of the sensor and fault mode as dataset description does not equal the existence of a causal chain
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses a sensor→fault-feature causal relation, rather than exact matching of English phrases

### ▶ For `is collected on` (Sensor Information type → Fault Location type)

**High Standard**: The paper must explicitly express that the sensor is **physically installed/arranged on** the target fault location, i.e., there is a description of the **physical positional relationship** between the sensor and the fault location.
The mere appearance in the dataset description of "a sensor used for a certain fault" is insufficient — the physical arrangement or installation context of the sensor must be reflected
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the relationship between the physical installation position of the sensor and the fault location, rather than exact matching of English phrases

### ▶ For `can be used for` (Dataset type → PHM Task type)

**High Standard**: The paper must explicitly express that the dataset is an **input at the methodological level**, rather than merely a background for experimental evaluation.
Merely mentioning "using a dataset to evaluate model performance" is insufficient — the methodological association between dataset and task must be reflected (e.g., "selecting a dataset for a specific task")
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the methodological relation of the dataset serving a certain PHM task, rather than exact matching of English phrases

---

## VI. LLM Constraints

### 6.1 Full-Text Understanding Principle

**For `induces_problem` edges**: Causal associations must be judged based on full-text understanding; encourage retaining directly mentioned and very likely indirectly existing causal relations, but relations that are completely unmentioned and cannot be inferred are not retainable.

**For other edge_type edges**: Whether the relation truly exists in the paper must be judged based on full-text understanding; please watch out for the following traps:
- The mere appearance of the English word of `edge_type` in the paper does not mean the relation exists
- It is necessary to judge in context whether the causal association of this type exists between source_node and target_node

### 6.2 Output Cleanliness Principle

- The output JSON must **not contain** any non-standard JSON content (e.g., comments, prefix descriptions, etc.)
- Each `edge_description` in the JSON array must be strictly extracted from the table above; do not rewrite it yourself

---

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
