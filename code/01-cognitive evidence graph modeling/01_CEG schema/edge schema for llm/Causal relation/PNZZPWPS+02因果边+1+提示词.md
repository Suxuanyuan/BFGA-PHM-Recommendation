# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PNZZPWPS
- **Paper Title**：Active Fault Diagnosis on a Hydraulic Pitch System Based on Frequency-Domain Identification
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `PNZZPWPS`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PNZZPWPS_E043", "edge_description": "Wind turbines / Wind power contains hydraulic pitch actuator"},
    {"edge_id": "PNZZPWPS_E044", "edge_description": "Wind turbines / Wind power contains pitch bearing"},
    {"edge_id": "PNZZPWPS_E045", "edge_description": "hydraulic pitch actuator contains pitch bearing"},
    {"edge_id": "PNZZPWPS_E046", "edge_description": "hydraulic pitch actuator contains hydraulic pump"},
    {"edge_id": "PNZZPWPS_E047", "edge_description": "hydraulic pitch actuator contains hydraulic oil"},
    {"edge_id": "PNZZPWPS_E048", "edge_description": "pitch bearing contains pitch bearing"},
    {"edge_id": "PNZZPWPS_E049", "edge_description": "pitch bearing contains hydraulic pump"},
    {"edge_id": "PNZZPWPS_E050", "edge_description": "pitch bearing contains hydraulic oil"},
    {"edge_id": "PNZZPWPS_E051", "edge_description": "hydraulic pitch actuator contains Operating conditions (mean wind speed and turbulence intensity)"},
    {"edge_id": "PNZZPWPS_E052", "edge_description": "pitch bearing contains Operating conditions (mean wind speed and turbulence intensity)"},
    {"edge_id": "PNZZPWPS_E053", "edge_description": "high bearing friction contains No Compound Fault"},
    {"edge_id": "PNZZPWPS_E054", "edge_description": "drop in the supply pressure contains No Compound Fault"},
    {"edge_id": "PNZZPWPS_E055", "edge_description": "air contamination contains No Compound Fault"},
    {"edge_id": "PNZZPWPS_E056", "edge_description": "water contamination contains No Compound Fault"},
    {"edge_id": "PNZZPWPS_E057", "edge_description": "pitch angle sensor is collected on pitch bearing"},
    {"edge_id": "PNZZPWPS_E058", "edge_description": "pitch angle sensor is collected on hydraulic pump"},
    {"edge_id": "PNZZPWPS_E059", "edge_description": "pitch angle sensor is collected on hydraulic oil"},
    {"edge_id": "PNZZPWPS_E060", "edge_description": "pitch angle sensor can obviously reflect high bearing friction"},
    {"edge_id": "PNZZPWPS_E061", "edge_description": "pitch angle sensor can obviously reflect drop in the supply pressure"},
    {"edge_id": "PNZZPWPS_E062", "edge_description": "pitch angle sensor can obviously reflect air contamination"},
    {"edge_id": "PNZZPWPS_E063", "edge_description": "pitch angle sensor can obviously reflect water contamination"},
    {"edge_id": "PNZZPWPS_E065", "edge_description": "pitch bearing has_fault_mode high bearing friction"},
    {"edge_id": "PNZZPWPS_E066", "edge_description": "pitch bearing has_fault_mode drop in the supply pressure"},
    {"edge_id": "PNZZPWPS_E067", "edge_description": "pitch bearing has_fault_mode air contamination"},
    {"edge_id": "PNZZPWPS_E068", "edge_description": "pitch bearing has_fault_mode water contamination"},
    {"edge_id": "PNZZPWPS_E069", "edge_description": "hydraulic pump has_fault_mode high bearing friction"},
    {"edge_id": "PNZZPWPS_E070", "edge_description": "hydraulic pump has_fault_mode drop in the supply pressure"},
    {"edge_id": "PNZZPWPS_E071", "edge_description": "hydraulic pump has_fault_mode air contamination"},
    {"edge_id": "PNZZPWPS_E072", "edge_description": "hydraulic pump has_fault_mode water contamination"},
    {"edge_id": "PNZZPWPS_E073", "edge_description": "hydraulic oil has_fault_mode high bearing friction"}
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
| 1 | `PNZZPWPS_E043` | `contains` | 01-Object Domain | Wind turbines / Wind power(Industrial) |  | 02-Object Type | hydraulic pitch actuator |  |
| 2 | `PNZZPWPS_E044` | `contains` | 01-Object Domain | Wind turbines / Wind power(Industrial) |  | 02-Object Type | pitch bearing |  |
| 3 | `PNZZPWPS_E045` | `contains` | 02-Object Type | hydraulic pitch actuator |  | 04-Fault Location | pitch bearing |  |
| 4 | `PNZZPWPS_E046` | `contains` | 02-Object Type | hydraulic pitch actuator |  | 04-Fault Location | hydraulic pump |  |
| 5 | `PNZZPWPS_E047` | `contains` | 02-Object Type | hydraulic pitch actuator |  | 04-Fault Location | hydraulic oil |  |
| 6 | `PNZZPWPS_E048` | `contains` | 02-Object Type | pitch bearing |  | 04-Fault Location | pitch bearing |  |
| 7 | `PNZZPWPS_E049` | `contains` | 02-Object Type | pitch bearing |  | 04-Fault Location | hydraulic pump |  |
| 8 | `PNZZPWPS_E050` | `contains` | 02-Object Type | pitch bearing |  | 04-Fault Location | hydraulic oil |  |
| 9 | `PNZZPWPS_E051` | `contains` | 02-Object Type | hydraulic pitch actuator |  | 03-Operating Conditions | Operating conditions (mean wind speed and turbulence intensity)(Multiple Conditions) |  |
| 10 | `PNZZPWPS_E052` | `contains` | 02-Object Type | pitch bearing |  | 03-Operating Conditions | Operating conditions (mean wind speed and turbulence intensity)(Multiple Conditions) |  |
| 11 | `PNZZPWPS_E053` | `contains` | 05-Fault Mode | high bearing friction |  | 07-Compound Fault | No Compound Fault |  |
| 12 | `PNZZPWPS_E054` | `contains` | 05-Fault Mode | drop in the supply pressure |  | 07-Compound Fault | No Compound Fault |  |
| 13 | `PNZZPWPS_E055` | `contains` | 05-Fault Mode | air contamination |  | 07-Compound Fault | No Compound Fault |  |
| 14 | `PNZZPWPS_E056` | `contains` | 05-Fault Mode | water contamination |  | 07-Compound Fault | No Compound Fault |  |
| 15 | `PNZZPWPS_E057` | `is collected on` | 11-Sensor Information | pitch angle sensor |  | 04-Fault Location | pitch bearing |  |
| 16 | `PNZZPWPS_E058` | `is collected on` | 11-Sensor Information | pitch angle sensor |  | 04-Fault Location | hydraulic pump |  |
| 17 | `PNZZPWPS_E059` | `is collected on` | 11-Sensor Information | pitch angle sensor |  | 04-Fault Location | hydraulic oil |  |
| 18 | `PNZZPWPS_E060` | `can obviously reflect` | 11-Sensor Information | pitch angle sensor |  | 05-Fault Mode | high bearing friction |  |
| 19 | `PNZZPWPS_E061` | `can obviously reflect` | 11-Sensor Information | pitch angle sensor |  | 05-Fault Mode | drop in the supply pressure |  |
| 20 | `PNZZPWPS_E062` | `can obviously reflect` | 11-Sensor Information | pitch angle sensor |  | 05-Fault Mode | air contamination |  |
| 21 | `PNZZPWPS_E063` | `can obviously reflect` | 11-Sensor Information | pitch angle sensor |  | 05-Fault Mode | water contamination |  |
| 22 | `PNZZPWPS_E065` | `has_fault_mode` | 04-Fault Location | pitch bearing |  | 05-Fault Mode | high bearing friction |  |
| 23 | `PNZZPWPS_E066` | `has_fault_mode` | 04-Fault Location | pitch bearing |  | 05-Fault Mode | drop in the supply pressure |  |
| 24 | `PNZZPWPS_E067` | `has_fault_mode` | 04-Fault Location | pitch bearing |  | 05-Fault Mode | air contamination |  |
| 25 | `PNZZPWPS_E068` | `has_fault_mode` | 04-Fault Location | pitch bearing |  | 05-Fault Mode | water contamination |  |
| 26 | `PNZZPWPS_E069` | `has_fault_mode` | 04-Fault Location | hydraulic pump |  | 05-Fault Mode | high bearing friction |  |
| 27 | `PNZZPWPS_E070` | `has_fault_mode` | 04-Fault Location | hydraulic pump |  | 05-Fault Mode | drop in the supply pressure |  |
| 28 | `PNZZPWPS_E071` | `has_fault_mode` | 04-Fault Location | hydraulic pump |  | 05-Fault Mode | air contamination |  |
| 29 | `PNZZPWPS_E072` | `has_fault_mode` | 04-Fault Location | hydraulic pump |  | 05-Fault Mode | water contamination |  |
| 30 | `PNZZPWPS_E073` | `has_fault_mode` | 04-Fault Location | hydraulic oil |  | 05-Fault Mode | high bearing friction |  |

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
