# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：9GCFGPLE
- **Paper Title**：Non-stationary vibration feature extraction method based on sparse decomposition and order tracking for gearbox fault diagnosis
- **Number of Candidate Edges to Judge**：21 

---

## II. LLM Input

> **Input Material**: Reference ID `9GCFGPLE`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "9GCFGPLE_E115", "edge_description": "coupling contains_phm_task fault diagnosis"},
    {"edge_id": "9GCFGPLE_E116", "edge_description": "broken tooth contains_phm_task fault diagnosis"},
    {"edge_id": "9GCFGPLE_E117", "edge_description": "misalignment contains_phm_task fault diagnosis"},
    {"edge_id": "9GCFGPLE_E119", "edge_description": "automobile transmission induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E120", "edge_description": "automobile transmission induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E121", "edge_description": "planetary gearbox induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E122", "edge_description": "planetary gearbox induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E123", "edge_description": "time-varying conditions, variable speed condition induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E124", "edge_description": "time-varying conditions, variable speed condition induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E125", "edge_description": "broken tooth induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E126", "edge_description": "broken tooth induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E127", "edge_description": "compound faults induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E128", "edge_description": "compound faults induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E129", "edge_description": "fault diagnosis induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E130", "edge_description": "fault diagnosis induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E131", "edge_description": "Sufficient induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E132", "edge_description": "Sufficient induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E133", "edge_description": "0 dB noise, −14.6 dB SNR induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E134", "edge_description": "0 dB noise, −14.6 dB SNR induces_problem noise robustness, low signal-to-noise ratio"},
    {"edge_id": "9GCFGPLE_E135", "edge_description": "computational efficiency induces_problem compound faults"},
    {"edge_id": "9GCFGPLE_E136", "edge_description": "computational efficiency induces_problem noise robustness, low signal-to-noise ratio"}
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
| 1 | `9GCFGPLE_E115` | `contains_phm_task` | 04-Fault Location | coupling |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 2 | `9GCFGPLE_E116` | `contains_phm_task` | 05-Fault Mode | broken tooth |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 3 | `9GCFGPLE_E117` | `contains_phm_task` | 05-Fault Mode | misalignment |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 4 | `9GCFGPLE_E119` | `induces_problem` | 02-Object Type | automobile transmission |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 5 | `9GCFGPLE_E120` | `induces_problem` | 02-Object Type | automobile transmission |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 6 | `9GCFGPLE_E121` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 7 | `9GCFGPLE_E122` | `induces_problem` | 02-Object Type | planetary gearbox |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 8 | `9GCFGPLE_E123` | `induces_problem` | 03-Operating Conditions | time-varying conditions, variable speed condition(Variable Conditions) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 9 | `9GCFGPLE_E124` | `induces_problem` | 03-Operating Conditions | time-varying conditions, variable speed condition(Variable Conditions) |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 10 | `9GCFGPLE_E125` | `induces_problem` | 06-Fault Severity | broken tooth(Single Severity) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 11 | `9GCFGPLE_E126` | `induces_problem` | 06-Fault Severity | broken tooth(Single Severity) |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 12 | `9GCFGPLE_E127` | `induces_problem` | 07-Compound Fault | compound faults(Compound Fault Across Structures) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 13 | `9GCFGPLE_E128` | `induces_problem` | 07-Compound Fault | compound faults(Compound Fault Across Structures) |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 14 | `9GCFGPLE_E129` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 15 | `9GCFGPLE_E130` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 16 | `9GCFGPLE_E131` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 17 | `9GCFGPLE_E132` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 18 | `9GCFGPLE_E133` | `induces_problem` | 13-Noise Level | 0 dB noise, −14.6 dB SNR(High Noise) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 19 | `9GCFGPLE_E134` | `induces_problem` | 13-Noise Level | 0 dB noise, −14.6 dB SNR(High Noise) |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |
| 20 | `9GCFGPLE_E135` | `induces_problem` | 14-Computational Resource | computational efficiency(Low Resource Consumption) |  | 09-Problem Scenario | compound faults(Compound Faults) |  |
| 21 | `9GCFGPLE_E136` | `induces_problem` | 14-Computational Resource | computational efficiency(Low Resource Consumption) |  | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 21 edges)*
