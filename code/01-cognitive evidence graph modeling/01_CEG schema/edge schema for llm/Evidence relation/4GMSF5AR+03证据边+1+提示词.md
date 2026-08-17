# Candidate Evidence Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate evidence edge relation judgment and description completion** task.

- **Reference ID**: 4GMSF5AR
- **Paper Title**: A framework to automate fault detection and diagnosis based on moving window principal component analysis and Bayesian network
- **Number of Candidate Edges to Judge**: 14

---

## II. LLM Input

> **Input Material**: Reference ID `4GMSF5AR` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
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
| 1 | `4GMSF5AR_E157` | `motivates` | 13-Noise Level | strong noise background, noises or unexpected variations(High Noise) |  | 15-Data Preprocessing Algorithm | Moving Window |  |
| 2 | `4GMSF5AR_E158` | `motivates` | 13-Noise Level | strong noise background, noises or unexpected variations(High Noise) |  | 16-Feature Extraction Algorithm | Principal Component Analysis |  |
| 3 | `4GMSF5AR_E159` | `motivates` | 09-Problem Scenario | absence of labeled fault data(Zero Fault Samples) |  | 15-Data Preprocessing Algorithm | Moving Window |  |
| 4 | `4GMSF5AR_E160` | `motivates` | 09-Problem Scenario | complex systems(Complex Systems) |  | 15-Data Preprocessing Algorithm | Moving Window |  |
| 5 | `4GMSF5AR_E161` | `motivates` | 09-Problem Scenario | uncertainty(Uncertainty) |  | 15-Data Preprocessing Algorithm | Moving Window |  |
| 6 | `4GMSF5AR_E162` | `motivates` | 09-Problem Scenario | absence of labeled fault data(Zero Fault Samples) |  | 16-Feature Extraction Algorithm | Principal Component Analysis |  |
| 7 | `4GMSF5AR_E163` | `motivates` | 09-Problem Scenario | complex systems(Complex Systems) |  | 16-Feature Extraction Algorithm | Principal Component Analysis |  |
| 8 | `4GMSF5AR_E164` | `motivates` | 09-Problem Scenario | uncertainty(Uncertainty) |  | 16-Feature Extraction Algorithm | Principal Component Analysis |  |
| 9 | `4GMSF5AR_E165` | `motivates` | 09-Problem Scenario | absence of labeled fault data(Zero Fault Samples) |  | 17-Core Classifier Algorithm | Bayesian Network |  |
| 10 | `4GMSF5AR_E166` | `motivates` | 09-Problem Scenario | complex systems(Complex Systems) |  | 17-Core Classifier Algorithm | Bayesian Network |  |
| 11 | `4GMSF5AR_E167` | `motivates` | 09-Problem Scenario | uncertainty(Uncertainty) |  | 17-Core Classifier Algorithm | Bayesian Network |  |
| 12 | `4GMSF5AR_E168` | `motivates` | 07-Compound Fault | No Compound Fault |  | 16-Feature Extraction Algorithm | Principal Component Analysis |  |
| 13 | `4GMSF5AR_E169` | `motivates` | 07-Compound Fault | No Compound Fault |  | 17-Core Classifier Algorithm | Bayesian Network |  |
| 14 | `4GMSF5AR_E170` | `motivates` | 06-Fault Severity | exponential gain as a function of time(Multiple Severities) |  | 17-Core Classifier Algorithm | Bayesian Network |  |

> **Auxiliary Note**: When judging, the information in each column of the table should be used comprehensively — `source_node` / `target_node` are node names; `source_description` / `target_description` are the original text descriptions extracted from the paper (highly valuable reference); `edge_type` is the relation semantics. **Prioritize using node names, and make a comprehensive judgment combining the original text descriptions and the edge_type semantics**.

---

## VI. [Mandatory Constraint] At Least 1 Evidence Edge Must Be Extracted Between 09-Problem Scenario and Nodes 15~19

The following candidate edges are of the type "09-Problem Scenario → Nodes 15~19 (Algorithm)"; **at least 1 of them must be judged as "existing" and extracted as an evidence edge**:
  - `4GMSF5AR_E159`：absence of labeled fault data(Zero Fault Samples) motivates Moving Window
  - `4GMSF5AR_E160`：complex systems(Complex Systems) motivates Moving Window
  - `4GMSF5AR_E161`：uncertainty(Uncertainty) motivates Moving Window
  - `4GMSF5AR_E162`：absence of labeled fault data(Zero Fault Samples) motivates Principal Component Analysis
  - `4GMSF5AR_E163`：complex systems(Complex Systems) motivates Principal Component Analysis
  - `4GMSF5AR_E164`：uncertainty(Uncertainty) motivates Principal Component Analysis
  - `4GMSF5AR_E165`：absence of labeled fault data(Zero Fault Samples) motivates Bayesian Network
  - `4GMSF5AR_E166`：complex systems(Complex Systems) motivates Bayesian Network
  - `4GMSF5AR_E167`：uncertainty(Uncertainty) motivates Bayesian Network

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

*This prompt is automatically generated by edge_03_prompt.py (Batch 1, total 14 edges)*
