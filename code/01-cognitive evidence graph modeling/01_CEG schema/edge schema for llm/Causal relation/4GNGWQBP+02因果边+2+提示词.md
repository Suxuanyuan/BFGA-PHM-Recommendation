# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：4GNGWQBP
- **Paper Title**：Fault diagnosis for circuit-breakers using adaptive chirp mode decomposition and attractor's morphological characteristics
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `4GNGWQBP`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "4GNGWQBP_E097", "edge_description": "roller has_fault_mode opening-spring problem"},
    {"edge_id": "4GNGWQBP_E098", "edge_description": "roller has_fault_mode roller anomaly"},
    {"edge_id": "4GNGWQBP_E099", "edge_description": "insulating rod malfunction contains Single Severity"},
    {"edge_id": "4GNGWQBP_E100", "edge_description": "shock absorber failure contains Single Severity"},
    {"edge_id": "4GNGWQBP_E101", "edge_description": "opening-spring problem contains Single Severity"},
    {"edge_id": "4GNGWQBP_E102", "edge_description": "roller anomaly contains Single Severity"},
    {"edge_id": "4GNGWQBP_E104", "edge_description": "insulating rod contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E105", "edge_description": "shock absorber contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E106", "edge_description": "opening-spring contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E107", "edge_description": "roller contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E108", "edge_description": "insulating rod malfunction contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E109", "edge_description": "shock absorber failure contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E110", "edge_description": "opening-spring problem contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E111", "edge_description": "roller anomaly contains_phm_task fault diagnosis"},
    {"edge_id": "4GNGWQBP_E113", "edge_description": "circuit-breaker induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E114", "edge_description": "circuit-breaker induces_problem highly time-varying and non-stationary vibration signals submerged in noise"},
    {"edge_id": "4GNGWQBP_E115", "edge_description": "standard operating mechanism triggers under laboratory conditions induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E116", "edge_description": "standard operating mechanism triggers under laboratory conditions induces_problem highly time-varying and non-stationary vibration signals submerged in noise"},
    {"edge_id": "4GNGWQBP_E117", "edge_description": "Single Severity induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E118", "edge_description": "Single Severity induces_problem highly time-varying and non-stationary vibration signals submerged in noise"},
    {"edge_id": "4GNGWQBP_E119", "edge_description": "No Compound Fault induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E120", "edge_description": "No Compound Fault induces_problem highly time-varying and non-stationary vibration signals submerged in noise"},
    {"edge_id": "4GNGWQBP_E121", "edge_description": "fault diagnosis induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E122", "edge_description": "fault diagnosis induces_problem highly time-varying and non-stationary vibration signals submerged in noise"},
    {"edge_id": "4GNGWQBP_E123", "edge_description": "vibration data recorded at least ten times in each condition induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E124", "edge_description": "vibration data recorded at least ten times in each condition induces_problem highly time-varying and non-stationary vibration signals submerged in noise"},
    {"edge_id": "4GNGWQBP_E125", "edge_description": "noise induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E126", "edge_description": "noise induces_problem highly time-varying and non-stationary vibration signals submerged in noise"},
    {"edge_id": "4GNGWQBP_E127", "edge_description": "not mentioned induces_problem complex and nonlinear mechanism system"},
    {"edge_id": "4GNGWQBP_E128", "edge_description": "not mentioned induces_problem highly time-varying and non-stationary vibration signals submerged in noise"}
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
| 1 | `4GNGWQBP_E097` | `has_fault_mode` | 04-Fault Location | roller |  | 05-Fault Mode | opening-spring problem |  |
| 2 | `4GNGWQBP_E098` | `has_fault_mode` | 04-Fault Location | roller |  | 05-Fault Mode | roller anomaly |  |
| 3 | `4GNGWQBP_E099` | `contains` | 05-Fault Mode | insulating rod malfunction |  | 06-Fault Severity | Single Severity |  |
| 4 | `4GNGWQBP_E100` | `contains` | 05-Fault Mode | shock absorber failure |  | 06-Fault Severity | Single Severity |  |
| 5 | `4GNGWQBP_E101` | `contains` | 05-Fault Mode | opening-spring problem |  | 06-Fault Severity | Single Severity |  |
| 6 | `4GNGWQBP_E102` | `contains` | 05-Fault Mode | roller anomaly |  | 06-Fault Severity | Single Severity |  |
| 7 | `4GNGWQBP_E104` | `contains_phm_task` | 04-Fault Location | insulating rod |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 8 | `4GNGWQBP_E105` | `contains_phm_task` | 04-Fault Location | shock absorber |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 9 | `4GNGWQBP_E106` | `contains_phm_task` | 04-Fault Location | opening-spring |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `4GNGWQBP_E107` | `contains_phm_task` | 04-Fault Location | roller |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `4GNGWQBP_E108` | `contains_phm_task` | 05-Fault Mode | insulating rod malfunction |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `4GNGWQBP_E109` | `contains_phm_task` | 05-Fault Mode | shock absorber failure |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `4GNGWQBP_E110` | `contains_phm_task` | 05-Fault Mode | opening-spring problem |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `4GNGWQBP_E111` | `contains_phm_task` | 05-Fault Mode | roller anomaly |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `4GNGWQBP_E113` | `induces_problem` | 02-Object Type | circuit-breaker |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 16 | `4GNGWQBP_E114` | `induces_problem` | 02-Object Type | circuit-breaker |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |
| 17 | `4GNGWQBP_E115` | `induces_problem` | 03-Operating Conditions | standard operating mechanism triggers under laboratory conditions(Single Condition) |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 18 | `4GNGWQBP_E116` | `induces_problem` | 03-Operating Conditions | standard operating mechanism triggers under laboratory conditions(Single Condition) |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |
| 19 | `4GNGWQBP_E117` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 20 | `4GNGWQBP_E118` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |
| 21 | `4GNGWQBP_E119` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 22 | `4GNGWQBP_E120` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |
| 23 | `4GNGWQBP_E121` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 24 | `4GNGWQBP_E122` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |
| 25 | `4GNGWQBP_E123` | `induces_problem` | 12-Training Data Availability | vibration data recorded at least ten times in each condition(Scarce) |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 26 | `4GNGWQBP_E124` | `induces_problem` | 12-Training Data Availability | vibration data recorded at least ten times in each condition(Scarce) |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |
| 27 | `4GNGWQBP_E125` | `induces_problem` | 13-Noise Level | noise(High Noise) |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 28 | `4GNGWQBP_E126` | `induces_problem` | 13-Noise Level | noise(High Noise) |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |
| 29 | `4GNGWQBP_E127` | `induces_problem` | 14-Computational Resource | not mentioned |  | 09-Problem Scenario | complex and nonlinear mechanism system(Complex Systems) |  |
| 30 | `4GNGWQBP_E128` | `induces_problem` | 14-Computational Resource | not mentioned |  | 09-Problem Scenario | highly time-varying and non-stationary vibration signals submerged in noise(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
