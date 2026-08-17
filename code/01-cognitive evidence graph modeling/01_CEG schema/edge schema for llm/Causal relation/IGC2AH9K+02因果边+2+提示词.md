# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：IGC2AH9K
- **Paper Title**：Application of small sample virtual expansion and spherical mapping model in wind turbine fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `IGC2AH9K`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "IGC2AH9K_E120", "edge_description": "gearbox has_fault_mode rolling element failure"},
    {"edge_id": "IGC2AH9K_E121", "edge_description": "end bearing has_fault_mode gear wear"},
    {"edge_id": "IGC2AH9K_E122", "edge_description": "end bearing has_fault_mode gear pitting"},
    {"edge_id": "IGC2AH9K_E123", "edge_description": "end bearing has_fault_mode tooth breakage"},
    {"edge_id": "IGC2AH9K_E124", "edge_description": "end bearing has_fault_mode bearing inner ring failure"},
    {"edge_id": "IGC2AH9K_E125", "edge_description": "end bearing has_fault_mode bearing outer ring failure"},
    {"edge_id": "IGC2AH9K_E126", "edge_description": "end bearing has_fault_mode cage failure"},
    {"edge_id": "IGC2AH9K_E127", "edge_description": "end bearing has_fault_mode rolling element failure"},
    {"edge_id": "IGC2AH9K_E128", "edge_description": "gear wear contains Single Severity"},
    {"edge_id": "IGC2AH9K_E129", "edge_description": "gear pitting contains Single Severity"},
    {"edge_id": "IGC2AH9K_E130", "edge_description": "tooth breakage contains Single Severity"},
    {"edge_id": "IGC2AH9K_E131", "edge_description": "bearing inner ring failure contains Single Severity"},
    {"edge_id": "IGC2AH9K_E132", "edge_description": "bearing outer ring failure contains Single Severity"},
    {"edge_id": "IGC2AH9K_E133", "edge_description": "cage failure contains Single Severity"},
    {"edge_id": "IGC2AH9K_E134", "edge_description": "rolling element failure contains Single Severity"},
    {"edge_id": "IGC2AH9K_E135", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E136", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E137", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E138", "edge_description": "end bearing contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E139", "edge_description": "gear wear contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E140", "edge_description": "gear pitting contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E141", "edge_description": "tooth breakage contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E142", "edge_description": "bearing inner ring failure contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E143", "edge_description": "bearing outer ring failure contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E144", "edge_description": "cage failure contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E145", "edge_description": "rolling element failure contains_phm_task fault diagnosis"},
    {"edge_id": "IGC2AH9K_E147", "edge_description": "gearbox induces_problem small sample"},
    {"edge_id": "IGC2AH9K_E148", "edge_description": "bearing induces_problem small sample"},
    {"edge_id": "IGC2AH9K_E149", "edge_description": "different wind speeds induces_problem small sample"},
    {"edge_id": "IGC2AH9K_E150", "edge_description": "Single Severity induces_problem small sample"}
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
| 1 | `IGC2AH9K_E120` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | rolling element failure |  |
| 2 | `IGC2AH9K_E121` | `has_fault_mode` | 04-Fault Location | end bearing |  | 05-Fault Mode | gear wear |  |
| 3 | `IGC2AH9K_E122` | `has_fault_mode` | 04-Fault Location | end bearing |  | 05-Fault Mode | gear pitting |  |
| 4 | `IGC2AH9K_E123` | `has_fault_mode` | 04-Fault Location | end bearing |  | 05-Fault Mode | tooth breakage |  |
| 5 | `IGC2AH9K_E124` | `has_fault_mode` | 04-Fault Location | end bearing |  | 05-Fault Mode | bearing inner ring failure |  |
| 6 | `IGC2AH9K_E125` | `has_fault_mode` | 04-Fault Location | end bearing |  | 05-Fault Mode | bearing outer ring failure |  |
| 7 | `IGC2AH9K_E126` | `has_fault_mode` | 04-Fault Location | end bearing |  | 05-Fault Mode | cage failure |  |
| 8 | `IGC2AH9K_E127` | `has_fault_mode` | 04-Fault Location | end bearing |  | 05-Fault Mode | rolling element failure |  |
| 9 | `IGC2AH9K_E128` | `contains` | 05-Fault Mode | gear wear |  | 06-Fault Severity | Single Severity |  |
| 10 | `IGC2AH9K_E129` | `contains` | 05-Fault Mode | gear pitting |  | 06-Fault Severity | Single Severity |  |
| 11 | `IGC2AH9K_E130` | `contains` | 05-Fault Mode | tooth breakage |  | 06-Fault Severity | Single Severity |  |
| 12 | `IGC2AH9K_E131` | `contains` | 05-Fault Mode | bearing inner ring failure |  | 06-Fault Severity | Single Severity |  |
| 13 | `IGC2AH9K_E132` | `contains` | 05-Fault Mode | bearing outer ring failure |  | 06-Fault Severity | Single Severity |  |
| 14 | `IGC2AH9K_E133` | `contains` | 05-Fault Mode | cage failure |  | 06-Fault Severity | Single Severity |  |
| 15 | `IGC2AH9K_E134` | `contains` | 05-Fault Mode | rolling element failure |  | 06-Fault Severity | Single Severity |  |
| 16 | `IGC2AH9K_E135` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `IGC2AH9K_E136` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `IGC2AH9K_E137` | `contains_phm_task` | 04-Fault Location | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `IGC2AH9K_E138` | `contains_phm_task` | 04-Fault Location | end bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `IGC2AH9K_E139` | `contains_phm_task` | 05-Fault Mode | gear wear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `IGC2AH9K_E140` | `contains_phm_task` | 05-Fault Mode | gear pitting |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `IGC2AH9K_E141` | `contains_phm_task` | 05-Fault Mode | tooth breakage |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 23 | `IGC2AH9K_E142` | `contains_phm_task` | 05-Fault Mode | bearing inner ring failure |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 24 | `IGC2AH9K_E143` | `contains_phm_task` | 05-Fault Mode | bearing outer ring failure |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 25 | `IGC2AH9K_E144` | `contains_phm_task` | 05-Fault Mode | cage failure |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 26 | `IGC2AH9K_E145` | `contains_phm_task` | 05-Fault Mode | rolling element failure |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 27 | `IGC2AH9K_E147` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | small sample(Small Fault Samples) |  |
| 28 | `IGC2AH9K_E148` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | small sample(Small Fault Samples) |  |
| 29 | `IGC2AH9K_E149` | `induces_problem` | 03-Operating Conditions | different wind speeds(Multiple Conditions) |  | 09-Problem Scenario | small sample(Small Fault Samples) |  |
| 30 | `IGC2AH9K_E150` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | small sample(Small Fault Samples) |  |

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
