# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：JJEU5RDV
- **Paper Title**：Online Fault Diagnosis Method Based on Transfer Convolutional Neural Networks
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `JJEU5RDV`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "JJEU5RDV_E081", "edge_description": "industrial equipment contains bearing"},
    {"edge_id": "JJEU5RDV_E082", "edge_description": "industrial equipment contains centrifugal pump"},
    {"edge_id": "JJEU5RDV_E083", "edge_description": "bearing contains bearing"},
    {"edge_id": "JJEU5RDV_E084", "edge_description": "bearing contains impeller"},
    {"edge_id": "JJEU5RDV_E085", "edge_description": "centrifugal pump contains bearing"},
    {"edge_id": "JJEU5RDV_E086", "edge_description": "centrifugal pump contains impeller"},
    {"edge_id": "JJEU5RDV_E087", "edge_description": "bearing contains different operating conditions / loads range from 0 to 3"},
    {"edge_id": "JJEU5RDV_E088", "edge_description": "centrifugal pump contains different operating conditions / loads range from 0 to 3"},
    {"edge_id": "JJEU5RDV_E089", "edge_description": "defect contains No Compound Fault"},
    {"edge_id": "JJEU5RDV_E090", "edge_description": "wearing contains No Compound Fault"},
    {"edge_id": "JJEU5RDV_E091", "edge_description": "accelerometers is collected on bearing"},
    {"edge_id": "JJEU5RDV_E092", "edge_description": "accelerometers is collected on impeller"},
    {"edge_id": "JJEU5RDV_E093", "edge_description": "accelerometers can obviously reflect defect"},
    {"edge_id": "JJEU5RDV_E094", "edge_description": "accelerometers can obviously reflect wearing"},
    {"edge_id": "JJEU5RDV_E095", "edge_description": "CWRU Bearing Data Center can be used for online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E096", "edge_description": "BaoSteel MRO Management System can be used for online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E097", "edge_description": "self-priming centrifugal pump fault data set can be used for online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E098", "edge_description": "bearing has_fault_mode defect"},
    {"edge_id": "JJEU5RDV_E099", "edge_description": "bearing has_fault_mode wearing"},
    {"edge_id": "JJEU5RDV_E100", "edge_description": "impeller has_fault_mode defect"},
    {"edge_id": "JJEU5RDV_E101", "edge_description": "impeller has_fault_mode wearing"},
    {"edge_id": "JJEU5RDV_E102", "edge_description": "defect contains damage sizes (0.18, 0.36, and 0.54 mm)"},
    {"edge_id": "JJEU5RDV_E103", "edge_description": "wearing contains damage sizes (0.18, 0.36, and 0.54 mm)"},
    {"edge_id": "JJEU5RDV_E104", "edge_description": "bearing contains_phm_task online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E105", "edge_description": "centrifugal pump contains_phm_task online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E106", "edge_description": "bearing contains_phm_task online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E107", "edge_description": "impeller contains_phm_task online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E108", "edge_description": "defect contains_phm_task online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E109", "edge_description": "wearing contains_phm_task online fault diagnosis"},
    {"edge_id": "JJEU5RDV_E111", "edge_description": "bearing induces_problem feature distribution of a training data set is the same as that of a test data set, which is unrealistic in practical industrial applications"}
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
| 1 | `JJEU5RDV_E081` | `contains` | 01-Object Domain | industrial equipment(Industrial) |  | 02-Object Type | bearing |  |
| 2 | `JJEU5RDV_E082` | `contains` | 01-Object Domain | industrial equipment(Industrial) |  | 02-Object Type | centrifugal pump |  |
| 3 | `JJEU5RDV_E083` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing |  |
| 4 | `JJEU5RDV_E084` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | impeller |  |
| 5 | `JJEU5RDV_E085` | `contains` | 02-Object Type | centrifugal pump |  | 04-Fault Location | bearing |  |
| 6 | `JJEU5RDV_E086` | `contains` | 02-Object Type | centrifugal pump |  | 04-Fault Location | impeller |  |
| 7 | `JJEU5RDV_E087` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | different operating conditions / loads range from 0 to 3(Multiple Conditions) |  |
| 8 | `JJEU5RDV_E088` | `contains` | 02-Object Type | centrifugal pump |  | 03-Operating Conditions | different operating conditions / loads range from 0 to 3(Multiple Conditions) |  |
| 9 | `JJEU5RDV_E089` | `contains` | 05-Fault Mode | defect |  | 07-Compound Fault | No Compound Fault |  |
| 10 | `JJEU5RDV_E090` | `contains` | 05-Fault Mode | wearing |  | 07-Compound Fault | No Compound Fault |  |
| 11 | `JJEU5RDV_E091` | `is collected on` | 11-Sensor Information | accelerometers |  | 04-Fault Location | bearing |  |
| 12 | `JJEU5RDV_E092` | `is collected on` | 11-Sensor Information | accelerometers |  | 04-Fault Location | impeller |  |
| 13 | `JJEU5RDV_E093` | `can obviously reflect` | 11-Sensor Information | accelerometers |  | 05-Fault Mode | defect |  |
| 14 | `JJEU5RDV_E094` | `can obviously reflect` | 11-Sensor Information | accelerometers |  | 05-Fault Mode | wearing |  |
| 15 | `JJEU5RDV_E095` | `can be used for` | 10-Dataset | CWRU Bearing Data Center |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 16 | `JJEU5RDV_E096` | `can be used for` | 10-Dataset | BaoSteel MRO Management System |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 17 | `JJEU5RDV_E097` | `can be used for` | 10-Dataset | self-priming centrifugal pump fault data set |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 18 | `JJEU5RDV_E098` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | defect |  |
| 19 | `JJEU5RDV_E099` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | wearing |  |
| 20 | `JJEU5RDV_E100` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | defect |  |
| 21 | `JJEU5RDV_E101` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | wearing |  |
| 22 | `JJEU5RDV_E102` | `contains` | 05-Fault Mode | defect |  | 06-Fault Severity | damage sizes (0.18, 0.36, and 0.54 mm)(Multiple Severities) |  |
| 23 | `JJEU5RDV_E103` | `contains` | 05-Fault Mode | wearing |  | 06-Fault Severity | damage sizes (0.18, 0.36, and 0.54 mm)(Multiple Severities) |  |
| 24 | `JJEU5RDV_E104` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 25 | `JJEU5RDV_E105` | `contains_phm_task` | 02-Object Type | centrifugal pump |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 26 | `JJEU5RDV_E106` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 27 | `JJEU5RDV_E107` | `contains_phm_task` | 04-Fault Location | impeller |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 28 | `JJEU5RDV_E108` | `contains_phm_task` | 05-Fault Mode | defect |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 29 | `JJEU5RDV_E109` | `contains_phm_task` | 05-Fault Mode | wearing |  | 08-PHM Task | online fault diagnosis(Diagnosis Task) |  |
| 30 | `JJEU5RDV_E111` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | feature distribution of a training data set is the same as that of a test data set, which is unrealistic in practical industrial applications(Distribution Discrepancy) |  |

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
