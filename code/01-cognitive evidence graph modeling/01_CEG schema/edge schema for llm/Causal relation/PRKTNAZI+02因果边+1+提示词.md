# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PRKTNAZI
- **Paper Title**：Domain Adversarial Transfer Network for Cross-Domain Fault Diagnosis of Rotary Machinery
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `PRKTNAZI`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PRKTNAZI_E061", "edge_description": "Rotary Machinery contains rolling element bearing"},
    {"edge_id": "PRKTNAZI_E062", "edge_description": "Rotary Machinery contains gearbox"},
    {"edge_id": "PRKTNAZI_E063", "edge_description": "rolling element bearing contains rolling element bearing"},
    {"edge_id": "PRKTNAZI_E064", "edge_description": "rolling element bearing contains gear / gearbox"},
    {"edge_id": "PRKTNAZI_E065", "edge_description": "gearbox contains rolling element bearing"},
    {"edge_id": "PRKTNAZI_E066", "edge_description": "gearbox contains gear / gearbox"},
    {"edge_id": "PRKTNAZI_E067", "edge_description": "rolling element bearing contains operating conditions"},
    {"edge_id": "PRKTNAZI_E068", "edge_description": "gearbox contains operating conditions"},
    {"edge_id": "PRKTNAZI_E069", "edge_description": "inner race fault, outer race fault contains compound faults combining gears and bearings"},
    {"edge_id": "PRKTNAZI_E070", "edge_description": "chipped tooth, missing tooth contains compound faults combining gears and bearings"},
    {"edge_id": "PRKTNAZI_E071", "edge_description": "accelerometer is collected on rolling element bearing"},
    {"edge_id": "PRKTNAZI_E072", "edge_description": "accelerometer is collected on gear / gearbox"},
    {"edge_id": "PRKTNAZI_E073", "edge_description": "accelerometer can obviously reflect inner race fault, outer race fault"},
    {"edge_id": "PRKTNAZI_E074", "edge_description": "accelerometer can obviously reflect chipped tooth, missing tooth"},
    {"edge_id": "PRKTNAZI_E075", "edge_description": "rolling element bearing dataset can be used for fault diagnosis"},
    {"edge_id": "PRKTNAZI_E076", "edge_description": "gearbox dataset can be used for fault diagnosis"},
    {"edge_id": "PRKTNAZI_E077", "edge_description": "rolling element bearing has_fault_mode inner race fault, outer race fault"},
    {"edge_id": "PRKTNAZI_E078", "edge_description": "rolling element bearing has_fault_mode chipped tooth, missing tooth"},
    {"edge_id": "PRKTNAZI_E079", "edge_description": "gear / gearbox has_fault_mode inner race fault, outer race fault"},
    {"edge_id": "PRKTNAZI_E080", "edge_description": "gear / gearbox has_fault_mode chipped tooth, missing tooth"},
    {"edge_id": "PRKTNAZI_E081", "edge_description": "inner race fault, outer race fault contains defect diameters of 0.5 mm and 2 mm, 0.2mm defect"},
    {"edge_id": "PRKTNAZI_E082", "edge_description": "chipped tooth, missing tooth contains defect diameters of 0.5 mm and 2 mm, 0.2mm defect"},
    {"edge_id": "PRKTNAZI_E083", "edge_description": "rolling element bearing contains_phm_task fault diagnosis"},
    {"edge_id": "PRKTNAZI_E084", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "PRKTNAZI_E085", "edge_description": "rolling element bearing contains_phm_task fault diagnosis"},
    {"edge_id": "PRKTNAZI_E086", "edge_description": "gear / gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "PRKTNAZI_E087", "edge_description": "inner race fault, outer race fault contains_phm_task fault diagnosis"},
    {"edge_id": "PRKTNAZI_E088", "edge_description": "chipped tooth, missing tooth contains_phm_task fault diagnosis"},
    {"edge_id": "PRKTNAZI_E090", "edge_description": "rolling element bearing induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E091", "edge_description": "rolling element bearing induces_problem noise contamination"}
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
| 1 | `PRKTNAZI_E061` | `contains` | 01-Object Domain | Rotary Machinery(Industrial) |  | 02-Object Type | rolling element bearing |  |
| 2 | `PRKTNAZI_E062` | `contains` | 01-Object Domain | Rotary Machinery(Industrial) |  | 02-Object Type | gearbox |  |
| 3 | `PRKTNAZI_E063` | `contains` | 02-Object Type | rolling element bearing |  | 04-Fault Location | rolling element bearing |  |
| 4 | `PRKTNAZI_E064` | `contains` | 02-Object Type | rolling element bearing |  | 04-Fault Location | gear / gearbox |  |
| 5 | `PRKTNAZI_E065` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | rolling element bearing |  |
| 6 | `PRKTNAZI_E066` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | gear / gearbox |  |
| 7 | `PRKTNAZI_E067` | `contains` | 02-Object Type | rolling element bearing |  | 03-Operating Conditions | operating conditions(Multiple Conditions) |  |
| 8 | `PRKTNAZI_E068` | `contains` | 02-Object Type | gearbox |  | 03-Operating Conditions | operating conditions(Multiple Conditions) |  |
| 9 | `PRKTNAZI_E069` | `contains` | 05-Fault Mode | inner race fault, outer race fault |  | 07-Compound Fault | compound faults combining gears and bearings(Compound Fault Across Structures) |  |
| 10 | `PRKTNAZI_E070` | `contains` | 05-Fault Mode | chipped tooth, missing tooth |  | 07-Compound Fault | compound faults combining gears and bearings(Compound Fault Across Structures) |  |
| 11 | `PRKTNAZI_E071` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | rolling element bearing |  |
| 12 | `PRKTNAZI_E072` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | gear / gearbox |  |
| 13 | `PRKTNAZI_E073` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | inner race fault, outer race fault |  |
| 14 | `PRKTNAZI_E074` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | chipped tooth, missing tooth |  |
| 15 | `PRKTNAZI_E075` | `can be used for` | 10-Dataset | rolling element bearing dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `PRKTNAZI_E076` | `can be used for` | 10-Dataset | gearbox dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `PRKTNAZI_E077` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | inner race fault, outer race fault |  |
| 18 | `PRKTNAZI_E078` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | chipped tooth, missing tooth |  |
| 19 | `PRKTNAZI_E079` | `has_fault_mode` | 04-Fault Location | gear / gearbox |  | 05-Fault Mode | inner race fault, outer race fault |  |
| 20 | `PRKTNAZI_E080` | `has_fault_mode` | 04-Fault Location | gear / gearbox |  | 05-Fault Mode | chipped tooth, missing tooth |  |
| 21 | `PRKTNAZI_E081` | `contains` | 05-Fault Mode | inner race fault, outer race fault |  | 06-Fault Severity | defect diameters of 0.5 mm and 2 mm, 0.2mm defect(Multiple Severities) |  |
| 22 | `PRKTNAZI_E082` | `contains` | 05-Fault Mode | chipped tooth, missing tooth |  | 06-Fault Severity | defect diameters of 0.5 mm and 2 mm, 0.2mm defect(Multiple Severities) |  |
| 23 | `PRKTNAZI_E083` | `contains_phm_task` | 02-Object Type | rolling element bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 24 | `PRKTNAZI_E084` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 25 | `PRKTNAZI_E085` | `contains_phm_task` | 04-Fault Location | rolling element bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 26 | `PRKTNAZI_E086` | `contains_phm_task` | 04-Fault Location | gear / gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 27 | `PRKTNAZI_E087` | `contains_phm_task` | 05-Fault Mode | inner race fault, outer race fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 28 | `PRKTNAZI_E088` | `contains_phm_task` | 05-Fault Mode | chipped tooth, missing tooth |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 29 | `PRKTNAZI_E090` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 30 | `PRKTNAZI_E091` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |

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
