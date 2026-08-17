# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：6XHTXQ5F
- **Paper Title**：Open-Circuit Fault Diagnosis in Power Inverters Through Currents Analysis in Time Domain
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `6XHTXQ5F`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "6XHTXQ5F_E035", "edge_description": "lightweight electric vehicle contains power inverter"},
    {"edge_id": "6XHTXQ5F_E036", "edge_description": "lightweight electric vehicle contains brushless dc (BLDC) electric motor"},
    {"edge_id": "6XHTXQ5F_E037", "edge_description": "power inverter contains power inverter"},
    {"edge_id": "6XHTXQ5F_E038", "edge_description": "power inverter contains IGBT switch"},
    {"edge_id": "6XHTXQ5F_E039", "edge_description": "brushless dc (BLDC) electric motor contains power inverter"},
    {"edge_id": "6XHTXQ5F_E040", "edge_description": "brushless dc (BLDC) electric motor contains IGBT switch"},
    {"edge_id": "6XHTXQ5F_E041", "edge_description": "power inverter contains nominal load"},
    {"edge_id": "6XHTXQ5F_E042", "edge_description": "brushless dc (BLDC) electric motor contains nominal load"},
    {"edge_id": "6XHTXQ5F_E044", "edge_description": "Current sensor is collected on power inverter"},
    {"edge_id": "6XHTXQ5F_E045", "edge_description": "Current sensor is collected on IGBT switch"},
    {"edge_id": "6XHTXQ5F_E048", "edge_description": "power inverter has_fault_mode open-circuit fault"},
    {"edge_id": "6XHTXQ5F_E049", "edge_description": "IGBT switch has_fault_mode open-circuit fault"},
    {"edge_id": "6XHTXQ5F_E051", "edge_description": "power inverter contains_phm_task open-circuit fault diagnosis and isolation"},
    {"edge_id": "6XHTXQ5F_E052", "edge_description": "brushless dc (BLDC) electric motor contains_phm_task open-circuit fault diagnosis and isolation"},
    {"edge_id": "6XHTXQ5F_E053", "edge_description": "power inverter contains_phm_task open-circuit fault diagnosis and isolation"},
    {"edge_id": "6XHTXQ5F_E054", "edge_description": "IGBT switch contains_phm_task open-circuit fault diagnosis and isolation"},
    {"edge_id": "6XHTXQ5F_E057", "edge_description": "power inverter induces_problem combined faults / simultaneous faults in multiple switches"},
    {"edge_id": "6XHTXQ5F_E058", "edge_description": "power inverter induces_problem high computational cost of conventional methods"},
    {"edge_id": "6XHTXQ5F_E059", "edge_description": "brushless dc (BLDC) electric motor induces_problem combined faults / simultaneous faults in multiple switches"},
    {"edge_id": "6XHTXQ5F_E060", "edge_description": "brushless dc (BLDC) electric motor induces_problem high computational cost of conventional methods"},
    {"edge_id": "6XHTXQ5F_E061", "edge_description": "nominal load induces_problem combined faults / simultaneous faults in multiple switches"},
    {"edge_id": "6XHTXQ5F_E062", "edge_description": "nominal load induces_problem high computational cost of conventional methods"},
    {"edge_id": "6XHTXQ5F_E063", "edge_description": "Single Severity induces_problem combined faults / simultaneous faults in multiple switches"},
    {"edge_id": "6XHTXQ5F_E064", "edge_description": "Single Severity induces_problem high computational cost of conventional methods"},
    {"edge_id": "6XHTXQ5F_E065", "edge_description": "simultaneous faults induces_problem combined faults / simultaneous faults in multiple switches"},
    {"edge_id": "6XHTXQ5F_E066", "edge_description": "simultaneous faults induces_problem high computational cost of conventional methods"},
    {"edge_id": "6XHTXQ5F_E067", "edge_description": "open-circuit fault diagnosis and isolation induces_problem combined faults / simultaneous faults in multiple switches"},
    {"edge_id": "6XHTXQ5F_E068", "edge_description": "open-circuit fault diagnosis and isolation induces_problem high computational cost of conventional methods"},
    {"edge_id": "6XHTXQ5F_E069", "edge_description": "None induces_problem combined faults / simultaneous faults in multiple switches"},
    {"edge_id": "6XHTXQ5F_E070", "edge_description": "None induces_problem high computational cost of conventional methods"}
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
| 1 | `6XHTXQ5F_E035` | `contains` | 01-Object Domain | lightweight electric vehicle(Vehicle) |  | 02-Object Type | power inverter |  |
| 2 | `6XHTXQ5F_E036` | `contains` | 01-Object Domain | lightweight electric vehicle(Vehicle) |  | 02-Object Type | brushless dc (BLDC) electric motor |  |
| 3 | `6XHTXQ5F_E037` | `contains` | 02-Object Type | power inverter |  | 04-Fault Location | power inverter |  |
| 4 | `6XHTXQ5F_E038` | `contains` | 02-Object Type | power inverter |  | 04-Fault Location | IGBT switch |  |
| 5 | `6XHTXQ5F_E039` | `contains` | 02-Object Type | brushless dc (BLDC) electric motor |  | 04-Fault Location | power inverter |  |
| 6 | `6XHTXQ5F_E040` | `contains` | 02-Object Type | brushless dc (BLDC) electric motor |  | 04-Fault Location | IGBT switch |  |
| 7 | `6XHTXQ5F_E041` | `contains` | 02-Object Type | power inverter |  | 03-Operating Conditions | nominal load(Single Condition) |  |
| 8 | `6XHTXQ5F_E042` | `contains` | 02-Object Type | brushless dc (BLDC) electric motor |  | 03-Operating Conditions | nominal load(Single Condition) |  |
| 9 | `6XHTXQ5F_E044` | `is collected on` | 11-Sensor Information | Current sensor |  | 04-Fault Location | power inverter |  |
| 10 | `6XHTXQ5F_E045` | `is collected on` | 11-Sensor Information | Current sensor |  | 04-Fault Location | IGBT switch |  |
| 11 | `6XHTXQ5F_E048` | `has_fault_mode` | 04-Fault Location | power inverter |  | 05-Fault Mode | open-circuit fault |  |
| 12 | `6XHTXQ5F_E049` | `has_fault_mode` | 04-Fault Location | IGBT switch |  | 05-Fault Mode | open-circuit fault |  |
| 13 | `6XHTXQ5F_E051` | `contains_phm_task` | 02-Object Type | power inverter |  | 08-PHM Task | open-circuit fault diagnosis and isolation(Diagnosis Task) |  |
| 14 | `6XHTXQ5F_E052` | `contains_phm_task` | 02-Object Type | brushless dc (BLDC) electric motor |  | 08-PHM Task | open-circuit fault diagnosis and isolation(Diagnosis Task) |  |
| 15 | `6XHTXQ5F_E053` | `contains_phm_task` | 04-Fault Location | power inverter |  | 08-PHM Task | open-circuit fault diagnosis and isolation(Diagnosis Task) |  |
| 16 | `6XHTXQ5F_E054` | `contains_phm_task` | 04-Fault Location | IGBT switch |  | 08-PHM Task | open-circuit fault diagnosis and isolation(Diagnosis Task) |  |
| 17 | `6XHTXQ5F_E057` | `induces_problem` | 02-Object Type | power inverter |  | 09-Problem Scenario | combined faults / simultaneous faults in multiple switches(Compound Faults) |  |
| 18 | `6XHTXQ5F_E058` | `induces_problem` | 02-Object Type | power inverter |  | 09-Problem Scenario | high computational cost of conventional methods(Other) |  |
| 19 | `6XHTXQ5F_E059` | `induces_problem` | 02-Object Type | brushless dc (BLDC) electric motor |  | 09-Problem Scenario | combined faults / simultaneous faults in multiple switches(Compound Faults) |  |
| 20 | `6XHTXQ5F_E060` | `induces_problem` | 02-Object Type | brushless dc (BLDC) electric motor |  | 09-Problem Scenario | high computational cost of conventional methods(Other) |  |
| 21 | `6XHTXQ5F_E061` | `induces_problem` | 03-Operating Conditions | nominal load(Single Condition) |  | 09-Problem Scenario | combined faults / simultaneous faults in multiple switches(Compound Faults) |  |
| 22 | `6XHTXQ5F_E062` | `induces_problem` | 03-Operating Conditions | nominal load(Single Condition) |  | 09-Problem Scenario | high computational cost of conventional methods(Other) |  |
| 23 | `6XHTXQ5F_E063` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | combined faults / simultaneous faults in multiple switches(Compound Faults) |  |
| 24 | `6XHTXQ5F_E064` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | high computational cost of conventional methods(Other) |  |
| 25 | `6XHTXQ5F_E065` | `induces_problem` | 07-Compound Fault | simultaneous faults(Compound Fault Within Same Structure) |  | 09-Problem Scenario | combined faults / simultaneous faults in multiple switches(Compound Faults) |  |
| 26 | `6XHTXQ5F_E066` | `induces_problem` | 07-Compound Fault | simultaneous faults(Compound Fault Within Same Structure) |  | 09-Problem Scenario | high computational cost of conventional methods(Other) |  |
| 27 | `6XHTXQ5F_E067` | `induces_problem` | 08-PHM Task | open-circuit fault diagnosis and isolation(Diagnosis Task) |  | 09-Problem Scenario | combined faults / simultaneous faults in multiple switches(Compound Faults) |  |
| 28 | `6XHTXQ5F_E068` | `induces_problem` | 08-PHM Task | open-circuit fault diagnosis and isolation(Diagnosis Task) |  | 09-Problem Scenario | high computational cost of conventional methods(Other) |  |
| 29 | `6XHTXQ5F_E069` | `induces_problem` | 12-Training Data Availability | None(Sufficient) |  | 09-Problem Scenario | combined faults / simultaneous faults in multiple switches(Compound Faults) |  |
| 30 | `6XHTXQ5F_E070` | `induces_problem` | 12-Training Data Availability | None(Sufficient) |  | 09-Problem Scenario | high computational cost of conventional methods(Other) |  |

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
