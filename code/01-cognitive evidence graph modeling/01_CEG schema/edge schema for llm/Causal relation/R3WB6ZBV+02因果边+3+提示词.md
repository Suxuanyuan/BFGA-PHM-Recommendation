# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：R3WB6ZBV
- **Paper Title**：Detection and Diagnosis of Faults in Induction Motor Using an Improved Artificial Ant Clustering Technique
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `R3WB6ZBV`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "R3WB6ZBV_E067", "edge_description": "induction motor contains different load levels"},
    {"edge_id": "R3WB6ZBV_E068", "edge_description": "bearing contains different load levels"},
    {"edge_id": "R3WB6ZBV_E069", "edge_description": "broken rotor bar contains No Compound Fault"},
    {"edge_id": "R3WB6ZBV_E070", "edge_description": "bearing failure contains No Compound Fault"},
    {"edge_id": "R3WB6ZBV_E071", "edge_description": "current sensor is collected on induction motor"},
    {"edge_id": "R3WB6ZBV_E072", "edge_description": "current sensor is collected on bearing"},
    {"edge_id": "R3WB6ZBV_E073", "edge_description": "voltage sensor is collected on induction motor"},
    {"edge_id": "R3WB6ZBV_E074", "edge_description": "voltage sensor is collected on bearing"},
    {"edge_id": "R3WB6ZBV_E075", "edge_description": "current sensor can obviously reflect broken rotor bar"},
    {"edge_id": "R3WB6ZBV_E076", "edge_description": "current sensor can obviously reflect bearing failure"},
    {"edge_id": "R3WB6ZBV_E077", "edge_description": "voltage sensor can obviously reflect broken rotor bar"},
    {"edge_id": "R3WB6ZBV_E078", "edge_description": "voltage sensor can obviously reflect bearing failure"},
    {"edge_id": "R3WB6ZBV_E079", "edge_description": "Experimental motor dataset can be used for fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E080", "edge_description": "Iris dataset can be used for fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E081", "edge_description": "induction motor has_fault_mode broken rotor bar"},
    {"edge_id": "R3WB6ZBV_E082", "edge_description": "induction motor has_fault_mode bearing failure"},
    {"edge_id": "R3WB6ZBV_E083", "edge_description": "bearing has_fault_mode broken rotor bar"},
    {"edge_id": "R3WB6ZBV_E084", "edge_description": "bearing has_fault_mode bearing failure"},
    {"edge_id": "R3WB6ZBV_E085", "edge_description": "broken rotor bar contains one broken bar, three broken bars, bearing failure degraded by an actual ageing process"},
    {"edge_id": "R3WB6ZBV_E086", "edge_description": "bearing failure contains one broken bar, three broken bars, bearing failure degraded by an actual ageing process"},
    {"edge_id": "R3WB6ZBV_E087", "edge_description": "induction motor contains_phm_task fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E088", "edge_description": "bearing contains_phm_task fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E089", "edge_description": "induction motor contains_phm_task fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E090", "edge_description": "bearing contains_phm_task fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E091", "edge_description": "broken rotor bar contains_phm_task fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E092", "edge_description": "bearing failure contains_phm_task fault detection and diagnosis"},
    {"edge_id": "R3WB6ZBV_E094", "edge_description": "induction motor induces_problem incomplete training set (no information on one of the operating modes)"},
    {"edge_id": "R3WB6ZBV_E095", "edge_description": "induction motor induces_problem incomplete knowledge in the operating modes (load variation)"},
    {"edge_id": "R3WB6ZBV_E096", "edge_description": "bearing induces_problem incomplete training set (no information on one of the operating modes)"},
    {"edge_id": "R3WB6ZBV_E097", "edge_description": "bearing induces_problem incomplete knowledge in the operating modes (load variation)"}
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
| 1 | `R3WB6ZBV_E067` | `contains` | 02-Object Type | induction motor |  | 03-Operating Conditions | different load levels(Multiple Conditions) |  |
| 2 | `R3WB6ZBV_E068` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | different load levels(Multiple Conditions) |  |
| 3 | `R3WB6ZBV_E069` | `contains` | 05-Fault Mode | broken rotor bar |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `R3WB6ZBV_E070` | `contains` | 05-Fault Mode | bearing failure |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `R3WB6ZBV_E071` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | induction motor |  |
| 6 | `R3WB6ZBV_E072` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | bearing |  |
| 7 | `R3WB6ZBV_E073` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | induction motor |  |
| 8 | `R3WB6ZBV_E074` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | bearing |  |
| 9 | `R3WB6ZBV_E075` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | broken rotor bar |  |
| 10 | `R3WB6ZBV_E076` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | bearing failure |  |
| 11 | `R3WB6ZBV_E077` | `can obviously reflect` | 11-Sensor Information | voltage sensor |  | 05-Fault Mode | broken rotor bar |  |
| 12 | `R3WB6ZBV_E078` | `can obviously reflect` | 11-Sensor Information | voltage sensor |  | 05-Fault Mode | bearing failure |  |
| 13 | `R3WB6ZBV_E079` | `can be used for` | 10-Dataset | Experimental motor dataset |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 14 | `R3WB6ZBV_E080` | `can be used for` | 10-Dataset | Iris dataset |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 15 | `R3WB6ZBV_E081` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | broken rotor bar |  |
| 16 | `R3WB6ZBV_E082` | `has_fault_mode` | 04-Fault Location | induction motor |  | 05-Fault Mode | bearing failure |  |
| 17 | `R3WB6ZBV_E083` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | broken rotor bar |  |
| 18 | `R3WB6ZBV_E084` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | bearing failure |  |
| 19 | `R3WB6ZBV_E085` | `contains` | 05-Fault Mode | broken rotor bar |  | 06-Fault Severity | one broken bar, three broken bars, bearing failure degraded by an actual ageing process(Multiple Severities) |  |
| 20 | `R3WB6ZBV_E086` | `contains` | 05-Fault Mode | bearing failure |  | 06-Fault Severity | one broken bar, three broken bars, bearing failure degraded by an actual ageing process(Multiple Severities) |  |
| 21 | `R3WB6ZBV_E087` | `contains_phm_task` | 02-Object Type | induction motor |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 22 | `R3WB6ZBV_E088` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 23 | `R3WB6ZBV_E089` | `contains_phm_task` | 04-Fault Location | induction motor |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 24 | `R3WB6ZBV_E090` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 25 | `R3WB6ZBV_E091` | `contains_phm_task` | 05-Fault Mode | broken rotor bar |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 26 | `R3WB6ZBV_E092` | `contains_phm_task` | 05-Fault Mode | bearing failure |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 27 | `R3WB6ZBV_E094` | `induces_problem` | 02-Object Type | induction motor |  | 09-Problem Scenario | incomplete training set (no information on one of the operating modes)(Zero Fault Samples) |  |
| 28 | `R3WB6ZBV_E095` | `induces_problem` | 02-Object Type | induction motor |  | 09-Problem Scenario | incomplete knowledge in the operating modes (load variation)(Distribution Discrepancy) |  |
| 29 | `R3WB6ZBV_E096` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | incomplete training set (no information on one of the operating modes)(Zero Fault Samples) |  |
| 30 | `R3WB6ZBV_E097` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | incomplete knowledge in the operating modes (load variation)(Distribution Discrepancy) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
