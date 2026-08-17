# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：UMI43QJH
- **Paper Title**：Intelligent fault diagnosis of planetary gearbox based on adaptive normalized CNN under complex variable working conditions and data imbalance
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `UMI43QJH`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "UMI43QJH_E135", "edge_description": "laser pulse tachometer can obviously reflect tooth root crack"},
    {"edge_id": "UMI43QJH_E136", "edge_description": "laser pulse tachometer can obviously reflect broken tooth"},
    {"edge_id": "UMI43QJH_E137", "edge_description": "laser pulse tachometer can obviously reflect missing tooth"},
    {"edge_id": "UMI43QJH_E138", "edge_description": "laser pulse tachometer can obviously reflect inner ring fault"},
    {"edge_id": "UMI43QJH_E139", "edge_description": "laser pulse tachometer can obviously reflect outer ring fault"},
    {"edge_id": "UMI43QJH_E140", "edge_description": "generic planetary gearbox for industrial applications can be used for intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E141", "edge_description": "drivetrain dynamic simulator (DDS) test rig can be used for intelligent fault diagnosis"},
    {"edge_id": "UMI43QJH_E142", "edge_description": "sun gear has_fault_mode tooth root crack"},
    {"edge_id": "UMI43QJH_E143", "edge_description": "sun gear has_fault_mode broken tooth"},
    {"edge_id": "UMI43QJH_E144", "edge_description": "sun gear has_fault_mode missing tooth"},
    {"edge_id": "UMI43QJH_E145", "edge_description": "sun gear has_fault_mode inner ring fault"},
    {"edge_id": "UMI43QJH_E146", "edge_description": "sun gear has_fault_mode outer ring fault"},
    {"edge_id": "UMI43QJH_E147", "edge_description": "planetary gear has_fault_mode tooth root crack"},
    {"edge_id": "UMI43QJH_E148", "edge_description": "planetary gear has_fault_mode broken tooth"},
    {"edge_id": "UMI43QJH_E149", "edge_description": "planetary gear has_fault_mode missing tooth"},
    {"edge_id": "UMI43QJH_E150", "edge_description": "planetary gear has_fault_mode inner ring fault"},
    {"edge_id": "UMI43QJH_E151", "edge_description": "planetary gear has_fault_mode outer ring fault"},
    {"edge_id": "UMI43QJH_E152", "edge_description": "ring gear has_fault_mode tooth root crack"},
    {"edge_id": "UMI43QJH_E153", "edge_description": "ring gear has_fault_mode broken tooth"},
    {"edge_id": "UMI43QJH_E154", "edge_description": "ring gear has_fault_mode missing tooth"},
    {"edge_id": "UMI43QJH_E155", "edge_description": "ring gear has_fault_mode inner ring fault"},
    {"edge_id": "UMI43QJH_E156", "edge_description": "ring gear has_fault_mode outer ring fault"},
    {"edge_id": "UMI43QJH_E157", "edge_description": "planetary bearing has_fault_mode tooth root crack"},
    {"edge_id": "UMI43QJH_E158", "edge_description": "planetary bearing has_fault_mode broken tooth"},
    {"edge_id": "UMI43QJH_E159", "edge_description": "planetary bearing has_fault_mode missing tooth"},
    {"edge_id": "UMI43QJH_E160", "edge_description": "planetary bearing has_fault_mode inner ring fault"},
    {"edge_id": "UMI43QJH_E161", "edge_description": "planetary bearing has_fault_mode outer ring fault"},
    {"edge_id": "UMI43QJH_E162", "edge_description": "tooth root crack contains Single Severity"},
    {"edge_id": "UMI43QJH_E163", "edge_description": "broken tooth contains Single Severity"},
    {"edge_id": "UMI43QJH_E164", "edge_description": "missing tooth contains Single Severity"}
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
| 1 | `UMI43QJH_E135` | `can obviously reflect` | 11-Sensor Information | laser pulse tachometer |  | 05-Fault Mode | tooth root crack |  |
| 2 | `UMI43QJH_E136` | `can obviously reflect` | 11-Sensor Information | laser pulse tachometer |  | 05-Fault Mode | broken tooth |  |
| 3 | `UMI43QJH_E137` | `can obviously reflect` | 11-Sensor Information | laser pulse tachometer |  | 05-Fault Mode | missing tooth |  |
| 4 | `UMI43QJH_E138` | `can obviously reflect` | 11-Sensor Information | laser pulse tachometer |  | 05-Fault Mode | inner ring fault |  |
| 5 | `UMI43QJH_E139` | `can obviously reflect` | 11-Sensor Information | laser pulse tachometer |  | 05-Fault Mode | outer ring fault |  |
| 6 | `UMI43QJH_E140` | `can be used for` | 10-Dataset | generic planetary gearbox for industrial applications |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 7 | `UMI43QJH_E141` | `can be used for` | 10-Dataset | drivetrain dynamic simulator (DDS) test rig |  | 08-PHM Task | intelligent fault diagnosis(Diagnosis Task) |  |
| 8 | `UMI43QJH_E142` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | tooth root crack |  |
| 9 | `UMI43QJH_E143` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | broken tooth |  |
| 10 | `UMI43QJH_E144` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | missing tooth |  |
| 11 | `UMI43QJH_E145` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | inner ring fault |  |
| 12 | `UMI43QJH_E146` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | outer ring fault |  |
| 13 | `UMI43QJH_E147` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | tooth root crack |  |
| 14 | `UMI43QJH_E148` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | broken tooth |  |
| 15 | `UMI43QJH_E149` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | missing tooth |  |
| 16 | `UMI43QJH_E150` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | inner ring fault |  |
| 17 | `UMI43QJH_E151` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | outer ring fault |  |
| 18 | `UMI43QJH_E152` | `has_fault_mode` | 04-Fault Location | ring gear |  | 05-Fault Mode | tooth root crack |  |
| 19 | `UMI43QJH_E153` | `has_fault_mode` | 04-Fault Location | ring gear |  | 05-Fault Mode | broken tooth |  |
| 20 | `UMI43QJH_E154` | `has_fault_mode` | 04-Fault Location | ring gear |  | 05-Fault Mode | missing tooth |  |
| 21 | `UMI43QJH_E155` | `has_fault_mode` | 04-Fault Location | ring gear |  | 05-Fault Mode | inner ring fault |  |
| 22 | `UMI43QJH_E156` | `has_fault_mode` | 04-Fault Location | ring gear |  | 05-Fault Mode | outer ring fault |  |
| 23 | `UMI43QJH_E157` | `has_fault_mode` | 04-Fault Location | planetary bearing |  | 05-Fault Mode | tooth root crack |  |
| 24 | `UMI43QJH_E158` | `has_fault_mode` | 04-Fault Location | planetary bearing |  | 05-Fault Mode | broken tooth |  |
| 25 | `UMI43QJH_E159` | `has_fault_mode` | 04-Fault Location | planetary bearing |  | 05-Fault Mode | missing tooth |  |
| 26 | `UMI43QJH_E160` | `has_fault_mode` | 04-Fault Location | planetary bearing |  | 05-Fault Mode | inner ring fault |  |
| 27 | `UMI43QJH_E161` | `has_fault_mode` | 04-Fault Location | planetary bearing |  | 05-Fault Mode | outer ring fault |  |
| 28 | `UMI43QJH_E162` | `contains` | 05-Fault Mode | tooth root crack |  | 06-Fault Severity | Single Severity |  |
| 29 | `UMI43QJH_E163` | `contains` | 05-Fault Mode | broken tooth |  | 06-Fault Severity | Single Severity |  |
| 30 | `UMI43QJH_E164` | `contains` | 05-Fault Mode | missing tooth |  | 06-Fault Severity | Single Severity |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
