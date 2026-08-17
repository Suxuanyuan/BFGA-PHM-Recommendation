# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：MIVICJ6P
- **Paper Title**：A new intelligent fault identification method based on transfer locality preserving projection for actual diagnosis scenario of rotating machinery
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `MIVICJ6P`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "MIVICJ6P_E127", "edge_description": "rolling element bearing has_fault_mode missing tooth"},
    {"edge_id": "MIVICJ6P_E128", "edge_description": "rolling element bearing has_fault_mode outer race fault"},
    {"edge_id": "MIVICJ6P_E129", "edge_description": "rolling element bearing has_fault_mode inner race fault"},
    {"edge_id": "MIVICJ6P_E130", "edge_description": "rolling element bearing has_fault_mode ball fault"},
    {"edge_id": "MIVICJ6P_E131", "edge_description": "chipped tooth contains 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault"},
    {"edge_id": "MIVICJ6P_E132", "edge_description": "missing tooth contains 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault"},
    {"edge_id": "MIVICJ6P_E133", "edge_description": "outer race fault contains 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault"},
    {"edge_id": "MIVICJ6P_E134", "edge_description": "inner race fault contains 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault"},
    {"edge_id": "MIVICJ6P_E135", "edge_description": "ball fault contains 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault"},
    {"edge_id": "MIVICJ6P_E136", "edge_description": "gearbox contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E137", "edge_description": "rolling element bearing contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E138", "edge_description": "helical gear contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E139", "edge_description": "rolling element bearing contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E140", "edge_description": "chipped tooth contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E141", "edge_description": "missing tooth contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E142", "edge_description": "outer race fault contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E143", "edge_description": "inner race fault contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E144", "edge_description": "ball fault contains_phm_task intelligent fault identification"},
    {"edge_id": "MIVICJ6P_E146", "edge_description": "gearbox induces_problem distribution discrepancy between different datasets / different operating conditions or other same-type machines"},
    {"edge_id": "MIVICJ6P_E147", "edge_description": "gearbox induces_problem inadequate information of target domain / only normal samples of target domain are available in training stage"},
    {"edge_id": "MIVICJ6P_E148", "edge_description": "rolling element bearing induces_problem distribution discrepancy between different datasets / different operating conditions or other same-type machines"},
    {"edge_id": "MIVICJ6P_E149", "edge_description": "rolling element bearing induces_problem inadequate information of target domain / only normal samples of target domain are available in training stage"},
    {"edge_id": "MIVICJ6P_E150", "edge_description": "different operating conditions (shaft speeds and loading conditions) induces_problem distribution discrepancy between different datasets / different operating conditions or other same-type machines"},
    {"edge_id": "MIVICJ6P_E151", "edge_description": "different operating conditions (shaft speeds and loading conditions) induces_problem inadequate information of target domain / only normal samples of target domain are available in training stage"},
    {"edge_id": "MIVICJ6P_E152", "edge_description": "0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault induces_problem distribution discrepancy between different datasets / different operating conditions or other same-type machines"},
    {"edge_id": "MIVICJ6P_E153", "edge_description": "0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault induces_problem inadequate information of target domain / only normal samples of target domain are available in training stage"},
    {"edge_id": "MIVICJ6P_E154", "edge_description": "No Compound Fault induces_problem distribution discrepancy between different datasets / different operating conditions or other same-type machines"},
    {"edge_id": "MIVICJ6P_E155", "edge_description": "No Compound Fault induces_problem inadequate information of target domain / only normal samples of target domain are available in training stage"},
    {"edge_id": "MIVICJ6P_E156", "edge_description": "intelligent fault identification induces_problem distribution discrepancy between different datasets / different operating conditions or other same-type machines"},
    {"edge_id": "MIVICJ6P_E157", "edge_description": "intelligent fault identification induces_problem inadequate information of target domain / only normal samples of target domain are available in training stage"}
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
| 1 | `MIVICJ6P_E127` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | missing tooth |  |
| 2 | `MIVICJ6P_E128` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | outer race fault |  |
| 3 | `MIVICJ6P_E129` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | inner race fault |  |
| 4 | `MIVICJ6P_E130` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | ball fault |  |
| 5 | `MIVICJ6P_E131` | `contains` | 05-Fault Mode | chipped tooth |  | 06-Fault Severity | 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault(Multiple Severities) |  |
| 6 | `MIVICJ6P_E132` | `contains` | 05-Fault Mode | missing tooth |  | 06-Fault Severity | 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault(Multiple Severities) |  |
| 7 | `MIVICJ6P_E133` | `contains` | 05-Fault Mode | outer race fault |  | 06-Fault Severity | 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault(Multiple Severities) |  |
| 8 | `MIVICJ6P_E134` | `contains` | 05-Fault Mode | inner race fault |  | 06-Fault Severity | 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault(Multiple Severities) |  |
| 9 | `MIVICJ6P_E135` | `contains` | 05-Fault Mode | ball fault |  | 06-Fault Severity | 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault(Multiple Severities) |  |
| 10 | `MIVICJ6P_E136` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 11 | `MIVICJ6P_E137` | `contains_phm_task` | 02-Object Type | rolling element bearing |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 12 | `MIVICJ6P_E138` | `contains_phm_task` | 04-Fault Location | helical gear |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 13 | `MIVICJ6P_E139` | `contains_phm_task` | 04-Fault Location | rolling element bearing |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 14 | `MIVICJ6P_E140` | `contains_phm_task` | 05-Fault Mode | chipped tooth |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 15 | `MIVICJ6P_E141` | `contains_phm_task` | 05-Fault Mode | missing tooth |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 16 | `MIVICJ6P_E142` | `contains_phm_task` | 05-Fault Mode | outer race fault |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 17 | `MIVICJ6P_E143` | `contains_phm_task` | 05-Fault Mode | inner race fault |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 18 | `MIVICJ6P_E144` | `contains_phm_task` | 05-Fault Mode | ball fault |  | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  |
| 19 | `MIVICJ6P_E146` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | distribution discrepancy between different datasets / different operating conditions or other same-type machines(Distribution Discrepancy) |  |
| 20 | `MIVICJ6P_E147` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | inadequate information of target domain / only normal samples of target domain are available in training stage(Small Fault Samples) |  |
| 21 | `MIVICJ6P_E148` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | distribution discrepancy between different datasets / different operating conditions or other same-type machines(Distribution Discrepancy) |  |
| 22 | `MIVICJ6P_E149` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | inadequate information of target domain / only normal samples of target domain are available in training stage(Small Fault Samples) |  |
| 23 | `MIVICJ6P_E150` | `induces_problem` | 03-Operating Conditions | different operating conditions (shaft speeds and loading conditions)(Multiple Conditions) |  | 09-Problem Scenario | distribution discrepancy between different datasets / different operating conditions or other same-type machines(Distribution Discrepancy) |  |
| 24 | `MIVICJ6P_E151` | `induces_problem` | 03-Operating Conditions | different operating conditions (shaft speeds and loading conditions)(Multiple Conditions) |  | 09-Problem Scenario | inadequate information of target domain / only normal samples of target domain are available in training stage(Small Fault Samples) |  |
| 25 | `MIVICJ6P_E152` | `induces_problem` | 06-Fault Severity | 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault(Multiple Severities) |  | 09-Problem Scenario | distribution discrepancy between different datasets / different operating conditions or other same-type machines(Distribution Discrepancy) |  |
| 26 | `MIVICJ6P_E153` | `induces_problem` | 06-Fault Severity | 0.18 mm, 0.36 mm, 0.53 mm, early fault, serious fault(Multiple Severities) |  | 09-Problem Scenario | inadequate information of target domain / only normal samples of target domain are available in training stage(Small Fault Samples) |  |
| 27 | `MIVICJ6P_E154` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | distribution discrepancy between different datasets / different operating conditions or other same-type machines(Distribution Discrepancy) |  |
| 28 | `MIVICJ6P_E155` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | inadequate information of target domain / only normal samples of target domain are available in training stage(Small Fault Samples) |  |
| 29 | `MIVICJ6P_E156` | `induces_problem` | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  | 09-Problem Scenario | distribution discrepancy between different datasets / different operating conditions or other same-type machines(Distribution Discrepancy) |  |
| 30 | `MIVICJ6P_E157` | `induces_problem` | 08-PHM Task | intelligent fault identification(Diagnosis Task) |  | 09-Problem Scenario | inadequate information of target domain / only normal samples of target domain are available in training stage(Small Fault Samples) |  |

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
