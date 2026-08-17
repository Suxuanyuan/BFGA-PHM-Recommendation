# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：8SEZD7QB
- **Paper Title**：Bearing defect diagnosis based on semi-supervised kernel Local Fisher Discriminant Analysis using pseudo labels
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `8SEZD7QB`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "8SEZD7QB_E072", "edge_description": "crack contains IF+OF, OF+RF, IF+RF, IF+OF+RF"},
    {"edge_id": "8SEZD7QB_E073", "edge_description": "dent contains IF+OF, OF+RF, IF+RF, IF+OF+RF"},
    {"edge_id": "8SEZD7QB_E075", "edge_description": "acceleration sensor can obviously reflect crack"},
    {"edge_id": "8SEZD7QB_E076", "edge_description": "acceleration sensor can obviously reflect dent"},
    {"edge_id": "8SEZD7QB_E078", "edge_description": "rolling bearing has_fault_mode crack"},
    {"edge_id": "8SEZD7QB_E079", "edge_description": "rolling bearing has_fault_mode dent"},
    {"edge_id": "8SEZD7QB_E080", "edge_description": "crack contains 0.6 mm width, 1 mm diameter and 2 mm depth"},
    {"edge_id": "8SEZD7QB_E081", "edge_description": "dent contains 0.6 mm width, 1 mm diameter and 2 mm depth"},
    {"edge_id": "8SEZD7QB_E084", "edge_description": "crack contains_phm_task defect diagnosis"},
    {"edge_id": "8SEZD7QB_E085", "edge_description": "dent contains_phm_task defect diagnosis"},
    {"edge_id": "8SEZD7QB_E087", "edge_description": "bearing induces_problem only a few labeled data available"},
    {"edge_id": "8SEZD7QB_E088", "edge_description": "bearing induces_problem noises"},
    {"edge_id": "8SEZD7QB_E089", "edge_description": "bearing induces_problem combinations of heath condition"},
    {"edge_id": "8SEZD7QB_E090", "edge_description": "rotational speed is 1500 rpm induces_problem only a few labeled data available"},
    {"edge_id": "8SEZD7QB_E091", "edge_description": "rotational speed is 1500 rpm induces_problem noises"},
    {"edge_id": "8SEZD7QB_E092", "edge_description": "rotational speed is 1500 rpm induces_problem combinations of heath condition"},
    {"edge_id": "8SEZD7QB_E093", "edge_description": "0.6 mm width, 1 mm diameter and 2 mm depth induces_problem only a few labeled data available"},
    {"edge_id": "8SEZD7QB_E094", "edge_description": "0.6 mm width, 1 mm diameter and 2 mm depth induces_problem noises"},
    {"edge_id": "8SEZD7QB_E095", "edge_description": "0.6 mm width, 1 mm diameter and 2 mm depth induces_problem combinations of heath condition"},
    {"edge_id": "8SEZD7QB_E096", "edge_description": "IF+OF, OF+RF, IF+RF, IF+OF+RF induces_problem only a few labeled data available"},
    {"edge_id": "8SEZD7QB_E097", "edge_description": "IF+OF, OF+RF, IF+RF, IF+OF+RF induces_problem noises"},
    {"edge_id": "8SEZD7QB_E098", "edge_description": "IF+OF, OF+RF, IF+RF, IF+OF+RF induces_problem combinations of heath condition"},
    {"edge_id": "8SEZD7QB_E099", "edge_description": "defect diagnosis induces_problem only a few labeled data available"},
    {"edge_id": "8SEZD7QB_E100", "edge_description": "defect diagnosis induces_problem noises"},
    {"edge_id": "8SEZD7QB_E101", "edge_description": "defect diagnosis induces_problem combinations of heath condition"},
    {"edge_id": "8SEZD7QB_E102", "edge_description": "500 training samples per class induces_problem only a few labeled data available"},
    {"edge_id": "8SEZD7QB_E103", "edge_description": "500 training samples per class induces_problem noises"},
    {"edge_id": "8SEZD7QB_E104", "edge_description": "500 training samples per class induces_problem combinations of heath condition"},
    {"edge_id": "8SEZD7QB_E105", "edge_description": "white noise is added into dataset to yield three noisy data with SNR of 10 dB, 5 dB and 2 dB induces_problem only a few labeled data available"},
    {"edge_id": "8SEZD7QB_E106", "edge_description": "white noise is added into dataset to yield three noisy data with SNR of 10 dB, 5 dB and 2 dB induces_problem noises"}
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
| 1 | `8SEZD7QB_E072` | `contains` | 05-Fault Mode | crack |  | 07-Compound Fault | IF+OF, OF+RF, IF+RF, IF+OF+RF(Compound Fault Within Same Structure) |  |
| 2 | `8SEZD7QB_E073` | `contains` | 05-Fault Mode | dent |  | 07-Compound Fault | IF+OF, OF+RF, IF+RF, IF+OF+RF(Compound Fault Within Same Structure) |  |
| 3 | `8SEZD7QB_E075` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | crack |  |
| 4 | `8SEZD7QB_E076` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | dent |  |
| 5 | `8SEZD7QB_E078` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | crack |  |
| 6 | `8SEZD7QB_E079` | `has_fault_mode` | 04-Fault Location | rolling bearing |  | 05-Fault Mode | dent |  |
| 7 | `8SEZD7QB_E080` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | 0.6 mm width, 1 mm diameter and 2 mm depth(Single Severity) |  |
| 8 | `8SEZD7QB_E081` | `contains` | 05-Fault Mode | dent |  | 06-Fault Severity | 0.6 mm width, 1 mm diameter and 2 mm depth(Single Severity) |  |
| 9 | `8SEZD7QB_E084` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | defect diagnosis(Diagnosis Task) |  |
| 10 | `8SEZD7QB_E085` | `contains_phm_task` | 05-Fault Mode | dent |  | 08-PHM Task | defect diagnosis(Diagnosis Task) |  |
| 11 | `8SEZD7QB_E087` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | only a few labeled data available(Small Fault Samples) |  |
| 12 | `8SEZD7QB_E088` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | noises(Uncertainty) |  |
| 13 | `8SEZD7QB_E089` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | combinations of heath condition(Compound Faults) |  |
| 14 | `8SEZD7QB_E090` | `induces_problem` | 03-Operating Conditions | rotational speed is 1500 rpm(Single Condition) |  | 09-Problem Scenario | only a few labeled data available(Small Fault Samples) |  |
| 15 | `8SEZD7QB_E091` | `induces_problem` | 03-Operating Conditions | rotational speed is 1500 rpm(Single Condition) |  | 09-Problem Scenario | noises(Uncertainty) |  |
| 16 | `8SEZD7QB_E092` | `induces_problem` | 03-Operating Conditions | rotational speed is 1500 rpm(Single Condition) |  | 09-Problem Scenario | combinations of heath condition(Compound Faults) |  |
| 17 | `8SEZD7QB_E093` | `induces_problem` | 06-Fault Severity | 0.6 mm width, 1 mm diameter and 2 mm depth(Single Severity) |  | 09-Problem Scenario | only a few labeled data available(Small Fault Samples) |  |
| 18 | `8SEZD7QB_E094` | `induces_problem` | 06-Fault Severity | 0.6 mm width, 1 mm diameter and 2 mm depth(Single Severity) |  | 09-Problem Scenario | noises(Uncertainty) |  |
| 19 | `8SEZD7QB_E095` | `induces_problem` | 06-Fault Severity | 0.6 mm width, 1 mm diameter and 2 mm depth(Single Severity) |  | 09-Problem Scenario | combinations of heath condition(Compound Faults) |  |
| 20 | `8SEZD7QB_E096` | `induces_problem` | 07-Compound Fault | IF+OF, OF+RF, IF+RF, IF+OF+RF(Compound Fault Within Same Structure) |  | 09-Problem Scenario | only a few labeled data available(Small Fault Samples) |  |
| 21 | `8SEZD7QB_E097` | `induces_problem` | 07-Compound Fault | IF+OF, OF+RF, IF+RF, IF+OF+RF(Compound Fault Within Same Structure) |  | 09-Problem Scenario | noises(Uncertainty) |  |
| 22 | `8SEZD7QB_E098` | `induces_problem` | 07-Compound Fault | IF+OF, OF+RF, IF+RF, IF+OF+RF(Compound Fault Within Same Structure) |  | 09-Problem Scenario | combinations of heath condition(Compound Faults) |  |
| 23 | `8SEZD7QB_E099` | `induces_problem` | 08-PHM Task | defect diagnosis(Diagnosis Task) |  | 09-Problem Scenario | only a few labeled data available(Small Fault Samples) |  |
| 24 | `8SEZD7QB_E100` | `induces_problem` | 08-PHM Task | defect diagnosis(Diagnosis Task) |  | 09-Problem Scenario | noises(Uncertainty) |  |
| 25 | `8SEZD7QB_E101` | `induces_problem` | 08-PHM Task | defect diagnosis(Diagnosis Task) |  | 09-Problem Scenario | combinations of heath condition(Compound Faults) |  |
| 26 | `8SEZD7QB_E102` | `induces_problem` | 12-Training Data Availability | 500 training samples per class(Sufficient) |  | 09-Problem Scenario | only a few labeled data available(Small Fault Samples) |  |
| 27 | `8SEZD7QB_E103` | `induces_problem` | 12-Training Data Availability | 500 training samples per class(Sufficient) |  | 09-Problem Scenario | noises(Uncertainty) |  |
| 28 | `8SEZD7QB_E104` | `induces_problem` | 12-Training Data Availability | 500 training samples per class(Sufficient) |  | 09-Problem Scenario | combinations of heath condition(Compound Faults) |  |
| 29 | `8SEZD7QB_E105` | `induces_problem` | 13-Noise Level | white noise is added into dataset to yield three noisy data with SNR of 10 dB, 5 dB and 2 dB(High Noise) |  | 09-Problem Scenario | only a few labeled data available(Small Fault Samples) |  |
| 30 | `8SEZD7QB_E106` | `induces_problem` | 13-Noise Level | white noise is added into dataset to yield three noisy data with SNR of 10 dB, 5 dB and 2 dB(High Noise) |  | 09-Problem Scenario | noises(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
