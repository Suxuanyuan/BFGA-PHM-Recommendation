# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：EZ2I6EWG
- **Paper Title**：Fault Characterization of a Proton Exchange Membrane Fuel Cell Stack
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `EZ2I6EWG`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "EZ2I6EWG_E078", "edge_description": "anode has_fault_mode CO poisoning"},
    {"edge_id": "EZ2I6EWG_E079", "edge_description": "anode has_fault_mode H2S poisoning"},
    {"edge_id": "EZ2I6EWG_E080", "edge_description": "cathode has_fault_mode reactant starvation"},
    {"edge_id": "EZ2I6EWG_E081", "edge_description": "cathode has_fault_mode flooding"},
    {"edge_id": "EZ2I6EWG_E082", "edge_description": "cathode has_fault_mode drying"},
    {"edge_id": "EZ2I6EWG_E083", "edge_description": "cathode has_fault_mode CO poisoning"},
    {"edge_id": "EZ2I6EWG_E084", "edge_description": "cathode has_fault_mode H2S poisoning"},
    {"edge_id": "EZ2I6EWG_E085", "edge_description": "proton exchange membrane has_fault_mode reactant starvation"},
    {"edge_id": "EZ2I6EWG_E086", "edge_description": "proton exchange membrane has_fault_mode flooding"},
    {"edge_id": "EZ2I6EWG_E087", "edge_description": "proton exchange membrane has_fault_mode drying"},
    {"edge_id": "EZ2I6EWG_E088", "edge_description": "proton exchange membrane has_fault_mode CO poisoning"},
    {"edge_id": "EZ2I6EWG_E089", "edge_description": "proton exchange membrane has_fault_mode H2S poisoning"},
    {"edge_id": "EZ2I6EWG_E090", "edge_description": "gas diffusion layer has_fault_mode reactant starvation"},
    {"edge_id": "EZ2I6EWG_E091", "edge_description": "gas diffusion layer has_fault_mode flooding"},
    {"edge_id": "EZ2I6EWG_E092", "edge_description": "gas diffusion layer has_fault_mode drying"},
    {"edge_id": "EZ2I6EWG_E093", "edge_description": "gas diffusion layer has_fault_mode CO poisoning"},
    {"edge_id": "EZ2I6EWG_E094", "edge_description": "gas diffusion layer has_fault_mode H2S poisoning"},
    {"edge_id": "EZ2I6EWG_E095", "edge_description": "reactant starvation contains fault intensity levels"},
    {"edge_id": "EZ2I6EWG_E096", "edge_description": "flooding contains fault intensity levels"},
    {"edge_id": "EZ2I6EWG_E097", "edge_description": "drying contains fault intensity levels"},
    {"edge_id": "EZ2I6EWG_E098", "edge_description": "CO poisoning contains fault intensity levels"},
    {"edge_id": "EZ2I6EWG_E099", "edge_description": "H2S poisoning contains fault intensity levels"},
    {"edge_id": "EZ2I6EWG_E101", "edge_description": "anode contains_phm_task fault diagnosis"},
    {"edge_id": "EZ2I6EWG_E102", "edge_description": "cathode contains_phm_task fault diagnosis"},
    {"edge_id": "EZ2I6EWG_E103", "edge_description": "proton exchange membrane contains_phm_task fault diagnosis"},
    {"edge_id": "EZ2I6EWG_E104", "edge_description": "gas diffusion layer contains_phm_task fault diagnosis"},
    {"edge_id": "EZ2I6EWG_E105", "edge_description": "reactant starvation contains_phm_task fault diagnosis"},
    {"edge_id": "EZ2I6EWG_E106", "edge_description": "flooding contains_phm_task fault diagnosis"},
    {"edge_id": "EZ2I6EWG_E107", "edge_description": "drying contains_phm_task fault diagnosis"},
    {"edge_id": "EZ2I6EWG_E108", "edge_description": "CO poisoning contains_phm_task fault diagnosis"}
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
| 1 | `EZ2I6EWG_E078` | `has_fault_mode` | 04-Fault Location | anode |  | 05-Fault Mode | CO poisoning |  |
| 2 | `EZ2I6EWG_E079` | `has_fault_mode` | 04-Fault Location | anode |  | 05-Fault Mode | H2S poisoning |  |
| 3 | `EZ2I6EWG_E080` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | reactant starvation |  |
| 4 | `EZ2I6EWG_E081` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | flooding |  |
| 5 | `EZ2I6EWG_E082` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | drying |  |
| 6 | `EZ2I6EWG_E083` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | CO poisoning |  |
| 7 | `EZ2I6EWG_E084` | `has_fault_mode` | 04-Fault Location | cathode |  | 05-Fault Mode | H2S poisoning |  |
| 8 | `EZ2I6EWG_E085` | `has_fault_mode` | 04-Fault Location | proton exchange membrane |  | 05-Fault Mode | reactant starvation |  |
| 9 | `EZ2I6EWG_E086` | `has_fault_mode` | 04-Fault Location | proton exchange membrane |  | 05-Fault Mode | flooding |  |
| 10 | `EZ2I6EWG_E087` | `has_fault_mode` | 04-Fault Location | proton exchange membrane |  | 05-Fault Mode | drying |  |
| 11 | `EZ2I6EWG_E088` | `has_fault_mode` | 04-Fault Location | proton exchange membrane |  | 05-Fault Mode | CO poisoning |  |
| 12 | `EZ2I6EWG_E089` | `has_fault_mode` | 04-Fault Location | proton exchange membrane |  | 05-Fault Mode | H2S poisoning |  |
| 13 | `EZ2I6EWG_E090` | `has_fault_mode` | 04-Fault Location | gas diffusion layer |  | 05-Fault Mode | reactant starvation |  |
| 14 | `EZ2I6EWG_E091` | `has_fault_mode` | 04-Fault Location | gas diffusion layer |  | 05-Fault Mode | flooding |  |
| 15 | `EZ2I6EWG_E092` | `has_fault_mode` | 04-Fault Location | gas diffusion layer |  | 05-Fault Mode | drying |  |
| 16 | `EZ2I6EWG_E093` | `has_fault_mode` | 04-Fault Location | gas diffusion layer |  | 05-Fault Mode | CO poisoning |  |
| 17 | `EZ2I6EWG_E094` | `has_fault_mode` | 04-Fault Location | gas diffusion layer |  | 05-Fault Mode | H2S poisoning |  |
| 18 | `EZ2I6EWG_E095` | `contains` | 05-Fault Mode | reactant starvation |  | 06-Fault Severity | fault intensity levels(Multiple Severities) |  |
| 19 | `EZ2I6EWG_E096` | `contains` | 05-Fault Mode | flooding |  | 06-Fault Severity | fault intensity levels(Multiple Severities) |  |
| 20 | `EZ2I6EWG_E097` | `contains` | 05-Fault Mode | drying |  | 06-Fault Severity | fault intensity levels(Multiple Severities) |  |
| 21 | `EZ2I6EWG_E098` | `contains` | 05-Fault Mode | CO poisoning |  | 06-Fault Severity | fault intensity levels(Multiple Severities) |  |
| 22 | `EZ2I6EWG_E099` | `contains` | 05-Fault Mode | H2S poisoning |  | 06-Fault Severity | fault intensity levels(Multiple Severities) |  |
| 23 | `EZ2I6EWG_E101` | `contains_phm_task` | 04-Fault Location | anode |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 24 | `EZ2I6EWG_E102` | `contains_phm_task` | 04-Fault Location | cathode |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 25 | `EZ2I6EWG_E103` | `contains_phm_task` | 04-Fault Location | proton exchange membrane |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 26 | `EZ2I6EWG_E104` | `contains_phm_task` | 04-Fault Location | gas diffusion layer |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 27 | `EZ2I6EWG_E105` | `contains_phm_task` | 05-Fault Mode | reactant starvation |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 28 | `EZ2I6EWG_E106` | `contains_phm_task` | 05-Fault Mode | flooding |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 29 | `EZ2I6EWG_E107` | `contains_phm_task` | 05-Fault Mode | drying |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 30 | `EZ2I6EWG_E108` | `contains_phm_task` | 05-Fault Mode | CO poisoning |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
