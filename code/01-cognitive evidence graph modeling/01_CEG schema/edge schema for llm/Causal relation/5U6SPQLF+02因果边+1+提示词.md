# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：5U6SPQLF
- **Paper Title**：Discriminative feature-based adaptive distribution alignment (DFADA) for rotating machine fault diagnosis under variable working conditions
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `5U6SPQLF`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "5U6SPQLF_E081", "edge_description": "rotating machinery contains bearing"},
    {"edge_id": "5U6SPQLF_E082", "edge_description": "rotating machinery contains gearbox"},
    {"edge_id": "5U6SPQLF_E083", "edge_description": "bearing contains bearing"},
    {"edge_id": "5U6SPQLF_E084", "edge_description": "bearing contains gearbox"},
    {"edge_id": "5U6SPQLF_E085", "edge_description": "gearbox contains bearing"},
    {"edge_id": "5U6SPQLF_E086", "edge_description": "gearbox contains gearbox"},
    {"edge_id": "5U6SPQLF_E087", "edge_description": "bearing contains variable working conditions"},
    {"edge_id": "5U6SPQLF_E088", "edge_description": "gearbox contains variable working conditions"},
    {"edge_id": "5U6SPQLF_E089", "edge_description": "pitting contains complicated faults"},
    {"edge_id": "5U6SPQLF_E090", "edge_description": "broken-tooth contains complicated faults"},
    {"edge_id": "5U6SPQLF_E091", "edge_description": "worn contains complicated faults"},
    {"edge_id": "5U6SPQLF_E092", "edge_description": "vibration sensor is collected on bearing"},
    {"edge_id": "5U6SPQLF_E093", "edge_description": "vibration sensor is collected on gearbox"},
    {"edge_id": "5U6SPQLF_E094", "edge_description": "vibration sensor can obviously reflect pitting"},
    {"edge_id": "5U6SPQLF_E095", "edge_description": "vibration sensor can obviously reflect broken-tooth"},
    {"edge_id": "5U6SPQLF_E096", "edge_description": "vibration sensor can obviously reflect worn"},
    {"edge_id": "5U6SPQLF_E097", "edge_description": "bearing dataset from Case Western Reserve University (CWRU) can be used for fault diagnosis"},
    {"edge_id": "5U6SPQLF_E098", "edge_description": "gearbox vibration signal dataset can be used for fault diagnosis"},
    {"edge_id": "5U6SPQLF_E099", "edge_description": "bearing has_fault_mode pitting"},
    {"edge_id": "5U6SPQLF_E100", "edge_description": "bearing has_fault_mode broken-tooth"},
    {"edge_id": "5U6SPQLF_E101", "edge_description": "bearing has_fault_mode worn"},
    {"edge_id": "5U6SPQLF_E102", "edge_description": "gearbox has_fault_mode pitting"},
    {"edge_id": "5U6SPQLF_E103", "edge_description": "gearbox has_fault_mode broken-tooth"},
    {"edge_id": "5U6SPQLF_E104", "edge_description": "gearbox has_fault_mode worn"},
    {"edge_id": "5U6SPQLF_E105", "edge_description": "pitting contains 10 health conditions"},
    {"edge_id": "5U6SPQLF_E106", "edge_description": "broken-tooth contains 10 health conditions"},
    {"edge_id": "5U6SPQLF_E107", "edge_description": "worn contains 10 health conditions"},
    {"edge_id": "5U6SPQLF_E108", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "5U6SPQLF_E109", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "5U6SPQLF_E110", "edge_description": "bearing contains_phm_task fault diagnosis"}
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
| 1 | `5U6SPQLF_E081` | `contains` | 01-Object Domain | rotating machinery(Industrial) |  | 02-Object Type | bearing |  |
| 2 | `5U6SPQLF_E082` | `contains` | 01-Object Domain | rotating machinery(Industrial) |  | 02-Object Type | gearbox |  |
| 3 | `5U6SPQLF_E083` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing |  |
| 4 | `5U6SPQLF_E084` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | gearbox |  |
| 5 | `5U6SPQLF_E085` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | bearing |  |
| 6 | `5U6SPQLF_E086` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | gearbox |  |
| 7 | `5U6SPQLF_E087` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | variable working conditions(Multiple Conditions) |  |
| 8 | `5U6SPQLF_E088` | `contains` | 02-Object Type | gearbox |  | 03-Operating Conditions | variable working conditions(Multiple Conditions) |  |
| 9 | `5U6SPQLF_E089` | `contains` | 05-Fault Mode | pitting |  | 07-Compound Fault | complicated faults(Compound Fault Within Same Structure) |  |
| 10 | `5U6SPQLF_E090` | `contains` | 05-Fault Mode | broken-tooth |  | 07-Compound Fault | complicated faults(Compound Fault Within Same Structure) |  |
| 11 | `5U6SPQLF_E091` | `contains` | 05-Fault Mode | worn |  | 07-Compound Fault | complicated faults(Compound Fault Within Same Structure) |  |
| 12 | `5U6SPQLF_E092` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | bearing |  |
| 13 | `5U6SPQLF_E093` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | gearbox |  |
| 14 | `5U6SPQLF_E094` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | pitting |  |
| 15 | `5U6SPQLF_E095` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | broken-tooth |  |
| 16 | `5U6SPQLF_E096` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | worn |  |
| 17 | `5U6SPQLF_E097` | `can be used for` | 10-Dataset | bearing dataset from Case Western Reserve University (CWRU) |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `5U6SPQLF_E098` | `can be used for` | 10-Dataset | gearbox vibration signal dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `5U6SPQLF_E099` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | pitting |  |
| 20 | `5U6SPQLF_E100` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | broken-tooth |  |
| 21 | `5U6SPQLF_E101` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | worn |  |
| 22 | `5U6SPQLF_E102` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | pitting |  |
| 23 | `5U6SPQLF_E103` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | broken-tooth |  |
| 24 | `5U6SPQLF_E104` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | worn |  |
| 25 | `5U6SPQLF_E105` | `contains` | 05-Fault Mode | pitting |  | 06-Fault Severity | 10 health conditions(Multiple Severities) |  |
| 26 | `5U6SPQLF_E106` | `contains` | 05-Fault Mode | broken-tooth |  | 06-Fault Severity | 10 health conditions(Multiple Severities) |  |
| 27 | `5U6SPQLF_E107` | `contains` | 05-Fault Mode | worn |  | 06-Fault Severity | 10 health conditions(Multiple Severities) |  |
| 28 | `5U6SPQLF_E108` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 29 | `5U6SPQLF_E109` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 30 | `5U6SPQLF_E110` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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
