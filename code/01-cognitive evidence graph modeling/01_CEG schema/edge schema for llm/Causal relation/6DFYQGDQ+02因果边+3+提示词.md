# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：6DFYQGDQ
- **Paper Title**：Refined composite multivariate multiscale symbolic dynamic entropy and its application to fault diagnosis of rotating machine
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `6DFYQGDQ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "6DFYQGDQ_E139", "edge_description": "crack contains_phm_task fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E140", "edge_description": "corrosive pitting contains_phm_task fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E141", "edge_description": "damage contains_phm_task fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E142", "edge_description": "defect contains_phm_task fault diagnosis"},
    {"edge_id": "6DFYQGDQ_E144", "edge_description": "centrifugal pump induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E145", "edge_description": "centrifugal pump induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E146", "edge_description": "centrifugal pump induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E147", "edge_description": "ball bearing induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E148", "edge_description": "ball bearing induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E149", "edge_description": "ball bearing induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E150", "edge_description": "constant speed conditions, time-varying speed conditions induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E151", "edge_description": "constant speed conditions, time-varying speed conditions induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E152", "edge_description": "constant speed conditions, time-varying speed conditions induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E153", "edge_description": "fault size less than 0.5mm, fault size of 2*3mm2 induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E154", "edge_description": "fault size less than 0.5mm, fault size of 2*3mm2 induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E155", "edge_description": "fault size less than 0.5mm, fault size of 2*3mm2 induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E156", "edge_description": "No Compound Fault induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E157", "edge_description": "No Compound Fault induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E158", "edge_description": "No Compound Fault induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E159", "edge_description": "fault diagnosis induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E160", "edge_description": "fault diagnosis induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E161", "edge_description": "fault diagnosis induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E162", "edge_description": "Training samples: 200 per class (Case 1), 960 per class (Case 2) induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E163", "edge_description": "Training samples: 200 per class (Case 1), 960 per class (Case 2) induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E164", "edge_description": "Training samples: 200 per class (Case 1), 960 per class (Case 2) induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E165", "edge_description": "synthetic signals with noise, resist the influence of noise and fluctuations induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E166", "edge_description": "synthetic signals with noise, resist the influence of noise and fluctuations induces_problem time-varying speed conditions"},
    {"edge_id": "6DFYQGDQ_E167", "edge_description": "synthetic signals with noise, resist the influence of noise and fluctuations induces_problem noise robustness"},
    {"edge_id": "6DFYQGDQ_E168", "edge_description": "computational efficiency, CPU time induces_problem multivariate signals, multisensory system"},
    {"edge_id": "6DFYQGDQ_E169", "edge_description": "computational efficiency, CPU time induces_problem time-varying speed conditions"}
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
| 1 | `6DFYQGDQ_E139` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 2 | `6DFYQGDQ_E140` | `contains_phm_task` | 05-Fault Mode | corrosive pitting |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 3 | `6DFYQGDQ_E141` | `contains_phm_task` | 05-Fault Mode | damage |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 4 | `6DFYQGDQ_E142` | `contains_phm_task` | 05-Fault Mode | defect |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 5 | `6DFYQGDQ_E144` | `induces_problem` | 02-Object Type | centrifugal pump |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 6 | `6DFYQGDQ_E145` | `induces_problem` | 02-Object Type | centrifugal pump |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 7 | `6DFYQGDQ_E146` | `induces_problem` | 02-Object Type | centrifugal pump |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 8 | `6DFYQGDQ_E147` | `induces_problem` | 02-Object Type | ball bearing |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 9 | `6DFYQGDQ_E148` | `induces_problem` | 02-Object Type | ball bearing |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 10 | `6DFYQGDQ_E149` | `induces_problem` | 02-Object Type | ball bearing |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 11 | `6DFYQGDQ_E150` | `induces_problem` | 03-Operating Conditions | constant speed conditions, time-varying speed conditions(Variable Conditions) |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 12 | `6DFYQGDQ_E151` | `induces_problem` | 03-Operating Conditions | constant speed conditions, time-varying speed conditions(Variable Conditions) |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 13 | `6DFYQGDQ_E152` | `induces_problem` | 03-Operating Conditions | constant speed conditions, time-varying speed conditions(Variable Conditions) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 14 | `6DFYQGDQ_E153` | `induces_problem` | 06-Fault Severity | fault size less than 0.5mm, fault size of 2*3mm2(Single Severity) |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 15 | `6DFYQGDQ_E154` | `induces_problem` | 06-Fault Severity | fault size less than 0.5mm, fault size of 2*3mm2(Single Severity) |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 16 | `6DFYQGDQ_E155` | `induces_problem` | 06-Fault Severity | fault size less than 0.5mm, fault size of 2*3mm2(Single Severity) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 17 | `6DFYQGDQ_E156` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 18 | `6DFYQGDQ_E157` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 19 | `6DFYQGDQ_E158` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 20 | `6DFYQGDQ_E159` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 21 | `6DFYQGDQ_E160` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 22 | `6DFYQGDQ_E161` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 23 | `6DFYQGDQ_E162` | `induces_problem` | 12-Training Data Availability | Training samples: 200 per class (Case 1), 960 per class (Case 2)(Sufficient) |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 24 | `6DFYQGDQ_E163` | `induces_problem` | 12-Training Data Availability | Training samples: 200 per class (Case 1), 960 per class (Case 2)(Sufficient) |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 25 | `6DFYQGDQ_E164` | `induces_problem` | 12-Training Data Availability | Training samples: 200 per class (Case 1), 960 per class (Case 2)(Sufficient) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 26 | `6DFYQGDQ_E165` | `induces_problem` | 13-Noise Level | synthetic signals with noise, resist the influence of noise and fluctuations(High Noise) |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 27 | `6DFYQGDQ_E166` | `induces_problem` | 13-Noise Level | synthetic signals with noise, resist the influence of noise and fluctuations(High Noise) |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |
| 28 | `6DFYQGDQ_E167` | `induces_problem` | 13-Noise Level | synthetic signals with noise, resist the influence of noise and fluctuations(High Noise) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 29 | `6DFYQGDQ_E168` | `induces_problem` | 14-Computational Resource | computational efficiency, CPU time(Low Resource Consumption) |  | 09-Problem Scenario | multivariate signals, multisensory system(Multi-Source Heterogeneous / Multimodal Data) |  |
| 30 | `6DFYQGDQ_E169` | `induces_problem` | 14-Computational Resource | computational efficiency, CPU time(Low Resource Consumption) |  | 09-Problem Scenario | time-varying speed conditions(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
