# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：BP9CZHH8
- **Paper Title**：A novel intelligent fault diagnosis method based on fast intrinsic component filtering and pseudo-normalization
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `BP9CZHH8`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "BP9CZHH8_E103", "edge_description": "bearings has_fault_mode outer race fault"},
    {"edge_id": "BP9CZHH8_E104", "edge_description": "bearings has_fault_mode inner race fault"},
    {"edge_id": "BP9CZHH8_E105", "edge_description": "bearings has_fault_mode roller fault"},
    {"edge_id": "BP9CZHH8_E106", "edge_description": "bearings has_fault_mode worn fault"},
    {"edge_id": "BP9CZHH8_E107", "edge_description": "bearings has_fault_mode broken tooth"},
    {"edge_id": "BP9CZHH8_E108", "edge_description": "planetary gear has_fault_mode outer race fault"},
    {"edge_id": "BP9CZHH8_E109", "edge_description": "planetary gear has_fault_mode inner race fault"},
    {"edge_id": "BP9CZHH8_E110", "edge_description": "planetary gear has_fault_mode roller fault"},
    {"edge_id": "BP9CZHH8_E111", "edge_description": "planetary gear has_fault_mode worn fault"},
    {"edge_id": "BP9CZHH8_E112", "edge_description": "planetary gear has_fault_mode broken tooth"},
    {"edge_id": "BP9CZHH8_E113", "edge_description": "outer race fault contains 0.18, 0.36, and 0.53 mm"},
    {"edge_id": "BP9CZHH8_E114", "edge_description": "inner race fault contains 0.18, 0.36, and 0.53 mm"},
    {"edge_id": "BP9CZHH8_E115", "edge_description": "roller fault contains 0.18, 0.36, and 0.53 mm"},
    {"edge_id": "BP9CZHH8_E116", "edge_description": "worn fault contains 0.18, 0.36, and 0.53 mm"},
    {"edge_id": "BP9CZHH8_E117", "edge_description": "broken tooth contains 0.18, 0.36, and 0.53 mm"},
    {"edge_id": "BP9CZHH8_E118", "edge_description": "rolling bearing contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E119", "edge_description": "planetary gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E120", "edge_description": "bearings contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E121", "edge_description": "planetary gear contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E122", "edge_description": "outer race fault contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E123", "edge_description": "inner race fault contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E124", "edge_description": "roller fault contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E125", "edge_description": "worn fault contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E126", "edge_description": "broken tooth contains_phm_task fault diagnosis"},
    {"edge_id": "BP9CZHH8_E128", "edge_description": "rolling bearing induces_problem lack of feature consistency and unequal feature contributions during testing"},
    {"edge_id": "BP9CZHH8_E129", "edge_description": "rolling bearing induces_problem compound fault diagnosis of planetary gearbox"},
    {"edge_id": "BP9CZHH8_E130", "edge_description": "planetary gearbox induces_problem lack of feature consistency and unequal feature contributions during testing"},
    {"edge_id": "BP9CZHH8_E131", "edge_description": "planetary gearbox induces_problem compound fault diagnosis of planetary gearbox"},
    {"edge_id": "BP9CZHH8_E132", "edge_description": "constant operating condition induces_problem lack of feature consistency and unequal feature contributions during testing"},
    {"edge_id": "BP9CZHH8_E133", "edge_description": "constant operating condition induces_problem compound fault diagnosis of planetary gearbox"}
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
| 1 | `BP9CZHH8_E103` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | outer race fault |  |
| 2 | `BP9CZHH8_E104` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | inner race fault |  |
| 3 | `BP9CZHH8_E105` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | roller fault |  |
| 4 | `BP9CZHH8_E106` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | worn fault |  |
| 5 | `BP9CZHH8_E107` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | broken tooth |  |
| 6 | `BP9CZHH8_E108` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | outer race fault |  |
| 7 | `BP9CZHH8_E109` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | inner race fault |  |
| 8 | `BP9CZHH8_E110` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | roller fault |  |
| 9 | `BP9CZHH8_E111` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | worn fault |  |
| 10 | `BP9CZHH8_E112` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | broken tooth |  |
| 11 | `BP9CZHH8_E113` | `contains` | 05-Fault Mode | outer race fault |  | 06-Fault Severity | 0.18, 0.36, and 0.53 mm(Multiple Severities) |  |
| 12 | `BP9CZHH8_E114` | `contains` | 05-Fault Mode | inner race fault |  | 06-Fault Severity | 0.18, 0.36, and 0.53 mm(Multiple Severities) |  |
| 13 | `BP9CZHH8_E115` | `contains` | 05-Fault Mode | roller fault |  | 06-Fault Severity | 0.18, 0.36, and 0.53 mm(Multiple Severities) |  |
| 14 | `BP9CZHH8_E116` | `contains` | 05-Fault Mode | worn fault |  | 06-Fault Severity | 0.18, 0.36, and 0.53 mm(Multiple Severities) |  |
| 15 | `BP9CZHH8_E117` | `contains` | 05-Fault Mode | broken tooth |  | 06-Fault Severity | 0.18, 0.36, and 0.53 mm(Multiple Severities) |  |
| 16 | `BP9CZHH8_E118` | `contains_phm_task` | 02-Object Type | rolling bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `BP9CZHH8_E119` | `contains_phm_task` | 02-Object Type | planetary gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `BP9CZHH8_E120` | `contains_phm_task` | 04-Fault Location | bearings |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `BP9CZHH8_E121` | `contains_phm_task` | 04-Fault Location | planetary gear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `BP9CZHH8_E122` | `contains_phm_task` | 05-Fault Mode | outer race fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `BP9CZHH8_E123` | `contains_phm_task` | 05-Fault Mode | inner race fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `BP9CZHH8_E124` | `contains_phm_task` | 05-Fault Mode | roller fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 23 | `BP9CZHH8_E125` | `contains_phm_task` | 05-Fault Mode | worn fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 24 | `BP9CZHH8_E126` | `contains_phm_task` | 05-Fault Mode | broken tooth |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 25 | `BP9CZHH8_E128` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | lack of feature consistency and unequal feature contributions during testing(Other) |  |
| 26 | `BP9CZHH8_E129` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | compound fault diagnosis of planetary gearbox(Compound Faults) |  |
| 27 | `BP9CZHH8_E130` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | lack of feature consistency and unequal feature contributions during testing(Other) |  |
| 28 | `BP9CZHH8_E131` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | compound fault diagnosis of planetary gearbox(Compound Faults) |  |
| 29 | `BP9CZHH8_E132` | `induces_problem` | 03-Operating Conditions | constant operating condition(Single Condition) |  | 09-Problem Scenario | lack of feature consistency and unequal feature contributions during testing(Other) |  |
| 30 | `BP9CZHH8_E133` | `induces_problem` | 03-Operating Conditions | constant operating condition(Single Condition) |  | 09-Problem Scenario | compound fault diagnosis of planetary gearbox(Compound Faults) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
