# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WFFU6EZP
- **Paper Title**：Fault diagnosis for a solar assisted heat pump system under incomplete data and expert knowledge
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `WFFU6EZP`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WFFU6EZP_E139", "edge_description": "refrigerant circuit has_fault_mode fouling of the evaporator"},
    {"edge_id": "WFFU6EZP_E140", "edge_description": "refrigerant circuit has_fault_mode excessive lift of expansion valve"},
    {"edge_id": "WFFU6EZP_E141", "edge_description": "refrigerant circuit has_fault_mode blocking of liquid pipeline"},
    {"edge_id": "WFFU6EZP_E142", "edge_description": "refrigerant leakage contains Single Severity"},
    {"edge_id": "WFFU6EZP_E143", "edge_description": "refrigerant overcharge contains Single Severity"},
    {"edge_id": "WFFU6EZP_E144", "edge_description": "fouling of the condenser contains Single Severity"},
    {"edge_id": "WFFU6EZP_E145", "edge_description": "fouling of the evaporator contains Single Severity"},
    {"edge_id": "WFFU6EZP_E146", "edge_description": "excessive lift of expansion valve contains Single Severity"},
    {"edge_id": "WFFU6EZP_E147", "edge_description": "blocking of liquid pipeline contains Single Severity"},
    {"edge_id": "WFFU6EZP_E149", "edge_description": "condenser contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E150", "edge_description": "evaporator contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E151", "edge_description": "expansion valve contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E152", "edge_description": "liquid pipeline contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E153", "edge_description": "refrigerant circuit contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E154", "edge_description": "refrigerant leakage contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E155", "edge_description": "refrigerant overcharge contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E156", "edge_description": "fouling of the condenser contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E157", "edge_description": "fouling of the evaporator contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E158", "edge_description": "excessive lift of expansion valve contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E159", "edge_description": "blocking of liquid pipeline contains_phm_task fault diagnosis"},
    {"edge_id": "WFFU6EZP_E161", "edge_description": "solar assisted heat pump system induces_problem incomplete data and incomplete expert knowledge"},
    {"edge_id": "WFFU6EZP_E162", "edge_description": "solar assisted heat pump system induces_problem parameter learning under incomplete data"},
    {"edge_id": "WFFU6EZP_E163", "edge_description": "incomplete simulation data induces_problem incomplete data and incomplete expert knowledge"},
    {"edge_id": "WFFU6EZP_E164", "edge_description": "incomplete simulation data induces_problem parameter learning under incomplete data"},
    {"edge_id": "WFFU6EZP_E165", "edge_description": "Single Severity induces_problem incomplete data and incomplete expert knowledge"},
    {"edge_id": "WFFU6EZP_E166", "edge_description": "Single Severity induces_problem parameter learning under incomplete data"},
    {"edge_id": "WFFU6EZP_E167", "edge_description": "No Compound Fault induces_problem incomplete data and incomplete expert knowledge"},
    {"edge_id": "WFFU6EZP_E168", "edge_description": "No Compound Fault induces_problem parameter learning under incomplete data"},
    {"edge_id": "WFFU6EZP_E169", "edge_description": "fault diagnosis induces_problem incomplete data and incomplete expert knowledge"},
    {"edge_id": "WFFU6EZP_E170", "edge_description": "fault diagnosis induces_problem parameter learning under incomplete data"}
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
| 1 | `WFFU6EZP_E139` | `has_fault_mode` | 04-Fault Location | refrigerant circuit |  | 05-Fault Mode | fouling of the evaporator |  |
| 2 | `WFFU6EZP_E140` | `has_fault_mode` | 04-Fault Location | refrigerant circuit |  | 05-Fault Mode | excessive lift of expansion valve |  |
| 3 | `WFFU6EZP_E141` | `has_fault_mode` | 04-Fault Location | refrigerant circuit |  | 05-Fault Mode | blocking of liquid pipeline |  |
| 4 | `WFFU6EZP_E142` | `contains` | 05-Fault Mode | refrigerant leakage |  | 06-Fault Severity | Single Severity |  |
| 5 | `WFFU6EZP_E143` | `contains` | 05-Fault Mode | refrigerant overcharge |  | 06-Fault Severity | Single Severity |  |
| 6 | `WFFU6EZP_E144` | `contains` | 05-Fault Mode | fouling of the condenser |  | 06-Fault Severity | Single Severity |  |
| 7 | `WFFU6EZP_E145` | `contains` | 05-Fault Mode | fouling of the evaporator |  | 06-Fault Severity | Single Severity |  |
| 8 | `WFFU6EZP_E146` | `contains` | 05-Fault Mode | excessive lift of expansion valve |  | 06-Fault Severity | Single Severity |  |
| 9 | `WFFU6EZP_E147` | `contains` | 05-Fault Mode | blocking of liquid pipeline |  | 06-Fault Severity | Single Severity |  |
| 10 | `WFFU6EZP_E149` | `contains_phm_task` | 04-Fault Location | condenser |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `WFFU6EZP_E150` | `contains_phm_task` | 04-Fault Location | evaporator |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `WFFU6EZP_E151` | `contains_phm_task` | 04-Fault Location | expansion valve |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `WFFU6EZP_E152` | `contains_phm_task` | 04-Fault Location | liquid pipeline |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `WFFU6EZP_E153` | `contains_phm_task` | 04-Fault Location | refrigerant circuit |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `WFFU6EZP_E154` | `contains_phm_task` | 05-Fault Mode | refrigerant leakage |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `WFFU6EZP_E155` | `contains_phm_task` | 05-Fault Mode | refrigerant overcharge |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `WFFU6EZP_E156` | `contains_phm_task` | 05-Fault Mode | fouling of the condenser |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `WFFU6EZP_E157` | `contains_phm_task` | 05-Fault Mode | fouling of the evaporator |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `WFFU6EZP_E158` | `contains_phm_task` | 05-Fault Mode | excessive lift of expansion valve |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `WFFU6EZP_E159` | `contains_phm_task` | 05-Fault Mode | blocking of liquid pipeline |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `WFFU6EZP_E161` | `induces_problem` | 02-Object Type | solar assisted heat pump system |  | 09-Problem Scenario | incomplete data and incomplete expert knowledge(Uncertainty) |  |
| 22 | `WFFU6EZP_E162` | `induces_problem` | 02-Object Type | solar assisted heat pump system |  | 09-Problem Scenario | parameter learning under incomplete data(Other) |  |
| 23 | `WFFU6EZP_E163` | `induces_problem` | 03-Operating Conditions | incomplete simulation data(Single Condition) |  | 09-Problem Scenario | incomplete data and incomplete expert knowledge(Uncertainty) |  |
| 24 | `WFFU6EZP_E164` | `induces_problem` | 03-Operating Conditions | incomplete simulation data(Single Condition) |  | 09-Problem Scenario | parameter learning under incomplete data(Other) |  |
| 25 | `WFFU6EZP_E165` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | incomplete data and incomplete expert knowledge(Uncertainty) |  |
| 26 | `WFFU6EZP_E166` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | parameter learning under incomplete data(Other) |  |
| 27 | `WFFU6EZP_E167` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | incomplete data and incomplete expert knowledge(Uncertainty) |  |
| 28 | `WFFU6EZP_E168` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | parameter learning under incomplete data(Other) |  |
| 29 | `WFFU6EZP_E169` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | incomplete data and incomplete expert knowledge(Uncertainty) |  |
| 30 | `WFFU6EZP_E170` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | parameter learning under incomplete data(Other) |  |

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
