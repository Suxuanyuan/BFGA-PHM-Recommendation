# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：8TA9ZRKQ
- **Paper Title**：An Advanced PLS Approach for Key Performance Indicator-Related Prediction and Diagnosis in Case of Outliers
- **Number of Candidate Edges to Judge**：22 

---

## II. LLM Input

> **Input Material**: Reference ID `8TA9ZRKQ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "8TA9ZRKQ_E160", "edge_description": "stripper has_fault_mode step change"},
    {"edge_id": "8TA9ZRKQ_E161", "edge_description": "stripper has_fault_mode drift"},
    {"edge_id": "8TA9ZRKQ_E162", "edge_description": "stripper has_fault_mode random variation"},
    {"edge_id": "8TA9ZRKQ_E163", "edge_description": "step change contains Single Severity"},
    {"edge_id": "8TA9ZRKQ_E164", "edge_description": "drift contains Single Severity"},
    {"edge_id": "8TA9ZRKQ_E165", "edge_description": "random variation contains Single Severity"},
    {"edge_id": "8TA9ZRKQ_E167", "edge_description": "reactor contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E168", "edge_description": "condenser contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E169", "edge_description": "vapor-liquid separator contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E170", "edge_description": "compressor contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E171", "edge_description": "stripper contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E172", "edge_description": "step change contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E173", "edge_description": "drift contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E174", "edge_description": "random variation contains_phm_task KPI-related prediction and fault diagnosis"},
    {"edge_id": "8TA9ZRKQ_E176", "edge_description": "chemical production process induces_problem outliers in training datasets"},
    {"edge_id": "8TA9ZRKQ_E177", "edge_description": "normal operating conditions induces_problem outliers in training datasets"},
    {"edge_id": "8TA9ZRKQ_E178", "edge_description": "Single Severity induces_problem outliers in training datasets"},
    {"edge_id": "8TA9ZRKQ_E179", "edge_description": "No Compound Fault induces_problem outliers in training datasets"},
    {"edge_id": "8TA9ZRKQ_E180", "edge_description": "KPI-related prediction and fault diagnosis induces_problem outliers in training datasets"},
    {"edge_id": "8TA9ZRKQ_E181", "edge_description": "one half of IDV(0) samples induces_problem outliers in training datasets"},
    {"edge_id": "8TA9ZRKQ_E182", "edge_description": "Normal induces_problem outliers in training datasets"},
    {"edge_id": "8TA9ZRKQ_E183", "edge_description": "small computation load induces_problem outliers in training datasets"}
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
| 1 | `8TA9ZRKQ_E160` | `has_fault_mode` | 04-Fault Location | stripper |  | 05-Fault Mode | step change |  |
| 2 | `8TA9ZRKQ_E161` | `has_fault_mode` | 04-Fault Location | stripper |  | 05-Fault Mode | drift |  |
| 3 | `8TA9ZRKQ_E162` | `has_fault_mode` | 04-Fault Location | stripper |  | 05-Fault Mode | random variation |  |
| 4 | `8TA9ZRKQ_E163` | `contains` | 05-Fault Mode | step change |  | 06-Fault Severity | Single Severity |  |
| 5 | `8TA9ZRKQ_E164` | `contains` | 05-Fault Mode | drift |  | 06-Fault Severity | Single Severity |  |
| 6 | `8TA9ZRKQ_E165` | `contains` | 05-Fault Mode | random variation |  | 06-Fault Severity | Single Severity |  |
| 7 | `8TA9ZRKQ_E167` | `contains_phm_task` | 04-Fault Location | reactor |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 8 | `8TA9ZRKQ_E168` | `contains_phm_task` | 04-Fault Location | condenser |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 9 | `8TA9ZRKQ_E169` | `contains_phm_task` | 04-Fault Location | vapor-liquid separator |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 10 | `8TA9ZRKQ_E170` | `contains_phm_task` | 04-Fault Location | compressor |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 11 | `8TA9ZRKQ_E171` | `contains_phm_task` | 04-Fault Location | stripper |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 12 | `8TA9ZRKQ_E172` | `contains_phm_task` | 05-Fault Mode | step change |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 13 | `8TA9ZRKQ_E173` | `contains_phm_task` | 05-Fault Mode | drift |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 14 | `8TA9ZRKQ_E174` | `contains_phm_task` | 05-Fault Mode | random variation |  | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  |
| 15 | `8TA9ZRKQ_E176` | `induces_problem` | 02-Object Type | chemical production process |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |
| 16 | `8TA9ZRKQ_E177` | `induces_problem` | 03-Operating Conditions | normal operating conditions(Single Condition) |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |
| 17 | `8TA9ZRKQ_E178` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |
| 18 | `8TA9ZRKQ_E179` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |
| 19 | `8TA9ZRKQ_E180` | `induces_problem` | 08-PHM Task | KPI-related prediction and fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |
| 20 | `8TA9ZRKQ_E181` | `induces_problem` | 12-Training Data Availability | one half of IDV(0) samples(Sufficient) |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |
| 21 | `8TA9ZRKQ_E182` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |
| 22 | `8TA9ZRKQ_E183` | `induces_problem` | 14-Computational Resource | small computation load(Low Resource Consumption) |  | 09-Problem Scenario | outliers in training datasets(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 22 edges)*
