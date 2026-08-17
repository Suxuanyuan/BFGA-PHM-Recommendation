# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TX9ITKE5
- **Paper Title**：Induction machine faults detection using stator current parametric spectral estimation
- **Number of Candidate Edges to Judge**：29 

---

## II. LLM Input

> **Input Material**: Reference ID `TX9ITKE5`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TX9ITKE5_E115", "edge_description": "Broken rotor bars contains number of broken rotor bars"},
    {"edge_id": "TX9ITKE5_E116", "edge_description": "Air gap eccentricity contains number of broken rotor bars"},
    {"edge_id": "TX9ITKE5_E117", "edge_description": "Bearing damage contains number of broken rotor bars"},
    {"edge_id": "TX9ITKE5_E118", "edge_description": "Induction machine contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E119", "edge_description": "Bearing contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E120", "edge_description": "Rotor bar contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E121", "edge_description": "Air gap contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E122", "edge_description": "Bearing contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E123", "edge_description": "Broken rotor bars contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E124", "edge_description": "Air gap eccentricity contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E125", "edge_description": "Bearing damage contains_phm_task Faults detection"},
    {"edge_id": "TX9ITKE5_E127", "edge_description": "Induction machine induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E128", "edge_description": "Induction machine induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E129", "edge_description": "Bearing induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E130", "edge_description": "Bearing induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E131", "edge_description": "Various load levels induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E132", "edge_description": "Various load levels induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E133", "edge_description": "number of broken rotor bars induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E134", "edge_description": "number of broken rotor bars induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E135", "edge_description": "No Compound Fault induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E136", "edge_description": "No Compound Fault induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E137", "edge_description": "Faults detection induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E138", "edge_description": "Faults detection induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E139", "edge_description": "N/A induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E140", "edge_description": "N/A induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E141", "edge_description": "White Gaussian noise induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E142", "edge_description": "White Gaussian noise induces_problem Sensitivity to noise of subspace techniques"},
    {"edge_id": "TX9ITKE5_E143", "edge_description": "FFT-based approximate approach for computational complexity reduction induces_problem Poor frequency resolution and leakage effects of classical spectral estimators"},
    {"edge_id": "TX9ITKE5_E144", "edge_description": "FFT-based approximate approach for computational complexity reduction induces_problem Sensitivity to noise of subspace techniques"}
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
| 1 | `TX9ITKE5_E115` | `contains` | 05-Fault Mode | Broken rotor bars |  | 06-Fault Severity | number of broken rotor bars(Multiple Severities) |  |
| 2 | `TX9ITKE5_E116` | `contains` | 05-Fault Mode | Air gap eccentricity |  | 06-Fault Severity | number of broken rotor bars(Multiple Severities) |  |
| 3 | `TX9ITKE5_E117` | `contains` | 05-Fault Mode | Bearing damage |  | 06-Fault Severity | number of broken rotor bars(Multiple Severities) |  |
| 4 | `TX9ITKE5_E118` | `contains_phm_task` | 02-Object Type | Induction machine |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 5 | `TX9ITKE5_E119` | `contains_phm_task` | 02-Object Type | Bearing |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 6 | `TX9ITKE5_E120` | `contains_phm_task` | 04-Fault Location | Rotor bar |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 7 | `TX9ITKE5_E121` | `contains_phm_task` | 04-Fault Location | Air gap |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 8 | `TX9ITKE5_E122` | `contains_phm_task` | 04-Fault Location | Bearing |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 9 | `TX9ITKE5_E123` | `contains_phm_task` | 05-Fault Mode | Broken rotor bars |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 10 | `TX9ITKE5_E124` | `contains_phm_task` | 05-Fault Mode | Air gap eccentricity |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 11 | `TX9ITKE5_E125` | `contains_phm_task` | 05-Fault Mode | Bearing damage |  | 08-PHM Task | Faults detection(Detection Task) |  |
| 12 | `TX9ITKE5_E127` | `induces_problem` | 02-Object Type | Induction machine |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 13 | `TX9ITKE5_E128` | `induces_problem` | 02-Object Type | Induction machine |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 14 | `TX9ITKE5_E129` | `induces_problem` | 02-Object Type | Bearing |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 15 | `TX9ITKE5_E130` | `induces_problem` | 02-Object Type | Bearing |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 16 | `TX9ITKE5_E131` | `induces_problem` | 03-Operating Conditions | Various load levels(Multiple Conditions) |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 17 | `TX9ITKE5_E132` | `induces_problem` | 03-Operating Conditions | Various load levels(Multiple Conditions) |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 18 | `TX9ITKE5_E133` | `induces_problem` | 06-Fault Severity | number of broken rotor bars(Multiple Severities) |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 19 | `TX9ITKE5_E134` | `induces_problem` | 06-Fault Severity | number of broken rotor bars(Multiple Severities) |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 20 | `TX9ITKE5_E135` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 21 | `TX9ITKE5_E136` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 22 | `TX9ITKE5_E137` | `induces_problem` | 08-PHM Task | Faults detection(Detection Task) |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 23 | `TX9ITKE5_E138` | `induces_problem` | 08-PHM Task | Faults detection(Detection Task) |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 24 | `TX9ITKE5_E139` | `induces_problem` | 12-Training Data Availability | N/A(Sufficient) |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 25 | `TX9ITKE5_E140` | `induces_problem` | 12-Training Data Availability | N/A(Sufficient) |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 26 | `TX9ITKE5_E141` | `induces_problem` | 13-Noise Level | White Gaussian noise(Normal) |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 27 | `TX9ITKE5_E142` | `induces_problem` | 13-Noise Level | White Gaussian noise(Normal) |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |
| 28 | `TX9ITKE5_E143` | `induces_problem` | 14-Computational Resource | FFT-based approximate approach for computational complexity reduction(Low Resource Consumption) |  | 09-Problem Scenario | Poor frequency resolution and leakage effects of classical spectral estimators(Other) |  |
| 29 | `TX9ITKE5_E144` | `induces_problem` | 14-Computational Resource | FFT-based approximate approach for computational complexity reduction(Low Resource Consumption) |  | 09-Problem Scenario | Sensitivity to noise of subspace techniques(Uncertainty) |  |

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
