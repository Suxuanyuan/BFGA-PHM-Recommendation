# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：9L2GTHEW
- **Paper Title**：Fault Isolability Analysis and Optimal Sensor Placement for Fault Diagnosis in Smart Buildings
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `9L2GTHEW`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "9L2GTHEW_E021", "edge_description": "smart buildings contains ventilation damper"},
    {"edge_id": "9L2GTHEW_E022", "edge_description": "smart buildings contains radiator valve"},
    {"edge_id": "9L2GTHEW_E023", "edge_description": "ventilation damper contains temperature sensor"},
    {"edge_id": "9L2GTHEW_E024", "edge_description": "ventilation damper contains radiator valve"},
    {"edge_id": "9L2GTHEW_E025", "edge_description": "ventilation damper contains ventilation damper"},
    {"edge_id": "9L2GTHEW_E026", "edge_description": "radiator valve contains temperature sensor"},
    {"edge_id": "9L2GTHEW_E027", "edge_description": "radiator valve contains radiator valve"},
    {"edge_id": "9L2GTHEW_E028", "edge_description": "radiator valve contains ventilation damper"},
    {"edge_id": "9L2GTHEW_E029", "edge_description": "ventilation damper contains dynamic and time-varying conditions"},
    {"edge_id": "9L2GTHEW_E030", "edge_description": "radiator valve contains dynamic and time-varying conditions"},
    {"edge_id": "9L2GTHEW_E031", "edge_description": "sensor fault contains No Compound Fault"},
    {"edge_id": "9L2GTHEW_E032", "edge_description": "percentage fault contains No Compound Fault"},
    {"edge_id": "9L2GTHEW_E033", "edge_description": "temperature sensor is collected on temperature sensor"},
    {"edge_id": "9L2GTHEW_E034", "edge_description": "temperature sensor is collected on radiator valve"},
    {"edge_id": "9L2GTHEW_E035", "edge_description": "temperature sensor is collected on ventilation damper"},
    {"edge_id": "9L2GTHEW_E036", "edge_description": "damper position sensor, heater valve position sensor is collected on temperature sensor"},
    {"edge_id": "9L2GTHEW_E037", "edge_description": "damper position sensor, heater valve position sensor is collected on radiator valve"},
    {"edge_id": "9L2GTHEW_E038", "edge_description": "damper position sensor, heater valve position sensor is collected on ventilation damper"},
    {"edge_id": "9L2GTHEW_E039", "edge_description": "temperature sensor can obviously reflect sensor fault"},
    {"edge_id": "9L2GTHEW_E040", "edge_description": "temperature sensor can obviously reflect percentage fault"},
    {"edge_id": "9L2GTHEW_E041", "edge_description": "damper position sensor, heater valve position sensor can obviously reflect sensor fault"},
    {"edge_id": "9L2GTHEW_E042", "edge_description": "damper position sensor, heater valve position sensor can obviously reflect percentage fault"},
    {"edge_id": "9L2GTHEW_E044", "edge_description": "temperature sensor has_fault_mode sensor fault"},
    {"edge_id": "9L2GTHEW_E045", "edge_description": "temperature sensor has_fault_mode percentage fault"},
    {"edge_id": "9L2GTHEW_E046", "edge_description": "radiator valve has_fault_mode sensor fault"},
    {"edge_id": "9L2GTHEW_E047", "edge_description": "radiator valve has_fault_mode percentage fault"},
    {"edge_id": "9L2GTHEW_E048", "edge_description": "ventilation damper has_fault_mode sensor fault"},
    {"edge_id": "9L2GTHEW_E049", "edge_description": "ventilation damper has_fault_mode percentage fault"},
    {"edge_id": "9L2GTHEW_E050", "edge_description": "sensor fault contains unknown size, unknown percentage error"},
    {"edge_id": "9L2GTHEW_E051", "edge_description": "percentage fault contains unknown size, unknown percentage error"}
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
| 1 | `9L2GTHEW_E021` | `contains` | 01-Object Domain | smart buildings(Other) |  | 02-Object Type | ventilation damper |  |
| 2 | `9L2GTHEW_E022` | `contains` | 01-Object Domain | smart buildings(Other) |  | 02-Object Type | radiator valve |  |
| 3 | `9L2GTHEW_E023` | `contains` | 02-Object Type | ventilation damper |  | 04-Fault Location | temperature sensor |  |
| 4 | `9L2GTHEW_E024` | `contains` | 02-Object Type | ventilation damper |  | 04-Fault Location | radiator valve |  |
| 5 | `9L2GTHEW_E025` | `contains` | 02-Object Type | ventilation damper |  | 04-Fault Location | ventilation damper |  |
| 6 | `9L2GTHEW_E026` | `contains` | 02-Object Type | radiator valve |  | 04-Fault Location | temperature sensor |  |
| 7 | `9L2GTHEW_E027` | `contains` | 02-Object Type | radiator valve |  | 04-Fault Location | radiator valve |  |
| 8 | `9L2GTHEW_E028` | `contains` | 02-Object Type | radiator valve |  | 04-Fault Location | ventilation damper |  |
| 9 | `9L2GTHEW_E029` | `contains` | 02-Object Type | ventilation damper |  | 03-Operating Conditions | dynamic and time-varying conditions(Variable Conditions) |  |
| 10 | `9L2GTHEW_E030` | `contains` | 02-Object Type | radiator valve |  | 03-Operating Conditions | dynamic and time-varying conditions(Variable Conditions) |  |
| 11 | `9L2GTHEW_E031` | `contains` | 05-Fault Mode | sensor fault |  | 07-Compound Fault | No Compound Fault |  |
| 12 | `9L2GTHEW_E032` | `contains` | 05-Fault Mode | percentage fault |  | 07-Compound Fault | No Compound Fault |  |
| 13 | `9L2GTHEW_E033` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | temperature sensor |  |
| 14 | `9L2GTHEW_E034` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | radiator valve |  |
| 15 | `9L2GTHEW_E035` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | ventilation damper |  |
| 16 | `9L2GTHEW_E036` | `is collected on` | 11-Sensor Information | damper position sensor, heater valve position sensor |  | 04-Fault Location | temperature sensor |  |
| 17 | `9L2GTHEW_E037` | `is collected on` | 11-Sensor Information | damper position sensor, heater valve position sensor |  | 04-Fault Location | radiator valve |  |
| 18 | `9L2GTHEW_E038` | `is collected on` | 11-Sensor Information | damper position sensor, heater valve position sensor |  | 04-Fault Location | ventilation damper |  |
| 19 | `9L2GTHEW_E039` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | sensor fault |  |
| 20 | `9L2GTHEW_E040` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | percentage fault |  |
| 21 | `9L2GTHEW_E041` | `can obviously reflect` | 11-Sensor Information | damper position sensor, heater valve position sensor |  | 05-Fault Mode | sensor fault |  |
| 22 | `9L2GTHEW_E042` | `can obviously reflect` | 11-Sensor Information | damper position sensor, heater valve position sensor |  | 05-Fault Mode | percentage fault |  |
| 23 | `9L2GTHEW_E044` | `has_fault_mode` | 04-Fault Location | temperature sensor |  | 05-Fault Mode | sensor fault |  |
| 24 | `9L2GTHEW_E045` | `has_fault_mode` | 04-Fault Location | temperature sensor |  | 05-Fault Mode | percentage fault |  |
| 25 | `9L2GTHEW_E046` | `has_fault_mode` | 04-Fault Location | radiator valve |  | 05-Fault Mode | sensor fault |  |
| 26 | `9L2GTHEW_E047` | `has_fault_mode` | 04-Fault Location | radiator valve |  | 05-Fault Mode | percentage fault |  |
| 27 | `9L2GTHEW_E048` | `has_fault_mode` | 04-Fault Location | ventilation damper |  | 05-Fault Mode | sensor fault |  |
| 28 | `9L2GTHEW_E049` | `has_fault_mode` | 04-Fault Location | ventilation damper |  | 05-Fault Mode | percentage fault |  |
| 29 | `9L2GTHEW_E050` | `contains` | 05-Fault Mode | sensor fault |  | 06-Fault Severity | unknown size, unknown percentage error(Single Severity) |  |
| 30 | `9L2GTHEW_E051` | `contains` | 05-Fault Mode | percentage fault |  | 06-Fault Severity | unknown size, unknown percentage error(Single Severity) |  |

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
