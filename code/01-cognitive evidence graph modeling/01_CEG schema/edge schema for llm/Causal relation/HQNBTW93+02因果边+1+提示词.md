# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：HQNBTW93
- **Paper Title**：Health monitoring of cooling fan bearings based on wavelet filter
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `HQNBTW93`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "HQNBTW93_E072", "edge_description": "crack contains cracks and dents in the outraces, inner races and rolling elements"},
    {"edge_id": "HQNBTW93_E073", "edge_description": "dent contains cracks and dents in the outraces, inner races and rolling elements"},
    {"edge_id": "HQNBTW93_E074", "edge_description": "PCB 352A42 accelerometer is collected on bearing"},
    {"edge_id": "HQNBTW93_E075", "edge_description": "condenser microphone is collected on bearing"},
    {"edge_id": "HQNBTW93_E076", "edge_description": "PCB 352A42 accelerometer can obviously reflect crack"},
    {"edge_id": "HQNBTW93_E077", "edge_description": "PCB 352A42 accelerometer can obviously reflect dent"},
    {"edge_id": "HQNBTW93_E078", "edge_description": "condenser microphone can obviously reflect crack"},
    {"edge_id": "HQNBTW93_E079", "edge_description": "condenser microphone can obviously reflect dent"},
    {"edge_id": "HQNBTW93_E081", "edge_description": "bearing has_fault_mode crack"},
    {"edge_id": "HQNBTW93_E082", "edge_description": "bearing has_fault_mode dent"},
    {"edge_id": "HQNBTW93_E083", "edge_description": "crack contains degradation"},
    {"edge_id": "HQNBTW93_E084", "edge_description": "dent contains degradation"},
    {"edge_id": "HQNBTW93_E087", "edge_description": "crack contains_phm_task degradation assessment"},
    {"edge_id": "HQNBTW93_E088", "edge_description": "dent contains_phm_task degradation assessment"},
    {"edge_id": "HQNBTW93_E090", "edge_description": "cooling fan bearing induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E091", "edge_description": "cooling fan bearing induces_problem noise robustness / vibration signal tainted by noise"},
    {"edge_id": "HQNBTW93_E092", "edge_description": "free airflow conditions and rotating speed of 4000 rpm induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E093", "edge_description": "free airflow conditions and rotating speed of 4000 rpm induces_problem noise robustness / vibration signal tainted by noise"},
    {"edge_id": "HQNBTW93_E094", "edge_description": "degradation induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E095", "edge_description": "degradation induces_problem noise robustness / vibration signal tainted by noise"},
    {"edge_id": "HQNBTW93_E096", "edge_description": "cracks and dents in the outraces, inner races and rolling elements induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E097", "edge_description": "cracks and dents in the outraces, inner races and rolling elements induces_problem noise robustness / vibration signal tainted by noise"},
    {"edge_id": "HQNBTW93_E098", "edge_description": "degradation assessment induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E099", "edge_description": "degradation assessment induces_problem noise robustness / vibration signal tainted by noise"},
    {"edge_id": "HQNBTW93_E100", "edge_description": "Sufficient induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E101", "edge_description": "Sufficient induces_problem noise robustness / vibration signal tainted by noise"},
    {"edge_id": "HQNBTW93_E102", "edge_description": "noisy vibration data induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E103", "edge_description": "noisy vibration data induces_problem noise robustness / vibration signal tainted by noise"},
    {"edge_id": "HQNBTW93_E104", "edge_description": "computationally efficient induces_problem early detection of faults / incipient defects"},
    {"edge_id": "HQNBTW93_E105", "edge_description": "computationally efficient induces_problem noise robustness / vibration signal tainted by noise"}
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
| 1 | `HQNBTW93_E072` | `contains` | 05-Fault Mode | crack |  | 07-Compound Fault | cracks and dents in the outraces, inner races and rolling elements(Compound Fault Within Same Structure) |  |
| 2 | `HQNBTW93_E073` | `contains` | 05-Fault Mode | dent |  | 07-Compound Fault | cracks and dents in the outraces, inner races and rolling elements(Compound Fault Within Same Structure) |  |
| 3 | `HQNBTW93_E074` | `is collected on` | 11-Sensor Information | PCB 352A42 accelerometer |  | 04-Fault Location | bearing |  |
| 4 | `HQNBTW93_E075` | `is collected on` | 11-Sensor Information | condenser microphone |  | 04-Fault Location | bearing |  |
| 5 | `HQNBTW93_E076` | `can obviously reflect` | 11-Sensor Information | PCB 352A42 accelerometer |  | 05-Fault Mode | crack |  |
| 6 | `HQNBTW93_E077` | `can obviously reflect` | 11-Sensor Information | PCB 352A42 accelerometer |  | 05-Fault Mode | dent |  |
| 7 | `HQNBTW93_E078` | `can obviously reflect` | 11-Sensor Information | condenser microphone |  | 05-Fault Mode | crack |  |
| 8 | `HQNBTW93_E079` | `can obviously reflect` | 11-Sensor Information | condenser microphone |  | 05-Fault Mode | dent |  |
| 9 | `HQNBTW93_E081` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | crack |  |
| 10 | `HQNBTW93_E082` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | dent |  |
| 11 | `HQNBTW93_E083` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | degradation(Multiple Severities) |  |
| 12 | `HQNBTW93_E084` | `contains` | 05-Fault Mode | dent |  | 06-Fault Severity | degradation(Multiple Severities) |  |
| 13 | `HQNBTW93_E087` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | degradation assessment(Assessment Task) |  |
| 14 | `HQNBTW93_E088` | `contains_phm_task` | 05-Fault Mode | dent |  | 08-PHM Task | degradation assessment(Assessment Task) |  |
| 15 | `HQNBTW93_E090` | `induces_problem` | 02-Object Type | cooling fan bearing |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 16 | `HQNBTW93_E091` | `induces_problem` | 02-Object Type | cooling fan bearing |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |
| 17 | `HQNBTW93_E092` | `induces_problem` | 03-Operating Conditions | free airflow conditions and rotating speed of 4000 rpm(Single Condition) |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 18 | `HQNBTW93_E093` | `induces_problem` | 03-Operating Conditions | free airflow conditions and rotating speed of 4000 rpm(Single Condition) |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |
| 19 | `HQNBTW93_E094` | `induces_problem` | 06-Fault Severity | degradation(Multiple Severities) |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 20 | `HQNBTW93_E095` | `induces_problem` | 06-Fault Severity | degradation(Multiple Severities) |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |
| 21 | `HQNBTW93_E096` | `induces_problem` | 07-Compound Fault | cracks and dents in the outraces, inner races and rolling elements(Compound Fault Within Same Structure) |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 22 | `HQNBTW93_E097` | `induces_problem` | 07-Compound Fault | cracks and dents in the outraces, inner races and rolling elements(Compound Fault Within Same Structure) |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |
| 23 | `HQNBTW93_E098` | `induces_problem` | 08-PHM Task | degradation assessment(Assessment Task) |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 24 | `HQNBTW93_E099` | `induces_problem` | 08-PHM Task | degradation assessment(Assessment Task) |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |
| 25 | `HQNBTW93_E100` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 26 | `HQNBTW93_E101` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |
| 27 | `HQNBTW93_E102` | `induces_problem` | 13-Noise Level | noisy vibration data(High Noise) |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 28 | `HQNBTW93_E103` | `induces_problem` | 13-Noise Level | noisy vibration data(High Noise) |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |
| 29 | `HQNBTW93_E104` | `induces_problem` | 14-Computational Resource | computationally efficient(Low Resource Consumption) |  | 09-Problem Scenario | early detection of faults / incipient defects(Early Degradation Prediction) |  |
| 30 | `HQNBTW93_E105` | `induces_problem` | 14-Computational Resource | computationally efficient(Low Resource Consumption) |  | 09-Problem Scenario | noise robustness / vibration signal tainted by noise(Uncertainty) |  |

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
