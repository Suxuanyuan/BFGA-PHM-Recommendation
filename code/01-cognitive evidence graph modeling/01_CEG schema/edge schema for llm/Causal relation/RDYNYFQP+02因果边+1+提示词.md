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
    {"edge_id": "RDYNYFQP_E125", "edge_description": "Industrial systems contains Binary phase shift keying (BPSK) communication system"},
    {"edge_id": "RDYNYFQP_E126", "edge_description": "Industrial systems contains 10-tank system"},
    {"edge_id": "RDYNYFQP_E127", "edge_description": "Binary phase shift keying (BPSK) communication system contains pseudo code generator"},
    {"edge_id": "RDYNYFQP_E128", "edge_description": "Binary phase shift keying (BPSK) communication system contains carrier generator"},
    {"edge_id": "RDYNYFQP_E129", "edge_description": "Binary phase shift keying (BPSK) communication system contains multiplier"},
    {"edge_id": "RDYNYFQP_E130", "edge_description": "Binary phase shift keying (BPSK) communication system contains amplifier"},
    {"edge_id": "RDYNYFQP_E131", "edge_description": "Binary phase shift keying (BPSK) communication system contains tank"},
    {"edge_id": "RDYNYFQP_E132", "edge_description": "Binary phase shift keying (BPSK) communication system contains pipe"},
    {"edge_id": "RDYNYFQP_E133", "edge_description": "10-tank system contains pseudo code generator"},
    {"edge_id": "RDYNYFQP_E134", "edge_description": "10-tank system contains carrier generator"},
    {"edge_id": "RDYNYFQP_E135", "edge_description": "10-tank system contains multiplier"},
    {"edge_id": "RDYNYFQP_E136", "edge_description": "10-tank system contains amplifier"},
    {"edge_id": "RDYNYFQP_E137", "edge_description": "10-tank system contains tank"},
    {"edge_id": "RDYNYFQP_E138", "edge_description": "10-tank system contains pipe"},
    {"edge_id": "RDYNYFQP_E139", "edge_description": "Binary phase shift keying (BPSK) communication system contains Stable states with 20dB noise"},
    {"edge_id": "RDYNYFQP_E140", "edge_description": "10-tank system contains Stable states with 20dB noise"},
    {"edge_id": "RDYNYFQP_E141", "edge_description": "stuck contains No Compound Fault"},
    {"edge_id": "RDYNYFQP_E142", "edge_description": "leakage contains No Compound Fault"},
    {"edge_id": "RDYNYFQP_E143", "edge_description": "rate anomaly contains No Compound Fault"},
    {"edge_id": "RDYNYFQP_E144", "edge_description": "power leakage contains No Compound Fault"},
    {"edge_id": "RDYNYFQP_E145", "edge_description": "timing anomaly contains No Compound Fault"},
    {"edge_id": "RDYNYFQP_E146", "edge_description": "conversion anomaly contains No Compound Fault"},
    {"edge_id": "RDYNYFQP_E147", "edge_description": "amplifier anomaly contains No Compound Fault"},
    {"edge_id": "RDYNYFQP_E148", "edge_description": "sensors for BPSK signals is collected on pseudo code generator"},
    {"edge_id": "RDYNYFQP_E149", "edge_description": "sensors for BPSK signals is collected on carrier generator"},
    {"edge_id": "RDYNYFQP_E150", "edge_description": "sensors for BPSK signals is collected on multiplier"},
    {"edge_id": "RDYNYFQP_E151", "edge_description": "sensors for BPSK signals is collected on amplifier"},
    {"edge_id": "RDYNYFQP_E152", "edge_description": "sensors for BPSK signals is collected on tank"},
    {"edge_id": "RDYNYFQP_E153", "edge_description": "sensors for BPSK signals is collected on pipe"},
    {"edge_id": "RDYNYFQP_E154", "edge_description": "level sensor is collected on pseudo code generator"}
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
| 1 | `RDYNYFQP_E125` | `contains` | 01-Object Domain | Industrial systems(Industrial) |  | 02-Object Type | Binary phase shift keying (BPSK) communication system |  |
| 2 | `RDYNYFQP_E126` | `contains` | 01-Object Domain | Industrial systems(Industrial) |  | 02-Object Type | 10-tank system |  |
| 3 | `RDYNYFQP_E127` | `contains` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 04-Fault Location | pseudo code generator |  |
| 4 | `RDYNYFQP_E128` | `contains` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 04-Fault Location | carrier generator |  |
| 5 | `RDYNYFQP_E129` | `contains` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 04-Fault Location | multiplier |  |
| 6 | `RDYNYFQP_E130` | `contains` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 04-Fault Location | amplifier |  |
| 7 | `RDYNYFQP_E131` | `contains` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 04-Fault Location | tank |  |
| 8 | `RDYNYFQP_E132` | `contains` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 04-Fault Location | pipe |  |
| 9 | `RDYNYFQP_E133` | `contains` | 02-Object Type | 10-tank system |  | 04-Fault Location | pseudo code generator |  |
| 10 | `RDYNYFQP_E134` | `contains` | 02-Object Type | 10-tank system |  | 04-Fault Location | carrier generator |  |
| 11 | `RDYNYFQP_E135` | `contains` | 02-Object Type | 10-tank system |  | 04-Fault Location | multiplier |  |
| 12 | `RDYNYFQP_E136` | `contains` | 02-Object Type | 10-tank system |  | 04-Fault Location | amplifier |  |
| 13 | `RDYNYFQP_E137` | `contains` | 02-Object Type | 10-tank system |  | 04-Fault Location | tank |  |
| 14 | `RDYNYFQP_E138` | `contains` | 02-Object Type | 10-tank system |  | 04-Fault Location | pipe |  |
| 15 | `RDYNYFQP_E139` | `contains` | 02-Object Type | Binary phase shift keying (BPSK) communication system |  | 03-Operating Conditions | Stable states with 20dB noise(Single Condition) |  |
| 16 | `RDYNYFQP_E140` | `contains` | 02-Object Type | 10-tank system |  | 03-Operating Conditions | Stable states with 20dB noise(Single Condition) |  |
| 17 | `RDYNYFQP_E141` | `contains` | 05-Fault Mode | stuck |  | 07-Compound Fault | No Compound Fault |  |
| 18 | `RDYNYFQP_E142` | `contains` | 05-Fault Mode | leakage |  | 07-Compound Fault | No Compound Fault |  |
| 19 | `RDYNYFQP_E143` | `contains` | 05-Fault Mode | rate anomaly |  | 07-Compound Fault | No Compound Fault |  |
| 20 | `RDYNYFQP_E144` | `contains` | 05-Fault Mode | power leakage |  | 07-Compound Fault | No Compound Fault |  |
| 21 | `RDYNYFQP_E145` | `contains` | 05-Fault Mode | timing anomaly |  | 07-Compound Fault | No Compound Fault |  |
| 22 | `RDYNYFQP_E146` | `contains` | 05-Fault Mode | conversion anomaly |  | 07-Compound Fault | No Compound Fault |  |
| 23 | `RDYNYFQP_E147` | `contains` | 05-Fault Mode | amplifier anomaly |  | 07-Compound Fault | No Compound Fault |  |
| 24 | `RDYNYFQP_E148` | `is collected on` | 11-Sensor Information | sensors for BPSK signals |  | 04-Fault Location | pseudo code generator |  |
| 25 | `RDYNYFQP_E149` | `is collected on` | 11-Sensor Information | sensors for BPSK signals |  | 04-Fault Location | carrier generator |  |
| 26 | `RDYNYFQP_E150` | `is collected on` | 11-Sensor Information | sensors for BPSK signals |  | 04-Fault Location | multiplier |  |
| 27 | `RDYNYFQP_E151` | `is collected on` | 11-Sensor Information | sensors for BPSK signals |  | 04-Fault Location | amplifier |  |
| 28 | `RDYNYFQP_E152` | `is collected on` | 11-Sensor Information | sensors for BPSK signals |  | 04-Fault Location | tank |  |
| 29 | `RDYNYFQP_E153` | `is collected on` | 11-Sensor Information | sensors for BPSK signals |  | 04-Fault Location | pipe |  |
| 30 | `RDYNYFQP_E154` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | pseudo code generator |  |

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

### ▶ For `is collected on` (Sensor Information type → Fault Location type)

**High Standard**: The paper must explicitly express that the sensor is **physically installed/arranged on** the target fault location, i.e., there is a description of the **physical positional relationship** between the sensor and the fault location.
The mere appearance in the dataset description of "a sensor used for a certain fault" is insufficient — the physical arrangement or installation context of the sensor must be reflected
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the relationship between the physical installation position of the sensor and the fault location, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
