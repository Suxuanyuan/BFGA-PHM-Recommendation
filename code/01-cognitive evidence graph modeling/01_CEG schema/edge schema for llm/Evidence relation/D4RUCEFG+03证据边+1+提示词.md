# Candidate Evidence Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate evidence edge relation judgment and description completion** task.

- **Reference ID**: D4RUCEFG
- **Paper Title**: Optimum IMFs Selection Based Envelope Analysis of Bearing Fault Diagnosis in Plunger Pump
- **Number of Candidate Edges to Judge**: 30

---

## II. LLM Input

> **Input Material**: Reference ID `D4RUCEFG` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
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
| 1 | `D4ISWLJF_E091` | `motivates` | 13-Noise Level | Normal |  | 15-Data Preprocessing Algorithm | Db8 Wavelet |  |
| 2 | `D4ISWLJF_E092` | `motivates` | 13-Noise Level | Normal |  | 16-Feature Extraction Algorithm | Pseudo Fourth-Order Moment |  |
| 3 | `D4ISWLJF_E093` | `motivates` | 09-Problem Scenario | bearing fault feature reconstruction and stable feature extraction from non-stationary signals(Other) |  | 15-Data Preprocessing Algorithm | Db8 Wavelet |  |
| 4 | `D4ISWLJF_E094` | `motivates` | 09-Problem Scenario | balancing data quantity and diagnosis accuracy(Other) |  | 15-Data Preprocessing Algorithm | Db8 Wavelet |  |
| 5 | `D4ISWLJF_E095` | `motivates` | 09-Problem Scenario | bearing fault feature reconstruction and stable feature extraction from non-stationary signals(Other) |  | 16-Feature Extraction Algorithm | Pseudo Fourth-Order Moment |  |
| 6 | `D4ISWLJF_E096` | `motivates` | 09-Problem Scenario | balancing data quantity and diagnosis accuracy(Other) |  | 16-Feature Extraction Algorithm | Pseudo Fourth-Order Moment |  |
| 7 | `D4ISWLJF_E097` | `motivates` | 09-Problem Scenario | bearing fault feature reconstruction and stable feature extraction from non-stationary signals(Other) |  | 17-Core Classifier Algorithm | Extreme Learning Machine |  |
| 8 | `D4ISWLJF_E098` | `motivates` | 09-Problem Scenario | balancing data quantity and diagnosis accuracy(Other) |  | 17-Core Classifier Algorithm | Extreme Learning Machine |  |
| 9 | `D4ISWLJF_E099` | `motivates` | 07-Compound Fault | No Compound Fault |  | 16-Feature Extraction Algorithm | Pseudo Fourth-Order Moment |  |
| 10 | `D4ISWLJF_E100` | `motivates` | 07-Compound Fault | No Compound Fault |  | 17-Core Classifier Algorithm | Extreme Learning Machine |  |
| 11 | `D4ISWLJF_E101` | `motivates` | 06-Fault Severity | 0.007 inch(Single Severity) |  | 17-Core Classifier Algorithm | Extreme Learning Machine |  |
| 12 | `D4PFSSCQ_E074` | `motivates` | 13-Noise Level | Normal |  | 16-Feature Extraction Algorithm | STFT |  |
| 13 | `D4PFSSCQ_E075` | `motivates` | 09-Problem Scenario | combined faults / simultaneous faults(Compound Faults) |  | 16-Feature Extraction Algorithm | STFT |  |
| 14 | `D4PFSSCQ_E076` | `motivates` | 09-Problem Scenario | false diagnostics in double cage and axial ducts rotors(Other) |  | 16-Feature Extraction Algorithm | STFT |  |
| 15 | `D4PFSSCQ_E077` | `motivates` | 09-Problem Scenario | combined faults / simultaneous faults(Compound Faults) |  | 17-Core Classifier Algorithm | Thresholding |  |
| 16 | `D4PFSSCQ_E078` | `motivates` | 09-Problem Scenario | false diagnostics in double cage and axial ducts rotors(Other) |  | 17-Core Classifier Algorithm | Thresholding |  |
| 17 | `D4PFSSCQ_E079` | `motivates` | 07-Compound Fault | combined failures(Compound Fault Within Same Structure) |  | 16-Feature Extraction Algorithm | STFT |  |
| 18 | `D4PFSSCQ_E080` | `motivates` | 07-Compound Fault | combined failures(Compound Fault Within Same Structure) |  | 17-Core Classifier Algorithm | Thresholding |  |
| 19 | `D4PFSSCQ_E081` | `motivates` | 06-Fault Severity | number of broken bars(Multiple Severities) |  | 17-Core Classifier Algorithm | Thresholding |  |
| 20 | `D4RUCEFG_E092` | `motivates` | 13-Noise Level | fault information is submerged in the noise and the disturbance impact signals(High Noise) |  | 15-Data Preprocessing Algorithm | EMD |  |
| 21 | `D4RUCEFG_E093` | `motivates` | 13-Noise Level | fault information is submerged in the noise and the disturbance impact signals(High Noise) |  | 16-Feature Extraction Algorithm | Hilbert transform |  |
| 22 | `D4RUCEFG_E094` | `motivates` | 09-Problem Scenario | submerged in the noise and the disturbance impact signals(Uncertainty) |  | 15-Data Preprocessing Algorithm | EMD |  |
| 23 | `D4RUCEFG_E095` | `motivates` | 09-Problem Scenario | compound fault in the inner race and roller(Compound Faults) |  | 15-Data Preprocessing Algorithm | EMD |  |
| 24 | `D4RUCEFG_E096` | `motivates` | 09-Problem Scenario | submerged in the noise and the disturbance impact signals(Uncertainty) |  | 16-Feature Extraction Algorithm | Hilbert transform |  |
| 25 | `D4RUCEFG_E097` | `motivates` | 09-Problem Scenario | compound fault in the inner race and roller(Compound Faults) |  | 16-Feature Extraction Algorithm | Hilbert transform |  |
| 26 | `D4RUCEFG_E098` | `motivates` | 09-Problem Scenario | submerged in the noise and the disturbance impact signals(Uncertainty) |  | 17-Core Classifier Algorithm | Spectrum comparison |  |
| 27 | `D4RUCEFG_E099` | `motivates` | 09-Problem Scenario | compound fault in the inner race and roller(Compound Faults) |  | 17-Core Classifier Algorithm | Spectrum comparison |  |
| 28 | `D4RUCEFG_E100` | `motivates` | 07-Compound Fault | compound fault in the inner race and roller(Compound Fault Within Same Structure) |  | 16-Feature Extraction Algorithm | Hilbert transform |  |
| 29 | `D4RUCEFG_E101` | `motivates` | 07-Compound Fault | compound fault in the inner race and roller(Compound Fault Within Same Structure) |  | 17-Core Classifier Algorithm | Spectrum comparison |  |
| 30 | `D4RUCEFG_E102` | `motivates` | 06-Fault Severity | fault diameters of 0.2 mm, and the fault depth is 0.3 mm(Single Severity) |  | 17-Core Classifier Algorithm | Spectrum comparison |  |

