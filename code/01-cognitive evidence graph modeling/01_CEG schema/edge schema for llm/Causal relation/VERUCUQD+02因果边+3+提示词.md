# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：VERUCUQD
- **Paper Title**：Sparse Exponential Discriminant Analysis and Its Application to Fault Diagnosis
- **Number of Candidate Edges to Judge**：18 

---

## II. LLM Input

> **Input Material**: Reference ID `VERUCUQD`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "VERUCUQD_E157", "edge_description": "random variation contains_phm_task fault diagnosis, fault isolation"},
    {"edge_id": "VERUCUQD_E158", "edge_description": "valve opening deviation contains_phm_task fault diagnosis, fault isolation"},
    {"edge_id": "VERUCUQD_E160", "edge_description": "Tennessee Eastman process induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E161", "edge_description": "Tennessee Eastman process induces_problem small-sample-size data, singularity problem"},
    {"edge_id": "VERUCUQD_E162", "edge_description": "cigarette production process (silk-processing operation) induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E163", "edge_description": "cigarette production process (silk-processing operation) induces_problem small-sample-size data, singularity problem"},
    {"edge_id": "VERUCUQD_E164", "edge_description": "normal operating data and fault conditions induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E165", "edge_description": "normal operating data and fault conditions induces_problem small-sample-size data, singularity problem"},
    {"edge_id": "VERUCUQD_E166", "edge_description": "increased by 25% induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E167", "edge_description": "increased by 25% induces_problem small-sample-size data, singularity problem"},
    {"edge_id": "VERUCUQD_E168", "edge_description": "No Compound Fault induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E169", "edge_description": "No Compound Fault induces_problem small-sample-size data, singularity problem"},
    {"edge_id": "VERUCUQD_E170", "edge_description": "fault diagnosis, fault isolation induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E171", "edge_description": "fault diagnosis, fault isolation induces_problem small-sample-size data, singularity problem"},
    {"edge_id": "VERUCUQD_E172", "edge_description": "50 fault samples of each fault induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E173", "edge_description": "50 fault samples of each fault induces_problem small-sample-size data, singularity problem"},
    {"edge_id": "VERUCUQD_E174", "edge_description": "Normal induces_problem poor model interpretability"},
    {"edge_id": "VERUCUQD_E175", "edge_description": "Normal induces_problem small-sample-size data, singularity problem"}
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
| 1 | `VERUCUQD_E157` | `contains_phm_task` | 05-Fault Mode | random variation |  | 08-PHM Task | fault diagnosis, fault isolation(Diagnosis Task) |  |
| 2 | `VERUCUQD_E158` | `contains_phm_task` | 05-Fault Mode | valve opening deviation |  | 08-PHM Task | fault diagnosis, fault isolation(Diagnosis Task) |  |
| 3 | `VERUCUQD_E160` | `induces_problem` | 02-Object Type | Tennessee Eastman process |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 4 | `VERUCUQD_E161` | `induces_problem` | 02-Object Type | Tennessee Eastman process |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |
| 5 | `VERUCUQD_E162` | `induces_problem` | 02-Object Type | cigarette production process (silk-processing operation) |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 6 | `VERUCUQD_E163` | `induces_problem` | 02-Object Type | cigarette production process (silk-processing operation) |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |
| 7 | `VERUCUQD_E164` | `induces_problem` | 03-Operating Conditions | normal operating data and fault conditions(Single Condition) |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 8 | `VERUCUQD_E165` | `induces_problem` | 03-Operating Conditions | normal operating data and fault conditions(Single Condition) |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |
| 9 | `VERUCUQD_E166` | `induces_problem` | 06-Fault Severity | increased by 25%(Single Severity) |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 10 | `VERUCUQD_E167` | `induces_problem` | 06-Fault Severity | increased by 25%(Single Severity) |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |
| 11 | `VERUCUQD_E168` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 12 | `VERUCUQD_E169` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |
| 13 | `VERUCUQD_E170` | `induces_problem` | 08-PHM Task | fault diagnosis, fault isolation(Diagnosis Task) |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 14 | `VERUCUQD_E171` | `induces_problem` | 08-PHM Task | fault diagnosis, fault isolation(Diagnosis Task) |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |
| 15 | `VERUCUQD_E172` | `induces_problem` | 12-Training Data Availability | 50 fault samples of each fault(Sufficient) |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 16 | `VERUCUQD_E173` | `induces_problem` | 12-Training Data Availability | 50 fault samples of each fault(Sufficient) |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |
| 17 | `VERUCUQD_E174` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | poor model interpretability(Trustworthiness / Interpretability) |  |
| 18 | `VERUCUQD_E175` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | small-sample-size data, singularity problem(Small Fault Samples) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 18 edges)*
