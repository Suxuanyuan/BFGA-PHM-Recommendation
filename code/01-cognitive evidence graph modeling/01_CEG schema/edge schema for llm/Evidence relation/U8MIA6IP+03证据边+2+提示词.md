# Candidate Evidence Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate evidence edge relation judgment and description completion** task.

- **Reference ID**: U8MIA6IP
- **Paper Title**: Spectral negentropy based sidebands and demodulation analysis for planet bearing fault diagnosis
- **Number of Candidate Edges to Judge**: 3

---

## II. LLM Input

> **Input Material**: Reference ID `U8MIA6IP` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
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
| 1 | `U8MIA6IP_E112` | `motivates` | 07-Compound Fault | No Compound Fault |  | 16-Feature Extraction Algorithm | Empirical Mode Decomposition |  |
| 2 | `U8MIA6IP_E113` | `motivates` | 07-Compound Fault | No Compound Fault |  | 17-Core Classifier Algorithm | Fourier transform |  |
| 3 | `U8MIA6IP_E114` | `motivates` | 06-Fault Severity | Outer race: 14.90mm x 0.44mm x 2.20mm, Rolling element: 10.18mm x 0.40mm x 1.30mm, Inner race: 14.90mm x 0.28mm x 1.10mm(Single Severity) |  | 17-Core Classifier Algorithm | Fourier transform |  |

> **Auxiliary Note**: When judging, the information in each column of the table should be used comprehensively — `source_node` / `target_node` are node names; `source_description` / `target_description` are the original text descriptions extracted from the paper (highly valuable reference); `edge_type` is the relation semantics. **Prioritize using node names, and make a comprehensive judgment combining the original text descriptions and the edge_type semantics**.

---

## VI. [Mandatory Constraint] At Least 1 Evidence Edge Must Be Extracted Between 09-Problem Scenario and Nodes 15~19

The following candidate edges are of the type "09-Problem Scenario → Nodes 15~19 (Algorithm)"; **at least 1 of them must be judged as "existing" and extracted as an evidence edge**:
  - `U8AGEI3J_E107`：noise robustness and false alarms(Uncertainty) motivates Genetic Algorithm
  - `U8AGEI3J_E108`：computational complexity and real-time constraints of PF(Other) motivates Genetic Algorithm
  - `U8AGEI3J_E112`：noise robustness and false alarms(Uncertainty) motivates Butterworth filter
  - `U8AGEI3J_E113`：computational complexity and real-time constraints of PF(Other) motivates Butterworth filter
  - `U8AGEI3J_E114`：noise robustness and false alarms(Uncertainty) motivates Recursive Least Squares
  - `U8AGEI3J_E115`：computational complexity and real-time constraints of PF(Other) motivates Recursive Least Squares
  - `U8AGEI3J_E116`：noise robustness and false alarms(Uncertainty) motivates mixed Particle Filter
  - `U8AGEI3J_E117`：computational complexity and real-time constraints of PF(Other) motivates mixed Particle Filter
  - `U8HVITYL_E066`：difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) motivates Overlapping Sliding Window
  - `U8HVITYL_E067`：difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) motivates Wavelet Packet Transform
  - `U8HVITYL_E068`：difference among feature distribution of the measured signals under different speed conditions(Distribution Discrepancy) motivates Weight Multi-Net
  - `U8MIA6IP_E106`：complex kinematics and multiple modulations(Complex Systems) motivates Spectral negentropy
  - `U8MIA6IP_E107`：contaminated by noise(Uncertainty) motivates Spectral negentropy
  - `U8MIA6IP_E108`：complex kinematics and multiple modulations(Complex Systems) motivates Empirical Mode Decomposition
  - `U8MIA6IP_E109`：contaminated by noise(Uncertainty) motivates Empirical Mode Decomposition
  - `U8MIA6IP_E110`：complex kinematics and multiple modulations(Complex Systems) motivates Fourier transform
  - `U8MIA6IP_E111`：contaminated by noise(Uncertainty) motivates Fourier transform

**Execution Rules**:
1. If at least 1 of the candidate edges is judged as "existing" → output normally
2. If **all candidate edges are judged as "not existing"** → must select the one with the closest semantics, force-judge it as "未明确指出但推理可知证据关系" (Not Explicitly Stated but Inferable Evidence Relation), and output it
3. If the literature **does not contain** this type of candidate edge → skip this constraint



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

*This prompt is automatically generated by edge_03_prompt.py (Batch 2, total 3 edges)*