> **Auxiliary Note**: When judging, the information in each column of the table should be used comprehensively — `source_node` / `target_node` are node names; `source_description` / `target_description` are the original text descriptions extracted from the paper (highly valuable reference); `edge_type` is the relation semantics. **Prioritize using node names, and make a comprehensive judgment combining the original text descriptions and the edge_type semantics**.

---

## VI. [Mandatory Constraint] At Least 1 Evidence Edge Must Be Extracted Between 09-Problem Scenario and Nodes 15~19

The following candidate edges are of the type "09-Problem Scenario → Nodes 15~19 (Algorithm)"; **at least 1 of them must be judged as "existing" and extracted as an evidence edge**:
  - `D4ISWLJF_E093`：bearing fault feature reconstruction and stable feature extraction from non-stationary signals(Other) motivates Db8 Wavelet
  - `D4ISWLJF_E094`：balancing data quantity and diagnosis accuracy(Other) motivates Db8 Wavelet
  - `D4ISWLJF_E095`：bearing fault feature reconstruction and stable feature extraction from non-stationary signals(Other) motivates Pseudo Fourth-Order Moment
  - `D4ISWLJF_E096`：balancing data quantity and diagnosis accuracy(Other) motivates Pseudo Fourth-Order Moment
  - `D4ISWLJF_E097`：bearing fault feature reconstruction and stable feature extraction from non-stationary signals(Other) motivates Extreme Learning Machine
  - `D4ISWLJF_E098`：balancing data quantity and diagnosis accuracy(Other) motivates Extreme Learning Machine
  - `D4PFSSCQ_E075`：combined faults / simultaneous faults(Compound Faults) motivates STFT
  - `D4PFSSCQ_E076`：false diagnostics in double cage and axial ducts rotors(Other) motivates STFT
  - `D4PFSSCQ_E077`：combined faults / simultaneous faults(Compound Faults) motivates Thresholding
  - `D4PFSSCQ_E078`：false diagnostics in double cage and axial ducts rotors(Other) motivates Thresholding
  - `D4RUCEFG_E094`：submerged in the noise and the disturbance impact signals(Uncertainty) motivates EMD
  - `D4RUCEFG_E095`：compound fault in the inner race and roller(Compound Faults) motivates EMD
  - `D4RUCEFG_E096`：submerged in the noise and the disturbance impact signals(Uncertainty) motivates Hilbert transform
  - `D4RUCEFG_E097`：compound fault in the inner race and roller(Compound Faults) motivates Hilbert transform
  - `D4RUCEFG_E098`：submerged in the noise and the disturbance impact signals(Uncertainty) motivates Spectrum comparison
  - `D4RUCEFG_E099`：compound fault in the inner race and roller(Compound Faults) motivates Spectrum comparison

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

*This prompt is automatically generated by edge_03_prompt.py (Batch 1, total 30 edges)*
