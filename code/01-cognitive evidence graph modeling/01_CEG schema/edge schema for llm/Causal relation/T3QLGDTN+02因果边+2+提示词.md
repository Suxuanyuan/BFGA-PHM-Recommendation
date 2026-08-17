# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：T3QLGDTN
- **Paper Title**：Optimized Relative Transformation Matrix Using Bacterial Foraging Algorithm for Process Fault Detection
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `T3QLGDTN`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "T3QLGDTN_E126", "edge_description": "aluminum reduction cell has_fault_mode aluminum liquid fluctuation"},
    {"edge_id": "T3QLGDTN_E127", "edge_description": "aluminum reduction cell has_fault_mode high anode-cathode distance"},
    {"edge_id": "T3QLGDTN_E128", "edge_description": "cathode has_fault_mode floating carbon residue"},
    {"edge_id": "T3QLGDTN_E129", "edge_description": "cathode has_fault_mode cathode breakage"},
    {"edge_id": "T3QLGDTN_E130", "edge_description": "cathode has_fault_mode aluminum liquid fluctuation"},
    {"edge_id": "T3QLGDTN_E131", "edge_description": "cathode has_fault_mode high anode-cathode distance"},
    {"edge_id": "T3QLGDTN_E132", "edge_description": "anode has_fault_mode floating carbon residue"},
    {"edge_id": "T3QLGDTN_E133", "edge_description": "anode has_fault_mode cathode breakage"},
    {"edge_id": "T3QLGDTN_E134", "edge_description": "anode has_fault_mode aluminum liquid fluctuation"},
    {"edge_id": "T3QLGDTN_E135", "edge_description": "anode has_fault_mode high anode-cathode distance"},
    {"edge_id": "T3QLGDTN_E136", "edge_description": "floating carbon residue contains Single Severity"},
    {"edge_id": "T3QLGDTN_E137", "edge_description": "cathode breakage contains Single Severity"},
    {"edge_id": "T3QLGDTN_E138", "edge_description": "aluminum liquid fluctuation contains Single Severity"},
    {"edge_id": "T3QLGDTN_E139", "edge_description": "high anode-cathode distance contains Single Severity"},
    {"edge_id": "T3QLGDTN_E141", "edge_description": "aluminum reduction cell contains_phm_task Process Fault Detection"},
    {"edge_id": "T3QLGDTN_E142", "edge_description": "cathode contains_phm_task Process Fault Detection"},
    {"edge_id": "T3QLGDTN_E143", "edge_description": "anode contains_phm_task Process Fault Detection"},
    {"edge_id": "T3QLGDTN_E144", "edge_description": "floating carbon residue contains_phm_task Process Fault Detection"},
    {"edge_id": "T3QLGDTN_E145", "edge_description": "cathode breakage contains_phm_task Process Fault Detection"},
    {"edge_id": "T3QLGDTN_E146", "edge_description": "aluminum liquid fluctuation contains_phm_task Process Fault Detection"},
    {"edge_id": "T3QLGDTN_E147", "edge_description": "high anode-cathode distance contains_phm_task Process Fault Detection"},
    {"edge_id": "T3QLGDTN_E149", "edge_description": "aluminum reduction cell induces_problem complicated industrial system with highly coupled parameters"},
    {"edge_id": "T3QLGDTN_E150", "edge_description": "aluminum reduction cell induces_problem uncertainties from system disturbance and state change"},
    {"edge_id": "T3QLGDTN_E151", "edge_description": "aluminum reduction cell induces_problem losing feature after the normalization of nonlinear variables in the feature subspace"},
    {"edge_id": "T3QLGDTN_E152", "edge_description": "1000 sets of daily data from a 170-KA series of aluminum reduction cell induces_problem complicated industrial system with highly coupled parameters"},
    {"edge_id": "T3QLGDTN_E153", "edge_description": "1000 sets of daily data from a 170-KA series of aluminum reduction cell induces_problem uncertainties from system disturbance and state change"},
    {"edge_id": "T3QLGDTN_E154", "edge_description": "1000 sets of daily data from a 170-KA series of aluminum reduction cell induces_problem losing feature after the normalization of nonlinear variables in the feature subspace"},
    {"edge_id": "T3QLGDTN_E155", "edge_description": "Single Severity induces_problem complicated industrial system with highly coupled parameters"},
    {"edge_id": "T3QLGDTN_E156", "edge_description": "Single Severity induces_problem uncertainties from system disturbance and state change"},
    {"edge_id": "T3QLGDTN_E157", "edge_description": "Single Severity induces_problem losing feature after the normalization of nonlinear variables in the feature subspace"}
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
| 1 | `T3QLGDTN_E126` | `has_fault_mode` | 04-Fault Location | aluminum reduction cell |  | 05-Fault Mode | aluminum liquid fluctuation |  |
| 2 | `T3QLGDTN_E127` | `has_fault_mode` | 04-Fault Location | aluminum reduction cell |  | 05-Fault Mode | high anode-cathode distance |  |
| 3 | `T3QLGDTN_E128` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | floating carbon residue |  |
| 4 | `T3QLGDTN_E129` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | cathode breakage |  |
| 5 | `T3QLGDTN_E130` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | aluminum liquid fluctuation |  |
| 6 | `T3QLGDTN_E131` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | high anode-cathode distance |  |
| 7 | `T3QLGDTN_E132` | `has_fault_mode` | 04-Fault Location | anode |  | 05-Fault Mode | floating carbon residue |  |
| 8 | `T3QLGDTN_E133` | `has_fault_mode` | 04-Fault Location | anode |  | 05-Fault Mode | cathode breakage |  |
| 9 | `T3QLGDTN_E134` | `has_fault_mode` | 04-Fault Location | anode |  | 05-Fault Mode | aluminum liquid fluctuation |  |
| 10 | `T3QLGDTN_E135` | `has_fault_mode` | 04-Fault Location | anode |  | 05-Fault Mode | high anode-cathode distance |  |
| 11 | `T3QLGDTN_E136` | `contains` | 05-Fault Mode | floating carbon residue |  | 06-Fault Severity | Single Severity |  |
| 12 | `T3QLGDTN_E137` | `contains` | 05-Fault Mode | cathode breakage |  | 06-Fault Severity | Single Severity |  |
| 13 | `T3QLGDTN_E138` | `contains` | 05-Fault Mode | aluminum liquid fluctuation |  | 06-Fault Severity | Single Severity |  |
| 14 | `T3QLGDTN_E139` | `contains` | 05-Fault Mode | high anode-cathode distance |  | 06-Fault Severity | Single Severity |  |
| 15 | `T3QLGDTN_E141` | `contains_phm_task` | 04-Fault Location | aluminum reduction cell |  | 08-PHM Task | Process Fault Detection(Detection Task) |  |
| 16 | `T3QLGDTN_E142` | `contains_phm_task` | 04-Fault Location | cathode |  | 08-PHM Task | Process Fault Detection(Detection Task) |  |
| 17 | `T3QLGDTN_E143` | `contains_phm_task` | 04-Fault Location | anode |  | 08-PHM Task | Process Fault Detection(Detection Task) |  |
| 18 | `T3QLGDTN_E144` | `contains_phm_task` | 05-Fault Mode | floating carbon residue |  | 08-PHM Task | Process Fault Detection(Detection Task) |  |
| 19 | `T3QLGDTN_E145` | `contains_phm_task` | 05-Fault Mode | cathode breakage |  | 08-PHM Task | Process Fault Detection(Detection Task) |  |
| 20 | `T3QLGDTN_E146` | `contains_phm_task` | 05-Fault Mode | aluminum liquid fluctuation |  | 08-PHM Task | Process Fault Detection(Detection Task) |  |
| 21 | `T3QLGDTN_E147` | `contains_phm_task` | 05-Fault Mode | high anode-cathode distance |  | 08-PHM Task | Process Fault Detection(Detection Task) |  |
| 22 | `T3QLGDTN_E149` | `induces_problem` | 02-Object Type | aluminum reduction cell |  | 09-Problem Scenario | complicated industrial system with highly coupled parameters(Complex Systems) |  |
| 23 | `T3QLGDTN_E150` | `induces_problem` | 02-Object Type | aluminum reduction cell |  | 09-Problem Scenario | uncertainties from system disturbance and state change(Uncertainty) |  |
| 24 | `T3QLGDTN_E151` | `induces_problem` | 02-Object Type | aluminum reduction cell |  | 09-Problem Scenario | losing feature after the normalization of nonlinear variables in the feature subspace(Other) |  |
| 25 | `T3QLGDTN_E152` | `induces_problem` | 03-Operating Conditions | 1000 sets of daily data from a 170-KA series of aluminum reduction cell(Single Condition) |  | 09-Problem Scenario | complicated industrial system with highly coupled parameters(Complex Systems) |  |
| 26 | `T3QLGDTN_E153` | `induces_problem` | 03-Operating Conditions | 1000 sets of daily data from a 170-KA series of aluminum reduction cell(Single Condition) |  | 09-Problem Scenario | uncertainties from system disturbance and state change(Uncertainty) |  |
| 27 | `T3QLGDTN_E154` | `induces_problem` | 03-Operating Conditions | 1000 sets of daily data from a 170-KA series of aluminum reduction cell(Single Condition) |  | 09-Problem Scenario | losing feature after the normalization of nonlinear variables in the feature subspace(Other) |  |
| 28 | `T3QLGDTN_E155` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | complicated industrial system with highly coupled parameters(Complex Systems) |  |
| 29 | `T3QLGDTN_E156` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | uncertainties from system disturbance and state change(Uncertainty) |  |
| 30 | `T3QLGDTN_E157` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | losing feature after the normalization of nonlinear variables in the feature subspace(Other) |  |

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
