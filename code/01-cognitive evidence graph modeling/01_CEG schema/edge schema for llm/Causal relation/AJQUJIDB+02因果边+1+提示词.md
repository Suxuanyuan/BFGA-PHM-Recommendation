# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AJQUJIDB
- **Paper Title**：Cross-correlation of whitened vibration signals for low-speed bearing diagnostics
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AJQUJIDB`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AJQUJIDB_E058", "edge_description": "crack contains No Compound Fault"},
    {"edge_id": "AJQUJIDB_E059", "edge_description": "wear contains No Compound Fault"},
    {"edge_id": "AJQUJIDB_E060", "edge_description": "vibration accelerometer is collected on rolling element bearing"},
    {"edge_id": "AJQUJIDB_E061", "edge_description": "quadrature incremental encoder is collected on rolling element bearing"},
    {"edge_id": "AJQUJIDB_E062", "edge_description": "vibration accelerometer can obviously reflect crack"},
    {"edge_id": "AJQUJIDB_E063", "edge_description": "vibration accelerometer can obviously reflect wear"},
    {"edge_id": "AJQUJIDB_E064", "edge_description": "quadrature incremental encoder can obviously reflect crack"},
    {"edge_id": "AJQUJIDB_E065", "edge_description": "quadrature incremental encoder can obviously reflect wear"},
    {"edge_id": "AJQUJIDB_E066", "edge_description": "Case Western Reserve University bearing fault database can be used for Bearing fault diagnostics"},
    {"edge_id": "AJQUJIDB_E067", "edge_description": "accelerated bearing life-time test rig can be used for Bearing fault diagnostics"},
    {"edge_id": "AJQUJIDB_E068", "edge_description": "rolling element bearing has_fault_mode crack"},
    {"edge_id": "AJQUJIDB_E069", "edge_description": "rolling element bearing has_fault_mode wear"},
    {"edge_id": "AJQUJIDB_E070", "edge_description": "crack contains million revolutions"},
    {"edge_id": "AJQUJIDB_E071", "edge_description": "wear contains million revolutions"},
    {"edge_id": "AJQUJIDB_E074", "edge_description": "crack contains_phm_task Bearing fault diagnostics"},
    {"edge_id": "AJQUJIDB_E075", "edge_description": "wear contains_phm_task Bearing fault diagnostics"},
    {"edge_id": "AJQUJIDB_E077", "edge_description": "Rolling element bearing induces_problem Low signal-to-noise ratio (SNR) under low-speed conditions"},
    {"edge_id": "AJQUJIDB_E078", "edge_description": "Rolling element bearing induces_problem Early fault detection / incipient fault diagnostics"},
    {"edge_id": "AJQUJIDB_E079", "edge_description": "Multiple rotational speeds (20 rpm, 50 rpm, 100 rpm, 250 rpm, 500 rpm) under constant load induces_problem Low signal-to-noise ratio (SNR) under low-speed conditions"},
    {"edge_id": "AJQUJIDB_E080", "edge_description": "Multiple rotational speeds (20 rpm, 50 rpm, 100 rpm, 250 rpm, 500 rpm) under constant load induces_problem Early fault detection / incipient fault diagnostics"},
    {"edge_id": "AJQUJIDB_E081", "edge_description": "million revolutions induces_problem Low signal-to-noise ratio (SNR) under low-speed conditions"},
    {"edge_id": "AJQUJIDB_E082", "edge_description": "million revolutions induces_problem Early fault detection / incipient fault diagnostics"},
    {"edge_id": "AJQUJIDB_E083", "edge_description": "No Compound Fault induces_problem Low signal-to-noise ratio (SNR) under low-speed conditions"},
    {"edge_id": "AJQUJIDB_E084", "edge_description": "No Compound Fault induces_problem Early fault detection / incipient fault diagnostics"},
    {"edge_id": "AJQUJIDB_E085", "edge_description": "Bearing fault diagnostics induces_problem Low signal-to-noise ratio (SNR) under low-speed conditions"},
    {"edge_id": "AJQUJIDB_E086", "edge_description": "Bearing fault diagnostics induces_problem Early fault detection / incipient fault diagnostics"},
    {"edge_id": "AJQUJIDB_E087", "edge_description": "Sufficient induces_problem Low signal-to-noise ratio (SNR) under low-speed conditions"},
    {"edge_id": "AJQUJIDB_E088", "edge_description": "Sufficient induces_problem Early fault detection / incipient fault diagnostics"},
    {"edge_id": "AJQUJIDB_E089", "edge_description": "Background noise induces_problem Low signal-to-noise ratio (SNR) under low-speed conditions"},
    {"edge_id": "AJQUJIDB_E090", "edge_description": "Background noise induces_problem Early fault detection / incipient fault diagnostics"}
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
| 1 | `AJQUJIDB_E058` | `contains` | 05-Fault Mode | crack |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `AJQUJIDB_E059` | `contains` | 05-Fault Mode | wear |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `AJQUJIDB_E060` | `is collected on` | 11-Sensor Information | vibration accelerometer |  | 04-Fault Location | rolling element bearing |  |
| 4 | `AJQUJIDB_E061` | `is collected on` | 11-Sensor Information | quadrature incremental encoder |  | 04-Fault Location | rolling element bearing |  |
| 5 | `AJQUJIDB_E062` | `can obviously reflect` | 11-Sensor Information | vibration accelerometer |  | 05-Fault Mode | crack |  |
| 6 | `AJQUJIDB_E063` | `can obviously reflect` | 11-Sensor Information | vibration accelerometer |  | 05-Fault Mode | wear |  |
| 7 | `AJQUJIDB_E064` | `can obviously reflect` | 11-Sensor Information | quadrature incremental encoder |  | 05-Fault Mode | crack |  |
| 8 | `AJQUJIDB_E065` | `can obviously reflect` | 11-Sensor Information | quadrature incremental encoder |  | 05-Fault Mode | wear |  |
| 9 | `AJQUJIDB_E066` | `can be used for` | 10-Dataset | Case Western Reserve University bearing fault database |  | 08-PHM Task | Bearing fault diagnostics(Diagnosis Task) |  |
| 10 | `AJQUJIDB_E067` | `can be used for` | 10-Dataset | accelerated bearing life-time test rig |  | 08-PHM Task | Bearing fault diagnostics(Diagnosis Task) |  |
| 11 | `AJQUJIDB_E068` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | crack |  |
| 12 | `AJQUJIDB_E069` | `has_fault_mode` | 04-Fault Location | rolling element bearing |  | 05-Fault Mode | wear |  |
| 13 | `AJQUJIDB_E070` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | million revolutions(Multiple Severities) |  |
| 14 | `AJQUJIDB_E071` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | million revolutions(Multiple Severities) |  |
| 15 | `AJQUJIDB_E074` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | Bearing fault diagnostics(Diagnosis Task) |  |
| 16 | `AJQUJIDB_E075` | `contains_phm_task` | 05-Fault Mode | wear |  | 08-PHM Task | Bearing fault diagnostics(Diagnosis Task) |  |
| 17 | `AJQUJIDB_E077` | `induces_problem` | 02-Object Type | Rolling element bearing |  | 09-Problem Scenario | Low signal-to-noise ratio (SNR) under low-speed conditions(Uncertainty) |  |
| 18 | `AJQUJIDB_E078` | `induces_problem` | 02-Object Type | Rolling element bearing |  | 09-Problem Scenario | Early fault detection / incipient fault diagnostics(Early Degradation Prediction) |  |
| 19 | `AJQUJIDB_E079` | `induces_problem` | 03-Operating Conditions | Multiple rotational speeds (20 rpm, 50 rpm, 100 rpm, 250 rpm, 500 rpm) under constant load(Multiple Conditions) |  | 09-Problem Scenario | Low signal-to-noise ratio (SNR) under low-speed conditions(Uncertainty) |  |
| 20 | `AJQUJIDB_E080` | `induces_problem` | 03-Operating Conditions | Multiple rotational speeds (20 rpm, 50 rpm, 100 rpm, 250 rpm, 500 rpm) under constant load(Multiple Conditions) |  | 09-Problem Scenario | Early fault detection / incipient fault diagnostics(Early Degradation Prediction) |  |
| 21 | `AJQUJIDB_E081` | `induces_problem` | 06-Fault Severity | million revolutions(Multiple Severities) |  | 09-Problem Scenario | Low signal-to-noise ratio (SNR) under low-speed conditions(Uncertainty) |  |
| 22 | `AJQUJIDB_E082` | `induces_problem` | 06-Fault Severity | million revolutions(Multiple Severities) |  | 09-Problem Scenario | Early fault detection / incipient fault diagnostics(Early Degradation Prediction) |  |
| 23 | `AJQUJIDB_E083` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Low signal-to-noise ratio (SNR) under low-speed conditions(Uncertainty) |  |
| 24 | `AJQUJIDB_E084` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Early fault detection / incipient fault diagnostics(Early Degradation Prediction) |  |
| 25 | `AJQUJIDB_E085` | `induces_problem` | 08-PHM Task | Bearing fault diagnostics(Diagnosis Task) |  | 09-Problem Scenario | Low signal-to-noise ratio (SNR) under low-speed conditions(Uncertainty) |  |
| 26 | `AJQUJIDB_E086` | `induces_problem` | 08-PHM Task | Bearing fault diagnostics(Diagnosis Task) |  | 09-Problem Scenario | Early fault detection / incipient fault diagnostics(Early Degradation Prediction) |  |
| 27 | `AJQUJIDB_E087` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | Low signal-to-noise ratio (SNR) under low-speed conditions(Uncertainty) |  |
| 28 | `AJQUJIDB_E088` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | Early fault detection / incipient fault diagnostics(Early Degradation Prediction) |  |
| 29 | `AJQUJIDB_E089` | `induces_problem` | 13-Noise Level | Background noise(High Noise) |  | 09-Problem Scenario | Low signal-to-noise ratio (SNR) under low-speed conditions(Uncertainty) |  |
| 30 | `AJQUJIDB_E090` | `induces_problem` | 13-Noise Level | Background noise(High Noise) |  | 09-Problem Scenario | Early fault detection / incipient fault diagnostics(Early Degradation Prediction) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
