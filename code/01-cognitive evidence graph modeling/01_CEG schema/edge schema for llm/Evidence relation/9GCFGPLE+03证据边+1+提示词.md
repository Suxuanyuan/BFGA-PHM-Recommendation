# Candidate Evidence Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate evidence edge relation judgment and description completion** task.

- **Reference ID**: 9GCFGPLE
- **Paper Title**: Non-stationary vibration feature extraction method based on sparse decomposition and order tracking for gearbox fault diagnosis
- **Number of Candidate Edges to Judge**: 14

---

## II. LLM Input

> **Input Material**: Reference ID `9GCFGPLE` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
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
| 1 | `9GCFGPLE_E137` | `motivates` | 09-Problem Scenario | compound faults(Compound Faults) |  | 19-Training Optimization Algorithm | Correlation Filtering |  |
| 2 | `9GCFGPLE_E138` | `motivates` | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  | 19-Training Optimization Algorithm | Correlation Filtering |  |
| 3 | `9GCFGPLE_E139` | `motivates` | 12-Training Data Availability | Sufficient |  | 19-Training Optimization Algorithm | Correlation Filtering |  |
| 4 | `9GCFGPLE_E140` | `motivates` | 13-Noise Level | 0 dB noise, −14.6 dB SNR(High Noise) |  | 15-Data Preprocessing Algorithm | Computed Order Tracking |  |
| 5 | `9GCFGPLE_E141` | `motivates` | 13-Noise Level | 0 dB noise, −14.6 dB SNR(High Noise) |  | 16-Feature Extraction Algorithm | Segmented Matching Pursuit |  |
| 6 | `9GCFGPLE_E142` | `motivates` | 09-Problem Scenario | compound faults(Compound Faults) |  | 15-Data Preprocessing Algorithm | Computed Order Tracking |  |
| 7 | `9GCFGPLE_E143` | `motivates` | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  | 15-Data Preprocessing Algorithm | Computed Order Tracking |  |
| 8 | `9GCFGPLE_E144` | `motivates` | 09-Problem Scenario | compound faults(Compound Faults) |  | 16-Feature Extraction Algorithm | Segmented Matching Pursuit |  |
| 9 | `9GCFGPLE_E145` | `motivates` | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  | 16-Feature Extraction Algorithm | Segmented Matching Pursuit |  |
| 10 | `9GCFGPLE_E146` | `motivates` | 09-Problem Scenario | compound faults(Compound Faults) |  | 17-Core Classifier Algorithm | Envelope Order Spectrum Analysis |  |
| 11 | `9GCFGPLE_E147` | `motivates` | 09-Problem Scenario | noise robustness, low signal-to-noise ratio(Uncertainty) |  | 17-Core Classifier Algorithm | Envelope Order Spectrum Analysis |  |
| 12 | `9GCFGPLE_E148` | `motivates` | 07-Compound Fault | compound faults(Compound Fault Across Structures) |  | 16-Feature Extraction Algorithm | Segmented Matching Pursuit |  |
| 13 | `9GCFGPLE_E149` | `motivates` | 07-Compound Fault | compound faults(Compound Fault Across Structures) |  | 17-Core Classifier Algorithm | Envelope Order Spectrum Analysis |  |
| 14 | `9GCFGPLE_E150` | `motivates` | 06-Fault Severity | broken tooth(Single Severity) |  | 17-Core Classifier Algorithm | Envelope Order Spectrum Analysis |  |

> **Auxiliary Note**: When judging, the information in each column of the table should be used comprehensively — `source_node` / `target_node` are node names; `source_description` / `target_description` are the original text descriptions extracted from the paper (highly valuable reference); `edge_type` is the relation semantics. **Prioritize using node names, and make a comprehensive judgment combining the original text descriptions and the edge_type semantics**.

---

## VI. [Mandatory Constraint] At Least 1 Evidence Edge Must Be Extracted Between 09-Problem Scenario and Nodes 15~19

The following candidate edges are of the type "09-Problem Scenario → Nodes 15~19 (Algorithm)"; **at least 1 of them must be judged as "existing" and extracted as an evidence edge**:
  - `9GCFGPLE_E137`：compound faults(Compound Faults) motivates Correlation Filtering
  - `9GCFGPLE_E138`：noise robustness, low signal-to-noise ratio(Uncertainty) motivates Correlation Filtering
  - `9GCFGPLE_E142`：compound faults(Compound Faults) motivates Computed Order Tracking
  - `9GCFGPLE_E143`：noise robustness, low signal-to-noise ratio(Uncertainty) motivates Computed Order Tracking
  - `9GCFGPLE_E144`：compound faults(Compound Faults) motivates Segmented Matching Pursuit
  - `9GCFGPLE_E145`：noise robustness, low signal-to-noise ratio(Uncertainty) motivates Segmented Matching Pursuit
  - `9GCFGPLE_E146`：compound faults(Compound Faults) motivates Envelope Order Spectrum Analysis
  - `9GCFGPLE_E147`：noise robustness, low signal-to-noise ratio(Uncertainty) motivates Envelope Order Spectrum Analysis

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

*This prompt is automatically generated by edge_03_prompt.py (Batch 1, total 14 edges)*
