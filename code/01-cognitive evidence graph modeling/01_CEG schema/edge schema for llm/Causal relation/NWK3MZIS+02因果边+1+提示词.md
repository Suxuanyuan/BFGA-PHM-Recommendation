# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：NWK3MZIS
- **Paper Title**：Fault Detection Methods for Three-Level NPC Inverter Based on DC-Bus Electromagnetic Signatures
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `NWK3MZIS`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "NWK3MZIS_E058", "edge_description": "Power electronics converters contains Three-level NPC inverter"},
    {"edge_id": "NWK3MZIS_E059", "edge_description": "Power electronics converters contains Clamping diodes"},
    {"edge_id": "NWK3MZIS_E060", "edge_description": "Three-level NPC inverter contains clamping diode"},
    {"edge_id": "NWK3MZIS_E061", "edge_description": "Three-level NPC inverter contains power switch"},
    {"edge_id": "NWK3MZIS_E062", "edge_description": "Clamping diodes contains clamping diode"},
    {"edge_id": "NWK3MZIS_E063", "edge_description": "Clamping diodes contains power switch"},
    {"edge_id": "NWK3MZIS_E064", "edge_description": "Three-level NPC inverter contains transient and steady state operations with variable modulation indexes"},
    {"edge_id": "NWK3MZIS_E065", "edge_description": "Clamping diodes contains transient and steady state operations with variable modulation indexes"},
    {"edge_id": "NWK3MZIS_E067", "edge_description": "EMI filter is collected on clamping diode"},
    {"edge_id": "NWK3MZIS_E068", "edge_description": "EMI filter is collected on power switch"},
    {"edge_id": "NWK3MZIS_E069", "edge_description": "Near-field antenna is collected on clamping diode"},
    {"edge_id": "NWK3MZIS_E070", "edge_description": "Near-field antenna is collected on power switch"},
    {"edge_id": "NWK3MZIS_E071", "edge_description": "EMI filter can obviously reflect open-circuit fault"},
    {"edge_id": "NWK3MZIS_E072", "edge_description": "Near-field antenna can obviously reflect open-circuit fault"},
    {"edge_id": "NWK3MZIS_E073", "edge_description": "Laboratory prototype experimental data can be used for open-circuit fault diagnosis and classification"},
    {"edge_id": "NWK3MZIS_E074", "edge_description": "Simulation data from high frequency model can be used for open-circuit fault diagnosis and classification"},
    {"edge_id": "NWK3MZIS_E075", "edge_description": "clamping diode has_fault_mode open-circuit fault"},
    {"edge_id": "NWK3MZIS_E076", "edge_description": "power switch has_fault_mode open-circuit fault"},
    {"edge_id": "NWK3MZIS_E078", "edge_description": "Three-level NPC inverter contains_phm_task open-circuit fault diagnosis and classification"},
    {"edge_id": "NWK3MZIS_E079", "edge_description": "Clamping diodes contains_phm_task open-circuit fault diagnosis and classification"},
    {"edge_id": "NWK3MZIS_E080", "edge_description": "clamping diode contains_phm_task open-circuit fault diagnosis and classification"},
    {"edge_id": "NWK3MZIS_E081", "edge_description": "power switch contains_phm_task open-circuit fault diagnosis and classification"},
    {"edge_id": "NWK3MZIS_E084", "edge_description": "Three-level NPC inverter induces_problem multiple open-circuit faults"},
    {"edge_id": "NWK3MZIS_E085", "edge_description": "Three-level NPC inverter induces_problem noise robustness and parameter sensitivity"},
    {"edge_id": "NWK3MZIS_E086", "edge_description": "Clamping diodes induces_problem multiple open-circuit faults"},
    {"edge_id": "NWK3MZIS_E087", "edge_description": "Clamping diodes induces_problem noise robustness and parameter sensitivity"},
    {"edge_id": "NWK3MZIS_E088", "edge_description": "transient and steady state operations with variable modulation indexes induces_problem multiple open-circuit faults"},
    {"edge_id": "NWK3MZIS_E089", "edge_description": "transient and steady state operations with variable modulation indexes induces_problem noise robustness and parameter sensitivity"},
    {"edge_id": "NWK3MZIS_E090", "edge_description": "Single Severity induces_problem multiple open-circuit faults"},
    {"edge_id": "NWK3MZIS_E091", "edge_description": "Single Severity induces_problem noise robustness and parameter sensitivity"}
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
| 1 | `NWK3MZIS_E058` | `contains` | 01-Object Domain | Power electronics converters(Electronics) |  | 02-Object Type | Three-level NPC inverter |  |
| 2 | `NWK3MZIS_E059` | `contains` | 01-Object Domain | Power electronics converters(Electronics) |  | 02-Object Type | Clamping diodes |  |
| 3 | `NWK3MZIS_E060` | `contains` | 02-Object Type | Three-level NPC inverter |  | 04-Fault Location | clamping diode |  |
| 4 | `NWK3MZIS_E061` | `contains` | 02-Object Type | Three-level NPC inverter |  | 04-Fault Location | power switch |  |
| 5 | `NWK3MZIS_E062` | `contains` | 02-Object Type | Clamping diodes |  | 04-Fault Location | clamping diode |  |
| 6 | `NWK3MZIS_E063` | `contains` | 02-Object Type | Clamping diodes |  | 04-Fault Location | power switch |  |
| 7 | `NWK3MZIS_E064` | `contains` | 02-Object Type | Three-level NPC inverter |  | 03-Operating Conditions | transient and steady state operations with variable modulation indexes(Variable Conditions) |  |
| 8 | `NWK3MZIS_E065` | `contains` | 02-Object Type | Clamping diodes |  | 03-Operating Conditions | transient and steady state operations with variable modulation indexes(Variable Conditions) |  |
| 9 | `NWK3MZIS_E067` | `is collected on` | 11-Sensor Information | EMI filter |  | 04-Fault Location | clamping diode |  |
| 10 | `NWK3MZIS_E068` | `is collected on` | 11-Sensor Information | EMI filter |  | 04-Fault Location | power switch |  |
| 11 | `NWK3MZIS_E069` | `is collected on` | 11-Sensor Information | Near-field antenna |  | 04-Fault Location | clamping diode |  |
| 12 | `NWK3MZIS_E070` | `is collected on` | 11-Sensor Information | Near-field antenna |  | 04-Fault Location | power switch |  |
| 13 | `NWK3MZIS_E071` | `can obviously reflect` | 11-Sensor Information | EMI filter |  | 05-Fault Mode | open-circuit fault |  |
| 14 | `NWK3MZIS_E072` | `can obviously reflect` | 11-Sensor Information | Near-field antenna |  | 05-Fault Mode | open-circuit fault |  |
| 15 | `NWK3MZIS_E073` | `can be used for` | 10-Dataset | Laboratory prototype experimental data |  | 08-PHM Task | open-circuit fault diagnosis and classification(Diagnosis Task) |  |
| 16 | `NWK3MZIS_E074` | `can be used for` | 10-Dataset | Simulation data from high frequency model |  | 08-PHM Task | open-circuit fault diagnosis and classification(Diagnosis Task) |  |
| 17 | `NWK3MZIS_E075` | `has_fault_mode` | 04-Fault Location | clamping diode |  | 05-Fault Mode | open-circuit fault |  |
| 18 | `NWK3MZIS_E076` | `has_fault_mode` | 04-Fault Location | power switch |  | 05-Fault Mode | open-circuit fault |  |
| 19 | `NWK3MZIS_E078` | `contains_phm_task` | 02-Object Type | Three-level NPC inverter |  | 08-PHM Task | open-circuit fault diagnosis and classification(Diagnosis Task) |  |
| 20 | `NWK3MZIS_E079` | `contains_phm_task` | 02-Object Type | Clamping diodes |  | 08-PHM Task | open-circuit fault diagnosis and classification(Diagnosis Task) |  |
| 21 | `NWK3MZIS_E080` | `contains_phm_task` | 04-Fault Location | clamping diode |  | 08-PHM Task | open-circuit fault diagnosis and classification(Diagnosis Task) |  |
| 22 | `NWK3MZIS_E081` | `contains_phm_task` | 04-Fault Location | power switch |  | 08-PHM Task | open-circuit fault diagnosis and classification(Diagnosis Task) |  |
| 23 | `NWK3MZIS_E084` | `induces_problem` | 02-Object Type | Three-level NPC inverter |  | 09-Problem Scenario | multiple open-circuit faults(Compound Faults) |  |
| 24 | `NWK3MZIS_E085` | `induces_problem` | 02-Object Type | Three-level NPC inverter |  | 09-Problem Scenario | noise robustness and parameter sensitivity(Uncertainty) |  |
| 25 | `NWK3MZIS_E086` | `induces_problem` | 02-Object Type | Clamping diodes |  | 09-Problem Scenario | multiple open-circuit faults(Compound Faults) |  |
| 26 | `NWK3MZIS_E087` | `induces_problem` | 02-Object Type | Clamping diodes |  | 09-Problem Scenario | noise robustness and parameter sensitivity(Uncertainty) |  |
| 27 | `NWK3MZIS_E088` | `induces_problem` | 03-Operating Conditions | transient and steady state operations with variable modulation indexes(Variable Conditions) |  | 09-Problem Scenario | multiple open-circuit faults(Compound Faults) |  |
| 28 | `NWK3MZIS_E089` | `induces_problem` | 03-Operating Conditions | transient and steady state operations with variable modulation indexes(Variable Conditions) |  | 09-Problem Scenario | noise robustness and parameter sensitivity(Uncertainty) |  |
| 29 | `NWK3MZIS_E090` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | multiple open-circuit faults(Compound Faults) |  |
| 30 | `NWK3MZIS_E091` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | noise robustness and parameter sensitivity(Uncertainty) |  |

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

### ▶ For `induces_problem` (X type → 09-Problem Scenario type)

**Retention Principle**: Encourage retaining but do not retain incorrect candidate edges. Specifically:
- **Retainable**: The paper **directly mentions** that source induces/causes the target problem scenario; or although not directly mentioned, it is **very likely to indirectly exist** when combining context/domain knowledge
- **Not Retainable**: The paper **does not mention it at all**, and it is **impossible to indirectly infer** this causal relation from the text content or domain knowledge(such edges will pollute the graph and must be deleted)
**Judgment Basis**: Comprehensively understand the full text, examining whether the problem description, experimental motivation, method design, etc., imply the source→target causal logic.

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
