# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WMYIVKSD
- **Paper Title**：Structural abstraction for model-based diagnosis with a strong fault model
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `WMYIVKSD`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WMYIVKSD_E038", "edge_description": "stuck-at-0 contains No Compound Fault"},
    {"edge_id": "WMYIVKSD_E039", "edge_description": "stuck-at-1 contains No Compound Fault"},
    {"edge_id": "WMYIVKSD_E040", "edge_description": "flip contains No Compound Fault"},
    {"edge_id": "WMYIVKSD_E042", "edge_description": "Boolean gate has_fault_mode stuck-at-0"},
    {"edge_id": "WMYIVKSD_E043", "edge_description": "Boolean gate has_fault_mode stuck-at-1"},
    {"edge_id": "WMYIVKSD_E044", "edge_description": "Boolean gate has_fault_mode flip"},
    {"edge_id": "WMYIVKSD_E045", "edge_description": "stuck-at-0 contains Single Severity"},
    {"edge_id": "WMYIVKSD_E046", "edge_description": "stuck-at-1 contains Single Severity"},
    {"edge_id": "WMYIVKSD_E047", "edge_description": "flip contains Single Severity"},
    {"edge_id": "WMYIVKSD_E050", "edge_description": "stuck-at-0 contains_phm_task model-based diagnosis"},
    {"edge_id": "WMYIVKSD_E051", "edge_description": "stuck-at-1 contains_phm_task model-based diagnosis"},
    {"edge_id": "WMYIVKSD_E052", "edge_description": "flip contains_phm_task model-based diagnosis"},
    {"edge_id": "WMYIVKSD_E054", "edge_description": "Boolean circuits induces_problem computationally challenging for large-scale and complex systems"},
    {"edge_id": "WMYIVKSD_E055", "edge_description": "Boolean circuits induces_problem multiple fault diagnosis"},
    {"edge_id": "WMYIVKSD_E056", "edge_description": "Boolean circuits induces_problem ungroundable abstract diagnoses in strong fault models"},
    {"edge_id": "WMYIVKSD_E057", "edge_description": "multiple observations with different fault mode probabilities induces_problem computationally challenging for large-scale and complex systems"},
    {"edge_id": "WMYIVKSD_E058", "edge_description": "multiple observations with different fault mode probabilities induces_problem multiple fault diagnosis"},
    {"edge_id": "WMYIVKSD_E059", "edge_description": "multiple observations with different fault mode probabilities induces_problem ungroundable abstract diagnoses in strong fault models"},
    {"edge_id": "WMYIVKSD_E060", "edge_description": "Single Severity induces_problem computationally challenging for large-scale and complex systems"},
    {"edge_id": "WMYIVKSD_E061", "edge_description": "Single Severity induces_problem multiple fault diagnosis"},
    {"edge_id": "WMYIVKSD_E062", "edge_description": "Single Severity induces_problem ungroundable abstract diagnoses in strong fault models"},
    {"edge_id": "WMYIVKSD_E063", "edge_description": "No Compound Fault induces_problem computationally challenging for large-scale and complex systems"},
    {"edge_id": "WMYIVKSD_E064", "edge_description": "No Compound Fault induces_problem multiple fault diagnosis"},
    {"edge_id": "WMYIVKSD_E065", "edge_description": "No Compound Fault induces_problem ungroundable abstract diagnoses in strong fault models"},
    {"edge_id": "WMYIVKSD_E066", "edge_description": "model-based diagnosis induces_problem computationally challenging for large-scale and complex systems"},
    {"edge_id": "WMYIVKSD_E067", "edge_description": "model-based diagnosis induces_problem multiple fault diagnosis"},
    {"edge_id": "WMYIVKSD_E068", "edge_description": "model-based diagnosis induces_problem ungroundable abstract diagnoses in strong fault models"},
    {"edge_id": "WMYIVKSD_E069", "edge_description": "dataset of 6550 cones induces_problem computationally challenging for large-scale and complex systems"},
    {"edge_id": "WMYIVKSD_E070", "edge_description": "dataset of 6550 cones induces_problem multiple fault diagnosis"},
    {"edge_id": "WMYIVKSD_E071", "edge_description": "dataset of 6550 cones induces_problem ungroundable abstract diagnoses in strong fault models"}
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
| 1 | `WMYIVKSD_E038` | `contains` | 05-Fault Mode | stuck-at-0 |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `WMYIVKSD_E039` | `contains` | 05-Fault Mode | stuck-at-1 |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `WMYIVKSD_E040` | `contains` | 05-Fault Mode | flip |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `WMYIVKSD_E042` | `has_fault_mode` | 04-Fault Location | Boolean gate |  | 05-Fault Mode | stuck-at-0 |  |
| 5 | `WMYIVKSD_E043` | `has_fault_mode` | 04-Fault Location | Boolean gate |  | 05-Fault Mode | stuck-at-1 |  |
| 6 | `WMYIVKSD_E044` | `has_fault_mode` | 04-Fault Location | Boolean gate |  | 05-Fault Mode | flip |  |
| 7 | `WMYIVKSD_E045` | `contains` | 05-Fault Mode | stuck-at-0 |  | 06-Fault Severity | Single Severity |  |
| 8 | `WMYIVKSD_E046` | `contains` | 05-Fault Mode | stuck-at-1 |  | 06-Fault Severity | Single Severity |  |
| 9 | `WMYIVKSD_E047` | `contains` | 05-Fault Mode | flip |  | 06-Fault Severity | Single Severity |  |
| 10 | `WMYIVKSD_E050` | `contains_phm_task` | 05-Fault Mode | stuck-at-0 |  | 08-PHM Task | model-based diagnosis(Diagnosis Task) |  |
| 11 | `WMYIVKSD_E051` | `contains_phm_task` | 05-Fault Mode | stuck-at-1 |  | 08-PHM Task | model-based diagnosis(Diagnosis Task) |  |
| 12 | `WMYIVKSD_E052` | `contains_phm_task` | 05-Fault Mode | flip |  | 08-PHM Task | model-based diagnosis(Diagnosis Task) |  |
| 13 | `WMYIVKSD_E054` | `induces_problem` | 02-Object Type | Boolean circuits |  | 09-Problem Scenario | computationally challenging for large-scale and complex systems(Complex Systems) |  |
| 14 | `WMYIVKSD_E055` | `induces_problem` | 02-Object Type | Boolean circuits |  | 09-Problem Scenario | multiple fault diagnosis(Compound Faults) |  |
| 15 | `WMYIVKSD_E056` | `induces_problem` | 02-Object Type | Boolean circuits |  | 09-Problem Scenario | ungroundable abstract diagnoses in strong fault models(Other) |  |
| 16 | `WMYIVKSD_E057` | `induces_problem` | 03-Operating Conditions | multiple observations with different fault mode probabilities(Multiple Conditions) |  | 09-Problem Scenario | computationally challenging for large-scale and complex systems(Complex Systems) |  |
| 17 | `WMYIVKSD_E058` | `induces_problem` | 03-Operating Conditions | multiple observations with different fault mode probabilities(Multiple Conditions) |  | 09-Problem Scenario | multiple fault diagnosis(Compound Faults) |  |
| 18 | `WMYIVKSD_E059` | `induces_problem` | 03-Operating Conditions | multiple observations with different fault mode probabilities(Multiple Conditions) |  | 09-Problem Scenario | ungroundable abstract diagnoses in strong fault models(Other) |  |
| 19 | `WMYIVKSD_E060` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | computationally challenging for large-scale and complex systems(Complex Systems) |  |
| 20 | `WMYIVKSD_E061` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | multiple fault diagnosis(Compound Faults) |  |
| 21 | `WMYIVKSD_E062` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | ungroundable abstract diagnoses in strong fault models(Other) |  |
| 22 | `WMYIVKSD_E063` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | computationally challenging for large-scale and complex systems(Complex Systems) |  |
| 23 | `WMYIVKSD_E064` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | multiple fault diagnosis(Compound Faults) |  |
| 24 | `WMYIVKSD_E065` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | ungroundable abstract diagnoses in strong fault models(Other) |  |
| 25 | `WMYIVKSD_E066` | `induces_problem` | 08-PHM Task | model-based diagnosis(Diagnosis Task) |  | 09-Problem Scenario | computationally challenging for large-scale and complex systems(Complex Systems) |  |
| 26 | `WMYIVKSD_E067` | `induces_problem` | 08-PHM Task | model-based diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multiple fault diagnosis(Compound Faults) |  |
| 27 | `WMYIVKSD_E068` | `induces_problem` | 08-PHM Task | model-based diagnosis(Diagnosis Task) |  | 09-Problem Scenario | ungroundable abstract diagnoses in strong fault models(Other) |  |
| 28 | `WMYIVKSD_E069` | `induces_problem` | 12-Training Data Availability | dataset of 6550 cones(Sufficient) |  | 09-Problem Scenario | computationally challenging for large-scale and complex systems(Complex Systems) |  |
| 29 | `WMYIVKSD_E070` | `induces_problem` | 12-Training Data Availability | dataset of 6550 cones(Sufficient) |  | 09-Problem Scenario | multiple fault diagnosis(Compound Faults) |  |
| 30 | `WMYIVKSD_E071` | `induces_problem` | 12-Training Data Availability | dataset of 6550 cones(Sufficient) |  | 09-Problem Scenario | ungroundable abstract diagnoses in strong fault models(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
