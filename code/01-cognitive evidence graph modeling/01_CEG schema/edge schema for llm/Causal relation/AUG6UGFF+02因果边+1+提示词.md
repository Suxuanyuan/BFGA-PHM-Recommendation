# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AUG6UGFF
- **Paper Title**：Analysis of coupling fault correlation and nonlinear vibration of multi-stage gear transmission system
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AUG6UGFF`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AUG6UGFF_E055", "edge_description": "multi-stage gear transmission system contains fixed-axis gear"},
    {"edge_id": "AUG6UGFF_E056", "edge_description": "multi-stage gear transmission system contains planetary gear"},
    {"edge_id": "AUG6UGFF_E057", "edge_description": "fixed-axis gear contains fixed-axis pinion (spur gear 1)"},
    {"edge_id": "AUG6UGFF_E058", "edge_description": "fixed-axis gear contains planetary gear"},
    {"edge_id": "AUG6UGFF_E059", "edge_description": "planetary gear contains fixed-axis pinion (spur gear 1)"},
    {"edge_id": "AUG6UGFF_E060", "edge_description": "planetary gear contains planetary gear"},
    {"edge_id": "AUG6UGFF_E061", "edge_description": "fixed-axis gear contains motor speed-up process"},
    {"edge_id": "AUG6UGFF_E062", "edge_description": "planetary gear contains motor speed-up process"},
    {"edge_id": "AUG6UGFF_E063", "edge_description": "crack contains two faults coupling"},
    {"edge_id": "AUG6UGFF_E064", "edge_description": "broken tooth contains two faults coupling"},
    {"edge_id": "AUG6UGFF_E065", "edge_description": "acceleration sensor is collected on fixed-axis pinion (spur gear 1)"},
    {"edge_id": "AUG6UGFF_E066", "edge_description": "acceleration sensor is collected on planetary gear"},
    {"edge_id": "AUG6UGFF_E067", "edge_description": "acceleration sensor can obviously reflect crack"},
    {"edge_id": "AUG6UGFF_E068", "edge_description": "acceleration sensor can obviously reflect broken tooth"},
    {"edge_id": "AUG6UGFF_E070", "edge_description": "fixed-axis pinion (spur gear 1) has_fault_mode crack"},
    {"edge_id": "AUG6UGFF_E071", "edge_description": "fixed-axis pinion (spur gear 1) has_fault_mode broken tooth"},
    {"edge_id": "AUG6UGFF_E072", "edge_description": "planetary gear has_fault_mode crack"},
    {"edge_id": "AUG6UGFF_E073", "edge_description": "planetary gear has_fault_mode broken tooth"},
    {"edge_id": "AUG6UGFF_E074", "edge_description": "crack contains crack length 1 mm, broken tooth length 8 mm"},
    {"edge_id": "AUG6UGFF_E075", "edge_description": "broken tooth contains crack length 1 mm, broken tooth length 8 mm"},
    {"edge_id": "AUG6UGFF_E076", "edge_description": "fixed-axis gear contains_phm_task decoupling and identification of the coupling fault"},
    {"edge_id": "AUG6UGFF_E077", "edge_description": "planetary gear contains_phm_task decoupling and identification of the coupling fault"},
    {"edge_id": "AUG6UGFF_E078", "edge_description": "fixed-axis pinion (spur gear 1) contains_phm_task decoupling and identification of the coupling fault"},
    {"edge_id": "AUG6UGFF_E079", "edge_description": "planetary gear contains_phm_task decoupling and identification of the coupling fault"},
    {"edge_id": "AUG6UGFF_E080", "edge_description": "crack contains_phm_task decoupling and identification of the coupling fault"},
    {"edge_id": "AUG6UGFF_E081", "edge_description": "broken tooth contains_phm_task decoupling and identification of the coupling fault"},
    {"edge_id": "AUG6UGFF_E083", "edge_description": "fixed-axis gear induces_problem coupling fault"},
    {"edge_id": "AUG6UGFF_E084", "edge_description": "fixed-axis gear induces_problem intelligent algorithm lacks physical significance"},
    {"edge_id": "AUG6UGFF_E085", "edge_description": "planetary gear induces_problem coupling fault"},
    {"edge_id": "AUG6UGFF_E086", "edge_description": "planetary gear induces_problem intelligent algorithm lacks physical significance"}
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
| 1 | `AUG6UGFF_E055` | `contains` | 01-Object Domain | multi-stage gear transmission system(Industrial) |  | 02-Object Type | fixed-axis gear |  |
| 2 | `AUG6UGFF_E056` | `contains` | 01-Object Domain | multi-stage gear transmission system(Industrial) |  | 02-Object Type | planetary gear |  |
| 3 | `AUG6UGFF_E057` | `contains` | 02-Object Type | fixed-axis gear |  | 04-Fault Location | fixed-axis pinion (spur gear 1) |  |
| 4 | `AUG6UGFF_E058` | `contains` | 02-Object Type | fixed-axis gear |  | 04-Fault Location | planetary gear |  |
| 5 | `AUG6UGFF_E059` | `contains` | 02-Object Type | planetary gear |  | 04-Fault Location | fixed-axis pinion (spur gear 1) |  |
| 6 | `AUG6UGFF_E060` | `contains` | 02-Object Type | planetary gear |  | 04-Fault Location | planetary gear |  |
| 7 | `AUG6UGFF_E061` | `contains` | 02-Object Type | fixed-axis gear |  | 03-Operating Conditions | motor speed-up process(Variable Conditions) |  |
| 8 | `AUG6UGFF_E062` | `contains` | 02-Object Type | planetary gear |  | 03-Operating Conditions | motor speed-up process(Variable Conditions) |  |
| 9 | `AUG6UGFF_E063` | `contains` | 05-Fault Mode | crack |  | 07-Compound Fault | two faults coupling(Compound Fault Across Structures) |  |
| 10 | `AUG6UGFF_E064` | `contains` | 05-Fault Mode | broken tooth |  | 07-Compound Fault | two faults coupling(Compound Fault Across Structures) |  |
| 11 | `AUG6UGFF_E065` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | fixed-axis pinion (spur gear 1) |  |
| 12 | `AUG6UGFF_E066` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | planetary gear |  |
| 13 | `AUG6UGFF_E067` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | crack |  |
| 14 | `AUG6UGFF_E068` | `can obviously reflect` | 11-Sensor Information | acceleration sensor |  | 05-Fault Mode | broken tooth |  |
| 15 | `AUG6UGFF_E070` | `has_fault_mode` | 04-Fault Location | fixed-axis pinion (spur gear 1) |  | 05-Fault Mode | crack |  |
| 16 | `AUG6UGFF_E071` | `has_fault_mode` | 04-Fault Location | fixed-axis pinion (spur gear 1) |  | 05-Fault Mode | broken tooth |  |
| 17 | `AUG6UGFF_E072` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | crack |  |
| 18 | `AUG6UGFF_E073` | `has_fault_mode` | 04-Fault Location | planetary gear |  | 05-Fault Mode | broken tooth |  |
| 19 | `AUG6UGFF_E074` | `contains` | 05-Fault Mode | crack |  | 06-Fault Severity | crack length 1 mm, broken tooth length 8 mm(Single Severity) |  |
| 20 | `AUG6UGFF_E075` | `contains` | 05-Fault Mode | broken tooth |  | 06-Fault Severity | crack length 1 mm, broken tooth length 8 mm(Single Severity) |  |
| 21 | `AUG6UGFF_E076` | `contains_phm_task` | 02-Object Type | fixed-axis gear |  | 08-PHM Task | decoupling and identification of the coupling fault(Diagnosis Task) |  |
| 22 | `AUG6UGFF_E077` | `contains_phm_task` | 02-Object Type | planetary gear |  | 08-PHM Task | decoupling and identification of the coupling fault(Diagnosis Task) |  |
| 23 | `AUG6UGFF_E078` | `contains_phm_task` | 04-Fault Location | fixed-axis pinion (spur gear 1) |  | 08-PHM Task | decoupling and identification of the coupling fault(Diagnosis Task) |  |
| 24 | `AUG6UGFF_E079` | `contains_phm_task` | 04-Fault Location | planetary gear |  | 08-PHM Task | decoupling and identification of the coupling fault(Diagnosis Task) |  |
| 25 | `AUG6UGFF_E080` | `contains_phm_task` | 05-Fault Mode | crack |  | 08-PHM Task | decoupling and identification of the coupling fault(Diagnosis Task) |  |
| 26 | `AUG6UGFF_E081` | `contains_phm_task` | 05-Fault Mode | broken tooth |  | 08-PHM Task | decoupling and identification of the coupling fault(Diagnosis Task) |  |
| 27 | `AUG6UGFF_E083` | `induces_problem` | 02-Object Type | fixed-axis gear |  | 09-Problem Scenario | coupling fault(Compound Faults) |  |
| 28 | `AUG6UGFF_E084` | `induces_problem` | 02-Object Type | fixed-axis gear |  | 09-Problem Scenario | intelligent algorithm lacks physical significance(Trustworthiness / Interpretability) |  |
| 29 | `AUG6UGFF_E085` | `induces_problem` | 02-Object Type | planetary gear |  | 09-Problem Scenario | coupling fault(Compound Faults) |  |
| 30 | `AUG6UGFF_E086` | `induces_problem` | 02-Object Type | planetary gear |  | 09-Problem Scenario | intelligent algorithm lacks physical significance(Trustworthiness / Interpretability) |  |

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
