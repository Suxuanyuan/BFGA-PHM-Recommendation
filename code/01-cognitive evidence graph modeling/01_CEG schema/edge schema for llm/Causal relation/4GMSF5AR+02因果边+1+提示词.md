# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：4GMSF5AR
- **Paper Title**：A framework to automate fault detection and diagnosis based on moving window principal component analysis and Bayesian network
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `4GMSF5AR`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "4GMSF5AR_E073", "edge_description": "hydrogenerator / hydroelectric power plant contains hydrogenerator"},
    {"edge_id": "4GMSF5AR_E074", "edge_description": "hydrogenerator / hydroelectric power plant contains turbine"},
    {"edge_id": "4GMSF5AR_E075", "edge_description": "hydrogenerator / hydroelectric power plant contains heat exchanger"},
    {"edge_id": "4GMSF5AR_E076", "edge_description": "hydrogenerator contains Generator shaft"},
    {"edge_id": "4GMSF5AR_E077", "edge_description": "hydrogenerator contains Stator"},
    {"edge_id": "4GMSF5AR_E078", "edge_description": "hydrogenerator contains Temperature sensor of combined bearing heat exchanger exit (hot) water"},
    {"edge_id": "4GMSF5AR_E079", "edge_description": "turbine contains Generator shaft"},
    {"edge_id": "4GMSF5AR_E080", "edge_description": "turbine contains Stator"},
    {"edge_id": "4GMSF5AR_E081", "edge_description": "turbine contains Temperature sensor of combined bearing heat exchanger exit (hot) water"},
    {"edge_id": "4GMSF5AR_E082", "edge_description": "heat exchanger contains Generator shaft"},
    {"edge_id": "4GMSF5AR_E083", "edge_description": "heat exchanger contains Stator"},
    {"edge_id": "4GMSF5AR_E084", "edge_description": "heat exchanger contains Temperature sensor of combined bearing heat exchanger exit (hot) water"},
    {"edge_id": "4GMSF5AR_E085", "edge_description": "hydrogenerator contains steady-state condition (variation of at most 1.5% of the nominal values of output power and the net head)"},
    {"edge_id": "4GMSF5AR_E086", "edge_description": "turbine contains steady-state condition (variation of at most 1.5% of the nominal values of output power and the net head)"},
    {"edge_id": "4GMSF5AR_E087", "edge_description": "heat exchanger contains steady-state condition (variation of at most 1.5% of the nominal values of output power and the net head)"},
    {"edge_id": "4GMSF5AR_E088", "edge_description": "Excessive vibration contains No Compound Fault"},
    {"edge_id": "4GMSF5AR_E089", "edge_description": "Premature degradation of copper insulation contains No Compound Fault"},
    {"edge_id": "4GMSF5AR_E090", "edge_description": "Does not indicate the actual temperature value contains No Compound Fault"},
    {"edge_id": "4GMSF5AR_E091", "edge_description": "temperature sensor is collected on Generator shaft"},
    {"edge_id": "4GMSF5AR_E092", "edge_description": "temperature sensor is collected on Stator"},
    {"edge_id": "4GMSF5AR_E093", "edge_description": "temperature sensor is collected on Temperature sensor of combined bearing heat exchanger exit (hot) water"},
    {"edge_id": "4GMSF5AR_E094", "edge_description": "proximity sensor is collected on Generator shaft"},
    {"edge_id": "4GMSF5AR_E095", "edge_description": "proximity sensor is collected on Stator"},
    {"edge_id": "4GMSF5AR_E096", "edge_description": "proximity sensor is collected on Temperature sensor of combined bearing heat exchanger exit (hot) water"},
    {"edge_id": "4GMSF5AR_E097", "edge_description": "temperature sensor can obviously reflect Excessive vibration"},
    {"edge_id": "4GMSF5AR_E098", "edge_description": "temperature sensor can obviously reflect Premature degradation of copper insulation"},
    {"edge_id": "4GMSF5AR_E099", "edge_description": "temperature sensor can obviously reflect Does not indicate the actual temperature value"},
    {"edge_id": "4GMSF5AR_E100", "edge_description": "proximity sensor can obviously reflect Excessive vibration"},
    {"edge_id": "4GMSF5AR_E101", "edge_description": "proximity sensor can obviously reflect Premature degradation of copper insulation"},
    {"edge_id": "4GMSF5AR_E102", "edge_description": "proximity sensor can obviously reflect Does not indicate the actual temperature value"}
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
| 1 | `4GMSF5AR_E073` | `contains` | 01-Object Domain | hydrogenerator / hydroelectric power plant(Industrial) |  | 02-Object Type | hydrogenerator |  |
| 2 | `4GMSF5AR_E074` | `contains` | 01-Object Domain | hydrogenerator / hydroelectric power plant(Industrial) |  | 02-Object Type | turbine |  |
| 3 | `4GMSF5AR_E075` | `contains` | 01-Object Domain | hydrogenerator / hydroelectric power plant(Industrial) |  | 02-Object Type | heat exchanger |  |
| 4 | `4GMSF5AR_E076` | `contains` | 02-Object Type | hydrogenerator |  | 04-Fault Location | Generator shaft |  |
| 5 | `4GMSF5AR_E077` | `contains` | 02-Object Type | hydrogenerator |  | 04-Fault Location | Stator |  |
| 6 | `4GMSF5AR_E078` | `contains` | 02-Object Type | hydrogenerator |  | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  |
| 7 | `4GMSF5AR_E079` | `contains` | 02-Object Type | turbine |  | 04-Fault Location | Generator shaft |  |
| 8 | `4GMSF5AR_E080` | `contains` | 02-Object Type | turbine |  | 04-Fault Location | Stator |  |
| 9 | `4GMSF5AR_E081` | `contains` | 02-Object Type | turbine |  | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  |
| 10 | `4GMSF5AR_E082` | `contains` | 02-Object Type | heat exchanger |  | 04-Fault Location | Generator shaft |  |
| 11 | `4GMSF5AR_E083` | `contains` | 02-Object Type | heat exchanger |  | 04-Fault Location | Stator |  |
| 12 | `4GMSF5AR_E084` | `contains` | 02-Object Type | heat exchanger |  | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  |
| 13 | `4GMSF5AR_E085` | `contains` | 02-Object Type | hydrogenerator |  | 03-Operating Conditions | steady-state condition (variation of at most 1.5% of the nominal values of output power and the net head)(Single Condition) |  |
| 14 | `4GMSF5AR_E086` | `contains` | 02-Object Type | turbine |  | 03-Operating Conditions | steady-state condition (variation of at most 1.5% of the nominal values of output power and the net head)(Single Condition) |  |
| 15 | `4GMSF5AR_E087` | `contains` | 02-Object Type | heat exchanger |  | 03-Operating Conditions | steady-state condition (variation of at most 1.5% of the nominal values of output power and the net head)(Single Condition) |  |
| 16 | `4GMSF5AR_E088` | `contains` | 05-Fault Mode | Excessive vibration |  | 07-Compound Fault | No Compound Fault |  |
| 17 | `4GMSF5AR_E089` | `contains` | 05-Fault Mode | Premature degradation of copper insulation |  | 07-Compound Fault | No Compound Fault |  |
| 18 | `4GMSF5AR_E090` | `contains` | 05-Fault Mode | Does not indicate the actual temperature value |  | 07-Compound Fault | No Compound Fault |  |
| 19 | `4GMSF5AR_E091` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | Generator shaft |  |
| 20 | `4GMSF5AR_E092` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | Stator |  |
| 21 | `4GMSF5AR_E093` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  |
| 22 | `4GMSF5AR_E094` | `is collected on` | 11-Sensor Information | proximity sensor |  | 04-Fault Location | Generator shaft |  |
| 23 | `4GMSF5AR_E095` | `is collected on` | 11-Sensor Information | proximity sensor |  | 04-Fault Location | Stator |  |
| 24 | `4GMSF5AR_E096` | `is collected on` | 11-Sensor Information | proximity sensor |  | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  |
| 25 | `4GMSF5AR_E097` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | Excessive vibration |  |
| 26 | `4GMSF5AR_E098` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | Premature degradation of copper insulation |  |
| 27 | `4GMSF5AR_E099` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | Does not indicate the actual temperature value |  |
| 28 | `4GMSF5AR_E100` | `can obviously reflect` | 11-Sensor Information | proximity sensor |  | 05-Fault Mode | Excessive vibration |  |
| 29 | `4GMSF5AR_E101` | `can obviously reflect` | 11-Sensor Information | proximity sensor |  | 05-Fault Mode | Premature degradation of copper insulation |  |
| 30 | `4GMSF5AR_E102` | `can obviously reflect` | 11-Sensor Information | proximity sensor |  | 05-Fault Mode | Does not indicate the actual temperature value |  |

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
