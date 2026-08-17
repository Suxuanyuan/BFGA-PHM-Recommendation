# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：BY4JBS4C
- **Paper Title**：Electric Motor Fault Detection and Diagnosis by Kernel Density Estimation and Kullback-Leibler Divergence Based on Stator Current Measurements
- **Number of Candidate Edges to Judge**：22 

---

## II. LLM Input

> **Input Material**: Reference ID `BY4JBS4C`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "BY4JBS4C_E091", "edge_description": "single-phase motor contains_phm_task fault detection and diagnosis"},
    {"edge_id": "BY4JBS4C_E092", "edge_description": "cracked rotor contains_phm_task fault detection and diagnosis"},
    {"edge_id": "BY4JBS4C_E093", "edge_description": "out-of-tolerance geometry rotor contains_phm_task fault detection and diagnosis"},
    {"edge_id": "BY4JBS4C_E094", "edge_description": "backlash contains_phm_task fault detection and diagnosis"},
    {"edge_id": "BY4JBS4C_E096", "edge_description": "asynchronous induction motor induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E097", "edge_description": "asynchronous induction motor induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E098", "edge_description": "single-phase motor induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E099", "edge_description": "single-phase motor induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E100", "edge_description": "different load and voltage levels induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E101", "edge_description": "different load and voltage levels induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E102", "edge_description": "Single Severity induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E103", "edge_description": "Single Severity induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E104", "edge_description": "No Compound Fault induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E105", "edge_description": "No Compound Fault induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E106", "edge_description": "fault detection and diagnosis induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E107", "edge_description": "fault detection and diagnosis induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E108", "edge_description": "Ten motors for each faulty case and for the healthy cases are tested. ... 1000 Monte Carlo simulations induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E109", "edge_description": "Ten motors for each faulty case and for the healthy cases are tested. ... 1000 Monte Carlo simulations induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E110", "edge_description": "The signature obtained is robust to disturbances induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E111", "edge_description": "The signature obtained is robust to disturbances induces_problem uncertainties and disturbances in current signals"},
    {"edge_id": "BY4JBS4C_E112", "edge_description": "KDE is improved by fast Gaussian transform and a points reduction procedure. Since these techniques achieve a remarkable computational cost reduction with respect to the standard KDE, the algorithm can be used online. induces_problem online monitoring computational cost"},
    {"edge_id": "BY4JBS4C_E113", "edge_description": "KDE is improved by fast Gaussian transform and a points reduction procedure. Since these techniques achieve a remarkable computational cost reduction with respect to the standard KDE, the algorithm can be used online. induces_problem uncertainties and disturbances in current signals"}
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
| 1 | `BY4JBS4C_E091` | `contains_phm_task` | 04-Fault Location | single-phase motor |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 2 | `BY4JBS4C_E092` | `contains_phm_task` | 05-Fault Mode | cracked rotor |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 3 | `BY4JBS4C_E093` | `contains_phm_task` | 05-Fault Mode | out-of-tolerance geometry rotor |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 4 | `BY4JBS4C_E094` | `contains_phm_task` | 05-Fault Mode | backlash |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 5 | `BY4JBS4C_E096` | `induces_problem` | 02-Object Type | asynchronous induction motor |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 6 | `BY4JBS4C_E097` | `induces_problem` | 02-Object Type | asynchronous induction motor |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 7 | `BY4JBS4C_E098` | `induces_problem` | 02-Object Type | single-phase motor |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 8 | `BY4JBS4C_E099` | `induces_problem` | 02-Object Type | single-phase motor |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 9 | `BY4JBS4C_E100` | `induces_problem` | 03-Operating Conditions | different load and voltage levels(Multiple Conditions) |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 10 | `BY4JBS4C_E101` | `induces_problem` | 03-Operating Conditions | different load and voltage levels(Multiple Conditions) |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 11 | `BY4JBS4C_E102` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 12 | `BY4JBS4C_E103` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 13 | `BY4JBS4C_E104` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 14 | `BY4JBS4C_E105` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 15 | `BY4JBS4C_E106` | `induces_problem` | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 16 | `BY4JBS4C_E107` | `induces_problem` | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 17 | `BY4JBS4C_E108` | `induces_problem` | 12-Training Data Availability | Ten motors for each faulty case and for the healthy cases are tested. ... 1000 Monte Carlo simulations(Sufficient) |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 18 | `BY4JBS4C_E109` | `induces_problem` | 12-Training Data Availability | Ten motors for each faulty case and for the healthy cases are tested. ... 1000 Monte Carlo simulations(Sufficient) |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 19 | `BY4JBS4C_E110` | `induces_problem` | 13-Noise Level | The signature obtained is robust to disturbances(Normal) |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 20 | `BY4JBS4C_E111` | `induces_problem` | 13-Noise Level | The signature obtained is robust to disturbances(Normal) |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |
| 21 | `BY4JBS4C_E112` | `induces_problem` | 14-Computational Resource | KDE is improved by fast Gaussian transform and a points reduction procedure. Since these techniques achieve a remarkable computational cost reduction with respect to the standard KDE, the algorithm can be used online.(Low Resource Consumption) |  | 09-Problem Scenario | online monitoring computational cost(Other) |  |
| 22 | `BY4JBS4C_E113` | `induces_problem` | 14-Computational Resource | KDE is improved by fast Gaussian transform and a points reduction procedure. Since these techniques achieve a remarkable computational cost reduction with respect to the standard KDE, the algorithm can be used online.(Low Resource Consumption) |  | 09-Problem Scenario | uncertainties and disturbances in current signals(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 22 edges)*
