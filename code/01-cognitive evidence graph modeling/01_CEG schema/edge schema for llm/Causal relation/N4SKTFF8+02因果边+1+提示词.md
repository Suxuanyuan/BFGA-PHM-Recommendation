# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：N4SKTFF8
- **Paper Title**：Incremental novelty detection and fault identification scheme applied to a kinematic chain under non-stationary operation
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `N4SKTFF8`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "N4R5BLFT_E020", "edge_description": "grid-connected photovoltaic systems contains photovoltaic module"},
    {"edge_id": "N4R5BLFT_E021", "edge_description": "grid-connected photovoltaic systems contains photovoltaic inverter"},
    {"edge_id": "N4R5BLFT_E022", "edge_description": "photovoltaic module contains PV module"},
    {"edge_id": "N4R5BLFT_E023", "edge_description": "photovoltaic inverter contains PV module"},
    {"edge_id": "N4R5BLFT_E024", "edge_description": "photovoltaic module contains natural outdoor environment (varying solar radiation and temperature)"},
    {"edge_id": "N4R5BLFT_E025", "edge_description": "photovoltaic inverter contains natural outdoor environment (varying solar radiation and temperature)"},
    {"edge_id": "N4R5BLFT_E027", "edge_description": "voltage sensors is collected on PV module"},
    {"edge_id": "N4R5BLFT_E028", "edge_description": "K-type Thermocouple is collected on PV module"},
    {"edge_id": "N4R5BLFT_E029", "edge_description": "reference solar cell is collected on PV module"},
    {"edge_id": "N4R5BLFT_E030", "edge_description": "current sensors is collected on PV module"},
    {"edge_id": "N4R5BLFT_E031", "edge_description": "voltage sensors can obviously reflect shading"},
    {"edge_id": "N4R5BLFT_E032", "edge_description": "K-type Thermocouple can obviously reflect shading"},
    {"edge_id": "N4R5BLFT_E033", "edge_description": "reference solar cell can obviously reflect shading"},
    {"edge_id": "N4R5BLFT_E034", "edge_description": "current sensors can obviously reflect shading"},
    {"edge_id": "N4R5BLFT_E038", "edge_description": "photovoltaic module contains_phm_task fault detection and diagnosis"},
    {"edge_id": "N4R5BLFT_E039", "edge_description": "photovoltaic inverter contains_phm_task fault detection and diagnosis"},
    {"edge_id": "N4R5BLFT_E043", "edge_description": "photovoltaic module induces_problem high cost of online monitoring and sensor placement optimization"},
    {"edge_id": "N4R5BLFT_E044", "edge_description": "photovoltaic module induces_problem multi-string multi-module fault diagnosis"},
    {"edge_id": "N4R5BLFT_E045", "edge_description": "photovoltaic inverter induces_problem high cost of online monitoring and sensor placement optimization"},
    {"edge_id": "N4R5BLFT_E046", "edge_description": "photovoltaic inverter induces_problem multi-string multi-module fault diagnosis"},
    {"edge_id": "N4R5BLFT_E047", "edge_description": "natural outdoor environment (varying solar radiation and temperature) induces_problem high cost of online monitoring and sensor placement optimization"},
    {"edge_id": "N4R5BLFT_E048", "edge_description": "natural outdoor environment (varying solar radiation and temperature) induces_problem multi-string multi-module fault diagnosis"},
    {"edge_id": "N4R5BLFT_E049", "edge_description": "fully shaded induces_problem high cost of online monitoring and sensor placement optimization"},
    {"edge_id": "N4R5BLFT_E050", "edge_description": "fully shaded induces_problem multi-string multi-module fault diagnosis"},
    {"edge_id": "N4R5BLFT_E051", "edge_description": "No Compound Fault induces_problem high cost of online monitoring and sensor placement optimization"},
    {"edge_id": "N4R5BLFT_E052", "edge_description": "No Compound Fault induces_problem multi-string multi-module fault diagnosis"},
    {"edge_id": "N4R5BLFT_E053", "edge_description": "fault detection and diagnosis induces_problem high cost of online monitoring and sensor placement optimization"},
    {"edge_id": "N4R5BLFT_E054", "edge_description": "fault detection and diagnosis induces_problem multi-string multi-module fault diagnosis"},
    {"edge_id": "N4R5BLFT_E055", "edge_description": "Sufficient induces_problem high cost of online monitoring and sensor placement optimization"},
    {"edge_id": "N4R5BLFT_E056", "edge_description": "Sufficient induces_problem multi-string multi-module fault diagnosis"}
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
| 1 | `N4R5BLFT_E020` | `contains` | 01-Object Domain | grid-connected photovoltaic systems(Industrial) |  | 02-Object Type | photovoltaic module |  |
| 2 | `N4R5BLFT_E021` | `contains` | 01-Object Domain | grid-connected photovoltaic systems(Industrial) |  | 02-Object Type | photovoltaic inverter |  |
| 3 | `N4R5BLFT_E022` | `contains` | 02-Object Type | photovoltaic module |  | 04-Fault Location | PV module |  |
| 4 | `N4R5BLFT_E023` | `contains` | 02-Object Type | photovoltaic inverter |  | 04-Fault Location | PV module |  |
| 5 | `N4R5BLFT_E024` | `contains` | 02-Object Type | photovoltaic module |  | 03-Operating Conditions | natural outdoor environment (varying solar radiation and temperature)(Variable Conditions) |  |
| 6 | `N4R5BLFT_E025` | `contains` | 02-Object Type | photovoltaic inverter |  | 03-Operating Conditions | natural outdoor environment (varying solar radiation and temperature)(Variable Conditions) |  |
| 7 | `N4R5BLFT_E027` | `is collected on` | 11-Sensor Information | voltage sensors |  | 04-Fault Location | PV module |  |
| 8 | `N4R5BLFT_E028` | `is collected on` | 11-Sensor Information | K-type Thermocouple |  | 04-Fault Location | PV module |  |
| 9 | `N4R5BLFT_E029` | `is collected on` | 11-Sensor Information | reference solar cell |  | 04-Fault Location | PV module |  |
| 10 | `N4R5BLFT_E030` | `is collected on` | 11-Sensor Information | current sensors |  | 04-Fault Location | PV module |  |
| 11 | `N4R5BLFT_E031` | `can obviously reflect` | 11-Sensor Information | voltage sensors |  | 05-Fault Mode | shading |  |
| 12 | `N4R5BLFT_E032` | `can obviously reflect` | 11-Sensor Information | K-type Thermocouple |  | 05-Fault Mode | shading |  |
| 13 | `N4R5BLFT_E033` | `can obviously reflect` | 11-Sensor Information | reference solar cell |  | 05-Fault Mode | shading |  |
| 14 | `N4R5BLFT_E034` | `can obviously reflect` | 11-Sensor Information | current sensors |  | 05-Fault Mode | shading |  |
| 15 | `N4R5BLFT_E038` | `contains_phm_task` | 02-Object Type | photovoltaic module |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 16 | `N4R5BLFT_E039` | `contains_phm_task` | 02-Object Type | photovoltaic inverter |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 17 | `N4R5BLFT_E043` | `induces_problem` | 02-Object Type | photovoltaic module |  | 09-Problem Scenario | high cost of online monitoring and sensor placement optimization(Other) |  |
| 18 | `N4R5BLFT_E044` | `induces_problem` | 02-Object Type | photovoltaic module |  | 09-Problem Scenario | multi-string multi-module fault diagnosis(Compound Faults) |  |
| 19 | `N4R5BLFT_E045` | `induces_problem` | 02-Object Type | photovoltaic inverter |  | 09-Problem Scenario | high cost of online monitoring and sensor placement optimization(Other) |  |
| 20 | `N4R5BLFT_E046` | `induces_problem` | 02-Object Type | photovoltaic inverter |  | 09-Problem Scenario | multi-string multi-module fault diagnosis(Compound Faults) |  |
| 21 | `N4R5BLFT_E047` | `induces_problem` | 03-Operating Conditions | natural outdoor environment (varying solar radiation and temperature)(Variable Conditions) |  | 09-Problem Scenario | high cost of online monitoring and sensor placement optimization(Other) |  |
| 22 | `N4R5BLFT_E048` | `induces_problem` | 03-Operating Conditions | natural outdoor environment (varying solar radiation and temperature)(Variable Conditions) |  | 09-Problem Scenario | multi-string multi-module fault diagnosis(Compound Faults) |  |
| 23 | `N4R5BLFT_E049` | `induces_problem` | 06-Fault Severity | fully shaded(Single Severity) |  | 09-Problem Scenario | high cost of online monitoring and sensor placement optimization(Other) |  |
| 24 | `N4R5BLFT_E050` | `induces_problem` | 06-Fault Severity | fully shaded(Single Severity) |  | 09-Problem Scenario | multi-string multi-module fault diagnosis(Compound Faults) |  |
| 25 | `N4R5BLFT_E051` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | high cost of online monitoring and sensor placement optimization(Other) |  |
| 26 | `N4R5BLFT_E052` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | multi-string multi-module fault diagnosis(Compound Faults) |  |
| 27 | `N4R5BLFT_E053` | `induces_problem` | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  | 09-Problem Scenario | high cost of online monitoring and sensor placement optimization(Other) |  |
| 28 | `N4R5BLFT_E054` | `induces_problem` | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multi-string multi-module fault diagnosis(Compound Faults) |  |
| 29 | `N4R5BLFT_E055` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | high cost of online monitoring and sensor placement optimization(Other) |  |
| 30 | `N4R5BLFT_E056` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | multi-string multi-module fault diagnosis(Compound Faults) |  |

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
