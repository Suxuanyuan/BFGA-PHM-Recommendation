# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：7LFIXXGS
- **Paper Title**：Distribution Adaptation and Manifold Alignment for complex processes fault diagnosis
- **Number of Candidate Edges to Judge**：21 

---

## II. LLM Input

> **Input Material**: Reference ID `7LFIXXGS`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "7LFIXXGS_E212", "edge_description": "reactor induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E213", "edge_description": "condenser induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E214", "edge_description": "condenser induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E215", "edge_description": "hydro-cyclone induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E216", "edge_description": "hydro-cyclone induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E217", "edge_description": "ball mill induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E218", "edge_description": "ball mill induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E219", "edge_description": "operating modes, different processes induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E220", "edge_description": "operating modes, different processes induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E221", "edge_description": "Single Severity induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E222", "edge_description": "Single Severity induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E223", "edge_description": "No Compound Fault induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E224", "edge_description": "No Compound Fault induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E225", "edge_description": "fault detection and diagnosis induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E226", "edge_description": "fault detection and diagnosis induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E227", "edge_description": "1800 groups of labeled data in the source domain induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E228", "edge_description": "1800 groups of labeled data in the source domain induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E229", "edge_description": "not considered when the sample is not balanced or the noise is large induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E230", "edge_description": "not considered when the sample is not balanced or the noise is large induces_problem complex processes / nonlinear trait"},
    {"edge_id": "7LFIXXGS_E231", "edge_description": "solved efficiently in a closed form induces_problem distribution shifts / unsupervised domain adaptation"},
    {"edge_id": "7LFIXXGS_E232", "edge_description": "solved efficiently in a closed form induces_problem complex processes / nonlinear trait"}
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
| 1 | `7LFIXXGS_E212` | `induces_problem` | 02-Object Type | reactor |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 2 | `7LFIXXGS_E213` | `induces_problem` | 02-Object Type | condenser |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 3 | `7LFIXXGS_E214` | `induces_problem` | 02-Object Type | condenser |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 4 | `7LFIXXGS_E215` | `induces_problem` | 02-Object Type | hydro-cyclone |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 5 | `7LFIXXGS_E216` | `induces_problem` | 02-Object Type | hydro-cyclone |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 6 | `7LFIXXGS_E217` | `induces_problem` | 02-Object Type | ball mill |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 7 | `7LFIXXGS_E218` | `induces_problem` | 02-Object Type | ball mill |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 8 | `7LFIXXGS_E219` | `induces_problem` | 03-Operating Conditions | operating modes, different processes(Multiple Conditions) |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 9 | `7LFIXXGS_E220` | `induces_problem` | 03-Operating Conditions | operating modes, different processes(Multiple Conditions) |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 10 | `7LFIXXGS_E221` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 11 | `7LFIXXGS_E222` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 12 | `7LFIXXGS_E223` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 13 | `7LFIXXGS_E224` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 14 | `7LFIXXGS_E225` | `induces_problem` | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 15 | `7LFIXXGS_E226` | `induces_problem` | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 16 | `7LFIXXGS_E227` | `induces_problem` | 12-Training Data Availability | 1800 groups of labeled data in the source domain(Sufficient) |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 17 | `7LFIXXGS_E228` | `induces_problem` | 12-Training Data Availability | 1800 groups of labeled data in the source domain(Sufficient) |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 18 | `7LFIXXGS_E229` | `induces_problem` | 13-Noise Level | not considered when the sample is not balanced or the noise is large(Normal) |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 19 | `7LFIXXGS_E230` | `induces_problem` | 13-Noise Level | not considered when the sample is not balanced or the noise is large(Normal) |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |
| 20 | `7LFIXXGS_E231` | `induces_problem` | 14-Computational Resource | solved efficiently in a closed form |  | 09-Problem Scenario | distribution shifts / unsupervised domain adaptation(Distribution Discrepancy) |  |
| 21 | `7LFIXXGS_E232` | `induces_problem` | 14-Computational Resource | solved efficiently in a closed form |  | 09-Problem Scenario | complex processes / nonlinear trait(Complex Systems) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 5, total 21 edges)*
