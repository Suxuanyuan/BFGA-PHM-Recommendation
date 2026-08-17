# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：K2VAMRKJ
- **Paper Title**：Fault Detection and Identification Scheme for Dual-Inverter Fed OEWIM Drive
- **Number of Candidate Edges to Judge**：19 

---

## II. LLM Input

> **Input Material**: Reference ID `K2VAMRKJ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "K2VAMRKJ_E033", "edge_description": "open-end winding induction motor drive system contains open-end winding induction motor"},
    {"edge_id": "K2VAMRKJ_E034", "edge_description": "open-end winding induction motor drive system contains dual-inverter"},
    {"edge_id": "K2VAMRKJ_E035", "edge_description": "open-end winding induction motor contains power switch"},
    {"edge_id": "K2VAMRKJ_E036", "edge_description": "dual-inverter contains power switch"},
    {"edge_id": "K2VAMRKJ_E037", "edge_description": "open-end winding induction motor contains multiple operating frequencies and loads"},
    {"edge_id": "K2VAMRKJ_E038", "edge_description": "dual-inverter contains multiple operating frequencies and loads"},
    {"edge_id": "K2VAMRKJ_E042", "edge_description": "MATLAB program for the dual-inverter OEWIM drive can be used for switch open-circuit fault detection and identification"},
    {"edge_id": "K2VAMRKJ_E043", "edge_description": "open-end winding induction motor (OEWIM) test rig can be used for switch open-circuit fault detection and identification"},
    {"edge_id": "K2VAMRKJ_E046", "edge_description": "open-end winding induction motor contains_phm_task switch open-circuit fault detection and identification"},
    {"edge_id": "K2VAMRKJ_E047", "edge_description": "dual-inverter contains_phm_task switch open-circuit fault detection and identification"},
    {"edge_id": "K2VAMRKJ_E051", "edge_description": "open-end winding induction motor induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E052", "edge_description": "dual-inverter induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E053", "edge_description": "multiple operating frequencies and loads induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E054", "edge_description": "Single Severity induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E055", "edge_description": "No Compound Fault induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E056", "edge_description": "switch open-circuit fault detection and identification induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E057", "edge_description": "Sufficient induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E058", "edge_description": "Normal induces_problem fault localization ambiguity due to topology symmetry"},
    {"edge_id": "K2VAMRKJ_E059", "edge_description": "32-bit DSP chip, TMS320F28335 induces_problem fault localization ambiguity due to topology symmetry"}
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
| 1 | `K2VAMRKJ_E033` | `contains` | 01-Object Domain | open-end winding induction motor drive system(Electronics) |  | 02-Object Type | open-end winding induction motor |  |
| 2 | `K2VAMRKJ_E034` | `contains` | 01-Object Domain | open-end winding induction motor drive system(Electronics) |  | 02-Object Type | dual-inverter |  |
| 3 | `K2VAMRKJ_E035` | `contains` | 02-Object Type | open-end winding induction motor |  | 04-Fault Location | power switch |  |
| 4 | `K2VAMRKJ_E036` | `contains` | 02-Object Type | dual-inverter |  | 04-Fault Location | power switch |  |
| 5 | `K2VAMRKJ_E037` | `contains` | 02-Object Type | open-end winding induction motor |  | 03-Operating Conditions | multiple operating frequencies and loads(Multiple Conditions) |  |
| 6 | `K2VAMRKJ_E038` | `contains` | 02-Object Type | dual-inverter |  | 03-Operating Conditions | multiple operating frequencies and loads(Multiple Conditions) |  |
| 7 | `K2VAMRKJ_E042` | `can be used for` | 10-Dataset | MATLAB program for the dual-inverter OEWIM drive |  | 08-PHM Task | switch open-circuit fault detection and identification(Diagnosis Task) |  |
| 8 | `K2VAMRKJ_E043` | `can be used for` | 10-Dataset | open-end winding induction motor (OEWIM) test rig |  | 08-PHM Task | switch open-circuit fault detection and identification(Diagnosis Task) |  |
| 9 | `K2VAMRKJ_E046` | `contains_phm_task` | 02-Object Type | open-end winding induction motor |  | 08-PHM Task | switch open-circuit fault detection and identification(Diagnosis Task) |  |
| 10 | `K2VAMRKJ_E047` | `contains_phm_task` | 02-Object Type | dual-inverter |  | 08-PHM Task | switch open-circuit fault detection and identification(Diagnosis Task) |  |
| 11 | `K2VAMRKJ_E051` | `induces_problem` | 02-Object Type | open-end winding induction motor |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 12 | `K2VAMRKJ_E052` | `induces_problem` | 02-Object Type | dual-inverter |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 13 | `K2VAMRKJ_E053` | `induces_problem` | 03-Operating Conditions | multiple operating frequencies and loads(Multiple Conditions) |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 14 | `K2VAMRKJ_E054` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 15 | `K2VAMRKJ_E055` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 16 | `K2VAMRKJ_E056` | `induces_problem` | 08-PHM Task | switch open-circuit fault detection and identification(Diagnosis Task) |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 17 | `K2VAMRKJ_E057` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 18 | `K2VAMRKJ_E058` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |
| 19 | `K2VAMRKJ_E059` | `induces_problem` | 14-Computational Resource | 32-bit DSP chip, TMS320F28335(Low Resource Consumption) |  | 09-Problem Scenario | fault localization ambiguity due to topology symmetry(Other) |  |

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

### ▶ For `can be used for` (Dataset type → PHM Task type)

**High Standard**: The paper must explicitly express that the dataset is an **input at the methodological level**, rather than merely a background for experimental evaluation.
Merely mentioning "using a dataset to evaluate model performance" is insufficient — the methodological association between dataset and task must be reflected (e.g., "selecting a dataset for a specific task")
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the methodological relation of the dataset serving a certain PHM task, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 19 edges)*
