# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：XCF2RRRB
- **Paper Title**：Study of factors impacting remote diagnosis performance on a PLC based automated system
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `XCF2RRRB`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "XCF2RRRB_E053", "edge_description": "Load cell can obviously reflect communication failure"},
    {"edge_id": "XCF2RRRB_E054", "edge_description": "Load cell can obviously reflect tolerance fault"},
    {"edge_id": "XCF2RRRB_E056", "edge_description": "sensor has_fault_mode sensor fault"},
    {"edge_id": "XCF2RRRB_E057", "edge_description": "sensor has_fault_mode software error"},
    {"edge_id": "XCF2RRRB_E058", "edge_description": "sensor has_fault_mode communication failure"},
    {"edge_id": "XCF2RRRB_E059", "edge_description": "sensor has_fault_mode tolerance fault"},
    {"edge_id": "XCF2RRRB_E060", "edge_description": "PLC has_fault_mode sensor fault"},
    {"edge_id": "XCF2RRRB_E061", "edge_description": "PLC has_fault_mode software error"},
    {"edge_id": "XCF2RRRB_E062", "edge_description": "PLC has_fault_mode communication failure"},
    {"edge_id": "XCF2RRRB_E063", "edge_description": "PLC has_fault_mode tolerance fault"},
    {"edge_id": "XCF2RRRB_E064", "edge_description": "solenoid valve has_fault_mode sensor fault"},
    {"edge_id": "XCF2RRRB_E065", "edge_description": "solenoid valve has_fault_mode software error"},
    {"edge_id": "XCF2RRRB_E066", "edge_description": "solenoid valve has_fault_mode communication failure"},
    {"edge_id": "XCF2RRRB_E067", "edge_description": "solenoid valve has_fault_mode tolerance fault"},
    {"edge_id": "XCF2RRRB_E068", "edge_description": "robotic gripper has_fault_mode sensor fault"},
    {"edge_id": "XCF2RRRB_E069", "edge_description": "robotic gripper has_fault_mode software error"},
    {"edge_id": "XCF2RRRB_E070", "edge_description": "robotic gripper has_fault_mode communication failure"},
    {"edge_id": "XCF2RRRB_E071", "edge_description": "robotic gripper has_fault_mode tolerance fault"},
    {"edge_id": "XCF2RRRB_E072", "edge_description": "sensor fault contains Single Severity"},
    {"edge_id": "XCF2RRRB_E073", "edge_description": "software error contains Single Severity"},
    {"edge_id": "XCF2RRRB_E074", "edge_description": "communication failure contains Single Severity"},
    {"edge_id": "XCF2RRRB_E075", "edge_description": "tolerance fault contains Single Severity"},
    {"edge_id": "XCF2RRRB_E076", "edge_description": "robot arm contains_phm_task remote fault diagnosis"},
    {"edge_id": "XCF2RRRB_E077", "edge_description": "programmable logic controller (PLC) contains_phm_task remote fault diagnosis"},
    {"edge_id": "XCF2RRRB_E078", "edge_description": "sensor contains_phm_task remote fault diagnosis"},
    {"edge_id": "XCF2RRRB_E079", "edge_description": "PLC contains_phm_task remote fault diagnosis"},
    {"edge_id": "XCF2RRRB_E080", "edge_description": "solenoid valve contains_phm_task remote fault diagnosis"},
    {"edge_id": "XCF2RRRB_E081", "edge_description": "robotic gripper contains_phm_task remote fault diagnosis"},
    {"edge_id": "XCF2RRRB_E082", "edge_description": "sensor fault contains_phm_task remote fault diagnosis"},
    {"edge_id": "XCF2RRRB_E083", "edge_description": "software error contains_phm_task remote fault diagnosis"}
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
| 1 | `XCF2RRRB_E053` | `can obviously reflect` | 11-Sensor Information | Load cell |  | 05-Fault Mode | communication failure |  |
| 2 | `XCF2RRRB_E054` | `can obviously reflect` | 11-Sensor Information | Load cell |  | 05-Fault Mode | tolerance fault |  |
| 3 | `XCF2RRRB_E056` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | sensor fault |  |
| 4 | `XCF2RRRB_E057` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | software error |  |
| 5 | `XCF2RRRB_E058` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | communication failure |  |
| 6 | `XCF2RRRB_E059` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | tolerance fault |  |
| 7 | `XCF2RRRB_E060` | `has_fault_mode` | 04-Fault Location | PLC |  | 05-Fault Mode | sensor fault |  |
| 8 | `XCF2RRRB_E061` | `has_fault_mode` | 04-Fault Location | PLC |  | 05-Fault Mode | software error |  |
| 9 | `XCF2RRRB_E062` | `has_fault_mode` | 04-Fault Location | PLC |  | 05-Fault Mode | communication failure |  |
| 10 | `XCF2RRRB_E063` | `has_fault_mode` | 04-Fault Location | PLC |  | 05-Fault Mode | tolerance fault |  |
| 11 | `XCF2RRRB_E064` | `has_fault_mode` | 04-Fault Location | solenoid valve |  | 05-Fault Mode | sensor fault |  |
| 12 | `XCF2RRRB_E065` | `has_fault_mode` | 04-Fault Location | solenoid valve |  | 05-Fault Mode | software error |  |
| 13 | `XCF2RRRB_E066` | `has_fault_mode` | 04-Fault Location | solenoid valve |  | 05-Fault Mode | communication failure |  |
| 14 | `XCF2RRRB_E067` | `has_fault_mode` | 04-Fault Location | solenoid valve |  | 05-Fault Mode | tolerance fault |  |
| 15 | `XCF2RRRB_E068` | `has_fault_mode` | 04-Fault Location | robotic gripper |  | 05-Fault Mode | sensor fault |  |
| 16 | `XCF2RRRB_E069` | `has_fault_mode` | 04-Fault Location | robotic gripper |  | 05-Fault Mode | software error |  |
| 17 | `XCF2RRRB_E070` | `has_fault_mode` | 04-Fault Location | robotic gripper |  | 05-Fault Mode | communication failure |  |
| 18 | `XCF2RRRB_E071` | `has_fault_mode` | 04-Fault Location | robotic gripper |  | 05-Fault Mode | tolerance fault |  |
| 19 | `XCF2RRRB_E072` | `contains` | 05-Fault Mode | sensor fault |  | 06-Fault Severity | Single Severity |  |
| 20 | `XCF2RRRB_E073` | `contains` | 05-Fault Mode | software error |  | 06-Fault Severity | Single Severity |  |
| 21 | `XCF2RRRB_E074` | `contains` | 05-Fault Mode | communication failure |  | 06-Fault Severity | Single Severity |  |
| 22 | `XCF2RRRB_E075` | `contains` | 05-Fault Mode | tolerance fault |  | 06-Fault Severity | Single Severity |  |
| 23 | `XCF2RRRB_E076` | `contains_phm_task` | 02-Object Type | robot arm |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |
| 24 | `XCF2RRRB_E077` | `contains_phm_task` | 02-Object Type | programmable logic controller (PLC) |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |
| 25 | `XCF2RRRB_E078` | `contains_phm_task` | 04-Fault Location | sensor |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |
| 26 | `XCF2RRRB_E079` | `contains_phm_task` | 04-Fault Location | PLC |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |
| 27 | `XCF2RRRB_E080` | `contains_phm_task` | 04-Fault Location | solenoid valve |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |
| 28 | `XCF2RRRB_E081` | `contains_phm_task` | 04-Fault Location | robotic gripper |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |
| 29 | `XCF2RRRB_E082` | `contains_phm_task` | 05-Fault Mode | sensor fault |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |
| 30 | `XCF2RRRB_E083` | `contains_phm_task` | 05-Fault Mode | software error |  | 08-PHM Task | remote fault diagnosis(Diagnosis Task) |  |

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
