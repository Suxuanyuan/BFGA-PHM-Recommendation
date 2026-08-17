# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：X6QJHKGG
- **Paper Title**：Rapid Fault Diagnosis of PEM Fuel Cells through Optimal Electrochemical Impedance Spectroscopy Tests
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `X6QJHKGG`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "X6B33SEW_E073", "edge_description": "flow sensor (ABB Watermaster FER100) can obviously reflect clogging"},
    {"edge_id": "X6B33SEW_E075", "edge_description": "journal bearing has_fault_mode wear"},
    {"edge_id": "X6B33SEW_E076", "edge_description": "journal bearing has_fault_mode dry-running"},
    {"edge_id": "X6B33SEW_E077", "edge_description": "journal bearing has_fault_mode clogging"},
    {"edge_id": "X6B33SEW_E078", "edge_description": "rotor has_fault_mode wear"},
    {"edge_id": "X6B33SEW_E079", "edge_description": "rotor has_fault_mode dry-running"},
    {"edge_id": "X6B33SEW_E080", "edge_description": "rotor has_fault_mode clogging"},
    {"edge_id": "X6B33SEW_E081", "edge_description": "impeller has_fault_mode wear"},
    {"edge_id": "X6B33SEW_E082", "edge_description": "impeller has_fault_mode dry-running"},
    {"edge_id": "X6B33SEW_E083", "edge_description": "impeller has_fault_mode clogging"},
    {"edge_id": "X6B33SEW_E084", "edge_description": "wear contains inner diameter from 20 mm to 21 mm, two of seven channels clogged"},
    {"edge_id": "X6B33SEW_E085", "edge_description": "dry-running contains inner diameter from 20 mm to 21 mm, two of seven channels clogged"},
    {"edge_id": "X6B33SEW_E086", "edge_description": "clogging contains inner diameter from 20 mm to 21 mm, two of seven channels clogged"},
    {"edge_id": "X6B33SEW_E087", "edge_description": "circulation pump contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E088", "edge_description": "permanent magnet synchronous motor contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E089", "edge_description": "journal bearing contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E090", "edge_description": "rotor contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E091", "edge_description": "impeller contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E092", "edge_description": "wear contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E093", "edge_description": "dry-running contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E094", "edge_description": "clogging contains_phm_task fault diagnosis"},
    {"edge_id": "X6B33SEW_E096", "edge_description": "circulation pump induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E097", "edge_description": "permanent magnet synchronous motor induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E098", "edge_description": "stationary operation and transient start-up induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E099", "edge_description": "inner diameter from 20 mm to 21 mm, two of seven channels clogged induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E100", "edge_description": "No Compound Fault induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E101", "edge_description": "fault diagnosis induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E102", "edge_description": "Sampling rate of 10 kHz with a running time of 60 s induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E103", "edge_description": "reduce both external and internal interference induces_problem fault separation"},
    {"edge_id": "X6B33SEW_E104", "edge_description": "Not explicitly mentioned induces_problem fault separation"}
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
| 1 | `X6B33SEW_E073` | `can obviously reflect` | 11-Sensor Information | flow sensor (ABB Watermaster FER100) |  | 05-Fault Mode | clogging |  |
| 2 | `X6B33SEW_E075` | `has_fault_mode` | 04-Fault Location | journal bearing |  | 05-Fault Mode | wear |  |
| 3 | `X6B33SEW_E076` | `has_fault_mode` | 04-Fault Location | journal bearing |  | 05-Fault Mode | dry-running |  |
| 4 | `X6B33SEW_E077` | `has_fault_mode` | 04-Fault Location | journal bearing |  | 05-Fault Mode | clogging |  |
| 5 | `X6B33SEW_E078` | `has_fault_mode` | 04-Fault Location | rotor |  | 05-Fault Mode | wear |  |
| 6 | `X6B33SEW_E079` | `has_fault_mode` | 04-Fault Location | rotor |  | 05-Fault Mode | dry-running |  |
| 7 | `X6B33SEW_E080` | `has_fault_mode` | 04-Fault Location | rotor |  | 05-Fault Mode | clogging |  |
| 8 | `X6B33SEW_E081` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | wear |  |
| 9 | `X6B33SEW_E082` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | dry-running |  |
| 10 | `X6B33SEW_E083` | `has_fault_mode` | 04-Fault Location | impeller |  | 05-Fault Mode | clogging |  |
| 11 | `X6B33SEW_E084` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | inner diameter from 20 mm to 21 mm, two of seven channels clogged(Single Severity) |  |
| 12 | `X6B33SEW_E085` | `contains` | 05-Fault Mode | dry-running |  | 06-Fault Severity | inner diameter from 20 mm to 21 mm, two of seven channels clogged(Single Severity) |  |
| 13 | `X6B33SEW_E086` | `contains` | 05-Fault Mode | clogging |  | 06-Fault Severity | inner diameter from 20 mm to 21 mm, two of seven channels clogged(Single Severity) |  |
| 14 | `X6B33SEW_E087` | `contains_phm_task` | 02-Object Type | circulation pump |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 15 | `X6B33SEW_E088` | `contains_phm_task` | 02-Object Type | permanent magnet synchronous motor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `X6B33SEW_E089` | `contains_phm_task` | 04-Fault Location | journal bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `X6B33SEW_E090` | `contains_phm_task` | 04-Fault Location | rotor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 18 | `X6B33SEW_E091` | `contains_phm_task` | 04-Fault Location | impeller |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 19 | `X6B33SEW_E092` | `contains_phm_task` | 05-Fault Mode | wear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `X6B33SEW_E093` | `contains_phm_task` | 05-Fault Mode | dry-running |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `X6B33SEW_E094` | `contains_phm_task` | 05-Fault Mode | clogging |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `X6B33SEW_E096` | `induces_problem` | 02-Object Type | circulation pump |  | 09-Problem Scenario | fault separation(Other) |  |
| 23 | `X6B33SEW_E097` | `induces_problem` | 02-Object Type | permanent magnet synchronous motor |  | 09-Problem Scenario | fault separation(Other) |  |
| 24 | `X6B33SEW_E098` | `induces_problem` | 03-Operating Conditions | stationary operation and transient start-up(Variable Conditions) |  | 09-Problem Scenario | fault separation(Other) |  |
| 25 | `X6B33SEW_E099` | `induces_problem` | 06-Fault Severity | inner diameter from 20 mm to 21 mm, two of seven channels clogged(Single Severity) |  | 09-Problem Scenario | fault separation(Other) |  |
| 26 | `X6B33SEW_E100` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | fault separation(Other) |  |
| 27 | `X6B33SEW_E101` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | fault separation(Other) |  |
| 28 | `X6B33SEW_E102` | `induces_problem` | 12-Training Data Availability | Sampling rate of 10 kHz with a running time of 60 s(Sufficient) |  | 09-Problem Scenario | fault separation(Other) |  |
| 29 | `X6B33SEW_E103` | `induces_problem` | 13-Noise Level | reduce both external and internal interference(Normal) |  | 09-Problem Scenario | fault separation(Other) |  |
| 30 | `X6B33SEW_E104` | `induces_problem` | 14-Computational Resource | Not explicitly mentioned |  | 09-Problem Scenario | fault separation(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
