# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：ZI2RIQFP
- **Paper Title**：Transfer between multiple machine plants: A modified fast self-organizing feature map and two-order selective ensemble based fault diagnosis strategy
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `ZI2RIQFP`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "ZI2RIQFP_E080", "edge_description": "crack contains No Compound Fault"},
    {"edge_id": "ZI2RIQFP_E081", "edge_description": "missing contains No Compound Fault"},
    {"edge_id": "ZI2RIQFP_E082", "edge_description": "chipped contains No Compound Fault"},
    {"edge_id": "ZI2RIQFP_E083", "edge_description": "surface wear contains No Compound Fault"},
    {"edge_id": "ZI2RIQFP_E085", "edge_description": "vibration sensors can obviously reflect crack"},
    {"edge_id": "ZI2RIQFP_E086", "edge_description": "vibration sensors can obviously reflect missing"},
    {"edge_id": "ZI2RIQFP_E087", "edge_description": "vibration sensors can obviously reflect chipped"},
    {"edge_id": "ZI2RIQFP_E088", "edge_description": "vibration sensors can obviously reflect surface wear"},
    {"edge_id": "ZI2RIQFP_E089", "edge_description": "Qianpeng testbed (QT) can be used for fault diagnosis"},
    {"edge_id": "ZI2RIQFP_E090", "edge_description": "Drivetrain dynamics simulator (DDS) can be used for fault diagnosis"},
    {"edge_id": "ZI2RIQFP_E091", "edge_description": "gear has_fault_mode crack"},
    {"edge_id": "ZI2RIQFP_E092", "edge_description": "gear has_fault_mode missing"},
    {"edge_id": "ZI2RIQFP_E093", "edge_description": "gear has_fault_mode chipped"},
    {"edge_id": "ZI2RIQFP_E094", "edge_description": "gear has_fault_mode surface wear"},
    {"edge_id": "ZI2RIQFP_E095", "edge_description": "crack contains light crack, small crack, medium crack, heavy crack"},
    {"edge_id": "ZI2RIQFP_E096", "edge_description": "missing contains light crack, small crack, medium crack, heavy crack"},
    {"edge_id": "ZI2RIQFP_E097", "edge_description": "chipped contains light crack, small crack, medium crack, heavy crack"},
    {"edge_id": "ZI2RIQFP_E098", "edge_description": "surface wear contains light crack, small crack, medium crack, heavy crack"},
    {"edge_id": "ZI2RIQFP_E101", "edge_description": "crack contains_phm_task fault diagnosis"},
    {"edge_id": "ZI2RIQFP_E102", "edge_description": "missing contains_phm_task fault diagnosis"},
    {"edge_id": "ZI2RIQFP_E103", "edge_description": "chipped contains_phm_task fault diagnosis"},
    {"edge_id": "ZI2RIQFP_E104", "edge_description": "surface wear contains_phm_task fault diagnosis"},
    {"edge_id": "ZI2RIQFP_E106", "edge_description": "gearbox induces_problem domain shift"},
    {"edge_id": "ZI2RIQFP_E107", "edge_description": "gearbox induces_problem data deficiency problem in target domain"},
    {"edge_id": "ZI2RIQFP_E108", "edge_description": "varying rotating speeds induces_problem domain shift"},
    {"edge_id": "ZI2RIQFP_E109", "edge_description": "varying rotating speeds induces_problem data deficiency problem in target domain"},
    {"edge_id": "ZI2RIQFP_E110", "edge_description": "light crack, small crack, medium crack, heavy crack induces_problem domain shift"},
    {"edge_id": "ZI2RIQFP_E111", "edge_description": "light crack, small crack, medium crack, heavy crack induces_problem data deficiency problem in target domain"},
    {"edge_id": "ZI2RIQFP_E112", "edge_description": "No Compound Fault induces_problem domain shift"},
    {"edge_id": "ZI2RIQFP_E113", "edge_description": "No Compound Fault induces_problem data deficiency problem in target domain"}
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
| 1 | `ZI2RIQFP_E080` | `contains` | 05-Fault Mode | crack |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `ZI2RIQFP_E081` | `contains` | 05-Fault Mode | missing |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `ZI2RIQFP_E082` | `contains` | 05-Fault Mode | chipped |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `ZI2RIQFP_E083` | `contains` | 05-Fault Mode | surface wear |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `ZI2RIQFP_E085` | `can obviously reflect` | 11-Sensor Information | vibration sensors |  | 05-Fault Mode | crack |  |
| 6 | `ZI2RIQFP_E086` | `can obviously reflect` | 11-Sensor Information | vibration sensors |  | 05-Fault Mode | missing |  |
| 7 | `ZI2RIQFP_E087` | `can obviously reflect` | 11-Sensor Information | vibration sensors |  | 05-Fault Mode | chipped |  |
| 8 | `ZI2RIQFP_E088` | `can obviously reflect` | 11-Sensor Information | vibration sensors |  | 05-Fault Mode | surface wear |  |
| 9 | `ZI2RIQFP_E089` | `can be used for` | 10-Dataset | Qianpeng testbed (QT) |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `ZI2RIQFP_E090` | `can be used for` | 10-Dataset | Drivetrain dynamics simulator (DDS) |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `ZI2RIQFP_E091` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | crack |  |
| 12 | `ZI2RIQFP_E092` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | missing |  |
| 13 | `ZI2RIQFP_E093` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | chipped |  |
| 14 | `ZI2RIQFP_E094` | `has_fault_mode` | 04-Fault Location | gear |  | 05-Fault Mode | surface wear |  |
| 15 | `ZI2RIQFP_E095` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | light crack, small crack, medium crack, heavy crack(Multiple Severities) |  |
| 16 | `ZI2RIQFP_E096` | `contains` | 05-Fault Mode | missing |  | 06-Fault Severity | light crack, small crack, medium crack, heavy crack(Multiple Severities) |  |
| 17 | `ZI2RIQFP_E097` | `contains` | 05-Fault Mode | chipped |  | 06-Fault Severity | light crack, small crack, medium crack, heavy crack(Multiple Severities) |  |
| 18 | `ZI2RIQFP_E098` | `contains` | 05-Fault Mode | surface wear |  | 06-Fault Severity | light crack, small crack, medium crack, heavy crack(Multiple Severities) |  |
| 19 | `ZI2RIQFP_E101` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 20 | `ZI2RIQFP_E102` | `contains_phm_task` | 05-Fault Mode | missing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 21 | `ZI2RIQFP_E103` | `contains_phm_task` | 05-Fault Mode | chipped |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 22 | `ZI2RIQFP_E104` | `contains_phm_task` | 05-Fault Mode | surface wear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 23 | `ZI2RIQFP_E106` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | domain shift(Distribution Discrepancy) |  |
| 24 | `ZI2RIQFP_E107` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | data deficiency problem in target domain(Small Fault Samples) |  |
| 25 | `ZI2RIQFP_E108` | `induces_problem` | 03-Operating Conditions | varying rotating speeds(Variable Conditions) |  | 09-Problem Scenario | domain shift(Distribution Discrepancy) |  |
| 26 | `ZI2RIQFP_E109` | `induces_problem` | 03-Operating Conditions | varying rotating speeds(Variable Conditions) |  | 09-Problem Scenario | data deficiency problem in target domain(Small Fault Samples) |  |
| 27 | `ZI2RIQFP_E110` | `induces_problem` | 06-Fault Severity | light crack, small crack, medium crack, heavy crack(Multiple Severities) |  | 09-Problem Scenario | domain shift(Distribution Discrepancy) |  |
| 28 | `ZI2RIQFP_E111` | `induces_problem` | 06-Fault Severity | light crack, small crack, medium crack, heavy crack(Multiple Severities) |  | 09-Problem Scenario | data deficiency problem in target domain(Small Fault Samples) |  |
| 29 | `ZI2RIQFP_E112` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | domain shift(Distribution Discrepancy) |  |
| 30 | `ZI2RIQFP_E113` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | data deficiency problem in target domain(Small Fault Samples) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
