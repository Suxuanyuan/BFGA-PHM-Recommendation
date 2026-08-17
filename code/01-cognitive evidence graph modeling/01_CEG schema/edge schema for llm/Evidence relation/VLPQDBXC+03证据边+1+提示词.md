# Candidate Evidence Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate evidence edge relation judgment and description completion** task.

- **Reference ID**: VLPQDBXC
- **Paper Title**: Real-Time Fault-Tolerant Moving Horizon Air Data Estimation for the RECONFIGURE Benchmark
- **Number of Candidate Edges to Judge**: 9

---

## II. LLM Input

> **Input Material**: Reference ID `VLPQDBXC` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
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
| 1 | `VLPQDBXC_E136` | `motivates` | 13-Noise Level | measurement noises, wind disturbances(High Noise) |  | 15-Data Preprocessing Algorithm | Adaptive Weighted Fusion |  |
| 2 | `VLPQDBXC_E137` | `motivates` | 09-Problem Scenario | tradeoff between robustness to wind disturbances and sensitivity to sensor faults(Uncertainty) |  | 15-Data Preprocessing Algorithm | Adaptive Weighted Fusion |  |
| 3 | `VLPQDBXC_E138` | `motivates` | 09-Problem Scenario | simultaneous multiple sensor faults within the triplex redundancy(Compound Faults) |  | 15-Data Preprocessing Algorithm | Adaptive Weighted Fusion |  |
| 4 | `VLPQDBXC_E139` | `motivates` | 09-Problem Scenario | real-time computation constraint of flight control computers, SAO graphical symbol library compliance(Other) |  | 15-Data Preprocessing Algorithm | Adaptive Weighted Fusion |  |
| 5 | `VLPQDBXC_E140` | `motivates` | 09-Problem Scenario | tradeoff between robustness to wind disturbances and sensitivity to sensor faults(Uncertainty) |  | 17-Core Classifier Algorithm | Constrained Moving Horizon Estimation |  |
| 6 | `VLPQDBXC_E141` | `motivates` | 09-Problem Scenario | simultaneous multiple sensor faults within the triplex redundancy(Compound Faults) |  | 17-Core Classifier Algorithm | Constrained Moving Horizon Estimation |  |
| 7 | `VLPQDBXC_E142` | `motivates` | 09-Problem Scenario | real-time computation constraint of flight control computers, SAO graphical symbol library compliance(Other) |  | 17-Core Classifier Algorithm | Constrained Moving Horizon Estimation |  |
| 8 | `VLPQDBXC_E143` | `motivates` | 07-Compound Fault | simultaneous AOA and VCAS sensor faults(Compound Fault Across Structures) |  | 17-Core Classifier Algorithm | Constrained Moving Horizon Estimation |  |
| 9 | `VLPQDBXC_E144` | `motivates` | 06-Fault Severity | Bias amplitude, Drift rate, Jamming amplitude, Runaway rate(Multiple Severities) |  | 17-Core Classifier Algorithm | Constrained Moving Horizon Estimation |  |

> **Auxiliary Note**: When judging, the information in each column of the table should be used comprehensively — `source_node` / `target_node` are node names; `source_description` / `target_description` are the original text descriptions extracted from the paper (highly valuable reference); `edge_type` is the relation semantics. **Prioritize using node names, and make a comprehensive judgment combining the original text descriptions and the edge_type semantics**.

---

## VI. [Mandatory Constraint] At Least 1 Evidence Edge Must Be Extracted Between 09-Problem Scenario and Nodes 15~19

The following candidate edges are of the type "09-Problem Scenario → Nodes 15~19 (Algorithm)"; **at least 1 of them must be judged as "existing" and extracted as an evidence edge**:
  - `VLPQDBXC_E137`：tradeoff between robustness to wind disturbances and sensitivity to sensor faults(Uncertainty) motivates Adaptive Weighted Fusion
  - `VLPQDBXC_E138`：simultaneous multiple sensor faults within the triplex redundancy(Compound Faults) motivates Adaptive Weighted Fusion
  - `VLPQDBXC_E139`：real-time computation constraint of flight control computers, SAO graphical symbol library compliance(Other) motivates Adaptive Weighted Fusion
  - `VLPQDBXC_E140`：tradeoff between robustness to wind disturbances and sensitivity to sensor faults(Uncertainty) motivates Constrained Moving Horizon Estimation
  - `VLPQDBXC_E141`：simultaneous multiple sensor faults within the triplex redundancy(Compound Faults) motivates Constrained Moving Horizon Estimation
  - `VLPQDBXC_E142`：real-time computation constraint of flight control computers, SAO graphical symbol library compliance(Other) motivates Constrained Moving Horizon Estimation

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

*This prompt is automatically generated by edge_03_prompt.py (Batch 1, total 9 edges)*
