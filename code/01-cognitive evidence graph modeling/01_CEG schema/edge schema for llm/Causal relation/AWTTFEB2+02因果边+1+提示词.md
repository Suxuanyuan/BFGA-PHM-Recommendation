# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AWTTFEB2
- **Paper Title**：A comparative study of sensor fault diagnosis methods based on observer for ECAS system
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AWTTFEB2`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AWTTFEB2_E023", "edge_description": "Electronically controlled air suspension (ECAS) system contains height sensor"},
    {"edge_id": "AWTTFEB2_E024", "edge_description": "Electronically controlled air suspension (ECAS) system contains gas pressure sensor"},
    {"edge_id": "AWTTFEB2_E025", "edge_description": "Electronically controlled air suspension (ECAS) system contains acceleration sensor"},
    {"edge_id": "AWTTFEB2_E027", "edge_description": "failure fault contains No Compound Fault"},
    {"edge_id": "AWTTFEB2_E028", "edge_description": "constant gain fault contains No Compound Fault"},
    {"edge_id": "AWTTFEB2_E029", "edge_description": "constant bias fault contains No Compound Fault"},
    {"edge_id": "AWTTFEB2_E030", "edge_description": "acceleration sensor / accelerometer is collected on height sensor"},
    {"edge_id": "AWTTFEB2_E031", "edge_description": "acceleration sensor / accelerometer is collected on gas pressure sensor"},
    {"edge_id": "AWTTFEB2_E032", "edge_description": "acceleration sensor / accelerometer is collected on acceleration sensor"},
    {"edge_id": "AWTTFEB2_E033", "edge_description": "gas pressure sensor is collected on height sensor"},
    {"edge_id": "AWTTFEB2_E034", "edge_description": "gas pressure sensor is collected on gas pressure sensor"},
    {"edge_id": "AWTTFEB2_E035", "edge_description": "gas pressure sensor is collected on acceleration sensor"},
    {"edge_id": "AWTTFEB2_E036", "edge_description": "height sensor is collected on height sensor"},
    {"edge_id": "AWTTFEB2_E037", "edge_description": "height sensor is collected on gas pressure sensor"},
    {"edge_id": "AWTTFEB2_E038", "edge_description": "height sensor is collected on acceleration sensor"},
    {"edge_id": "AWTTFEB2_E039", "edge_description": "acceleration sensor / accelerometer can obviously reflect failure fault"},
    {"edge_id": "AWTTFEB2_E040", "edge_description": "acceleration sensor / accelerometer can obviously reflect constant gain fault"},
    {"edge_id": "AWTTFEB2_E041", "edge_description": "acceleration sensor / accelerometer can obviously reflect constant bias fault"},
    {"edge_id": "AWTTFEB2_E042", "edge_description": "gas pressure sensor can obviously reflect failure fault"},
    {"edge_id": "AWTTFEB2_E043", "edge_description": "gas pressure sensor can obviously reflect constant gain fault"},
    {"edge_id": "AWTTFEB2_E044", "edge_description": "gas pressure sensor can obviously reflect constant bias fault"},
    {"edge_id": "AWTTFEB2_E045", "edge_description": "height sensor can obviously reflect failure fault"},
    {"edge_id": "AWTTFEB2_E046", "edge_description": "height sensor can obviously reflect constant gain fault"},
    {"edge_id": "AWTTFEB2_E047", "edge_description": "height sensor can obviously reflect constant bias fault"},
    {"edge_id": "AWTTFEB2_E048", "edge_description": "Simulation data of 1/4 vehicle model can be used for Sensor fault detection and isolation (FDI)"},
    {"edge_id": "AWTTFEB2_E049", "edge_description": "Experimental data from test bench can be used for Sensor fault detection and isolation (FDI)"},
    {"edge_id": "AWTTFEB2_E050", "edge_description": "height sensor has_fault_mode failure fault"},
    {"edge_id": "AWTTFEB2_E051", "edge_description": "height sensor has_fault_mode constant gain fault"},
    {"edge_id": "AWTTFEB2_E052", "edge_description": "height sensor has_fault_mode constant bias fault"},
    {"edge_id": "AWTTFEB2_E053", "edge_description": "gas pressure sensor has_fault_mode failure fault"}
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
| 1 | `AWTTFEB2_E023` | `contains` | 02-Object Type | Electronically controlled air suspension (ECAS) system |  | 04-Fault Location | height sensor |  |
| 2 | `AWTTFEB2_E024` | `contains` | 02-Object Type | Electronically controlled air suspension (ECAS) system |  | 04-Fault Location | gas pressure sensor |  |
| 3 | `AWTTFEB2_E025` | `contains` | 02-Object Type | Electronically controlled air suspension (ECAS) system |  | 04-Fault Location | acceleration sensor |  |
| 4 | `AWTTFEB2_E027` | `contains` | 05-Fault Mode | failure fault |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `AWTTFEB2_E028` | `contains` | 05-Fault Mode | constant gain fault |  | 07-Compound Fault | No Compound Fault |  |
| 6 | `AWTTFEB2_E029` | `contains` | 05-Fault Mode | constant bias fault |  | 07-Compound Fault | No Compound Fault |  |
| 7 | `AWTTFEB2_E030` | `is collected on` | 11-Sensor Information | acceleration sensor / accelerometer |  | 04-Fault Location | height sensor |  |
| 8 | `AWTTFEB2_E031` | `is collected on` | 11-Sensor Information | acceleration sensor / accelerometer |  | 04-Fault Location | gas pressure sensor |  |
| 9 | `AWTTFEB2_E032` | `is collected on` | 11-Sensor Information | acceleration sensor / accelerometer |  | 04-Fault Location | acceleration sensor |  |
| 10 | `AWTTFEB2_E033` | `is collected on` | 11-Sensor Information | gas pressure sensor |  | 04-Fault Location | height sensor |  |
| 11 | `AWTTFEB2_E034` | `is collected on` | 11-Sensor Information | gas pressure sensor |  | 04-Fault Location | gas pressure sensor |  |
| 12 | `AWTTFEB2_E035` | `is collected on` | 11-Sensor Information | gas pressure sensor |  | 04-Fault Location | acceleration sensor |  |
| 13 | `AWTTFEB2_E036` | `is collected on` | 11-Sensor Information | height sensor |  | 04-Fault Location | height sensor |  |
| 14 | `AWTTFEB2_E037` | `is collected on` | 11-Sensor Information | height sensor |  | 04-Fault Location | gas pressure sensor |  |
| 15 | `AWTTFEB2_E038` | `is collected on` | 11-Sensor Information | height sensor |  | 04-Fault Location | acceleration sensor |  |
| 16 | `AWTTFEB2_E039` | `can obviously reflect` | 11-Sensor Information | acceleration sensor / accelerometer |  | 05-Fault Mode | failure fault |  |
| 17 | `AWTTFEB2_E040` | `can obviously reflect` | 11-Sensor Information | acceleration sensor / accelerometer |  | 05-Fault Mode | constant gain fault |  |
| 18 | `AWTTFEB2_E041` | `can obviously reflect` | 11-Sensor Information | acceleration sensor / accelerometer |  | 05-Fault Mode | constant bias fault |  |
| 19 | `AWTTFEB2_E042` | `can obviously reflect` | 11-Sensor Information | gas pressure sensor |  | 05-Fault Mode | failure fault |  |
| 20 | `AWTTFEB2_E043` | `can obviously reflect` | 11-Sensor Information | gas pressure sensor |  | 05-Fault Mode | constant gain fault |  |
| 21 | `AWTTFEB2_E044` | `can obviously reflect` | 11-Sensor Information | gas pressure sensor |  | 05-Fault Mode | constant bias fault |  |
| 22 | `AWTTFEB2_E045` | `can obviously reflect` | 11-Sensor Information | height sensor |  | 05-Fault Mode | failure fault |  |
| 23 | `AWTTFEB2_E046` | `can obviously reflect` | 11-Sensor Information | height sensor |  | 05-Fault Mode | constant gain fault |  |
| 24 | `AWTTFEB2_E047` | `can obviously reflect` | 11-Sensor Information | height sensor |  | 05-Fault Mode | constant bias fault |  |
| 25 | `AWTTFEB2_E048` | `can be used for` | 10-Dataset | Simulation data of 1/4 vehicle model |  | 08-PHM Task | Sensor fault detection and isolation (FDI)(Diagnosis Task) |  |
| 26 | `AWTTFEB2_E049` | `can be used for` | 10-Dataset | Experimental data from test bench |  | 08-PHM Task | Sensor fault detection and isolation (FDI)(Diagnosis Task) |  |
| 27 | `AWTTFEB2_E050` | `has_fault_mode` | 04-Fault Location | height sensor |  | 05-Fault Mode | failure fault |  |
| 28 | `AWTTFEB2_E051` | `has_fault_mode` | 04-Fault Location | height sensor |  | 05-Fault Mode | constant gain fault |  |
| 29 | `AWTTFEB2_E052` | `has_fault_mode` | 04-Fault Location | height sensor |  | 05-Fault Mode | constant bias fault |  |
| 30 | `AWTTFEB2_E053` | `has_fault_mode` | 04-Fault Location | gas pressure sensor |  | 05-Fault Mode | failure fault |  |

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
