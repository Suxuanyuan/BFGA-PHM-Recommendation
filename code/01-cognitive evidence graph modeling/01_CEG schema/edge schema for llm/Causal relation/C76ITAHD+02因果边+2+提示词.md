# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：C76ITAHD
- **Paper Title**：Fault Diagnosis of Wind Turbine Gearbox Using a Novel Method of Fast Deep Graph Convolutional Networks
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `C76ITAHD`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "C76ITAHD_E100", "edge_description": "gearbox has_fault_mode ball fault / inner raceway fault / outer raceway fault"},
    {"edge_id": "C76ITAHD_E101", "edge_description": "bearing has_fault_mode chipped tooth / missed tooth / broken teeth"},
    {"edge_id": "C76ITAHD_E102", "edge_description": "bearing has_fault_mode wear"},
    {"edge_id": "C76ITAHD_E103", "edge_description": "bearing has_fault_mode pitting"},
    {"edge_id": "C76ITAHD_E104", "edge_description": "bearing has_fault_mode eccentric"},
    {"edge_id": "C76ITAHD_E105", "edge_description": "bearing has_fault_mode ball fault / inner raceway fault / outer raceway fault"},
    {"edge_id": "C76ITAHD_E106", "edge_description": "chipped tooth / missed tooth / broken teeth contains Single Severity"},
    {"edge_id": "C76ITAHD_E107", "edge_description": "wear contains Single Severity"},
    {"edge_id": "C76ITAHD_E108", "edge_description": "pitting contains Single Severity"},
    {"edge_id": "C76ITAHD_E109", "edge_description": "eccentric contains Single Severity"},
    {"edge_id": "C76ITAHD_E110", "edge_description": "ball fault / inner raceway fault / outer raceway fault contains Single Severity"},
    {"edge_id": "C76ITAHD_E111", "edge_description": "wind turbine gearbox contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E112", "edge_description": "bearing contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E113", "edge_description": "gear contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E114", "edge_description": "gearbox contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E115", "edge_description": "bearing contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E116", "edge_description": "chipped tooth / missed tooth / broken teeth contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E117", "edge_description": "wear contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E118", "edge_description": "pitting contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E119", "edge_description": "eccentric contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E120", "edge_description": "ball fault / inner raceway fault / outer raceway fault contains_phm_task Fault diagnosis"},
    {"edge_id": "C76ITAHD_E122", "edge_description": "wind turbine gearbox induces_problem noise robustness"},
    {"edge_id": "C76ITAHD_E123", "edge_description": "wind turbine gearbox induces_problem overfitting and high training volume of GCNs"},
    {"edge_id": "C76ITAHD_E124", "edge_description": "bearing induces_problem noise robustness"},
    {"edge_id": "C76ITAHD_E125", "edge_description": "bearing induces_problem overfitting and high training volume of GCNs"},
    {"edge_id": "C76ITAHD_E126", "edge_description": "gear induces_problem noise robustness"},
    {"edge_id": "C76ITAHD_E127", "edge_description": "gear induces_problem overfitting and high training volume of GCNs"},
    {"edge_id": "C76ITAHD_E128", "edge_description": "1200 r/min induces_problem noise robustness"},
    {"edge_id": "C76ITAHD_E129", "edge_description": "1200 r/min induces_problem overfitting and high training volume of GCNs"},
    {"edge_id": "C76ITAHD_E130", "edge_description": "Single Severity induces_problem noise robustness"}
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
| 1 | `C76ITAHD_E100` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | ball fault / inner raceway fault / outer raceway fault |  |
| 2 | `C76ITAHD_E101` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | chipped tooth / missed tooth / broken teeth |  |
| 3 | `C76ITAHD_E102` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | wear |  |
| 4 | `C76ITAHD_E103` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | pitting |  |
| 5 | `C76ITAHD_E104` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | eccentric |  |
| 6 | `C76ITAHD_E105` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | ball fault / inner raceway fault / outer raceway fault |  |
| 7 | `C76ITAHD_E106` | `contains` | 05-Fault Mode | chipped tooth / missed tooth / broken teeth |  | 06-Fault Severity | Single Severity |  |
| 8 | `C76ITAHD_E107` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | Single Severity |  |
| 9 | `C76ITAHD_E108` | `contains` | 05-Fault Mode | pitting |  | 06-Fault Severity | Single Severity |  |
| 10 | `C76ITAHD_E109` | `contains` | 05-Fault Mode | eccentric |  | 06-Fault Severity | Single Severity |  |
| 11 | `C76ITAHD_E110` | `contains` | 05-Fault Mode | ball fault / inner raceway fault / outer raceway fault |  | 06-Fault Severity | Single Severity |  |
| 12 | `C76ITAHD_E111` | `contains_phm_task` | 02-Object Type | wind turbine gearbox |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 13 | `C76ITAHD_E112` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 14 | `C76ITAHD_E113` | `contains_phm_task` | 02-Object Type | gear |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 15 | `C76ITAHD_E114` | `contains_phm_task` | 04-Fault Location | gearbox |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 16 | `C76ITAHD_E115` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 17 | `C76ITAHD_E116` | `contains_phm_task` | 05-Fault Mode | chipped tooth / missed tooth / broken teeth |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 18 | `C76ITAHD_E117` | `contains_phm_task` | 05-Fault Mode | wear |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 19 | `C76ITAHD_E118` | `contains_phm_task` | 05-Fault Mode | pitting |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 20 | `C76ITAHD_E119` | `contains_phm_task` | 05-Fault Mode | eccentric |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 21 | `C76ITAHD_E120` | `contains_phm_task` | 05-Fault Mode | ball fault / inner raceway fault / outer raceway fault |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 22 | `C76ITAHD_E122` | `induces_problem` | 02-Object Type | wind turbine gearbox |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 23 | `C76ITAHD_E123` | `induces_problem` | 02-Object Type | wind turbine gearbox |  | 09-Problem Scenario | overfitting and high training volume of GCNs(Other) |  |
| 24 | `C76ITAHD_E124` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 25 | `C76ITAHD_E125` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | overfitting and high training volume of GCNs(Other) |  |
| 26 | `C76ITAHD_E126` | `induces_problem` | 02-Object Type | gear |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 27 | `C76ITAHD_E127` | `induces_problem` | 02-Object Type | gear |  | 09-Problem Scenario | overfitting and high training volume of GCNs(Other) |  |
| 28 | `C76ITAHD_E128` | `induces_problem` | 03-Operating Conditions | 1200 r/min(Single Condition) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 29 | `C76ITAHD_E129` | `induces_problem` | 03-Operating Conditions | 1200 r/min(Single Condition) |  | 09-Problem Scenario | overfitting and high training volume of GCNs(Other) |  |
| 30 | `C76ITAHD_E130` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |

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
