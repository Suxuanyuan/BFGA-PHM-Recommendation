# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：4TXMIDZ8
- **Paper Title**：Research on Fault Feature Extraction Method of Rolling Bearing Based on NMD and Wavelet Threshold Denoising
- **Number of Candidate Edges to Judge**：26 

---

## II. LLM Input

> **Input Material**: Reference ID `4TXMIDZ8`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "4TXMIDZ8_E053", "edge_description": "rolling bearing contains inner race"},
    {"edge_id": "4TXMIDZ8_E054", "edge_description": "rolling bearing contains outer race"},
    {"edge_id": "4TXMIDZ8_E057", "edge_description": "accelerometer is collected on inner race"},
    {"edge_id": "4TXMIDZ8_E058", "edge_description": "accelerometer is collected on outer race"},
    {"edge_id": "4TXMIDZ8_E060", "edge_description": "real motor bearing data provided by Case Western Reserve University can be used for fault diagnosis"},
    {"edge_id": "4TXMIDZ8_E061", "edge_description": "simulation experiment can be used for fault diagnosis"},
    {"edge_id": "4TXMIDZ8_E062", "edge_description": "inner race has_fault_mode single point faults"},
    {"edge_id": "4TXMIDZ8_E063", "edge_description": "outer race has_fault_mode single point faults"},
    {"edge_id": "4TXMIDZ8_E066", "edge_description": "inner race contains_phm_task fault diagnosis"},
    {"edge_id": "4TXMIDZ8_E067", "edge_description": "outer race contains_phm_task fault diagnosis"},
    {"edge_id": "4TXMIDZ8_E070", "edge_description": "rolling bearing induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E071", "edge_description": "rolling bearing induces_problem parameter sensitivity"},
    {"edge_id": "4TXMIDZ8_E072", "edge_description": "motor speed was 1797 rpm induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E073", "edge_description": "motor speed was 1797 rpm induces_problem parameter sensitivity"},
    {"edge_id": "4TXMIDZ8_E074", "edge_description": "fault diameter of 0.021 inches, fault depth of 0.011 inches induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E075", "edge_description": "fault diameter of 0.021 inches, fault depth of 0.011 inches induces_problem parameter sensitivity"},
    {"edge_id": "4TXMIDZ8_E076", "edge_description": "No Compound Fault induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E077", "edge_description": "No Compound Fault induces_problem parameter sensitivity"},
    {"edge_id": "4TXMIDZ8_E078", "edge_description": "fault diagnosis induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E079", "edge_description": "fault diagnosis induces_problem parameter sensitivity"},
    {"edge_id": "4TXMIDZ8_E080", "edge_description": "Sufficient induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E081", "edge_description": "Sufficient induces_problem parameter sensitivity"},
    {"edge_id": "4TXMIDZ8_E082", "edge_description": "mixed with serious noise induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E083", "edge_description": "mixed with serious noise induces_problem parameter sensitivity"},
    {"edge_id": "4TXMIDZ8_E084", "edge_description": "shorter processing time and higher diagnostic efficiency induces_problem noise robustness"},
    {"edge_id": "4TXMIDZ8_E085", "edge_description": "shorter processing time and higher diagnostic efficiency induces_problem parameter sensitivity"}
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
| 1 | `4TXMIDZ8_E053` | `contains` | 02-Object Type | rolling bearing |  | 04-Fault Location | inner race |  |
| 2 | `4TXMIDZ8_E054` | `contains` | 02-Object Type | rolling bearing |  | 04-Fault Location | outer race |  |
| 3 | `4TXMIDZ8_E057` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | inner race |  |
| 4 | `4TXMIDZ8_E058` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | outer race |  |
| 5 | `4TXMIDZ8_E060` | `can be used for` | 10-Dataset | real motor bearing data provided by Case Western Reserve University |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 6 | `4TXMIDZ8_E061` | `can be used for` | 10-Dataset | simulation experiment |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 7 | `4TXMIDZ8_E062` | `has_fault_mode` | 04-Fault Location | inner race |  | 05-Fault Mode | single point faults |  |
| 8 | `4TXMIDZ8_E063` | `has_fault_mode` | 04-Fault Location | outer race |  | 05-Fault Mode | single point faults |  |
| 9 | `4TXMIDZ8_E066` | `contains_phm_task` | 04-Fault Location | inner race |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `4TXMIDZ8_E067` | `contains_phm_task` | 04-Fault Location | outer race |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `4TXMIDZ8_E070` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 12 | `4TXMIDZ8_E071` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | parameter sensitivity(Other) |  |
| 13 | `4TXMIDZ8_E072` | `induces_problem` | 03-Operating Conditions | motor speed was 1797 rpm(Single Condition) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 14 | `4TXMIDZ8_E073` | `induces_problem` | 03-Operating Conditions | motor speed was 1797 rpm(Single Condition) |  | 09-Problem Scenario | parameter sensitivity(Other) |  |
| 15 | `4TXMIDZ8_E074` | `induces_problem` | 06-Fault Severity | fault diameter of 0.021 inches, fault depth of 0.011 inches(Single Severity) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 16 | `4TXMIDZ8_E075` | `induces_problem` | 06-Fault Severity | fault diameter of 0.021 inches, fault depth of 0.011 inches(Single Severity) |  | 09-Problem Scenario | parameter sensitivity(Other) |  |
| 17 | `4TXMIDZ8_E076` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 18 | `4TXMIDZ8_E077` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | parameter sensitivity(Other) |  |
| 19 | `4TXMIDZ8_E078` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 20 | `4TXMIDZ8_E079` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | parameter sensitivity(Other) |  |
| 21 | `4TXMIDZ8_E080` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 22 | `4TXMIDZ8_E081` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | parameter sensitivity(Other) |  |
| 23 | `4TXMIDZ8_E082` | `induces_problem` | 13-Noise Level | mixed with serious noise(High Noise) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 24 | `4TXMIDZ8_E083` | `induces_problem` | 13-Noise Level | mixed with serious noise(High Noise) |  | 09-Problem Scenario | parameter sensitivity(Other) |  |
| 25 | `4TXMIDZ8_E084` | `induces_problem` | 14-Computational Resource | shorter processing time and higher diagnostic efficiency(Low Resource Consumption) |  | 09-Problem Scenario | noise robustness(Uncertainty) |  |
| 26 | `4TXMIDZ8_E085` | `induces_problem` | 14-Computational Resource | shorter processing time and higher diagnostic efficiency(Low Resource Consumption) |  | 09-Problem Scenario | parameter sensitivity(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 26 edges)*
