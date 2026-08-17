# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PRKTNAZI
- **Paper Title**：Domain Adversarial Transfer Network for Cross-Domain Fault Diagnosis of Rotary Machinery
- **Number of Candidate Edges to Judge**：25 

---

## II. LLM Input

> **Input Material**: Reference ID `PRKTNAZI`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PRKTNAZI_E092", "edge_description": "rolling element bearing induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E093", "edge_description": "gearbox induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E094", "edge_description": "gearbox induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E095", "edge_description": "gearbox induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E096", "edge_description": "operating conditions induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E097", "edge_description": "operating conditions induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E098", "edge_description": "operating conditions induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E099", "edge_description": "defect diameters of 0.5 mm and 2 mm, 0.2mm defect induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E100", "edge_description": "defect diameters of 0.5 mm and 2 mm, 0.2mm defect induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E101", "edge_description": "defect diameters of 0.5 mm and 2 mm, 0.2mm defect induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E102", "edge_description": "compound faults combining gears and bearings induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E103", "edge_description": "compound faults combining gears and bearings induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E104", "edge_description": "compound faults combining gears and bearings induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E105", "edge_description": "fault diagnosis induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E106", "edge_description": "fault diagnosis induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E107", "edge_description": "fault diagnosis induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E108", "edge_description": "labelled source samples and unlabeled target samples induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E109", "edge_description": "labelled source samples and unlabeled target samples induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E110", "edge_description": "labelled source samples and unlabeled target samples induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E111", "edge_description": "Gaussian white noise induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E112", "edge_description": "Gaussian white noise induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E113", "edge_description": "Gaussian white noise induces_problem compound faults"},
    {"edge_id": "PRKTNAZI_E114", "edge_description": "computation cost in the training stage induces_problem domain shift / distribution discrepancy"},
    {"edge_id": "PRKTNAZI_E115", "edge_description": "computation cost in the training stage induces_problem noise contamination"},
    {"edge_id": "PRKTNAZI_E116", "edge_description": "computation cost in the training stage induces_problem compound faults"}
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
| 1 | `PRKTNAZI_E092` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 2 | `PRKTNAZI_E093` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 3 | `PRKTNAZI_E094` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 4 | `PRKTNAZI_E095` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 5 | `PRKTNAZI_E096` | `induces_problem` | 03-Operating Conditions | operating conditions(Multiple Conditions) |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 6 | `PRKTNAZI_E097` | `induces_problem` | 03-Operating Conditions | operating conditions(Multiple Conditions) |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 7 | `PRKTNAZI_E098` | `induces_problem` | 03-Operating Conditions | operating conditions(Multiple Conditions) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 8 | `PRKTNAZI_E099` | `induces_problem` | 06-Fault Severity | defect diameters of 0.5 mm and 2 mm, 0.2mm defect(Multiple Severities) |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 9 | `PRKTNAZI_E100` | `induces_problem` | 06-Fault Severity | defect diameters of 0.5 mm and 2 mm, 0.2mm defect(Multiple Severities) |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 10 | `PRKTNAZI_E101` | `induces_problem` | 06-Fault Severity | defect diameters of 0.5 mm and 2 mm, 0.2mm defect(Multiple Severities) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 11 | `PRKTNAZI_E102` | `induces_problem` | 07-Compound Fault | compound faults combining gears and bearings(Compound Fault Across Structures) |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 12 | `PRKTNAZI_E103` | `induces_problem` | 07-Compound Fault | compound faults combining gears and bearings(Compound Fault Across Structures) |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 13 | `PRKTNAZI_E104` | `induces_problem` | 07-Compound Fault | compound faults combining gears and bearings(Compound Fault Across Structures) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 14 | `PRKTNAZI_E105` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 15 | `PRKTNAZI_E106` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 16 | `PRKTNAZI_E107` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 17 | `PRKTNAZI_E108` | `induces_problem` | 12-Training Data Availability | labelled source samples and unlabeled target samples(Sufficient) |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 18 | `PRKTNAZI_E109` | `induces_problem` | 12-Training Data Availability | labelled source samples and unlabeled target samples(Sufficient) |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 19 | `PRKTNAZI_E110` | `induces_problem` | 12-Training Data Availability | labelled source samples and unlabeled target samples(Sufficient) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 20 | `PRKTNAZI_E111` | `induces_problem` | 13-Noise Level | Gaussian white noise(High Noise) |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 21 | `PRKTNAZI_E112` | `induces_problem` | 13-Noise Level | Gaussian white noise(High Noise) |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 22 | `PRKTNAZI_E113` | `induces_problem` | 13-Noise Level | Gaussian white noise(High Noise) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 23 | `PRKTNAZI_E114` | `induces_problem` | 14-Computational Resource | computation cost in the training stage(High Resource Consumption) |  | 09-Problem Scenario | domain shift / distribution discrepancy(Distribution Discrepancy) |  |
| 24 | `PRKTNAZI_E115` | `induces_problem` | 14-Computational Resource | computation cost in the training stage(High Resource Consumption) |  | 09-Problem Scenario | noise contamination(Uncertainty) |  |
| 25 | `PRKTNAZI_E116` | `induces_problem` | 14-Computational Resource | computation cost in the training stage(High Resource Consumption) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 25 edges)*
