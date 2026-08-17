# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：77QNBQRB
- **Paper Title**：Early Fault Detection of Machine Tools Based on Deep Learning and Dynamic Identification
- **Number of Candidate Edges to Judge**：26 

---

## II. LLM Input

> **Input Material**: Reference ID `77QNBQRB`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "77QNBQRB_E049", "edge_description": "CNC machine tool manufacturing contains CNC machining center"},
    {"edge_id": "77QNBQRB_E050", "edge_description": "CNC machine tool manufacturing contains ball screw"},
    {"edge_id": "77QNBQRB_E051", "edge_description": "CNC machining center contains ball screw"},
    {"edge_id": "77QNBQRB_E052", "edge_description": "ball screw contains ball screw"},
    {"edge_id": "77QNBQRB_E053", "edge_description": "CNC machining center contains time-varying working conditions"},
    {"edge_id": "77QNBQRB_E054", "edge_description": "ball screw contains time-varying working conditions"},
    {"edge_id": "77QNBQRB_E061", "edge_description": "CNC machining center contains_phm_task early fault detection"},
    {"edge_id": "77QNBQRB_E062", "edge_description": "ball screw contains_phm_task early fault detection"},
    {"edge_id": "77QNBQRB_E066", "edge_description": "CNC machining center induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E067", "edge_description": "CNC machining center induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E068", "edge_description": "ball screw induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E069", "edge_description": "ball screw induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E070", "edge_description": "time-varying working conditions induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E071", "edge_description": "time-varying working conditions induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E072", "edge_description": "health, slight deterioration, rapid deterioration and severe deterioration induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E073", "edge_description": "health, slight deterioration, rapid deterioration and severe deterioration induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E074", "edge_description": "No Compound Fault induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E075", "edge_description": "No Compound Fault induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E076", "edge_description": "early fault detection induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E077", "edge_description": "early fault detection induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E078", "edge_description": "9000 samples are randomly selected for training induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E079", "edge_description": "9000 samples are randomly selected for training induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E080", "edge_description": "fault features are often weakened and disturbed by the time-varying harmonics and noise during machining induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E081", "edge_description": "fault features are often weakened and disturbed by the time-varying harmonics and noise during machining induces_problem early fault detection and tracing the slight fault features"},
    {"edge_id": "77QNBQRB_E082", "edge_description": "The vibration data volume is huge thus the computational burden is considerable induces_problem different feature spaces and different distributions caused by non-stationary conditions"},
    {"edge_id": "77QNBQRB_E083", "edge_description": "The vibration data volume is huge thus the computational burden is considerable induces_problem early fault detection and tracing the slight fault features"}
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
| 1 | `77QNBQRB_E049` | `contains` | 01-Object Domain | CNC machine tool manufacturing(Industrial) |  | 02-Object Type | CNC machining center |  |
| 2 | `77QNBQRB_E050` | `contains` | 01-Object Domain | CNC machine tool manufacturing(Industrial) |  | 02-Object Type | ball screw |  |
| 3 | `77QNBQRB_E051` | `contains` | 02-Object Type | CNC machining center |  | 04-Fault Location | ball screw |  |
| 4 | `77QNBQRB_E052` | `contains` | 02-Object Type | ball screw |  | 04-Fault Location | ball screw |  |
| 5 | `77QNBQRB_E053` | `contains` | 02-Object Type | CNC machining center |  | 03-Operating Conditions | time-varying working conditions(Variable Conditions) |  |
| 6 | `77QNBQRB_E054` | `contains` | 02-Object Type | ball screw |  | 03-Operating Conditions | time-varying working conditions(Variable Conditions) |  |
| 7 | `77QNBQRB_E061` | `contains_phm_task` | 02-Object Type | CNC machining center |  | 08-PHM Task | early fault detection(Detection Task) |  |
| 8 | `77QNBQRB_E062` | `contains_phm_task` | 02-Object Type | ball screw |  | 08-PHM Task | early fault detection(Detection Task) |  |
| 9 | `77QNBQRB_E066` | `induces_problem` | 02-Object Type | CNC machining center |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 10 | `77QNBQRB_E067` | `induces_problem` | 02-Object Type | CNC machining center |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 11 | `77QNBQRB_E068` | `induces_problem` | 02-Object Type | ball screw |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 12 | `77QNBQRB_E069` | `induces_problem` | 02-Object Type | ball screw |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 13 | `77QNBQRB_E070` | `induces_problem` | 03-Operating Conditions | time-varying working conditions(Variable Conditions) |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 14 | `77QNBQRB_E071` | `induces_problem` | 03-Operating Conditions | time-varying working conditions(Variable Conditions) |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 15 | `77QNBQRB_E072` | `induces_problem` | 06-Fault Severity | health, slight deterioration, rapid deterioration and severe deterioration(Multiple Severities) |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 16 | `77QNBQRB_E073` | `induces_problem` | 06-Fault Severity | health, slight deterioration, rapid deterioration and severe deterioration(Multiple Severities) |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 17 | `77QNBQRB_E074` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 18 | `77QNBQRB_E075` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 19 | `77QNBQRB_E076` | `induces_problem` | 08-PHM Task | early fault detection(Detection Task) |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 20 | `77QNBQRB_E077` | `induces_problem` | 08-PHM Task | early fault detection(Detection Task) |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 21 | `77QNBQRB_E078` | `induces_problem` | 12-Training Data Availability | 9000 samples are randomly selected for training(Sufficient) |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 22 | `77QNBQRB_E079` | `induces_problem` | 12-Training Data Availability | 9000 samples are randomly selected for training(Sufficient) |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 23 | `77QNBQRB_E080` | `induces_problem` | 13-Noise Level | fault features are often weakened and disturbed by the time-varying harmonics and noise during machining(High Noise) |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 24 | `77QNBQRB_E081` | `induces_problem` | 13-Noise Level | fault features are often weakened and disturbed by the time-varying harmonics and noise during machining(High Noise) |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |
| 25 | `77QNBQRB_E082` | `induces_problem` | 14-Computational Resource | The vibration data volume is huge thus the computational burden is considerable(High Resource Consumption) |  | 09-Problem Scenario | different feature spaces and different distributions caused by non-stationary conditions(Distribution Discrepancy) |  |
| 26 | `77QNBQRB_E083` | `induces_problem` | 14-Computational Resource | The vibration data volume is huge thus the computational burden is considerable(High Resource Consumption) |  | 09-Problem Scenario | early fault detection and tracing the slight fault features(Early Degradation Prediction) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 26 edges)*
