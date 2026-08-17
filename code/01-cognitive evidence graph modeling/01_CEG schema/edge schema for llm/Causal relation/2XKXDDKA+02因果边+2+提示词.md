# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：2XKXDDKA
- **Paper Title**：Multi-source transfer learning network to complement knowledge for intelligent diagnosis of machines with unseen faults
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `2XKXDDKA`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "2XKXDDKA_E103", "edge_description": "crack contains Single Severity"},
    {"edge_id": "2XKXDDKA_E104", "edge_description": "wear contains Single Severity"},
    {"edge_id": "2XKXDDKA_E105", "edge_description": "chipped tooth contains Single Severity"},
    {"edge_id": "2XKXDDKA_E106", "edge_description": "spalling contains Single Severity"},
    {"edge_id": "2XKXDDKA_E107", "edge_description": "planetary gearbox contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E108", "edge_description": "roller element bearing contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E109", "edge_description": "planetary gearbox contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E110", "edge_description": "bearing contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E111", "edge_description": "crack contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E112", "edge_description": "wear contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E113", "edge_description": "chipped tooth contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E114", "edge_description": "spalling contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "2XKXDDKA_E116", "edge_description": "planetary gearbox induces_problem unseen faults"},
    {"edge_id": "2XKXDDKA_E117", "edge_description": "planetary gearbox induces_problem imbalanced target samples"},
    {"edge_id": "2XKXDDKA_E118", "edge_description": "planetary gearbox induces_problem multi-source transfer learning / distribution discrepancy"},
    {"edge_id": "2XKXDDKA_E119", "edge_description": "roller element bearing induces_problem unseen faults"},
    {"edge_id": "2XKXDDKA_E120", "edge_description": "roller element bearing induces_problem imbalanced target samples"},
    {"edge_id": "2XKXDDKA_E121", "edge_description": "roller element bearing induces_problem multi-source transfer learning / distribution discrepancy"},
    {"edge_id": "2XKXDDKA_E122", "edge_description": "different working conditions induces_problem unseen faults"},
    {"edge_id": "2XKXDDKA_E123", "edge_description": "different working conditions induces_problem imbalanced target samples"},
    {"edge_id": "2XKXDDKA_E124", "edge_description": "different working conditions induces_problem multi-source transfer learning / distribution discrepancy"},
    {"edge_id": "2XKXDDKA_E125", "edge_description": "Single Severity induces_problem unseen faults"},
    {"edge_id": "2XKXDDKA_E126", "edge_description": "Single Severity induces_problem imbalanced target samples"},
    {"edge_id": "2XKXDDKA_E127", "edge_description": "Single Severity induces_problem multi-source transfer learning / distribution discrepancy"},
    {"edge_id": "2XKXDDKA_E128", "edge_description": "No Compound Fault induces_problem unseen faults"},
    {"edge_id": "2XKXDDKA_E129", "edge_description": "No Compound Fault induces_problem imbalanced target samples"},
    {"edge_id": "2XKXDDKA_E130", "edge_description": "No Compound Fault induces_problem multi-source transfer learning / distribution discrepancy"},
    {"edge_id": "2XKXDDKA_E131", "edge_description": "intelligent fault diagnosis induces_problem unseen faults"},
    {"edge_id": "2XKXDDKA_E132", "edge_description": "intelligent fault diagnosis induces_problem imbalanced target samples"},
    {"edge_id": "2XKXDDKA_E133", "edge_description": "intelligent fault diagnosis induces_problem multi-source transfer learning / distribution discrepancy"}
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
| 1 | `2XKXDDKA_E103` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | Single Severity |  |
| 2 | `2XKXDDKA_E104` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | Single Severity |  |
| 3 | `2XKXDDKA_E105` | `contains` | 05-Fault Mode | chipped tooth |  | 06-Fault Severity | Single Severity |  |
| 4 | `2XKXDDKA_E106` | `contains` | 05-Fault Mode | spalling |  | 06-Fault Severity | Single Severity |  |
| 5 | `2XKXDDKA_E107` | `contains_phm_task` | 02-Object Type | planetary gearbox |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 6 | `2XKXDDKA_E108` | `contains_phm_task` | 02-Object Type | roller element bearing |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 7 | `2XKXDDKA_E109` | `contains_phm_task` | 04-Fault Location | planetary gearbox |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 8 | `2XKXDDKA_E110` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 9 | `2XKXDDKA_E111` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 10 | `2XKXDDKA_E112` | `contains_phm_task` | 05-Fault Mode | wear |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 11 | `2XKXDDKA_E113` | `contains_phm_task` | 05-Fault Mode | chipped tooth |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 12 | `2XKXDDKA_E114` | `contains_phm_task` | 05-Fault Mode | spalling |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 13 | `2XKXDDKA_E116` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | unseen faults(Zero Fault Samples) |  |
| 14 | `2XKXDDKA_E117` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | imbalanced target samples(Small Fault Samples) |  |
| 15 | `2XKXDDKA_E118` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | multi-source transfer learning / distribution discrepancy(Distribution Discrepancy) |  |
| 16 | `2XKXDDKA_E119` | `induces_problem` | 02-Object Type | roller element bearing |  | 09-Problem Scenario | unseen faults(Zero Fault Samples) |  |
| 17 | `2XKXDDKA_E120` | `induces_problem` | 02-Object Type | roller element bearing |  | 09-Problem Scenario | imbalanced target samples(Small Fault Samples) |  |
| 18 | `2XKXDDKA_E121` | `induces_problem` | 02-Object Type | roller element bearing |  | 09-Problem Scenario | multi-source transfer learning / distribution discrepancy(Distribution Discrepancy) |  |
| 19 | `2XKXDDKA_E122` | `induces_problem` | 03-Operating Conditions | different working conditions(Multiple Conditions) |  | 09-Problem Scenario | unseen faults(Zero Fault Samples) |  |
| 20 | `2XKXDDKA_E123` | `induces_problem` | 03-Operating Conditions | different working conditions(Multiple Conditions) |  | 09-Problem Scenario | imbalanced target samples(Small Fault Samples) |  |
| 21 | `2XKXDDKA_E124` | `induces_problem` | 03-Operating Conditions | different working conditions(Multiple Conditions) |  | 09-Problem Scenario | multi-source transfer learning / distribution discrepancy(Distribution Discrepancy) |  |
| 22 | `2XKXDDKA_E125` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | unseen faults(Zero Fault Samples) |  |
| 23 | `2XKXDDKA_E126` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | imbalanced target samples(Small Fault Samples) |  |
| 24 | `2XKXDDKA_E127` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | multi-source transfer learning / distribution discrepancy(Distribution Discrepancy) |  |
| 25 | `2XKXDDKA_E128` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | unseen faults(Zero Fault Samples) |  |
| 26 | `2XKXDDKA_E129` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | imbalanced target samples(Small Fault Samples) |  |
| 27 | `2XKXDDKA_E130` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | multi-source transfer learning / distribution discrepancy(Distribution Discrepancy) |  |
| 28 | `2XKXDDKA_E131` | `induces_problem` | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | unseen faults(Zero Fault Samples) |  |
| 29 | `2XKXDDKA_E132` | `induces_problem` | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | imbalanced target samples(Small Fault Samples) |  |
| 30 | `2XKXDDKA_E133` | `induces_problem` | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multi-source transfer learning / distribution discrepancy(Distribution Discrepancy) |  |

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
