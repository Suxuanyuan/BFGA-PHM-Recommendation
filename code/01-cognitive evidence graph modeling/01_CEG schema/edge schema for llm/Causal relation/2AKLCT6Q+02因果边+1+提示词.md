# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：2AKLCT6Q
- **Paper Title**：Detection and Spatial Identification of Fault for Parabolic Distributed Parameter Systems
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `2AKLCT6Q`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "2AKLCT6Q_E055", "edge_description": "industrial processes contains catalytic rod"},
    {"edge_id": "2AKLCT6Q_E056", "edge_description": "industrial processes contains snap curing oven"},
    {"edge_id": "2AKLCT6Q_E057", "edge_description": "catalytic rod contains actuator"},
    {"edge_id": "2AKLCT6Q_E058", "edge_description": "catalytic rod contains heater"},
    {"edge_id": "2AKLCT6Q_E059", "edge_description": "snap curing oven contains actuator"},
    {"edge_id": "2AKLCT6Q_E060", "edge_description": "snap curing oven contains heater"},
    {"edge_id": "2AKLCT6Q_E061", "edge_description": "catalytic rod contains normal and abnormal operating conditions with static distributions"},
    {"edge_id": "2AKLCT6Q_E062", "edge_description": "snap curing oven contains normal and abnormal operating conditions with static distributions"},
    {"edge_id": "2AKLCT6Q_E064", "edge_description": "thermocouples, temperature sensors is collected on actuator"},
    {"edge_id": "2AKLCT6Q_E065", "edge_description": "thermocouples, temperature sensors is collected on heater"},
    {"edge_id": "2AKLCT6Q_E067", "edge_description": "Simulation: Catalytic rod model can be used for fault detection and spatial identification"},
    {"edge_id": "2AKLCT6Q_E068", "edge_description": "Self-collected: Snap curing oven experimental data can be used for fault detection and spatial identification"},
    {"edge_id": "2AKLCT6Q_E069", "edge_description": "actuator has_fault_mode actuator fault"},
    {"edge_id": "2AKLCT6Q_E070", "edge_description": "heater has_fault_mode actuator fault"},
    {"edge_id": "2AKLCT6Q_E072", "edge_description": "catalytic rod contains_phm_task fault detection and spatial identification"},
    {"edge_id": "2AKLCT6Q_E073", "edge_description": "snap curing oven contains_phm_task fault detection and spatial identification"},
    {"edge_id": "2AKLCT6Q_E074", "edge_description": "actuator contains_phm_task fault detection and spatial identification"},
    {"edge_id": "2AKLCT6Q_E075", "edge_description": "heater contains_phm_task fault detection and spatial identification"},
    {"edge_id": "2AKLCT6Q_E078", "edge_description": "catalytic rod induces_problem infinite-dimensional characteristic of DPSs"},
    {"edge_id": "2AKLCT6Q_E079", "edge_description": "catalytic rod induces_problem limited sensors in real industry processes"},
    {"edge_id": "2AKLCT6Q_E080", "edge_description": "snap curing oven induces_problem infinite-dimensional characteristic of DPSs"},
    {"edge_id": "2AKLCT6Q_E081", "edge_description": "snap curing oven induces_problem limited sensors in real industry processes"},
    {"edge_id": "2AKLCT6Q_E082", "edge_description": "normal and abnormal operating conditions with static distributions induces_problem infinite-dimensional characteristic of DPSs"},
    {"edge_id": "2AKLCT6Q_E083", "edge_description": "normal and abnormal operating conditions with static distributions induces_problem limited sensors in real industry processes"},
    {"edge_id": "2AKLCT6Q_E084", "edge_description": "bf(pi/8) = 8 * bu(pi/8), bf(7pi/8) = 9 * bu(7pi/8), u1 -> 2 * u1, u4 -> u4 + 0.3 induces_problem infinite-dimensional characteristic of DPSs"},
    {"edge_id": "2AKLCT6Q_E085", "edge_description": "bf(pi/8) = 8 * bu(pi/8), bf(7pi/8) = 9 * bu(7pi/8), u1 -> 2 * u1, u4 -> u4 + 0.3 induces_problem limited sensors in real industry processes"},
    {"edge_id": "2AKLCT6Q_E086", "edge_description": "No Compound Fault induces_problem infinite-dimensional characteristic of DPSs"},
    {"edge_id": "2AKLCT6Q_E087", "edge_description": "No Compound Fault induces_problem limited sensors in real industry processes"},
    {"edge_id": "2AKLCT6Q_E088", "edge_description": "fault detection and spatial identification induces_problem infinite-dimensional characteristic of DPSs"},
    {"edge_id": "2AKLCT6Q_E089", "edge_description": "fault detection and spatial identification induces_problem limited sensors in real industry processes"}
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
| 1 | `2AKLCT6Q_E055` | `contains` | 01-Object Domain | industrial processes(Industrial) |  | 02-Object Type | catalytic rod |  |
| 2 | `2AKLCT6Q_E056` | `contains` | 01-Object Domain | industrial processes(Industrial) |  | 02-Object Type | snap curing oven |  |
| 3 | `2AKLCT6Q_E057` | `contains` | 02-Object Type | catalytic rod |  | 04-Fault Location | actuator |  |
| 4 | `2AKLCT6Q_E058` | `contains` | 02-Object Type | catalytic rod |  | 04-Fault Location | heater |  |
| 5 | `2AKLCT6Q_E059` | `contains` | 02-Object Type | snap curing oven |  | 04-Fault Location | actuator |  |
| 6 | `2AKLCT6Q_E060` | `contains` | 02-Object Type | snap curing oven |  | 04-Fault Location | heater |  |
| 7 | `2AKLCT6Q_E061` | `contains` | 02-Object Type | catalytic rod |  | 03-Operating Conditions | normal and abnormal operating conditions with static distributions(Single Condition) |  |
| 8 | `2AKLCT6Q_E062` | `contains` | 02-Object Type | snap curing oven |  | 03-Operating Conditions | normal and abnormal operating conditions with static distributions(Single Condition) |  |
| 9 | `2AKLCT6Q_E064` | `is collected on` | 11-Sensor Information | thermocouples, temperature sensors |  | 04-Fault Location | actuator |  |
| 10 | `2AKLCT6Q_E065` | `is collected on` | 11-Sensor Information | thermocouples, temperature sensors |  | 04-Fault Location | heater |  |
| 11 | `2AKLCT6Q_E067` | `can be used for` | 10-Dataset | Simulation: Catalytic rod model |  | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  |
| 12 | `2AKLCT6Q_E068` | `can be used for` | 10-Dataset | Self-collected: Snap curing oven experimental data |  | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  |
| 13 | `2AKLCT6Q_E069` | `has_fault_mode` | 04-Fault Location | actuator |  | 05-Fault Mode | actuator fault |  |
| 14 | `2AKLCT6Q_E070` | `has_fault_mode` | 04-Fault Location | heater |  | 05-Fault Mode | actuator fault |  |
| 15 | `2AKLCT6Q_E072` | `contains_phm_task` | 02-Object Type | catalytic rod |  | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  |
| 16 | `2AKLCT6Q_E073` | `contains_phm_task` | 02-Object Type | snap curing oven |  | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  |
| 17 | `2AKLCT6Q_E074` | `contains_phm_task` | 04-Fault Location | actuator |  | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  |
| 18 | `2AKLCT6Q_E075` | `contains_phm_task` | 04-Fault Location | heater |  | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  |
| 19 | `2AKLCT6Q_E078` | `induces_problem` | 02-Object Type | catalytic rod |  | 09-Problem Scenario | infinite-dimensional characteristic of DPSs(Complex Systems) |  |
| 20 | `2AKLCT6Q_E079` | `induces_problem` | 02-Object Type | catalytic rod |  | 09-Problem Scenario | limited sensors in real industry processes(Other) |  |
| 21 | `2AKLCT6Q_E080` | `induces_problem` | 02-Object Type | snap curing oven |  | 09-Problem Scenario | infinite-dimensional characteristic of DPSs(Complex Systems) |  |
| 22 | `2AKLCT6Q_E081` | `induces_problem` | 02-Object Type | snap curing oven |  | 09-Problem Scenario | limited sensors in real industry processes(Other) |  |
| 23 | `2AKLCT6Q_E082` | `induces_problem` | 03-Operating Conditions | normal and abnormal operating conditions with static distributions(Single Condition) |  | 09-Problem Scenario | infinite-dimensional characteristic of DPSs(Complex Systems) |  |
| 24 | `2AKLCT6Q_E083` | `induces_problem` | 03-Operating Conditions | normal and abnormal operating conditions with static distributions(Single Condition) |  | 09-Problem Scenario | limited sensors in real industry processes(Other) |  |
| 25 | `2AKLCT6Q_E084` | `induces_problem` | 06-Fault Severity | bf(pi/8) = 8 * bu(pi/8), bf(7pi/8) = 9 * bu(7pi/8), u1 -> 2 * u1, u4 -> u4 + 0.3(Single Severity) |  | 09-Problem Scenario | infinite-dimensional characteristic of DPSs(Complex Systems) |  |
| 26 | `2AKLCT6Q_E085` | `induces_problem` | 06-Fault Severity | bf(pi/8) = 8 * bu(pi/8), bf(7pi/8) = 9 * bu(7pi/8), u1 -> 2 * u1, u4 -> u4 + 0.3(Single Severity) |  | 09-Problem Scenario | limited sensors in real industry processes(Other) |  |
| 27 | `2AKLCT6Q_E086` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | infinite-dimensional characteristic of DPSs(Complex Systems) |  |
| 28 | `2AKLCT6Q_E087` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | limited sensors in real industry processes(Other) |  |
| 29 | `2AKLCT6Q_E088` | `induces_problem` | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  | 09-Problem Scenario | infinite-dimensional characteristic of DPSs(Complex Systems) |  |
| 30 | `2AKLCT6Q_E089` | `induces_problem` | 08-PHM Task | fault detection and spatial identification(Diagnosis Task) |  | 09-Problem Scenario | limited sensors in real industry processes(Other) |  |

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
