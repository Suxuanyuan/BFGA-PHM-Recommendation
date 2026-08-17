# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：NY4HLI6F
- **Paper Title**：Cascade Convolutional Neural Network With Progressive Optimization for Motor Fault Diagnosis Under Nonstationary Conditions
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `NY4HLI6F`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "NY4HLI6F_E071", "edge_description": "motor contains motor"},
    {"edge_id": "NY4HLI6F_E072", "edge_description": "motor contains bearing"},
    {"edge_id": "NY4HLI6F_E073", "edge_description": "motor contains coupling"},
    {"edge_id": "NY4HLI6F_E075", "edge_description": "broken rotor bar contains No Compound Fault"},
    {"edge_id": "NY4HLI6F_E076", "edge_description": "unbalanced rotor contains No Compound Fault"},
    {"edge_id": "NY4HLI6F_E077", "edge_description": "angular misalignment, parallel misalignment contains No Compound Fault"},
    {"edge_id": "NY4HLI6F_E078", "edge_description": "faulted bearing contains No Compound Fault"},
    {"edge_id": "NY4HLI6F_E079", "edge_description": "bowed rotor contains No Compound Fault"},
    {"edge_id": "NY4HLI6F_E080", "edge_description": "low impedance, high impedance contains No Compound Fault"},
    {"edge_id": "NY4HLI6F_E081", "edge_description": "accelerometer is collected on motor"},
    {"edge_id": "NY4HLI6F_E082", "edge_description": "accelerometer is collected on bearing"},
    {"edge_id": "NY4HLI6F_E083", "edge_description": "accelerometer is collected on coupling"},
    {"edge_id": "NY4HLI6F_E084", "edge_description": "accelerometer can obviously reflect broken rotor bar"},
    {"edge_id": "NY4HLI6F_E085", "edge_description": "accelerometer can obviously reflect unbalanced rotor"},
    {"edge_id": "NY4HLI6F_E086", "edge_description": "accelerometer can obviously reflect angular misalignment, parallel misalignment"},
    {"edge_id": "NY4HLI6F_E087", "edge_description": "accelerometer can obviously reflect faulted bearing"},
    {"edge_id": "NY4HLI6F_E088", "edge_description": "accelerometer can obviously reflect bowed rotor"},
    {"edge_id": "NY4HLI6F_E089", "edge_description": "accelerometer can obviously reflect low impedance, high impedance"},
    {"edge_id": "NY4HLI6F_E090", "edge_description": "Motor experiment under constant rotating speed can be used for motor fault diagnosis"},
    {"edge_id": "NY4HLI6F_E091", "edge_description": "Motor experiment under variable speed can be used for motor fault diagnosis"},
    {"edge_id": "NY4HLI6F_E092", "edge_description": "motor has_fault_mode broken rotor bar"},
    {"edge_id": "NY4HLI6F_E093", "edge_description": "motor has_fault_mode unbalanced rotor"},
    {"edge_id": "NY4HLI6F_E094", "edge_description": "motor has_fault_mode angular misalignment, parallel misalignment"},
    {"edge_id": "NY4HLI6F_E095", "edge_description": "motor has_fault_mode faulted bearing"},
    {"edge_id": "NY4HLI6F_E096", "edge_description": "motor has_fault_mode bowed rotor"},
    {"edge_id": "NY4HLI6F_E097", "edge_description": "motor has_fault_mode low impedance, high impedance"},
    {"edge_id": "NY4HLI6F_E098", "edge_description": "bearing has_fault_mode broken rotor bar"},
    {"edge_id": "NY4HLI6F_E099", "edge_description": "bearing has_fault_mode unbalanced rotor"},
    {"edge_id": "NY4HLI6F_E100", "edge_description": "bearing has_fault_mode angular misalignment, parallel misalignment"},
    {"edge_id": "NY4HLI6F_E101", "edge_description": "bearing has_fault_mode faulted bearing"}
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
| 1 | `NY4HLI6F_E071` | `contains` | 02-Object Type | motor |  | 04-Fault Location | motor |  |
| 2 | `NY4HLI6F_E072` | `contains` | 02-Object Type | motor |  | 04-Fault Location | bearing |  |
| 3 | `NY4HLI6F_E073` | `contains` | 02-Object Type | motor |  | 04-Fault Location | coupling |  |
| 4 | `NY4HLI6F_E075` | `contains` | 05-Fault Mode | broken rotor bar |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `NY4HLI6F_E076` | `contains` | 05-Fault Mode | unbalanced rotor |  | 07-Compound Fault | No Compound Fault |  |
| 6 | `NY4HLI6F_E077` | `contains` | 05-Fault Mode | angular misalignment, parallel misalignment |  | 07-Compound Fault | No Compound Fault |  |
| 7 | `NY4HLI6F_E078` | `contains` | 05-Fault Mode | faulted bearing |  | 07-Compound Fault | No Compound Fault |  |
| 8 | `NY4HLI6F_E079` | `contains` | 05-Fault Mode | bowed rotor |  | 07-Compound Fault | No Compound Fault |  |
| 9 | `NY4HLI6F_E080` | `contains` | 05-Fault Mode | low impedance, high impedance |  | 07-Compound Fault | No Compound Fault |  |
| 10 | `NY4HLI6F_E081` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | motor |  |
| 11 | `NY4HLI6F_E082` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | bearing |  |
| 12 | `NY4HLI6F_E083` | `is collected on` | 11-Sensor Information | accelerometer |  | 04-Fault Location | coupling |  |
| 13 | `NY4HLI6F_E084` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | broken rotor bar |  |
| 14 | `NY4HLI6F_E085` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | unbalanced rotor |  |
| 15 | `NY4HLI6F_E086` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | angular misalignment, parallel misalignment |  |
| 16 | `NY4HLI6F_E087` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | faulted bearing |  |
| 17 | `NY4HLI6F_E088` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | bowed rotor |  |
| 18 | `NY4HLI6F_E089` | `can obviously reflect` | 11-Sensor Information | accelerometer |  | 05-Fault Mode | low impedance, high impedance |  |
| 19 | `NY4HLI6F_E090` | `can be used for` | 10-Dataset | Motor experiment under constant rotating speed |  | 08-PHM Task | motor fault diagnosis(Diagnosis Task) |  |
| 20 | `NY4HLI6F_E091` | `can be used for` | 10-Dataset | Motor experiment under variable speed |  | 08-PHM Task | motor fault diagnosis(Diagnosis Task) |  |
| 21 | `NY4HLI6F_E092` | `has_fault_mode` | 04-Fault Location | motor |  | 05-Fault Mode | broken rotor bar |  |
| 22 | `NY4HLI6F_E093` | `has_fault_mode` | 04-Fault Location | motor |  | 05-Fault Mode | unbalanced rotor |  |
| 23 | `NY4HLI6F_E094` | `has_fault_mode` | 04-Fault Location | motor |  | 05-Fault Mode | angular misalignment, parallel misalignment |  |
| 24 | `NY4HLI6F_E095` | `has_fault_mode` | 04-Fault Location | motor |  | 05-Fault Mode | faulted bearing |  |
| 25 | `NY4HLI6F_E096` | `has_fault_mode` | 04-Fault Location | motor |  | 05-Fault Mode | bowed rotor |  |
| 26 | `NY4HLI6F_E097` | `has_fault_mode` | 04-Fault Location | motor |  | 05-Fault Mode | low impedance, high impedance |  |
| 27 | `NY4HLI6F_E098` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | broken rotor bar |  |
| 28 | `NY4HLI6F_E099` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | unbalanced rotor |  |
| 29 | `NY4HLI6F_E100` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | angular misalignment, parallel misalignment |  |
| 30 | `NY4HLI6F_E101` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | faulted bearing |  |

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
