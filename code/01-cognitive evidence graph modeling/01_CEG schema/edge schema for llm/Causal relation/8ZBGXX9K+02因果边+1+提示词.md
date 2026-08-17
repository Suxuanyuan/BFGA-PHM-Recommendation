# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：8ZBGXX9K
- **Paper Title**：Frequency domain averaging based experimental evaluation of gear fault without tachometer for fluctuating speed conditions
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `8ZBGXX9K`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "8ZBGXX9K_E055", "edge_description": "industrial gearbox / wind turbine applications contains gearbox"},
    {"edge_id": "8ZBGXX9K_E056", "edge_description": "industrial gearbox / wind turbine applications contains spur gear"},
    {"edge_id": "8ZBGXX9K_E057", "edge_description": "gearbox contains gear / pinion"},
    {"edge_id": "8ZBGXX9K_E058", "edge_description": "spur gear contains gear / pinion"},
    {"edge_id": "8ZBGXX9K_E059", "edge_description": "gearbox contains fluctuating speed conditions"},
    {"edge_id": "8ZBGXX9K_E060", "edge_description": "spur gear contains fluctuating speed conditions"},
    {"edge_id": "8ZBGXX9K_E061", "edge_description": "tooth crack contains No Compound Fault"},
    {"edge_id": "8ZBGXX9K_E062", "edge_description": "chipped tooth contains No Compound Fault"},
    {"edge_id": "8ZBGXX9K_E063", "edge_description": "missing tooth contains No Compound Fault"},
    {"edge_id": "8ZBGXX9K_E065", "edge_description": "uniaxial accelerometer can obviously reflect tooth crack"},
    {"edge_id": "8ZBGXX9K_E066", "edge_description": "uniaxial accelerometer can obviously reflect chipped tooth"},
    {"edge_id": "8ZBGXX9K_E067", "edge_description": "uniaxial accelerometer can obviously reflect missing tooth"},
    {"edge_id": "8ZBGXX9K_E069", "edge_description": "gear / pinion has_fault_mode tooth crack"},
    {"edge_id": "8ZBGXX9K_E070", "edge_description": "gear / pinion has_fault_mode chipped tooth"},
    {"edge_id": "8ZBGXX9K_E071", "edge_description": "gear / pinion has_fault_mode missing tooth"},
    {"edge_id": "8ZBGXX9K_E072", "edge_description": "tooth crack contains initial crack, advanced crack, chipped tooth, missing tooth"},
    {"edge_id": "8ZBGXX9K_E073", "edge_description": "chipped tooth contains initial crack, advanced crack, chipped tooth, missing tooth"},
    {"edge_id": "8ZBGXX9K_E074", "edge_description": "missing tooth contains initial crack, advanced crack, chipped tooth, missing tooth"},
    {"edge_id": "8ZBGXX9K_E075", "edge_description": "gearbox contains_phm_task gear fault diagnosis"},
    {"edge_id": "8ZBGXX9K_E076", "edge_description": "spur gear contains_phm_task gear fault diagnosis"},
    {"edge_id": "8ZBGXX9K_E078", "edge_description": "tooth crack contains_phm_task gear fault diagnosis"},
    {"edge_id": "8ZBGXX9K_E079", "edge_description": "chipped tooth contains_phm_task gear fault diagnosis"},
    {"edge_id": "8ZBGXX9K_E080", "edge_description": "missing tooth contains_phm_task gear fault diagnosis"},
    {"edge_id": "8ZBGXX9K_E082", "edge_description": "gearbox induces_problem fluctuating speed without tachometer"},
    {"edge_id": "8ZBGXX9K_E083", "edge_description": "gearbox induces_problem weak fault features masked by noise"},
    {"edge_id": "8ZBGXX9K_E084", "edge_description": "spur gear induces_problem fluctuating speed without tachometer"},
    {"edge_id": "8ZBGXX9K_E085", "edge_description": "spur gear induces_problem weak fault features masked by noise"},
    {"edge_id": "8ZBGXX9K_E086", "edge_description": "fluctuating speed conditions induces_problem fluctuating speed without tachometer"},
    {"edge_id": "8ZBGXX9K_E087", "edge_description": "fluctuating speed conditions induces_problem weak fault features masked by noise"},
    {"edge_id": "8ZBGXX9K_E088", "edge_description": "initial crack, advanced crack, chipped tooth, missing tooth induces_problem fluctuating speed without tachometer"}
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
| 1 | `8ZBGXX9K_E055` | `contains` | 01-Object Domain | industrial gearbox / wind turbine applications(Industrial) |  | 02-Object Type | gearbox |  |
| 2 | `8ZBGXX9K_E056` | `contains` | 01-Object Domain | industrial gearbox / wind turbine applications(Industrial) |  | 02-Object Type | spur gear |  |
| 3 | `8ZBGXX9K_E057` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | gear / pinion |  |
| 4 | `8ZBGXX9K_E058` | `contains` | 02-Object Type | spur gear |  | 04-Fault Location | gear / pinion |  |
| 5 | `8ZBGXX9K_E059` | `contains` | 02-Object Type | gearbox |  | 03-Operating Conditions | fluctuating speed conditions(Variable Conditions) |  |
| 6 | `8ZBGXX9K_E060` | `contains` | 02-Object Type | spur gear |  | 03-Operating Conditions | fluctuating speed conditions(Variable Conditions) |  |
| 7 | `8ZBGXX9K_E061` | `contains` | 05-Fault Mode | tooth crack |  | 07-Compound Fault | No Compound Fault |  |
| 8 | `8ZBGXX9K_E062` | `contains` | 05-Fault Mode | chipped tooth |  | 07-Compound Fault | No Compound Fault |  |
| 9 | `8ZBGXX9K_E063` | `contains` | 05-Fault Mode | missing tooth |  | 07-Compound Fault | No Compound Fault |  |
| 10 | `8ZBGXX9K_E065` | `can obviously reflect` | 11-Sensor Information | uniaxial accelerometer |  | 05-Fault Mode | tooth crack |  |
| 11 | `8ZBGXX9K_E066` | `can obviously reflect` | 11-Sensor Information | uniaxial accelerometer |  | 05-Fault Mode | chipped tooth |  |
| 12 | `8ZBGXX9K_E067` | `can obviously reflect` | 11-Sensor Information | uniaxial accelerometer |  | 05-Fault Mode | missing tooth |  |
| 13 | `8ZBGXX9K_E069` | `has_fault_mode` | 04-Fault Location | gear / pinion |  | 05-Fault Mode | tooth crack |  |
| 14 | `8ZBGXX9K_E070` | `has_fault_mode` | 04-Fault Location | gear / pinion |  | 05-Fault Mode | chipped tooth |  |
| 15 | `8ZBGXX9K_E071` | `has_fault_mode` | 04-Fault Location | gear / pinion |  | 05-Fault Mode | missing tooth |  |
| 16 | `8ZBGXX9K_E072` | `contains` | 05-Fault Mode | tooth crack |  | 06-Fault Severity | initial crack, advanced crack, chipped tooth, missing tooth(Multiple Severities) |  |
| 17 | `8ZBGXX9K_E073` | `contains` | 05-Fault Mode | chipped tooth |  | 06-Fault Severity | initial crack, advanced crack, chipped tooth, missing tooth(Multiple Severities) |  |
| 18 | `8ZBGXX9K_E074` | `contains` | 05-Fault Mode | missing tooth |  | 06-Fault Severity | initial crack, advanced crack, chipped tooth, missing tooth(Multiple Severities) |  |
| 19 | `8ZBGXX9K_E075` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  |
| 20 | `8ZBGXX9K_E076` | `contains_phm_task` | 02-Object Type | spur gear |  | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  |
| 21 | `8ZBGXX9K_E078` | `contains_phm_task` | 05-Fault Mode | tooth crack |  | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  |
| 22 | `8ZBGXX9K_E079` | `contains_phm_task` | 05-Fault Mode | chipped tooth |  | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  |
| 23 | `8ZBGXX9K_E080` | `contains_phm_task` | 05-Fault Mode | missing tooth |  | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  |
| 24 | `8ZBGXX9K_E082` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | fluctuating speed without tachometer(Other) |  |
| 25 | `8ZBGXX9K_E083` | `induces_problem` | 02-Object Type | gearbox |  | 09-Problem Scenario | weak fault features masked by noise(Uncertainty) |  |
| 26 | `8ZBGXX9K_E084` | `induces_problem` | 02-Object Type | spur gear |  | 09-Problem Scenario | fluctuating speed without tachometer(Other) |  |
| 27 | `8ZBGXX9K_E085` | `induces_problem` | 02-Object Type | spur gear |  | 09-Problem Scenario | weak fault features masked by noise(Uncertainty) |  |
| 28 | `8ZBGXX9K_E086` | `induces_problem` | 03-Operating Conditions | fluctuating speed conditions(Variable Conditions) |  | 09-Problem Scenario | fluctuating speed without tachometer(Other) |  |
| 29 | `8ZBGXX9K_E087` | `induces_problem` | 03-Operating Conditions | fluctuating speed conditions(Variable Conditions) |  | 09-Problem Scenario | weak fault features masked by noise(Uncertainty) |  |
| 30 | `8ZBGXX9K_E088` | `induces_problem` | 06-Fault Severity | initial crack, advanced crack, chipped tooth, missing tooth(Multiple Severities) |  | 09-Problem Scenario | fluctuating speed without tachometer(Other) |  |

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
