# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：ZWXHI3E5
- **Paper Title**：Comparative Study of Time-Frequency Decomposition Techniques for Fault Detection in Induction Motors Using Vibration Analysis during Startup Transient
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `ZWXHI3E5`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "ZWXHI3E5_E041", "edge_description": "industry / manufacturing contains induction motor"},
    {"edge_id": "ZWXHI3E5_E042", "edge_description": "industry / manufacturing contains bearing"},
    {"edge_id": "ZWXHI3E5_E043", "edge_description": "induction motor contains rotor"},
    {"edge_id": "ZWXHI3E5_E044", "edge_description": "induction motor contains bearing"},
    {"edge_id": "ZWXHI3E5_E045", "edge_description": "induction motor contains pulley"},
    {"edge_id": "ZWXHI3E5_E046", "edge_description": "bearing contains rotor"},
    {"edge_id": "ZWXHI3E5_E047", "edge_description": "bearing contains bearing"},
    {"edge_id": "ZWXHI3E5_E048", "edge_description": "bearing contains pulley"},
    {"edge_id": "ZWXHI3E5_E049", "edge_description": "induction motor contains startup transient"},
    {"edge_id": "ZWXHI3E5_E050", "edge_description": "bearing contains startup transient"},
    {"edge_id": "ZWXHI3E5_E051", "edge_description": "broken rotor bar contains No Compound Fault"},
    {"edge_id": "ZWXHI3E5_E052", "edge_description": "bearing defect contains No Compound Fault"},
    {"edge_id": "ZWXHI3E5_E053", "edge_description": "unbalance contains No Compound Fault"},
    {"edge_id": "ZWXHI3E5_E054", "edge_description": "triaxial accelerometer (model LIS3L02AS4) is collected on rotor"},
    {"edge_id": "ZWXHI3E5_E055", "edge_description": "triaxial accelerometer (model LIS3L02AS4) is collected on bearing"},
    {"edge_id": "ZWXHI3E5_E056", "edge_description": "triaxial accelerometer (model LIS3L02AS4) is collected on pulley"},
    {"edge_id": "ZWXHI3E5_E057", "edge_description": "triaxial accelerometer (model LIS3L02AS4) can obviously reflect broken rotor bar"},
    {"edge_id": "ZWXHI3E5_E058", "edge_description": "triaxial accelerometer (model LIS3L02AS4) can obviously reflect bearing defect"},
    {"edge_id": "ZWXHI3E5_E059", "edge_description": "triaxial accelerometer (model LIS3L02AS4) can obviously reflect unbalance"},
    {"edge_id": "ZWXHI3E5_E061", "edge_description": "rotor has_fault_mode broken rotor bar"},
    {"edge_id": "ZWXHI3E5_E062", "edge_description": "rotor has_fault_mode bearing defect"},
    {"edge_id": "ZWXHI3E5_E063", "edge_description": "rotor has_fault_mode unbalance"},
    {"edge_id": "ZWXHI3E5_E064", "edge_description": "bearing has_fault_mode broken rotor bar"},
    {"edge_id": "ZWXHI3E5_E065", "edge_description": "bearing has_fault_mode bearing defect"},
    {"edge_id": "ZWXHI3E5_E066", "edge_description": "bearing has_fault_mode unbalance"},
    {"edge_id": "ZWXHI3E5_E067", "edge_description": "pulley has_fault_mode broken rotor bar"},
    {"edge_id": "ZWXHI3E5_E068", "edge_description": "pulley has_fault_mode bearing defect"},
    {"edge_id": "ZWXHI3E5_E069", "edge_description": "pulley has_fault_mode unbalance"},
    {"edge_id": "ZWXHI3E5_E070", "edge_description": "broken rotor bar contains one broken rotor bar, two broken bars"},
    {"edge_id": "ZWXHI3E5_E071", "edge_description": "bearing defect contains one broken rotor bar, two broken bars"}
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
| 1 | `ZWXHI3E5_E041` | `contains` | 01-Object Domain | industry / manufacturing(Industrial) |  | 02-Object Type | induction motor |  |
| 2 | `ZWXHI3E5_E042` | `contains` | 01-Object Domain | industry / manufacturing(Industrial) |  | 02-Object Type | bearing |  |
| 3 | `ZWXHI3E5_E043` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | rotor |  |
| 4 | `ZWXHI3E5_E044` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | bearing |  |
| 5 | `ZWXHI3E5_E045` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | pulley |  |
| 6 | `ZWXHI3E5_E046` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | rotor |  |
| 7 | `ZWXHI3E5_E047` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing |  |
| 8 | `ZWXHI3E5_E048` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | pulley |  |
| 9 | `ZWXHI3E5_E049` | `contains` | 02-Object Type | induction motor |  | 03-Operating Conditions | startup transient(Variable Conditions) |  |
| 10 | `ZWXHI3E5_E050` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | startup transient(Variable Conditions) |  |
| 11 | `ZWXHI3E5_E051` | `contains` | 05-Fault Mode | broken rotor bar |  | 07-Compound Fault | No Compound Fault |  |
| 12 | `ZWXHI3E5_E052` | `contains` | 05-Fault Mode | bearing defect |  | 07-Compound Fault | No Compound Fault |  |
| 13 | `ZWXHI3E5_E053` | `contains` | 05-Fault Mode | unbalance |  | 07-Compound Fault | No Compound Fault |  |
| 14 | `ZWXHI3E5_E054` | `is collected on` | 11-Sensor Information | triaxial accelerometer (model LIS3L02AS4) |  | 04-Fault Location | rotor |  |
| 15 | `ZWXHI3E5_E055` | `is collected on` | 11-Sensor Information | triaxial accelerometer (model LIS3L02AS4) |  | 04-Fault Location | bearing |  |
| 16 | `ZWXHI3E5_E056` | `is collected on` | 11-Sensor Information | triaxial accelerometer (model LIS3L02AS4) |  | 04-Fault Location | pulley |  |
| 17 | `ZWXHI3E5_E057` | `can obviously reflect` | 11-Sensor Information | triaxial accelerometer (model LIS3L02AS4) |  | 05-Fault Mode | broken rotor bar |  |
| 18 | `ZWXHI3E5_E058` | `can obviously reflect` | 11-Sensor Information | triaxial accelerometer (model LIS3L02AS4) |  | 05-Fault Mode | bearing defect |  |
| 19 | `ZWXHI3E5_E059` | `can obviously reflect` | 11-Sensor Information | triaxial accelerometer (model LIS3L02AS4) |  | 05-Fault Mode | unbalance |  |
| 20 | `ZWXHI3E5_E061` | `has_fault_mode` | 04-Fault Location | rotor |  | 05-Fault Mode | broken rotor bar |  |
| 21 | `ZWXHI3E5_E062` | `has_fault_mode` | 04-Fault Location | rotor |  | 05-Fault Mode | bearing defect |  |
| 22 | `ZWXHI3E5_E063` | `has_fault_mode` | 04-Fault Location | rotor |  | 05-Fault Mode | unbalance |  |
| 23 | `ZWXHI3E5_E064` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | broken rotor bar |  |
| 24 | `ZWXHI3E5_E065` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | bearing defect |  |
| 25 | `ZWXHI3E5_E066` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | unbalance |  |
| 26 | `ZWXHI3E5_E067` | `has_fault_mode` | 04-Fault Location | pulley |  | 05-Fault Mode | broken rotor bar |  |
| 27 | `ZWXHI3E5_E068` | `has_fault_mode` | 04-Fault Location | pulley |  | 05-Fault Mode | bearing defect |  |
| 28 | `ZWXHI3E5_E069` | `has_fault_mode` | 04-Fault Location | pulley |  | 05-Fault Mode | unbalance |  |
| 29 | `ZWXHI3E5_E070` | `contains` | 05-Fault Mode | broken rotor bar |  | 06-Fault Severity | one broken rotor bar, two broken bars(Multiple Severities) |  |
| 30 | `ZWXHI3E5_E071` | `contains` | 05-Fault Mode | bearing defect |  | 06-Fault Severity | one broken rotor bar, two broken bars(Multiple Severities) |  |

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
