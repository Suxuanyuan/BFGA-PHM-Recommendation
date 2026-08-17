# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：XCALVT2V
- **Paper Title**：Fault Diagnosis for PEMFC Systems in Consideration of Dynamic Behaviors and Spatial Inhomogeneity
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `XCALVT2V`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "XCALVT2V_E058", "edge_description": "Low pressure fault contains No Compound Fault"},
    {"edge_id": "XCALVT2V_E059", "edge_description": "High pressure fault contains No Compound Fault"},
    {"edge_id": "XCALVT2V_E060", "edge_description": "Drying fault contains No Compound Fault"},
    {"edge_id": "XCALVT2V_E061", "edge_description": "Low air stoichiometry fault contains No Compound Fault"},
    {"edge_id": "XCALVT2V_E063", "edge_description": "Giant Magnetoresistance (GMR) voltage sensors can obviously reflect Low pressure fault"},
    {"edge_id": "XCALVT2V_E064", "edge_description": "Giant Magnetoresistance (GMR) voltage sensors can obviously reflect High pressure fault"},
    {"edge_id": "XCALVT2V_E065", "edge_description": "Giant Magnetoresistance (GMR) voltage sensors can obviously reflect Drying fault"},
    {"edge_id": "XCALVT2V_E066", "edge_description": "Giant Magnetoresistance (GMR) voltage sensors can obviously reflect Low air stoichiometry fault"},
    {"edge_id": "XCALVT2V_E068", "edge_description": "PEMFC stack has_fault_mode Low pressure fault"},
    {"edge_id": "XCALVT2V_E069", "edge_description": "PEMFC stack has_fault_mode High pressure fault"},
    {"edge_id": "XCALVT2V_E070", "edge_description": "PEMFC stack has_fault_mode Drying fault"},
    {"edge_id": "XCALVT2V_E071", "edge_description": "PEMFC stack has_fault_mode Low air stoichiometry fault"},
    {"edge_id": "XCALVT2V_E072", "edge_description": "Low pressure fault contains Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5"},
    {"edge_id": "XCALVT2V_E073", "edge_description": "High pressure fault contains Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5"},
    {"edge_id": "XCALVT2V_E074", "edge_description": "Drying fault contains Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5"},
    {"edge_id": "XCALVT2V_E075", "edge_description": "Low air stoichiometry fault contains Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5"},
    {"edge_id": "XCALVT2V_E078", "edge_description": "Low pressure fault contains_phm_task fault detection and fault isolation"},
    {"edge_id": "XCALVT2V_E079", "edge_description": "High pressure fault contains_phm_task fault detection and fault isolation"},
    {"edge_id": "XCALVT2V_E080", "edge_description": "Drying fault contains_phm_task fault detection and fault isolation"},
    {"edge_id": "XCALVT2V_E081", "edge_description": "Low air stoichiometry fault contains_phm_task fault detection and fault isolation"},
    {"edge_id": "XCALVT2V_E083", "edge_description": "Proton Exchange Membrane Fuel Cell (PEMFC) system induces_problem system dynamics and spatial inhomogeneity"},
    {"edge_id": "XCALVT2V_E084", "edge_description": "Proton Exchange Membrane Fuel Cell (PEMFC) system induces_problem unseen fault recognition"},
    {"edge_id": "XCALVT2V_E085", "edge_description": "operated near to the nominal current value induces_problem system dynamics and spatial inhomogeneity"},
    {"edge_id": "XCALVT2V_E086", "edge_description": "operated near to the nominal current value induces_problem unseen fault recognition"},
    {"edge_id": "XCALVT2V_E087", "edge_description": "Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5 induces_problem system dynamics and spatial inhomogeneity"},
    {"edge_id": "XCALVT2V_E088", "edge_description": "Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5 induces_problem unseen fault recognition"},
    {"edge_id": "XCALVT2V_E089", "edge_description": "No Compound Fault induces_problem system dynamics and spatial inhomogeneity"},
    {"edge_id": "XCALVT2V_E090", "edge_description": "No Compound Fault induces_problem unseen fault recognition"},
    {"edge_id": "XCALVT2V_E091", "edge_description": "fault detection and fault isolation induces_problem system dynamics and spatial inhomogeneity"},
    {"edge_id": "XCALVT2V_E092", "edge_description": "fault detection and fault isolation induces_problem unseen fault recognition"}
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
| 1 | `XCALVT2V_E058` | `contains` | 05-Fault Mode | Low pressure fault |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `XCALVT2V_E059` | `contains` | 05-Fault Mode | High pressure fault |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `XCALVT2V_E060` | `contains` | 05-Fault Mode | Drying fault |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `XCALVT2V_E061` | `contains` | 05-Fault Mode | Low air stoichiometry fault |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `XCALVT2V_E063` | `can obviously reflect` | 11-Sensor Information | Giant Magnetoresistance (GMR) voltage sensors |  | 05-Fault Mode | Low pressure fault |  |
| 6 | `XCALVT2V_E064` | `can obviously reflect` | 11-Sensor Information | Giant Magnetoresistance (GMR) voltage sensors |  | 05-Fault Mode | High pressure fault |  |
| 7 | `XCALVT2V_E065` | `can obviously reflect` | 11-Sensor Information | Giant Magnetoresistance (GMR) voltage sensors |  | 05-Fault Mode | Drying fault |  |
| 8 | `XCALVT2V_E066` | `can obviously reflect` | 11-Sensor Information | Giant Magnetoresistance (GMR) voltage sensors |  | 05-Fault Mode | Low air stoichiometry fault |  |
| 9 | `XCALVT2V_E068` | `has_fault_mode` | 04-Fault Location | PEMFC stack |  | 05-Fault Mode | Low pressure fault |  |
| 10 | `XCALVT2V_E069` | `has_fault_mode` | 04-Fault Location | PEMFC stack |  | 05-Fault Mode | High pressure fault |  |
| 11 | `XCALVT2V_E070` | `has_fault_mode` | 04-Fault Location | PEMFC stack |  | 05-Fault Mode | Drying fault |  |
| 12 | `XCALVT2V_E071` | `has_fault_mode` | 04-Fault Location | PEMFC stack |  | 05-Fault Mode | Low air stoichiometry fault |  |
| 13 | `XCALVT2V_E072` | `contains` | 05-Fault Mode | Low pressure fault |  | 06-Fault Severity | Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5(Single Severity) |  |
| 14 | `XCALVT2V_E073` | `contains` | 05-Fault Mode | High pressure fault |  | 06-Fault Severity | Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5(Single Severity) |  |
| 15 | `XCALVT2V_E074` | `contains` | 05-Fault Mode | Drying fault |  | 06-Fault Severity | Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5(Single Severity) |  |
| 16 | `XCALVT2V_E075` | `contains` | 05-Fault Mode | Low air stoichiometry fault |  | 06-Fault Severity | Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5(Single Severity) |  |
| 17 | `XCALVT2V_E078` | `contains_phm_task` | 05-Fault Mode | Low pressure fault |  | 08-PHM Task | fault detection and fault isolation(Diagnosis Task) |  |
| 18 | `XCALVT2V_E079` | `contains_phm_task` | 05-Fault Mode | High pressure fault |  | 08-PHM Task | fault detection and fault isolation(Diagnosis Task) |  |
| 19 | `XCALVT2V_E080` | `contains_phm_task` | 05-Fault Mode | Drying fault |  | 08-PHM Task | fault detection and fault isolation(Diagnosis Task) |  |
| 20 | `XCALVT2V_E081` | `contains_phm_task` | 05-Fault Mode | Low air stoichiometry fault |  | 08-PHM Task | fault detection and fault isolation(Diagnosis Task) |  |
| 21 | `XCALVT2V_E083` | `induces_problem` | 02-Object Type | Proton Exchange Membrane Fuel Cell (PEMFC) system |  | 09-Problem Scenario | system dynamics and spatial inhomogeneity(Complex Systems) |  |
| 22 | `XCALVT2V_E084` | `induces_problem` | 02-Object Type | Proton Exchange Membrane Fuel Cell (PEMFC) system |  | 09-Problem Scenario | unseen fault recognition(Zero Fault Samples) |  |
| 23 | `XCALVT2V_E085` | `induces_problem` | 03-Operating Conditions | operated near to the nominal current value(Single Condition) |  | 09-Problem Scenario | system dynamics and spatial inhomogeneity(Complex Systems) |  |
| 24 | `XCALVT2V_E086` | `induces_problem` | 03-Operating Conditions | operated near to the nominal current value(Single Condition) |  | 09-Problem Scenario | unseen fault recognition(Zero Fault Samples) |  |
| 25 | `XCALVT2V_E087` | `induces_problem` | 06-Fault Severity | Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5(Single Severity) |  | 09-Problem Scenario | system dynamics and spatial inhomogeneity(Complex Systems) |  |
| 26 | `XCALVT2V_E088` | `induces_problem` | 06-Fault Severity | Pressure of 1.3 bar, Pressure of 1.7 bar, Stoichiometry Air 1.5(Single Severity) |  | 09-Problem Scenario | unseen fault recognition(Zero Fault Samples) |  |
| 27 | `XCALVT2V_E089` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | system dynamics and spatial inhomogeneity(Complex Systems) |  |
| 28 | `XCALVT2V_E090` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | unseen fault recognition(Zero Fault Samples) |  |
| 29 | `XCALVT2V_E091` | `induces_problem` | 08-PHM Task | fault detection and fault isolation(Diagnosis Task) |  | 09-Problem Scenario | system dynamics and spatial inhomogeneity(Complex Systems) |  |
| 30 | `XCALVT2V_E092` | `induces_problem` | 08-PHM Task | fault detection and fault isolation(Diagnosis Task) |  | 09-Problem Scenario | unseen fault recognition(Zero Fault Samples) |  |

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
