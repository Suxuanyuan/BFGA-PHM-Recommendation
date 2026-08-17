# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：6DFYQGDQ
- **Paper Title**：Refined composite multivariate multiscale symbolic dynamic entropy and its application to fault diagnosis of rotating machine
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `6DFYQGDQ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "6DFYQGDQ_E109", "edge_description": "flow sensor can obviously reflect crack"},
    {"edge_id": "6DFYQGDQ_E110", "edge_description": "flow sensor can obviously reflect corrosive pitting"},
    {"edge_id": "6DFYQGDQ_E111", "edge_description": "flow sensor can obviously reflect damage"},
    {"edge_id": "6DFYQGDQ_E112", "edge_description": "flow sensor can obviously reflect defect"},
    {"edge_id": "6DFYQGDQ_E113", "edge_description": "oil temperature sensor can obviously reflect crack"},
    {"edge_id": "6DFYQGDQ_E114", "edge_description": "oil temperature sensor can obviously reflect corrosive pitting"},
    {"edge_id": "6DFYQGDQ_E115", "edge_description": "oil temperature sensor can obviously reflect damage"},
    {"edge_id": "6DFYQGDQ_E116", "edge_description": "oil temperature sensor can obviously reflect defect"},
    {"edge_id": "6DFYQGDQ_E117", "edge_description": "incremental encoder can obviously reflect crack"},
    {"edge_id": "6DFYQGDQ_E118", "edge_description": "incremental encoder can obviously reflect corrosive pitting"},
    {"edge_id": "6DFYQGDQ_E119", "edge_description": "incremental encoder can obviously reflect damage"},
    {"edge_id": "6DFYQGDQ_E120", "edge_description": "incremental encoder can obviously reflect defect"},
    {"edge_id": "6DFYQGDQ_E121", "edge_description": "centrifugal pump dataset can be used for fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E122", "edge_description": "bearing dataset under time-varying speed conditions can be used for fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E123", "edge_description": "ball bearing has_fault_mode crack"},
    {"edge_id": "6DFYQGDQ_E124", "edge_description": "ball bearing has_fault_mode corrosive pitting"},
    {"edge_id": "6DFYQGDQ_E125", "edge_description": "ball bearing has_fault_mode damage"},
    {"edge_id": "6DFYQGDQ_E126", "edge_description": "ball bearing has_fault_mode defect"},
    {"edge_id": "6DFYQGDQ_E127", "edge_description": "impeller has_fault_mode crack"},
    {"edge_id": "6DFYQGDQ_E128", "edge_description": "impeller has_fault_mode corrosive pitting"},
    {"edge_id": "6DFYQGDQ_E129", "edge_description": "impeller has_fault_mode damage"},
    {"edge_id": "6DFYQGDQ_E130", "edge_description": "impeller has_fault_mode defect"},
    {"edge_id": "6DFYQGDQ_E131", "edge_description": "crack contains fault size less than 0.5mm, fault size of 2*3mm2"},
    {"edge_id": "6DFYQGDQ_E132", "edge_description": "corrosive pitting contains fault size less than 0.5mm, fault size of 2*3mm2"},
    {"edge_id": "6DFYQGDQ_E133", "edge_description": "damage contains fault size less than 0.5mm, fault size of 2*3mm2"},
    {"edge_id": "6DFYQGDQ_E134", "edge_description": "defect contains fault size less than 0.5mm, fault size of 2*3mm2"},
    {"edge_id": "6DFYQGDQ_E135", "edge_description": "centrifugal pump contains_phm_task fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E136", "edge_description": "ball bearing contains_phm_task fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E137", "edge_description": "ball bearing contains_phm_task fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E138", "edge_description": "impeller contains_phm_task fault diagnosis"}
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
| 1 | `6DFYQGDQ_E109` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | crack |  |
| 2 | `6DFYQGDQ_E110` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | corrosive pitting |  |
| 3 | `6DFYQGDQ_E111` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | damage |  |
| 4 | `6DFYQGDQ_E112` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | defect |  |
| 5 | `6DFYQGDQ_E113` | `can obviously reflect` | 11-Sensor Information | oil temperature sensor |  | 05-Fault Mode | crack |  |
| 6 | `6DFYQGDQ_E114` | `can obviously reflect` | 11-Sensor Information | oil temperature sensor |  | 05-Fault Mode | corrosive pitting |  |
| 7 | `6DFYQGDQ_E115` | `can obviously reflect` | 11-Sensor Information | oil temperature sensor |  | 05-Fault Mode | damage |  |
| 8 | `6DFYQGDQ_E116` | `can obviously reflect` | 11-Sensor Information | oil temperature sensor |  | 05-Fault Mode | defect |  |
| 9 | `6DFYQGDQ_E117` | `can obviously reflect` | 11-Sensor Information | incremental encoder |  | 05-Fault Mode | crack |  |
| 10 | `6DFYQGDQ_E118` | `can obviously reflect` | 11-Sensor Information | incremental encoder |  | 05-Fault Mode | corrosive pitting |  |
| 11 | `6DFYQGDQ_E119` | `can obviously reflect` | 11-Sensor Information | incremental encoder |  | 05-Fault Mode | damage |  |
| 12 | `6DFYQGDQ_E120` | `can obviously reflect` | 11-Sensor Information | incremental encoder |  | 05-Fault Mode | defect |  |
| 13 | `6DFYQGDQ_E121` | `can be used for` | 10-Dataset | centrifugal pump dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `6DFYQGDQ_E122` | `can be used for` | 10-Dataset | bearing dataset under time-varying speed conditions |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `6DFYQGDQ_E123` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | crack |  |
| 16 | `6DFYQGDQ_E124` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | corrosive pitting |  |
| 17 | `6DFYQGDQ_E125` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | damage |  |
| 18 | `6DFYQGDQ_E126` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | defect |  |
| 19 | `6DFYQGDQ_E127` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | crack |  |
| 20 | `6DFYQGDQ_E128` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | corrosive pitting |  |
| 21 | `6DFYQGDQ_E129` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | damage |  |
| 22 | `6DFYQGDQ_E130` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | defect |  |
| 23 | `6DFYQGDQ_E131` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | fault size less than 0.5mm, fault size of 2*3mm2(Single Severity) |  |
| 24 | `6DFYQGDQ_E132` | `contains` | 05-Fault Mode | corrosive pitting |  | 06-Fault Severity | fault size less than 0.5mm, fault size of 2*3mm2(Single Severity) |  |
| 25 | `6DFYQGDQ_E133` | `contains` | 05-Fault Mode | damage |  | 06-Fault Severity | fault size less than 0.5mm, fault size of 2*3mm2(Single Severity) |  |
| 26 | `6DFYQGDQ_E134` | `contains` | 05-Fault Mode | defect |  | 06-Fault Severity | fault size less than 0.5mm, fault size of 2*3mm2(Single Severity) |  |
| 27 | `6DFYQGDQ_E135` | `contains_phm_task` | 02-Object Type | centrifugal pump |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 28 | `6DFYQGDQ_E136` | `contains_phm_task` | 02-Object Type | ball bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 29 | `6DFYQGDQ_E137` | `contains_phm_task` | 04-Fault Location | ball bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 30 | `6DFYQGDQ_E138` | `contains_phm_task` | 04-Fault Location | impeller |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
