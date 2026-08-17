# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：HQYLWLVF
- **Paper Title**：Research of weak fault feature information extraction of planetary gear based on ensemble empirical mode decomposition and adaptive stochastic resonance
- **Number of Candidate Edges to Judge**：26 

---

## II. LLM Input

> **Input Material**: Reference ID `HQYLWLVF`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "HQYLWLVF_E052", "edge_description": "breakage contains No Compound Fault"},
    {"edge_id": "HQYLWLVF_E053", "edge_description": "root crack contains No Compound Fault"},
    {"edge_id": "HQYLWLVF_E055", "edge_description": "acceleration sensors can obviously reflect breakage"},
    {"edge_id": "HQYLWLVF_E056", "edge_description": "acceleration sensors can obviously reflect root crack"},
    {"edge_id": "HQYLWLVF_E058", "edge_description": "sun gear has_fault_mode breakage"},
    {"edge_id": "HQYLWLVF_E059", "edge_description": "sun gear has_fault_mode root crack"},
    {"edge_id": "HQYLWLVF_E060", "edge_description": "breakage contains Single Severity"},
    {"edge_id": "HQYLWLVF_E061", "edge_description": "root crack contains Single Severity"},
    {"edge_id": "HQYLWLVF_E064", "edge_description": "breakage contains_phm_task Planetary gear fault diagnosis"},
    {"edge_id": "HQYLWLVF_E065", "edge_description": "root crack contains_phm_task Planetary gear fault diagnosis"},
    {"edge_id": "HQYLWLVF_E067", "edge_description": "Planetary gear induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E068", "edge_description": "Planetary gear induces_problem Nonlinear and non-stationary vibration of planetary gear"},
    {"edge_id": "HQYLWLVF_E069", "edge_description": "Constant operating conditions induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E070", "edge_description": "Constant operating conditions induces_problem Nonlinear and non-stationary vibration of planetary gear"},
    {"edge_id": "HQYLWLVF_E071", "edge_description": "Single Severity induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E072", "edge_description": "Single Severity induces_problem Nonlinear and non-stationary vibration of planetary gear"},
    {"edge_id": "HQYLWLVF_E073", "edge_description": "No Compound Fault induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E074", "edge_description": "No Compound Fault induces_problem Nonlinear and non-stationary vibration of planetary gear"},
    {"edge_id": "HQYLWLVF_E075", "edge_description": "Planetary gear fault diagnosis induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E076", "edge_description": "Planetary gear fault diagnosis induces_problem Nonlinear and non-stationary vibration of planetary gear"},
    {"edge_id": "HQYLWLVF_E077", "edge_description": "N/A induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E078", "edge_description": "N/A induces_problem Nonlinear and non-stationary vibration of planetary gear"},
    {"edge_id": "HQYLWLVF_E079", "edge_description": "noise interferences induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E080", "edge_description": "noise interferences induces_problem Nonlinear and non-stationary vibration of planetary gear"},
    {"edge_id": "HQYLWLVF_E081", "edge_description": "N/A induces_problem Weak fault feature submerged in noise"},
    {"edge_id": "HQYLWLVF_E082", "edge_description": "N/A induces_problem Nonlinear and non-stationary vibration of planetary gear"}
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
| 1 | `HQYLWLVF_E052` | `contains` | 05-Fault Mode | breakage |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `HQYLWLVF_E053` | `contains` | 05-Fault Mode | root crack |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `HQYLWLVF_E055` | `can obviously reflect` | 11-Sensor Information | acceleration sensors |  | 05-Fault Mode | breakage |  |
| 4 | `HQYLWLVF_E056` | `can obviously reflect` | 11-Sensor Information | acceleration sensors |  | 05-Fault Mode | root crack |  |
| 5 | `HQYLWLVF_E058` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | breakage |  |
| 6 | `HQYLWLVF_E059` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | root crack |  |
| 7 | `HQYLWLVF_E060` | `contains` | 05-Fault Mode | breakage |  | 06-Fault Severity | Single Severity |  |
| 8 | `HQYLWLVF_E061` | `contains` | 05-Fault Mode | root crack |  | 06-Fault Severity | Single Severity |  |
| 9 | `HQYLWLVF_E064` | `contains_phm_task` | 05-Fault Mode | breakage |  | 08-PHM Task | Planetary gear fault diagnosis(Diagnosis Task) |  |
| 10 | `HQYLWLVF_E065` | `contains_phm_task` | 05-Fault Mode | root crack |  | 08-PHM Task | Planetary gear fault diagnosis(Diagnosis Task) |  |
| 11 | `HQYLWLVF_E067` | `induces_problem` | 02-Object Type | Planetary gear |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 12 | `HQYLWLVF_E068` | `induces_problem` | 02-Object Type | Planetary gear |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |
| 13 | `HQYLWLVF_E069` | `induces_problem` | 03-Operating Conditions | Constant operating conditions(Single Condition) |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 14 | `HQYLWLVF_E070` | `induces_problem` | 03-Operating Conditions | Constant operating conditions(Single Condition) |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |
| 15 | `HQYLWLVF_E071` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 16 | `HQYLWLVF_E072` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |
| 17 | `HQYLWLVF_E073` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 18 | `HQYLWLVF_E074` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |
| 19 | `HQYLWLVF_E075` | `induces_problem` | 08-PHM Task | Planetary gear fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 20 | `HQYLWLVF_E076` | `induces_problem` | 08-PHM Task | Planetary gear fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |
| 21 | `HQYLWLVF_E077` | `induces_problem` | 12-Training Data Availability | N/A(Sufficient) |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 22 | `HQYLWLVF_E078` | `induces_problem` | 12-Training Data Availability | N/A(Sufficient) |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |
| 23 | `HQYLWLVF_E079` | `induces_problem` | 13-Noise Level | noise interferences(High Noise) |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 24 | `HQYLWLVF_E080` | `induces_problem` | 13-Noise Level | noise interferences(High Noise) |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |
| 25 | `HQYLWLVF_E081` | `induces_problem` | 14-Computational Resource | N/A |  | 09-Problem Scenario | Weak fault feature submerged in noise(Uncertainty) |  |
| 26 | `HQYLWLVF_E082` | `induces_problem` | 14-Computational Resource | N/A |  | 09-Problem Scenario | Nonlinear and non-stationary vibration of planetary gear(Complex Systems) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 26 edges)*
