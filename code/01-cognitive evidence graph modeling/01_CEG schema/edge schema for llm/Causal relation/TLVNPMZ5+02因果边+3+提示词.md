# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TLVNPMZ5
- **Paper Title**：Intelligent Bearing Fault Diagnosis Method Combining Compressed Data Acquisition and Deep Learning
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `TLVNPMZ5`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TLVNPMZ5_E169", "edge_description": "yaw mechanism has_fault_mode pedestal loosening"},
    {"edge_id": "TLVNPMZ5_E170", "edge_description": "yaw mechanism has_fault_mode misalignment"},
    {"edge_id": "TLVNPMZ5_E171", "edge_description": "yaw mechanism has_fault_mode variation in airfoil of blades"},
    {"edge_id": "TLVNPMZ5_E172", "edge_description": "yaw mechanism has_fault_mode yaw fault"},
    {"edge_id": "TLVNPMZ5_E173", "edge_description": "pitting contains fault diameter, damage extent"},
    {"edge_id": "TLVNPMZ5_E174", "edge_description": "indentations contains fault diameter, damage extent"},
    {"edge_id": "TLVNPMZ5_E175", "edge_description": "pedestal loosening contains fault diameter, damage extent"},
    {"edge_id": "TLVNPMZ5_E176", "edge_description": "misalignment contains fault diameter, damage extent"},
    {"edge_id": "TLVNPMZ5_E177", "edge_description": "variation in airfoil of blades contains fault diameter, damage extent"},
    {"edge_id": "TLVNPMZ5_E178", "edge_description": "yaw fault contains fault diameter, damage extent"},
    {"edge_id": "TLVNPMZ5_E179", "edge_description": "wind turbine contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E180", "edge_description": "bearing contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E181", "edge_description": "bearing contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E182", "edge_description": "bearing pedestal contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E183", "edge_description": "rotor / shaft / coupling contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E184", "edge_description": "blade contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E185", "edge_description": "yaw mechanism contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E186", "edge_description": "pitting contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E187", "edge_description": "indentations contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E188", "edge_description": "pedestal loosening contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E189", "edge_description": "misalignment contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E190", "edge_description": "variation in airfoil of blades contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E191", "edge_description": "yaw fault contains_phm_task machinery fault diagnosis"},
    {"edge_id": "TLVNPMZ5_E193", "edge_description": "wind turbine induces_problem limited data / sparse target data"},
    {"edge_id": "TLVNPMZ5_E194", "edge_description": "wind turbine induces_problem distribution discrepancy / domain shift"},
    {"edge_id": "TLVNPMZ5_E195", "edge_description": "bearing induces_problem limited data / sparse target data"},
    {"edge_id": "TLVNPMZ5_E196", "edge_description": "bearing induces_problem distribution discrepancy / domain shift"},
    {"edge_id": "TLVNPMZ5_E197", "edge_description": "diverse working conditions induces_problem limited data / sparse target data"},
    {"edge_id": "TLVNPMZ5_E198", "edge_description": "diverse working conditions induces_problem distribution discrepancy / domain shift"},
    {"edge_id": "TLVNPMZ5_E199", "edge_description": "fault diameter, damage extent induces_problem limited data / sparse target data"}
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
| 1 | `TLVNPMZ5_E169` | `has_fault_mode` | 04-Fault Location | yaw mechanism |  | 05-Fault Mode | pedestal loosening |  |
| 2 | `TLVNPMZ5_E170` | `has_fault_mode` | 04-Fault Location | yaw mechanism |  | 05-Fault Mode | misalignment |  |
| 3 | `TLVNPMZ5_E171` | `has_fault_mode` | 04-Fault Location | yaw mechanism |  | 05-Fault Mode | variation in airfoil of blades |  |
| 4 | `TLVNPMZ5_E172` | `has_fault_mode` | 04-Fault Location | yaw mechanism |  | 05-Fault Mode | yaw fault |  |
| 5 | `TLVNPMZ5_E173` | `contains` | 05-Fault Mode | pitting |  | 06-Fault Severity | fault diameter, damage extent(Multiple Severities) |  |
| 6 | `TLVNPMZ5_E174` | `contains` | 05-Fault Mode | indentations |  | 06-Fault Severity | fault diameter, damage extent(Multiple Severities) |  |
| 7 | `TLVNPMZ5_E175` | `contains` | 05-Fault Mode | pedestal loosening |  | 06-Fault Severity | fault diameter, damage extent(Multiple Severities) |  |
| 8 | `TLVNPMZ5_E176` | `contains` | 05-Fault Mode | misalignment |  | 06-Fault Severity | fault diameter, damage extent(Multiple Severities) |  |
| 9 | `TLVNPMZ5_E177` | `contains` | 05-Fault Mode | variation in airfoil of blades |  | 06-Fault Severity | fault diameter, damage extent(Multiple Severities) |  |
| 10 | `TLVNPMZ5_E178` | `contains` | 05-Fault Mode | yaw fault |  | 06-Fault Severity | fault diameter, damage extent(Multiple Severities) |  |
| 11 | `TLVNPMZ5_E179` | `contains_phm_task` | 02-Object Type | wind turbine |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 12 | `TLVNPMZ5_E180` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 13 | `TLVNPMZ5_E181` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 14 | `TLVNPMZ5_E182` | `contains_phm_task` | 04-Fault Location | bearing pedestal |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 15 | `TLVNPMZ5_E183` | `contains_phm_task` | 04-Fault Location | rotor / shaft / coupling |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 16 | `TLVNPMZ5_E184` | `contains_phm_task` | 04-Fault Location | blade |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 17 | `TLVNPMZ5_E185` | `contains_phm_task` | 04-Fault Location | yaw mechanism |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 18 | `TLVNPMZ5_E186` | `contains_phm_task` | 05-Fault Mode | pitting |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 19 | `TLVNPMZ5_E187` | `contains_phm_task` | 05-Fault Mode | indentations |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 20 | `TLVNPMZ5_E188` | `contains_phm_task` | 05-Fault Mode | pedestal loosening |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 21 | `TLVNPMZ5_E189` | `contains_phm_task` | 05-Fault Mode | misalignment |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 22 | `TLVNPMZ5_E190` | `contains_phm_task` | 05-Fault Mode | variation in airfoil of blades |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 23 | `TLVNPMZ5_E191` | `contains_phm_task` | 05-Fault Mode | yaw fault |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 24 | `TLVNPMZ5_E193` | `induces_problem` | 02-Object Type | wind turbine |  | 09-Problem Scenario | limited data / sparse target data(Small Fault Samples) |  |
| 25 | `TLVNPMZ5_E194` | `induces_problem` | 02-Object Type | wind turbine |  | 09-Problem Scenario | distribution discrepancy / domain shift(Distribution Discrepancy) |  |
| 26 | `TLVNPMZ5_E195` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | limited data / sparse target data(Small Fault Samples) |  |
| 27 | `TLVNPMZ5_E196` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | distribution discrepancy / domain shift(Distribution Discrepancy) |  |
| 28 | `TLVNPMZ5_E197` | `induces_problem` | 03-Operating Conditions | diverse working conditions(Multiple Conditions) |  | 09-Problem Scenario | limited data / sparse target data(Small Fault Samples) |  |
| 29 | `TLVNPMZ5_E198` | `induces_problem` | 03-Operating Conditions | diverse working conditions(Multiple Conditions) |  | 09-Problem Scenario | distribution discrepancy / domain shift(Distribution Discrepancy) |  |
| 30 | `TLVNPMZ5_E199` | `induces_problem` | 06-Fault Severity | fault diameter, damage extent(Multiple Severities) |  | 09-Problem Scenario | limited data / sparse target data(Small Fault Samples) |  |

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
