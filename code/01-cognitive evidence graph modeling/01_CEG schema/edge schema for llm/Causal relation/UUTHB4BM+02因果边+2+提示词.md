# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：UUTHB4BM
- **Paper Title**：Neural adaptive observer-based sensor and actuator fault detection in nonlinear systems: Application in UAV
- **Number of Candidate Edges to Judge**：27 

---

## II. LLM Input

> **Input Material**: Reference ID `UUTHB4BM`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "UUTHB4BM_E072", "edge_description": "angular rate sensors contains_phm_task sensor and actuator fault detection"},
    {"edge_id": "UUTHB4BM_E073", "edge_description": "actuators contains_phm_task sensor and actuator fault detection"},
    {"edge_id": "UUTHB4BM_E074", "edge_description": "actuator (aileron, elevator, rudder) contains_phm_task sensor and actuator fault detection"},
    {"edge_id": "UUTHB4BM_E075", "edge_description": "angular rate sensor (p, q, r) contains_phm_task sensor and actuator fault detection"},
    {"edge_id": "UUTHB4BM_E076", "edge_description": "abrupt fault contains_phm_task sensor and actuator fault detection"},
    {"edge_id": "UUTHB4BM_E077", "edge_description": "incipient fault contains_phm_task sensor and actuator fault detection"},
    {"edge_id": "UUTHB4BM_E078", "edge_description": "intermittent fault contains_phm_task sensor and actuator fault detection"},
    {"edge_id": "UUTHB4BM_E080", "edge_description": "WVU YF-22 unmanned aircraft induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E081", "edge_description": "WVU YF-22 unmanned aircraft induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E082", "edge_description": "angular rate sensors induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E083", "edge_description": "angular rate sensors induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E084", "edge_description": "actuators induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E085", "edge_description": "actuators induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E086", "edge_description": "nonlinear dynamic flight conditions induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E087", "edge_description": "nonlinear dynamic flight conditions induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E088", "edge_description": "null induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E089", "edge_description": "null induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E090", "edge_description": "simultaneous faults induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E091", "edge_description": "simultaneous faults induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E092", "edge_description": "sensor and actuator fault detection induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E093", "edge_description": "sensor and actuator fault detection induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E094", "edge_description": "Online adaptation induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E095", "edge_description": "Online adaptation induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E096", "edge_description": "Noise added to the system induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E097", "edge_description": "Noise added to the system induces_problem multiple simultaneous faults"},
    {"edge_id": "UUTHB4BM_E098", "edge_description": "efficient in terms of computational load induces_problem system's uncertainties and noise"},
    {"edge_id": "UUTHB4BM_E099", "edge_description": "efficient in terms of computational load induces_problem multiple simultaneous faults"}
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
| 1 | `UUTHB4BM_E072` | `contains_phm_task` | 02-Object Type | angular rate sensors |  | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  |
| 2 | `UUTHB4BM_E073` | `contains_phm_task` | 02-Object Type | actuators |  | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  |
| 3 | `UUTHB4BM_E074` | `contains_phm_task` | 04-Fault Location | actuator (aileron, elevator, rudder) |  | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  |
| 4 | `UUTHB4BM_E075` | `contains_phm_task` | 04-Fault Location | angular rate sensor (p, q, r) |  | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  |
| 5 | `UUTHB4BM_E076` | `contains_phm_task` | 05-Fault Mode | abrupt fault |  | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  |
| 6 | `UUTHB4BM_E077` | `contains_phm_task` | 05-Fault Mode | incipient fault |  | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  |
| 7 | `UUTHB4BM_E078` | `contains_phm_task` | 05-Fault Mode | intermittent fault |  | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  |
| 8 | `UUTHB4BM_E080` | `induces_problem` | 02-Object Type | WVU YF-22 unmanned aircraft |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 9 | `UUTHB4BM_E081` | `induces_problem` | 02-Object Type | WVU YF-22 unmanned aircraft |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 10 | `UUTHB4BM_E082` | `induces_problem` | 02-Object Type | angular rate sensors |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 11 | `UUTHB4BM_E083` | `induces_problem` | 02-Object Type | angular rate sensors |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 12 | `UUTHB4BM_E084` | `induces_problem` | 02-Object Type | actuators |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 13 | `UUTHB4BM_E085` | `induces_problem` | 02-Object Type | actuators |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 14 | `UUTHB4BM_E086` | `induces_problem` | 03-Operating Conditions | nonlinear dynamic flight conditions(Variable Conditions) |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 15 | `UUTHB4BM_E087` | `induces_problem` | 03-Operating Conditions | nonlinear dynamic flight conditions(Variable Conditions) |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 16 | `UUTHB4BM_E088` | `induces_problem` | 06-Fault Severity | null(Single Severity) |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 17 | `UUTHB4BM_E089` | `induces_problem` | 06-Fault Severity | null(Single Severity) |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 18 | `UUTHB4BM_E090` | `induces_problem` | 07-Compound Fault | simultaneous faults(Compound Fault Within Same Structure) |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 19 | `UUTHB4BM_E091` | `induces_problem` | 07-Compound Fault | simultaneous faults(Compound Fault Within Same Structure) |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 20 | `UUTHB4BM_E092` | `induces_problem` | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 21 | `UUTHB4BM_E093` | `induces_problem` | 08-PHM Task | sensor and actuator fault detection(Detection Task) |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 22 | `UUTHB4BM_E094` | `induces_problem` | 12-Training Data Availability | Online adaptation(Sufficient) |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 23 | `UUTHB4BM_E095` | `induces_problem` | 12-Training Data Availability | Online adaptation(Sufficient) |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 24 | `UUTHB4BM_E096` | `induces_problem` | 13-Noise Level | Noise added to the system(High Noise) |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 25 | `UUTHB4BM_E097` | `induces_problem` | 13-Noise Level | Noise added to the system(High Noise) |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |
| 26 | `UUTHB4BM_E098` | `induces_problem` | 14-Computational Resource | efficient in terms of computational load(Low Resource Consumption) |  | 09-Problem Scenario | system's uncertainties and noise(Uncertainty) |  |
| 27 | `UUTHB4BM_E099` | `induces_problem` | 14-Computational Resource | efficient in terms of computational load(Low Resource Consumption) |  | 09-Problem Scenario | multiple simultaneous faults(Compound Faults) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 27 edges)*
