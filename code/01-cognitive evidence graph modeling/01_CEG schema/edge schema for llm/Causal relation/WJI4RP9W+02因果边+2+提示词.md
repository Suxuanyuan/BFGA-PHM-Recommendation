# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WJI4RP9W
- **Paper Title**：A generic framework for decision fusion in Fault Detection and Diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `WJI4RP9W`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WJI4RP9W_E078", "edge_description": "Reactor has_fault_mode Cooling water inlet temperature change"},
    {"edge_id": "WJI4RP9W_E079", "edge_description": "Reactor has_fault_mode Feed loss"},
    {"edge_id": "WJI4RP9W_E080", "edge_description": "Reactor has_fault_mode Header pressure loss"},
    {"edge_id": "WJI4RP9W_E081", "edge_description": "Reactor has_fault_mode Reaction kinetics slow drift"},
    {"edge_id": "WJI4RP9W_E082", "edge_description": "Feed stream has_fault_mode Feed ratio / composition change"},
    {"edge_id": "WJI4RP9W_E083", "edge_description": "Feed stream has_fault_mode Cooling water inlet temperature change"},
    {"edge_id": "WJI4RP9W_E084", "edge_description": "Feed stream has_fault_mode Feed loss"},
    {"edge_id": "WJI4RP9W_E085", "edge_description": "Feed stream has_fault_mode Header pressure loss"},
    {"edge_id": "WJI4RP9W_E086", "edge_description": "Feed stream has_fault_mode Reaction kinetics slow drift"},
    {"edge_id": "WJI4RP9W_E087", "edge_description": "Feed ratio / composition change contains Single Severity"},
    {"edge_id": "WJI4RP9W_E088", "edge_description": "Cooling water inlet temperature change contains Single Severity"},
    {"edge_id": "WJI4RP9W_E089", "edge_description": "Feed loss contains Single Severity"},
    {"edge_id": "WJI4RP9W_E090", "edge_description": "Header pressure loss contains Single Severity"},
    {"edge_id": "WJI4RP9W_E091", "edge_description": "Reaction kinetics slow drift contains Single Severity"},
    {"edge_id": "WJI4RP9W_E093", "edge_description": "Condenser contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E094", "edge_description": "Reactor contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E095", "edge_description": "Feed stream contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E096", "edge_description": "Feed ratio / composition change contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E097", "edge_description": "Cooling water inlet temperature change contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E098", "edge_description": "Feed loss contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E099", "edge_description": "Header pressure loss contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E100", "edge_description": "Reaction kinetics slow drift contains_phm_task Fault Detection and Diagnosis"},
    {"edge_id": "WJI4RP9W_E102", "edge_description": "Tennessee Eastman Process induces_problem uncertainties or incomplete and conflicting information"},
    {"edge_id": "WJI4RP9W_E103", "edge_description": "Tennessee Eastman Process induces_problem multiple heterogeneous Fault Detection and Diagnosis (FDD) methods"},
    {"edge_id": "WJI4RP9W_E104", "edge_description": "normal operating conditions induces_problem uncertainties or incomplete and conflicting information"},
    {"edge_id": "WJI4RP9W_E105", "edge_description": "normal operating conditions induces_problem multiple heterogeneous Fault Detection and Diagnosis (FDD) methods"},
    {"edge_id": "WJI4RP9W_E106", "edge_description": "Single Severity induces_problem uncertainties or incomplete and conflicting information"},
    {"edge_id": "WJI4RP9W_E107", "edge_description": "Single Severity induces_problem multiple heterogeneous Fault Detection and Diagnosis (FDD) methods"},
    {"edge_id": "WJI4RP9W_E108", "edge_description": "No Compound Fault induces_problem uncertainties or incomplete and conflicting information"},
    {"edge_id": "WJI4RP9W_E109", "edge_description": "No Compound Fault induces_problem multiple heterogeneous Fault Detection and Diagnosis (FDD) methods"}
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
| 1 | `WJI4RP9W_E078` | `has_fault_mode` | 04-Fault Location | Reactor |  | 05-Fault Mode | Cooling water inlet temperature change |  |
| 2 | `WJI4RP9W_E079` | `has_fault_mode` | 04-Fault Location | Reactor |  | 05-Fault Mode | Feed loss |  |
| 3 | `WJI4RP9W_E080` | `has_fault_mode` | 04-Fault Location | Reactor |  | 05-Fault Mode | Header pressure loss |  |
| 4 | `WJI4RP9W_E081` | `has_fault_mode` | 04-Fault Location | Reactor |  | 05-Fault Mode | Reaction kinetics slow drift |  |
| 5 | `WJI4RP9W_E082` | `has_fault_mode` | 04-Fault Location | Feed stream |  | 05-Fault Mode | Feed ratio / composition change |  |
| 6 | `WJI4RP9W_E083` | `has_fault_mode` | 04-Fault Location | Feed stream |  | 05-Fault Mode | Cooling water inlet temperature change |  |
| 7 | `WJI4RP9W_E084` | `has_fault_mode` | 04-Fault Location | Feed stream |  | 05-Fault Mode | Feed loss |  |
| 8 | `WJI4RP9W_E085` | `has_fault_mode` | 04-Fault Location | Feed stream |  | 05-Fault Mode | Header pressure loss |  |
| 9 | `WJI4RP9W_E086` | `has_fault_mode` | 04-Fault Location | Feed stream |  | 05-Fault Mode | Reaction kinetics slow drift |  |
| 10 | `WJI4RP9W_E087` | `contains` | 05-Fault Mode | Feed ratio / composition change |  | 06-Fault Severity | Single Severity |  |
| 11 | `WJI4RP9W_E088` | `contains` | 05-Fault Mode | Cooling water inlet temperature change |  | 06-Fault Severity | Single Severity |  |
| 12 | `WJI4RP9W_E089` | `contains` | 05-Fault Mode | Feed loss |  | 06-Fault Severity | Single Severity |  |
| 13 | `WJI4RP9W_E090` | `contains` | 05-Fault Mode | Header pressure loss |  | 06-Fault Severity | Single Severity |  |
| 14 | `WJI4RP9W_E091` | `contains` | 05-Fault Mode | Reaction kinetics slow drift |  | 06-Fault Severity | Single Severity |  |
| 15 | `WJI4RP9W_E093` | `contains_phm_task` | 04-Fault Location | Condenser |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 16 | `WJI4RP9W_E094` | `contains_phm_task` | 04-Fault Location | Reactor |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 17 | `WJI4RP9W_E095` | `contains_phm_task` | 04-Fault Location | Feed stream |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 18 | `WJI4RP9W_E096` | `contains_phm_task` | 05-Fault Mode | Feed ratio / composition change |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 19 | `WJI4RP9W_E097` | `contains_phm_task` | 05-Fault Mode | Cooling water inlet temperature change |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 20 | `WJI4RP9W_E098` | `contains_phm_task` | 05-Fault Mode | Feed loss |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 21 | `WJI4RP9W_E099` | `contains_phm_task` | 05-Fault Mode | Header pressure loss |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 22 | `WJI4RP9W_E100` | `contains_phm_task` | 05-Fault Mode | Reaction kinetics slow drift |  | 08-PHM Task | Fault Detection and Diagnosis(Diagnosis Task) |  |
| 23 | `WJI4RP9W_E102` | `induces_problem` | 02-Object Type | Tennessee Eastman Process |  | 09-Problem Scenario | uncertainties or incomplete and conflicting information(Uncertainty) |  |
| 24 | `WJI4RP9W_E103` | `induces_problem` | 02-Object Type | Tennessee Eastman Process |  | 09-Problem Scenario | multiple heterogeneous Fault Detection and Diagnosis (FDD) methods(Multi-Source Heterogeneous / Multimodal Data) |  |
| 25 | `WJI4RP9W_E104` | `induces_problem` | 03-Operating Conditions | normal operating conditions(Single Condition) |  | 09-Problem Scenario | uncertainties or incomplete and conflicting information(Uncertainty) |  |
| 26 | `WJI4RP9W_E105` | `induces_problem` | 03-Operating Conditions | normal operating conditions(Single Condition) |  | 09-Problem Scenario | multiple heterogeneous Fault Detection and Diagnosis (FDD) methods(Multi-Source Heterogeneous / Multimodal Data) |  |
| 27 | `WJI4RP9W_E106` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | uncertainties or incomplete and conflicting information(Uncertainty) |  |
| 28 | `WJI4RP9W_E107` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | multiple heterogeneous Fault Detection and Diagnosis (FDD) methods(Multi-Source Heterogeneous / Multimodal Data) |  |
| 29 | `WJI4RP9W_E108` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | uncertainties or incomplete and conflicting information(Uncertainty) |  |
| 30 | `WJI4RP9W_E109` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | multiple heterogeneous Fault Detection and Diagnosis (FDD) methods(Multi-Source Heterogeneous / Multimodal Data) |  |

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
