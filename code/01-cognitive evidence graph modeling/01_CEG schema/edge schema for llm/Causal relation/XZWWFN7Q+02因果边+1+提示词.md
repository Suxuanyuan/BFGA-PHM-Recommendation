# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：XZWWFN7Q
- **Paper Title**：Discrimination of Synchronous Machines Rotor Faults in Electrical Signature Analysis Based on Symmetrical Components
- **Number of Candidate Edges to Judge**：24 

---

## II. LLM Input

> **Input Material**: Reference ID `XZWWFN7Q`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "XZWWFN7Q_E055", "edge_description": "Rotor winding inter-turn short circuit contains No Compound Fault"},
    {"edge_id": "XZWWFN7Q_E056", "edge_description": "Rotor mechanical imbalance contains No Compound Fault"},
    {"edge_id": "XZWWFN7Q_E057", "edge_description": "voltage transducers is collected on Rotor"},
    {"edge_id": "XZWWFN7Q_E058", "edge_description": "current transducers is collected on Rotor"},
    {"edge_id": "XZWWFN7Q_E059", "edge_description": "voltage transducers can obviously reflect Rotor winding inter-turn short circuit"},
    {"edge_id": "XZWWFN7Q_E060", "edge_description": "voltage transducers can obviously reflect Rotor mechanical imbalance"},
    {"edge_id": "XZWWFN7Q_E061", "edge_description": "current transducers can obviously reflect Rotor winding inter-turn short circuit"},
    {"edge_id": "XZWWFN7Q_E062", "edge_description": "current transducers can obviously reflect Rotor mechanical imbalance"},
    {"edge_id": "XZWWFN7Q_E063", "edge_description": "synchronous generator test rig can be used for fault diagnosis"},
    {"edge_id": "XZWWFN7Q_E064", "edge_description": "404 MW TermoNorte Thermal Power-Plant can be used for fault diagnosis"},
    {"edge_id": "XZWWFN7Q_E065", "edge_description": "Rotor has_fault_mode Rotor winding inter-turn short circuit"},
    {"edge_id": "XZWWFN7Q_E066", "edge_description": "Rotor has_fault_mode Rotor mechanical imbalance"},
    {"edge_id": "XZWWFN7Q_E067", "edge_description": "Rotor winding inter-turn short circuit contains 34% of the winding shorted"},
    {"edge_id": "XZWWFN7Q_E068", "edge_description": "Rotor mechanical imbalance contains 34% of the winding shorted"},
    {"edge_id": "XZWWFN7Q_E071", "edge_description": "Rotor winding inter-turn short circuit contains_phm_task fault diagnosis"},
    {"edge_id": "XZWWFN7Q_E072", "edge_description": "Rotor mechanical imbalance contains_phm_task fault diagnosis"},
    {"edge_id": "XZWWFN7Q_E074", "edge_description": "synchronous generator induces_problem discrimination of electrical and mechanical faults with coupled signatures"},
    {"edge_id": "XZWWFN7Q_E075", "edge_description": "50 Hz fundamental frequency, resistive-inductive load of 180//j115.7 Ω induces_problem discrimination of electrical and mechanical faults with coupled signatures"},
    {"edge_id": "XZWWFN7Q_E076", "edge_description": "34% of the winding shorted induces_problem discrimination of electrical and mechanical faults with coupled signatures"},
    {"edge_id": "XZWWFN7Q_E077", "edge_description": "No Compound Fault induces_problem discrimination of electrical and mechanical faults with coupled signatures"},
    {"edge_id": "XZWWFN7Q_E078", "edge_description": "fault diagnosis induces_problem discrimination of electrical and mechanical faults with coupled signatures"},
    {"edge_id": "XZWWFN7Q_E079", "edge_description": "experimental tests induces_problem discrimination of electrical and mechanical faults with coupled signatures"},
    {"edge_id": "XZWWFN7Q_E080", "edge_description": "noise level induces_problem discrimination of electrical and mechanical faults with coupled signatures"},
    {"edge_id": "XZWWFN7Q_E081", "edge_description": "simple, low-cost induces_problem discrimination of electrical and mechanical faults with coupled signatures"}
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
| 1 | `XZWWFN7Q_E055` | `contains` | 05-Fault Mode | Rotor winding inter-turn short circuit |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `XZWWFN7Q_E056` | `contains` | 05-Fault Mode | Rotor mechanical imbalance |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `XZWWFN7Q_E057` | `is collected on` | 11-Sensor Information | voltage transducers |  | 04-Fault Location | Rotor |  |
| 4 | `XZWWFN7Q_E058` | `is collected on` | 11-Sensor Information | current transducers |  | 04-Fault Location | Rotor |  |
| 5 | `XZWWFN7Q_E059` | `can obviously reflect` | 11-Sensor Information | voltage transducers |  | 05-Fault Mode | Rotor winding inter-turn short circuit |  |
| 6 | `XZWWFN7Q_E060` | `can obviously reflect` | 11-Sensor Information | voltage transducers |  | 05-Fault Mode | Rotor mechanical imbalance |  |
| 7 | `XZWWFN7Q_E061` | `can obviously reflect` | 11-Sensor Information | current transducers |  | 05-Fault Mode | Rotor winding inter-turn short circuit |  |
| 8 | `XZWWFN7Q_E062` | `can obviously reflect` | 11-Sensor Information | current transducers |  | 05-Fault Mode | Rotor mechanical imbalance |  |
| 9 | `XZWWFN7Q_E063` | `can be used for` | 10-Dataset | synchronous generator test rig |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `XZWWFN7Q_E064` | `can be used for` | 10-Dataset | 404 MW TermoNorte Thermal Power-Plant |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `XZWWFN7Q_E065` | `has_fault_mode` | 04-Fault Location | Rotor |  | 05-Fault Mode | Rotor winding inter-turn short circuit |  |
| 12 | `XZWWFN7Q_E066` | `has_fault_mode` | 04-Fault Location | Rotor |  | 05-Fault Mode | Rotor mechanical imbalance |  |
| 13 | `XZWWFN7Q_E067` | `contains` | 05-Fault Mode | Rotor winding inter-turn short circuit |  | 06-Fault Severity | 34% of the winding shorted(Single Severity) |  |
| 14 | `XZWWFN7Q_E068` | `contains` | 05-Fault Mode | Rotor mechanical imbalance |  | 06-Fault Severity | 34% of the winding shorted(Single Severity) |  |
| 15 | `XZWWFN7Q_E071` | `contains_phm_task` | 05-Fault Mode | Rotor winding inter-turn short circuit |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 16 | `XZWWFN7Q_E072` | `contains_phm_task` | 05-Fault Mode | Rotor mechanical imbalance |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 17 | `XZWWFN7Q_E074` | `induces_problem` | 02-Object Type | synchronous generator |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |
| 18 | `XZWWFN7Q_E075` | `induces_problem` | 03-Operating Conditions | 50 Hz fundamental frequency, resistive-inductive load of 180//j115.7 Ω(Single Condition) |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |
| 19 | `XZWWFN7Q_E076` | `induces_problem` | 06-Fault Severity | 34% of the winding shorted(Single Severity) |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |
| 20 | `XZWWFN7Q_E077` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |
| 21 | `XZWWFN7Q_E078` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |
| 22 | `XZWWFN7Q_E079` | `induces_problem` | 12-Training Data Availability | experimental tests(Sufficient) |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |
| 23 | `XZWWFN7Q_E080` | `induces_problem` | 13-Noise Level | noise level(High Noise) |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |
| 24 | `XZWWFN7Q_E081` | `induces_problem` | 14-Computational Resource | simple, low-cost |  | 09-Problem Scenario | discrimination of electrical and mechanical faults with coupled signatures(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 24 edges)*
