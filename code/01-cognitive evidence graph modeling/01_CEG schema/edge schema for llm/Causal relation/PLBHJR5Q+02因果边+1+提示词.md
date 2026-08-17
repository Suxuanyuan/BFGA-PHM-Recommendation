# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PLBHJR5Q
- **Paper Title**：A novel fault diagnosis method for aircraft actuator based on ensemble model
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `PLBHJR5Q`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PLBHJR5Q_E104", "edge_description": "floating fault contains No Compound Fault"},
    {"edge_id": "PLBHJR5Q_E105", "edge_description": "instability fault contains No Compound Fault"},
    {"edge_id": "PLBHJR5Q_E106", "edge_description": "no response fault contains No Compound Fault"},
    {"edge_id": "PLBHJR5Q_E107", "edge_description": "slow response contains No Compound Fault"},
    {"edge_id": "PLBHJR5Q_E108", "edge_description": "stuck fault contains No Compound Fault"},
    {"edge_id": "PLBHJR5Q_E109", "edge_description": "constant deviation fault contains No Compound Fault"},
    {"edge_id": "PLBHJR5Q_E111", "edge_description": "rudder deflection angle sensor can obviously reflect floating fault"},
    {"edge_id": "PLBHJR5Q_E112", "edge_description": "rudder deflection angle sensor can obviously reflect instability fault"},
    {"edge_id": "PLBHJR5Q_E113", "edge_description": "rudder deflection angle sensor can obviously reflect no response fault"},
    {"edge_id": "PLBHJR5Q_E114", "edge_description": "rudder deflection angle sensor can obviously reflect slow response"},
    {"edge_id": "PLBHJR5Q_E115", "edge_description": "rudder deflection angle sensor can obviously reflect stuck fault"},
    {"edge_id": "PLBHJR5Q_E116", "edge_description": "rudder deflection angle sensor can obviously reflect constant deviation fault"},
    {"edge_id": "PLBHJR5Q_E118", "edge_description": "actuator has_fault_mode floating fault"},
    {"edge_id": "PLBHJR5Q_E119", "edge_description": "actuator has_fault_mode instability fault"},
    {"edge_id": "PLBHJR5Q_E120", "edge_description": "actuator has_fault_mode no response fault"},
    {"edge_id": "PLBHJR5Q_E121", "edge_description": "actuator has_fault_mode slow response"},
    {"edge_id": "PLBHJR5Q_E122", "edge_description": "actuator has_fault_mode stuck fault"},
    {"edge_id": "PLBHJR5Q_E123", "edge_description": "actuator has_fault_mode constant deviation fault"},
    {"edge_id": "PLBHJR5Q_E124", "edge_description": "floating fault contains fault magnitude"},
    {"edge_id": "PLBHJR5Q_E125", "edge_description": "instability fault contains fault magnitude"},
    {"edge_id": "PLBHJR5Q_E126", "edge_description": "no response fault contains fault magnitude"},
    {"edge_id": "PLBHJR5Q_E127", "edge_description": "slow response contains fault magnitude"},
    {"edge_id": "PLBHJR5Q_E128", "edge_description": "stuck fault contains fault magnitude"},
    {"edge_id": "PLBHJR5Q_E129", "edge_description": "constant deviation fault contains fault magnitude"},
    {"edge_id": "PLBHJR5Q_E132", "edge_description": "floating fault contains_phm_task fault diagnosis"},
    {"edge_id": "PLBHJR5Q_E133", "edge_description": "instability fault contains_phm_task fault diagnosis"},
    {"edge_id": "PLBHJR5Q_E134", "edge_description": "no response fault contains_phm_task fault diagnosis"},
    {"edge_id": "PLBHJR5Q_E135", "edge_description": "slow response contains_phm_task fault diagnosis"},
    {"edge_id": "PLBHJR5Q_E136", "edge_description": "stuck fault contains_phm_task fault diagnosis"},
    {"edge_id": "PLBHJR5Q_E137", "edge_description": "constant deviation fault contains_phm_task fault diagnosis"}
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
| 1 | `PLBHJR5Q_E104` | `contains` | 05-Fault Mode | floating fault |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `PLBHJR5Q_E105` | `contains` | 05-Fault Mode | instability fault |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `PLBHJR5Q_E106` | `contains` | 05-Fault Mode | no response fault |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `PLBHJR5Q_E107` | `contains` | 05-Fault Mode | slow response |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `PLBHJR5Q_E108` | `contains` | 05-Fault Mode | stuck fault |  | 07-Compound Fault | No Compound Fault |  |
| 6 | `PLBHJR5Q_E109` | `contains` | 05-Fault Mode | constant deviation fault |  | 07-Compound Fault | No Compound Fault |  |
| 7 | `PLBHJR5Q_E111` | `can obviously reflect` | 11-Sensor Information | rudder deflection angle sensor |  | 05-Fault Mode | floating fault |  |
| 8 | `PLBHJR5Q_E112` | `can obviously reflect` | 11-Sensor Information | rudder deflection angle sensor |  | 05-Fault Mode | instability fault |  |
| 9 | `PLBHJR5Q_E113` | `can obviously reflect` | 11-Sensor Information | rudder deflection angle sensor |  | 05-Fault Mode | no response fault |  |
| 10 | `PLBHJR5Q_E114` | `can obviously reflect` | 11-Sensor Information | rudder deflection angle sensor |  | 05-Fault Mode | slow response |  |
| 11 | `PLBHJR5Q_E115` | `can obviously reflect` | 11-Sensor Information | rudder deflection angle sensor |  | 05-Fault Mode | stuck fault |  |
| 12 | `PLBHJR5Q_E116` | `can obviously reflect` | 11-Sensor Information | rudder deflection angle sensor |  | 05-Fault Mode | constant deviation fault |  |
| 13 | `PLBHJR5Q_E118` | `has_fault_mode` | 04-Fault Location | actuator |  | 05-Fault Mode | floating fault |  |
| 14 | `PLBHJR5Q_E119` | `has_fault_mode` | 04-Fault Location | actuator |  | 05-Fault Mode | instability fault |  |
| 15 | `PLBHJR5Q_E120` | `has_fault_mode` | 04-Fault Location | actuator |  | 05-Fault Mode | no response fault |  |
| 16 | `PLBHJR5Q_E121` | `has_fault_mode` | 04-Fault Location | actuator |  | 05-Fault Mode | slow response |  |
| 17 | `PLBHJR5Q_E122` | `has_fault_mode` | 04-Fault Location | actuator |  | 05-Fault Mode | stuck fault |  |
| 18 | `PLBHJR5Q_E123` | `has_fault_mode` | 04-Fault Location | actuator |  | 05-Fault Mode | constant deviation fault |  |
| 19 | `PLBHJR5Q_E124` | `contains` | 05-Fault Mode | floating fault |  | 06-Fault Severity | fault magnitude(Multiple Severities) |  |
| 20 | `PLBHJR5Q_E125` | `contains` | 05-Fault Mode | instability fault |  | 06-Fault Severity | fault magnitude(Multiple Severities) |  |
| 21 | `PLBHJR5Q_E126` | `contains` | 05-Fault Mode | no response fault |  | 06-Fault Severity | fault magnitude(Multiple Severities) |  |
| 22 | `PLBHJR5Q_E127` | `contains` | 05-Fault Mode | slow response |  | 06-Fault Severity | fault magnitude(Multiple Severities) |  |
| 23 | `PLBHJR5Q_E128` | `contains` | 05-Fault Mode | stuck fault |  | 06-Fault Severity | fault magnitude(Multiple Severities) |  |
| 24 | `PLBHJR5Q_E129` | `contains` | 05-Fault Mode | constant deviation fault |  | 06-Fault Severity | fault magnitude(Multiple Severities) |  |
| 25 | `PLBHJR5Q_E132` | `contains_phm_task` | 05-Fault Mode | floating fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 26 | `PLBHJR5Q_E133` | `contains_phm_task` | 05-Fault Mode | instability fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 27 | `PLBHJR5Q_E134` | `contains_phm_task` | 05-Fault Mode | no response fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 28 | `PLBHJR5Q_E135` | `contains_phm_task` | 05-Fault Mode | slow response |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 29 | `PLBHJR5Q_E136` | `contains_phm_task` | 05-Fault Mode | stuck fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 30 | `PLBHJR5Q_E137` | `contains_phm_task` | 05-Fault Mode | constant deviation fault |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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

### ▶ For `can obviously reflect` (Sensor Information type → Fault Mode type)

**Very High Standard**: All of the following **conditions must be met** to be judged as "existing":
1. The paper explicitly states that the sensor **collects** data of this fault mode (i.e., the sensor appears in the fault data acquisition scenario)
2. The paper explicitly states that the sensor can **directly reflect/characterize** the physical features of this fault
3. The mere appearance of the sensor and fault mode in the dataset description is **insufficient** for judgment — the sensor must play an active role in the research method
**Trap to Watch Out For**: The mere appearance of the sensor and fault mode as dataset description does not equal the existence of a causal chain
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses a sensor→fault-feature causal relation, rather than exact matching of English phrases

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
