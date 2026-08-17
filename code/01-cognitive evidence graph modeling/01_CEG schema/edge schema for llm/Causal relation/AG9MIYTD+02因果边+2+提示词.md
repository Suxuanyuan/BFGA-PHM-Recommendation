# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AG9MIYTD
- **Paper Title**：Implementation of VLSI model as a tool in diagnostics of slowly varying process parameters which affect the performance of steam turbine
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AG9MIYTD`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AG9MIYTD_E080", "edge_description": "IP turbine has_fault_mode deposits"},
    {"edge_id": "AG9MIYTD_E081", "edge_description": "IP turbine has_fault_mode peening"},
    {"edge_id": "AG9MIYTD_E082", "edge_description": "IP turbine has_fault_mode rubs"},
    {"edge_id": "AG9MIYTD_E083", "edge_description": "IP turbine has_fault_mode damages"},
    {"edge_id": "AG9MIYTD_E084", "edge_description": "LP turbine has_fault_mode solid particle erosion"},
    {"edge_id": "AG9MIYTD_E085", "edge_description": "LP turbine has_fault_mode deposits"},
    {"edge_id": "AG9MIYTD_E086", "edge_description": "LP turbine has_fault_mode peening"},
    {"edge_id": "AG9MIYTD_E087", "edge_description": "LP turbine has_fault_mode rubs"},
    {"edge_id": "AG9MIYTD_E088", "edge_description": "LP turbine has_fault_mode damages"},
    {"edge_id": "AG9MIYTD_E089", "edge_description": "solid particle erosion contains Single Severity"},
    {"edge_id": "AG9MIYTD_E090", "edge_description": "deposits contains Single Severity"},
    {"edge_id": "AG9MIYTD_E091", "edge_description": "peening contains Single Severity"},
    {"edge_id": "AG9MIYTD_E092", "edge_description": "rubs contains Single Severity"},
    {"edge_id": "AG9MIYTD_E093", "edge_description": "damages contains Single Severity"},
    {"edge_id": "AG9MIYTD_E095", "edge_description": "HP turbine contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E096", "edge_description": "IP turbine contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E097", "edge_description": "LP turbine contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E098", "edge_description": "solid particle erosion contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E099", "edge_description": "deposits contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E100", "edge_description": "peening contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E101", "edge_description": "rubs contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E102", "edge_description": "damages contains_phm_task fault diagnosis"},
    {"edge_id": "AG9MIYTD_E104", "edge_description": "steam turbine induces_problem slowly happening and accumulating physical phenomena"},
    {"edge_id": "AG9MIYTD_E105", "edge_description": "steam turbine induces_problem noisy data"},
    {"edge_id": "AG9MIYTD_E106", "edge_description": "steam turbine induces_problem strong interactions between measurements"},
    {"edge_id": "AG9MIYTD_E107", "edge_description": "500 MW, 400 MW and 300 MW induces_problem slowly happening and accumulating physical phenomena"},
    {"edge_id": "AG9MIYTD_E108", "edge_description": "500 MW, 400 MW and 300 MW induces_problem noisy data"},
    {"edge_id": "AG9MIYTD_E109", "edge_description": "500 MW, 400 MW and 300 MW induces_problem strong interactions between measurements"},
    {"edge_id": "AG9MIYTD_E110", "edge_description": "Single Severity induces_problem slowly happening and accumulating physical phenomena"},
    {"edge_id": "AG9MIYTD_E111", "edge_description": "Single Severity induces_problem noisy data"}
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
| 1 | `AG9MIYTD_E080` | `has_fault_mode` | 04-Fault Location | IP turbine |  | 05-Fault Mode | deposits |  |
| 2 | `AG9MIYTD_E081` | `has_fault_mode` | 04-Fault Location | IP turbine |  | 05-Fault Mode | peening |  |
| 3 | `AG9MIYTD_E082` | `has_fault_mode` | 04-Fault Location | IP turbine |  | 05-Fault Mode | rubs |  |
| 4 | `AG9MIYTD_E083` | `has_fault_mode` | 04-Fault Location | IP turbine |  | 05-Fault Mode | damages |  |
| 5 | `AG9MIYTD_E084` | `has_fault_mode` | 04-Fault Location | LP turbine |  | 05-Fault Mode | solid particle erosion |  |
| 6 | `AG9MIYTD_E085` | `has_fault_mode` | 04-Fault Location | LP turbine |  | 05-Fault Mode | deposits |  |
| 7 | `AG9MIYTD_E086` | `has_fault_mode` | 04-Fault Location | LP turbine |  | 05-Fault Mode | peening |  |
| 8 | `AG9MIYTD_E087` | `has_fault_mode` | 04-Fault Location | LP turbine |  | 05-Fault Mode | rubs |  |
| 9 | `AG9MIYTD_E088` | `has_fault_mode` | 04-Fault Location | LP turbine |  | 05-Fault Mode | damages |  |
| 10 | `AG9MIYTD_E089` | `contains` | 05-Fault Mode | solid particle erosion |  | 06-Fault Severity | Single Severity |  |
| 11 | `AG9MIYTD_E090` | `contains` | 05-Fault Mode | deposits |  | 06-Fault Severity | Single Severity |  |
| 12 | `AG9MIYTD_E091` | `contains` | 05-Fault Mode | peening |  | 06-Fault Severity | Single Severity |  |
| 13 | `AG9MIYTD_E092` | `contains` | 05-Fault Mode | rubs |  | 06-Fault Severity | Single Severity |  |
| 14 | `AG9MIYTD_E093` | `contains` | 05-Fault Mode | damages |  | 06-Fault Severity | Single Severity |  |
| 15 | `AG9MIYTD_E095` | `contains_phm_task` | 04-Fault Location | HP turbine |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `AG9MIYTD_E096` | `contains_phm_task` | 04-Fault Location | IP turbine |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `AG9MIYTD_E097` | `contains_phm_task` | 04-Fault Location | LP turbine |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `AG9MIYTD_E098` | `contains_phm_task` | 05-Fault Mode | solid particle erosion |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `AG9MIYTD_E099` | `contains_phm_task` | 05-Fault Mode | deposits |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `AG9MIYTD_E100` | `contains_phm_task` | 05-Fault Mode | peening |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `AG9MIYTD_E101` | `contains_phm_task` | 05-Fault Mode | rubs |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `AG9MIYTD_E102` | `contains_phm_task` | 05-Fault Mode | damages |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 23 | `AG9MIYTD_E104` | `induces_problem` | 02-Object Type | steam turbine |  | 09-Problem Scenario | slowly happening and accumulating physical phenomena(Early Degradation Prediction) |  |
| 24 | `AG9MIYTD_E105` | `induces_problem` | 02-Object Type | steam turbine |  | 09-Problem Scenario | noisy data(Uncertainty) |  |
| 25 | `AG9MIYTD_E106` | `induces_problem` | 02-Object Type | steam turbine |  | 09-Problem Scenario | strong interactions between measurements(Complex Systems) |  |
| 26 | `AG9MIYTD_E107` | `induces_problem` | 03-Operating Conditions | 500 MW, 400 MW and 300 MW(Multiple Conditions) |  | 09-Problem Scenario | slowly happening and accumulating physical phenomena(Early Degradation Prediction) |  |
| 27 | `AG9MIYTD_E108` | `induces_problem` | 03-Operating Conditions | 500 MW, 400 MW and 300 MW(Multiple Conditions) |  | 09-Problem Scenario | noisy data(Uncertainty) |  |
| 28 | `AG9MIYTD_E109` | `induces_problem` | 03-Operating Conditions | 500 MW, 400 MW and 300 MW(Multiple Conditions) |  | 09-Problem Scenario | strong interactions between measurements(Complex Systems) |  |
| 29 | `AG9MIYTD_E110` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | slowly happening and accumulating physical phenomena(Early Degradation Prediction) |  |
| 30 | `AG9MIYTD_E111` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | noisy data(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
