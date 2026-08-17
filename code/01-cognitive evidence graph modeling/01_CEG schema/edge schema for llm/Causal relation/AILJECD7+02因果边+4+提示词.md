# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AILJECD7
- **Paper Title**：Fault template extraction to assist operators during industrial alarm floods
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AILJECD7`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AILJECD7_E204", "edge_description": "sensor has_fault_mode broken"},
    {"edge_id": "AILJECD7_E205", "edge_description": "sensor has_fault_mode sensor problem"},
    {"edge_id": "AILJECD7_E206", "edge_description": "leak contains Single Severity"},
    {"edge_id": "AILJECD7_E207", "edge_description": "blockage contains Single Severity"},
    {"edge_id": "AILJECD7_E208", "edge_description": "stoppage contains Single Severity"},
    {"edge_id": "AILJECD7_E209", "edge_description": "broken contains Single Severity"},
    {"edge_id": "AILJECD7_E210", "edge_description": "sensor problem contains Single Severity"},
    {"edge_id": "AILJECD7_E211", "edge_description": "gas system contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E212", "edge_description": "pump contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E213", "edge_description": "mass flow controller contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E214", "edge_description": "bottles contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E215", "edge_description": "Buffer contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E216", "edge_description": "mass flow controllers contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E217", "edge_description": "pump contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E218", "edge_description": "bubblers contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E219", "edge_description": "sensor contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E220", "edge_description": "leak contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E221", "edge_description": "blockage contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E222", "edge_description": "stoppage contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E223", "edge_description": "broken contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E224", "edge_description": "sensor problem contains_phm_task fault isolation / fault diagnosis"},
    {"edge_id": "AILJECD7_E226", "edge_description": "gas system induces_problem alarm floods in complex systems"},
    {"edge_id": "AILJECD7_E227", "edge_description": "gas system induces_problem non-deterministic processes and environmental variation"},
    {"edge_id": "AILJECD7_E228", "edge_description": "pump induces_problem alarm floods in complex systems"},
    {"edge_id": "AILJECD7_E229", "edge_description": "pump induces_problem non-deterministic processes and environmental variation"},
    {"edge_id": "AILJECD7_E230", "edge_description": "mass flow controller induces_problem alarm floods in complex systems"},
    {"edge_id": "AILJECD7_E231", "edge_description": "mass flow controller induces_problem non-deterministic processes and environmental variation"},
    {"edge_id": "AILJECD7_E232", "edge_description": "different operating conditions induces_problem alarm floods in complex systems"},
    {"edge_id": "AILJECD7_E233", "edge_description": "different operating conditions induces_problem non-deterministic processes and environmental variation"},
    {"edge_id": "AILJECD7_E234", "edge_description": "Single Severity induces_problem alarm floods in complex systems"}
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
| 1 | `AILJECD7_E204` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | broken |  |
| 2 | `AILJECD7_E205` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | sensor problem |  |
| 3 | `AILJECD7_E206` | `contains` | 05-Fault Mode | leak |  | 06-Fault Severity | Single Severity |  |
| 4 | `AILJECD7_E207` | `contains` | 05-Fault Mode | blockage |  | 06-Fault Severity | Single Severity |  |
| 5 | `AILJECD7_E208` | `contains` | 05-Fault Mode | stoppage |  | 06-Fault Severity | Single Severity |  |
| 6 | `AILJECD7_E209` | `contains` | 05-Fault Mode | broken |  | 06-Fault Severity | Single Severity |  |
| 7 | `AILJECD7_E210` | `contains` | 05-Fault Mode | sensor problem |  | 06-Fault Severity | Single Severity |  |
| 8 | `AILJECD7_E211` | `contains_phm_task` | 02-Object Type | gas system |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 9 | `AILJECD7_E212` | `contains_phm_task` | 02-Object Type | pump |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 10 | `AILJECD7_E213` | `contains_phm_task` | 02-Object Type | mass flow controller |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 11 | `AILJECD7_E214` | `contains_phm_task` | 04-Fault Location | bottles |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 12 | `AILJECD7_E215` | `contains_phm_task` | 04-Fault Location | Buffer |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 13 | `AILJECD7_E216` | `contains_phm_task` | 04-Fault Location | mass flow controllers |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 14 | `AILJECD7_E217` | `contains_phm_task` | 04-Fault Location | pump |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 15 | `AILJECD7_E218` | `contains_phm_task` | 04-Fault Location | bubblers |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 16 | `AILJECD7_E219` | `contains_phm_task` | 04-Fault Location | sensor |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 17 | `AILJECD7_E220` | `contains_phm_task` | 05-Fault Mode | leak |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 18 | `AILJECD7_E221` | `contains_phm_task` | 05-Fault Mode | blockage |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 19 | `AILJECD7_E222` | `contains_phm_task` | 05-Fault Mode | stoppage |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 20 | `AILJECD7_E223` | `contains_phm_task` | 05-Fault Mode | broken |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 21 | `AILJECD7_E224` | `contains_phm_task` | 05-Fault Mode | sensor problem |  | 08-PHM Task | fault isolation / fault diagnosis(Diagnosis Task) |  |
| 22 | `AILJECD7_E226` | `induces_problem` | 02-Object Type | gas system |  | 09-Problem Scenario | alarm floods in complex systems(Complex Systems) |  |
| 23 | `AILJECD7_E227` | `induces_problem` | 02-Object Type | gas system |  | 09-Problem Scenario | non-deterministic processes and environmental variation(Uncertainty) |  |
| 24 | `AILJECD7_E228` | `induces_problem` | 02-Object Type | pump |  | 09-Problem Scenario | alarm floods in complex systems(Complex Systems) |  |
| 25 | `AILJECD7_E229` | `induces_problem` | 02-Object Type | pump |  | 09-Problem Scenario | non-deterministic processes and environmental variation(Uncertainty) |  |
| 26 | `AILJECD7_E230` | `induces_problem` | 02-Object Type | mass flow controller |  | 09-Problem Scenario | alarm floods in complex systems(Complex Systems) |  |
| 27 | `AILJECD7_E231` | `induces_problem` | 02-Object Type | mass flow controller |  | 09-Problem Scenario | non-deterministic processes and environmental variation(Uncertainty) |  |
| 28 | `AILJECD7_E232` | `induces_problem` | 03-Operating Conditions | different operating conditions(Multiple Conditions) |  | 09-Problem Scenario | alarm floods in complex systems(Complex Systems) |  |
| 29 | `AILJECD7_E233` | `induces_problem` | 03-Operating Conditions | different operating conditions(Multiple Conditions) |  | 09-Problem Scenario | non-deterministic processes and environmental variation(Uncertainty) |  |
| 30 | `AILJECD7_E234` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | alarm floods in complex systems(Complex Systems) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 4, total 30 edges)*
