# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：EU3F5TIE
- **Paper Title**：A Comprehensive Monitoring System for Online Fault Diagnosis and Aging Detection of Non-Isolated DC-DC Converters' Components
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `EU3F5TIE`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "EU3F5TIE_E090", "edge_description": "power switch has_fault_mode aging"},
    {"edge_id": "EU3F5TIE_E091", "edge_description": "power switch has_fault_mode inter-turn fault"},
    {"edge_id": "EU3F5TIE_E092", "edge_description": "diode has_fault_mode open circuit fault"},
    {"edge_id": "EU3F5TIE_E093", "edge_description": "diode has_fault_mode short circuit fault"},
    {"edge_id": "EU3F5TIE_E094", "edge_description": "diode has_fault_mode aging"},
    {"edge_id": "EU3F5TIE_E095", "edge_description": "diode has_fault_mode inter-turn fault"},
    {"edge_id": "EU3F5TIE_E096", "edge_description": "capacitor has_fault_mode open circuit fault"},
    {"edge_id": "EU3F5TIE_E097", "edge_description": "capacitor has_fault_mode short circuit fault"},
    {"edge_id": "EU3F5TIE_E098", "edge_description": "capacitor has_fault_mode aging"},
    {"edge_id": "EU3F5TIE_E099", "edge_description": "capacitor has_fault_mode inter-turn fault"},
    {"edge_id": "EU3F5TIE_E100", "edge_description": "inductor has_fault_mode open circuit fault"},
    {"edge_id": "EU3F5TIE_E101", "edge_description": "inductor has_fault_mode short circuit fault"},
    {"edge_id": "EU3F5TIE_E102", "edge_description": "inductor has_fault_mode aging"},
    {"edge_id": "EU3F5TIE_E103", "edge_description": "inductor has_fault_mode inter-turn fault"},
    {"edge_id": "EU3F5TIE_E104", "edge_description": "open circuit fault contains 0.5 ohm resistor, 20% inductance reduction"},
    {"edge_id": "EU3F5TIE_E105", "edge_description": "short circuit fault contains 0.5 ohm resistor, 20% inductance reduction"},
    {"edge_id": "EU3F5TIE_E106", "edge_description": "aging contains 0.5 ohm resistor, 20% inductance reduction"},
    {"edge_id": "EU3F5TIE_E107", "edge_description": "inter-turn fault contains 0.5 ohm resistor, 20% inductance reduction"},
    {"edge_id": "EU3F5TIE_E108", "edge_description": "non-isolated DC-DC converter contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E109", "edge_description": "power switch contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E110", "edge_description": "diode contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E111", "edge_description": "electrolytic capacitor contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E112", "edge_description": "inductor contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E113", "edge_description": "power switch contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E114", "edge_description": "diode contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E115", "edge_description": "capacitor contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E116", "edge_description": "inductor contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E117", "edge_description": "open circuit fault contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E118", "edge_description": "short circuit fault contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E119", "edge_description": "aging contains_phm_task online fault diagnosis and aging monitoring"}
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
| 1 | `EU3F5TIE_E090` | `has_fault_mode` | 04-Fault Location | power switch |  | 05-Fault Mode | aging |  |
| 2 | `EU3F5TIE_E091` | `has_fault_mode` | 04-Fault Location | power switch |  | 05-Fault Mode | inter-turn fault |  |
| 3 | `EU3F5TIE_E092` | `has_fault_mode` | 04-Fault Location | diode |  | 05-Fault Mode | open circuit fault |  |
| 4 | `EU3F5TIE_E093` | `has_fault_mode` | 04-Fault Location | diode |  | 05-Fault Mode | short circuit fault |  |
| 5 | `EU3F5TIE_E094` | `has_fault_mode` | 04-Fault Location | diode |  | 05-Fault Mode | aging |  |
| 6 | `EU3F5TIE_E095` | `has_fault_mode` | 04-Fault Location | diode |  | 05-Fault Mode | inter-turn fault |  |
| 7 | `EU3F5TIE_E096` | `has_fault_mode` | 04-Fault Location | capacitor |  | 05-Fault Mode | open circuit fault |  |
| 8 | `EU3F5TIE_E097` | `has_fault_mode` | 04-Fault Location | capacitor |  | 05-Fault Mode | short circuit fault |  |
| 9 | `EU3F5TIE_E098` | `has_fault_mode` | 04-Fault Location | capacitor |  | 05-Fault Mode | aging |  |
| 10 | `EU3F5TIE_E099` | `has_fault_mode` | 04-Fault Location | capacitor |  | 05-Fault Mode | inter-turn fault |  |
| 11 | `EU3F5TIE_E100` | `has_fault_mode` | 04-Fault Location | inductor |  | 05-Fault Mode | open circuit fault |  |
| 12 | `EU3F5TIE_E101` | `has_fault_mode` | 04-Fault Location | inductor |  | 05-Fault Mode | short circuit fault |  |
| 13 | `EU3F5TIE_E102` | `has_fault_mode` | 04-Fault Location | inductor |  | 05-Fault Mode | aging |  |
| 14 | `EU3F5TIE_E103` | `has_fault_mode` | 04-Fault Location | inductor |  | 05-Fault Mode | inter-turn fault |  |
| 15 | `EU3F5TIE_E104` | `contains` | 05-Fault Mode | open circuit fault |  | 06-Fault Severity | 0.5 ohm resistor, 20% inductance reduction(Single Severity) |  |
| 16 | `EU3F5TIE_E105` | `contains` | 05-Fault Mode | short circuit fault |  | 06-Fault Severity | 0.5 ohm resistor, 20% inductance reduction(Single Severity) |  |
| 17 | `EU3F5TIE_E106` | `contains` | 05-Fault Mode | aging |  | 06-Fault Severity | 0.5 ohm resistor, 20% inductance reduction(Single Severity) |  |
| 18 | `EU3F5TIE_E107` | `contains` | 05-Fault Mode | inter-turn fault |  | 06-Fault Severity | 0.5 ohm resistor, 20% inductance reduction(Single Severity) |  |
| 19 | `EU3F5TIE_E108` | `contains_phm_task` | 02-Object Type | non-isolated DC-DC converter |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 20 | `EU3F5TIE_E109` | `contains_phm_task` | 02-Object Type | power switch |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 21 | `EU3F5TIE_E110` | `contains_phm_task` | 02-Object Type | diode |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 22 | `EU3F5TIE_E111` | `contains_phm_task` | 02-Object Type | electrolytic capacitor |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 23 | `EU3F5TIE_E112` | `contains_phm_task` | 02-Object Type | inductor |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 24 | `EU3F5TIE_E113` | `contains_phm_task` | 04-Fault Location | power switch |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 25 | `EU3F5TIE_E114` | `contains_phm_task` | 04-Fault Location | diode |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 26 | `EU3F5TIE_E115` | `contains_phm_task` | 04-Fault Location | capacitor |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 27 | `EU3F5TIE_E116` | `contains_phm_task` | 04-Fault Location | inductor |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 28 | `EU3F5TIE_E117` | `contains_phm_task` | 05-Fault Mode | open circuit fault |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 29 | `EU3F5TIE_E118` | `contains_phm_task` | 05-Fault Mode | short circuit fault |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 30 | `EU3F5TIE_E119` | `contains_phm_task` | 05-Fault Mode | aging |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
