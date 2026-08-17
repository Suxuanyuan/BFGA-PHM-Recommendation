# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：X3YNV6JC
- **Paper Title**：Study on intra-wave frequency modulation phenomenon in detection of rub-impact fault
- **Number of Candidate Edges to Judge**：28 

---

## II. LLM Input

> **Input Material**: Reference ID `X3YNV6JC`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "X3HNH5UY_E071", "edge_description": "Case Western Reserve University (CWRU) dataset can be used for fault diagnosis"},
    {"edge_id": "X3HNH5UY_E072", "edge_description": "locomotive bearing dataset can be used for fault diagnosis"},
    {"edge_id": "X3HNH5UY_E079", "edge_description": "rolling bearing induces_problem few labeled data"},
    {"edge_id": "X3HNH5UY_E080", "edge_description": "rolling bearing induces_problem probability distributions discrepancies"},
    {"edge_id": "X3HNH5UY_E081", "edge_description": "varying operation conditions induces_problem few labeled data"},
    {"edge_id": "X3HNH5UY_E082", "edge_description": "varying operation conditions induces_problem probability distributions discrepancies"},
    {"edge_id": "X3HNH5UY_E083", "edge_description": "defect diameter induces_problem few labeled data"},
    {"edge_id": "X3HNH5UY_E084", "edge_description": "defect diameter induces_problem probability distributions discrepancies"},
    {"edge_id": "X3HNH5UY_E085", "edge_description": "No Compound Fault induces_problem few labeled data"},
    {"edge_id": "X3HNH5UY_E086", "edge_description": "No Compound Fault induces_problem probability distributions discrepancies"},
    {"edge_id": "X3HNH5UY_E087", "edge_description": "fault diagnosis induces_problem few labeled data"},
    {"edge_id": "X3HNH5UY_E088", "edge_description": "fault diagnosis induces_problem probability distributions discrepancies"},
    {"edge_id": "X3HNH5UY_E089", "edge_description": "few labeled data induces_problem few labeled data"},
    {"edge_id": "X3HNH5UY_E090", "edge_description": "few labeled data induces_problem probability distributions discrepancies"},
    {"edge_id": "X3HNH5UY_E091", "edge_description": "Normal induces_problem few labeled data"},
    {"edge_id": "X3HNH5UY_E092", "edge_description": "Normal induces_problem probability distributions discrepancies"},
    {"edge_id": "X3YNV6JC_E055", "edge_description": "rotating machinery / heavy oil catalytic cracking machine set contains rotor system"},
    {"edge_id": "X3YNV6JC_E056", "edge_description": "rotating machinery / heavy oil catalytic cracking machine set contains gas turbine"},
    {"edge_id": "X3YNV6JC_E057", "edge_description": "rotor system contains rotor"},
    {"edge_id": "X3YNV6JC_E058", "edge_description": "rotor system contains stator"},
    {"edge_id": "X3YNV6JC_E059", "edge_description": "gas turbine contains rotor"},
    {"edge_id": "X3YNV6JC_E060", "edge_description": "gas turbine contains stator"},
    {"edge_id": "X3YNV6JC_E061", "edge_description": "rotor system contains 1500 rpm, 6000 rpm, 9000 rpm, and 5381 rpm"},
    {"edge_id": "X3YNV6JC_E062", "edge_description": "gas turbine contains 1500 rpm, 6000 rpm, 9000 rpm, and 5381 rpm"},
    {"edge_id": "X3YNV6JC_E064", "edge_description": "eddy current transducer is collected on rotor"},
    {"edge_id": "X3YNV6JC_E065", "edge_description": "eddy current transducer is collected on stator"},
    {"edge_id": "X3YNV6JC_E067", "edge_description": "Simulation: Jeffcott rotor model can be used for rub-impact fault diagnosis"},
    {"edge_id": "X3YNV6JC_E068", "edge_description": "Vibration response from a heavy oil catalytic cracking machine set can be used for rub-impact fault diagnosis"}
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
| 1 | `X3HNH5UY_E071` | `can be used for` | 10-Dataset | Case Western Reserve University (CWRU) dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 2 | `X3HNH5UY_E072` | `can be used for` | 10-Dataset | locomotive bearing dataset |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 3 | `X3HNH5UY_E079` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | few labeled data(Small Fault Samples) |  |
| 4 | `X3HNH5UY_E080` | `induces_problem` | 02-Object Type | rolling bearing |  | 09-Problem Scenario | probability distributions discrepancies(Distribution Discrepancy) |  |
| 5 | `X3HNH5UY_E081` | `induces_problem` | 03-Operating Conditions | varying operation conditions(Multiple Conditions) |  | 09-Problem Scenario | few labeled data(Small Fault Samples) |  |
| 6 | `X3HNH5UY_E082` | `induces_problem` | 03-Operating Conditions | varying operation conditions(Multiple Conditions) |  | 09-Problem Scenario | probability distributions discrepancies(Distribution Discrepancy) |  |
| 7 | `X3HNH5UY_E083` | `induces_problem` | 06-Fault Severity | defect diameter(Multiple Severities) |  | 09-Problem Scenario | few labeled data(Small Fault Samples) |  |
| 8 | `X3HNH5UY_E084` | `induces_problem` | 06-Fault Severity | defect diameter(Multiple Severities) |  | 09-Problem Scenario | probability distributions discrepancies(Distribution Discrepancy) |  |
| 9 | `X3HNH5UY_E085` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | few labeled data(Small Fault Samples) |  |
| 10 | `X3HNH5UY_E086` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | probability distributions discrepancies(Distribution Discrepancy) |  |
| 11 | `X3HNH5UY_E087` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | few labeled data(Small Fault Samples) |  |
| 12 | `X3HNH5UY_E088` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | probability distributions discrepancies(Distribution Discrepancy) |  |
| 13 | `X3HNH5UY_E089` | `induces_problem` | 12-Training Data Availability | few labeled data(Scarce) |  | 09-Problem Scenario | few labeled data(Small Fault Samples) |  |
| 14 | `X3HNH5UY_E090` | `induces_problem` | 12-Training Data Availability | few labeled data(Scarce) |  | 09-Problem Scenario | probability distributions discrepancies(Distribution Discrepancy) |  |
| 15 | `X3HNH5UY_E091` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | few labeled data(Small Fault Samples) |  |
| 16 | `X3HNH5UY_E092` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | probability distributions discrepancies(Distribution Discrepancy) |  |
| 17 | `X3YNV6JC_E055` | `contains` | 01-Object Domain | rotating machinery / heavy oil catalytic cracking machine set(Industrial) |  | 02-Object Type | rotor system |  |
| 18 | `X3YNV6JC_E056` | `contains` | 01-Object Domain | rotating machinery / heavy oil catalytic cracking machine set(Industrial) |  | 02-Object Type | gas turbine |  |
| 19 | `X3YNV6JC_E057` | `contains` | 02-Object Type | rotor system |  | 04-Fault Location | rotor |  |
| 20 | `X3YNV6JC_E058` | `contains` | 02-Object Type | rotor system |  | 04-Fault Location | stator |  |
| 21 | `X3YNV6JC_E059` | `contains` | 02-Object Type | gas turbine |  | 04-Fault Location | rotor |  |
| 22 | `X3YNV6JC_E060` | `contains` | 02-Object Type | gas turbine |  | 04-Fault Location | stator |  |
| 23 | `X3YNV6JC_E061` | `contains` | 02-Object Type | rotor system |  | 03-Operating Conditions | 1500 rpm, 6000 rpm, 9000 rpm, and 5381 rpm(Multiple Conditions) |  |
| 24 | `X3YNV6JC_E062` | `contains` | 02-Object Type | gas turbine |  | 03-Operating Conditions | 1500 rpm, 6000 rpm, 9000 rpm, and 5381 rpm(Multiple Conditions) |  |
| 25 | `X3YNV6JC_E064` | `is collected on` | 11-Sensor Information | eddy current transducer |  | 04-Fault Location | rotor |  |
| 26 | `X3YNV6JC_E065` | `is collected on` | 11-Sensor Information | eddy current transducer |  | 04-Fault Location | stator |  |
| 27 | `X3YNV6JC_E067` | `can be used for` | 10-Dataset | Simulation: Jeffcott rotor model |  | 08-PHM Task | rub-impact fault diagnosis(Diagnosis Task) |  |
| 28 | `X3YNV6JC_E068` | `can be used for` | 10-Dataset | Vibration response from a heavy oil catalytic cracking machine set |  | 08-PHM Task | rub-impact fault diagnosis(Diagnosis Task) |  |

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

### ▶ For `can be used for` (Dataset type → PHM Task type)

**High Standard**: The paper must explicitly express that the dataset is an **input at the methodological level**, rather than merely a background for experimental evaluation.
Merely mentioning "using a dataset to evaluate model performance" is insufficient — the methodological association between dataset and task must be reflected (e.g., "selecting a dataset for a specific task")
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the methodological relation of the dataset serving a certain PHM task, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 28 edges)*
