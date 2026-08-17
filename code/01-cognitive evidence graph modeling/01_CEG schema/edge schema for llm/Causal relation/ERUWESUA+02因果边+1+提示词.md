# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：ERUWESUA
- **Paper Title**：Fault tolerant system based on non-integers order observers: Application in a heat exchanger
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `ERUWESUA`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "ERUWESUA_E036", "edge_description": "double pipe countercurrent heat exchanger contains Tco temperature sensor"},
    {"edge_id": "ERUWESUA_E037", "edge_description": "double pipe countercurrent heat exchanger contains Tho temperature sensor"},
    {"edge_id": "ERUWESUA_E039", "edge_description": "partial fault contains No Compound Fault"},
    {"edge_id": "ERUWESUA_E040", "edge_description": "total fault contains No Compound Fault"},
    {"edge_id": "ERUWESUA_E041", "edge_description": "RTD Pt-100 temperature sensors is collected on Tco temperature sensor"},
    {"edge_id": "ERUWESUA_E042", "edge_description": "RTD Pt-100 temperature sensors is collected on Tho temperature sensor"},
    {"edge_id": "ERUWESUA_E043", "edge_description": "analogical flowmeters is collected on Tco temperature sensor"},
    {"edge_id": "ERUWESUA_E044", "edge_description": "analogical flowmeters is collected on Tho temperature sensor"},
    {"edge_id": "ERUWESUA_E045", "edge_description": "RTD Pt-100 temperature sensors can obviously reflect partial fault"},
    {"edge_id": "ERUWESUA_E046", "edge_description": "RTD Pt-100 temperature sensors can obviously reflect total fault"},
    {"edge_id": "ERUWESUA_E047", "edge_description": "analogical flowmeters can obviously reflect partial fault"},
    {"edge_id": "ERUWESUA_E048", "edge_description": "analogical flowmeters can obviously reflect total fault"},
    {"edge_id": "ERUWESUA_E050", "edge_description": "Tco temperature sensor has_fault_mode partial fault"},
    {"edge_id": "ERUWESUA_E051", "edge_description": "Tco temperature sensor has_fault_mode total fault"},
    {"edge_id": "ERUWESUA_E052", "edge_description": "Tho temperature sensor has_fault_mode partial fault"},
    {"edge_id": "ERUWESUA_E053", "edge_description": "Tho temperature sensor has_fault_mode total fault"},
    {"edge_id": "ERUWESUA_E054", "edge_description": "partial fault contains partial fault, total fault"},
    {"edge_id": "ERUWESUA_E055", "edge_description": "total fault contains partial fault, total fault"},
    {"edge_id": "ERUWESUA_E057", "edge_description": "Tco temperature sensor contains_phm_task fault diagnosis and isolation"},
    {"edge_id": "ERUWESUA_E058", "edge_description": "Tho temperature sensor contains_phm_task fault diagnosis and isolation"},
    {"edge_id": "ERUWESUA_E059", "edge_description": "partial fault contains_phm_task fault diagnosis and isolation"},
    {"edge_id": "ERUWESUA_E060", "edge_description": "total fault contains_phm_task fault diagnosis and isolation"},
    {"edge_id": "ERUWESUA_E062", "edge_description": "double pipe countercurrent heat exchanger induces_problem parametric uncertainties and measurement noise"},
    {"edge_id": "ERUWESUA_E063", "edge_description": "single operating condition induces_problem parametric uncertainties and measurement noise"},
    {"edge_id": "ERUWESUA_E064", "edge_description": "partial fault, total fault induces_problem parametric uncertainties and measurement noise"},
    {"edge_id": "ERUWESUA_E065", "edge_description": "No Compound Fault induces_problem parametric uncertainties and measurement noise"},
    {"edge_id": "ERUWESUA_E066", "edge_description": "fault diagnosis and isolation induces_problem parametric uncertainties and measurement noise"},
    {"edge_id": "ERUWESUA_E067", "edge_description": "Sufficient induces_problem parametric uncertainties and measurement noise"},
    {"edge_id": "ERUWESUA_E068", "edge_description": "measurement noise of ± 0.3 °C induces_problem parametric uncertainties and measurement noise"},
    {"edge_id": "ERUWESUA_E069", "edge_description": "Intel Core i7, 2.6 GHz processor, 16.0-GB RAM induces_problem parametric uncertainties and measurement noise"}
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
| 1 | `ERUWESUA_E036` | `contains` | 02-Object Type | double pipe countercurrent heat exchanger |  | 04-Fault Location | Tco temperature sensor |  |
| 2 | `ERUWESUA_E037` | `contains` | 02-Object Type | double pipe countercurrent heat exchanger |  | 04-Fault Location | Tho temperature sensor |  |
| 3 | `ERUWESUA_E039` | `contains` | 05-Fault Mode | partial fault |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `ERUWESUA_E040` | `contains` | 05-Fault Mode | total fault |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `ERUWESUA_E041` | `is collected on` | 11-Sensor Information | RTD Pt-100 temperature sensors |  | 04-Fault Location | Tco temperature sensor |  |
| 6 | `ERUWESUA_E042` | `is collected on` | 11-Sensor Information | RTD Pt-100 temperature sensors |  | 04-Fault Location | Tho temperature sensor |  |
| 7 | `ERUWESUA_E043` | `is collected on` | 11-Sensor Information | analogical flowmeters |  | 04-Fault Location | Tco temperature sensor |  |
| 8 | `ERUWESUA_E044` | `is collected on` | 11-Sensor Information | analogical flowmeters |  | 04-Fault Location | Tho temperature sensor |  |
| 9 | `ERUWESUA_E045` | `can obviously reflect` | 11-Sensor Information | RTD Pt-100 temperature sensors |  | 05-Fault Mode | partial fault |  |
| 10 | `ERUWESUA_E046` | `can obviously reflect` | 11-Sensor Information | RTD Pt-100 temperature sensors |  | 05-Fault Mode | total fault |  |
| 11 | `ERUWESUA_E047` | `can obviously reflect` | 11-Sensor Information | analogical flowmeters |  | 05-Fault Mode | partial fault |  |
| 12 | `ERUWESUA_E048` | `can obviously reflect` | 11-Sensor Information | analogical flowmeters |  | 05-Fault Mode | total fault |  |
| 13 | `ERUWESUA_E050` | `has_fault_mode` | 04-Fault Location | Tco temperature sensor |  | 05-Fault Mode | partial fault |  |
| 14 | `ERUWESUA_E051` | `has_fault_mode` | 04-Fault Location | Tco temperature sensor |  | 05-Fault Mode | total fault |  |
| 15 | `ERUWESUA_E052` | `has_fault_mode` | 04-Fault Location | Tho temperature sensor |  | 05-Fault Mode | partial fault |  |
| 16 | `ERUWESUA_E053` | `has_fault_mode` | 04-Fault Location | Tho temperature sensor |  | 05-Fault Mode | total fault |  |
| 17 | `ERUWESUA_E054` | `contains` | 05-Fault Mode | partial fault |  | 06-Fault Severity | partial fault, total fault(Multiple Severities) |  |
| 18 | `ERUWESUA_E055` | `contains` | 05-Fault Mode | total fault |  | 06-Fault Severity | partial fault, total fault(Multiple Severities) |  |
| 19 | `ERUWESUA_E057` | `contains_phm_task` | 04-Fault Location | Tco temperature sensor |  | 08-PHM Task | fault diagnosis and isolation(Diagnosis Task) |  |
| 20 | `ERUWESUA_E058` | `contains_phm_task` | 04-Fault Location | Tho temperature sensor |  | 08-PHM Task | fault diagnosis and isolation(Diagnosis Task) |  |
| 21 | `ERUWESUA_E059` | `contains_phm_task` | 05-Fault Mode | partial fault |  | 08-PHM Task | fault diagnosis and isolation(Diagnosis Task) |  |
| 22 | `ERUWESUA_E060` | `contains_phm_task` | 05-Fault Mode | total fault |  | 08-PHM Task | fault diagnosis and isolation(Diagnosis Task) |  |
| 23 | `ERUWESUA_E062` | `induces_problem` | 02-Object Type | double pipe countercurrent heat exchanger |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |
| 24 | `ERUWESUA_E063` | `induces_problem` | 03-Operating Conditions | single operating condition(Single Condition) |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |
| 25 | `ERUWESUA_E064` | `induces_problem` | 06-Fault Severity | partial fault, total fault(Multiple Severities) |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |
| 26 | `ERUWESUA_E065` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |
| 27 | `ERUWESUA_E066` | `induces_problem` | 08-PHM Task | fault diagnosis and isolation(Diagnosis Task) |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |
| 28 | `ERUWESUA_E067` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |
| 29 | `ERUWESUA_E068` | `induces_problem` | 13-Noise Level | measurement noise of ± 0.3 °C(High Noise) |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |
| 30 | `ERUWESUA_E069` | `induces_problem` | 14-Computational Resource | Intel Core i7, 2.6 GHz processor, 16.0-GB RAM |  | 09-Problem Scenario | parametric uncertainties and measurement noise(Uncertainty) |  |

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
