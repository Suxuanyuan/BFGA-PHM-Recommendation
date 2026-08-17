# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WNVRAXPR
- **Paper Title**：Multiblock Concurrent PLS for Decentralized Monitoring of Continuous Annealing Processes
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `WNVRAXPR`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WNVRAXPR_E061", "edge_description": "cold rolling continuous annealing processes contains carrying roll"},
    {"edge_id": "WNVRAXPR_E062", "edge_description": "cold rolling continuous annealing processes contains motor"},
    {"edge_id": "WNVRAXPR_E063", "edge_description": "cold rolling continuous annealing processes contains dancer roll"},
    {"edge_id": "WNVRAXPR_E064", "edge_description": "carrying roll contains steel strip"},
    {"edge_id": "WNVRAXPR_E065", "edge_description": "motor contains steel strip"},
    {"edge_id": "WNVRAXPR_E066", "edge_description": "dancer roll contains steel strip"},
    {"edge_id": "WNVRAXPR_E067", "edge_description": "carrying roll contains normal operation"},
    {"edge_id": "WNVRAXPR_E068", "edge_description": "motor contains normal operation"},
    {"edge_id": "WNVRAXPR_E069", "edge_description": "dancer roll contains normal operation"},
    {"edge_id": "WNVRAXPR_E070", "edge_description": "defective processing material contains No Compound Fault"},
    {"edge_id": "WNVRAXPR_E071", "edge_description": "strip break contains No Compound Fault"},
    {"edge_id": "WNVRAXPR_E072", "edge_description": "speed sensor is collected on steel strip"},
    {"edge_id": "WNVRAXPR_E073", "edge_description": "current sensor is collected on steel strip"},
    {"edge_id": "WNVRAXPR_E074", "edge_description": "pressure sensor is collected on steel strip"},
    {"edge_id": "WNVRAXPR_E075", "edge_description": "speed sensor can obviously reflect defective processing material"},
    {"edge_id": "WNVRAXPR_E076", "edge_description": "speed sensor can obviously reflect strip break"},
    {"edge_id": "WNVRAXPR_E077", "edge_description": "current sensor can obviously reflect defective processing material"},
    {"edge_id": "WNVRAXPR_E078", "edge_description": "current sensor can obviously reflect strip break"},
    {"edge_id": "WNVRAXPR_E079", "edge_description": "pressure sensor can obviously reflect defective processing material"},
    {"edge_id": "WNVRAXPR_E080", "edge_description": "pressure sensor can obviously reflect strip break"},
    {"edge_id": "WNVRAXPR_E082", "edge_description": "steel strip has_fault_mode defective processing material"},
    {"edge_id": "WNVRAXPR_E083", "edge_description": "steel strip has_fault_mode strip break"},
    {"edge_id": "WNVRAXPR_E084", "edge_description": "defective processing material contains Single Severity"},
    {"edge_id": "WNVRAXPR_E085", "edge_description": "strip break contains Single Severity"},
    {"edge_id": "WNVRAXPR_E086", "edge_description": "carrying roll contains_phm_task decentralized process monitoring and fault diagnosis"},
    {"edge_id": "WNVRAXPR_E087", "edge_description": "motor contains_phm_task decentralized process monitoring and fault diagnosis"},
    {"edge_id": "WNVRAXPR_E088", "edge_description": "dancer roll contains_phm_task decentralized process monitoring and fault diagnosis"},
    {"edge_id": "WNVRAXPR_E090", "edge_description": "defective processing material contains_phm_task decentralized process monitoring and fault diagnosis"},
    {"edge_id": "WNVRAXPR_E091", "edge_description": "strip break contains_phm_task decentralized process monitoring and fault diagnosis"},
    {"edge_id": "WNVRAXPR_E093", "edge_description": "carrying roll induces_problem large-scale processes monitoring"}
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
| 1 | `WNVRAXPR_E061` | `contains` | 01-Object Domain | cold rolling continuous annealing processes(Industrial) |  | 02-Object Type | carrying roll |  |
| 2 | `WNVRAXPR_E062` | `contains` | 01-Object Domain | cold rolling continuous annealing processes(Industrial) |  | 02-Object Type | motor |  |
| 3 | `WNVRAXPR_E063` | `contains` | 01-Object Domain | cold rolling continuous annealing processes(Industrial) |  | 02-Object Type | dancer roll |  |
| 4 | `WNVRAXPR_E064` | `contains` | 02-Object Type | carrying roll |  | 04-Fault Location | steel strip |  |
| 5 | `WNVRAXPR_E065` | `contains` | 02-Object Type | motor |  | 04-Fault Location | steel strip |  |
| 6 | `WNVRAXPR_E066` | `contains` | 02-Object Type | dancer roll |  | 04-Fault Location | steel strip |  |
| 7 | `WNVRAXPR_E067` | `contains` | 02-Object Type | carrying roll |  | 03-Operating Conditions | normal operation(Single Condition) |  |
| 8 | `WNVRAXPR_E068` | `contains` | 02-Object Type | motor |  | 03-Operating Conditions | normal operation(Single Condition) |  |
| 9 | `WNVRAXPR_E069` | `contains` | 02-Object Type | dancer roll |  | 03-Operating Conditions | normal operation(Single Condition) |  |
| 10 | `WNVRAXPR_E070` | `contains` | 05-Fault Mode | defective processing material |  | 07-Compound Fault | No Compound Fault |  |
| 11 | `WNVRAXPR_E071` | `contains` | 05-Fault Mode | strip break |  | 07-Compound Fault | No Compound Fault |  |
| 12 | `WNVRAXPR_E072` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | steel strip |  |
| 13 | `WNVRAXPR_E073` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | steel strip |  |
| 14 | `WNVRAXPR_E074` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | steel strip |  |
| 15 | `WNVRAXPR_E075` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | defective processing material |  |
| 16 | `WNVRAXPR_E076` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | strip break |  |
| 17 | `WNVRAXPR_E077` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | defective processing material |  |
| 18 | `WNVRAXPR_E078` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | strip break |  |
| 19 | `WNVRAXPR_E079` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | defective processing material |  |
| 20 | `WNVRAXPR_E080` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | strip break |  |
| 21 | `WNVRAXPR_E082` | `has_fault_mode` | 04-Fault Location | steel strip |  | 05-Fault Mode | defective processing material |  |
| 22 | `WNVRAXPR_E083` | `has_fault_mode` | 04-Fault Location | steel strip |  | 05-Fault Mode | strip break |  |
| 23 | `WNVRAXPR_E084` | `contains` | 05-Fault Mode | defective processing material |  | 06-Fault Severity | Single Severity |  |
| 24 | `WNVRAXPR_E085` | `contains` | 05-Fault Mode | strip break |  | 06-Fault Severity | Single Severity |  |
| 25 | `WNVRAXPR_E086` | `contains_phm_task` | 02-Object Type | carrying roll |  | 08-PHM Task | decentralized process monitoring and fault diagnosis(Diagnosis Task) |  |
| 26 | `WNVRAXPR_E087` | `contains_phm_task` | 02-Object Type | motor |  | 08-PHM Task | decentralized process monitoring and fault diagnosis(Diagnosis Task) |  |
| 27 | `WNVRAXPR_E088` | `contains_phm_task` | 02-Object Type | dancer roll |  | 08-PHM Task | decentralized process monitoring and fault diagnosis(Diagnosis Task) |  |
| 28 | `WNVRAXPR_E090` | `contains_phm_task` | 05-Fault Mode | defective processing material |  | 08-PHM Task | decentralized process monitoring and fault diagnosis(Diagnosis Task) |  |
| 29 | `WNVRAXPR_E091` | `contains_phm_task` | 05-Fault Mode | strip break |  | 08-PHM Task | decentralized process monitoring and fault diagnosis(Diagnosis Task) |  |
| 30 | `WNVRAXPR_E093` | `induces_problem` | 02-Object Type | carrying roll |  | 09-Problem Scenario | large-scale processes monitoring(Complex Systems) |  |

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
