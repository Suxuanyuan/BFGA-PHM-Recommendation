# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：8EEFKLFF
- **Paper Title**：A novel supervised sparse feature extraction method and its application on rotating machine fault diagnosis
- **Number of Candidate Edges to Judge**：22 

---

## II. LLM Input

> **Input Material**: Reference ID `8EEFKLFF`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "8EEFKLFF_E111", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "8EEFKLFF_E112", "edge_description": "pitting contains_phm_task fault diagnosis"},
    {"edge_id": "8EEFKLFF_E113", "edge_description": "worn contains_phm_task fault diagnosis"},
    {"edge_id": "8EEFKLFF_E114", "edge_description": "broken-tooth contains_phm_task fault diagnosis"},
    {"edge_id": "8EEFKLFF_E116", "edge_description": "bearing induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E117", "edge_description": "bearing induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E118", "edge_description": "gearbox induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E119", "edge_description": "gearbox induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E120", "edge_description": "3 different loads (0, 1, 2 hp) for bearing, 4 loads for gearbox induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E121", "edge_description": "3 different loads (0, 1, 2 hp) for bearing, 4 loads for gearbox induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E122", "edge_description": "severity levels (0.18, 0.36 and 0.54 mm) induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E123", "edge_description": "severity levels (0.18, 0.36 and 0.54 mm) induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E124", "edge_description": "wheel gear pitting and pinion gear worn (WPPW), wheel gear broken-tooth and pinion gear worn (WBPW) induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E125", "edge_description": "wheel gear pitting and pinion gear worn (WPPW), wheel gear broken-tooth and pinion gear worn (WBPW) induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E126", "edge_description": "fault diagnosis induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E127", "edge_description": "fault diagnosis induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E128", "edge_description": "240 samples are obtained from each health condition under one load / 104 samples are acquired from each health condition under one load induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E129", "edge_description": "240 samples are obtained from each health condition under one load / 104 samples are acquired from each health condition under one load induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E130", "edge_description": "Normal induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E131", "edge_description": "Normal induces_problem physical interpretation / interpretability"},
    {"edge_id": "8EEFKLFF_E132", "edge_description": "The label matrix increases almost no computing cost / Since l-BFGS computes fast and needs less computing cost / training time is less than 70 s induces_problem compound fault"},
    {"edge_id": "8EEFKLFF_E133", "edge_description": "The label matrix increases almost no computing cost / Since l-BFGS computes fast and needs less computing cost / training time is less than 70 s induces_problem physical interpretation / interpretability"}
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
| 1 | `8EEFKLFF_E111` | `contains_phm_task` | 04-Fault Location | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 2 | `8EEFKLFF_E112` | `contains_phm_task` | 05-Fault Mode | pitting |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 3 | `8EEFKLFF_E113` | `contains_phm_task` | 05-Fault Mode | worn |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 4 | `8EEFKLFF_E114` | `contains_phm_task` | 05-Fault Mode | broken-tooth |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 5 | `8EEFKLFF_E116` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 6 | `8EEFKLFF_E117` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 7 | `8EEFKLFF_E118` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 8 | `8EEFKLFF_E119` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 9 | `8EEFKLFF_E120` | `induces_problem` | 03-Operating Conditions | 3 different loads (0, 1, 2 hp) for bearing, 4 loads for gearbox(Multiple Conditions) |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 10 | `8EEFKLFF_E121` | `induces_problem` | 03-Operating Conditions | 3 different loads (0, 1, 2 hp) for bearing, 4 loads for gearbox(Multiple Conditions) |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 11 | `8EEFKLFF_E122` | `induces_problem` | 06-Fault Severity | severity levels (0.18, 0.36 and 0.54 mm)(Multiple Severities) |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 12 | `8EEFKLFF_E123` | `induces_problem` | 06-Fault Severity | severity levels (0.18, 0.36 and 0.54 mm)(Multiple Severities) |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 13 | `8EEFKLFF_E124` | `induces_problem` | 07-Compound Fault | wheel gear pitting and pinion gear worn (WPPW), wheel gear broken-tooth and pinion gear worn (WBPW)(Compound Fault Within Same Structure) |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 14 | `8EEFKLFF_E125` | `induces_problem` | 07-Compound Fault | wheel gear pitting and pinion gear worn (WPPW), wheel gear broken-tooth and pinion gear worn (WBPW)(Compound Fault Within Same Structure) |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 15 | `8EEFKLFF_E126` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 16 | `8EEFKLFF_E127` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 17 | `8EEFKLFF_E128` | `induces_problem` | 12-Training Data Availability | 240 samples are obtained from each health condition under one load / 104 samples are acquired from each health condition under one load(Sufficient) |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 18 | `8EEFKLFF_E129` | `induces_problem` | 12-Training Data Availability | 240 samples are obtained from each health condition under one load / 104 samples are acquired from each health condition under one load(Sufficient) |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 19 | `8EEFKLFF_E130` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 20 | `8EEFKLFF_E131` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |
| 21 | `8EEFKLFF_E132` | `induces_problem` | 14-Computational Resource | The label matrix increases almost no computing cost / Since l-BFGS computes fast and needs less computing cost / training time is less than 70 s(Low Resource Consumption) |  | 09-Problem Scenario | compound fault(Compound Faults) |  |
| 22 | `8EEFKLFF_E133` | `induces_problem` | 14-Computational Resource | The label matrix increases almost no computing cost / Since l-BFGS computes fast and needs less computing cost / training time is less than 70 s(Low Resource Consumption) |  | 09-Problem Scenario | physical interpretation / interpretability(Trustworthiness / Interpretability) |  |

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
