# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：JJHTKIUS
- **Paper Title**：Time-frequency manifold for nonlinear feature extraction in machinery fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `JJHTKIUS`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "JJHTKIUS_E097", "edge_description": "rolling element bearing has_fault_mode inner-race defect"},
    {"edge_id": "JJHTKIUS_E098", "edge_description": "rolling element bearing has_fault_mode rolling-element defect"},
    {"edge_id": "JJHTKIUS_E099", "edge_description": "wear contains slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in."},
    {"edge_id": "JJHTKIUS_E100", "edge_description": "tooth-broken contains slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in."},
    {"edge_id": "JJHTKIUS_E101", "edge_description": "outer-race defect contains slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in."},
    {"edge_id": "JJHTKIUS_E102", "edge_description": "inner-race defect contains slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in."},
    {"edge_id": "JJHTKIUS_E103", "edge_description": "rolling-element defect contains slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in."},
    {"edge_id": "JJHTKIUS_E104", "edge_description": "automobile transmission gearbox contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E105", "edge_description": "rolling element bearing contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E106", "edge_description": "driving gear, gearbox contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E107", "edge_description": "rolling element bearing contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E108", "edge_description": "wear contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E109", "edge_description": "tooth-broken contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E110", "edge_description": "outer-race defect contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E111", "edge_description": "inner-race defect contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E112", "edge_description": "rolling-element defect contains_phm_task machinery fault diagnosis"},
    {"edge_id": "JJHTKIUS_E114", "edge_description": "automobile transmission gearbox induces_problem noise corruption and condition variance"},
    {"edge_id": "JJHTKIUS_E115", "edge_description": "automobile transmission gearbox induces_problem dimensionality reduction issues of time-frequency distribution"},
    {"edge_id": "JJHTKIUS_E116", "edge_description": "rolling element bearing induces_problem noise corruption and condition variance"},
    {"edge_id": "JJHTKIUS_E117", "edge_description": "rolling element bearing induces_problem dimensionality reduction issues of time-frequency distribution"},
    {"edge_id": "JJHTKIUS_E118", "edge_description": "rotating speed of 1600 rpm, 1723 rpm, 1772 rpm, and 1774 rpm induces_problem noise corruption and condition variance"},
    {"edge_id": "JJHTKIUS_E119", "edge_description": "rotating speed of 1600 rpm, 1723 rpm, 1772 rpm, and 1774 rpm induces_problem dimensionality reduction issues of time-frequency distribution"},
    {"edge_id": "JJHTKIUS_E120", "edge_description": "slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in. induces_problem noise corruption and condition variance"},
    {"edge_id": "JJHTKIUS_E121", "edge_description": "slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in. induces_problem dimensionality reduction issues of time-frequency distribution"},
    {"edge_id": "JJHTKIUS_E122", "edge_description": "No Compound Fault induces_problem noise corruption and condition variance"},
    {"edge_id": "JJHTKIUS_E123", "edge_description": "No Compound Fault induces_problem dimensionality reduction issues of time-frequency distribution"},
    {"edge_id": "JJHTKIUS_E124", "edge_description": "machinery fault diagnosis induces_problem noise corruption and condition variance"},
    {"edge_id": "JJHTKIUS_E125", "edge_description": "machinery fault diagnosis induces_problem dimensionality reduction issues of time-frequency distribution"},
    {"edge_id": "JJHTKIUS_E126", "edge_description": "30 training samples per class (gear case), 50 training samples per class (bearing cases) induces_problem noise corruption and condition variance"},
    {"edge_id": "JJHTKIUS_E127", "edge_description": "30 training samples per class (gear case), 50 training samples per class (bearing cases) induces_problem dimensionality reduction issues of time-frequency distribution"}
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
| 1 | `JJHTKIUS_E097` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | inner-race defect |  |
| 2 | `JJHTKIUS_E098` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | rolling-element defect |  |
| 3 | `JJHTKIUS_E099` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in.(Multiple Severities) |  |
| 4 | `JJHTKIUS_E100` | `contains` | 05-Fault Mode | tooth-broken |  | 06-Fault Severity | slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in.(Multiple Severities) |  |
| 5 | `JJHTKIUS_E101` | `contains` | 05-Fault Mode | outer-race defect |  | 06-Fault Severity | slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in.(Multiple Severities) |  |
| 6 | `JJHTKIUS_E102` | `contains` | 05-Fault Mode | inner-race defect |  | 06-Fault Severity | slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in.(Multiple Severities) |  |
| 7 | `JJHTKIUS_E103` | `contains` | 05-Fault Mode | rolling-element defect |  | 06-Fault Severity | slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in.(Multiple Severities) |  |
| 8 | `JJHTKIUS_E104` | `contains_phm_task` | 02-Object Type | automobile transmission gearbox |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 9 | `JJHTKIUS_E105` | `contains_phm_task` | 02-Object Type | rolling element bearing |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 10 | `JJHTKIUS_E106` | `contains_phm_task` | 04-Fault Location | driving gear, gearbox |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 11 | `JJHTKIUS_E107` | `contains_phm_task` | 04-Fault Location | rolling element bearing |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 12 | `JJHTKIUS_E108` | `contains_phm_task` | 05-Fault Mode | wear |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 13 | `JJHTKIUS_E109` | `contains_phm_task` | 05-Fault Mode | tooth-broken |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 14 | `JJHTKIUS_E110` | `contains_phm_task` | 05-Fault Mode | outer-race defect |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 15 | `JJHTKIUS_E111` | `contains_phm_task` | 05-Fault Mode | inner-race defect |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 16 | `JJHTKIUS_E112` | `contains_phm_task` | 05-Fault Mode | rolling-element defect |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 17 | `JJHTKIUS_E114` | `induces_problem` | 02-Object Type | automobile transmission gearbox |  | 09-Problem Scenario | noise corruption and condition variance(Uncertainty) |  |
| 18 | `JJHTKIUS_E115` | `induces_problem` | 02-Object Type | automobile transmission gearbox |  | 09-Problem Scenario | dimensionality reduction issues of time-frequency distribution(Other) |  |
| 19 | `JJHTKIUS_E116` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | noise corruption and condition variance(Uncertainty) |  |
| 20 | `JJHTKIUS_E117` | `induces_problem` | 02-Object Type | rolling element bearing |  | 09-Problem Scenario | dimensionality reduction issues of time-frequency distribution(Other) |  |
| 21 | `JJHTKIUS_E118` | `induces_problem` | 03-Operating Conditions | rotating speed of 1600 rpm, 1723 rpm, 1772 rpm, and 1774 rpm(Multiple Conditions) |  | 09-Problem Scenario | noise corruption and condition variance(Uncertainty) |  |
| 22 | `JJHTKIUS_E119` | `induces_problem` | 03-Operating Conditions | rotating speed of 1600 rpm, 1723 rpm, 1772 rpm, and 1774 rpm(Multiple Conditions) |  | 09-Problem Scenario | dimensionality reduction issues of time-frequency distribution(Other) |  |
| 23 | `JJHTKIUS_E120` | `induces_problem` | 06-Fault Severity | slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in.(Multiple Severities) |  | 09-Problem Scenario | noise corruption and condition variance(Uncertainty) |  |
| 24 | `JJHTKIUS_E121` | `induces_problem` | 06-Fault Severity | slight fault, severe fault, 0.007 in., 0.014 in., 0.021 in., 0.028 in.(Multiple Severities) |  | 09-Problem Scenario | dimensionality reduction issues of time-frequency distribution(Other) |  |
| 25 | `JJHTKIUS_E122` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise corruption and condition variance(Uncertainty) |  |
| 26 | `JJHTKIUS_E123` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | dimensionality reduction issues of time-frequency distribution(Other) |  |
| 27 | `JJHTKIUS_E124` | `induces_problem` | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | noise corruption and condition variance(Uncertainty) |  |
| 28 | `JJHTKIUS_E125` | `induces_problem` | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | dimensionality reduction issues of time-frequency distribution(Other) |  |
| 29 | `JJHTKIUS_E126` | `induces_problem` | 12-Training Data Availability | 30 training samples per class (gear case), 50 training samples per class (bearing cases)(Sufficient) |  | 09-Problem Scenario | noise corruption and condition variance(Uncertainty) |  |
| 30 | `JJHTKIUS_E127` | `induces_problem` | 12-Training Data Availability | 30 training samples per class (gear case), 50 training samples per class (bearing cases)(Sufficient) |  | 09-Problem Scenario | dimensionality reduction issues of time-frequency distribution(Other) |  |

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
