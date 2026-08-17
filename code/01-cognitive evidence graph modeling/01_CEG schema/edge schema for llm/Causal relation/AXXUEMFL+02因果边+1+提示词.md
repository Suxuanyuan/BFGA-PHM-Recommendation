# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AXXUEMFL
- **Paper Title**：Fault Diagnosis of Rotating Machinery Based on Stochastic Resonance with a Bistable Confining Potential
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AXXUEMFL`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AXXUEMFL_E064", "edge_description": "rotating machinery contains rolling bearing"},
    {"edge_id": "AXXUEMFL_E065", "edge_description": "rotating machinery contains planetary gearbox"},
    {"edge_id": "AXXUEMFL_E066", "edge_description": "rolling bearing contains inner race of bearing"},
    {"edge_id": "AXXUEMFL_E067", "edge_description": "rolling bearing contains sun gear"},
    {"edge_id": "AXXUEMFL_E068", "edge_description": "planetary gearbox contains inner race of bearing"},
    {"edge_id": "AXXUEMFL_E069", "edge_description": "planetary gearbox contains sun gear"},
    {"edge_id": "AXXUEMFL_E070", "edge_description": "rolling bearing contains motor speed 600r/min, brake set voltage 1.2 V and current 1.1 A"},
    {"edge_id": "AXXUEMFL_E071", "edge_description": "planetary gearbox contains motor speed 600r/min, brake set voltage 1.2 V and current 1.1 A"},
    {"edge_id": "AXXUEMFL_E072", "edge_description": "slight damage contains No Compound Fault"},
    {"edge_id": "AXXUEMFL_E073", "edge_description": "missing tooth contains No Compound Fault"},
    {"edge_id": "AXXUEMFL_E074", "edge_description": "broken tooth contains No Compound Fault"},
    {"edge_id": "AXXUEMFL_E075", "edge_description": "vibration sensor is collected on inner race of bearing"},
    {"edge_id": "AXXUEMFL_E076", "edge_description": "vibration sensor is collected on sun gear"},
    {"edge_id": "AXXUEMFL_E077", "edge_description": "vibration sensor can obviously reflect slight damage"},
    {"edge_id": "AXXUEMFL_E078", "edge_description": "vibration sensor can obviously reflect missing tooth"},
    {"edge_id": "AXXUEMFL_E079", "edge_description": "vibration sensor can obviously reflect broken tooth"},
    {"edge_id": "AXXUEMFL_E080", "edge_description": "Simulated bearing fault signal can be used for fault diagnosis"},
    {"edge_id": "AXXUEMFL_E081", "edge_description": "ER-10k bearing vibration experimental data can be used for fault diagnosis"},
    {"edge_id": "AXXUEMFL_E082", "edge_description": "Planetary gearbox experimental data can be used for fault diagnosis"},
    {"edge_id": "AXXUEMFL_E083", "edge_description": "inner race of bearing has_fault_mode slight damage"},
    {"edge_id": "AXXUEMFL_E084", "edge_description": "inner race of bearing has_fault_mode missing tooth"},
    {"edge_id": "AXXUEMFL_E085", "edge_description": "inner race of bearing has_fault_mode broken tooth"},
    {"edge_id": "AXXUEMFL_E086", "edge_description": "sun gear has_fault_mode slight damage"},
    {"edge_id": "AXXUEMFL_E087", "edge_description": "sun gear has_fault_mode missing tooth"},
    {"edge_id": "AXXUEMFL_E088", "edge_description": "sun gear has_fault_mode broken tooth"},
    {"edge_id": "AXXUEMFL_E089", "edge_description": "slight damage contains Single Severity"},
    {"edge_id": "AXXUEMFL_E090", "edge_description": "missing tooth contains Single Severity"},
    {"edge_id": "AXXUEMFL_E091", "edge_description": "broken tooth contains Single Severity"},
    {"edge_id": "AXXUEMFL_E092", "edge_description": "rolling bearing contains_phm_task fault diagnosis"},
    {"edge_id": "AXXUEMFL_E093", "edge_description": "planetary gearbox contains_phm_task fault diagnosis"}
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
| 1 | `AXXUEMFL_E064` | `contains` | 01-Object Domain | rotating machinery(Industrial) |  | 02-Object Type | rolling bearing |  |
| 2 | `AXXUEMFL_E065` | `contains` | 01-Object Domain | rotating machinery(Industrial) |  | 02-Object Type | planetary gearbox |  |
| 3 | `AXXUEMFL_E066` | `contains` | 02-Object Type | rolling bearing |  | 04-Fault Location | inner race of bearing |  |
| 4 | `AXXUEMFL_E067` | `contains` | 02-Object Type | rolling bearing |  | 04-Fault Location | sun gear |  |
| 5 | `AXXUEMFL_E068` | `contains` | 02-Object Type | planetary gearbox |  | 04-Fault Location | inner race of bearing |  |
| 6 | `AXXUEMFL_E069` | `contains` | 02-Object Type | planetary gearbox |  | 04-Fault Location | sun gear |  |
| 7 | `AXXUEMFL_E070` | `contains` | 02-Object Type | rolling bearing |  | 03-Operating Conditions | motor speed 600r/min, brake set voltage 1.2 V and current 1.1 A(Single Condition) |  |
| 8 | `AXXUEMFL_E071` | `contains` | 02-Object Type | planetary gearbox |  | 03-Operating Conditions | motor speed 600r/min, brake set voltage 1.2 V and current 1.1 A(Single Condition) |  |
| 9 | `AXXUEMFL_E072` | `contains` | 05-Fault Mode | slight damage |  | 07-Compound Fault | No Compound Fault |  |
| 10 | `AXXUEMFL_E073` | `contains` | 05-Fault Mode | missing tooth |  | 07-Compound Fault | No Compound Fault |  |
| 11 | `AXXUEMFL_E074` | `contains` | 05-Fault Mode | broken tooth |  | 07-Compound Fault | No Compound Fault |  |
| 12 | `AXXUEMFL_E075` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | inner race of bearing |  |
| 13 | `AXXUEMFL_E076` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | sun gear |  |
| 14 | `AXXUEMFL_E077` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | slight damage |  |
| 15 | `AXXUEMFL_E078` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | missing tooth |  |
| 16 | `AXXUEMFL_E079` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | broken tooth |  |
| 17 | `AXXUEMFL_E080` | `can be used for` | 10-Dataset | Simulated bearing fault signal |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `AXXUEMFL_E081` | `can be used for` | 10-Dataset | ER-10k bearing vibration experimental data |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `AXXUEMFL_E082` | `can be used for` | 10-Dataset | Planetary gearbox experimental data |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `AXXUEMFL_E083` | `has_fault_mode` | 04-Fault Location | inner race of bearing |  | 05-Fault Mode | slight damage |  |
| 21 | `AXXUEMFL_E084` | `has_fault_mode` | 04-Fault Location | inner race of bearing |  | 05-Fault Mode | missing tooth |  |
| 22 | `AXXUEMFL_E085` | `has_fault_mode` | 04-Fault Location | inner race of bearing |  | 05-Fault Mode | broken tooth |  |
| 23 | `AXXUEMFL_E086` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | slight damage |  |
| 24 | `AXXUEMFL_E087` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | missing tooth |  |
| 25 | `AXXUEMFL_E088` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | broken tooth |  |
| 26 | `AXXUEMFL_E089` | `contains` | 05-Fault Mode | slight damage |  | 06-Fault Severity | Single Severity |  |
| 27 | `AXXUEMFL_E090` | `contains` | 05-Fault Mode | missing tooth |  | 06-Fault Severity | Single Severity |  |
| 28 | `AXXUEMFL_E091` | `contains` | 05-Fault Mode | broken tooth |  | 06-Fault Severity | Single Severity |  |
| 29 | `AXXUEMFL_E092` | `contains_phm_task` | 02-Object Type | rolling bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 30 | `AXXUEMFL_E093` | `contains_phm_task` | 02-Object Type | planetary gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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
