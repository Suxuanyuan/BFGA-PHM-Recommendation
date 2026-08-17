# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WI5JAEU6
- **Paper Title**：A frequency-shifted bispectrum for rolling element bearing diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `WI5JAEU6`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WI5JAEU6_E058", "edge_description": "industrial rotary machinery contains rolling element bearing"},
    {"edge_id": "WI5JAEU6_E059", "edge_description": "industrial rotary machinery contains gearbox"},
    {"edge_id": "WI5JAEU6_E060", "edge_description": "rolling element bearing contains rolling element bearing"},
    {"edge_id": "WI5JAEU6_E061", "edge_description": "gearbox contains rolling element bearing"},
    {"edge_id": "WI5JAEU6_E062", "edge_description": "rolling element bearing contains constant operating speed"},
    {"edge_id": "WI5JAEU6_E063", "edge_description": "gearbox contains constant operating speed"},
    {"edge_id": "WI5JAEU6_E064", "edge_description": "spall contains No Compound Fault"},
    {"edge_id": "WI5JAEU6_E065", "edge_description": "slot contains No Compound Fault"},
    {"edge_id": "WI5JAEU6_E067", "edge_description": "accelerometer can obviously reflect spall"},
    {"edge_id": "WI5JAEU6_E068", "edge_description": "accelerometer can obviously reflect slot"},
    {"edge_id": "WI5JAEU6_E069", "edge_description": "Self-collected rolling element bearing experimental data can be used for rolling element bearing diagnosis"},
    {"edge_id": "WI5JAEU6_E070", "edge_description": "UNSW gearbox dataset can be used for rolling element bearing diagnosis"},
    {"edge_id": "WI5JAEU6_E071", "edge_description": "IMS bearing run-to-failure dataset can be used for rolling element bearing diagnosis"},
    {"edge_id": "WI5JAEU6_E072", "edge_description": "rolling element bearing has_fault_mode spall"},
    {"edge_id": "WI5JAEU6_E073", "edge_description": "rolling element bearing has_fault_mode slot"},
    {"edge_id": "WI5JAEU6_E074", "edge_description": "spall contains run-to-failure"},
    {"edge_id": "WI5JAEU6_E075", "edge_description": "slot contains run-to-failure"},
    {"edge_id": "WI5JAEU6_E076", "edge_description": "rolling element bearing contains_phm_task rolling element bearing diagnosis"},
    {"edge_id": "WI5JAEU6_E077", "edge_description": "gearbox contains_phm_task rolling element bearing diagnosis"},
    {"edge_id": "WI5JAEU6_E079", "edge_description": "spall contains_phm_task rolling element bearing diagnosis"},
    {"edge_id": "WI5JAEU6_E080", "edge_description": "slot contains_phm_task rolling element bearing diagnosis"},
    {"edge_id": "WI5JAEU6_E082", "edge_description": "rolling element bearing induces_problem strong environmental noise"},
    {"edge_id": "WI5JAEU6_E083", "edge_description": "rolling element bearing induces_problem early fault detection and degradation tracking"},
    {"edge_id": "WI5JAEU6_E084", "edge_description": "gearbox induces_problem strong environmental noise"},
    {"edge_id": "WI5JAEU6_E085", "edge_description": "gearbox induces_problem early fault detection and degradation tracking"},
    {"edge_id": "WI5JAEU6_E086", "edge_description": "constant operating speed induces_problem strong environmental noise"},
    {"edge_id": "WI5JAEU6_E087", "edge_description": "constant operating speed induces_problem early fault detection and degradation tracking"},
    {"edge_id": "WI5JAEU6_E088", "edge_description": "run-to-failure induces_problem strong environmental noise"},
    {"edge_id": "WI5JAEU6_E089", "edge_description": "run-to-failure induces_problem early fault detection and degradation tracking"},
    {"edge_id": "WI5JAEU6_E090", "edge_description": "No Compound Fault induces_problem strong environmental noise"}
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
| 1 | `WI5JAEU6_E058` | `contains` | 01-Object Domain | industrial rotary machinery(Industrial) |  | 02-Object Type | rolling element bearing |  |
| 2 | `WI5JAEU6_E059` | `contains` | 01-Object Domain | industrial rotary machinery(Industrial) |  | 02-Object Type | gearbox |  |
| 3 | `WI5JAEU6_E060` | `contains` | 02-Object Type | rolling element bearing |  | 04-Fault Location | rolling element bearing |  |
| 4 | `WI5JAEU6_E061` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | rolling element bearing |  |
| 5 | `WI5JAEU6_E062` | `contains` | 02-Object Type | rolling element bearing |  | 03-Operating Conditions | constant operating speed(Single Condition) |  |
| 6 | `WI5JAEU6_E063` | `contains` | 02-Object Type | gearbox |  | 03-Operating Conditions | constant operating speed(Single Condition) |  |
| 7 | `WI5JAEU6_E064` | `contains` | 05-Fault Mode | spall |  | 07-Compound Fault | No Compound Fault |  |
| 8 | `WI5JAEU6_E065` | `contains` | 05-Fault Mode | slot |  | 07-Compound Fault | No Compound Fault |  |
| 9 | `WI5JAEU6_E067` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | spall |  |
| 10 | `WI5JAEU6_E068` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | slot |  |
| 11 | `WI5JAEU6_E069` | `can be used for` | 10-Dataset | Self-collected rolling element bearing experimental data |  | 08-PHM Task | rolling element bearing diagnosis(Diagnosis Task) |  |
| 12 | `WI5JAEU6_E070` | `can be used for` | 10-Dataset | UNSW gearbox dataset |  | 08-PHM Task | rolling element bearing diagnosis(Diagnosis Task) |  |
| 13 | `WI5JAEU6_E071` | `can be used for` | 10-Dataset | IMS bearing run-to-failure dataset |  | 08-PHM Task | rolling element bearing diagnosis(Diagnosis Task) |  |
| 14 | `WI5JAEU6_E072` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | spall |  |
| 15 | `WI5JAEU6_E073` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | slot |  |
| 16 | `WI5JAEU6_E074` | `contains` | 05-Fault Mode | spall |  | 06-Fault Severity | run-to-failure(Multiple Severities) |  |
| 17 | `WI5JAEU6_E075` | `contains` | 05-Fault Mode | slot |  | 06-Fault Severity | run-to-failure(Multiple Severities) |  |
| 18 | `WI5JAEU6_E076` | `contains_phm_task` | 02-Object Type | rolling element bearing |  | 08-PHM Task | rolling element bearing diagnosis(Diagnosis Task) |  |
| 19 | `WI5JAEU6_E077` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | rolling element bearing diagnosis(Diagnosis Task) |  |
| 20 | `WI5JAEU6_E079` | `contains_phm_task` | 05-Fault Mode | spall |  | 08-PHM Task | rolling element bearing diagnosis(Diagnosis Task) |  |
| 21 | `WI5JAEU6_E080` | `contains_phm_task` | 05-Fault Mode | slot |  | 08-PHM Task | rolling element bearing diagnosis(Diagnosis Task) |  |
| 22 | `WI5JAEU6_E082` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | strong environmental noise(Uncertainty) |  |
| 23 | `WI5JAEU6_E083` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | early fault detection and degradation tracking(Early Degradation Prediction) |  |
| 24 | `WI5JAEU6_E084` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | strong environmental noise(Uncertainty) |  |
| 25 | `WI5JAEU6_E085` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | early fault detection and degradation tracking(Early Degradation Prediction) |  |
| 26 | `WI5JAEU6_E086` | `induces_problem` | 03-Operating Conditions | constant operating speed(Single Condition) |  | 09-Problem Scenario | strong environmental noise(Uncertainty) |  |
| 27 | `WI5JAEU6_E087` | `induces_problem` | 03-Operating Conditions | constant operating speed(Single Condition) |  | 09-Problem Scenario | early fault detection and degradation tracking(Early Degradation Prediction) |  |
| 28 | `WI5JAEU6_E088` | `induces_problem` | 06-Fault Severity | run-to-failure(Multiple Severities) |  | 09-Problem Scenario | strong environmental noise(Uncertainty) |  |
| 29 | `WI5JAEU6_E089` | `induces_problem` | 06-Fault Severity | run-to-failure(Multiple Severities) |  | 09-Problem Scenario | early fault detection and degradation tracking(Early Degradation Prediction) |  |
| 30 | `WI5JAEU6_E090` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | strong environmental noise(Uncertainty) |  |

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
