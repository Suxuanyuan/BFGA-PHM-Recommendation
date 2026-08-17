# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：UMI43QJH
- **Paper Title**：Intelligent fault diagnosis of planetary gearbox based on adaptive normalized CNN under complex variable working conditions and data imbalance
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `UMI43QJH`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "UMI43QJH_E165", "edge_description": "inner ring fault contains Single Severity"},
    {"edge_id": "UMI43QJH_E166", "edge_description": "outer ring fault contains Single Severity"},
    {"edge_id": "UMI43QJH_E167", "edge_description": "planetary gearbox contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E168", "edge_description": "planetary bearing contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E169", "edge_description": "sun gear contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E170", "edge_description": "planetary gear contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E171", "edge_description": "ring gear contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E172", "edge_description": "planetary bearing contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E173", "edge_description": "tooth root crack contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E174", "edge_description": "broken tooth contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E175", "edge_description": "missing tooth contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E176", "edge_description": "inner ring fault contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E177", "edge_description": "outer ring fault contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E179", "edge_description": "planetary gearbox induces_problem data imbalance"},
    {"edge_id": "UMI43QJH_E180", "edge_description": "planetary gearbox induces_problem distribution differences"},
    {"edge_id": "UMI43QJH_E181", "edge_description": "planetary gearbox induces_problem noise robustness"},
    {"edge_id": "UMI43QJH_E182", "edge_description": "planetary bearing induces_problem data imbalance"},
    {"edge_id": "UMI43QJH_E183", "edge_description": "planetary bearing induces_problem distribution differences"},
    {"edge_id": "UMI43QJH_E184", "edge_description": "planetary bearing induces_problem noise robustness"},
    {"edge_id": "UMI43QJH_E185", "edge_description": "complex variable working conditions (variable speed and variable load) induces_problem data imbalance"},
    {"edge_id": "UMI43QJH_E186", "edge_description": "complex variable working conditions (variable speed and variable load) induces_problem distribution differences"},
    {"edge_id": "UMI43QJH_E187", "edge_description": "complex variable working conditions (variable speed and variable load) induces_problem noise robustness"},
    {"edge_id": "UMI43QJH_E188", "edge_description": "Single Severity induces_problem data imbalance"},
    {"edge_id": "UMI43QJH_E189", "edge_description": "Single Severity induces_problem distribution differences"},
    {"edge_id": "UMI43QJH_E190", "edge_description": "Single Severity induces_problem noise robustness"},
    {"edge_id": "UMI43QJH_E191", "edge_description": "compound fault induces_problem data imbalance"},
    {"edge_id": "UMI43QJH_E192", "edge_description": "compound fault induces_problem distribution differences"},
    {"edge_id": "UMI43QJH_E193", "edge_description": "compound fault induces_problem noise robustness"},
    {"edge_id": "UMI43QJH_E194", "edge_description": "intelligent fault diagnosis induces_problem data imbalance"},
    {"edge_id": "UMI43QJH_E195", "edge_description": "intelligent fault diagnosis induces_problem distribution differences"}
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
| 1 | `UMI43QJH_E165` | `contains` | 05-Fault Mode | inner ring fault |  | 06-Fault Severity | Single Severity |  |
| 2 | `UMI43QJH_E166` | `contains` | 05-Fault Mode | outer ring fault |  | 06-Fault Severity | Single Severity |  |
| 3 | `UMI43QJH_E167` | `contains_phm_task` | 02-Object Type | planetary gearbox |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 4 | `UMI43QJH_E168` | `contains_phm_task` | 02-Object Type | planetary bearing |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 5 | `UMI43QJH_E169` | `contains_phm_task` | 04-Fault Location | sun gear |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 6 | `UMI43QJH_E170` | `contains_phm_task` | 04-Fault Location | planetary gear |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 7 | `UMI43QJH_E171` | `contains_phm_task` | 04-Fault Location | ring gear |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 8 | `UMI43QJH_E172` | `contains_phm_task` | 04-Fault Location | planetary bearing |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 9 | `UMI43QJH_E173` | `contains_phm_task` | 05-Fault Mode | tooth root crack |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 10 | `UMI43QJH_E174` | `contains_phm_task` | 05-Fault Mode | broken tooth |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 11 | `UMI43QJH_E175` | `contains_phm_task` | 05-Fault Mode | missing tooth |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 12 | `UMI43QJH_E176` | `contains_phm_task` | 05-Fault Mode | inner ring fault |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 13 | `UMI43QJH_E177` | `contains_phm_task` | 05-Fault Mode | outer ring fault |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 14 | `UMI43QJH_E179` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | data imbalance(Small Fault Samples) |  |
| 15 | `UMI43QJH_E180` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | distribution differences(Distribution Discrepancy) |  |
| 16 | `UMI43QJH_E181` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 17 | `UMI43QJH_E182` | `induces_problem` | 02-Object Type | planetary bearing |  | 09-Problem Scenario | data imbalance(Small Fault Samples) |  |
| 18 | `UMI43QJH_E183` | `induces_problem` | 02-Object Type | planetary bearing |  | 09-Problem Scenario | distribution differences(Distribution Discrepancy) |  |
| 19 | `UMI43QJH_E184` | `induces_problem` | 02-Object Type | planetary bearing |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 20 | `UMI43QJH_E185` | `induces_problem` | 03-Operating Conditions | complex variable working conditions (variable speed and variable load)(Variable Conditions) |  | 09-Problem Scenario | data imbalance(Small Fault Samples) |  |
| 21 | `UMI43QJH_E186` | `induces_problem` | 03-Operating Conditions | complex variable working conditions (variable speed and variable load)(Variable Conditions) |  | 09-Problem Scenario | distribution differences(Distribution Discrepancy) |  |
| 22 | `UMI43QJH_E187` | `induces_problem` | 03-Operating Conditions | complex variable working conditions (variable speed and variable load)(Variable Conditions) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 23 | `UMI43QJH_E188` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | data imbalance(Small Fault Samples) |  |
| 24 | `UMI43QJH_E189` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | distribution differences(Distribution Discrepancy) |  |
| 25 | `UMI43QJH_E190` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 26 | `UMI43QJH_E191` | `induces_problem` | 07-Compound Fault | compound fault(Compound Fault Across Structures) |  | 09-Problem Scenario | data imbalance(Small Fault Samples) |  |
| 27 | `UMI43QJH_E192` | `induces_problem` | 07-Compound Fault | compound fault(Compound Fault Across Structures) |  | 09-Problem Scenario | distribution differences(Distribution Discrepancy) |  |
| 28 | `UMI43QJH_E193` | `induces_problem` | 07-Compound Fault | compound fault(Compound Fault Across Structures) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 29 | `UMI43QJH_E194` | `induces_problem` | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | data imbalance(Small Fault Samples) |  |
| 30 | `UMI43QJH_E195` | `induces_problem` | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | distribution differences(Distribution Discrepancy) |  |

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
