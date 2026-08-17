# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：ECSG5ICS
- **Paper Title**：Fault Diagnosis of Bearing in Wind Turbine Gearbox Under Actual Operating Conditions Driven by Limited Data With Noise Labels
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `ECSG5ICS`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "ECSG5ICS_E187", "edge_description": "PLC upwind bearing has_fault_mode Assembly damage"},
    {"edge_id": "ECSG5ICS_E188", "edge_description": "PLC upwind bearing has_fault_mode Scuffing"},
    {"edge_id": "ECSG5ICS_E189", "edge_description": "PLC upwind bearing has_fault_mode Dents"},
    {"edge_id": "ECSG5ICS_E190", "edge_description": "PLC upwind bearing has_fault_mode Fretting corrosion"},
    {"edge_id": "ECSG5ICS_E191", "edge_description": "Overheating contains Single Severity"},
    {"edge_id": "ECSG5ICS_E192", "edge_description": "Assembly damage contains Single Severity"},
    {"edge_id": "ECSG5ICS_E193", "edge_description": "Scuffing contains Single Severity"},
    {"edge_id": "ECSG5ICS_E194", "edge_description": "Dents contains Single Severity"},
    {"edge_id": "ECSG5ICS_E195", "edge_description": "Fretting corrosion contains Single Severity"},
    {"edge_id": "ECSG5ICS_E196", "edge_description": "rolling bearing contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E197", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E198", "edge_description": "HS-SH downwind bearings contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E199", "edge_description": "IMS-SH upwind bearing contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E200", "edge_description": "IMS-SH downwind bearings contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E201", "edge_description": "PLC upwind bearing contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E202", "edge_description": "Overheating contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E203", "edge_description": "Assembly damage contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E204", "edge_description": "Scuffing contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E205", "edge_description": "Dents contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E206", "edge_description": "Fretting corrosion contains_phm_task fault diagnosis"},
    {"edge_id": "ECSG5ICS_E208", "edge_description": "rolling bearing induces_problem limited data"},
    {"edge_id": "ECSG5ICS_E209", "edge_description": "rolling bearing induces_problem label noises"},
    {"edge_id": "ECSG5ICS_E210", "edge_description": "gearbox induces_problem limited data"},
    {"edge_id": "ECSG5ICS_E211", "edge_description": "gearbox induces_problem label noises"},
    {"edge_id": "ECSG5ICS_E212", "edge_description": "actual operating conditions induces_problem limited data"},
    {"edge_id": "ECSG5ICS_E213", "edge_description": "actual operating conditions induces_problem label noises"},
    {"edge_id": "ECSG5ICS_E214", "edge_description": "Single Severity induces_problem limited data"},
    {"edge_id": "ECSG5ICS_E215", "edge_description": "Single Severity induces_problem label noises"},
    {"edge_id": "ECSG5ICS_E216", "edge_description": "No Compound Fault induces_problem limited data"},
    {"edge_id": "ECSG5ICS_E217", "edge_description": "No Compound Fault induces_problem label noises"}
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
| 1 | `ECSG5ICS_E187` | `has_fault_mode` | 04-Fault Location | PLC upwind bearing |  | 05-Fault Mode | Assembly damage |  |
| 2 | `ECSG5ICS_E188` | `has_fault_mode` | 04-Fault Location | PLC upwind bearing |  | 05-Fault Mode | Scuffing |  |
| 3 | `ECSG5ICS_E189` | `has_fault_mode` | 04-Fault Location | PLC upwind bearing |  | 05-Fault Mode | Dents |  |
| 4 | `ECSG5ICS_E190` | `has_fault_mode` | 04-Fault Location | PLC upwind bearing |  | 05-Fault Mode | Fretting corrosion |  |
| 5 | `ECSG5ICS_E191` | `contains` | 05-Fault Mode | Overheating |  | 06-Fault Severity | Single Severity |  |
| 6 | `ECSG5ICS_E192` | `contains` | 05-Fault Mode | Assembly damage |  | 06-Fault Severity | Single Severity |  |
| 7 | `ECSG5ICS_E193` | `contains` | 05-Fault Mode | Scuffing |  | 06-Fault Severity | Single Severity |  |
| 8 | `ECSG5ICS_E194` | `contains` | 05-Fault Mode | Dents |  | 06-Fault Severity | Single Severity |  |
| 9 | `ECSG5ICS_E195` | `contains` | 05-Fault Mode | Fretting corrosion |  | 06-Fault Severity | Single Severity |  |
| 10 | `ECSG5ICS_E196` | `contains_phm_task` | 02-Object Type | rolling bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `ECSG5ICS_E197` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `ECSG5ICS_E198` | `contains_phm_task` | 04-Fault Location | HS-SH downwind bearings |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `ECSG5ICS_E199` | `contains_phm_task` | 04-Fault Location | IMS-SH upwind bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `ECSG5ICS_E200` | `contains_phm_task` | 04-Fault Location | IMS-SH downwind bearings |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `ECSG5ICS_E201` | `contains_phm_task` | 04-Fault Location | PLC upwind bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `ECSG5ICS_E202` | `contains_phm_task` | 05-Fault Mode | Overheating |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `ECSG5ICS_E203` | `contains_phm_task` | 05-Fault Mode | Assembly damage |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `ECSG5ICS_E204` | `contains_phm_task` | 05-Fault Mode | Scuffing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `ECSG5ICS_E205` | `contains_phm_task` | 05-Fault Mode | Dents |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `ECSG5ICS_E206` | `contains_phm_task` | 05-Fault Mode | Fretting corrosion |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `ECSG5ICS_E208` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | limited data(Small Fault Samples) |  |
| 22 | `ECSG5ICS_E209` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | label noises(Uncertainty) |  |
| 23 | `ECSG5ICS_E210` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | limited data(Small Fault Samples) |  |
| 24 | `ECSG5ICS_E211` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | label noises(Uncertainty) |  |
| 25 | `ECSG5ICS_E212` | `induces_problem` | 03-Operating Conditions | actual operating conditions(Variable Conditions) |  | 09-Problem Scenario | limited data(Small Fault Samples) |  |
| 26 | `ECSG5ICS_E213` | `induces_problem` | 03-Operating Conditions | actual operating conditions(Variable Conditions) |  | 09-Problem Scenario | label noises(Uncertainty) |  |
| 27 | `ECSG5ICS_E214` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | limited data(Small Fault Samples) |  |
| 28 | `ECSG5ICS_E215` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | label noises(Uncertainty) |  |
| 29 | `ECSG5ICS_E216` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | limited data(Small Fault Samples) |  |
| 30 | `ECSG5ICS_E217` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | label noises(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
