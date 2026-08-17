# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：SKWZZBDC
- **Paper Title**：Analytic Model for Induction Motors Under Localized Bearing Faults
- **Number of Candidate Edges to Judge**：22 

---

## II. LLM Input

> **Input Material**: Reference ID `SKWZZBDC`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "SKWZZBDC_E052", "edge_description": "induction motors contains induction motor"},
    {"edge_id": "SKWZZBDC_E053", "edge_description": "induction motors contains roller bearing"},
    {"edge_id": "SKWZZBDC_E054", "edge_description": "induction motor contains ball bearing"},
    {"edge_id": "SKWZZBDC_E055", "edge_description": "roller bearing contains ball bearing"},
    {"edge_id": "SKWZZBDC_E056", "edge_description": "induction motor contains nominal frequency 50 Hz, nominal voltage 380 V"},
    {"edge_id": "SKWZZBDC_E057", "edge_description": "roller bearing contains nominal frequency 50 Hz, nominal voltage 380 V"},
    {"edge_id": "SKWZZBDC_E059", "edge_description": "current sensors of type LTS6-NP is collected on ball bearing"},
    {"edge_id": "SKWZZBDC_E060", "edge_description": "voltage sensors of type LV25-P is collected on ball bearing"},
    {"edge_id": "SKWZZBDC_E061", "edge_description": "current sensors of type LTS6-NP can obviously reflect localized defects"},
    {"edge_id": "SKWZZBDC_E062", "edge_description": "voltage sensors of type LV25-P can obviously reflect localized defects"},
    {"edge_id": "SKWZZBDC_E063", "edge_description": "Simulation data based on multiple coupled circuit method (MCCM) can be used for fault diagnosis"},
    {"edge_id": "SKWZZBDC_E064", "edge_description": "Experimental data of a 1.1 kW squirrel cage induction motor can be used for fault diagnosis"},
    {"edge_id": "SKWZZBDC_E067", "edge_description": "induction motor contains_phm_task fault diagnosis"},
    {"edge_id": "SKWZZBDC_E068", "edge_description": "roller bearing contains_phm_task fault diagnosis"},
    {"edge_id": "SKWZZBDC_E072", "edge_description": "induction motor induces_problem analytic model / physical modeling"},
    {"edge_id": "SKWZZBDC_E073", "edge_description": "roller bearing induces_problem analytic model / physical modeling"},
    {"edge_id": "SKWZZBDC_E074", "edge_description": "nominal frequency 50 Hz, nominal voltage 380 V induces_problem analytic model / physical modeling"},
    {"edge_id": "SKWZZBDC_E075", "edge_description": "hole of 2 mm and 5 mm diameter induces_problem analytic model / physical modeling"},
    {"edge_id": "SKWZZBDC_E076", "edge_description": "No Compound Fault induces_problem analytic model / physical modeling"},
    {"edge_id": "SKWZZBDC_E077", "edge_description": "fault diagnosis induces_problem analytic model / physical modeling"},
    {"edge_id": "SKWZZBDC_E078", "edge_description": "Sufficient induces_problem analytic model / physical modeling"},
    {"edge_id": "SKWZZBDC_E079", "edge_description": "noise level induces_problem analytic model / physical modeling"}
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
| 1 | `SKWZZBDC_E052` | `contains` | 01-Object Domain | induction motors(Electronics) |  | 02-Object Type | induction motor |  |
| 2 | `SKWZZBDC_E053` | `contains` | 01-Object Domain | induction motors(Electronics) |  | 02-Object Type | roller bearing |  |
| 3 | `SKWZZBDC_E054` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | ball bearing |  |
| 4 | `SKWZZBDC_E055` | `contains` | 02-Object Type | roller bearing |  | 04-Fault Location | ball bearing |  |
| 5 | `SKWZZBDC_E056` | `contains` | 02-Object Type | induction motor |  | 03-Operating Conditions | nominal frequency 50 Hz, nominal voltage 380 V(Single Condition) |  |
| 6 | `SKWZZBDC_E057` | `contains` | 02-Object Type | roller bearing |  | 03-Operating Conditions | nominal frequency 50 Hz, nominal voltage 380 V(Single Condition) |  |
| 7 | `SKWZZBDC_E059` | `is collected on` | 11-Sensor Information | current sensors of type LTS6-NP |  | 04-Fault Location | ball bearing |  |
| 8 | `SKWZZBDC_E060` | `is collected on` | 11-Sensor Information | voltage sensors of type LV25-P |  | 04-Fault Location | ball bearing |  |
| 9 | `SKWZZBDC_E061` | `can obviously reflect` | 11-Sensor Information | current sensors of type LTS6-NP |  | 05-Fault Mode | localized defects |  |
| 10 | `SKWZZBDC_E062` | `can obviously reflect` | 11-Sensor Information | voltage sensors of type LV25-P |  | 05-Fault Mode | localized defects |  |
| 11 | `SKWZZBDC_E063` | `can be used for` | 10-Dataset | Simulation data based on multiple coupled circuit method (MCCM) |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `SKWZZBDC_E064` | `can be used for` | 10-Dataset | Experimental data of a 1.1 kW squirrel cage induction motor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `SKWZZBDC_E067` | `contains_phm_task` | 02-Object Type | induction motor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `SKWZZBDC_E068` | `contains_phm_task` | 02-Object Type | roller bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `SKWZZBDC_E072` | `induces_problem` | 02-Object Type | induction motor |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |
| 16 | `SKWZZBDC_E073` | `induces_problem` | 02-Object Type | roller bearing |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |
| 17 | `SKWZZBDC_E074` | `induces_problem` | 03-Operating Conditions | nominal frequency 50 Hz, nominal voltage 380 V(Single Condition) |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |
| 18 | `SKWZZBDC_E075` | `induces_problem` | 06-Fault Severity | hole of 2 mm and 5 mm diameter(Multiple Severities) |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |
| 19 | `SKWZZBDC_E076` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |
| 20 | `SKWZZBDC_E077` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |
| 21 | `SKWZZBDC_E078` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |
| 22 | `SKWZZBDC_E079` | `induces_problem` | 13-Noise Level | noise level(High Noise) |  | 09-Problem Scenario | analytic model / physical modeling(Trustworthiness / Interpretability) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 22 edges)*
