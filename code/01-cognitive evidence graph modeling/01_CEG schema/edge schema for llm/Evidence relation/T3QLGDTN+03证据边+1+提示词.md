# Candidate Evidence Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate evidence edge relation judgment and description completion** task.

- **Reference ID**: T3QLGDTN
- **Paper Title**: Optimized Relative Transformation Matrix Using Bacterial Foraging Algorithm for Process Fault Detection
- **Number of Candidate Edges to Judge**: 18

---

## II. LLM Input

> **Input Material**: Reference ID `T3QLGDTN` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments, and conclusions, and then judge each of the following candidate edges one by one.

---

## III. Output Format

### 3.1 Output Format

```json
[
{"edge_id": "<edge_id>", "edge_description": "<source_node> <edge_type> <target_node>|<tone judgment>|<evidence field>"}
]
```

### 3.2 Field Description

| Field | Description | Data Type |
|------|------|---------|
| `edge_id` | Unique identifier of the candidate edge | String, must be exactly the same as the input |
| `edge_description` | Format: `<source_node> <edge_type> <target_node>|<tone judgment>|<evidence field>`, three parts separated by `|` | String |

### 3.3 Mandatory Constraints

1. **`edge_id` must be exactly the same as the candidate edge list**; do not generate or modify it yourself.
2. **`edge_description` format must strictly be three parts: `node relation|tone judgment|evidence field`; do not add, delete, or modify the delimiter `|`**; any `|` in the content must be escaped as `\|`.
3. **Tone judgment must be one of two**: `明确指出证据关系` (Explicitly Stated Evidence Relation) or `未明确指出但推理可知证据关系` (Not Explicitly Stated but Inferable Evidence Relation); no other expressions are allowed.
4. **Only output candidate edges judged as "existing"**; if judged as "not existing", skip directly.
5. If all candidate edges are judged as not existing, output the empty array `[]`.

---

## IV. Core Judgment Principles

### 4.1 Understanding the Essential Intent

When judging candidate edges, the information in each column of the table should be used comprehensively:

- **source_node / target_node**: Node names; prioritize using the original names as the judgment basis
- **source_description / target_description**: The original text descriptions when extracting these nodes from the paper (highly valuable reference), providing context for judging relations
- **edge_type**: Semantics need to be understood in the context of the full text, rather than literal retrieval

**The core of judging the relation is understanding the essential intent of the candidate edge, rather than exactly matching a particular sentence in the original text.**

A candidate edge jointly expresses a semantic relation (e.g., "a certain problem drives the choice of a certain method") through `source_node` (including source_description), `edge_type`, and `target_node` (including target_description).

### 4.2 Tone Judgment (Choose One)

