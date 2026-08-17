# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：CBAZUCRE
- **Paper Title**：Multi-Physics Graphical Model-Based Fault Detection and Isolation in Wind Turbines
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `CBAZUCRE`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "CBAZUCRE_E182", "edge_description": "DC-Link capacitor contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E183", "edge_description": "hydraulic pitch actuator contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E184", "edge_description": "gear connected to LSS contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E185", "edge_description": "inter-turn short circuit contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E186", "edge_description": "open circuit fault contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E187", "edge_description": "short circuit fault contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E188", "edge_description": "capacitance reduction contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E189", "edge_description": "pressure drop contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E190", "edge_description": "broken tooth contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E192", "edge_description": "Doubly-Fed Induction Generator induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E193", "edge_description": "Doubly-Fed Induction Generator induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E194", "edge_description": "Gearbox and drive-train induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E195", "edge_description": "Gearbox and drive-train induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E196", "edge_description": "Hydraulic pitch actuator induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E197", "edge_description": "Hydraulic pitch actuator induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E198", "edge_description": "AC/DC/AC back-to-back power converter induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E199", "edge_description": "AC/DC/AC back-to-back power converter induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E200", "edge_description": "hybrid dynamical system under wind speed excitation and maximum power point tracking control induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E201", "edge_description": "hybrid dynamical system under wind speed excitation and maximum power point tracking control induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E202", "edge_description": "5% shorted, 10% reduction, pressure drop, broken tooth induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E203", "edge_description": "5% shorted, 10% reduction, pressure drop, broken tooth induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E204", "edge_description": "No Compound Fault induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E205", "edge_description": "No Compound Fault induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E206", "edge_description": "Fault Detection and Isolation (FDI) induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E207", "edge_description": "Fault Detection and Isolation (FDI) induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E208", "edge_description": "Sufficient induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E209", "edge_description": "Sufficient induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E210", "edge_description": "presence of noise induces_problem complex hybrid system with subsystems from different physical domains"},
    {"edge_id": "CBAZUCRE_E211", "edge_description": "presence of noise induces_problem measurement noise corruption and threshold determination uncertainty"},
    {"edge_id": "CBAZUCRE_E212", "edge_description": "low computational burden induces_problem complex hybrid system with subsystems from different physical domains"}
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
| 1 | `CBAZUCRE_E182` | `contains_phm_task` | 04-Fault Location | DC-Link capacitor |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 2 | `CBAZUCRE_E183` | `contains_phm_task` | 04-Fault Location | hydraulic pitch actuator |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 3 | `CBAZUCRE_E184` | `contains_phm_task` | 04-Fault Location | gear connected to LSS |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 4 | `CBAZUCRE_E185` | `contains_phm_task` | 05-Fault Mode | inter-turn short circuit |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 5 | `CBAZUCRE_E186` | `contains_phm_task` | 05-Fault Mode | open circuit fault |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 6 | `CBAZUCRE_E187` | `contains_phm_task` | 05-Fault Mode | short circuit fault |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 7 | `CBAZUCRE_E188` | `contains_phm_task` | 05-Fault Mode | capacitance reduction |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 8 | `CBAZUCRE_E189` | `contains_phm_task` | 05-Fault Mode | pressure drop |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 9 | `CBAZUCRE_E190` | `contains_phm_task` | 05-Fault Mode | broken tooth |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 10 | `CBAZUCRE_E192` | `induces_problem` | 02-Object Type | Doubly-Fed Induction Generator |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 11 | `CBAZUCRE_E193` | `induces_problem` | 02-Object Type | Doubly-Fed Induction Generator |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 12 | `CBAZUCRE_E194` | `induces_problem` | 02-Object Type | Gearbox and drive-train |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 13 | `CBAZUCRE_E195` | `induces_problem` | 02-Object Type | Gearbox and drive-train |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 14 | `CBAZUCRE_E196` | `induces_problem` | 02-Object Type | Hydraulic pitch actuator |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 15 | `CBAZUCRE_E197` | `induces_problem` | 02-Object Type | Hydraulic pitch actuator |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 16 | `CBAZUCRE_E198` | `induces_problem` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 17 | `CBAZUCRE_E199` | `induces_problem` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 18 | `CBAZUCRE_E200` | `induces_problem` | 03-Operating Conditions | hybrid dynamical system under wind speed excitation and maximum power point tracking control(Variable Conditions) |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 19 | `CBAZUCRE_E201` | `induces_problem` | 03-Operating Conditions | hybrid dynamical system under wind speed excitation and maximum power point tracking control(Variable Conditions) |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 20 | `CBAZUCRE_E202` | `induces_problem` | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 21 | `CBAZUCRE_E203` | `induces_problem` | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 22 | `CBAZUCRE_E204` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 23 | `CBAZUCRE_E205` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 24 | `CBAZUCRE_E206` | `induces_problem` | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 25 | `CBAZUCRE_E207` | `induces_problem` | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 26 | `CBAZUCRE_E208` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 27 | `CBAZUCRE_E209` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 28 | `CBAZUCRE_E210` | `induces_problem` | 13-Noise Level | presence of noise(High Noise) |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |
| 29 | `CBAZUCRE_E211` | `induces_problem` | 13-Noise Level | presence of noise(High Noise) |  | 09-Problem Scenario | measurement noise corruption and threshold determination uncertainty(Uncertainty) |  |
| 30 | `CBAZUCRE_E212` | `induces_problem` | 14-Computational Resource | low computational burden(Low Resource Consumption) |  | 09-Problem Scenario | complex hybrid system with subsystems from different physical domains(Complex Systems) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 5, total 30 edges)*
