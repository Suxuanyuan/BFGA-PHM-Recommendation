# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：8U7HYWDM
- **Paper Title**：Learning from Class-imbalanced Data with a Model-Agnostic Framework for Machine Intelligent Diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `8U7HYWDM`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "8U7HYWDM_E093", "edge_description": "Rotating machinery contains bearing"},
    {"edge_id": "8U7HYWDM_E094", "edge_description": "Rotating machinery contains gearbox"},
    {"edge_id": "8U7HYWDM_E095", "edge_description": "bearing contains bearing"},
    {"edge_id": "8U7HYWDM_E096", "edge_description": "bearing contains gear / gearbox"},
    {"edge_id": "8U7HYWDM_E097", "edge_description": "gearbox contains bearing"},
    {"edge_id": "8U7HYWDM_E098", "edge_description": "gearbox contains gear / gearbox"},
    {"edge_id": "8U7HYWDM_E099", "edge_description": "bearing contains 900 rpm rotational speed, 0.7 Nm load torque, and 1000 N radial force; 600 rpm rotational speed; 20 Hz – 0 V working condition"},
    {"edge_id": "8U7HYWDM_E100", "edge_description": "gearbox contains 900 rpm rotational speed, 0.7 Nm load torque, and 1000 N radial force; 600 rpm rotational speed; 20 Hz – 0 V working condition"},
    {"edge_id": "8U7HYWDM_E101", "edge_description": "missing tooth contains No Compound Fault"},
    {"edge_id": "8U7HYWDM_E102", "edge_description": "crack contains No Compound Fault"},
    {"edge_id": "8U7HYWDM_E103", "edge_description": "spalling contains No Compound Fault"},
    {"edge_id": "8U7HYWDM_E104", "edge_description": "chipping contains No Compound Fault"},
    {"edge_id": "8U7HYWDM_E105", "edge_description": "wear contains No Compound Fault"},
    {"edge_id": "8U7HYWDM_E106", "edge_description": "accelerometer, vibration sensor is collected on bearing"},
    {"edge_id": "8U7HYWDM_E107", "edge_description": "accelerometer, vibration sensor is collected on gear / gearbox"},
    {"edge_id": "8U7HYWDM_E108", "edge_description": "accelerometer, vibration sensor can obviously reflect missing tooth"},
    {"edge_id": "8U7HYWDM_E109", "edge_description": "accelerometer, vibration sensor can obviously reflect crack"},
    {"edge_id": "8U7HYWDM_E110", "edge_description": "accelerometer, vibration sensor can obviously reflect spalling"},
    {"edge_id": "8U7HYWDM_E111", "edge_description": "accelerometer, vibration sensor can obviously reflect chipping"},
    {"edge_id": "8U7HYWDM_E112", "edge_description": "accelerometer, vibration sensor can obviously reflect wear"},
    {"edge_id": "8U7HYWDM_E113", "edge_description": "UoC gearbox datasets can be used for fault diagnosis"},
    {"edge_id": "8U7HYWDM_E114", "edge_description": "PU bearing datasets can be used for fault diagnosis"},
    {"edge_id": "8U7HYWDM_E115", "edge_description": "JNU bearing datasets can be used for fault diagnosis"},
    {"edge_id": "8U7HYWDM_E116", "edge_description": "SEU gearbox datasets can be used for fault diagnosis"},
    {"edge_id": "8U7HYWDM_E117", "edge_description": "bearing has_fault_mode missing tooth"},
    {"edge_id": "8U7HYWDM_E118", "edge_description": "bearing has_fault_mode crack"},
    {"edge_id": "8U7HYWDM_E119", "edge_description": "bearing has_fault_mode spalling"},
    {"edge_id": "8U7HYWDM_E120", "edge_description": "bearing has_fault_mode chipping"},
    {"edge_id": "8U7HYWDM_E121", "edge_description": "bearing has_fault_mode wear"},
    {"edge_id": "8U7HYWDM_E122", "edge_description": "gear / gearbox has_fault_mode missing tooth"}
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
| 1 | `8U7HYWDM_E093` | `contains` | 01-Object Domain | Rotating machinery(Industrial) |  | 02-Object Type | bearing |  |
| 2 | `8U7HYWDM_E094` | `contains` | 01-Object Domain | Rotating machinery(Industrial) |  | 02-Object Type | gearbox |  |
| 3 | `8U7HYWDM_E095` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing |  |
| 4 | `8U7HYWDM_E096` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | gear / gearbox |  |
| 5 | `8U7HYWDM_E097` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | bearing |  |
| 6 | `8U7HYWDM_E098` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | gear / gearbox |  |
| 7 | `8U7HYWDM_E099` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | 900 rpm rotational speed, 0.7 Nm load torque, and 1000 N radial force; 600 rpm rotational speed; 20 Hz – 0 V working condition(Single Condition) |  |
| 8 | `8U7HYWDM_E100` | `contains` | 02-Object Type | gearbox |  | 03-Operating Conditions | 900 rpm rotational speed, 0.7 Nm load torque, and 1000 N radial force; 600 rpm rotational speed; 20 Hz – 0 V working condition(Single Condition) |  |
| 9 | `8U7HYWDM_E101` | `contains` | 05-Fault Mode | missing tooth |  | 07-Compound Fault | No Compound Fault |  |
| 10 | `8U7HYWDM_E102` | `contains` | 05-Fault Mode | crack |  | 07-Compound Fault | No Compound Fault |  |
| 11 | `8U7HYWDM_E103` | `contains` | 05-Fault Mode | spalling |  | 07-Compound Fault | No Compound Fault |  |
| 12 | `8U7HYWDM_E104` | `contains` | 05-Fault Mode | chipping |  | 07-Compound Fault | No Compound Fault |  |
| 13 | `8U7HYWDM_E105` | `contains` | 05-Fault Mode | wear |  | 07-Compound Fault | No Compound Fault |  |
| 14 | `8U7HYWDM_E106` | `is collected on` | 11-Sensor Information | accelerometer, vibration sensor |  | 04-Fault Location | bearing |  |
| 15 | `8U7HYWDM_E107` | `is collected on` | 11-Sensor Information | accelerometer, vibration sensor |  | 04-Fault Location | gear / gearbox |  |
| 16 | `8U7HYWDM_E108` | `can obviously reflect` | 11-Sensor Information | accelerometer, vibration sensor |  | 05-Fault Mode | missing tooth |  |
| 17 | `8U7HYWDM_E109` | `can obviously reflect` | 11-Sensor Information | accelerometer, vibration sensor |  | 05-Fault Mode | crack |  |
| 18 | `8U7HYWDM_E110` | `can obviously reflect` | 11-Sensor Information | accelerometer, vibration sensor |  | 05-Fault Mode | spalling |  |
| 19 | `8U7HYWDM_E111` | `can obviously reflect` | 11-Sensor Information | accelerometer, vibration sensor |  | 05-Fault Mode | chipping |  |
| 20 | `8U7HYWDM_E112` | `can obviously reflect` | 11-Sensor Information | accelerometer, vibration sensor |  | 05-Fault Mode | wear |  |
| 21 | `8U7HYWDM_E113` | `can be used for` | 10-Dataset | UoC gearbox datasets |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `8U7HYWDM_E114` | `can be used for` | 10-Dataset | PU bearing datasets |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 23 | `8U7HYWDM_E115` | `can be used for` | 10-Dataset | JNU bearing datasets |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 24 | `8U7HYWDM_E116` | `can be used for` | 10-Dataset | SEU gearbox datasets |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 25 | `8U7HYWDM_E117` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | missing tooth |  |
| 26 | `8U7HYWDM_E118` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | crack |  |
| 27 | `8U7HYWDM_E119` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | spalling |  |
| 28 | `8U7HYWDM_E120` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | chipping |  |
| 29 | `8U7HYWDM_E121` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | wear |  |
| 30 | `8U7HYWDM_E122` | `has_fault_mode` | 04-Fault Location | gear / gearbox |  | 05-Fault Mode | missing tooth |  |

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
