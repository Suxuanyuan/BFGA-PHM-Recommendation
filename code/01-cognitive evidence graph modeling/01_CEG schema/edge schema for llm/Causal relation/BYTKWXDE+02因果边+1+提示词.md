# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：BYTKWXDE
- **Paper Title**：A New Nonlinear Model-Based Fault Detection Method Using Mann-Whitney Test
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `BYTKWXDE`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "BYTKWXDE_E040", "edge_description": "three vessel water tank system contains tank 3"},
    {"edge_id": "BYTKWXDE_E041", "edge_description": "three vessel water tank system contains sensor"},
    {"edge_id": "BYTKWXDE_E042", "edge_description": "three vessel water tank system contains outflow pipe"},
    {"edge_id": "BYTKWXDE_E044", "edge_description": "leakage contains Sensor fault and component fault are considered simultaneously"},
    {"edge_id": "BYTKWXDE_E045", "edge_description": "sensor fault contains Sensor fault and component fault are considered simultaneously"},
    {"edge_id": "BYTKWXDE_E046", "edge_description": "jamming contains Sensor fault and component fault are considered simultaneously"},
    {"edge_id": "BYTKWXDE_E047", "edge_description": "level sensor is collected on tank 3"},
    {"edge_id": "BYTKWXDE_E048", "edge_description": "level sensor is collected on sensor"},
    {"edge_id": "BYTKWXDE_E049", "edge_description": "level sensor is collected on outflow pipe"},
    {"edge_id": "BYTKWXDE_E050", "edge_description": "level sensor can obviously reflect leakage"},
    {"edge_id": "BYTKWXDE_E051", "edge_description": "level sensor can obviously reflect sensor fault"},
    {"edge_id": "BYTKWXDE_E052", "edge_description": "level sensor can obviously reflect jamming"},
    {"edge_id": "BYTKWXDE_E054", "edge_description": "tank 3 has_fault_mode leakage"},
    {"edge_id": "BYTKWXDE_E055", "edge_description": "tank 3 has_fault_mode sensor fault"},
    {"edge_id": "BYTKWXDE_E056", "edge_description": "tank 3 has_fault_mode jamming"},
    {"edge_id": "BYTKWXDE_E057", "edge_description": "sensor has_fault_mode leakage"},
    {"edge_id": "BYTKWXDE_E058", "edge_description": "sensor has_fault_mode sensor fault"},
    {"edge_id": "BYTKWXDE_E059", "edge_description": "sensor has_fault_mode jamming"},
    {"edge_id": "BYTKWXDE_E060", "edge_description": "outflow pipe has_fault_mode leakage"},
    {"edge_id": "BYTKWXDE_E061", "edge_description": "outflow pipe has_fault_mode sensor fault"},
    {"edge_id": "BYTKWXDE_E062", "edge_description": "outflow pipe has_fault_mode jamming"},
    {"edge_id": "BYTKWXDE_E063", "edge_description": "leakage contains c = 0.3, r = 0.5cm, f2,1,k = -4 x 10^-5 m^3/s, f2,2,k = 3 x 10^-5 m^3/s"},
    {"edge_id": "BYTKWXDE_E064", "edge_description": "sensor fault contains c = 0.3, r = 0.5cm, f2,1,k = -4 x 10^-5 m^3/s, f2,2,k = 3 x 10^-5 m^3/s"},
    {"edge_id": "BYTKWXDE_E065", "edge_description": "jamming contains c = 0.3, r = 0.5cm, f2,1,k = -4 x 10^-5 m^3/s, f2,2,k = 3 x 10^-5 m^3/s"},
    {"edge_id": "BYTKWXDE_E067", "edge_description": "tank 3 contains_phm_task fault detection"},
    {"edge_id": "BYTKWXDE_E068", "edge_description": "sensor contains_phm_task fault detection"},
    {"edge_id": "BYTKWXDE_E069", "edge_description": "outflow pipe contains_phm_task fault detection"},
    {"edge_id": "BYTKWXDE_E070", "edge_description": "leakage contains_phm_task fault detection"},
    {"edge_id": "BYTKWXDE_E071", "edge_description": "sensor fault contains_phm_task fault detection"},
    {"edge_id": "BYTKWXDE_E072", "edge_description": "jamming contains_phm_task fault detection"}
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
| 1 | `BYTKWXDE_E040` | `contains` | 02-Object Type | three vessel water tank system |  | 04-Fault Location | tank 3 |  |
| 2 | `BYTKWXDE_E041` | `contains` | 02-Object Type | three vessel water tank system |  | 04-Fault Location | sensor |  |
| 3 | `BYTKWXDE_E042` | `contains` | 02-Object Type | three vessel water tank system |  | 04-Fault Location | outflow pipe |  |
| 4 | `BYTKWXDE_E044` | `contains` | 05-Fault Mode | leakage |  | 07-Compound Fault | Sensor fault and component fault are considered simultaneously(Compound Fault Across Structures) |  |
| 5 | `BYTKWXDE_E045` | `contains` | 05-Fault Mode | sensor fault |  | 07-Compound Fault | Sensor fault and component fault are considered simultaneously(Compound Fault Across Structures) |  |
| 6 | `BYTKWXDE_E046` | `contains` | 05-Fault Mode | jamming |  | 07-Compound Fault | Sensor fault and component fault are considered simultaneously(Compound Fault Across Structures) |  |
| 7 | `BYTKWXDE_E047` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | tank 3 |  |
| 8 | `BYTKWXDE_E048` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | sensor |  |
| 9 | `BYTKWXDE_E049` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | outflow pipe |  |
| 10 | `BYTKWXDE_E050` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | leakage |  |
| 11 | `BYTKWXDE_E051` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | sensor fault |  |
| 12 | `BYTKWXDE_E052` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | jamming |  |
| 13 | `BYTKWXDE_E054` | `has_fault_mode` | 04-Fault Location | tank 3 |  | 05-Fault Mode | leakage |  |
| 14 | `BYTKWXDE_E055` | `has_fault_mode` | 04-Fault Location | tank 3 |  | 05-Fault Mode | sensor fault |  |
| 15 | `BYTKWXDE_E056` | `has_fault_mode` | 04-Fault Location | tank 3 |  | 05-Fault Mode | jamming |  |
| 16 | `BYTKWXDE_E057` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | leakage |  |
| 17 | `BYTKWXDE_E058` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | sensor fault |  |
| 18 | `BYTKWXDE_E059` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | jamming |  |
| 19 | `BYTKWXDE_E060` | `has_fault_mode` | 04-Fault Location | outflow pipe |  | 05-Fault Mode | leakage |  |
| 20 | `BYTKWXDE_E061` | `has_fault_mode` | 04-Fault Location | outflow pipe |  | 05-Fault Mode | sensor fault |  |
| 21 | `BYTKWXDE_E062` | `has_fault_mode` | 04-Fault Location | outflow pipe |  | 05-Fault Mode | jamming |  |
| 22 | `BYTKWXDE_E063` | `contains` | 05-Fault Mode | leakage |  | 06-Fault Severity | c = 0.3, r = 0.5cm, f2,1,k = -4 x 10^-5 m^3/s, f2,2,k = 3 x 10^-5 m^3/s(Single Severity) |  |
| 23 | `BYTKWXDE_E064` | `contains` | 05-Fault Mode | sensor fault |  | 06-Fault Severity | c = 0.3, r = 0.5cm, f2,1,k = -4 x 10^-5 m^3/s, f2,2,k = 3 x 10^-5 m^3/s(Single Severity) |  |
| 24 | `BYTKWXDE_E065` | `contains` | 05-Fault Mode | jamming |  | 06-Fault Severity | c = 0.3, r = 0.5cm, f2,1,k = -4 x 10^-5 m^3/s, f2,2,k = 3 x 10^-5 m^3/s(Single Severity) |  |
| 25 | `BYTKWXDE_E067` | `contains_phm_task` | 04-Fault Location | tank 3 |  | 08-PHM Task | fault detection(Detection Task) |  |
| 26 | `BYTKWXDE_E068` | `contains_phm_task` | 04-Fault Location | sensor |  | 08-PHM Task | fault detection(Detection Task) |  |
| 27 | `BYTKWXDE_E069` | `contains_phm_task` | 04-Fault Location | outflow pipe |  | 08-PHM Task | fault detection(Detection Task) |  |
| 28 | `BYTKWXDE_E070` | `contains_phm_task` | 05-Fault Mode | leakage |  | 08-PHM Task | fault detection(Detection Task) |  |
| 29 | `BYTKWXDE_E071` | `contains_phm_task` | 05-Fault Mode | sensor fault |  | 08-PHM Task | fault detection(Detection Task) |  |
| 30 | `BYTKWXDE_E072` | `contains_phm_task` | 05-Fault Mode | jamming |  | 08-PHM Task | fault detection(Detection Task) |  |

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
