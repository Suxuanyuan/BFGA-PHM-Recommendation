# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：83EHBXXQ
- **Paper Title**：Real-Time Diagnosis for Open-Circuited and Unbalance Faults in Electronic Converters Connected to Residential Wind Systems
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `83EHBXXQ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "83EHBXXQ_E067", "edge_description": "residential wind systems contains power electronic converter"},
    {"edge_id": "83EHBXXQ_E068", "edge_description": "residential wind systems contains uncontrolled three-phase rectifier"},
    {"edge_id": "83EHBXXQ_E069", "edge_description": "residential wind systems contains boost chopper"},
    {"edge_id": "83EHBXXQ_E070", "edge_description": "residential wind systems contains single-phase inverter"},
    {"edge_id": "83EHBXXQ_E071", "edge_description": "power electronic converter contains uncontrolled three-phase rectifier"},
    {"edge_id": "83EHBXXQ_E072", "edge_description": "power electronic converter contains boost chopper"},
    {"edge_id": "83EHBXXQ_E073", "edge_description": "power electronic converter contains single-phase inverter"},
    {"edge_id": "83EHBXXQ_E074", "edge_description": "uncontrolled three-phase rectifier contains uncontrolled three-phase rectifier"},
    {"edge_id": "83EHBXXQ_E075", "edge_description": "uncontrolled three-phase rectifier contains boost chopper"},
    {"edge_id": "83EHBXXQ_E076", "edge_description": "uncontrolled three-phase rectifier contains single-phase inverter"},
    {"edge_id": "83EHBXXQ_E077", "edge_description": "boost chopper contains uncontrolled three-phase rectifier"},
    {"edge_id": "83EHBXXQ_E078", "edge_description": "boost chopper contains boost chopper"},
    {"edge_id": "83EHBXXQ_E079", "edge_description": "boost chopper contains single-phase inverter"},
    {"edge_id": "83EHBXXQ_E080", "edge_description": "single-phase inverter contains uncontrolled three-phase rectifier"},
    {"edge_id": "83EHBXXQ_E081", "edge_description": "single-phase inverter contains boost chopper"},
    {"edge_id": "83EHBXXQ_E082", "edge_description": "single-phase inverter contains single-phase inverter"},
    {"edge_id": "83EHBXXQ_E083", "edge_description": "power electronic converter contains input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V"},
    {"edge_id": "83EHBXXQ_E084", "edge_description": "uncontrolled three-phase rectifier contains input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V"},
    {"edge_id": "83EHBXXQ_E085", "edge_description": "boost chopper contains input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V"},
    {"edge_id": "83EHBXXQ_E086", "edge_description": "single-phase inverter contains input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V"},
    {"edge_id": "83EHBXXQ_E087", "edge_description": "open circuit faults contains No Compound Fault"},
    {"edge_id": "83EHBXXQ_E088", "edge_description": "unbalance input voltage contains No Compound Fault"},
    {"edge_id": "83EHBXXQ_E089", "edge_description": "voltage sensor is collected on uncontrolled three-phase rectifier"},
    {"edge_id": "83EHBXXQ_E090", "edge_description": "voltage sensor is collected on boost chopper"},
    {"edge_id": "83EHBXXQ_E091", "edge_description": "voltage sensor is collected on single-phase inverter"},
    {"edge_id": "83EHBXXQ_E092", "edge_description": "current sensor is collected on uncontrolled three-phase rectifier"},
    {"edge_id": "83EHBXXQ_E093", "edge_description": "current sensor is collected on boost chopper"},
    {"edge_id": "83EHBXXQ_E094", "edge_description": "current sensor is collected on single-phase inverter"},
    {"edge_id": "83EHBXXQ_E095", "edge_description": "voltage sensor can obviously reflect open circuit faults"},
    {"edge_id": "83EHBXXQ_E096", "edge_description": "voltage sensor can obviously reflect unbalance input voltage"}
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
| 1 | `83EHBXXQ_E067` | `contains` | 01-Object Domain | residential wind systems(Industrial) |  | 02-Object Type | power electronic converter |  |
| 2 | `83EHBXXQ_E068` | `contains` | 01-Object Domain | residential wind systems(Industrial) |  | 02-Object Type | uncontrolled three-phase rectifier |  |
| 3 | `83EHBXXQ_E069` | `contains` | 01-Object Domain | residential wind systems(Industrial) |  | 02-Object Type | boost chopper |  |
| 4 | `83EHBXXQ_E070` | `contains` | 01-Object Domain | residential wind systems(Industrial) |  | 02-Object Type | single-phase inverter |  |
| 5 | `83EHBXXQ_E071` | `contains` | 02-Object Type | power electronic converter |  | 04-Fault Location | uncontrolled three-phase rectifier |  |
| 6 | `83EHBXXQ_E072` | `contains` | 02-Object Type | power electronic converter |  | 04-Fault Location | boost chopper |  |
| 7 | `83EHBXXQ_E073` | `contains` | 02-Object Type | power electronic converter |  | 04-Fault Location | single-phase inverter |  |
| 8 | `83EHBXXQ_E074` | `contains` | 02-Object Type | uncontrolled three-phase rectifier |  | 04-Fault Location | uncontrolled three-phase rectifier |  |
| 9 | `83EHBXXQ_E075` | `contains` | 02-Object Type | uncontrolled three-phase rectifier |  | 04-Fault Location | boost chopper |  |
| 10 | `83EHBXXQ_E076` | `contains` | 02-Object Type | uncontrolled three-phase rectifier |  | 04-Fault Location | single-phase inverter |  |
| 11 | `83EHBXXQ_E077` | `contains` | 02-Object Type | boost chopper |  | 04-Fault Location | uncontrolled three-phase rectifier |  |
| 12 | `83EHBXXQ_E078` | `contains` | 02-Object Type | boost chopper |  | 04-Fault Location | boost chopper |  |
| 13 | `83EHBXXQ_E079` | `contains` | 02-Object Type | boost chopper |  | 04-Fault Location | single-phase inverter |  |
| 14 | `83EHBXXQ_E080` | `contains` | 02-Object Type | single-phase inverter |  | 04-Fault Location | uncontrolled three-phase rectifier |  |
| 15 | `83EHBXXQ_E081` | `contains` | 02-Object Type | single-phase inverter |  | 04-Fault Location | boost chopper |  |
| 16 | `83EHBXXQ_E082` | `contains` | 02-Object Type | single-phase inverter |  | 04-Fault Location | single-phase inverter |  |
| 17 | `83EHBXXQ_E083` | `contains` | 02-Object Type | power electronic converter |  | 03-Operating Conditions | input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V(Multiple Conditions) |  |
| 18 | `83EHBXXQ_E084` | `contains` | 02-Object Type | uncontrolled three-phase rectifier |  | 03-Operating Conditions | input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V(Multiple Conditions) |  |
| 19 | `83EHBXXQ_E085` | `contains` | 02-Object Type | boost chopper |  | 03-Operating Conditions | input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V(Multiple Conditions) |  |
| 20 | `83EHBXXQ_E086` | `contains` | 02-Object Type | single-phase inverter |  | 03-Operating Conditions | input frequencies from 20 to 80 Hz, supply voltage VSrms from 50 to 250 V and 100 to 300 V(Multiple Conditions) |  |
| 21 | `83EHBXXQ_E087` | `contains` | 05-Fault Mode | open circuit faults |  | 07-Compound Fault | No Compound Fault |  |
| 22 | `83EHBXXQ_E088` | `contains` | 05-Fault Mode | unbalance input voltage |  | 07-Compound Fault | No Compound Fault |  |
| 23 | `83EHBXXQ_E089` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | uncontrolled three-phase rectifier |  |
| 24 | `83EHBXXQ_E090` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | boost chopper |  |
| 25 | `83EHBXXQ_E091` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | single-phase inverter |  |
| 26 | `83EHBXXQ_E092` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | uncontrolled three-phase rectifier |  |
| 27 | `83EHBXXQ_E093` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | boost chopper |  |
| 28 | `83EHBXXQ_E094` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | single-phase inverter |  |
| 29 | `83EHBXXQ_E095` | `can obviously reflect` | 11-Sensor Information | voltage sensor |  | 05-Fault Mode | open circuit faults |  |
| 30 | `83EHBXXQ_E096` | `can obviously reflect` | 11-Sensor Information | voltage sensor |  | 05-Fault Mode | unbalance input voltage |  |

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
