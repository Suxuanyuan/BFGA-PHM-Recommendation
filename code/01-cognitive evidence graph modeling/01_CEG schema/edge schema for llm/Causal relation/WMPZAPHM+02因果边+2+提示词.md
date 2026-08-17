# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WMPZAPHM
- **Paper Title**：Robust Interpretable Deep Learning for Intelligent Fault Diagnosis of Induction Motors
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `WMPZAPHM`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WMPZAPHM_E097", "edge_description": "cage fault contains incipient broken bar, one broken bar, two broken bars"},
    {"edge_id": "WMPZAPHM_E098", "edge_description": "broken rotor bar contains incipient broken bar, one broken bar, two broken bars"},
    {"edge_id": "WMPZAPHM_E099", "edge_description": "double cage induction motor contains_phm_task multi-fault diagnosis"},
    {"edge_id": "WMPZAPHM_E100", "edge_description": "6206 ball bearing contains_phm_task multi-fault diagnosis"},
    {"edge_id": "WMPZAPHM_E101", "edge_description": "bearing contains_phm_task multi-fault diagnosis"},
    {"edge_id": "WMPZAPHM_E102", "edge_description": "rotor bar contains_phm_task multi-fault diagnosis"},
    {"edge_id": "WMPZAPHM_E103", "edge_description": "outer race fault, inner race fault contains_phm_task multi-fault diagnosis"},
    {"edge_id": "WMPZAPHM_E104", "edge_description": "cage fault contains_phm_task multi-fault diagnosis"},
    {"edge_id": "WMPZAPHM_E105", "edge_description": "broken rotor bar contains_phm_task multi-fault diagnosis"},
    {"edge_id": "WMPZAPHM_E107", "edge_description": "double cage induction motor induces_problem lack of physical interpretability"},
    {"edge_id": "WMPZAPHM_E108", "edge_description": "double cage induction motor induces_problem robustness against noisy environments"},
    {"edge_id": "WMPZAPHM_E109", "edge_description": "double cage induction motor induces_problem combined faults"},
    {"edge_id": "WMPZAPHM_E110", "edge_description": "6206 ball bearing induces_problem lack of physical interpretability"},
    {"edge_id": "WMPZAPHM_E111", "edge_description": "6206 ball bearing induces_problem robustness against noisy environments"},
    {"edge_id": "WMPZAPHM_E112", "edge_description": "6206 ball bearing induces_problem combined faults"},
    {"edge_id": "WMPZAPHM_E113", "edge_description": "0%, 25%, 50%, 75% and 100% of load induces_problem lack of physical interpretability"},
    {"edge_id": "WMPZAPHM_E114", "edge_description": "0%, 25%, 50%, 75% and 100% of load induces_problem robustness against noisy environments"},
    {"edge_id": "WMPZAPHM_E115", "edge_description": "0%, 25%, 50%, 75% and 100% of load induces_problem combined faults"},
    {"edge_id": "WMPZAPHM_E116", "edge_description": "incipient broken bar, one broken bar, two broken bars induces_problem lack of physical interpretability"},
    {"edge_id": "WMPZAPHM_E117", "edge_description": "incipient broken bar, one broken bar, two broken bars induces_problem robustness against noisy environments"},
    {"edge_id": "WMPZAPHM_E118", "edge_description": "incipient broken bar, one broken bar, two broken bars induces_problem combined faults"},
    {"edge_id": "WMPZAPHM_E119", "edge_description": "combined faults induces_problem lack of physical interpretability"},
    {"edge_id": "WMPZAPHM_E120", "edge_description": "combined faults induces_problem robustness against noisy environments"},
    {"edge_id": "WMPZAPHM_E121", "edge_description": "combined faults induces_problem combined faults"},
    {"edge_id": "WMPZAPHM_E122", "edge_description": "multi-fault diagnosis induces_problem lack of physical interpretability"},
    {"edge_id": "WMPZAPHM_E123", "edge_description": "multi-fault diagnosis induces_problem robustness against noisy environments"},
    {"edge_id": "WMPZAPHM_E124", "edge_description": "multi-fault diagnosis induces_problem combined faults"},
    {"edge_id": "WMPZAPHM_E125", "edge_description": "30 acquisitions for each motor condition induces_problem lack of physical interpretability"},
    {"edge_id": "WMPZAPHM_E126", "edge_description": "30 acquisitions for each motor condition induces_problem robustness against noisy environments"},
    {"edge_id": "WMPZAPHM_E127", "edge_description": "30 acquisitions for each motor condition induces_problem combined faults"}
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
| 1 | `WMPZAPHM_E097` | `contains` | 05-Fault Mode | cage fault |  | 06-Fault Severity | incipient broken bar, one broken bar, two broken bars(Multiple Severities) |  |
| 2 | `WMPZAPHM_E098` | `contains` | 05-Fault Mode | broken rotor bar |  | 06-Fault Severity | incipient broken bar, one broken bar, two broken bars(Multiple Severities) |  |
| 3 | `WMPZAPHM_E099` | `contains_phm_task` | 02-Object Type | double cage induction motor |  | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  |
| 4 | `WMPZAPHM_E100` | `contains_phm_task` | 02-Object Type | 6206 ball bearing |  | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  |
| 5 | `WMPZAPHM_E101` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  |
| 6 | `WMPZAPHM_E102` | `contains_phm_task` | 04-Fault Location | rotor bar |  | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  |
| 7 | `WMPZAPHM_E103` | `contains_phm_task` | 05-Fault Mode | outer race fault, inner race fault |  | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  |
| 8 | `WMPZAPHM_E104` | `contains_phm_task` | 05-Fault Mode | cage fault |  | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  |
| 9 | `WMPZAPHM_E105` | `contains_phm_task` | 05-Fault Mode | broken rotor bar |  | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  |
| 10 | `WMPZAPHM_E107` | `induces_problem` | 02-Object Type | double cage induction motor |  | 09-Problem Scenario | lack of physical interpretability(Trustworthiness / Interpretability) |  |
| 11 | `WMPZAPHM_E108` | `induces_problem` | 02-Object Type | double cage induction motor |  | 09-Problem Scenario | robustness against noisy environments(Uncertainty) |  |
| 12 | `WMPZAPHM_E109` | `induces_problem` | 02-Object Type | double cage induction motor |  | 09-Problem Scenario | combined faults(Compound Faults) |  |
| 13 | `WMPZAPHM_E110` | `induces_problem` | 02-Object Type | 6206 ball bearing |  | 09-Problem Scenario | lack of physical interpretability(Trustworthiness / Interpretability) |  |
| 14 | `WMPZAPHM_E111` | `induces_problem` | 02-Object Type | 6206 ball bearing |  | 09-Problem Scenario | robustness against noisy environments(Uncertainty) |  |
| 15 | `WMPZAPHM_E112` | `induces_problem` | 02-Object Type | 6206 ball bearing |  | 09-Problem Scenario | combined faults(Compound Faults) |  |
| 16 | `WMPZAPHM_E113` | `induces_problem` | 03-Operating Conditions | 0%, 25%, 50%, 75% and 100% of load(Multiple Conditions) |  | 09-Problem Scenario | lack of physical interpretability(Trustworthiness / Interpretability) |  |
| 17 | `WMPZAPHM_E114` | `induces_problem` | 03-Operating Conditions | 0%, 25%, 50%, 75% and 100% of load(Multiple Conditions) |  | 09-Problem Scenario | robustness against noisy environments(Uncertainty) |  |
| 18 | `WMPZAPHM_E115` | `induces_problem` | 03-Operating Conditions | 0%, 25%, 50%, 75% and 100% of load(Multiple Conditions) |  | 09-Problem Scenario | combined faults(Compound Faults) |  |
| 19 | `WMPZAPHM_E116` | `induces_problem` | 06-Fault Severity | incipient broken bar, one broken bar, two broken bars(Multiple Severities) |  | 09-Problem Scenario | lack of physical interpretability(Trustworthiness / Interpretability) |  |
| 20 | `WMPZAPHM_E117` | `induces_problem` | 06-Fault Severity | incipient broken bar, one broken bar, two broken bars(Multiple Severities) |  | 09-Problem Scenario | robustness against noisy environments(Uncertainty) |  |
| 21 | `WMPZAPHM_E118` | `induces_problem` | 06-Fault Severity | incipient broken bar, one broken bar, two broken bars(Multiple Severities) |  | 09-Problem Scenario | combined faults(Compound Faults) |  |
| 22 | `WMPZAPHM_E119` | `induces_problem` | 07-Compound Fault | combined faults(Compound Fault Across Structures) |  | 09-Problem Scenario | lack of physical interpretability(Trustworthiness / Interpretability) |  |
| 23 | `WMPZAPHM_E120` | `induces_problem` | 07-Compound Fault | combined faults(Compound Fault Across Structures) |  | 09-Problem Scenario | robustness against noisy environments(Uncertainty) |  |
| 24 | `WMPZAPHM_E121` | `induces_problem` | 07-Compound Fault | combined faults(Compound Fault Across Structures) |  | 09-Problem Scenario | combined faults(Compound Faults) |  |
| 25 | `WMPZAPHM_E122` | `induces_problem` | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | lack of physical interpretability(Trustworthiness / Interpretability) |  |
| 26 | `WMPZAPHM_E123` | `induces_problem` | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | robustness against noisy environments(Uncertainty) |  |
| 27 | `WMPZAPHM_E124` | `induces_problem` | 08-PHM Task | multi-fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | combined faults(Compound Faults) |  |
| 28 | `WMPZAPHM_E125` | `induces_problem` | 12-Training Data Availability | 30 acquisitions for each motor condition(Sufficient) |  | 09-Problem Scenario | lack of physical interpretability(Trustworthiness / Interpretability) |  |
| 29 | `WMPZAPHM_E126` | `induces_problem` | 12-Training Data Availability | 30 acquisitions for each motor condition(Sufficient) |  | 09-Problem Scenario | robustness against noisy environments(Uncertainty) |  |
| 30 | `WMPZAPHM_E127` | `induces_problem` | 12-Training Data Availability | 30 acquisitions for each motor condition(Sufficient) |  | 09-Problem Scenario | combined faults(Compound Faults) |  |

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
