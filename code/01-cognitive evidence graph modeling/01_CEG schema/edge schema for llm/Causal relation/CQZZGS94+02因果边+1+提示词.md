# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：CQZZGS94
- **Paper Title**：Fisher vector encoding for improving the performance of fault diagnosis in a synchronous generator
- **Number of Candidate Edges to Judge**：16 

---

## II. LLM Input

> **Input Material**: Reference ID `CQZZGS94`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "CQZZGS94_E047", "edge_description": "synchronous generator contains stator winding"},
    {"edge_id": "CQZZGS94_E048", "edge_description": "synchronous generator contains field winding"},
    {"edge_id": "CQZZGS94_E051", "edge_description": "current sensors is collected on stator winding"},
    {"edge_id": "CQZZGS94_E052", "edge_description": "current sensors is collected on field winding"},
    {"edge_id": "CQZZGS94_E055", "edge_description": "stator winding has_fault_mode inter-turn fault"},
    {"edge_id": "CQZZGS94_E056", "edge_description": "field winding has_fault_mode inter-turn fault"},
    {"edge_id": "CQZZGS94_E059", "edge_description": "stator winding contains_phm_task inter turn fault diagnosis"},
    {"edge_id": "CQZZGS94_E060", "edge_description": "field winding contains_phm_task inter turn fault diagnosis"},
    {"edge_id": "CQZZGS94_E063", "edge_description": "synchronous generator induces_problem statistical features exhibits non-linear characteristics"},
    {"edge_id": "CQZZGS94_E064", "edge_description": "different loading conditions from 0.5 A to 3.5 A with an increment of 0.5 A induces_problem statistical features exhibits non-linear characteristics"},
    {"edge_id": "CQZZGS94_E065", "edge_description": "30%, 60%, and 82% of the total number of turns induces_problem statistical features exhibits non-linear characteristics"},
    {"edge_id": "CQZZGS94_E066", "edge_description": "No Compound Fault induces_problem statistical features exhibits non-linear characteristics"},
    {"edge_id": "CQZZGS94_E067", "edge_description": "inter turn fault diagnosis induces_problem statistical features exhibits non-linear characteristics"},
    {"edge_id": "CQZZGS94_E068", "edge_description": "Training data (13300 normal samples, 10640 fault samples) induces_problem statistical features exhibits non-linear characteristics"},
    {"edge_id": "CQZZGS94_E069", "edge_description": "Not mentioned induces_problem statistical features exhibits non-linear characteristics"},
    {"edge_id": "CQZZGS94_E070", "edge_description": "computationally efficient algorithm, CPU time for encoding induces_problem statistical features exhibits non-linear characteristics"}
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
| 1 | `CQZZGS94_E047` | `contains` | 02-Object Type | synchronous generator |  | 04-Fault Location | stator winding |  |
| 2 | `CQZZGS94_E048` | `contains` | 02-Object Type | synchronous generator |  | 04-Fault Location | field winding |  |
| 3 | `CQZZGS94_E051` | `is collected on` | 11-Sensor Information | current sensors |  | 04-Fault Location | stator winding |  |
| 4 | `CQZZGS94_E052` | `is collected on` | 11-Sensor Information | current sensors |  | 04-Fault Location | field winding |  |
| 5 | `CQZZGS94_E055` | `has_fault_mode` | 04-Fault Location | stator winding |  | 05-Fault Mode | inter-turn fault |  |
| 6 | `CQZZGS94_E056` | `has_fault_mode` | 04-Fault Location | field winding |  | 05-Fault Mode | inter-turn fault |  |
| 7 | `CQZZGS94_E059` | `contains_phm_task` | 04-Fault Location | stator winding |  | 08-PHM Task | inter turn fault diagnosis(Diagnosis Task) |  |
| 8 | `CQZZGS94_E060` | `contains_phm_task` | 04-Fault Location | field winding |  | 08-PHM Task | inter turn fault diagnosis(Diagnosis Task) |  |
| 9 | `CQZZGS94_E063` | `induces_problem` | 02-Object Type | synchronous generator |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |
| 10 | `CQZZGS94_E064` | `induces_problem` | 03-Operating Conditions | different loading conditions from 0.5 A to 3.5 A with an increment of 0.5 A(Multiple Conditions) |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |
| 11 | `CQZZGS94_E065` | `induces_problem` | 06-Fault Severity | 30%, 60%, and 82% of the total number of turns(Multiple Severities) |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |
| 12 | `CQZZGS94_E066` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |
| 13 | `CQZZGS94_E067` | `induces_problem` | 08-PHM Task | inter turn fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |
| 14 | `CQZZGS94_E068` | `induces_problem` | 12-Training Data Availability | Training data (13300 normal samples, 10640 fault samples)(Sufficient) |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |
| 15 | `CQZZGS94_E069` | `induces_problem` | 13-Noise Level | Not mentioned(Normal) |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |
| 16 | `CQZZGS94_E070` | `induces_problem` | 14-Computational Resource | computationally efficient algorithm, CPU time for encoding(Low Resource Consumption) |  | 09-Problem Scenario | statistical features exhibits non-linear characteristics(Other) |  |

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

### ▶ For `is collected on` (Sensor Information type → Fault Location type)

**High Standard**: The paper must explicitly express that the sensor is **physically installed/arranged on** the target fault location, i.e., there is a description of the **physical positional relationship** between the sensor and the fault location.
The mere appearance in the dataset description of "a sensor used for a certain fault" is insufficient — the physical arrangement or installation context of the sensor must be reflected
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the relationship between the physical installation position of the sensor and the fault location, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 16 edges)*
