# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：LSBUDAE9
- **Paper Title**：Highly Accurate Machine Fault Diagnosis Using Deep Transfer Learning
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `LSBUDAE9`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "LSBUDAE9_E131", "edge_description": "Gearbox Dataset can be used for machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E132", "edge_description": "induction motors has_fault_mode stator winding defect (3 turns shorted)"},
    {"edge_id": "LSBUDAE9_E133", "edge_description": "induction motors has_fault_mode unbalanced rotor"},
    {"edge_id": "LSBUDAE9_E134", "edge_description": "induction motors has_fault_mode broken bar, miss"},
    {"edge_id": "LSBUDAE9_E135", "edge_description": "induction motors has_fault_mode crack, chipped, root crack"},
    {"edge_id": "LSBUDAE9_E136", "edge_description": "induction motors has_fault_mode surface wear"},
    {"edge_id": "LSBUDAE9_E137", "edge_description": "bearings has_fault_mode stator winding defect (3 turns shorted)"},
    {"edge_id": "LSBUDAE9_E138", "edge_description": "bearings has_fault_mode unbalanced rotor"},
    {"edge_id": "LSBUDAE9_E139", "edge_description": "bearings has_fault_mode broken bar, miss"},
    {"edge_id": "LSBUDAE9_E140", "edge_description": "bearings has_fault_mode crack, chipped, root crack"},
    {"edge_id": "LSBUDAE9_E141", "edge_description": "bearings has_fault_mode surface wear"},
    {"edge_id": "LSBUDAE9_E142", "edge_description": "gearboxes has_fault_mode stator winding defect (3 turns shorted)"},
    {"edge_id": "LSBUDAE9_E143", "edge_description": "gearboxes has_fault_mode unbalanced rotor"},
    {"edge_id": "LSBUDAE9_E144", "edge_description": "gearboxes has_fault_mode broken bar, miss"},
    {"edge_id": "LSBUDAE9_E145", "edge_description": "gearboxes has_fault_mode crack, chipped, root crack"},
    {"edge_id": "LSBUDAE9_E146", "edge_description": "gearboxes has_fault_mode surface wear"},
    {"edge_id": "LSBUDAE9_E147", "edge_description": "stator winding defect (3 turns shorted) contains fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches"},
    {"edge_id": "LSBUDAE9_E148", "edge_description": "unbalanced rotor contains fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches"},
    {"edge_id": "LSBUDAE9_E149", "edge_description": "broken bar, miss contains fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches"},
    {"edge_id": "LSBUDAE9_E150", "edge_description": "crack, chipped, root crack contains fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches"},
    {"edge_id": "LSBUDAE9_E151", "edge_description": "surface wear contains fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches"},
    {"edge_id": "LSBUDAE9_E152", "edge_description": "induction motors contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E153", "edge_description": "bearings contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E154", "edge_description": "gearboxes contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E155", "edge_description": "induction motors contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E156", "edge_description": "bearings contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E157", "edge_description": "gearboxes contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E158", "edge_description": "stator winding defect (3 turns shorted) contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E159", "edge_description": "unbalanced rotor contains_phm_task machine fault diagnosis / fault classification"},
    {"edge_id": "LSBUDAE9_E160", "edge_description": "broken bar, miss contains_phm_task machine fault diagnosis / fault classification"}
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
| 1 | `LSBUDAE9_E131` | `can be used for` | 10-Dataset | Gearbox Dataset |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 2 | `LSBUDAE9_E132` | `has_fault_mode` | 04-Fault Location | induction motors |  | 05-Fault Mode | stator winding defect (3 turns shorted) |  |
| 3 | `LSBUDAE9_E133` | `has_fault_mode` | 04-Fault Location | induction motors |  | 05-Fault Mode | unbalanced rotor |  |
| 4 | `LSBUDAE9_E134` | `has_fault_mode` | 04-Fault Location | induction motors |  | 05-Fault Mode | broken bar, miss |  |
| 5 | `LSBUDAE9_E135` | `has_fault_mode` | 04-Fault Location | induction motors |  | 05-Fault Mode | crack, chipped, root crack |  |
| 6 | `LSBUDAE9_E136` | `has_fault_mode` | 04-Fault Location | induction motors |  | 05-Fault Mode | surface wear |  |
| 7 | `LSBUDAE9_E137` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | stator winding defect (3 turns shorted) |  |
| 8 | `LSBUDAE9_E138` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | unbalanced rotor |  |
| 9 | `LSBUDAE9_E139` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | broken bar, miss |  |
| 10 | `LSBUDAE9_E140` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | crack, chipped, root crack |  |
| 11 | `LSBUDAE9_E141` | `has_fault_mode` | 04-Fault Location | bearings |  | 05-Fault Mode | surface wear |  |
| 12 | `LSBUDAE9_E142` | `has_fault_mode` | 04-Fault Location | gearboxes |  | 05-Fault Mode | stator winding defect (3 turns shorted) |  |
| 13 | `LSBUDAE9_E143` | `has_fault_mode` | 04-Fault Location | gearboxes |  | 05-Fault Mode | unbalanced rotor |  |
| 14 | `LSBUDAE9_E144` | `has_fault_mode` | 04-Fault Location | gearboxes |  | 05-Fault Mode | broken bar, miss |  |
| 15 | `LSBUDAE9_E145` | `has_fault_mode` | 04-Fault Location | gearboxes |  | 05-Fault Mode | crack, chipped, root crack |  |
| 16 | `LSBUDAE9_E146` | `has_fault_mode` | 04-Fault Location | gearboxes |  | 05-Fault Mode | surface wear |  |
| 17 | `LSBUDAE9_E147` | `contains` | 05-Fault Mode | stator winding defect (3 turns shorted) |  | 06-Fault Severity | fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches(Multiple Severities) |  |
| 18 | `LSBUDAE9_E148` | `contains` | 05-Fault Mode | unbalanced rotor |  | 06-Fault Severity | fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches(Multiple Severities) |  |
| 19 | `LSBUDAE9_E149` | `contains` | 05-Fault Mode | broken bar, miss |  | 06-Fault Severity | fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches(Multiple Severities) |  |
| 20 | `LSBUDAE9_E150` | `contains` | 05-Fault Mode | crack, chipped, root crack |  | 06-Fault Severity | fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches(Multiple Severities) |  |
| 21 | `LSBUDAE9_E151` | `contains` | 05-Fault Mode | surface wear |  | 06-Fault Severity | fault diameters of 0.007 inches, 0.014 inches, and 0.021 inches(Multiple Severities) |  |
| 22 | `LSBUDAE9_E152` | `contains_phm_task` | 02-Object Type | induction motors |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 23 | `LSBUDAE9_E153` | `contains_phm_task` | 02-Object Type | bearings |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 24 | `LSBUDAE9_E154` | `contains_phm_task` | 02-Object Type | gearboxes |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 25 | `LSBUDAE9_E155` | `contains_phm_task` | 04-Fault Location | induction motors |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 26 | `LSBUDAE9_E156` | `contains_phm_task` | 04-Fault Location | bearings |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 27 | `LSBUDAE9_E157` | `contains_phm_task` | 04-Fault Location | gearboxes |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 28 | `LSBUDAE9_E158` | `contains_phm_task` | 05-Fault Mode | stator winding defect (3 turns shorted) |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 29 | `LSBUDAE9_E159` | `contains_phm_task` | 05-Fault Mode | unbalanced rotor |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |
| 30 | `LSBUDAE9_E160` | `contains_phm_task` | 05-Fault Mode | broken bar, miss |  | 08-PHM Task | machine fault diagnosis / fault classification(Diagnosis Task) |  |

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
