# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PNZZPWPS
- **Paper Title**：Active Fault Diagnosis on a Hydraulic Pitch System Based on Frequency-Domain Identification
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `PNZZPWPS`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PNZZPWPS_E074", "edge_description": "hydraulic oil has_fault_mode drop in the supply pressure"},
    {"edge_id": "PNZZPWPS_E075", "edge_description": "hydraulic oil has_fault_mode air contamination"},
    {"edge_id": "PNZZPWPS_E076", "edge_description": "hydraulic oil has_fault_mode water contamination"},
    {"edge_id": "PNZZPWPS_E077", "edge_description": "high bearing friction contains R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95"},
    {"edge_id": "PNZZPWPS_E078", "edge_description": "drop in the supply pressure contains R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95"},
    {"edge_id": "PNZZPWPS_E079", "edge_description": "air contamination contains R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95"},
    {"edge_id": "PNZZPWPS_E080", "edge_description": "water contamination contains R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95"},
    {"edge_id": "PNZZPWPS_E081", "edge_description": "hydraulic pitch actuator contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E082", "edge_description": "pitch bearing contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E083", "edge_description": "pitch bearing contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E084", "edge_description": "hydraulic pump contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E085", "edge_description": "hydraulic oil contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E086", "edge_description": "high bearing friction contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E087", "edge_description": "drop in the supply pressure contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E088", "edge_description": "air contamination contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E089", "edge_description": "water contamination contains_phm_task Active model-based fault detection and isolation (FDI)"},
    {"edge_id": "PNZZPWPS_E091", "edge_description": "hydraulic pitch actuator induces_problem noise in measurements and stochastic nonlinear distortions"},
    {"edge_id": "PNZZPWPS_E092", "edge_description": "hydraulic pitch actuator induces_problem incipient multiplicative faults"},
    {"edge_id": "PNZZPWPS_E093", "edge_description": "pitch bearing induces_problem noise in measurements and stochastic nonlinear distortions"},
    {"edge_id": "PNZZPWPS_E094", "edge_description": "pitch bearing induces_problem incipient multiplicative faults"},
    {"edge_id": "PNZZPWPS_E095", "edge_description": "Operating conditions (mean wind speed and turbulence intensity) induces_problem noise in measurements and stochastic nonlinear distortions"},
    {"edge_id": "PNZZPWPS_E096", "edge_description": "Operating conditions (mean wind speed and turbulence intensity) induces_problem incipient multiplicative faults"},
    {"edge_id": "PNZZPWPS_E097", "edge_description": "R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95 induces_problem noise in measurements and stochastic nonlinear distortions"},
    {"edge_id": "PNZZPWPS_E098", "edge_description": "R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95 induces_problem incipient multiplicative faults"},
    {"edge_id": "PNZZPWPS_E099", "edge_description": "No Compound Fault induces_problem noise in measurements and stochastic nonlinear distortions"},
    {"edge_id": "PNZZPWPS_E100", "edge_description": "No Compound Fault induces_problem incipient multiplicative faults"},
    {"edge_id": "PNZZPWPS_E101", "edge_description": "Active model-based fault detection and isolation (FDI) induces_problem noise in measurements and stochastic nonlinear distortions"},
    {"edge_id": "PNZZPWPS_E102", "edge_description": "Active model-based fault detection and isolation (FDI) induces_problem incipient multiplicative faults"},
    {"edge_id": "PNZZPWPS_E103", "edge_description": "45 identification experiments and 250 validation experiments induces_problem noise in measurements and stochastic nonlinear distortions"},
    {"edge_id": "PNZZPWPS_E104", "edge_description": "45 identification experiments and 250 validation experiments induces_problem incipient multiplicative faults"}
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
| 1 | `PNZZPWPS_E074` | `has_fault_mode` | 04-Fault Location | hydraulic oil |  | 05-Fault Mode | drop in the supply pressure |  |
| 2 | `PNZZPWPS_E075` | `has_fault_mode` | 04-Fault Location | hydraulic oil |  | 05-Fault Mode | air contamination |  |
| 3 | `PNZZPWPS_E076` | `has_fault_mode` | 04-Fault Location | hydraulic oil |  | 05-Fault Mode | water contamination |  |
| 4 | `PNZZPWPS_E077` | `contains` | 05-Fault Mode | high bearing friction |  | 06-Fault Severity | R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95(Multiple Severities) |  |
| 5 | `PNZZPWPS_E078` | `contains` | 05-Fault Mode | drop in the supply pressure |  | 06-Fault Severity | R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95(Multiple Severities) |  |
| 6 | `PNZZPWPS_E079` | `contains` | 05-Fault Mode | air contamination |  | 06-Fault Severity | R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95(Multiple Severities) |  |
| 7 | `PNZZPWPS_E080` | `contains` | 05-Fault Mode | water contamination |  | 06-Fault Severity | R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95(Multiple Severities) |  |
| 8 | `PNZZPWPS_E081` | `contains_phm_task` | 02-Object Type | hydraulic pitch actuator |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 9 | `PNZZPWPS_E082` | `contains_phm_task` | 02-Object Type | pitch bearing |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 10 | `PNZZPWPS_E083` | `contains_phm_task` | 04-Fault Location | pitch bearing |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 11 | `PNZZPWPS_E084` | `contains_phm_task` | 04-Fault Location | hydraulic pump |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 12 | `PNZZPWPS_E085` | `contains_phm_task` | 04-Fault Location | hydraulic oil |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 13 | `PNZZPWPS_E086` | `contains_phm_task` | 05-Fault Mode | high bearing friction |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 14 | `PNZZPWPS_E087` | `contains_phm_task` | 05-Fault Mode | drop in the supply pressure |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 15 | `PNZZPWPS_E088` | `contains_phm_task` | 05-Fault Mode | air contamination |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 16 | `PNZZPWPS_E089` | `contains_phm_task` | 05-Fault Mode | water contamination |  | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  |
| 17 | `PNZZPWPS_E091` | `induces_problem` | 02-Object Type | hydraulic pitch actuator |  | 09-Problem Scenario | noise in measurements and stochastic nonlinear distortions(Uncertainty) |  |
| 18 | `PNZZPWPS_E092` | `induces_problem` | 02-Object Type | hydraulic pitch actuator |  | 09-Problem Scenario | incipient multiplicative faults(Early Degradation Prediction) |  |
| 19 | `PNZZPWPS_E093` | `induces_problem` | 02-Object Type | pitch bearing |  | 09-Problem Scenario | noise in measurements and stochastic nonlinear distortions(Uncertainty) |  |
| 20 | `PNZZPWPS_E094` | `induces_problem` | 02-Object Type | pitch bearing |  | 09-Problem Scenario | incipient multiplicative faults(Early Degradation Prediction) |  |
| 21 | `PNZZPWPS_E095` | `induces_problem` | 03-Operating Conditions | Operating conditions (mean wind speed and turbulence intensity)(Multiple Conditions) |  | 09-Problem Scenario | noise in measurements and stochastic nonlinear distortions(Uncertainty) |  |
| 22 | `PNZZPWPS_E096` | `induces_problem` | 03-Operating Conditions | Operating conditions (mean wind speed and turbulence intensity)(Multiple Conditions) |  | 09-Problem Scenario | incipient multiplicative faults(Early Degradation Prediction) |  |
| 23 | `PNZZPWPS_E097` | `induces_problem` | 06-Fault Severity | R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95(Multiple Severities) |  | 09-Problem Scenario | noise in measurements and stochastic nonlinear distortions(Uncertainty) |  |
| 24 | `PNZZPWPS_E098` | `induces_problem` | 06-Fault Severity | R >= 7.3%, mu >= 0.004, PS/P_S^N <= 0.95(Multiple Severities) |  | 09-Problem Scenario | incipient multiplicative faults(Early Degradation Prediction) |  |
| 25 | `PNZZPWPS_E099` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise in measurements and stochastic nonlinear distortions(Uncertainty) |  |
| 26 | `PNZZPWPS_E100` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | incipient multiplicative faults(Early Degradation Prediction) |  |
| 27 | `PNZZPWPS_E101` | `induces_problem` | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  | 09-Problem Scenario | noise in measurements and stochastic nonlinear distortions(Uncertainty) |  |
| 28 | `PNZZPWPS_E102` | `induces_problem` | 08-PHM Task | Active model-based fault detection and isolation (FDI)(Diagnosis Task) |  | 09-Problem Scenario | incipient multiplicative faults(Early Degradation Prediction) |  |
| 29 | `PNZZPWPS_E103` | `induces_problem` | 12-Training Data Availability | 45 identification experiments and 250 validation experiments(Sufficient) |  | 09-Problem Scenario | noise in measurements and stochastic nonlinear distortions(Uncertainty) |  |
| 30 | `PNZZPWPS_E104` | `induces_problem` | 12-Training Data Availability | 45 identification experiments and 250 validation experiments(Sufficient) |  | 09-Problem Scenario | incipient multiplicative faults(Early Degradation Prediction) |  |

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
