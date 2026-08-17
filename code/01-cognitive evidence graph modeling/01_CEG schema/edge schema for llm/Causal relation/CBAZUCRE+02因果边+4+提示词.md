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
    {"edge_id": "CBAZUCRE_E152", "edge_description": "DC-Link capacitor has_fault_mode inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E153", "edge_description": "DC-Link capacitor has_fault_mode open circuit fault"},
    {"edge_id": "CBAZUCRE_E154", "edge_description": "DC-Link capacitor has_fault_mode short circuit fault"},
    {"edge_id": "CBAZUCRE_E155", "edge_description": "DC-Link capacitor has_fault_mode capacitance reduction"},
    {"edge_id": "CBAZUCRE_E156", "edge_description": "DC-Link capacitor has_fault_mode pressure drop"},
    {"edge_id": "CBAZUCRE_E157", "edge_description": "DC-Link capacitor has_fault_mode broken tooth"},
    {"edge_id": "CBAZUCRE_E158", "edge_description": "hydraulic pitch actuator has_fault_mode inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E159", "edge_description": "hydraulic pitch actuator has_fault_mode open circuit fault"},
    {"edge_id": "CBAZUCRE_E160", "edge_description": "hydraulic pitch actuator has_fault_mode short circuit fault"},
    {"edge_id": "CBAZUCRE_E161", "edge_description": "hydraulic pitch actuator has_fault_mode capacitance reduction"},
    {"edge_id": "CBAZUCRE_E162", "edge_description": "hydraulic pitch actuator has_fault_mode pressure drop"},
    {"edge_id": "CBAZUCRE_E163", "edge_description": "hydraulic pitch actuator has_fault_mode broken tooth"},
    {"edge_id": "CBAZUCRE_E164", "edge_description": "gear connected to LSS has_fault_mode inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E165", "edge_description": "gear connected to LSS has_fault_mode open circuit fault"},
    {"edge_id": "CBAZUCRE_E166", "edge_description": "gear connected to LSS has_fault_mode short circuit fault"},
    {"edge_id": "CBAZUCRE_E167", "edge_description": "gear connected to LSS has_fault_mode capacitance reduction"},
    {"edge_id": "CBAZUCRE_E168", "edge_description": "gear connected to LSS has_fault_mode pressure drop"},
    {"edge_id": "CBAZUCRE_E169", "edge_description": "gear connected to LSS has_fault_mode broken tooth"},
    {"edge_id": "CBAZUCRE_E170", "edge_description": "inter-turn short circuit contains 5% shorted, 10% reduction, pressure drop, broken tooth"},
    {"edge_id": "CBAZUCRE_E171", "edge_description": "open circuit fault contains 5% shorted, 10% reduction, pressure drop, broken tooth"},
    {"edge_id": "CBAZUCRE_E172", "edge_description": "short circuit fault contains 5% shorted, 10% reduction, pressure drop, broken tooth"},
    {"edge_id": "CBAZUCRE_E173", "edge_description": "capacitance reduction contains 5% shorted, 10% reduction, pressure drop, broken tooth"},
    {"edge_id": "CBAZUCRE_E174", "edge_description": "pressure drop contains 5% shorted, 10% reduction, pressure drop, broken tooth"},
    {"edge_id": "CBAZUCRE_E175", "edge_description": "broken tooth contains 5% shorted, 10% reduction, pressure drop, broken tooth"},
    {"edge_id": "CBAZUCRE_E176", "edge_description": "Doubly-Fed Induction Generator contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E177", "edge_description": "Gearbox and drive-train contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E178", "edge_description": "Hydraulic pitch actuator contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E179", "edge_description": "AC/DC/AC back-to-back power converter contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E180", "edge_description": "rotor windings contains_phm_task Fault Detection and Isolation (FDI)"},
    {"edge_id": "CBAZUCRE_E181", "edge_description": "switches of power converter contains_phm_task Fault Detection and Isolation (FDI)"}
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
| 1 | `CBAZUCRE_E152` | `has_fault_mode` | 04-Fault Location | DC-Link capacitor |  | 05-Fault Mode | inter-turn short circuit |  |
| 2 | `CBAZUCRE_E153` | `has_fault_mode` | 04-Fault Location | DC-Link capacitor |  | 05-Fault Mode | open circuit fault |  |
| 3 | `CBAZUCRE_E154` | `has_fault_mode` | 04-Fault Location | DC-Link capacitor |  | 05-Fault Mode | short circuit fault |  |
| 4 | `CBAZUCRE_E155` | `has_fault_mode` | 04-Fault Location | DC-Link capacitor |  | 05-Fault Mode | capacitance reduction |  |
| 5 | `CBAZUCRE_E156` | `has_fault_mode` | 04-Fault Location | DC-Link capacitor |  | 05-Fault Mode | pressure drop |  |
| 6 | `CBAZUCRE_E157` | `has_fault_mode` | 04-Fault Location | DC-Link capacitor |  | 05-Fault Mode | broken tooth |  |
| 7 | `CBAZUCRE_E158` | `has_fault_mode` | 04-Fault Location | hydraulic pitch actuator |  | 05-Fault Mode | inter-turn short circuit |  |
| 8 | `CBAZUCRE_E159` | `has_fault_mode` | 04-Fault Location | hydraulic pitch actuator |  | 05-Fault Mode | open circuit fault |  |
| 9 | `CBAZUCRE_E160` | `has_fault_mode` | 04-Fault Location | hydraulic pitch actuator |  | 05-Fault Mode | short circuit fault |  |
| 10 | `CBAZUCRE_E161` | `has_fault_mode` | 04-Fault Location | hydraulic pitch actuator |  | 05-Fault Mode | capacitance reduction |  |
| 11 | `CBAZUCRE_E162` | `has_fault_mode` | 04-Fault Location | hydraulic pitch actuator |  | 05-Fault Mode | pressure drop |  |
| 12 | `CBAZUCRE_E163` | `has_fault_mode` | 04-Fault Location | hydraulic pitch actuator |  | 05-Fault Mode | broken tooth |  |
| 13 | `CBAZUCRE_E164` | `has_fault_mode` | 04-Fault Location | gear connected to LSS |  | 05-Fault Mode | inter-turn short circuit |  |
| 14 | `CBAZUCRE_E165` | `has_fault_mode` | 04-Fault Location | gear connected to LSS |  | 05-Fault Mode | open circuit fault |  |
| 15 | `CBAZUCRE_E166` | `has_fault_mode` | 04-Fault Location | gear connected to LSS |  | 05-Fault Mode | short circuit fault |  |
| 16 | `CBAZUCRE_E167` | `has_fault_mode` | 04-Fault Location | gear connected to LSS |  | 05-Fault Mode | capacitance reduction |  |
| 17 | `CBAZUCRE_E168` | `has_fault_mode` | 04-Fault Location | gear connected to LSS |  | 05-Fault Mode | pressure drop |  |
| 18 | `CBAZUCRE_E169` | `has_fault_mode` | 04-Fault Location | gear connected to LSS |  | 05-Fault Mode | broken tooth |  |
| 19 | `CBAZUCRE_E170` | `contains` | 05-Fault Mode | inter-turn short circuit |  | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  |
| 20 | `CBAZUCRE_E171` | `contains` | 05-Fault Mode | open circuit fault |  | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  |
| 21 | `CBAZUCRE_E172` | `contains` | 05-Fault Mode | short circuit fault |  | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  |
| 22 | `CBAZUCRE_E173` | `contains` | 05-Fault Mode | capacitance reduction |  | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  |
| 23 | `CBAZUCRE_E174` | `contains` | 05-Fault Mode | pressure drop |  | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  |
| 24 | `CBAZUCRE_E175` | `contains` | 05-Fault Mode | broken tooth |  | 06-Fault Severity | 5% shorted, 10% reduction, pressure drop, broken tooth(Single Severity) |  |
| 25 | `CBAZUCRE_E176` | `contains_phm_task` | 02-Object Type | Doubly-Fed Induction Generator |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 26 | `CBAZUCRE_E177` | `contains_phm_task` | 02-Object Type | Gearbox and drive-train |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 27 | `CBAZUCRE_E178` | `contains_phm_task` | 02-Object Type | Hydraulic pitch actuator |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 28 | `CBAZUCRE_E179` | `contains_phm_task` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 29 | `CBAZUCRE_E180` | `contains_phm_task` | 04-Fault Location | rotor windings |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |
| 30 | `CBAZUCRE_E181` | `contains_phm_task` | 04-Fault Location | switches of power converter |  | 08-PHM Task | Fault Detection and Isolation (FDI)(Diagnosis Task) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 4, total 30 edges)*
