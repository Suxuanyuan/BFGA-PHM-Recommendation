# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：XSVHIQI8
- **Paper Title**：Least-Squares Fault Detection and Diagnosis for Networked Sensing Systems Using A Direct State Estimation Approach
- **Number of Candidate Edges to Judge**：28 

---

## II. LLM Input

> **Input Material**: Reference ID `XSVHIQI8`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "XSVHIQI8_E019", "edge_description": "three-tank system contains Tank 1"},
    {"edge_id": "XSVHIQI8_E020", "edge_description": "three-tank system contains Tank 2"},
    {"edge_id": "XSVHIQI8_E021", "edge_description": "three-tank system contains Tank 3"},
    {"edge_id": "XSVHIQI8_E024", "edge_description": "level sensor is collected on Tank 1"},
    {"edge_id": "XSVHIQI8_E025", "edge_description": "level sensor is collected on Tank 2"},
    {"edge_id": "XSVHIQI8_E026", "edge_description": "level sensor is collected on Tank 3"},
    {"edge_id": "XSVHIQI8_E029", "edge_description": "Tank 1 has_fault_mode leakage"},
    {"edge_id": "XSVHIQI8_E030", "edge_description": "Tank 2 has_fault_mode leakage"},
    {"edge_id": "XSVHIQI8_E031", "edge_description": "Tank 3 has_fault_mode leakage"},
    {"edge_id": "XSVHIQI8_E034", "edge_description": "Tank 1 contains_phm_task fault detection, isolation, and estimation"},
    {"edge_id": "XSVHIQI8_E035", "edge_description": "Tank 2 contains_phm_task fault detection, isolation, and estimation"},
    {"edge_id": "XSVHIQI8_E036", "edge_description": "Tank 3 contains_phm_task fault detection, isolation, and estimation"},
    {"edge_id": "XSVHIQI8_E039", "edge_description": "three-tank system induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E040", "edge_description": "three-tank system induces_problem time-varying systems"},
    {"edge_id": "XSVHIQI8_E041", "edge_description": "time-varying parameters induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E042", "edge_description": "time-varying parameters induces_problem time-varying systems"},
    {"edge_id": "XSVHIQI8_E043", "edge_description": "amplitude about 1.0 * 10^-4 m^3/s induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E044", "edge_description": "amplitude about 1.0 * 10^-4 m^3/s induces_problem time-varying systems"},
    {"edge_id": "XSVHIQI8_E045", "edge_description": "No Compound Fault induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E046", "edge_description": "No Compound Fault induces_problem time-varying systems"},
    {"edge_id": "XSVHIQI8_E047", "edge_description": "fault detection, isolation, and estimation induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E048", "edge_description": "fault detection, isolation, and estimation induces_problem time-varying systems"},
    {"edge_id": "XSVHIQI8_E049", "edge_description": "recursive filter design induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E050", "edge_description": "recursive filter design induces_problem time-varying systems"},
    {"edge_id": "XSVHIQI8_E051", "edge_description": "external disturbances and transmission noise induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E052", "edge_description": "external disturbances and transmission noise induces_problem time-varying systems"},
    {"edge_id": "XSVHIQI8_E053", "edge_description": "recursive algorithm suitable for online applications induces_problem delayed and missing measurements"},
    {"edge_id": "XSVHIQI8_E054", "edge_description": "recursive algorithm suitable for online applications induces_problem time-varying systems"}
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
| 1 | `XSVHIQI8_E019` | `contains` | 02-Object Type | three-tank system |  | 04-Fault Location | Tank 1 |  |
| 2 | `XSVHIQI8_E020` | `contains` | 02-Object Type | three-tank system |  | 04-Fault Location | Tank 2 |  |
| 3 | `XSVHIQI8_E021` | `contains` | 02-Object Type | three-tank system |  | 04-Fault Location | Tank 3 |  |
| 4 | `XSVHIQI8_E024` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | Tank 1 |  |
| 5 | `XSVHIQI8_E025` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | Tank 2 |  |
| 6 | `XSVHIQI8_E026` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | Tank 3 |  |
| 7 | `XSVHIQI8_E029` | `has_fault_mode` | 04-Fault Location | Tank 1 |  | 05-Fault Mode | leakage |  |
| 8 | `XSVHIQI8_E030` | `has_fault_mode` | 04-Fault Location | Tank 2 |  | 05-Fault Mode | leakage |  |
| 9 | `XSVHIQI8_E031` | `has_fault_mode` | 04-Fault Location | Tank 3 |  | 05-Fault Mode | leakage |  |
| 10 | `XSVHIQI8_E034` | `contains_phm_task` | 04-Fault Location | Tank 1 |  | 08-PHM Task | fault detection, isolation, and estimation(Diagnosis Task) |  |
| 11 | `XSVHIQI8_E035` | `contains_phm_task` | 04-Fault Location | Tank 2 |  | 08-PHM Task | fault detection, isolation, and estimation(Diagnosis Task) |  |
| 12 | `XSVHIQI8_E036` | `contains_phm_task` | 04-Fault Location | Tank 3 |  | 08-PHM Task | fault detection, isolation, and estimation(Diagnosis Task) |  |
| 13 | `XSVHIQI8_E039` | `induces_problem` | 02-Object Type | three-tank system |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 14 | `XSVHIQI8_E040` | `induces_problem` | 02-Object Type | three-tank system |  | 09-Problem Scenario | time-varying systems(Other) |  |
| 15 | `XSVHIQI8_E041` | `induces_problem` | 03-Operating Conditions | time-varying parameters(Variable Conditions) |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 16 | `XSVHIQI8_E042` | `induces_problem` | 03-Operating Conditions | time-varying parameters(Variable Conditions) |  | 09-Problem Scenario | time-varying systems(Other) |  |
| 17 | `XSVHIQI8_E043` | `induces_problem` | 06-Fault Severity | amplitude about 1.0 * 10^-4 m^3/s(Single Severity) |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 18 | `XSVHIQI8_E044` | `induces_problem` | 06-Fault Severity | amplitude about 1.0 * 10^-4 m^3/s(Single Severity) |  | 09-Problem Scenario | time-varying systems(Other) |  |
| 19 | `XSVHIQI8_E045` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 20 | `XSVHIQI8_E046` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | time-varying systems(Other) |  |
| 21 | `XSVHIQI8_E047` | `induces_problem` | 08-PHM Task | fault detection, isolation, and estimation(Diagnosis Task) |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 22 | `XSVHIQI8_E048` | `induces_problem` | 08-PHM Task | fault detection, isolation, and estimation(Diagnosis Task) |  | 09-Problem Scenario | time-varying systems(Other) |  |
| 23 | `XSVHIQI8_E049` | `induces_problem` | 12-Training Data Availability | recursive filter design(Sufficient) |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 24 | `XSVHIQI8_E050` | `induces_problem` | 12-Training Data Availability | recursive filter design(Sufficient) |  | 09-Problem Scenario | time-varying systems(Other) |  |
| 25 | `XSVHIQI8_E051` | `induces_problem` | 13-Noise Level | external disturbances and transmission noise(High Noise) |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 26 | `XSVHIQI8_E052` | `induces_problem` | 13-Noise Level | external disturbances and transmission noise(High Noise) |  | 09-Problem Scenario | time-varying systems(Other) |  |
| 27 | `XSVHIQI8_E053` | `induces_problem` | 14-Computational Resource | recursive algorithm suitable for online applications(Low Resource Consumption) |  | 09-Problem Scenario | delayed and missing measurements(Uncertainty) |  |
| 28 | `XSVHIQI8_E054` | `induces_problem` | 14-Computational Resource | recursive algorithm suitable for online applications(Low Resource Consumption) |  | 09-Problem Scenario | time-varying systems(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 28 edges)*
