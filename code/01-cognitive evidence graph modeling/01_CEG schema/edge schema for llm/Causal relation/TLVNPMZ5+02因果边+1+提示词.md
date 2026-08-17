# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TLVNPMZ5
- **Paper Title**：Intelligent Bearing Fault Diagnosis Method Combining Compressed Data Acquisition and Deep Learning
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `TLVNPMZ5`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TLVNPMZ5_E109", "edge_description": "wind turbine platform and bearings contains wind turbine"},
    {"edge_id": "TLVNPMZ5_E110", "edge_description": "wind turbine platform and bearings contains bearing"},
    {"edge_id": "TLVNPMZ5_E111", "edge_description": "wind turbine contains bearing"},
    {"edge_id": "TLVNPMZ5_E112", "edge_description": "wind turbine contains bearing pedestal"},
    {"edge_id": "TLVNPMZ5_E113", "edge_description": "wind turbine contains rotor / shaft / coupling"},
    {"edge_id": "TLVNPMZ5_E114", "edge_description": "wind turbine contains blade"},
    {"edge_id": "TLVNPMZ5_E115", "edge_description": "wind turbine contains yaw mechanism"},
    {"edge_id": "TLVNPMZ5_E116", "edge_description": "bearing contains bearing"},
    {"edge_id": "TLVNPMZ5_E117", "edge_description": "bearing contains bearing pedestal"},
    {"edge_id": "TLVNPMZ5_E118", "edge_description": "bearing contains rotor / shaft / coupling"},
    {"edge_id": "TLVNPMZ5_E119", "edge_description": "bearing contains blade"},
    {"edge_id": "TLVNPMZ5_E120", "edge_description": "bearing contains yaw mechanism"},
    {"edge_id": "TLVNPMZ5_E121", "edge_description": "wind turbine contains diverse working conditions"},
    {"edge_id": "TLVNPMZ5_E122", "edge_description": "bearing contains diverse working conditions"},
    {"edge_id": "TLVNPMZ5_E123", "edge_description": "pitting contains No Compound Fault"},
    {"edge_id": "TLVNPMZ5_E124", "edge_description": "indentations contains No Compound Fault"},
    {"edge_id": "TLVNPMZ5_E125", "edge_description": "pedestal loosening contains No Compound Fault"},
    {"edge_id": "TLVNPMZ5_E126", "edge_description": "misalignment contains No Compound Fault"},
    {"edge_id": "TLVNPMZ5_E127", "edge_description": "variation in airfoil of blades contains No Compound Fault"},
    {"edge_id": "TLVNPMZ5_E128", "edge_description": "yaw fault contains No Compound Fault"},
    {"edge_id": "TLVNPMZ5_E129", "edge_description": "acceleration sensor is collected on bearing"},
    {"edge_id": "TLVNPMZ5_E130", "edge_description": "acceleration sensor is collected on bearing pedestal"},
    {"edge_id": "TLVNPMZ5_E131", "edge_description": "acceleration sensor is collected on rotor / shaft / coupling"},
    {"edge_id": "TLVNPMZ5_E132", "edge_description": "acceleration sensor is collected on blade"},
    {"edge_id": "TLVNPMZ5_E133", "edge_description": "acceleration sensor is collected on yaw mechanism"},
    {"edge_id": "TLVNPMZ5_E134", "edge_description": "acceleration sensor can obviously reflect pitting"},
    {"edge_id": "TLVNPMZ5_E135", "edge_description": "acceleration sensor can obviously reflect indentations"},
    {"edge_id": "TLVNPMZ5_E136", "edge_description": "acceleration sensor can obviously reflect pedestal loosening"},
    {"edge_id": "TLVNPMZ5_E137", "edge_description": "acceleration sensor can obviously reflect misalignment"},
    {"edge_id": "TLVNPMZ5_E138", "edge_description": "acceleration sensor can obviously reflect variation in airfoil of blades"}
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
| 1 | `TLVNPMZ5_E109` | `contains` | 01-Object Domain | wind turbine platform and bearings(Industrial) |  | 02-Object Type | wind turbine |  |
| 2 | `TLVNPMZ5_E110` | `contains` | 01-Object Domain | wind turbine platform and bearings(Industrial) |  | 02-Object Type | bearing |  |
| 3 | `TLVNPMZ5_E111` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | bearing |  |
| 4 | `TLVNPMZ5_E112` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | bearing pedestal |  |
| 5 | `TLVNPMZ5_E113` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | rotor / shaft / coupling |  |
| 6 | `TLVNPMZ5_E114` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | blade |  |
| 7 | `TLVNPMZ5_E115` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | yaw mechanism |  |
| 8 | `TLVNPMZ5_E116` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing |  |
| 9 | `TLVNPMZ5_E117` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing pedestal |  |
| 10 | `TLVNPMZ5_E118` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | rotor / shaft / coupling |  |
| 11 | `TLVNPMZ5_E119` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | blade |  |
| 12 | `TLVNPMZ5_E120` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | yaw mechanism |  |
| 13 | `TLVNPMZ5_E121` | `contains` | 02-Object Type | wind turbine |  | 03-Operating Conditions | diverse working conditions(Multiple Conditions) |  |
| 14 | `TLVNPMZ5_E122` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | diverse working conditions(Multiple Conditions) |  |
| 15 | `TLVNPMZ5_E123` | `contains` | 05-Fault Mode | pitting |  | 07-Compound Fault | No Compound Fault |  |
| 16 | `TLVNPMZ5_E124` | `contains` | 05-Fault Mode | indentations |  | 07-Compound Fault | No Compound Fault |  |
| 17 | `TLVNPMZ5_E125` | `contains` | 05-Fault Mode | pedestal loosening |  | 07-Compound Fault | No Compound Fault |  |
| 18 | `TLVNPMZ5_E126` | `contains` | 05-Fault Mode | misalignment |  | 07-Compound Fault | No Compound Fault |  |
| 19 | `TLVNPMZ5_E127` | `contains` | 05-Fault Mode | variation in airfoil of blades |  | 07-Compound Fault | No Compound Fault |  |
| 20 | `TLVNPMZ5_E128` | `contains` | 05-Fault Mode | yaw fault |  | 07-Compound Fault | No Compound Fault |  |
| 21 | `TLVNPMZ5_E129` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | bearing |  |
| 22 | `TLVNPMZ5_E130` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | bearing pedestal |  |
| 23 | `TLVNPMZ5_E131` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | rotor / shaft / coupling |  |
| 24 | `TLVNPMZ5_E132` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | blade |  |
| 25 | `TLVNPMZ5_E133` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | yaw mechanism |  |
| 26 | `TLVNPMZ5_E134` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | pitting |  |
| 27 | `TLVNPMZ5_E135` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | indentations |  |
| 28 | `TLVNPMZ5_E136` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | pedestal loosening |  |
| 29 | `TLVNPMZ5_E137` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | misalignment |  |
| 30 | `TLVNPMZ5_E138` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | variation in airfoil of blades |  |

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
