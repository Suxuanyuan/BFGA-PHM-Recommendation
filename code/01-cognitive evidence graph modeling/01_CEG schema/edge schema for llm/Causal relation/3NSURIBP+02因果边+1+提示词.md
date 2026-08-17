# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：3NSURIBP
- **Paper Title**：Fault detection of rolling element bearings using optimal segmentation of vibrating signals
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `3NSURIBP`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "3NSURIBP_E056", "edge_description": "rolling element bearings contains inner race"},
    {"edge_id": "3NSURIBP_E057", "edge_description": "rolling element bearings contains ball"},
    {"edge_id": "3NSURIBP_E058", "edge_description": "rolling element bearings contains outer race"},
    {"edge_id": "3NSURIBP_E061", "edge_description": "transducer is collected on inner race"},
    {"edge_id": "3NSURIBP_E062", "edge_description": "transducer is collected on ball"},
    {"edge_id": "3NSURIBP_E063", "edge_description": "transducer is collected on outer race"},
    {"edge_id": "3NSURIBP_E065", "edge_description": "Case Western Reserve University Bearing Data Center can be used for fault detection"},
    {"edge_id": "3NSURIBP_E066", "edge_description": "Monte Carlo simulation data can be used for fault detection"},
    {"edge_id": "3NSURIBP_E067", "edge_description": "inner race has_fault_mode localized defect"},
    {"edge_id": "3NSURIBP_E068", "edge_description": "ball has_fault_mode localized defect"},
    {"edge_id": "3NSURIBP_E069", "edge_description": "outer race has_fault_mode localized defect"},
    {"edge_id": "3NSURIBP_E072", "edge_description": "inner race contains_phm_task fault detection"},
    {"edge_id": "3NSURIBP_E073", "edge_description": "ball contains_phm_task fault detection"},
    {"edge_id": "3NSURIBP_E074", "edge_description": "outer race contains_phm_task fault detection"},
    {"edge_id": "3NSURIBP_E077", "edge_description": "rolling element bearings induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E078", "edge_description": "rolling element bearings induces_problem gradual change detection"},
    {"edge_id": "3NSURIBP_E079", "edge_description": "constant operating condition induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E080", "edge_description": "constant operating condition induces_problem gradual change detection"},
    {"edge_id": "3NSURIBP_E081", "edge_description": "0.007 inch, 0.014 inch, 0.021 inch, 0.028 inch induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E082", "edge_description": "0.007 inch, 0.014 inch, 0.021 inch, 0.028 inch induces_problem gradual change detection"},
    {"edge_id": "3NSURIBP_E083", "edge_description": "No Compound Fault induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E084", "edge_description": "No Compound Fault induces_problem gradual change detection"},
    {"edge_id": "3NSURIBP_E085", "edge_description": "fault detection induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E086", "edge_description": "fault detection induces_problem gradual change detection"},
    {"edge_id": "3NSURIBP_E087", "edge_description": "4096 samples per vector, concatenated to 8192, 16384 and 20480 samples induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E088", "edge_description": "4096 samples per vector, concatenated to 8192, 16384 and 20480 samples induces_problem gradual change detection"},
    {"edge_id": "3NSURIBP_E089", "edge_description": "white Gaussian noise, disturbances, noise scaling induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E090", "edge_description": "white Gaussian noise, disturbances, noise scaling induces_problem gradual change detection"},
    {"edge_id": "3NSURIBP_E091", "edge_description": "MCMC numerical search, dynamic programming induces_problem noise and disturbance robustness"},
    {"edge_id": "3NSURIBP_E092", "edge_description": "MCMC numerical search, dynamic programming induces_problem gradual change detection"}
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
| 1 | `3NSURIBP_E056` | `contains` | 02-Object Type | rolling element bearings |  | 04-Fault Location | inner race |  |
| 2 | `3NSURIBP_E057` | `contains` | 02-Object Type | rolling element bearings |  | 04-Fault Location | ball |  |
| 3 | `3NSURIBP_E058` | `contains` | 02-Object Type | rolling element bearings |  | 04-Fault Location | outer race |  |
| 4 | `3NSURIBP_E061` | `is collected on` | 11-Sensor Information | transducer |  | 04-Fault Location | inner race |  |
| 5 | `3NSURIBP_E062` | `is collected on` | 11-Sensor Information | transducer |  | 04-Fault Location | ball |  |
| 6 | `3NSURIBP_E063` | `is collected on` | 11-Sensor Information | transducer |  | 04-Fault Location | outer race |  |
| 7 | `3NSURIBP_E065` | `can be used for` | 10-Dataset | Case Western Reserve University Bearing Data Center |  | 08-PHM Task | fault detection(Detection Task) |  |
| 8 | `3NSURIBP_E066` | `can be used for` | 10-Dataset | Monte Carlo simulation data |  | 08-PHM Task | fault detection(Detection Task) |  |
| 9 | `3NSURIBP_E067` | `has_fault_mode` | 04-Fault Location | inner race |  | 05-Fault Mode | localized defect |  |
| 10 | `3NSURIBP_E068` | `has_fault_mode` | 04-Fault Location | ball |  | 05-Fault Mode | localized defect |  |
| 11 | `3NSURIBP_E069` | `has_fault_mode` | 04-Fault Location | outer race |  | 05-Fault Mode | localized defect |  |
| 12 | `3NSURIBP_E072` | `contains_phm_task` | 04-Fault Location | inner race |  | 08-PHM Task | fault detection(Detection Task) |  |
| 13 | `3NSURIBP_E073` | `contains_phm_task` | 04-Fault Location | ball |  | 08-PHM Task | fault detection(Detection Task) |  |
| 14 | `3NSURIBP_E074` | `contains_phm_task` | 04-Fault Location | outer race |  | 08-PHM Task | fault detection(Detection Task) |  |
| 15 | `3NSURIBP_E077` | `induces_problem` | 02-Object Type | rolling element bearings |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 16 | `3NSURIBP_E078` | `induces_problem` | 02-Object Type | rolling element bearings |  | 09-Problem Scenario | gradual change detection(Other) |  |
| 17 | `3NSURIBP_E079` | `induces_problem` | 03-Operating Conditions | constant operating condition(Single Condition) |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 18 | `3NSURIBP_E080` | `induces_problem` | 03-Operating Conditions | constant operating condition(Single Condition) |  | 09-Problem Scenario | gradual change detection(Other) |  |
| 19 | `3NSURIBP_E081` | `induces_problem` | 06-Fault Severity | 0.007 inch, 0.014 inch, 0.021 inch, 0.028 inch(Multiple Severities) |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 20 | `3NSURIBP_E082` | `induces_problem` | 06-Fault Severity | 0.007 inch, 0.014 inch, 0.021 inch, 0.028 inch(Multiple Severities) |  | 09-Problem Scenario | gradual change detection(Other) |  |
| 21 | `3NSURIBP_E083` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 22 | `3NSURIBP_E084` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | gradual change detection(Other) |  |
| 23 | `3NSURIBP_E085` | `induces_problem` | 08-PHM Task | fault detection(Detection Task) |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 24 | `3NSURIBP_E086` | `induces_problem` | 08-PHM Task | fault detection(Detection Task) |  | 09-Problem Scenario | gradual change detection(Other) |  |
| 25 | `3NSURIBP_E087` | `induces_problem` | 12-Training Data Availability | 4096 samples per vector, concatenated to 8192, 16384 and 20480 samples(Sufficient) |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 26 | `3NSURIBP_E088` | `induces_problem` | 12-Training Data Availability | 4096 samples per vector, concatenated to 8192, 16384 and 20480 samples(Sufficient) |  | 09-Problem Scenario | gradual change detection(Other) |  |
| 27 | `3NSURIBP_E089` | `induces_problem` | 13-Noise Level | white Gaussian noise, disturbances, noise scaling(High Noise) |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 28 | `3NSURIBP_E090` | `induces_problem` | 13-Noise Level | white Gaussian noise, disturbances, noise scaling(High Noise) |  | 09-Problem Scenario | gradual change detection(Other) |  |
| 29 | `3NSURIBP_E091` | `induces_problem` | 14-Computational Resource | MCMC numerical search, dynamic programming |  | 09-Problem Scenario | noise and disturbance robustness(Uncertainty) |  |
| 30 | `3NSURIBP_E092` | `induces_problem` | 14-Computational Resource | MCMC numerical search, dynamic programming |  | 09-Problem Scenario | gradual change detection(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
