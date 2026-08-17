# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：KQ3DMBWB
- **Paper Title**：Early and extremely early multi-label fault diagnosis in induction motors
- **Number of Candidate Edges to Judge**：24 

---

## II. LLM Input

> **Input Material**: Reference ID `KQ3DMBWB`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "KQ3DMBWB_E137", "edge_description": "rotor contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E138", "edge_description": "rotor pulley contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E139", "edge_description": "pulley-belt system contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E140", "edge_description": "bearing contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E141", "edge_description": "broken rotor bar contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E142", "edge_description": "unbalance contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E143", "edge_description": "misalignment contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E144", "edge_description": "bearing defect contains_phm_task multi-label fault diagnosis"},
    {"edge_id": "KQ3DMBWB_E146", "edge_description": "induction motor induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E147", "edge_description": "induction motor induces_problem multiple sensor information from different physical magnitudes"},
    {"edge_id": "KQ3DMBWB_E148", "edge_description": "three types of load conditions (no-load, half-load, and full-load) and three operating frequencies (3 Hz, 30 Hz, and direct supply) induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E149", "edge_description": "three types of load conditions (no-load, half-load, and full-load) and three operating frequencies (3 Hz, 30 Hz, and direct supply) induces_problem multiple sensor information from different physical magnitudes"},
    {"edge_id": "KQ3DMBWB_E150", "edge_description": "rough-hole of 2 mm diameter, 1.191 mm tungsten drill bit induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E151", "edge_description": "rough-hole of 2 mm diameter, 1.191 mm tungsten drill bit induces_problem multiple sensor information from different physical magnitudes"},
    {"edge_id": "KQ3DMBWB_E152", "edge_description": "combined, and simultaneous faulty conditions induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E153", "edge_description": "combined, and simultaneous faulty conditions induces_problem multiple sensor information from different physical magnitudes"},
    {"edge_id": "KQ3DMBWB_E154", "edge_description": "multi-label fault diagnosis induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E155", "edge_description": "multi-label fault diagnosis induces_problem multiple sensor information from different physical magnitudes"},
    {"edge_id": "KQ3DMBWB_E156", "edge_description": "2 521 instances induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E157", "edge_description": "2 521 instances induces_problem multiple sensor information from different physical magnitudes"},
    {"edge_id": "KQ3DMBWB_E158", "edge_description": "noise subspace induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E159", "edge_description": "noise subspace induces_problem multiple sensor information from different physical magnitudes"},
    {"edge_id": "KQ3DMBWB_E160", "edge_description": "low computational burden of this tool means that it can be used for real-time condition monitoring induces_problem simultaneous fault detection"},
    {"edge_id": "KQ3DMBWB_E161", "edge_description": "low computational burden of this tool means that it can be used for real-time condition monitoring induces_problem multiple sensor information from different physical magnitudes"}
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
| 1 | `KQ3DMBWB_E137` | `contains_phm_task` | 04-Fault Location | rotor |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 2 | `KQ3DMBWB_E138` | `contains_phm_task` | 04-Fault Location | rotor pulley |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 3 | `KQ3DMBWB_E139` | `contains_phm_task` | 04-Fault Location | pulley-belt system |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 4 | `KQ3DMBWB_E140` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 5 | `KQ3DMBWB_E141` | `contains_phm_task` | 05-Fault Mode | broken rotor bar |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 6 | `KQ3DMBWB_E142` | `contains_phm_task` | 05-Fault Mode | unbalance |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 7 | `KQ3DMBWB_E143` | `contains_phm_task` | 05-Fault Mode | misalignment |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 8 | `KQ3DMBWB_E144` | `contains_phm_task` | 05-Fault Mode | bearing defect |  | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  |
| 9 | `KQ3DMBWB_E146` | `induces_problem` | 02-Object Type | induction motor |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 10 | `KQ3DMBWB_E147` | `induces_problem` | 02-Object Type | induction motor |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |
| 11 | `KQ3DMBWB_E148` | `induces_problem` | 03-Operating Conditions | three types of load conditions (no-load, half-load, and full-load) and three operating frequencies (3 Hz, 30 Hz, and direct supply)(Multiple Conditions) |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 12 | `KQ3DMBWB_E149` | `induces_problem` | 03-Operating Conditions | three types of load conditions (no-load, half-load, and full-load) and three operating frequencies (3 Hz, 30 Hz, and direct supply)(Multiple Conditions) |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |
| 13 | `KQ3DMBWB_E150` | `induces_problem` | 06-Fault Severity | rough-hole of 2 mm diameter, 1.191 mm tungsten drill bit(Single Severity) |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 14 | `KQ3DMBWB_E151` | `induces_problem` | 06-Fault Severity | rough-hole of 2 mm diameter, 1.191 mm tungsten drill bit(Single Severity) |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |
| 15 | `KQ3DMBWB_E152` | `induces_problem` | 07-Compound Fault | combined, and simultaneous faulty conditions(Compound Fault Across Structures) |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 16 | `KQ3DMBWB_E153` | `induces_problem` | 07-Compound Fault | combined, and simultaneous faulty conditions(Compound Fault Across Structures) |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |
| 17 | `KQ3DMBWB_E154` | `induces_problem` | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 18 | `KQ3DMBWB_E155` | `induces_problem` | 08-PHM Task | multi-label fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |
| 19 | `KQ3DMBWB_E156` | `induces_problem` | 12-Training Data Availability | 2 521 instances(Sufficient) |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 20 | `KQ3DMBWB_E157` | `induces_problem` | 12-Training Data Availability | 2 521 instances(Sufficient) |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |
| 21 | `KQ3DMBWB_E158` | `induces_problem` | 13-Noise Level | noise subspace(Normal) |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 22 | `KQ3DMBWB_E159` | `induces_problem` | 13-Noise Level | noise subspace(Normal) |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |
| 23 | `KQ3DMBWB_E160` | `induces_problem` | 14-Computational Resource | low computational burden of this tool means that it can be used for real-time condition monitoring(Low Resource Consumption) |  | 09-Problem Scenario | simultaneous fault detection(Compound Faults) |  |
| 24 | `KQ3DMBWB_E161` | `induces_problem` | 14-Computational Resource | low computational burden of this tool means that it can be used for real-time condition monitoring(Low Resource Consumption) |  | 09-Problem Scenario | multiple sensor information from different physical magnitudes(Multi-Source Heterogeneous / Multimodal Data) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 24 edges)*
