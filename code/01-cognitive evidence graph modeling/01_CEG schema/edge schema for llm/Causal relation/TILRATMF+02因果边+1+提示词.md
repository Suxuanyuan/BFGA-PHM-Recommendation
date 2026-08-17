# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TILRATMF
- **Paper Title**：Deep transfer learning with limited data for machinery fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `TILRATMF`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TILRATMF_E093", "edge_description": "rotating machinery contains rolling bearing"},
    {"edge_id": "TILRATMF_E094", "edge_description": "rotating machinery contains gearbox"},
    {"edge_id": "TILRATMF_E095", "edge_description": "rolling bearing contains bearing"},
    {"edge_id": "TILRATMF_E096", "edge_description": "rolling bearing contains gear"},
    {"edge_id": "TILRATMF_E097", "edge_description": "gearbox contains bearing"},
    {"edge_id": "TILRATMF_E098", "edge_description": "gearbox contains gear"},
    {"edge_id": "TILRATMF_E099", "edge_description": "rolling bearing contains variable conditions, time-varying"},
    {"edge_id": "TILRATMF_E100", "edge_description": "gearbox contains variable conditions, time-varying"},
    {"edge_id": "TILRATMF_E101", "edge_description": "pitting contains Outer + inner"},
    {"edge_id": "TILRATMF_E102", "edge_description": "Plastic deform.: Indentations contains Outer + inner"},
    {"edge_id": "TILRATMF_E103", "edge_description": "missing teeth contains Outer + inner"},
    {"edge_id": "TILRATMF_E104", "edge_description": "root crack contains Outer + inner"},
    {"edge_id": "TILRATMF_E105", "edge_description": "surface wear contains Outer + inner"},
    {"edge_id": "TILRATMF_E106", "edge_description": "acceleration sensors is collected on bearing"},
    {"edge_id": "TILRATMF_E107", "edge_description": "acceleration sensors is collected on gear"},
    {"edge_id": "TILRATMF_E108", "edge_description": "acceleration sensors can obviously reflect pitting"},
    {"edge_id": "TILRATMF_E109", "edge_description": "acceleration sensors can obviously reflect Plastic deform.: Indentations"},
    {"edge_id": "TILRATMF_E110", "edge_description": "acceleration sensors can obviously reflect missing teeth"},
    {"edge_id": "TILRATMF_E111", "edge_description": "acceleration sensors can obviously reflect root crack"},
    {"edge_id": "TILRATMF_E112", "edge_description": "acceleration sensors can obviously reflect surface wear"},
    {"edge_id": "TILRATMF_E113", "edge_description": "PU bearings fault datasets can be used for machinery fault diagnosis"},
    {"edge_id": "TILRATMF_E114", "edge_description": "SQI gears fault datasets can be used for machinery fault diagnosis"},
    {"edge_id": "TILRATMF_E115", "edge_description": "Qianpeng gears fault datasets can be used for machinery fault diagnosis"},
    {"edge_id": "TILRATMF_E116", "edge_description": "bearing has_fault_mode pitting"},
    {"edge_id": "TILRATMF_E117", "edge_description": "bearing has_fault_mode Plastic deform.: Indentations"},
    {"edge_id": "TILRATMF_E118", "edge_description": "bearing has_fault_mode missing teeth"},
    {"edge_id": "TILRATMF_E119", "edge_description": "bearing has_fault_mode root crack"},
    {"edge_id": "TILRATMF_E120", "edge_description": "bearing has_fault_mode surface wear"},
    {"edge_id": "TILRATMF_E121", "edge_description": "gear has_fault_mode pitting"},
    {"edge_id": "TILRATMF_E122", "edge_description": "gear has_fault_mode Plastic deform.: Indentations"}
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
| 1 | `TILRATMF_E093` | `contains` | 01-Object Domain | rotating machinery(Industrial) |  | 02-Object Type | rolling bearing |  |
| 2 | `TILRATMF_E094` | `contains` | 01-Object Domain | rotating machinery(Industrial) |  | 02-Object Type | gearbox |  |
| 3 | `TILRATMF_E095` | `contains` | 02-Object Type | rolling bearing |  | 04-Fault Location | bearing |  |
| 4 | `TILRATMF_E096` | `contains` | 02-Object Type | rolling bearing |  | 04-Fault Location | gear |  |
| 5 | `TILRATMF_E097` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | bearing |  |
| 6 | `TILRATMF_E098` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | gear |  |
| 7 | `TILRATMF_E099` | `contains` | 02-Object Type | rolling bearing |  | 03-Operating Conditions | variable conditions, time-varying(Variable Conditions) |  |
| 8 | `TILRATMF_E100` | `contains` | 02-Object Type | gearbox |  | 03-Operating Conditions | variable conditions, time-varying(Variable Conditions) |  |
| 9 | `TILRATMF_E101` | `contains` | 05-Fault Mode | pitting |  | 07-Compound Fault | Outer + inner(Compound Fault Within Same Structure) |  |
| 10 | `TILRATMF_E102` | `contains` | 05-Fault Mode | Plastic deform.: Indentations |  | 07-Compound Fault | Outer + inner(Compound Fault Within Same Structure) |  |
| 11 | `TILRATMF_E103` | `contains` | 05-Fault Mode | missing teeth |  | 07-Compound Fault | Outer + inner(Compound Fault Within Same Structure) |  |
| 12 | `TILRATMF_E104` | `contains` | 05-Fault Mode | root crack |  | 07-Compound Fault | Outer + inner(Compound Fault Within Same Structure) |  |
| 13 | `TILRATMF_E105` | `contains` | 05-Fault Mode | surface wear |  | 07-Compound Fault | Outer + inner(Compound Fault Within Same Structure) |  |
| 14 | `TILRATMF_E106` | `is collected on` | 11-Sensor Information | acceleration sensors |  | 04-Fault Location | bearing |  |
| 15 | `TILRATMF_E107` | `is collected on` | 11-Sensor Information | acceleration sensors |  | 04-Fault Location | gear |  |
| 16 | `TILRATMF_E108` | `can obviously reflect` | 11-Sensor Information | acceleration sensors |  | 05-Fault Mode | pitting |  |
| 17 | `TILRATMF_E109` | `can obviously reflect` | 11-Sensor Information | acceleration sensors |  | 05-Fault Mode | Plastic deform.: Indentations |  |
| 18 | `TILRATMF_E110` | `can obviously reflect` | 11-Sensor Information | acceleration sensors |  | 05-Fault Mode | missing teeth |  |
| 19 | `TILRATMF_E111` | `can obviously reflect` | 11-Sensor Information | acceleration sensors |  | 05-Fault Mode | root crack |  |
| 20 | `TILRATMF_E112` | `can obviously reflect` | 11-Sensor Information | acceleration sensors |  | 05-Fault Mode | surface wear |  |
| 21 | `TILRATMF_E113` | `can be used for` | 10-Dataset | PU bearings fault datasets |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 22 | `TILRATMF_E114` | `can be used for` | 10-Dataset | SQI gears fault datasets |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 23 | `TILRATMF_E115` | `can be used for` | 10-Dataset | Qianpeng gears fault datasets |  | 08-PHM Task | machinery fault diagnosis(Diagnosis Task) |  |
| 24 | `TILRATMF_E116` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | pitting |  |
| 25 | `TILRATMF_E117` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | Plastic deform.: Indentations |  |
| 26 | `TILRATMF_E118` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | missing teeth |  |
| 27 | `TILRATMF_E119` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | root crack |  |
| 28 | `TILRATMF_E120` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | surface wear |  |
| 29 | `TILRATMF_E121` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | pitting |  |
| 30 | `TILRATMF_E122` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | Plastic deform.: Indentations |  |

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
