# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：BRECWDVQ
- **Paper Title**：Adaptive fault-tolerant PI tracking control for ship propulsion system
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `BRECWDVQ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "BRECWDVQ_E035", "edge_description": "ship propulsion system contains diesel engine"},
    {"edge_id": "BRECWDVQ_E036", "edge_description": "ship propulsion system contains pitch angle actuator"},
    {"edge_id": "BRECWDVQ_E037", "edge_description": "diesel engine contains diesel engine"},
    {"edge_id": "BRECWDVQ_E038", "edge_description": "diesel engine contains pitch angle actuator"},
    {"edge_id": "BRECWDVQ_E039", "edge_description": "pitch angle actuator contains diesel engine"},
    {"edge_id": "BRECWDVQ_E040", "edge_description": "pitch angle actuator contains pitch angle actuator"},
    {"edge_id": "BRECWDVQ_E041", "edge_description": "diesel engine contains operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0]"},
    {"edge_id": "BRECWDVQ_E042", "edge_description": "pitch angle actuator contains operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0]"},
    {"edge_id": "BRECWDVQ_E044", "edge_description": "shaft speed sensor is collected on diesel engine"},
    {"edge_id": "BRECWDVQ_E045", "edge_description": "shaft speed sensor is collected on pitch angle actuator"},
    {"edge_id": "BRECWDVQ_E048", "edge_description": "diesel engine has_fault_mode loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E049", "edge_description": "pitch angle actuator has_fault_mode loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E051", "edge_description": "diesel engine contains_phm_task adaptive fault-tolerant tracking control"},
    {"edge_id": "BRECWDVQ_E052", "edge_description": "pitch angle actuator contains_phm_task adaptive fault-tolerant tracking control"},
    {"edge_id": "BRECWDVQ_E053", "edge_description": "diesel engine contains_phm_task adaptive fault-tolerant tracking control"},
    {"edge_id": "BRECWDVQ_E054", "edge_description": "pitch angle actuator contains_phm_task adaptive fault-tolerant tracking control"},
    {"edge_id": "BRECWDVQ_E057", "edge_description": "diesel engine induces_problem simultaneous diesel engine gain fault and pitch angle actuator fault"},
    {"edge_id": "BRECWDVQ_E058", "edge_description": "diesel engine induces_problem disturbances and unknown loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E059", "edge_description": "pitch angle actuator induces_problem simultaneous diesel engine gain fault and pitch angle actuator fault"},
    {"edge_id": "BRECWDVQ_E060", "edge_description": "pitch angle actuator induces_problem disturbances and unknown loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E061", "edge_description": "operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0] induces_problem simultaneous diesel engine gain fault and pitch angle actuator fault"},
    {"edge_id": "BRECWDVQ_E062", "edge_description": "operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0] induces_problem disturbances and unknown loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E063", "edge_description": "loss of effectiveness of 50%, loss of 90% effectiveness induces_problem simultaneous diesel engine gain fault and pitch angle actuator fault"},
    {"edge_id": "BRECWDVQ_E064", "edge_description": "loss of effectiveness of 50%, loss of 90% effectiveness induces_problem disturbances and unknown loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E065", "edge_description": "simultaneous diesel engine gain fault and pitch angle actuator fault induces_problem simultaneous diesel engine gain fault and pitch angle actuator fault"},
    {"edge_id": "BRECWDVQ_E066", "edge_description": "simultaneous diesel engine gain fault and pitch angle actuator fault induces_problem disturbances and unknown loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E067", "edge_description": "adaptive fault-tolerant tracking control induces_problem simultaneous diesel engine gain fault and pitch angle actuator fault"},
    {"edge_id": "BRECWDVQ_E068", "edge_description": "adaptive fault-tolerant tracking control induces_problem disturbances and unknown loss of actuator effectiveness"},
    {"edge_id": "BRECWDVQ_E069", "edge_description": "Sufficient induces_problem simultaneous diesel engine gain fault and pitch angle actuator fault"},
    {"edge_id": "BRECWDVQ_E070", "edge_description": "Sufficient induces_problem disturbances and unknown loss of actuator effectiveness"}
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
| 1 | `BRECWDVQ_E035` | `contains` | 01-Object Domain | ship propulsion system(Marine) |  | 02-Object Type | diesel engine |  |
| 2 | `BRECWDVQ_E036` | `contains` | 01-Object Domain | ship propulsion system(Marine) |  | 02-Object Type | pitch angle actuator |  |
| 3 | `BRECWDVQ_E037` | `contains` | 02-Object Type | diesel engine |  | 04-Fault Location | diesel engine |  |
| 4 | `BRECWDVQ_E038` | `contains` | 02-Object Type | diesel engine |  | 04-Fault Location | pitch angle actuator |  |
| 5 | `BRECWDVQ_E039` | `contains` | 02-Object Type | pitch angle actuator |  | 04-Fault Location | diesel engine |  |
| 6 | `BRECWDVQ_E040` | `contains` | 02-Object Type | pitch angle actuator |  | 04-Fault Location | pitch angle actuator |  |
| 7 | `BRECWDVQ_E041` | `contains` | 02-Object Type | diesel engine |  | 03-Operating Conditions | operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0](Single Condition) |  |
| 8 | `BRECWDVQ_E042` | `contains` | 02-Object Type | pitch angle actuator |  | 03-Operating Conditions | operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0](Single Condition) |  |
| 9 | `BRECWDVQ_E044` | `is collected on` | 11-Sensor Information | shaft speed sensor |  | 04-Fault Location | diesel engine |  |
| 10 | `BRECWDVQ_E045` | `is collected on` | 11-Sensor Information | shaft speed sensor |  | 04-Fault Location | pitch angle actuator |  |
| 11 | `BRECWDVQ_E048` | `has_fault_mode` | 04-Fault Location | diesel engine |  | 05-Fault Mode | loss of actuator effectiveness |  |
| 12 | `BRECWDVQ_E049` | `has_fault_mode` | 04-Fault Location | pitch angle actuator |  | 05-Fault Mode | loss of actuator effectiveness |  |
| 13 | `BRECWDVQ_E051` | `contains_phm_task` | 02-Object Type | diesel engine |  | 08-PHM Task | adaptive fault-tolerant tracking control(Other Task) |  |
| 14 | `BRECWDVQ_E052` | `contains_phm_task` | 02-Object Type | pitch angle actuator |  | 08-PHM Task | adaptive fault-tolerant tracking control(Other Task) |  |
| 15 | `BRECWDVQ_E053` | `contains_phm_task` | 04-Fault Location | diesel engine |  | 08-PHM Task | adaptive fault-tolerant tracking control(Other Task) |  |
| 16 | `BRECWDVQ_E054` | `contains_phm_task` | 04-Fault Location | pitch angle actuator |  | 08-PHM Task | adaptive fault-tolerant tracking control(Other Task) |  |
| 17 | `BRECWDVQ_E057` | `induces_problem` | 02-Object Type | diesel engine |  | 09-Problem Scenario | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Faults) |  |
| 18 | `BRECWDVQ_E058` | `induces_problem` | 02-Object Type | diesel engine |  | 09-Problem Scenario | disturbances and unknown loss of actuator effectiveness(Uncertainty) |  |
| 19 | `BRECWDVQ_E059` | `induces_problem` | 02-Object Type | pitch angle actuator |  | 09-Problem Scenario | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Faults) |  |
| 20 | `BRECWDVQ_E060` | `induces_problem` | 02-Object Type | pitch angle actuator |  | 09-Problem Scenario | disturbances and unknown loss of actuator effectiveness(Uncertainty) |  |
| 21 | `BRECWDVQ_E061` | `induces_problem` | 03-Operating Conditions | operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0](Single Condition) |  | 09-Problem Scenario | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Faults) |  |
| 22 | `BRECWDVQ_E062` | `induces_problem` | 03-Operating Conditions | operating point x_0 = [10.66; 5], u_0 = [0.85; Y_0](Single Condition) |  | 09-Problem Scenario | disturbances and unknown loss of actuator effectiveness(Uncertainty) |  |
| 23 | `BRECWDVQ_E063` | `induces_problem` | 06-Fault Severity | loss of effectiveness of 50%, loss of 90% effectiveness(Single Severity) |  | 09-Problem Scenario | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Faults) |  |
| 24 | `BRECWDVQ_E064` | `induces_problem` | 06-Fault Severity | loss of effectiveness of 50%, loss of 90% effectiveness(Single Severity) |  | 09-Problem Scenario | disturbances and unknown loss of actuator effectiveness(Uncertainty) |  |
| 25 | `BRECWDVQ_E065` | `induces_problem` | 07-Compound Fault | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Fault Across Structures) |  | 09-Problem Scenario | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Faults) |  |
| 26 | `BRECWDVQ_E066` | `induces_problem` | 07-Compound Fault | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Fault Across Structures) |  | 09-Problem Scenario | disturbances and unknown loss of actuator effectiveness(Uncertainty) |  |
| 27 | `BRECWDVQ_E067` | `induces_problem` | 08-PHM Task | adaptive fault-tolerant tracking control(Other Task) |  | 09-Problem Scenario | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Faults) |  |
| 28 | `BRECWDVQ_E068` | `induces_problem` | 08-PHM Task | adaptive fault-tolerant tracking control(Other Task) |  | 09-Problem Scenario | disturbances and unknown loss of actuator effectiveness(Uncertainty) |  |
| 29 | `BRECWDVQ_E069` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | simultaneous diesel engine gain fault and pitch angle actuator fault(Compound Faults) |  |
| 30 | `BRECWDVQ_E070` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | disturbances and unknown loss of actuator effectiveness(Uncertainty) |  |

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
