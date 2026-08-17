# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：F6VLUYBT
- **Paper Title**：Evaluation of the Influence of Rotor Magnetic Anisotropy on Condition Monitoring of Two-Pole Induction Motors
- **Number of Candidate Edges to Judge**：29 

---

## II. LLM Input

> **Input Material**: Reference ID `F6VLUYBT`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "F6PYPTP8_E055", "edge_description": "pitting contains No Compound Fault"},
    {"edge_id": "F6PYPTP8_E056", "edge_description": "wear contains No Compound Fault"},
    {"edge_id": "F6PYPTP8_E057", "edge_description": "crack / broken teeth contains No Compound Fault"},
    {"edge_id": "F6PYPTP8_E059", "edge_description": "accelerometer can obviously reflect pitting"},
    {"edge_id": "F6PYPTP8_E060", "edge_description": "accelerometer can obviously reflect wear"},
    {"edge_id": "F6PYPTP8_E061", "edge_description": "accelerometer can obviously reflect crack / broken teeth"},
    {"edge_id": "F6PYPTP8_E063", "edge_description": "gearbox has_fault_mode pitting"},
    {"edge_id": "F6PYPTP8_E064", "edge_description": "gearbox has_fault_mode wear"},
    {"edge_id": "F6PYPTP8_E065", "edge_description": "gearbox has_fault_mode crack / broken teeth"},
    {"edge_id": "F6PYPTP8_E066", "edge_description": "pitting contains six defect levels"},
    {"edge_id": "F6PYPTP8_E067", "edge_description": "wear contains six defect levels"},
    {"edge_id": "F6PYPTP8_E068", "edge_description": "crack / broken teeth contains six defect levels"},
    {"edge_id": "F6PYPTP8_E071", "edge_description": "pitting contains_phm_task Gearbox fault diagnosis"},
    {"edge_id": "F6PYPTP8_E072", "edge_description": "wear contains_phm_task Gearbox fault diagnosis"},
    {"edge_id": "F6PYPTP8_E073", "edge_description": "crack / broken teeth contains_phm_task Gearbox fault diagnosis"},
    {"edge_id": "F6PYPTP8_E075", "edge_description": "Planetary gearbox induces_problem Extracting effective fault features from noised vibration signals"},
    {"edge_id": "F6PYPTP8_E076", "edge_description": "Planetary gearbox induces_problem Simultaneous optimization of DNN parameters and structure"},
    {"edge_id": "F6PYPTP8_E077", "edge_description": "Three different motor speeds (294, 588, and 882 r/min) under load-free conditions induces_problem Extracting effective fault features from noised vibration signals"},
    {"edge_id": "F6PYPTP8_E078", "edge_description": "Three different motor speeds (294, 588, and 882 r/min) under load-free conditions induces_problem Simultaneous optimization of DNN parameters and structure"},
    {"edge_id": "F6PYPTP8_E079", "edge_description": "six defect levels induces_problem Extracting effective fault features from noised vibration signals"},
    {"edge_id": "F6PYPTP8_E080", "edge_description": "six defect levels induces_problem Simultaneous optimization of DNN parameters and structure"},
    {"edge_id": "F6PYPTP8_E081", "edge_description": "No Compound Fault induces_problem Extracting effective fault features from noised vibration signals"},
    {"edge_id": "F6PYPTP8_E082", "edge_description": "No Compound Fault induces_problem Simultaneous optimization of DNN parameters and structure"},
    {"edge_id": "F6PYPTP8_E083", "edge_description": "Gearbox fault diagnosis induces_problem Extracting effective fault features from noised vibration signals"},
    {"edge_id": "F6PYPTP8_E084", "edge_description": "Gearbox fault diagnosis induces_problem Simultaneous optimization of DNN parameters and structure"},
    {"edge_id": "F6PYPTP8_E085", "edge_description": "Each condition contains 921 samples and there will be 921*9 samples in total. The random 60% of the dataset are used as the training samples induces_problem Extracting effective fault features from noised vibration signals"},
    {"edge_id": "F6PYPTP8_E086", "edge_description": "Each condition contains 921 samples and there will be 921*9 samples in total. The random 60% of the dataset are used as the training samples induces_problem Simultaneous optimization of DNN parameters and structure"},
    {"edge_id": "F6PYPTP8_E087", "edge_description": "extract effective fault features from noised vibration signals / This original feature set still consists of much noise induces_problem Extracting effective fault features from noised vibration signals"},
    {"edge_id": "F6PYPTP8_E088", "edge_description": "extract effective fault features from noised vibration signals / This original feature set still consists of much noise induces_problem Simultaneous optimization of DNN parameters and structure"}
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
| 1 | `F6PYPTP8_E055` | `contains` | 05-Fault Mode | pitting |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `F6PYPTP8_E056` | `contains` | 05-Fault Mode | wear |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `F6PYPTP8_E057` | `contains` | 05-Fault Mode | crack / broken teeth |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `F6PYPTP8_E059` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | pitting |  |
| 5 | `F6PYPTP8_E060` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | wear |  |
| 6 | `F6PYPTP8_E061` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | crack / broken teeth |  |
| 7 | `F6PYPTP8_E063` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | pitting |  |
| 8 | `F6PYPTP8_E064` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | wear |  |
| 9 | `F6PYPTP8_E065` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | crack / broken teeth |  |
| 10 | `F6PYPTP8_E066` | `contains` | 05-Fault Mode | pitting |  | 06-Fault Severity | six defect levels(Multiple Severities) |  |
| 11 | `F6PYPTP8_E067` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | six defect levels(Multiple Severities) |  |
| 12 | `F6PYPTP8_E068` | `contains` | 05-Fault Mode | crack / broken teeth |  | 06-Fault Severity | six defect levels(Multiple Severities) |  |
| 13 | `F6PYPTP8_E071` | `contains_phm_task` | 05-Fault Mode | pitting |  | 08-PHM Task | Gearbox fault diagnosis(Diagnosis Task) |  |
| 14 | `F6PYPTP8_E072` | `contains_phm_task` | 05-Fault Mode | wear |  | 08-PHM Task | Gearbox fault diagnosis(Diagnosis Task) |  |
| 15 | `F6PYPTP8_E073` | `contains_phm_task` | 05-Fault Mode | crack / broken teeth |  | 08-PHM Task | Gearbox fault diagnosis(Diagnosis Task) |  |
| 16 | `F6PYPTP8_E075` | `induces_problem` | 02-Object Type | Planetary gearbox |  | 09-Problem Scenario | Extracting effective fault features from noised vibration signals(Uncertainty) |  |
| 17 | `F6PYPTP8_E076` | `induces_problem` | 02-Object Type | Planetary gearbox |  | 09-Problem Scenario | Simultaneous optimization of DNN parameters and structure(Other) |  |
| 18 | `F6PYPTP8_E077` | `induces_problem` | 03-Operating Conditions | Three different motor speeds (294, 588, and 882 r/min) under load-free conditions(Multiple Conditions) |  | 09-Problem Scenario | Extracting effective fault features from noised vibration signals(Uncertainty) |  |
| 19 | `F6PYPTP8_E078` | `induces_problem` | 03-Operating Conditions | Three different motor speeds (294, 588, and 882 r/min) under load-free conditions(Multiple Conditions) |  | 09-Problem Scenario | Simultaneous optimization of DNN parameters and structure(Other) |  |
| 20 | `F6PYPTP8_E079` | `induces_problem` | 06-Fault Severity | six defect levels(Multiple Severities) |  | 09-Problem Scenario | Extracting effective fault features from noised vibration signals(Uncertainty) |  |
| 21 | `F6PYPTP8_E080` | `induces_problem` | 06-Fault Severity | six defect levels(Multiple Severities) |  | 09-Problem Scenario | Simultaneous optimization of DNN parameters and structure(Other) |  |
| 22 | `F6PYPTP8_E081` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Extracting effective fault features from noised vibration signals(Uncertainty) |  |
| 23 | `F6PYPTP8_E082` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Simultaneous optimization of DNN parameters and structure(Other) |  |
| 24 | `F6PYPTP8_E083` | `induces_problem` | 08-PHM Task | Gearbox fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | Extracting effective fault features from noised vibration signals(Uncertainty) |  |
| 25 | `F6PYPTP8_E084` | `induces_problem` | 08-PHM Task | Gearbox fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | Simultaneous optimization of DNN parameters and structure(Other) |  |
| 26 | `F6PYPTP8_E085` | `induces_problem` | 12-Training Data Availability | Each condition contains 921 samples and there will be 921*9 samples in total. The random 60% of the dataset are used as the training samples(Sufficient) |  | 09-Problem Scenario | Extracting effective fault features from noised vibration signals(Uncertainty) |  |
| 27 | `F6PYPTP8_E086` | `induces_problem` | 12-Training Data Availability | Each condition contains 921 samples and there will be 921*9 samples in total. The random 60% of the dataset are used as the training samples(Sufficient) |  | 09-Problem Scenario | Simultaneous optimization of DNN parameters and structure(Other) |  |
| 28 | `F6PYPTP8_E087` | `induces_problem` | 13-Noise Level | extract effective fault features from noised vibration signals / This original feature set still consists of much noise(High Noise) |  | 09-Problem Scenario | Extracting effective fault features from noised vibration signals(Uncertainty) |  |
| 29 | `F6PYPTP8_E088` | `induces_problem` | 13-Noise Level | extract effective fault features from noised vibration signals / This original feature set still consists of much noise(High Noise) |  | 09-Problem Scenario | Simultaneous optimization of DNN parameters and structure(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 29 edges)*
