# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：DNA5PWZ6
- **Paper Title**：Fault Diagnosis of Induction Motors Using Recurrence Quantification Analysis and LSTM with Weighted BN
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `DNA5PWZ6`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "DNA5PWZ6_E068", "edge_description": "three-phase induction motor contains induction motor"},
    {"edge_id": "DNA5PWZ6_E069", "edge_description": "three-phase induction motor contains bearings"},
    {"edge_id": "DNA5PWZ6_E071", "edge_description": "broken rotor bars contains one inner race faulted bearing and one outer race faulted bearing"},
    {"edge_id": "DNA5PWZ6_E072", "edge_description": "bowed rotor contains one inner race faulted bearing and one outer race faulted bearing"},
    {"edge_id": "DNA5PWZ6_E073", "edge_description": "rotor misalignment contains one inner race faulted bearing and one outer race faulted bearing"},
    {"edge_id": "DNA5PWZ6_E074", "edge_description": "shorted stator winding turns contains one inner race faulted bearing and one outer race faulted bearing"},
    {"edge_id": "DNA5PWZ6_E075", "edge_description": "single phasing contains one inner race faulted bearing and one outer race faulted bearing"},
    {"edge_id": "DNA5PWZ6_E076", "edge_description": "rotor unbalance contains one inner race faulted bearing and one outer race faulted bearing"},
    {"edge_id": "DNA5PWZ6_E077", "edge_description": "inner race faulted and outer race faulted bearings contains one inner race faulted bearing and one outer race faulted bearing"},
    {"edge_id": "DNA5PWZ6_E078", "edge_description": "acceleration sensor BW-BJ14530 is collected on induction motor"},
    {"edge_id": "DNA5PWZ6_E079", "edge_description": "acceleration sensor BW-BJ14530 is collected on bearings"},
    {"edge_id": "DNA5PWZ6_E080", "edge_description": "acceleration sensor BW-BJ14530 can obviously reflect broken rotor bars"},
    {"edge_id": "DNA5PWZ6_E081", "edge_description": "acceleration sensor BW-BJ14530 can obviously reflect bowed rotor"},
    {"edge_id": "DNA5PWZ6_E082", "edge_description": "acceleration sensor BW-BJ14530 can obviously reflect rotor misalignment"},
    {"edge_id": "DNA5PWZ6_E083", "edge_description": "acceleration sensor BW-BJ14530 can obviously reflect shorted stator winding turns"},
    {"edge_id": "DNA5PWZ6_E084", "edge_description": "acceleration sensor BW-BJ14530 can obviously reflect single phasing"},
    {"edge_id": "DNA5PWZ6_E085", "edge_description": "acceleration sensor BW-BJ14530 can obviously reflect rotor unbalance"},
    {"edge_id": "DNA5PWZ6_E086", "edge_description": "acceleration sensor BW-BJ14530 can obviously reflect inner race faulted and outer race faulted bearings"},
    {"edge_id": "DNA5PWZ6_E088", "edge_description": "induction motor has_fault_mode broken rotor bars"},
    {"edge_id": "DNA5PWZ6_E089", "edge_description": "induction motor has_fault_mode bowed rotor"},
    {"edge_id": "DNA5PWZ6_E090", "edge_description": "induction motor has_fault_mode rotor misalignment"},
    {"edge_id": "DNA5PWZ6_E091", "edge_description": "induction motor has_fault_mode shorted stator winding turns"},
    {"edge_id": "DNA5PWZ6_E092", "edge_description": "induction motor has_fault_mode single phasing"},
    {"edge_id": "DNA5PWZ6_E093", "edge_description": "induction motor has_fault_mode rotor unbalance"},
    {"edge_id": "DNA5PWZ6_E094", "edge_description": "induction motor has_fault_mode inner race faulted and outer race faulted bearings"},
    {"edge_id": "DNA5PWZ6_E095", "edge_description": "bearings has_fault_mode broken rotor bars"},
    {"edge_id": "DNA5PWZ6_E096", "edge_description": "bearings has_fault_mode bowed rotor"},
    {"edge_id": "DNA5PWZ6_E097", "edge_description": "bearings has_fault_mode rotor misalignment"},
    {"edge_id": "DNA5PWZ6_E098", "edge_description": "bearings has_fault_mode shorted stator winding turns"},
    {"edge_id": "DNA5PWZ6_E099", "edge_description": "bearings has_fault_mode single phasing"}
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
| 1 | `DNA5PWZ6_E068` | `contains` | 02-Object Type | three-phase induction motor |  | 04-Fault Location | induction motor |  |
| 2 | `DNA5PWZ6_E069` | `contains` | 02-Object Type | three-phase induction motor |  | 04-Fault Location | bearings |  |
| 3 | `DNA5PWZ6_E071` | `contains` | 05-Fault Mode | broken rotor bars |  | 07-Compound Fault | one inner race faulted bearing and one outer race faulted bearing(Compound Fault Within Same Structure) |  |
| 4 | `DNA5PWZ6_E072` | `contains` | 05-Fault Mode | bowed rotor |  | 07-Compound Fault | one inner race faulted bearing and one outer race faulted bearing(Compound Fault Within Same Structure) |  |
| 5 | `DNA5PWZ6_E073` | `contains` | 05-Fault Mode | rotor misalignment |  | 07-Compound Fault | one inner race faulted bearing and one outer race faulted bearing(Compound Fault Within Same Structure) |  |
| 6 | `DNA5PWZ6_E074` | `contains` | 05-Fault Mode | shorted stator winding turns |  | 07-Compound Fault | one inner race faulted bearing and one outer race faulted bearing(Compound Fault Within Same Structure) |  |
| 7 | `DNA5PWZ6_E075` | `contains` | 05-Fault Mode | single phasing |  | 07-Compound Fault | one inner race faulted bearing and one outer race faulted bearing(Compound Fault Within Same Structure) |  |
| 8 | `DNA5PWZ6_E076` | `contains` | 05-Fault Mode | rotor unbalance |  | 07-Compound Fault | one inner race faulted bearing and one outer race faulted bearing(Compound Fault Within Same Structure) |  |
| 9 | `DNA5PWZ6_E077` | `contains` | 05-Fault Mode | inner race faulted and outer race faulted bearings |  | 07-Compound Fault | one inner race faulted bearing and one outer race faulted bearing(Compound Fault Within Same Structure) |  |
| 10 | `DNA5PWZ6_E078` | `is collected on` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 04-Fault Location | induction motor |  |
| 11 | `DNA5PWZ6_E079` | `is collected on` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 04-Fault Location | bearings |  |
| 12 | `DNA5PWZ6_E080` | `can obviously reflect` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 05-Fault Mode | broken rotor bars |  |
| 13 | `DNA5PWZ6_E081` | `can obviously reflect` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 05-Fault Mode | bowed rotor |  |
| 14 | `DNA5PWZ6_E082` | `can obviously reflect` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 05-Fault Mode | rotor misalignment |  |
| 15 | `DNA5PWZ6_E083` | `can obviously reflect` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 05-Fault Mode | shorted stator winding turns |  |
| 16 | `DNA5PWZ6_E084` | `can obviously reflect` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 05-Fault Mode | single phasing |  |
| 17 | `DNA5PWZ6_E085` | `can obviously reflect` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 05-Fault Mode | rotor unbalance |  |
| 18 | `DNA5PWZ6_E086` | `can obviously reflect` | 11-Sensor Information | acceleration sensor BW-BJ14530 |  | 05-Fault Mode | inner race faulted and outer race faulted bearings |  |
| 19 | `DNA5PWZ6_E088` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | broken rotor bars |  |
| 20 | `DNA5PWZ6_E089` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | bowed rotor |  |
| 21 | `DNA5PWZ6_E090` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | rotor misalignment |  |
| 22 | `DNA5PWZ6_E091` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | shorted stator winding turns |  |
| 23 | `DNA5PWZ6_E092` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | single phasing |  |
| 24 | `DNA5PWZ6_E093` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | rotor unbalance |  |
| 25 | `DNA5PWZ6_E094` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | inner race faulted and outer race faulted bearings |  |
| 26 | `DNA5PWZ6_E095` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | broken rotor bars |  |
| 27 | `DNA5PWZ6_E096` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | bowed rotor |  |
| 28 | `DNA5PWZ6_E097` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | rotor misalignment |  |
| 29 | `DNA5PWZ6_E098` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | shorted stator winding turns |  |
| 30 | `DNA5PWZ6_E099` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | single phasing |  |

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
