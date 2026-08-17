# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：GTY2C8YC
- **Paper Title**：A Current Signal-Based Adaptive Semisupervised Framework for Bearing Faults Diagnosis in Drivetrains
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `GTY2C8YC`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "GTY2C8YC_E094", "edge_description": "outer fault contains No Compound Fault"},
    {"edge_id": "GTY2C8YC_E095", "edge_description": "inner fault contains No Compound Fault"},
    {"edge_id": "GTY2C8YC_E097", "edge_description": "current sensor can obviously reflect outer fault"},
    {"edge_id": "GTY2C8YC_E098", "edge_description": "current sensor can obviously reflect inner fault"},
    {"edge_id": "GTY2C8YC_E099", "edge_description": "mechanical fault simulation (MFS) test rig can be used for bearing faults diagnosis"},
    {"edge_id": "GTY2C8YC_E100", "edge_description": "KAt-DataCenter (Paderborn University) can be used for bearing faults diagnosis"},
    {"edge_id": "GTY2C8YC_E101", "edge_description": "bearing has_fault_mode outer fault"},
    {"edge_id": "GTY2C8YC_E102", "edge_description": "bearing has_fault_mode inner fault"},
    {"edge_id": "GTY2C8YC_E103", "edge_description": "outer fault contains 2, 4, and 6 mm"},
    {"edge_id": "GTY2C8YC_E104", "edge_description": "inner fault contains 2, 4, and 6 mm"},
    {"edge_id": "GTY2C8YC_E107", "edge_description": "outer fault contains_phm_task bearing faults diagnosis"},
    {"edge_id": "GTY2C8YC_E108", "edge_description": "inner fault contains_phm_task bearing faults diagnosis"},
    {"edge_id": "GTY2C8YC_E110", "edge_description": "rolling bearing induces_problem lack data with fault labels"},
    {"edge_id": "GTY2C8YC_E111", "edge_description": "rolling bearing induces_problem only needs normal data to complete network training"},
    {"edge_id": "GTY2C8YC_E112", "edge_description": "rolling bearing induces_problem fault representations in current signals are extremely weak"},
    {"edge_id": "GTY2C8YC_E113", "edge_description": "300 and 600 rpm, constant load induces_problem lack data with fault labels"},
    {"edge_id": "GTY2C8YC_E114", "edge_description": "300 and 600 rpm, constant load induces_problem only needs normal data to complete network training"},
    {"edge_id": "GTY2C8YC_E115", "edge_description": "300 and 600 rpm, constant load induces_problem fault representations in current signals are extremely weak"},
    {"edge_id": "GTY2C8YC_E116", "edge_description": "2, 4, and 6 mm induces_problem lack data with fault labels"},
    {"edge_id": "GTY2C8YC_E117", "edge_description": "2, 4, and 6 mm induces_problem only needs normal data to complete network training"},
    {"edge_id": "GTY2C8YC_E118", "edge_description": "2, 4, and 6 mm induces_problem fault representations in current signals are extremely weak"},
    {"edge_id": "GTY2C8YC_E119", "edge_description": "No Compound Fault induces_problem lack data with fault labels"},
    {"edge_id": "GTY2C8YC_E120", "edge_description": "No Compound Fault induces_problem only needs normal data to complete network training"},
    {"edge_id": "GTY2C8YC_E121", "edge_description": "No Compound Fault induces_problem fault representations in current signals are extremely weak"},
    {"edge_id": "GTY2C8YC_E122", "edge_description": "bearing faults diagnosis induces_problem lack data with fault labels"},
    {"edge_id": "GTY2C8YC_E123", "edge_description": "bearing faults diagnosis induces_problem only needs normal data to complete network training"},
    {"edge_id": "GTY2C8YC_E124", "edge_description": "bearing faults diagnosis induces_problem fault representations in current signals are extremely weak"},
    {"edge_id": "GTY2C8YC_E125", "edge_description": "extract recognizable features from only normal current signals induces_problem lack data with fault labels"},
    {"edge_id": "GTY2C8YC_E126", "edge_description": "extract recognizable features from only normal current signals induces_problem only needs normal data to complete network training"},
    {"edge_id": "GTY2C8YC_E127", "edge_description": "extract recognizable features from only normal current signals induces_problem fault representations in current signals are extremely weak"}
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
| 1 | `GTY2C8YC_E094` | `contains` | 05-Fault Mode | outer fault |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `GTY2C8YC_E095` | `contains` | 05-Fault Mode | inner fault |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `GTY2C8YC_E097` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | outer fault |  |
| 4 | `GTY2C8YC_E098` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | inner fault |  |
| 5 | `GTY2C8YC_E099` | `can be used for` | 10-Dataset | mechanical fault simulation (MFS) test rig |  | 08-PHM Task | bearing faults diagnosis(Diagnosis Task) |  |
| 6 | `GTY2C8YC_E100` | `can be used for` | 10-Dataset | KAt-DataCenter (Paderborn University) |  | 08-PHM Task | bearing faults diagnosis(Diagnosis Task) |  |
| 7 | `GTY2C8YC_E101` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | outer fault |  |
| 8 | `GTY2C8YC_E102` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | inner fault |  |
| 9 | `GTY2C8YC_E103` | `contains` | 05-Fault Mode | outer fault |  | 06-Fault Severity | 2, 4, and 6 mm(Multiple Severities) |  |
| 10 | `GTY2C8YC_E104` | `contains` | 05-Fault Mode | inner fault |  | 06-Fault Severity | 2, 4, and 6 mm(Multiple Severities) |  |
| 11 | `GTY2C8YC_E107` | `contains_phm_task` | 05-Fault Mode | outer fault |  | 08-PHM Task | bearing faults diagnosis(Diagnosis Task) |  |
| 12 | `GTY2C8YC_E108` | `contains_phm_task` | 05-Fault Mode | inner fault |  | 08-PHM Task | bearing faults diagnosis(Diagnosis Task) |  |
| 13 | `GTY2C8YC_E110` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | lack data with fault labels(Small Fault Samples) |  |
| 14 | `GTY2C8YC_E111` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | only needs normal data to complete network training(Zero Fault Samples) |  |
| 15 | `GTY2C8YC_E112` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | fault representations in current signals are extremely weak(Uncertainty) |  |
| 16 | `GTY2C8YC_E113` | `induces_problem` | 03-Operating Conditions | 300 and 600 rpm, constant load(Multiple Conditions) |  | 09-Problem Scenario | lack data with fault labels(Small Fault Samples) |  |
| 17 | `GTY2C8YC_E114` | `induces_problem` | 03-Operating Conditions | 300 and 600 rpm, constant load(Multiple Conditions) |  | 09-Problem Scenario | only needs normal data to complete network training(Zero Fault Samples) |  |
| 18 | `GTY2C8YC_E115` | `induces_problem` | 03-Operating Conditions | 300 and 600 rpm, constant load(Multiple Conditions) |  | 09-Problem Scenario | fault representations in current signals are extremely weak(Uncertainty) |  |
| 19 | `GTY2C8YC_E116` | `induces_problem` | 06-Fault Severity | 2, 4, and 6 mm(Multiple Severities) |  | 09-Problem Scenario | lack data with fault labels(Small Fault Samples) |  |
| 20 | `GTY2C8YC_E117` | `induces_problem` | 06-Fault Severity | 2, 4, and 6 mm(Multiple Severities) |  | 09-Problem Scenario | only needs normal data to complete network training(Zero Fault Samples) |  |
| 21 | `GTY2C8YC_E118` | `induces_problem` | 06-Fault Severity | 2, 4, and 6 mm(Multiple Severities) |  | 09-Problem Scenario | fault representations in current signals are extremely weak(Uncertainty) |  |
| 22 | `GTY2C8YC_E119` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | lack data with fault labels(Small Fault Samples) |  |
| 23 | `GTY2C8YC_E120` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | only needs normal data to complete network training(Zero Fault Samples) |  |
| 24 | `GTY2C8YC_E121` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | fault representations in current signals are extremely weak(Uncertainty) |  |
| 25 | `GTY2C8YC_E122` | `induces_problem` | 08-PHM Task | bearing faults diagnosis(Diagnosis Task) |  | 09-Problem Scenario | lack data with fault labels(Small Fault Samples) |  |
| 26 | `GTY2C8YC_E123` | `induces_problem` | 08-PHM Task | bearing faults diagnosis(Diagnosis Task) |  | 09-Problem Scenario | only needs normal data to complete network training(Zero Fault Samples) |  |
| 27 | `GTY2C8YC_E124` | `induces_problem` | 08-PHM Task | bearing faults diagnosis(Diagnosis Task) |  | 09-Problem Scenario | fault representations in current signals are extremely weak(Uncertainty) |  |
| 28 | `GTY2C8YC_E125` | `induces_problem` | 12-Training Data Availability | extract recognizable features from only normal current signals(Zero-Sample) |  | 09-Problem Scenario | lack data with fault labels(Small Fault Samples) |  |
| 29 | `GTY2C8YC_E126` | `induces_problem` | 12-Training Data Availability | extract recognizable features from only normal current signals(Zero-Sample) |  | 09-Problem Scenario | only needs normal data to complete network training(Zero Fault Samples) |  |
| 30 | `GTY2C8YC_E127` | `induces_problem` | 12-Training Data Availability | extract recognizable features from only normal current signals(Zero-Sample) |  | 09-Problem Scenario | fault representations in current signals are extremely weak(Uncertainty) |  |

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
