# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TYD5W2WP
- **Paper Title**：An adaptive data fusion strategy for fault diagnosis based on the convolutional neural network
- **Number of Candidate Edges to Judge**：29 

---

## II. LLM Input

> **Input Material**: Reference ID `TYD5W2WP`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TYD5W2WP_E136", "edge_description": "flaking contains Single Severity"},
    {"edge_id": "TYD5W2WP_E137", "edge_description": "defect contains Single Severity"},
    {"edge_id": "TYD5W2WP_E138", "edge_description": "imbalance contains Single Severity"},
    {"edge_id": "TYD5W2WP_E139", "edge_description": "loose bearing housing contains Single Severity"},
    {"edge_id": "TYD5W2WP_E140", "edge_description": "shaft misalignment contains Single Severity"},
    {"edge_id": "TYD5W2WP_E141", "edge_description": "cavitation contains Single Severity"},
    {"edge_id": "TYD5W2WP_E142", "edge_description": "industrial fan contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E143", "edge_description": "centrifugal pump contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E144", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E145", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E146", "edge_description": "shaft contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E147", "edge_description": "blade contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E148", "edge_description": "impeller contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E149", "edge_description": "flaking contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E150", "edge_description": "defect contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E151", "edge_description": "imbalance contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E152", "edge_description": "loose bearing housing contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E153", "edge_description": "shaft misalignment contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E154", "edge_description": "cavitation contains_phm_task fault diagnosis"},
    {"edge_id": "TYD5W2WP_E156", "edge_description": "industrial fan induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E157", "edge_description": "centrifugal pump induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E158", "edge_description": "bearing induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E159", "edge_description": "800 rpm, 2000 rpm, 3000 rpm induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E160", "edge_description": "Single Severity induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E161", "edge_description": "No Compound Fault induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E162", "edge_description": "fault diagnosis induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E163", "edge_description": "Among the 10,800 measured signal samples, 9,000 samples, which were evenly selected from the nine types, were used to train the model. induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E164", "edge_description": "Normal induces_problem multiple source data fusion"},
    {"edge_id": "TYD5W2WP_E165", "edge_description": "without incurring an additional computational burden, reduces the complexity of the FAC-CNN induces_problem multiple source data fusion"}
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
| 1 | `TYD5W2WP_E136` | `contains` | 05-Fault Mode | flaking |  | 06-Fault Severity | Single Severity |  |
| 2 | `TYD5W2WP_E137` | `contains` | 05-Fault Mode | defect |  | 06-Fault Severity | Single Severity |  |
| 3 | `TYD5W2WP_E138` | `contains` | 05-Fault Mode | imbalance |  | 06-Fault Severity | Single Severity |  |
| 4 | `TYD5W2WP_E139` | `contains` | 05-Fault Mode | loose bearing housing |  | 06-Fault Severity | Single Severity |  |
| 5 | `TYD5W2WP_E140` | `contains` | 05-Fault Mode | shaft misalignment |  | 06-Fault Severity | Single Severity |  |
| 6 | `TYD5W2WP_E141` | `contains` | 05-Fault Mode | cavitation |  | 06-Fault Severity | Single Severity |  |
| 7 | `TYD5W2WP_E142` | `contains_phm_task` | 02-Object Type | industrial fan |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 8 | `TYD5W2WP_E143` | `contains_phm_task` | 02-Object Type | centrifugal pump |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 9 | `TYD5W2WP_E144` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `TYD5W2WP_E145` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `TYD5W2WP_E146` | `contains_phm_task` | 04-Fault Location | shaft |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `TYD5W2WP_E147` | `contains_phm_task` | 04-Fault Location | blade |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `TYD5W2WP_E148` | `contains_phm_task` | 04-Fault Location | impeller |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `TYD5W2WP_E149` | `contains_phm_task` | 05-Fault Mode | flaking |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `TYD5W2WP_E150` | `contains_phm_task` | 05-Fault Mode | defect |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `TYD5W2WP_E151` | `contains_phm_task` | 05-Fault Mode | imbalance |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `TYD5W2WP_E152` | `contains_phm_task` | 05-Fault Mode | loose bearing housing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `TYD5W2WP_E153` | `contains_phm_task` | 05-Fault Mode | shaft misalignment |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `TYD5W2WP_E154` | `contains_phm_task` | 05-Fault Mode | cavitation |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `TYD5W2WP_E156` | `induces_problem` | 02-Object Type | industrial fan |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 21 | `TYD5W2WP_E157` | `induces_problem` | 02-Object Type | centrifugal pump |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 22 | `TYD5W2WP_E158` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 23 | `TYD5W2WP_E159` | `induces_problem` | 03-Operating Conditions | 800 rpm, 2000 rpm, 3000 rpm(Multiple Conditions) |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 24 | `TYD5W2WP_E160` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 25 | `TYD5W2WP_E161` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 26 | `TYD5W2WP_E162` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 27 | `TYD5W2WP_E163` | `induces_problem` | 12-Training Data Availability | Among the 10,800 measured signal samples, 9,000 samples, which were evenly selected from the nine types, were used to train the model.(Sufficient) |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 28 | `TYD5W2WP_E164` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |
| 29 | `TYD5W2WP_E165` | `induces_problem` | 14-Computational Resource | without incurring an additional computational burden, reduces the complexity of the FAC-CNN(Low Resource Consumption) |  | 09-Problem Scenario | multiple source data fusion(Multi-Source Heterogeneous / Multimodal Data) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 29 edges)*
