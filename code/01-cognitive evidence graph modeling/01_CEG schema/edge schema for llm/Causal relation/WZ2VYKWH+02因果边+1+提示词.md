# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WZ2VYKWH
- **Paper Title**：A modified scale-space guiding variational mode decomposition for high-speed railway bearing fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `WZ2VYKWH`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WZ2VYKWH_E056", "edge_description": "double-row tapered roller bearing contains outer race"},
    {"edge_id": "WZ2VYKWH_E057", "edge_description": "double-row tapered roller bearing contains rolling element"},
    {"edge_id": "WZ2VYKWH_E059", "edge_description": "crack contains multiple fault"},
    {"edge_id": "WZ2VYKWH_E060", "edge_description": "defect contains multiple fault"},
    {"edge_id": "WZ2VYKWH_E061", "edge_description": "accelerometer is collected on outer race"},
    {"edge_id": "WZ2VYKWH_E062", "edge_description": "accelerometer is collected on rolling element"},
    {"edge_id": "WZ2VYKWH_E063", "edge_description": "accelerometer can obviously reflect crack"},
    {"edge_id": "WZ2VYKWH_E064", "edge_description": "accelerometer can obviously reflect defect"},
    {"edge_id": "WZ2VYKWH_E065", "edge_description": "Simulated signals can be used for bearing fault diagnosis"},
    {"edge_id": "WZ2VYKWH_E066", "edge_description": "TPL bearing dataset can be used for bearing fault diagnosis"},
    {"edge_id": "WZ2VYKWH_E067", "edge_description": "outer race has_fault_mode crack"},
    {"edge_id": "WZ2VYKWH_E068", "edge_description": "outer race has_fault_mode defect"},
    {"edge_id": "WZ2VYKWH_E069", "edge_description": "rolling element has_fault_mode crack"},
    {"edge_id": "WZ2VYKWH_E070", "edge_description": "rolling element has_fault_mode defect"},
    {"edge_id": "WZ2VYKWH_E071", "edge_description": "crack contains Single Severity"},
    {"edge_id": "WZ2VYKWH_E072", "edge_description": "defect contains Single Severity"},
    {"edge_id": "WZ2VYKWH_E074", "edge_description": "outer race contains_phm_task bearing fault diagnosis"},
    {"edge_id": "WZ2VYKWH_E075", "edge_description": "rolling element contains_phm_task bearing fault diagnosis"},
    {"edge_id": "WZ2VYKWH_E076", "edge_description": "crack contains_phm_task bearing fault diagnosis"},
    {"edge_id": "WZ2VYKWH_E077", "edge_description": "defect contains_phm_task bearing fault diagnosis"},
    {"edge_id": "WZ2VYKWH_E079", "edge_description": "double-row tapered roller bearing induces_problem multiple fault"},
    {"edge_id": "WZ2VYKWH_E080", "edge_description": "double-row tapered roller bearing induces_problem adaptive determination of VMD parameters"},
    {"edge_id": "WZ2VYKWH_E081", "edge_description": "constant speed of 100 km/h induces_problem multiple fault"},
    {"edge_id": "WZ2VYKWH_E082", "edge_description": "constant speed of 100 km/h induces_problem adaptive determination of VMD parameters"},
    {"edge_id": "WZ2VYKWH_E083", "edge_description": "Single Severity induces_problem multiple fault"},
    {"edge_id": "WZ2VYKWH_E084", "edge_description": "Single Severity induces_problem adaptive determination of VMD parameters"},
    {"edge_id": "WZ2VYKWH_E085", "edge_description": "multiple fault induces_problem multiple fault"},
    {"edge_id": "WZ2VYKWH_E086", "edge_description": "multiple fault induces_problem adaptive determination of VMD parameters"},
    {"edge_id": "WZ2VYKWH_E087", "edge_description": "bearing fault diagnosis induces_problem multiple fault"},
    {"edge_id": "WZ2VYKWH_E088", "edge_description": "bearing fault diagnosis induces_problem adaptive determination of VMD parameters"}
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
| 1 | `WZ2VYKWH_E056` | `contains` | 02-Object Type | double-row tapered roller bearing |  | 04-Fault Location | outer race |  |
| 2 | `WZ2VYKWH_E057` | `contains` | 02-Object Type | double-row tapered roller bearing |  | 04-Fault Location | rolling element |  |
| 3 | `WZ2VYKWH_E059` | `contains` | 05-Fault Mode | crack |  | 07-Compound Fault | multiple fault(Compound Fault Within Same Structure) |  |
| 4 | `WZ2VYKWH_E060` | `contains` | 05-Fault Mode | defect |  | 07-Compound Fault | multiple fault(Compound Fault Within Same Structure) |  |
| 5 | `WZ2VYKWH_E061` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | outer race |  |
| 6 | `WZ2VYKWH_E062` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | rolling element |  |
| 7 | `WZ2VYKWH_E063` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | crack |  |
| 8 | `WZ2VYKWH_E064` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | defect |  |
| 9 | `WZ2VYKWH_E065` | `can be used for` | 10-Dataset | Simulated signals |  | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  |
| 10 | `WZ2VYKWH_E066` | `can be used for` | 10-Dataset | TPL bearing dataset |  | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  |
| 11 | `WZ2VYKWH_E067` | `has_fault_mode` | 04-Fault Location | outer race |  | 05-Fault Mode | crack |  |
| 12 | `WZ2VYKWH_E068` | `has_fault_mode` | 04-Fault Location | outer race |  | 05-Fault Mode | defect |  |
| 13 | `WZ2VYKWH_E069` | `has_fault_mode` | 04-Fault Location | rolling element |  | 05-Fault Mode | crack |  |
| 14 | `WZ2VYKWH_E070` | `has_fault_mode` | 04-Fault Location | rolling element |  | 05-Fault Mode | defect |  |
| 15 | `WZ2VYKWH_E071` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | Single Severity |  |
| 16 | `WZ2VYKWH_E072` | `contains` | 05-Fault Mode | defect |  | 06-Fault Severity | Single Severity |  |
| 17 | `WZ2VYKWH_E074` | `contains_phm_task` | 04-Fault Location | outer race |  | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  |
| 18 | `WZ2VYKWH_E075` | `contains_phm_task` | 04-Fault Location | rolling element |  | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  |
| 19 | `WZ2VYKWH_E076` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  |
| 20 | `WZ2VYKWH_E077` | `contains_phm_task` | 05-Fault Mode | defect |  | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  |
| 21 | `WZ2VYKWH_E079` | `induces_problem` | 02-Object Type | double-row tapered roller bearing |  | 09-Problem Scenario | multiple fault(Compound Faults) |  |
| 22 | `WZ2VYKWH_E080` | `induces_problem` | 02-Object Type | double-row tapered roller bearing |  | 09-Problem Scenario | adaptive determination of VMD parameters(Other) |  |
| 23 | `WZ2VYKWH_E081` | `induces_problem` | 03-Operating Conditions | constant speed of 100 km/h(Single Condition) |  | 09-Problem Scenario | multiple fault(Compound Faults) |  |
| 24 | `WZ2VYKWH_E082` | `induces_problem` | 03-Operating Conditions | constant speed of 100 km/h(Single Condition) |  | 09-Problem Scenario | adaptive determination of VMD parameters(Other) |  |
| 25 | `WZ2VYKWH_E083` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | multiple fault(Compound Faults) |  |
| 26 | `WZ2VYKWH_E084` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | adaptive determination of VMD parameters(Other) |  |
| 27 | `WZ2VYKWH_E085` | `induces_problem` | 07-Compound Fault | multiple fault(Compound Fault Within Same Structure) |  | 09-Problem Scenario | multiple fault(Compound Faults) |  |
| 28 | `WZ2VYKWH_E086` | `induces_problem` | 07-Compound Fault | multiple fault(Compound Fault Within Same Structure) |  | 09-Problem Scenario | adaptive determination of VMD parameters(Other) |  |
| 29 | `WZ2VYKWH_E087` | `induces_problem` | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multiple fault(Compound Faults) |  |
| 30 | `WZ2VYKWH_E088` | `induces_problem` | 08-PHM Task | bearing fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | adaptive determination of VMD parameters(Other) |  |

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
