# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：UWKDAGPF
- **Paper Title**：A novel multi-agent approach to identify faults in line connected three-phase induction motors
- **Number of Candidate Edges to Judge**：28 

---

## II. LLM Input

> **Input Material**: Reference ID `UWKDAGPF`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "UWKDAGPF_E076", "edge_description": "bearing has_fault_mode short-circuit"},
    {"edge_id": "UWKDAGPF_E077", "edge_description": "bearing has_fault_mode broken rotor bar"},
    {"edge_id": "UWKDAGPF_E078", "edge_description": "bearing has_fault_mode excessive wear"},
    {"edge_id": "UWKDAGPF_E079", "edge_description": "bearing has_fault_mode grooves"},
    {"edge_id": "UWKDAGPF_E080", "edge_description": "bearing has_fault_mode electric shock"},
    {"edge_id": "UWKDAGPF_E081", "edge_description": "bearing has_fault_mode defect in the spheres"},
    {"edge_id": "UWKDAGPF_E082", "edge_description": "short-circuit contains short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars"},
    {"edge_id": "UWKDAGPF_E083", "edge_description": "broken rotor bar contains short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars"},
    {"edge_id": "UWKDAGPF_E084", "edge_description": "excessive wear contains short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars"},
    {"edge_id": "UWKDAGPF_E085", "edge_description": "grooves contains short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars"},
    {"edge_id": "UWKDAGPF_E086", "edge_description": "electric shock contains short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars"},
    {"edge_id": "UWKDAGPF_E087", "edge_description": "defect in the spheres contains short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars"},
    {"edge_id": "UWKDAGPF_E089", "edge_description": "stator winding contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E090", "edge_description": "rotor bar contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E091", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E092", "edge_description": "short-circuit contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E093", "edge_description": "broken rotor bar contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E094", "edge_description": "excessive wear contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E095", "edge_description": "grooves contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E096", "edge_description": "electric shock contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E097", "edge_description": "defect in the spheres contains_phm_task fault diagnosis"},
    {"edge_id": "UWKDAGPF_E099", "edge_description": "three-phase induction motor induces_problem generalization across different motor powers"},
    {"edge_id": "UWKDAGPF_E100", "edge_description": "various sinusoidal power and mechanical load conditions induces_problem generalization across different motor powers"},
    {"edge_id": "UWKDAGPF_E101", "edge_description": "short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars induces_problem generalization across different motor powers"},
    {"edge_id": "UWKDAGPF_E102", "edge_description": "No Compound Fault induces_problem generalization across different motor powers"},
    {"edge_id": "UWKDAGPF_E103", "edge_description": "fault diagnosis induces_problem generalization across different motor powers"},
    {"edge_id": "UWKDAGPF_E104", "edge_description": "960 sample signals gathered from the 1 hp motors induces_problem generalization across different motor powers"},
    {"edge_id": "UWKDAGPF_E105", "edge_description": "Normal induces_problem generalization across different motor powers"}
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
| 1 | `UWKDAGPF_E076` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | short-circuit |  |
| 2 | `UWKDAGPF_E077` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | broken rotor bar |  |
| 3 | `UWKDAGPF_E078` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | excessive wear |  |
| 4 | `UWKDAGPF_E079` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | grooves |  |
| 5 | `UWKDAGPF_E080` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | electric shock |  |
| 6 | `UWKDAGPF_E081` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | defect in the spheres |  |
| 7 | `UWKDAGPF_E082` | `contains` | 05-Fault Mode | short-circuit |  | 06-Fault Severity | short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars(Multiple Severities) |  |
| 8 | `UWKDAGPF_E083` | `contains` | 05-Fault Mode | broken rotor bar |  | 06-Fault Severity | short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars(Multiple Severities) |  |
| 9 | `UWKDAGPF_E084` | `contains` | 05-Fault Mode | excessive wear |  | 06-Fault Severity | short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars(Multiple Severities) |  |
| 10 | `UWKDAGPF_E085` | `contains` | 05-Fault Mode | grooves |  | 06-Fault Severity | short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars(Multiple Severities) |  |
| 11 | `UWKDAGPF_E086` | `contains` | 05-Fault Mode | electric shock |  | 06-Fault Severity | short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars(Multiple Severities) |  |
| 12 | `UWKDAGPF_E087` | `contains` | 05-Fault Mode | defect in the spheres |  | 06-Fault Severity | short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars(Multiple Severities) |  |
| 13 | `UWKDAGPF_E089` | `contains_phm_task` | 04-Fault Location | stator winding |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `UWKDAGPF_E090` | `contains_phm_task` | 04-Fault Location | rotor bar |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `UWKDAGPF_E091` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `UWKDAGPF_E092` | `contains_phm_task` | 05-Fault Mode | short-circuit |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `UWKDAGPF_E093` | `contains_phm_task` | 05-Fault Mode | broken rotor bar |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `UWKDAGPF_E094` | `contains_phm_task` | 05-Fault Mode | excessive wear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `UWKDAGPF_E095` | `contains_phm_task` | 05-Fault Mode | grooves |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `UWKDAGPF_E096` | `contains_phm_task` | 05-Fault Mode | electric shock |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `UWKDAGPF_E097` | `contains_phm_task` | 05-Fault Mode | defect in the spheres |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `UWKDAGPF_E099` | `induces_problem` | 02-Object Type | three-phase induction motor |  | 09-Problem Scenario | generalization across different motor powers(Distribution Discrepancy) |  |
| 23 | `UWKDAGPF_E100` | `induces_problem` | 03-Operating Conditions | various sinusoidal power and mechanical load conditions(Multiple Conditions) |  | 09-Problem Scenario | generalization across different motor powers(Distribution Discrepancy) |  |
| 24 | `UWKDAGPF_E101` | `induces_problem` | 06-Fault Severity | short-circuit severity levels: 1%, 3%, 5%, 7%, 10%, 15%, 20%; broken rotor bars: one, two, and four consecutive bars(Multiple Severities) |  | 09-Problem Scenario | generalization across different motor powers(Distribution Discrepancy) |  |
| 25 | `UWKDAGPF_E102` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | generalization across different motor powers(Distribution Discrepancy) |  |
| 26 | `UWKDAGPF_E103` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | generalization across different motor powers(Distribution Discrepancy) |  |
| 27 | `UWKDAGPF_E104` | `induces_problem` | 12-Training Data Availability | 960 sample signals gathered from the 1 hp motors(Sufficient) |  | 09-Problem Scenario | generalization across different motor powers(Distribution Discrepancy) |  |
| 28 | `UWKDAGPF_E105` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | generalization across different motor powers(Distribution Discrepancy) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 28 edges)*
