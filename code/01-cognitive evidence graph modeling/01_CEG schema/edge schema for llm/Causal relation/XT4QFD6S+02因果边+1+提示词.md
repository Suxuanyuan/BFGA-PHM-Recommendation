# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：XT4QFD6S
- **Paper Title**：An Empirical Demodulation for Electrical Fault Detection in Induction Motors
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `XT4QFD6S`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "XT4QFD6S_E062", "edge_description": "three-phase induction motor contains stator winding"},
    {"edge_id": "XT4QFD6S_E063", "edge_description": "three-phase induction motor contains rotor bar"},
    {"edge_id": "XT4QFD6S_E065", "edge_description": "interturn short circuit contains No Compound Fault"},
    {"edge_id": "XT4QFD6S_E066", "edge_description": "unbalanced phase contains No Compound Fault"},
    {"edge_id": "XT4QFD6S_E067", "edge_description": "broken rotor bar contains No Compound Fault"},
    {"edge_id": "XT4QFD6S_E068", "edge_description": "DeltaTron accelerometer, type 4517 is collected on stator winding"},
    {"edge_id": "XT4QFD6S_E069", "edge_description": "DeltaTron accelerometer, type 4517 is collected on rotor bar"},
    {"edge_id": "XT4QFD6S_E070", "edge_description": "magnetic flux sensor is collected on stator winding"},
    {"edge_id": "XT4QFD6S_E071", "edge_description": "magnetic flux sensor is collected on rotor bar"},
    {"edge_id": "XT4QFD6S_E072", "edge_description": "DeltaTron accelerometer, type 4517 can obviously reflect interturn short circuit"},
    {"edge_id": "XT4QFD6S_E073", "edge_description": "DeltaTron accelerometer, type 4517 can obviously reflect unbalanced phase"},
    {"edge_id": "XT4QFD6S_E074", "edge_description": "DeltaTron accelerometer, type 4517 can obviously reflect broken rotor bar"},
    {"edge_id": "XT4QFD6S_E075", "edge_description": "magnetic flux sensor can obviously reflect interturn short circuit"},
    {"edge_id": "XT4QFD6S_E076", "edge_description": "magnetic flux sensor can obviously reflect unbalanced phase"},
    {"edge_id": "XT4QFD6S_E077", "edge_description": "magnetic flux sensor can obviously reflect broken rotor bar"},
    {"edge_id": "XT4QFD6S_E078", "edge_description": "numerical signals from three-phase induction motor simulations can be used for Electrical Fault Detection"},
    {"edge_id": "XT4QFD6S_E079", "edge_description": "experimental bench dataset of interturn short circuits and unbalanced voltage supply faults can be used for Electrical Fault Detection"},
    {"edge_id": "XT4QFD6S_E080", "edge_description": "stator winding has_fault_mode interturn short circuit"},
    {"edge_id": "XT4QFD6S_E081", "edge_description": "stator winding has_fault_mode unbalanced phase"},
    {"edge_id": "XT4QFD6S_E082", "edge_description": "stator winding has_fault_mode broken rotor bar"},
    {"edge_id": "XT4QFD6S_E083", "edge_description": "rotor bar has_fault_mode interturn short circuit"},
    {"edge_id": "XT4QFD6S_E084", "edge_description": "rotor bar has_fault_mode unbalanced phase"},
    {"edge_id": "XT4QFD6S_E085", "edge_description": "rotor bar has_fault_mode broken rotor bar"},
    {"edge_id": "XT4QFD6S_E086", "edge_description": "interturn short circuit contains two-, four-, and eight-turn short circuits"},
    {"edge_id": "XT4QFD6S_E087", "edge_description": "unbalanced phase contains two-, four-, and eight-turn short circuits"},
    {"edge_id": "XT4QFD6S_E088", "edge_description": "broken rotor bar contains two-, four-, and eight-turn short circuits"},
    {"edge_id": "XT4QFD6S_E090", "edge_description": "stator winding contains_phm_task Electrical Fault Detection"},
    {"edge_id": "XT4QFD6S_E091", "edge_description": "rotor bar contains_phm_task Electrical Fault Detection"},
    {"edge_id": "XT4QFD6S_E092", "edge_description": "interturn short circuit contains_phm_task Electrical Fault Detection"},
    {"edge_id": "XT4QFD6S_E093", "edge_description": "unbalanced phase contains_phm_task Electrical Fault Detection"}
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
| 1 | `XT4QFD6S_E062` | `contains` | 02-Object Type | three-phase induction motor |  | 04-Fault Location | stator winding |  |
| 2 | `XT4QFD6S_E063` | `contains` | 02-Object Type | three-phase induction motor |  | 04-Fault Location | rotor bar |  |
| 3 | `XT4QFD6S_E065` | `contains` | 05-Fault Mode | interturn short circuit |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `XT4QFD6S_E066` | `contains` | 05-Fault Mode | unbalanced phase |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `XT4QFD6S_E067` | `contains` | 05-Fault Mode | broken rotor bar |  | 07-Compound Fault | No Compound Fault |  |
| 6 | `XT4QFD6S_E068` | `is collected on` | 11-Sensor Information | DeltaTron accelerometer, type 4517 |  | 04-Fault Location | stator winding |  |
| 7 | `XT4QFD6S_E069` | `is collected on` | 11-Sensor Information | DeltaTron accelerometer, type 4517 |  | 04-Fault Location | rotor bar |  |
| 8 | `XT4QFD6S_E070` | `is collected on` | 11-Sensor Information | magnetic flux sensor |  | 04-Fault Location | stator winding |  |
| 9 | `XT4QFD6S_E071` | `is collected on` | 11-Sensor Information | magnetic flux sensor |  | 04-Fault Location | rotor bar |  |
| 10 | `XT4QFD6S_E072` | `can obviously reflect` | 11-Sensor Information | DeltaTron accelerometer, type 4517 |  | 05-Fault Mode | interturn short circuit |  |
| 11 | `XT4QFD6S_E073` | `can obviously reflect` | 11-Sensor Information | DeltaTron accelerometer, type 4517 |  | 05-Fault Mode | unbalanced phase |  |
| 12 | `XT4QFD6S_E074` | `can obviously reflect` | 11-Sensor Information | DeltaTron accelerometer, type 4517 |  | 05-Fault Mode | broken rotor bar |  |
| 13 | `XT4QFD6S_E075` | `can obviously reflect` | 11-Sensor Information | magnetic flux sensor |  | 05-Fault Mode | interturn short circuit |  |
| 14 | `XT4QFD6S_E076` | `can obviously reflect` | 11-Sensor Information | magnetic flux sensor |  | 05-Fault Mode | unbalanced phase |  |
| 15 | `XT4QFD6S_E077` | `can obviously reflect` | 11-Sensor Information | magnetic flux sensor |  | 05-Fault Mode | broken rotor bar |  |
| 16 | `XT4QFD6S_E078` | `can be used for` | 10-Dataset | numerical signals from three-phase induction motor simulations |  | 08-PHM Task | Electrical Fault Detection(Detection Task) |  |
| 17 | `XT4QFD6S_E079` | `can be used for` | 10-Dataset | experimental bench dataset of interturn short circuits and unbalanced voltage supply faults |  | 08-PHM Task | Electrical Fault Detection(Detection Task) |  |
| 18 | `XT4QFD6S_E080` | `has_fault_mode` | 04-Fault Location | stator winding |  | 05-Fault Mode | interturn short circuit |  |
| 19 | `XT4QFD6S_E081` | `has_fault_mode` | 04-Fault Location | stator winding |  | 05-Fault Mode | unbalanced phase |  |
| 20 | `XT4QFD6S_E082` | `has_fault_mode` | 04-Fault Location | stator winding |  | 05-Fault Mode | broken rotor bar |  |
| 21 | `XT4QFD6S_E083` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | interturn short circuit |  |
| 22 | `XT4QFD6S_E084` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | unbalanced phase |  |
| 23 | `XT4QFD6S_E085` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | broken rotor bar |  |
| 24 | `XT4QFD6S_E086` | `contains` | 05-Fault Mode | interturn short circuit |  | 06-Fault Severity | two-, four-, and eight-turn short circuits(Multiple Severities) |  |
| 25 | `XT4QFD6S_E087` | `contains` | 05-Fault Mode | unbalanced phase |  | 06-Fault Severity | two-, four-, and eight-turn short circuits(Multiple Severities) |  |
| 26 | `XT4QFD6S_E088` | `contains` | 05-Fault Mode | broken rotor bar |  | 06-Fault Severity | two-, four-, and eight-turn short circuits(Multiple Severities) |  |
| 27 | `XT4QFD6S_E090` | `contains_phm_task` | 04-Fault Location | stator winding |  | 08-PHM Task | Electrical Fault Detection(Detection Task) |  |
| 28 | `XT4QFD6S_E091` | `contains_phm_task` | 04-Fault Location | rotor bar |  | 08-PHM Task | Electrical Fault Detection(Detection Task) |  |
| 29 | `XT4QFD6S_E092` | `contains_phm_task` | 05-Fault Mode | interturn short circuit |  | 08-PHM Task | Electrical Fault Detection(Detection Task) |  |
| 30 | `XT4QFD6S_E093` | `contains_phm_task` | 05-Fault Mode | unbalanced phase |  | 08-PHM Task | Electrical Fault Detection(Detection Task) |  |

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
