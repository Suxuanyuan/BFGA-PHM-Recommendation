# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：BQWYTHIR
- **Paper Title**：Classifier Inconsistency-Based Domain Adaptation Network for Partial Transfer Intelligent Diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `BQWYTHIR`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "BQWYTHIR_E103", "edge_description": "planet gear has_fault_mode surface pitting"},
    {"edge_id": "BQWYTHIR_E104", "edge_description": "planet gear has_fault_mode surface corrosion"},
    {"edge_id": "BQWYTHIR_E105", "edge_description": "planet gear has_fault_mode inner race fault, outer race fault, roller fault"},
    {"edge_id": "BQWYTHIR_E106", "edge_description": "rolling bearing has_fault_mode tooth crack"},
    {"edge_id": "BQWYTHIR_E107", "edge_description": "rolling bearing has_fault_mode tooth spalling, surface spalling"},
    {"edge_id": "BQWYTHIR_E108", "edge_description": "rolling bearing has_fault_mode tooth wear"},
    {"edge_id": "BQWYTHIR_E109", "edge_description": "rolling bearing has_fault_mode mild tooth broken, sever tooth broken"},
    {"edge_id": "BQWYTHIR_E110", "edge_description": "rolling bearing has_fault_mode surface pitting"},
    {"edge_id": "BQWYTHIR_E111", "edge_description": "rolling bearing has_fault_mode surface corrosion"},
    {"edge_id": "BQWYTHIR_E112", "edge_description": "rolling bearing has_fault_mode inner race fault, outer race fault, roller fault"},
    {"edge_id": "BQWYTHIR_E113", "edge_description": "tooth crack contains mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils"},
    {"edge_id": "BQWYTHIR_E114", "edge_description": "tooth spalling, surface spalling contains mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils"},
    {"edge_id": "BQWYTHIR_E115", "edge_description": "tooth wear contains mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils"},
    {"edge_id": "BQWYTHIR_E116", "edge_description": "mild tooth broken, sever tooth broken contains mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils"},
    {"edge_id": "BQWYTHIR_E117", "edge_description": "surface pitting contains mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils"},
    {"edge_id": "BQWYTHIR_E118", "edge_description": "surface corrosion contains mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils"},
    {"edge_id": "BQWYTHIR_E119", "edge_description": "inner race fault, outer race fault, roller fault contains mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils"},
    {"edge_id": "BQWYTHIR_E120", "edge_description": "planetary gearbox contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E121", "edge_description": "rolling bearing contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E122", "edge_description": "planet gear contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E123", "edge_description": "rolling bearing contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E124", "edge_description": "tooth crack contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E125", "edge_description": "tooth spalling, surface spalling contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E126", "edge_description": "tooth wear contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E127", "edge_description": "mild tooth broken, sever tooth broken contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E128", "edge_description": "surface pitting contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E129", "edge_description": "surface corrosion contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E130", "edge_description": "inner race fault, outer race fault, roller fault contains_phm_task intelligent fault diagnosis"},
    {"edge_id": "BQWYTHIR_E132", "edge_description": "planetary gearbox induces_problem unsupervised partial transfer diagnosis (UPTD)"},
    {"edge_id": "BQWYTHIR_E133", "edge_description": "planetary gearbox induces_problem environment noise robustness"}
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
| 1 | `BQWYTHIR_E103` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | surface pitting |  |
| 2 | `BQWYTHIR_E104` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | surface corrosion |  |
| 3 | `BQWYTHIR_E105` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | inner race fault, outer race fault, roller fault |  |
| 4 | `BQWYTHIR_E106` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | tooth crack |  |
| 5 | `BQWYTHIR_E107` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | tooth spalling, surface spalling |  |
| 6 | `BQWYTHIR_E108` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | tooth wear |  |
| 7 | `BQWYTHIR_E109` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | mild tooth broken, sever tooth broken |  |
| 8 | `BQWYTHIR_E110` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | surface pitting |  |
| 9 | `BQWYTHIR_E111` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | surface corrosion |  |
| 10 | `BQWYTHIR_E112` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | inner race fault, outer race fault, roller fault |  |
| 11 | `BQWYTHIR_E113` | `contains` | 05-Fault Mode | tooth crack |  | 06-Fault Severity | mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils(Multiple Severities) |  |
| 12 | `BQWYTHIR_E114` | `contains` | 05-Fault Mode | tooth spalling, surface spalling |  | 06-Fault Severity | mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils(Multiple Severities) |  |
| 13 | `BQWYTHIR_E115` | `contains` | 05-Fault Mode | tooth wear |  | 06-Fault Severity | mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils(Multiple Severities) |  |
| 14 | `BQWYTHIR_E116` | `contains` | 05-Fault Mode | mild tooth broken, sever tooth broken |  | 06-Fault Severity | mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils(Multiple Severities) |  |
| 15 | `BQWYTHIR_E117` | `contains` | 05-Fault Mode | surface pitting |  | 06-Fault Severity | mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils(Multiple Severities) |  |
| 16 | `BQWYTHIR_E118` | `contains` | 05-Fault Mode | surface corrosion |  | 06-Fault Severity | mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils(Multiple Severities) |  |
| 17 | `BQWYTHIR_E119` | `contains` | 05-Fault Mode | inner race fault, outer race fault, roller fault |  | 06-Fault Severity | mild tooth broken, sever tooth broken, 7mils, 14mils, 21mils(Multiple Severities) |  |
| 18 | `BQWYTHIR_E120` | `contains_phm_task` | 02-Object Type | planetary gearbox |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 19 | `BQWYTHIR_E121` | `contains_phm_task` | 02-Object Type | rolling bearing |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 20 | `BQWYTHIR_E122` | `contains_phm_task` | 04-Fault Location | planet gear |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 21 | `BQWYTHIR_E123` | `contains_phm_task` | 04-Fault Location | rolling bearing |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 22 | `BQWYTHIR_E124` | `contains_phm_task` | 05-Fault Mode | tooth crack |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 23 | `BQWYTHIR_E125` | `contains_phm_task` | 05-Fault Mode | tooth spalling, surface spalling |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 24 | `BQWYTHIR_E126` | `contains_phm_task` | 05-Fault Mode | tooth wear |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 25 | `BQWYTHIR_E127` | `contains_phm_task` | 05-Fault Mode | mild tooth broken, sever tooth broken |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 26 | `BQWYTHIR_E128` | `contains_phm_task` | 05-Fault Mode | surface pitting |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 27 | `BQWYTHIR_E129` | `contains_phm_task` | 05-Fault Mode | surface corrosion |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 28 | `BQWYTHIR_E130` | `contains_phm_task` | 05-Fault Mode | inner race fault, outer race fault, roller fault |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 29 | `BQWYTHIR_E132` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | unsupervised partial transfer diagnosis (UPTD)(Distribution Discrepancy) |  |
| 30 | `BQWYTHIR_E133` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | environment noise robustness(Uncertainty) |  |

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
