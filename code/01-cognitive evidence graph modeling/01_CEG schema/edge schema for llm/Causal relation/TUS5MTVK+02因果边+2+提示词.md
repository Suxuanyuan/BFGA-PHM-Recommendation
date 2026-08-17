# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TUS5MTVK
- **Paper Title**：A Performance Evaluation of Two Bispectrum Analysis Methods Applied to Electrical Current Signals for Monitoring Induction Motor-Driven Systems
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `TUS5MTVK`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TUS5MTVK_E115", "edge_description": "current sensor is collected on intercooler"},
    {"edge_id": "TUS5MTVK_E116", "edge_description": "vibration sensor is collected on rotor bar"},
    {"edge_id": "TUS5MTVK_E117", "edge_description": "vibration sensor is collected on gear"},
    {"edge_id": "TUS5MTVK_E118", "edge_description": "vibration sensor is collected on discharge valve"},
    {"edge_id": "TUS5MTVK_E119", "edge_description": "vibration sensor is collected on transmission belt"},
    {"edge_id": "TUS5MTVK_E120", "edge_description": "vibration sensor is collected on intercooler"},
    {"edge_id": "TUS5MTVK_E121", "edge_description": "current sensor can obviously reflect broken rotor bar"},
    {"edge_id": "TUS5MTVK_E122", "edge_description": "current sensor can obviously reflect gear wear"},
    {"edge_id": "TUS5MTVK_E123", "edge_description": "current sensor can obviously reflect discharge valve leakage"},
    {"edge_id": "TUS5MTVK_E124", "edge_description": "current sensor can obviously reflect transmission belt looseness"},
    {"edge_id": "TUS5MTVK_E125", "edge_description": "current sensor can obviously reflect intercooler leakage"},
    {"edge_id": "TUS5MTVK_E126", "edge_description": "vibration sensor can obviously reflect broken rotor bar"},
    {"edge_id": "TUS5MTVK_E127", "edge_description": "vibration sensor can obviously reflect gear wear"},
    {"edge_id": "TUS5MTVK_E128", "edge_description": "vibration sensor can obviously reflect discharge valve leakage"},
    {"edge_id": "TUS5MTVK_E129", "edge_description": "vibration sensor can obviously reflect transmission belt looseness"},
    {"edge_id": "TUS5MTVK_E130", "edge_description": "vibration sensor can obviously reflect intercooler leakage"},
    {"edge_id": "TUS5MTVK_E131", "edge_description": "Induction motor broken rotor bar experimental dataset can be used for fault diagnosis"},
    {"edge_id": "TUS5MTVK_E132", "edge_description": "Two-stage helical gearbox deterioration experimental dataset can be used for fault diagnosis"},
    {"edge_id": "TUS5MTVK_E133", "edge_description": "Reciprocating compressor experimental dataset can be used for fault diagnosis"},
    {"edge_id": "TUS5MTVK_E134", "edge_description": "rotor bar has_fault_mode broken rotor bar"},
    {"edge_id": "TUS5MTVK_E135", "edge_description": "rotor bar has_fault_mode gear wear"},
    {"edge_id": "TUS5MTVK_E136", "edge_description": "rotor bar has_fault_mode discharge valve leakage"},
    {"edge_id": "TUS5MTVK_E137", "edge_description": "rotor bar has_fault_mode transmission belt looseness"},
    {"edge_id": "TUS5MTVK_E138", "edge_description": "rotor bar has_fault_mode intercooler leakage"},
    {"edge_id": "TUS5MTVK_E139", "edge_description": "gear has_fault_mode broken rotor bar"},
    {"edge_id": "TUS5MTVK_E140", "edge_description": "gear has_fault_mode gear wear"},
    {"edge_id": "TUS5MTVK_E141", "edge_description": "gear has_fault_mode discharge valve leakage"},
    {"edge_id": "TUS5MTVK_E142", "edge_description": "gear has_fault_mode transmission belt looseness"},
    {"edge_id": "TUS5MTVK_E143", "edge_description": "gear has_fault_mode intercooler leakage"},
    {"edge_id": "TUS5MTVK_E144", "edge_description": "discharge valve has_fault_mode broken rotor bar"}
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
| 1 | `TUS5MTVK_E115` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | intercooler |  |
| 2 | `TUS5MTVK_E116` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | rotor bar |  |
| 3 | `TUS5MTVK_E117` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | gear |  |
| 4 | `TUS5MTVK_E118` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | discharge valve |  |
| 5 | `TUS5MTVK_E119` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | transmission belt |  |
| 6 | `TUS5MTVK_E120` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | intercooler |  |
| 7 | `TUS5MTVK_E121` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | broken rotor bar |  |
| 8 | `TUS5MTVK_E122` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | gear wear |  |
| 9 | `TUS5MTVK_E123` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | discharge valve leakage |  |
| 10 | `TUS5MTVK_E124` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | transmission belt looseness |  |
| 11 | `TUS5MTVK_E125` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | intercooler leakage |  |
| 12 | `TUS5MTVK_E126` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | broken rotor bar |  |
| 13 | `TUS5MTVK_E127` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | gear wear |  |
| 14 | `TUS5MTVK_E128` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | discharge valve leakage |  |
| 15 | `TUS5MTVK_E129` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | transmission belt looseness |  |
| 16 | `TUS5MTVK_E130` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | intercooler leakage |  |
| 17 | `TUS5MTVK_E131` | `can be used for` | 10-Dataset | Induction motor broken rotor bar experimental dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `TUS5MTVK_E132` | `can be used for` | 10-Dataset | Two-stage helical gearbox deterioration experimental dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `TUS5MTVK_E133` | `can be used for` | 10-Dataset | Reciprocating compressor experimental dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `TUS5MTVK_E134` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | broken rotor bar |  |
| 21 | `TUS5MTVK_E135` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | gear wear |  |
| 22 | `TUS5MTVK_E136` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | discharge valve leakage |  |
| 23 | `TUS5MTVK_E137` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | transmission belt looseness |  |
| 24 | `TUS5MTVK_E138` | `has_fault_mode` | 04-Fault Location | rotor bar |  | 05-Fault Mode | intercooler leakage |  |
| 25 | `TUS5MTVK_E139` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | broken rotor bar |  |
| 26 | `TUS5MTVK_E140` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | gear wear |  |
| 27 | `TUS5MTVK_E141` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | discharge valve leakage |  |
| 28 | `TUS5MTVK_E142` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | transmission belt looseness |  |
| 29 | `TUS5MTVK_E143` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | intercooler leakage |  |
| 30 | `TUS5MTVK_E144` | `has_fault_mode` | 04-Fault Location | discharge valve |  | 05-Fault Mode | broken rotor bar |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
