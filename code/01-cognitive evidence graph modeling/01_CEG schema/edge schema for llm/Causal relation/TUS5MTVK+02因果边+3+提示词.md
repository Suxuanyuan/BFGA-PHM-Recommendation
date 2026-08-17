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
    {"edge_id": "TUS5MTVK_E145", "edge_description": "discharge valve has_fault_mode gear wear"},
    {"edge_id": "TUS5MTVK_E146", "edge_description": "discharge valve has_fault_mode discharge valve leakage"},
    {"edge_id": "TUS5MTVK_E147", "edge_description": "discharge valve has_fault_mode transmission belt looseness"},
    {"edge_id": "TUS5MTVK_E148", "edge_description": "discharge valve has_fault_mode intercooler leakage"},
    {"edge_id": "TUS5MTVK_E149", "edge_description": "transmission belt has_fault_mode broken rotor bar"},
    {"edge_id": "TUS5MTVK_E150", "edge_description": "transmission belt has_fault_mode gear wear"},
    {"edge_id": "TUS5MTVK_E151", "edge_description": "transmission belt has_fault_mode discharge valve leakage"},
    {"edge_id": "TUS5MTVK_E152", "edge_description": "transmission belt has_fault_mode transmission belt looseness"},
    {"edge_id": "TUS5MTVK_E153", "edge_description": "transmission belt has_fault_mode intercooler leakage"},
    {"edge_id": "TUS5MTVK_E154", "edge_description": "intercooler has_fault_mode broken rotor bar"},
    {"edge_id": "TUS5MTVK_E155", "edge_description": "intercooler has_fault_mode gear wear"},
    {"edge_id": "TUS5MTVK_E156", "edge_description": "intercooler has_fault_mode discharge valve leakage"},
    {"edge_id": "TUS5MTVK_E157", "edge_description": "intercooler has_fault_mode transmission belt looseness"},
    {"edge_id": "TUS5MTVK_E158", "edge_description": "intercooler has_fault_mode intercooler leakage"},
    {"edge_id": "TUS5MTVK_E159", "edge_description": "broken rotor bar contains half a BRB, one complete bar broken, two continuous broken bars, wear progressions"},
    {"edge_id": "TUS5MTVK_E160", "edge_description": "gear wear contains half a BRB, one complete bar broken, two continuous broken bars, wear progressions"},
    {"edge_id": "TUS5MTVK_E161", "edge_description": "discharge valve leakage contains half a BRB, one complete bar broken, two continuous broken bars, wear progressions"},
    {"edge_id": "TUS5MTVK_E162", "edge_description": "transmission belt looseness contains half a BRB, one complete bar broken, two continuous broken bars, wear progressions"},
    {"edge_id": "TUS5MTVK_E163", "edge_description": "intercooler leakage contains half a BRB, one complete bar broken, two continuous broken bars, wear progressions"},
    {"edge_id": "TUS5MTVK_E164", "edge_description": "induction motor contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E165", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E166", "edge_description": "reciprocating compressor contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E167", "edge_description": "rotor bar contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E168", "edge_description": "gear contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E169", "edge_description": "discharge valve contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E170", "edge_description": "transmission belt contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E171", "edge_description": "intercooler contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E172", "edge_description": "broken rotor bar contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E173", "edge_description": "gear wear contains_phm_task fault diagnosis"},
    {"edge_id": "TUS5MTVK_E174", "edge_description": "discharge valve leakage contains_phm_task fault diagnosis"}
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
| 1 | `TUS5MTVK_E145` | `has_fault_mode` | 04-Fault Location | discharge valve |  | 05-Fault Mode | gear wear |  |
| 2 | `TUS5MTVK_E146` | `has_fault_mode` | 04-Fault Location | discharge valve |  | 05-Fault Mode | discharge valve leakage |  |
| 3 | `TUS5MTVK_E147` | `has_fault_mode` | 04-Fault Location | discharge valve |  | 05-Fault Mode | transmission belt looseness |  |
| 4 | `TUS5MTVK_E148` | `has_fault_mode` | 04-Fault Location | discharge valve |  | 05-Fault Mode | intercooler leakage |  |
| 5 | `TUS5MTVK_E149` | `has_fault_mode` | 04-Fault Location | transmission belt |  | 05-Fault Mode | broken rotor bar |  |
| 6 | `TUS5MTVK_E150` | `has_fault_mode` | 04-Fault Location | transmission belt |  | 05-Fault Mode | gear wear |  |
| 7 | `TUS5MTVK_E151` | `has_fault_mode` | 04-Fault Location | transmission belt |  | 05-Fault Mode | discharge valve leakage |  |
| 8 | `TUS5MTVK_E152` | `has_fault_mode` | 04-Fault Location | transmission belt |  | 05-Fault Mode | transmission belt looseness |  |
| 9 | `TUS5MTVK_E153` | `has_fault_mode` | 04-Fault Location | transmission belt |  | 05-Fault Mode | intercooler leakage |  |
| 10 | `TUS5MTVK_E154` | `has_fault_mode` | 04-Fault Location | intercooler |  | 05-Fault Mode | broken rotor bar |  |
| 11 | `TUS5MTVK_E155` | `has_fault_mode` | 04-Fault Location | intercooler |  | 05-Fault Mode | gear wear |  |
| 12 | `TUS5MTVK_E156` | `has_fault_mode` | 04-Fault Location | intercooler |  | 05-Fault Mode | discharge valve leakage |  |
| 13 | `TUS5MTVK_E157` | `has_fault_mode` | 04-Fault Location | intercooler |  | 05-Fault Mode | transmission belt looseness |  |
| 14 | `TUS5MTVK_E158` | `has_fault_mode` | 04-Fault Location | intercooler |  | 05-Fault Mode | intercooler leakage |  |
| 15 | `TUS5MTVK_E159` | `contains` | 05-Fault Mode | broken rotor bar |  | 06-Fault Severity | half a BRB, one complete bar broken, two continuous broken bars, wear progressions(Multiple Severities) |  |
| 16 | `TUS5MTVK_E160` | `contains` | 05-Fault Mode | gear wear |  | 06-Fault Severity | half a BRB, one complete bar broken, two continuous broken bars, wear progressions(Multiple Severities) |  |
| 17 | `TUS5MTVK_E161` | `contains` | 05-Fault Mode | discharge valve leakage |  | 06-Fault Severity | half a BRB, one complete bar broken, two continuous broken bars, wear progressions(Multiple Severities) |  |
| 18 | `TUS5MTVK_E162` | `contains` | 05-Fault Mode | transmission belt looseness |  | 06-Fault Severity | half a BRB, one complete bar broken, two continuous broken bars, wear progressions(Multiple Severities) |  |
| 19 | `TUS5MTVK_E163` | `contains` | 05-Fault Mode | intercooler leakage |  | 06-Fault Severity | half a BRB, one complete bar broken, two continuous broken bars, wear progressions(Multiple Severities) |  |
| 20 | `TUS5MTVK_E164` | `contains_phm_task` | 02-Object Type | induction motor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `TUS5MTVK_E165` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `TUS5MTVK_E166` | `contains_phm_task` | 02-Object Type | reciprocating compressor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 23 | `TUS5MTVK_E167` | `contains_phm_task` | 04-Fault Location | rotor bar |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 24 | `TUS5MTVK_E168` | `contains_phm_task` | 04-Fault Location | gear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 25 | `TUS5MTVK_E169` | `contains_phm_task` | 04-Fault Location | discharge valve |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 26 | `TUS5MTVK_E170` | `contains_phm_task` | 04-Fault Location | transmission belt |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 27 | `TUS5MTVK_E171` | `contains_phm_task` | 04-Fault Location | intercooler |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 28 | `TUS5MTVK_E172` | `contains_phm_task` | 05-Fault Mode | broken rotor bar |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 29 | `TUS5MTVK_E173` | `contains_phm_task` | 05-Fault Mode | gear wear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 30 | `TUS5MTVK_E174` | `contains_phm_task` | 05-Fault Mode | discharge valve leakage |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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