| Option | Meaning |
|------|------|
| `明确指出证据关系` (Explicitly Stated Evidence Relation) | The original text has a coherent paragraph in the same place, directly describing the driving relation between source and target |
| `未明确指出但推理可知证据关系` (Not Explicitly Stated but Inferable Evidence Relation) | The original text has no coherent paragraph directly describing the relation, but combining the context (including the LLM's built-in common knowledge), the relation can be judged to exist |

### 4.3 Evidence Field Filling Rules

**Type A - Explicitly Stated Evidence Relation**: Evidence field = directly quoted original text (verbatim copy, 1~3 sentences, no rewriting)

**Type B - Not Explicitly Stated but Inferable Evidence Relation**: Evidence field = quoted original text + LLM inference

```
【Quoted Original Text】<PDF verbatim copy of the relevant excerpt, 1~3 sentences>
【LLM Inference】<logical derivation based on the quoted original text, 1~2 sentences, explaining why the relation exists>
```

> **Quoted original text must be extracted verbatim; do not add/delete/modify any characters. LLM inference must be entirely based on the quoted original text; do not exceed the scope of the original text with speculation.**

---

## V. Candidate Edge Judgment Table

Please judge each candidate edge in the table below:

| No. | edge_id | edge_type | source_type | source_node | source_description | target_type | target_node | target_description |
|------|---------|-----------|------------|------------|------------------|------------|------------|-------------------|
| 1 | `T3QLGDTN_E173` | `motivates` | 09-Problem Scenario | complicated industrial system with highly coupled parameters(Complex Systems) |  | 19-Training Optimization Algorithm | BFA |  |
| 2 | `T3QLGDTN_E174` | `motivates` | 09-Problem Scenario | uncertainties from system disturbance and state change(Uncertainty) |  | 19-Training Optimization Algorithm | BFA |  |
| 3 | `T3QLGDTN_E175` | `motivates` | 09-Problem Scenario | losing feature after the normalization of nonlinear variables in the feature subspace(Other) |  | 19-Training Optimization Algorithm | BFA |  |
| 4 | `T3QLGDTN_E176` | `motivates` | 12-Training Data Availability | 400 training datasets(Sufficient) |  | 19-Training Optimization Algorithm | BFA |  |
| 5 | `T3QLGDTN_E177` | `motivates` | 13-Noise Level | system disturbance(Normal) |  | 15-Data Preprocessing Algorithm | Normalization |  |
| 6 | `T3QLGDTN_E178` | `motivates` | 13-Noise Level | system disturbance(Normal) |  | 16-Feature Extraction Algorithm | KPCA |  |
| 7 | `T3QLGDTN_E179` | `motivates` | 09-Problem Scenario | complicated industrial system with highly coupled parameters(Complex Systems) |  | 15-Data Preprocessing Algorithm | Normalization |  |
| 8 | `T3QLGDTN_E180` | `motivates` | 09-Problem Scenario | uncertainties from system disturbance and state change(Uncertainty) |  | 15-Data Preprocessing Algorithm | Normalization |  |
| 9 | `T3QLGDTN_E181` | `motivates` | 09-Problem Scenario | losing feature after the normalization of nonlinear variables in the feature subspace(Other) |  | 15-Data Preprocessing Algorithm | Normalization |  |
| 10 | `T3QLGDTN_E182` | `motivates` | 09-Problem Scenario | complicated industrial system with highly coupled parameters(Complex Systems) |  | 16-Feature Extraction Algorithm | KPCA |  |
| 11 | `T3QLGDTN_E183` | `motivates` | 09-Problem Scenario | uncertainties from system disturbance and state change(Uncertainty) |  | 16-Feature Extraction Algorithm | KPCA |  |
| 12 | `T3QLGDTN_E184` | `motivates` | 09-Problem Scenario | losing feature after the normalization of nonlinear variables in the feature subspace(Other) |  | 16-Feature Extraction Algorithm | KPCA |  |
| 13 | `T3QLGDTN_E185` | `motivates` | 09-Problem Scenario | complicated industrial system with highly coupled parameters(Complex Systems) |  | 17-Core Classifier Algorithm | BPNN |  |
| 14 | `T3QLGDTN_E186` | `motivates` | 09-Problem Scenario | uncertainties from system disturbance and state change(Uncertainty) |  | 17-Core Classifier Algorithm | BPNN |  |
| 15 | `T3QLGDTN_E187` | `motivates` | 09-Problem Scenario | losing feature after the normalization of nonlinear variables in the feature subspace(Other) |  | 17-Core Classifier Algorithm | BPNN |  |
| 16 | `T3QLGDTN_E188` | `motivates` | 07-Compound Fault | No Compound Fault |  | 16-Feature Extraction Algorithm | KPCA |  |
| 17 | `T3QLGDTN_E189` | `motivates` | 07-Compound Fault | No Compound Fault |  | 17-Core Classifier Algorithm | BPNN |  |
| 18 | `T3QLGDTN_E190` | `motivates` | 06-Fault Severity | Single Severity |  | 17-Core Classifier Algorithm | BPNN |  |

> **Auxiliary Note**: When judging, the information in each column of the table should be used comprehensively — `source_node` / `target_node` are node names; `source_description` / `target_description` are the original text descriptions extracted from the paper (highly valuable reference); `edge_type` is the relation semantics. **Prioritize using node names, and make a comprehensive judgment combining the original text descriptions and the edge_type semantics**.

---

## VI. [Mandatory Constraint] At Least 1 Evidence Edge Must Be Extracted Between 09-Problem Scenario and Nodes 15~19

The following candidate edges are of the type "09-Problem Scenario → Nodes 15~19 (Algorithm)"; **at least 1 of them must be judged as "existing" and extracted as an evidence edge**:
  - `T3QLGDTN_E173`：complicated industrial system with highly coupled parameters(Complex Systems) motivates BFA
  - `T3QLGDTN_E174`：uncertainties from system disturbance and state change(Uncertainty) motivates BFA
  - `T3QLGDTN_E175`：losing feature after the normalization of nonlinear variables in the feature subspace(Other) motivates BFA
  - `T3QLGDTN_E179`：complicated industrial system with highly coupled parameters(Complex Systems) motivates Normalization
  - `T3QLGDTN_E180`：uncertainties from system disturbance and state change(Uncertainty) motivates Normalization
  - `T3QLGDTN_E181`：losing feature after the normalization of nonlinear variables in the feature subspace(Other) motivates Normalization
  - `T3QLGDTN_E182`：complicated industrial system with highly coupled parameters(Complex Systems) motivates KPCA
  - `T3QLGDTN_E183`：uncertainties from system disturbance and state change(Uncertainty) motivates KPCA
  - `T3QLGDTN_E184`：losing feature after the normalization of nonlinear variables in the feature subspace(Other) motivates KPCA
  - `T3QLGDTN_E185`：complicated industrial system with highly coupled parameters(Complex Systems) motivates BPNN
  - `T3QLGDTN_E186`：uncertainties from system disturbance and state change(Uncertainty) motivates BPNN
  - `T3QLGDTN_E187`：losing feature after the normalization of nonlinear variables in the feature subspace(Other) motivates BPNN

**Execution Rules**:
1. If at least 1 of the candidate edges is judged as "existing" → output normally
2. If **all candidate edges are judged as "not existing"** → must select the one with the closest semantics, force-judge it as "未明确指出但推理可知证据关系" (Not Explicitly Stated but Inferable Evidence Relation), and output it
3. If the literature **does not contain** this type of candidate edge → skip this constraint

### ▶ Type C: `Data-Scarcity-Driven Evidence Edge` (12-Training Data Availability → Nodes 18/19/15/16 (Algorithm))

**Applicable Conditions**: source_node belongs to the "Training Data Availability" type (e.g., data scarce, insufficient samples), and target_node is a data generation algorithm (18), training optimization algorithm (19), or pre-processing / feature extraction algorithm (15/16).

**Core Principle**: This kind of relation is a basic methodological common knowledge in the PHM domain ("data insufficient → use data augmentation"), and is almost never described in papers using explicit driving words like `motivates`; instead, it is reflected through "method selection" and "experimental design".

**Evidence Field**:
```
【Quoted Original Text】<PDF coherent paragraph describing the data amount issue and the corresponding method, 1~3 sentences>
【LLM Inference】<logical derivation based on the quoted original text, 1~2 sentences>
```

**Judgment Criteria**: As long as the quoted original text describes the combination of "data amount issue + corresponding method", it is acceptable.

**Forbidden**: Merely describing data amount values (e.g., "The dataset contains 1000 samples") without involving method selection.

---

## VII. LLM Constraints

1. **Only output "existing" edges**; if judged as "not existing", skip directly and do not write to JSON.
2. **Tone judgment is forced to choose one**: `明确指出证据关系` (Explicitly Stated Evidence Relation) or `未明确指出但推理可知证据关系` (Not Explicitly Stated but Inferable Evidence Relation); no other forms are allowed.
3. **Absolutely Forbidden**:
   - Rewriting, summarizing, splicing, or truncating the middle of sentences in the original text
   - Inference beyond the scope of the quoted original text (speculation)
   - Outputting summary descriptions like "according to the paper..." instead of the original text
4. **Output Cleanliness Principle**: The JSON must not contain any non-standard JSON content (e.g., comments, prefix descriptions).

---

*This prompt is automatically generated by edge_03_prompt.py (Batch 1, total 18 edges)*
