# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：SJMVC5LY
- **Paper Title**：Wavelet support vector machine and multi-layer perceptron neural network with continues wavelet transform for fault diagnosis of gearboxes
- **Number of Candidate Edges to Judge**：29 

---

## II. LLM Input

> **Input Material**: Reference ID `SJMVC5LY`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "SJMVC5LY_E095", "edge_description": "ball bearing has_fault_mode eccentric gear"},
    {"edge_id": "SJMVC5LY_E096", "edge_description": "ball bearing has_fault_mode inner race fault"},
    {"edge_id": "SJMVC5LY_E097", "edge_description": "ball bearing has_fault_mode outer race fault"},
    {"edge_id": "SJMVC5LY_E098", "edge_description": "ball bearing has_fault_mode ball fault"},
    {"edge_id": "SJMVC5LY_E099", "edge_description": "tooth breakage contains Single Severity"},
    {"edge_id": "SJMVC5LY_E100", "edge_description": "chipped gear contains Single Severity"},
    {"edge_id": "SJMVC5LY_E101", "edge_description": "eccentric gear contains Single Severity"},
    {"edge_id": "SJMVC5LY_E102", "edge_description": "inner race fault contains Single Severity"},
    {"edge_id": "SJMVC5LY_E103", "edge_description": "outer race fault contains Single Severity"},
    {"edge_id": "SJMVC5LY_E104", "edge_description": "ball fault contains Single Severity"},
    {"edge_id": "SJMVC5LY_E105", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E106", "edge_description": "ball bearing contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E107", "edge_description": "pinion wheel contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E108", "edge_description": "ball bearing contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E109", "edge_description": "tooth breakage contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E110", "edge_description": "chipped gear contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E111", "edge_description": "eccentric gear contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E112", "edge_description": "inner race fault contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E113", "edge_description": "outer race fault contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E114", "edge_description": "ball fault contains_phm_task fault diagnosis"},
    {"edge_id": "SJMVC5LY_E116", "edge_description": "gearbox induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E117", "edge_description": "ball bearing induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E118", "edge_description": "five variable rotational speeds of the input shaft until 30, 35, 40, 45 and 50 Hz induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E119", "edge_description": "Single Severity induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E120", "edge_description": "bearing with combined fault induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E121", "edge_description": "fault diagnosis induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E122", "edge_description": "680 samples divided into 440 training and 240 testing instances induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E123", "edge_description": "raw vibration signals induces_problem compound faults"},
    {"edge_id": "SJMVC5LY_E124", "edge_description": "Running time / Training time induces_problem compound faults"}
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
| 1 | `SJMVC5LY_E095` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | eccentric gear |  |
| 2 | `SJMVC5LY_E096` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | inner race fault |  |
| 3 | `SJMVC5LY_E097` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | outer race fault |  |
| 4 | `SJMVC5LY_E098` | `has_fault_mode` | 04-Fault Location | ball bearing |  | 05-Fault Mode | ball fault |  |
| 5 | `SJMVC5LY_E099` | `contains` | 05-Fault Mode | tooth breakage |  | 06-Fault Severity | Single Severity |  |
| 6 | `SJMVC5LY_E100` | `contains` | 05-Fault Mode | chipped gear |  | 06-Fault Severity | Single Severity |  |
| 7 | `SJMVC5LY_E101` | `contains` | 05-Fault Mode | eccentric gear |  | 06-Fault Severity | Single Severity |  |
| 8 | `SJMVC5LY_E102` | `contains` | 05-Fault Mode | inner race fault |  | 06-Fault Severity | Single Severity |  |
| 9 | `SJMVC5LY_E103` | `contains` | 05-Fault Mode | outer race fault |  | 06-Fault Severity | Single Severity |  |
| 10 | `SJMVC5LY_E104` | `contains` | 05-Fault Mode | ball fault |  | 06-Fault Severity | Single Severity |  |
| 11 | `SJMVC5LY_E105` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `SJMVC5LY_E106` | `contains_phm_task` | 02-Object Type | ball bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `SJMVC5LY_E107` | `contains_phm_task` | 04-Fault Location | pinion wheel |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `SJMVC5LY_E108` | `contains_phm_task` | 04-Fault Location | ball bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `SJMVC5LY_E109` | `contains_phm_task` | 05-Fault Mode | tooth breakage |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `SJMVC5LY_E110` | `contains_phm_task` | 05-Fault Mode | chipped gear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `SJMVC5LY_E111` | `contains_phm_task` | 05-Fault Mode | eccentric gear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `SJMVC5LY_E112` | `contains_phm_task` | 05-Fault Mode | inner race fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `SJMVC5LY_E113` | `contains_phm_task` | 05-Fault Mode | outer race fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `SJMVC5LY_E114` | `contains_phm_task` | 05-Fault Mode | ball fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `SJMVC5LY_E116` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 22 | `SJMVC5LY_E117` | `induces_problem` | 02-Object Type | ball bearing |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 23 | `SJMVC5LY_E118` | `induces_problem` | 03-Operating Conditions | five variable rotational speeds of the input shaft until 30, 35, 40, 45 and 50 Hz(Multiple Conditions) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 24 | `SJMVC5LY_E119` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 25 | `SJMVC5LY_E120` | `induces_problem` | 07-Compound Fault | bearing with combined fault(Compound Fault Within Same Structure) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 26 | `SJMVC5LY_E121` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 27 | `SJMVC5LY_E122` | `induces_problem` | 12-Training Data Availability | 680 samples divided into 440 training and 240 testing instances(Sufficient) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 28 | `SJMVC5LY_E123` | `induces_problem` | 13-Noise Level | raw vibration signals(Normal) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 29 | `SJMVC5LY_E124` | `induces_problem` | 14-Computational Resource | Running time / Training time |  | 09-Problem Scenario | compound faults(Compound Faults) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 29 edges)*
