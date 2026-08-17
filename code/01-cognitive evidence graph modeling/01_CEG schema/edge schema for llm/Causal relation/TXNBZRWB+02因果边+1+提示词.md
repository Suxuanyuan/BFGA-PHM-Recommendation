# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TXNBZRWB
- **Paper Title**：Deep Fuzzy Echo State Networks for Machinery Fault Diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `TXNBZRWB`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TXNBZRWB_E073", "edge_description": "machinery manufacturing contains joint bearing, rolling bearing"},
    {"edge_id": "TXNBZRWB_E074", "edge_description": "machinery manufacturing contains synchronous belt"},
    {"edge_id": "TXNBZRWB_E075", "edge_description": "machinery manufacturing contains 3D printer"},
    {"edge_id": "TXNBZRWB_E076", "edge_description": "joint bearing, rolling bearing contains joint bearing"},
    {"edge_id": "TXNBZRWB_E077", "edge_description": "joint bearing, rolling bearing contains synchronous belt"},
    {"edge_id": "TXNBZRWB_E078", "edge_description": "joint bearing, rolling bearing contains bearing"},
    {"edge_id": "TXNBZRWB_E079", "edge_description": "synchronous belt contains joint bearing"},
    {"edge_id": "TXNBZRWB_E080", "edge_description": "synchronous belt contains synchronous belt"},
    {"edge_id": "TXNBZRWB_E081", "edge_description": "synchronous belt contains bearing"},
    {"edge_id": "TXNBZRWB_E082", "edge_description": "3D printer contains joint bearing"},
    {"edge_id": "TXNBZRWB_E083", "edge_description": "3D printer contains synchronous belt"},
    {"edge_id": "TXNBZRWB_E084", "edge_description": "3D printer contains bearing"},
    {"edge_id": "TXNBZRWB_E085", "edge_description": "joint bearing, rolling bearing contains multiple operating conditions"},
    {"edge_id": "TXNBZRWB_E086", "edge_description": "synchronous belt contains multiple operating conditions"},
    {"edge_id": "TXNBZRWB_E087", "edge_description": "3D printer contains multiple operating conditions"},
    {"edge_id": "TXNBZRWB_E088", "edge_description": "wear contains No Compound Fault"},
    {"edge_id": "TXNBZRWB_E089", "edge_description": "clearance contains No Compound Fault"},
    {"edge_id": "TXNBZRWB_E090", "edge_description": "relaxed contains No Compound Fault"},
    {"edge_id": "TXNBZRWB_E091", "edge_description": "groove defect contains No Compound Fault"},
    {"edge_id": "TXNBZRWB_E092", "edge_description": "attitude sensor is collected on joint bearing"},
    {"edge_id": "TXNBZRWB_E093", "edge_description": "attitude sensor is collected on synchronous belt"},
    {"edge_id": "TXNBZRWB_E094", "edge_description": "attitude sensor is collected on bearing"},
    {"edge_id": "TXNBZRWB_E095", "edge_description": "vibration sensor is collected on joint bearing"},
    {"edge_id": "TXNBZRWB_E096", "edge_description": "vibration sensor is collected on synchronous belt"},
    {"edge_id": "TXNBZRWB_E097", "edge_description": "vibration sensor is collected on bearing"},
    {"edge_id": "TXNBZRWB_E098", "edge_description": "attitude sensor can obviously reflect wear"},
    {"edge_id": "TXNBZRWB_E099", "edge_description": "attitude sensor can obviously reflect clearance"},
    {"edge_id": "TXNBZRWB_E100", "edge_description": "attitude sensor can obviously reflect relaxed"},
    {"edge_id": "TXNBZRWB_E101", "edge_description": "attitude sensor can obviously reflect groove defect"},
    {"edge_id": "TXNBZRWB_E102", "edge_description": "vibration sensor can obviously reflect wear"}
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
| 1 | `TXNBZRWB_E073` | `contains` | 01-Object Domain | machinery manufacturing(Industrial) |  | 02-Object Type | joint bearing, rolling bearing |  |
| 2 | `TXNBZRWB_E074` | `contains` | 01-Object Domain | machinery manufacturing(Industrial) |  | 02-Object Type | synchronous belt |  |
| 3 | `TXNBZRWB_E075` | `contains` | 01-Object Domain | machinery manufacturing(Industrial) |  | 02-Object Type | 3D printer |  |
| 4 | `TXNBZRWB_E076` | `contains` | 02-Object Type | joint bearing, rolling bearing |  | 04-Fault Location | joint bearing |  |
| 5 | `TXNBZRWB_E077` | `contains` | 02-Object Type | joint bearing, rolling bearing |  | 04-Fault Location | synchronous belt |  |
| 6 | `TXNBZRWB_E078` | `contains` | 02-Object Type | joint bearing, rolling bearing |  | 04-Fault Location | bearing |  |
| 7 | `TXNBZRWB_E079` | `contains` | 02-Object Type | synchronous belt |  | 04-Fault Location | joint bearing |  |
| 8 | `TXNBZRWB_E080` | `contains` | 02-Object Type | synchronous belt |  | 04-Fault Location | synchronous belt |  |
| 9 | `TXNBZRWB_E081` | `contains` | 02-Object Type | synchronous belt |  | 04-Fault Location | bearing |  |
| 10 | `TXNBZRWB_E082` | `contains` | 02-Object Type | 3D printer |  | 04-Fault Location | joint bearing |  |
| 11 | `TXNBZRWB_E083` | `contains` | 02-Object Type | 3D printer |  | 04-Fault Location | synchronous belt |  |
| 12 | `TXNBZRWB_E084` | `contains` | 02-Object Type | 3D printer |  | 04-Fault Location | bearing |  |
| 13 | `TXNBZRWB_E085` | `contains` | 02-Object Type | joint bearing, rolling bearing |  | 03-Operating Conditions | multiple operating conditions(Multiple Conditions) |  |
| 14 | `TXNBZRWB_E086` | `contains` | 02-Object Type | synchronous belt |  | 03-Operating Conditions | multiple operating conditions(Multiple Conditions) |  |
| 15 | `TXNBZRWB_E087` | `contains` | 02-Object Type | 3D printer |  | 03-Operating Conditions | multiple operating conditions(Multiple Conditions) |  |
| 16 | `TXNBZRWB_E088` | `contains` | 05-Fault Mode | wear |  | 07-Compound Fault | No Compound Fault |  |
| 17 | `TXNBZRWB_E089` | `contains` | 05-Fault Mode | clearance |  | 07-Compound Fault | No Compound Fault |  |
| 18 | `TXNBZRWB_E090` | `contains` | 05-Fault Mode | relaxed |  | 07-Compound Fault | No Compound Fault |  |
| 19 | `TXNBZRWB_E091` | `contains` | 05-Fault Mode | groove defect |  | 07-Compound Fault | No Compound Fault |  |
| 20 | `TXNBZRWB_E092` | `is collected on` | 11-Sensor Information | attitude sensor |  | 04-Fault Location | joint bearing |  |
| 21 | `TXNBZRWB_E093` | `is collected on` | 11-Sensor Information | attitude sensor |  | 04-Fault Location | synchronous belt |  |
| 22 | `TXNBZRWB_E094` | `is collected on` | 11-Sensor Information | attitude sensor |  | 04-Fault Location | bearing |  |
| 23 | `TXNBZRWB_E095` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | joint bearing |  |
| 24 | `TXNBZRWB_E096` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | synchronous belt |  |
| 25 | `TXNBZRWB_E097` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | bearing |  |
| 26 | `TXNBZRWB_E098` | `can obviously reflect` | 11-Sensor Information | attitude sensor |  | 05-Fault Mode | wear |  |
| 27 | `TXNBZRWB_E099` | `can obviously reflect` | 11-Sensor Information | attitude sensor |  | 05-Fault Mode | clearance |  |
| 28 | `TXNBZRWB_E100` | `can obviously reflect` | 11-Sensor Information | attitude sensor |  | 05-Fault Mode | relaxed |  |
| 29 | `TXNBZRWB_E101` | `can obviously reflect` | 11-Sensor Information | attitude sensor |  | 05-Fault Mode | groove defect |  |
| 30 | `TXNBZRWB_E102` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | wear |  |

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
