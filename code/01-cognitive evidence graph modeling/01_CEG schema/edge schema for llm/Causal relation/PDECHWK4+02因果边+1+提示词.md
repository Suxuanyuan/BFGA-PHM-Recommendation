# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PDECHWK4
- **Paper Title**：Ground Fault Detection Method for Variable Speed Drives
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `PDECHWK4`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PDECHWK4_E041", "edge_description": "Variable speed drives / Power electronics contains Variable speed drive"},
    {"edge_id": "PDECHWK4_E042", "edge_description": "Variable speed drives / Power electronics contains Power converter"},
    {"edge_id": "PDECHWK4_E043", "edge_description": "Variable speed drives / Power electronics contains Main power transformer"},
    {"edge_id": "PDECHWK4_E044", "edge_description": "Variable speed drive contains AC grid side"},
    {"edge_id": "PDECHWK4_E045", "edge_description": "Variable speed drive contains DC link"},
    {"edge_id": "PDECHWK4_E046", "edge_description": "Variable speed drive contains AC inverter side"},
    {"edge_id": "PDECHWK4_E047", "edge_description": "Power converter contains AC grid side"},
    {"edge_id": "PDECHWK4_E048", "edge_description": "Power converter contains DC link"},
    {"edge_id": "PDECHWK4_E049", "edge_description": "Power converter contains AC inverter side"},
    {"edge_id": "PDECHWK4_E050", "edge_description": "Main power transformer contains AC grid side"},
    {"edge_id": "PDECHWK4_E051", "edge_description": "Main power transformer contains DC link"},
    {"edge_id": "PDECHWK4_E052", "edge_description": "Main power transformer contains AC inverter side"},
    {"edge_id": "PDECHWK4_E053", "edge_description": "Variable speed drive contains Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency"},
    {"edge_id": "PDECHWK4_E054", "edge_description": "Power converter contains Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency"},
    {"edge_id": "PDECHWK4_E055", "edge_description": "Main power transformer contains Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency"},
    {"edge_id": "PDECHWK4_E057", "edge_description": "voltage sensor (oscilloscope) is collected on AC grid side"},
    {"edge_id": "PDECHWK4_E058", "edge_description": "voltage sensor (oscilloscope) is collected on DC link"},
    {"edge_id": "PDECHWK4_E059", "edge_description": "voltage sensor (oscilloscope) is collected on AC inverter side"},
    {"edge_id": "PDECHWK4_E061", "edge_description": "Matlab Simulink simulation data can be used for Ground fault detection"},
    {"edge_id": "PDECHWK4_E062", "edge_description": "Experimental data from a 140 kW power converter setup can be used for Ground fault detection"},
    {"edge_id": "PDECHWK4_E063", "edge_description": "AC grid side has_fault_mode ground fault"},
    {"edge_id": "PDECHWK4_E064", "edge_description": "DC link has_fault_mode ground fault"},
    {"edge_id": "PDECHWK4_E065", "edge_description": "AC inverter side has_fault_mode ground fault"},
    {"edge_id": "PDECHWK4_E067", "edge_description": "Variable speed drive contains_phm_task Ground fault detection"},
    {"edge_id": "PDECHWK4_E068", "edge_description": "Power converter contains_phm_task Ground fault detection"},
    {"edge_id": "PDECHWK4_E069", "edge_description": "Main power transformer contains_phm_task Ground fault detection"},
    {"edge_id": "PDECHWK4_E070", "edge_description": "AC grid side contains_phm_task Ground fault detection"},
    {"edge_id": "PDECHWK4_E071", "edge_description": "DC link contains_phm_task Ground fault detection"},
    {"edge_id": "PDECHWK4_E072", "edge_description": "AC inverter side contains_phm_task Ground fault detection"},
    {"edge_id": "PDECHWK4_E075", "edge_description": "Variable speed drive induces_problem Ground fault detection across different stages of variable speed drives"}
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
| 1 | `PDECHWK4_E041` | `contains` | 01-Object Domain | Variable speed drives / Power electronics(Electronics) |  | 02-Object Type | Variable speed drive |  |
| 2 | `PDECHWK4_E042` | `contains` | 01-Object Domain | Variable speed drives / Power electronics(Electronics) |  | 02-Object Type | Power converter |  |
| 3 | `PDECHWK4_E043` | `contains` | 01-Object Domain | Variable speed drives / Power electronics(Electronics) |  | 02-Object Type | Main power transformer |  |
| 4 | `PDECHWK4_E044` | `contains` | 02-Object Type | Variable speed drive |  | 04-Fault Location | AC grid side |  |
| 5 | `PDECHWK4_E045` | `contains` | 02-Object Type | Variable speed drive |  | 04-Fault Location | DC link |  |
| 6 | `PDECHWK4_E046` | `contains` | 02-Object Type | Variable speed drive |  | 04-Fault Location | AC inverter side |  |
| 7 | `PDECHWK4_E047` | `contains` | 02-Object Type | Power converter |  | 04-Fault Location | AC grid side |  |
| 8 | `PDECHWK4_E048` | `contains` | 02-Object Type | Power converter |  | 04-Fault Location | DC link |  |
| 9 | `PDECHWK4_E049` | `contains` | 02-Object Type | Power converter |  | 04-Fault Location | AC inverter side |  |
| 10 | `PDECHWK4_E050` | `contains` | 02-Object Type | Main power transformer |  | 04-Fault Location | AC grid side |  |
| 11 | `PDECHWK4_E051` | `contains` | 02-Object Type | Main power transformer |  | 04-Fault Location | DC link |  |
| 12 | `PDECHWK4_E052` | `contains` | 02-Object Type | Main power transformer |  | 04-Fault Location | AC inverter side |  |
| 13 | `PDECHWK4_E053` | `contains` | 02-Object Type | Variable speed drive |  | 03-Operating Conditions | Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency(Single Condition) |  |
| 14 | `PDECHWK4_E054` | `contains` | 02-Object Type | Power converter |  | 03-Operating Conditions | Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency(Single Condition) |  |
| 15 | `PDECHWK4_E055` | `contains` | 02-Object Type | Main power transformer |  | 03-Operating Conditions | Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency(Single Condition) |  |
| 16 | `PDECHWK4_E057` | `is collected on` | 11-Sensor Information | voltage sensor (oscilloscope) |  | 04-Fault Location | AC grid side |  |
| 17 | `PDECHWK4_E058` | `is collected on` | 11-Sensor Information | voltage sensor (oscilloscope) |  | 04-Fault Location | DC link |  |
| 18 | `PDECHWK4_E059` | `is collected on` | 11-Sensor Information | voltage sensor (oscilloscope) |  | 04-Fault Location | AC inverter side |  |
| 19 | `PDECHWK4_E061` | `can be used for` | 10-Dataset | Matlab Simulink simulation data |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 20 | `PDECHWK4_E062` | `can be used for` | 10-Dataset | Experimental data from a 140 kW power converter setup |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 21 | `PDECHWK4_E063` | `has_fault_mode` | 04-Fault Location | AC grid side |  | 05-Fault Mode | ground fault |  |
| 22 | `PDECHWK4_E064` | `has_fault_mode` | 04-Fault Location | DC link |  | 05-Fault Mode | ground fault |  |
| 23 | `PDECHWK4_E065` | `has_fault_mode` | 04-Fault Location | AC inverter side |  | 05-Fault Mode | ground fault |  |
| 24 | `PDECHWK4_E067` | `contains_phm_task` | 02-Object Type | Variable speed drive |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 25 | `PDECHWK4_E068` | `contains_phm_task` | 02-Object Type | Power converter |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 26 | `PDECHWK4_E069` | `contains_phm_task` | 02-Object Type | Main power transformer |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 27 | `PDECHWK4_E070` | `contains_phm_task` | 04-Fault Location | AC grid side |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 28 | `PDECHWK4_E071` | `contains_phm_task` | 04-Fault Location | DC link |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 29 | `PDECHWK4_E072` | `contains_phm_task` | 04-Fault Location | AC inverter side |  | 08-PHM Task | Ground fault detection(Detection Task) |  |
| 30 | `PDECHWK4_E075` | `induces_problem` | 02-Object Type | Variable speed drive |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |

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
