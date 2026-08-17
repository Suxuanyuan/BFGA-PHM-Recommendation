# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：HK5DWGTC
- **Paper Title**：Bidirectional deep recurrent neural networks for process fault classification
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `HK5DWGTC`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "HK5DWGTC_E089", "edge_description": "step change contains No Compound Fault"},
    {"edge_id": "HK5DWGTC_E090", "edge_description": "random variation contains No Compound Fault"},
    {"edge_id": "HK5DWGTC_E091", "edge_description": "slow drift contains No Compound Fault"},
    {"edge_id": "HK5DWGTC_E092", "edge_description": "sticking contains No Compound Fault"},
    {"edge_id": "HK5DWGTC_E093", "edge_description": "valve fixed contains No Compound Fault"},
    {"edge_id": "HK5DWGTC_E094", "edge_description": "feed loss contains No Compound Fault"},
    {"edge_id": "HK5DWGTC_E095", "edge_description": "temperature sensor is collected on reactor"},
    {"edge_id": "HK5DWGTC_E096", "edge_description": "temperature sensor is collected on condenser"},
    {"edge_id": "HK5DWGTC_E097", "edge_description": "temperature sensor is collected on valve"},
    {"edge_id": "HK5DWGTC_E098", "edge_description": "temperature sensor is collected on feed line"},
    {"edge_id": "HK5DWGTC_E099", "edge_description": "pressure sensor is collected on reactor"},
    {"edge_id": "HK5DWGTC_E100", "edge_description": "pressure sensor is collected on condenser"},
    {"edge_id": "HK5DWGTC_E101", "edge_description": "pressure sensor is collected on valve"},
    {"edge_id": "HK5DWGTC_E102", "edge_description": "pressure sensor is collected on feed line"},
    {"edge_id": "HK5DWGTC_E103", "edge_description": "temperature sensor can obviously reflect step change"},
    {"edge_id": "HK5DWGTC_E104", "edge_description": "temperature sensor can obviously reflect random variation"},
    {"edge_id": "HK5DWGTC_E105", "edge_description": "temperature sensor can obviously reflect slow drift"},
    {"edge_id": "HK5DWGTC_E106", "edge_description": "temperature sensor can obviously reflect sticking"},
    {"edge_id": "HK5DWGTC_E107", "edge_description": "temperature sensor can obviously reflect valve fixed"},
    {"edge_id": "HK5DWGTC_E108", "edge_description": "temperature sensor can obviously reflect feed loss"},
    {"edge_id": "HK5DWGTC_E109", "edge_description": "pressure sensor can obviously reflect step change"},
    {"edge_id": "HK5DWGTC_E110", "edge_description": "pressure sensor can obviously reflect random variation"},
    {"edge_id": "HK5DWGTC_E111", "edge_description": "pressure sensor can obviously reflect slow drift"},
    {"edge_id": "HK5DWGTC_E112", "edge_description": "pressure sensor can obviously reflect sticking"},
    {"edge_id": "HK5DWGTC_E113", "edge_description": "pressure sensor can obviously reflect valve fixed"},
    {"edge_id": "HK5DWGTC_E114", "edge_description": "pressure sensor can obviously reflect feed loss"},
    {"edge_id": "HK5DWGTC_E116", "edge_description": "reactor has_fault_mode step change"},
    {"edge_id": "HK5DWGTC_E117", "edge_description": "reactor has_fault_mode random variation"},
    {"edge_id": "HK5DWGTC_E118", "edge_description": "reactor has_fault_mode slow drift"},
    {"edge_id": "HK5DWGTC_E119", "edge_description": "reactor has_fault_mode sticking"}
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
| 1 | `HK5DWGTC_E089` | `contains` | 05-Fault Mode | step change |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `HK5DWGTC_E090` | `contains` | 05-Fault Mode | random variation |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `HK5DWGTC_E091` | `contains` | 05-Fault Mode | slow drift |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `HK5DWGTC_E092` | `contains` | 05-Fault Mode | sticking |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `HK5DWGTC_E093` | `contains` | 05-Fault Mode | valve fixed |  | 07-Compound Fault | No Compound Fault |  |
| 6 | `HK5DWGTC_E094` | `contains` | 05-Fault Mode | feed loss |  | 07-Compound Fault | No Compound Fault |  |
| 7 | `HK5DWGTC_E095` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | reactor |  |
| 8 | `HK5DWGTC_E096` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | condenser |  |
| 9 | `HK5DWGTC_E097` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | valve |  |
| 10 | `HK5DWGTC_E098` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | feed line |  |
| 11 | `HK5DWGTC_E099` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | reactor |  |
| 12 | `HK5DWGTC_E100` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | condenser |  |
| 13 | `HK5DWGTC_E101` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | valve |  |
| 14 | `HK5DWGTC_E102` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | feed line |  |
| 15 | `HK5DWGTC_E103` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | step change |  |
| 16 | `HK5DWGTC_E104` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | random variation |  |
| 17 | `HK5DWGTC_E105` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | slow drift |  |
| 18 | `HK5DWGTC_E106` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | sticking |  |
| 19 | `HK5DWGTC_E107` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | valve fixed |  |
| 20 | `HK5DWGTC_E108` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | feed loss |  |
| 21 | `HK5DWGTC_E109` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | step change |  |
| 22 | `HK5DWGTC_E110` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | random variation |  |
| 23 | `HK5DWGTC_E111` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | slow drift |  |
| 24 | `HK5DWGTC_E112` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | sticking |  |
| 25 | `HK5DWGTC_E113` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | valve fixed |  |
| 26 | `HK5DWGTC_E114` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | feed loss |  |
| 27 | `HK5DWGTC_E116` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | step change |  |
| 28 | `HK5DWGTC_E117` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | random variation |  |
| 29 | `HK5DWGTC_E118` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | slow drift |  |
| 30 | `HK5DWGTC_E119` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | sticking |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
