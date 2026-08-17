# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：IDP29JMR
- **Paper Title**：Rotor resistance estimation using Extended Kalman filter and spectral analysis for rotor bar fault diagnosis of sensorless vector control induction motor
- **Number of Candidate Edges to Judge**：24 

---

## II. LLM Input

> **Input Material**: Reference ID `IDP29JMR`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "IDP29JMR_E041", "edge_description": "Hall type current sensors is collected on rotor bar"},
    {"edge_id": "IDP29JMR_E042", "edge_description": "voltage sensors is collected on rotor bar"},
    {"edge_id": "IDP29JMR_E043", "edge_description": "Incremental encoder is collected on rotor bar"},
    {"edge_id": "IDP29JMR_E044", "edge_description": "Hall type current sensors can obviously reflect broken rotor bar"},
    {"edge_id": "IDP29JMR_E045", "edge_description": "voltage sensors can obviously reflect broken rotor bar"},
    {"edge_id": "IDP29JMR_E046", "edge_description": "Incremental encoder can obviously reflect broken rotor bar"},
    {"edge_id": "IDP29JMR_E047", "edge_description": "Simulation data can be used for fault diagnosis"},
    {"edge_id": "IDP29JMR_E048", "edge_description": "Experimental data can be used for fault diagnosis"},
    {"edge_id": "IDP29JMR_E055", "edge_description": "Induction motor induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E056", "edge_description": "Induction motor induces_problem closed-loop control masks the fault effect"},
    {"edge_id": "IDP29JMR_E057", "edge_description": "variable speed operating, rated load, reverse speed, low speed regions induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E058", "edge_description": "variable speed operating, rated load, reverse speed, low speed regions induces_problem closed-loop control masks the fault effect"},
    {"edge_id": "IDP29JMR_E059", "edge_description": "adjacent two broken rotor bars, 3.1mm diameter hole induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E060", "edge_description": "adjacent two broken rotor bars, 3.1mm diameter hole induces_problem closed-loop control masks the fault effect"},
    {"edge_id": "IDP29JMR_E061", "edge_description": "No Compound Fault induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E062", "edge_description": "No Compound Fault induces_problem closed-loop control masks the fault effect"},
    {"edge_id": "IDP29JMR_E063", "edge_description": "fault diagnosis induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E064", "edge_description": "fault diagnosis induces_problem closed-loop control masks the fault effect"},
    {"edge_id": "IDP29JMR_E065", "edge_description": "Not explicitly mentioned induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E066", "edge_description": "Not explicitly mentioned induces_problem closed-loop control masks the fault effect"},
    {"edge_id": "IDP29JMR_E067", "edge_description": "noisy nonlinear systems, measurement noise, external disturbances induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E068", "edge_description": "noisy nonlinear systems, measurement noise, external disturbances induces_problem closed-loop control masks the fault effect"},
    {"edge_id": "IDP29JMR_E069", "edge_description": "real-time implementation, dSpace 1104 board, DSP induces_problem parametric variation due to the motor heating or other perturbation"},
    {"edge_id": "IDP29JMR_E070", "edge_description": "real-time implementation, dSpace 1104 board, DSP induces_problem closed-loop control masks the fault effect"}
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
| 1 | `IDP29JMR_E041` | `is collected on` | 11-Sensor Information | Hall type current sensors |  | 04-Fault Location | rotor bar |  |
| 2 | `IDP29JMR_E042` | `is collected on` | 11-Sensor Information | voltage sensors |  | 04-Fault Location | rotor bar |  |
| 3 | `IDP29JMR_E043` | `is collected on` | 11-Sensor Information | Incremental encoder |  | 04-Fault Location | rotor bar |  |
| 4 | `IDP29JMR_E044` | `can obviously reflect` | 11-Sensor Information | Hall type current sensors |  | 05-Fault Mode | broken rotor bar |  |
| 5 | `IDP29JMR_E045` | `can obviously reflect` | 11-Sensor Information | voltage sensors |  | 05-Fault Mode | broken rotor bar |  |
| 6 | `IDP29JMR_E046` | `can obviously reflect` | 11-Sensor Information | Incremental encoder |  | 05-Fault Mode | broken rotor bar |  |
| 7 | `IDP29JMR_E047` | `can be used for` | 10-Dataset | Simulation data |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 8 | `IDP29JMR_E048` | `can be used for` | 10-Dataset | Experimental data |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 9 | `IDP29JMR_E055` | `induces_problem` | 02-Object Type | Induction motor |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 10 | `IDP29JMR_E056` | `induces_problem` | 02-Object Type | Induction motor |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |
| 11 | `IDP29JMR_E057` | `induces_problem` | 03-Operating Conditions | variable speed operating, rated load, reverse speed, low speed regions(Multiple Conditions) |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 12 | `IDP29JMR_E058` | `induces_problem` | 03-Operating Conditions | variable speed operating, rated load, reverse speed, low speed regions(Multiple Conditions) |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |
| 13 | `IDP29JMR_E059` | `induces_problem` | 06-Fault Severity | adjacent two broken rotor bars, 3.1mm diameter hole(Single Severity) |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 14 | `IDP29JMR_E060` | `induces_problem` | 06-Fault Severity | adjacent two broken rotor bars, 3.1mm diameter hole(Single Severity) |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |
| 15 | `IDP29JMR_E061` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 16 | `IDP29JMR_E062` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |
| 17 | `IDP29JMR_E063` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 18 | `IDP29JMR_E064` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |
| 19 | `IDP29JMR_E065` | `induces_problem` | 12-Training Data Availability | Not explicitly mentioned(Sufficient) |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 20 | `IDP29JMR_E066` | `induces_problem` | 12-Training Data Availability | Not explicitly mentioned(Sufficient) |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |
| 21 | `IDP29JMR_E067` | `induces_problem` | 13-Noise Level | noisy nonlinear systems, measurement noise, external disturbances(High Noise) |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 22 | `IDP29JMR_E068` | `induces_problem` | 13-Noise Level | noisy nonlinear systems, measurement noise, external disturbances(High Noise) |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |
| 23 | `IDP29JMR_E069` | `induces_problem` | 14-Computational Resource | real-time implementation, dSpace 1104 board, DSP(Low Resource Consumption) |  | 09-Problem Scenario | parametric variation due to the motor heating or other perturbation(Uncertainty) |  |
| 24 | `IDP29JMR_E070` | `induces_problem` | 14-Computational Resource | real-time implementation, dSpace 1104 board, DSP(Low Resource Consumption) |  | 09-Problem Scenario | closed-loop control masks the fault effect(Other) |  |

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

### ▶ For `can obviously reflect` (Sensor Information type → Fault Mode type)

**Very High Standard**: All of the following **conditions must be met** to be judged as "existing":
1. The paper explicitly states that the sensor **collects** data of this fault mode (i.e., the sensor appears in the fault data acquisition scenario)
2. The paper explicitly states that the sensor can **directly reflect/characterize** the physical features of this fault
3. The mere appearance of the sensor and fault mode in the dataset description is **insufficient** for judgment — the sensor must play an active role in the research method
**Trap to Watch Out For**: The mere appearance of the sensor and fault mode as dataset description does not equal the existence of a causal chain
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses a sensor→fault-feature causal relation, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 24 edges)*
