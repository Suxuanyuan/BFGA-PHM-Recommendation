# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：VLSM3MA7
- **Paper Title**：Joint pairwise graph embedded sparse deep belief network for fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `VLSM3MA7`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "VLSM3MA7_E136", "edge_description": "chipping tips contains four different levels of severity, 7 mils, 21 mils"},
    {"edge_id": "VLSM3MA7_E137", "edge_description": "damage contains four different levels of severity, 7 mils, 21 mils"},
    {"edge_id": "VLSM3MA7_E138", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E139", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E140", "edge_description": "pinion contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E141", "edge_description": "inner race contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E142", "edge_description": "ball contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E143", "edge_description": "outer raceway contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E144", "edge_description": "missing tooth contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E145", "edge_description": "root crack contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E146", "edge_description": "spalling contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E147", "edge_description": "chipping tips contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E148", "edge_description": "damage contains_phm_task fault diagnosis"},
    {"edge_id": "VLSM3MA7_E150", "edge_description": "gearbox induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E151", "edge_description": "gearbox induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E152", "edge_description": "bearing induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E153", "edge_description": "bearing induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E154", "edge_description": "constant operating conditions induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E155", "edge_description": "constant operating conditions induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E156", "edge_description": "four different levels of severity, 7 mils, 21 mils induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E157", "edge_description": "four different levels of severity, 7 mils, 21 mils induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E158", "edge_description": "No Compound Fault induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E159", "edge_description": "No Compound Fault induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E160", "edge_description": "fault diagnosis induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E161", "edge_description": "fault diagnosis induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E162", "edge_description": "60% of 104 samples per condition for gearbox, 80% of 500 samples per class for bearings induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E163", "edge_description": "60% of 104 samples per condition for gearbox, 80% of 500 samples per class for bearings induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E164", "edge_description": "not mentioned induces_problem extract the intrinsic information of the object from a large amount of interference"},
    {"edge_id": "VLSM3MA7_E165", "edge_description": "not mentioned induces_problem gradient diffusion and local optimal in supervised learning"},
    {"edge_id": "VLSM3MA7_E166", "edge_description": "proposed models may increase training time due to the increase in parameters from regularization induces_problem extract the intrinsic information of the object from a large amount of interference"}
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
| 1 | `VLSM3MA7_E136` | `contains` | 05-Fault Mode | chipping tips |  | 06-Fault Severity | four different levels of severity, 7 mils, 21 mils(Multiple Severities) |  |
| 2 | `VLSM3MA7_E137` | `contains` | 05-Fault Mode | damage |  | 06-Fault Severity | four different levels of severity, 7 mils, 21 mils(Multiple Severities) |  |
| 3 | `VLSM3MA7_E138` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 4 | `VLSM3MA7_E139` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 5 | `VLSM3MA7_E140` | `contains_phm_task` | 04-Fault Location | pinion |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 6 | `VLSM3MA7_E141` | `contains_phm_task` | 04-Fault Location | inner race |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 7 | `VLSM3MA7_E142` | `contains_phm_task` | 04-Fault Location | ball |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 8 | `VLSM3MA7_E143` | `contains_phm_task` | 04-Fault Location | outer raceway |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 9 | `VLSM3MA7_E144` | `contains_phm_task` | 05-Fault Mode | missing tooth |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `VLSM3MA7_E145` | `contains_phm_task` | 05-Fault Mode | root crack |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `VLSM3MA7_E146` | `contains_phm_task` | 05-Fault Mode | spalling |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `VLSM3MA7_E147` | `contains_phm_task` | 05-Fault Mode | chipping tips |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `VLSM3MA7_E148` | `contains_phm_task` | 05-Fault Mode | damage |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `VLSM3MA7_E150` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 15 | `VLSM3MA7_E151` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 16 | `VLSM3MA7_E152` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 17 | `VLSM3MA7_E153` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 18 | `VLSM3MA7_E154` | `induces_problem` | 03-Operating Conditions | constant operating conditions(Single Condition) |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 19 | `VLSM3MA7_E155` | `induces_problem` | 03-Operating Conditions | constant operating conditions(Single Condition) |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 20 | `VLSM3MA7_E156` | `induces_problem` | 06-Fault Severity | four different levels of severity, 7 mils, 21 mils(Multiple Severities) |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 21 | `VLSM3MA7_E157` | `induces_problem` | 06-Fault Severity | four different levels of severity, 7 mils, 21 mils(Multiple Severities) |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 22 | `VLSM3MA7_E158` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 23 | `VLSM3MA7_E159` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 24 | `VLSM3MA7_E160` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 25 | `VLSM3MA7_E161` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 26 | `VLSM3MA7_E162` | `induces_problem` | 12-Training Data Availability | 60% of 104 samples per condition for gearbox, 80% of 500 samples per class for bearings(Sufficient) |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 27 | `VLSM3MA7_E163` | `induces_problem` | 12-Training Data Availability | 60% of 104 samples per condition for gearbox, 80% of 500 samples per class for bearings(Sufficient) |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 28 | `VLSM3MA7_E164` | `induces_problem` | 13-Noise Level | not mentioned(Normal) |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |
| 29 | `VLSM3MA7_E165` | `induces_problem` | 13-Noise Level | not mentioned(Normal) |  | 09-Problem Scenario | gradient diffusion and local optimal in supervised learning(Other) |  |
| 30 | `VLSM3MA7_E166` | `induces_problem` | 14-Computational Resource | proposed models may increase training time due to the increase in parameters from regularization(High Resource Consumption) |  | 09-Problem Scenario | extract the intrinsic information of the object from a large amount of interference(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
