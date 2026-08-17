# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：RDYNYFQP
- **Paper Title**：Knowledge distilling based model compression and feature learning in fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `RDYNYFQP`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "RDYNYFQP_E215", "edge_description": "amplifier has_fault_mode conversion anomaly"},
    {"edge_id": "RDYNYFQP_E216", "edge_description": "amplifier has_fault_mode amplifier anomaly"},
    {"edge_id": "RDYNYFQP_E217", "edge_description": "tank has_fault_mode stuck"},
    {"edge_id": "RDYNYFQP_E218", "edge_description": "tank has_fault_mode leakage"},
    {"edge_id": "RDYNYFQP_E219", "edge_description": "tank has_fault_mode rate anomaly"},
    {"edge_id": "RDYNYFQP_E220", "edge_description": "tank has_fault_mode power leakage"},
    {"edge_id": "RDYNYFQP_E221", "edge_description": "tank has_fault_mode timing anomaly"},
    {"edge_id": "RDYNYFQP_E222", "edge_description": "tank has_fault_mode conversion anomaly"},
    {"edge_id": "RDYNYFQP_E223", "edge_description": "tank has_fault_mode amplifier anomaly"},
    {"edge_id": "RDYNYFQP_E224", "edge_description": "pipe has_fault_mode stuck"},
    {"edge_id": "RDYNYFQP_E225", "edge_description": "pipe has_fault_mode leakage"},
    {"edge_id": "RDYNYFQP_E226", "edge_description": "pipe has_fault_mode rate anomaly"},
    {"edge_id": "RDYNYFQP_E227", "edge_description": "pipe has_fault_mode power leakage"},
    {"edge_id": "RDYNYFQP_E228", "edge_description": "pipe has_fault_mode timing anomaly"},
    {"edge_id": "RDYNYFQP_E229", "edge_description": "pipe has_fault_mode conversion anomaly"},
    {"edge_id": "RDYNYFQP_E230", "edge_description": "pipe has_fault_mode amplifier anomaly"},
    {"edge_id": "RDYNYFQP_E231", "edge_description": "stuck contains fault parameter"},
    {"edge_id": "RDYNYFQP_E232", "edge_description": "leakage contains fault parameter"},
    {"edge_id": "RDYNYFQP_E233", "edge_description": "rate anomaly contains fault parameter"},
    {"edge_id": "RDYNYFQP_E234", "edge_description": "power leakage contains fault parameter"},
    {"edge_id": "RDYNYFQP_E235", "edge_description": "timing anomaly contains fault parameter"},
    {"edge_id": "RDYNYFQP_E236", "edge_description": "conversion anomaly contains fault parameter"},
    {"edge_id": "RDYNYFQP_E237", "edge_description": "amplifier anomaly contains fault parameter"},
    {"edge_id": "RDYNYFQP_E238", "edge_description": "Binary phase shift keying (BPSK) communication system contains_phm_task Fault diagnosis"},
    {"edge_id": "RDYNYFQP_E239", "edge_description": "10-tank system contains_phm_task Fault diagnosis"},
    {"edge_id": "RDYNYFQP_E240", "edge_description": "pseudo code generator contains_phm_task Fault diagnosis"},
    {"edge_id": "RDYNYFQP_E241", "edge_description": "carrier generator contains_phm_task Fault diagnosis"},
    {"edge_id": "RDYNYFQP_E242", "edge_description": "multiplier contains_phm_task Fault diagnosis"},
    {"edge_id": "RDYNYFQP_E243", "edge_description": "amplifier contains_phm_task Fault diagnosis"},
    {"edge_id": "RDYNYFQP_E244", "edge_description": "tank contains_phm_task Fault diagnosis"}
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
| 1 | `RDYNYFQP_E215` | `has_fault_mode` | 04-Fault Location | amplifier |  | 05-Fault Mode | conversion anomaly |  |
| 2 | `RDYNYFQP_E216` | `has_fault_mode` | 04-Fault Location | amplifier |  | 05-Fault Mode | amplifier anomaly |  |
| 3 | `RDYNYFQP_E217` | `has_fault_mode` | 04-Fault Location | tank |  | 05-Fault Mode | stuck |  |
| 4 | `RDYNYFQP_E218` | `has_fault_mode` | 04-Fault Location | tank |  | 05-Fault Mode | leakage |  |
| 5 | `RDYNYFQP_E219` | `has_fault_mode` | 04-Fault Location | tank |  | 05-Fault Mode | rate anomaly |  |
| 6 | `RDYNYFQP_E220` | `has_fault_mode` | 04-Fault Location | tank |  | 05-Fault Mode | power leakage |  |
| 7 | `RDYNYFQP_E221` | `has_fault_mode` | 04-Fault Location | tank |  | 05-Fault Mode | timing anomaly |  |
| 8 | `RDYNYFQP_E222` | `has_fault_mode` | 04-Fault Location | tank |  | 05-Fault Mode | conversion anomaly |  |
| 9 | `RDYNYFQP_E223` | `has_fault_mode` | 04-Fault Location | tank |  | 05-Fault Mode | amplifier anomaly |  |
| 10 | `RDYNYFQP_E224` | `has_fault_mode` | 04-Fault Location | pipe |  | 05-Fault Mode | stuck |  |
| 11 | `RDYNYFQP_E225` | `has_fault_mode` | 04-Fault Location | pipe |  | 05-Fault Mode | leakage |  |
| 12 | `RDYNYFQP_E226` | `has_fault_mode` | 04-Fault Location | pipe |  | 05-Fault Mode | rate anomaly |  |
| 13 | `RDYNYFQP_E227` | `has_fault_mode` | 04-Fault Location | pipe |  | 05-Fault Mode | power leakage |  |
| 14 | `RDYNYFQP_E228` | `has_fault_mode` | 04-Fault Location | pipe |  | 05-Fault Mode | timing anomaly |  |
| 15 | `RDYNYFQP_E229` | `has_fault_mode` | 04-Fault Location | pipe |  | 05-Fault Mode | conversion anomaly |  |
| 16 | `RDYNYFQP_E230` | `has_fault_mode` | 04-Fault Location | pipe |  | 05-Fault Mode | amplifier anomaly |  |
| 17 | `RDYNYFQP_E231` | `contains` | 05-Fault Mode | stuck |  | 06-Fault Severity | fault parameter(Multiple Severities) |  |
| 18 | `RDYNYFQP_E232` | `contains` | 05-Fault Mode | leakage |  | 06-Fault Severity | fault parameter(Multiple Severities) |  |
| 19 | `RDYNYFQP_E233` | `contains` | 05-Fault Mode | rate anomaly |  | 06-Fault Severity | fault parameter(Multiple Severities) |  |
| 20 | `RDYNYFQP_E234` | `contains` | 05-Fault Mode | power leakage |  | 06-Fault Severity | fault parameter(Multiple Severities) |  |
| 21 | `RDYNYFQP_E235` | `contains` | 05-Fault Mode | timing anomaly |  | 06-Fault Severity | fault parameter(Multiple Severities) |  |
| 22 | `RDYNYFQP_E236` | `contains` | 05-Fault Mode | conversion anomaly |  | 06-Fault Severity | fault parameter(Multiple Severities) |  |
| 23 | `RDYNYFQP_E237` | `contains` | 05-Fault Mode | amplifier anomaly |  | 06-Fault Severity | fault parameter(Multiple Severities) |  |
| 24 | `RDYNYFQP_E238` | `contains_phm_task` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 25 | `RDYNYFQP_E239` | `contains_phm_task` | 02-Object Type | 10-tank system |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 26 | `RDYNYFQP_E240` | `contains_phm_task` | 04-Fault Location | pseudo code generator |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 27 | `RDYNYFQP_E241` | `contains_phm_task` | 04-Fault Location | carrier generator |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 28 | `RDYNYFQP_E242` | `contains_phm_task` | 04-Fault Location | multiplier |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 29 | `RDYNYFQP_E243` | `contains_phm_task` | 04-Fault Location | amplifier |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |
| 30 | `RDYNYFQP_E244` | `contains_phm_task` | 04-Fault Location | tank |  | 08-PHM Task | Fault diagnosis(Diagnosis Task) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 4, total 30 edges)*
