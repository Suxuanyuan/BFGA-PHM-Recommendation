# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：NNJ4BWXV
- **Paper Title**：Intelligent Decision Support System for Detection and Root Cause Analysis of Faults in Coal Mills
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `NNJ4BWXV`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "NNJ4BWXV_E026", "edge_description": "coal mill contains coal mill"},
    {"edge_id": "NNJ4BWXV_E027", "edge_description": "coal mill contains coal feeder"},
    {"edge_id": "NNJ4BWXV_E028", "edge_description": "coal mill contains reject line"},
    {"edge_id": "NNJ4BWXV_E030", "edge_description": "mill choking contains No Compound Fault"},
    {"edge_id": "NNJ4BWXV_E031", "edge_description": "coal shortage contains No Compound Fault"},
    {"edge_id": "NNJ4BWXV_E032", "edge_description": "mill fire contains No Compound Fault"},
    {"edge_id": "NNJ4BWXV_E033", "edge_description": "reject choked contains No Compound Fault"},
    {"edge_id": "NNJ4BWXV_E034", "edge_description": "temperature sensor is collected on coal mill"},
    {"edge_id": "NNJ4BWXV_E035", "edge_description": "temperature sensor is collected on coal feeder"},
    {"edge_id": "NNJ4BWXV_E036", "edge_description": "temperature sensor is collected on reject line"},
    {"edge_id": "NNJ4BWXV_E037", "edge_description": "differential pressure sensor is collected on coal mill"},
    {"edge_id": "NNJ4BWXV_E038", "edge_description": "differential pressure sensor is collected on coal feeder"},
    {"edge_id": "NNJ4BWXV_E039", "edge_description": "differential pressure sensor is collected on reject line"},
    {"edge_id": "NNJ4BWXV_E040", "edge_description": "current sensor is collected on coal mill"},
    {"edge_id": "NNJ4BWXV_E041", "edge_description": "current sensor is collected on coal feeder"},
    {"edge_id": "NNJ4BWXV_E042", "edge_description": "current sensor is collected on reject line"},
    {"edge_id": "NNJ4BWXV_E043", "edge_description": "speed sensor is collected on coal mill"},
    {"edge_id": "NNJ4BWXV_E044", "edge_description": "speed sensor is collected on coal feeder"},
    {"edge_id": "NNJ4BWXV_E045", "edge_description": "speed sensor is collected on reject line"},
    {"edge_id": "NNJ4BWXV_E046", "edge_description": "flow sensor is collected on coal mill"},
    {"edge_id": "NNJ4BWXV_E047", "edge_description": "flow sensor is collected on coal feeder"},
    {"edge_id": "NNJ4BWXV_E048", "edge_description": "flow sensor is collected on reject line"},
    {"edge_id": "NNJ4BWXV_E049", "edge_description": "temperature sensor can obviously reflect mill choking"},
    {"edge_id": "NNJ4BWXV_E050", "edge_description": "temperature sensor can obviously reflect coal shortage"},
    {"edge_id": "NNJ4BWXV_E051", "edge_description": "temperature sensor can obviously reflect mill fire"},
    {"edge_id": "NNJ4BWXV_E052", "edge_description": "temperature sensor can obviously reflect reject choked"},
    {"edge_id": "NNJ4BWXV_E053", "edge_description": "differential pressure sensor can obviously reflect mill choking"},
    {"edge_id": "NNJ4BWXV_E054", "edge_description": "differential pressure sensor can obviously reflect coal shortage"},
    {"edge_id": "NNJ4BWXV_E055", "edge_description": "differential pressure sensor can obviously reflect mill fire"},
    {"edge_id": "NNJ4BWXV_E056", "edge_description": "differential pressure sensor can obviously reflect reject choked"}
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
| 1 | `NNJ4BWXV_E026` | `contains` | 02-Object Type | coal mill |  | 04-Fault Location | coal mill |  |
| 2 | `NNJ4BWXV_E027` | `contains` | 02-Object Type | coal mill |  | 04-Fault Location | coal feeder |  |
| 3 | `NNJ4BWXV_E028` | `contains` | 02-Object Type | coal mill |  | 04-Fault Location | reject line |  |
| 4 | `NNJ4BWXV_E030` | `contains` | 05-Fault Mode | mill choking |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `NNJ4BWXV_E031` | `contains` | 05-Fault Mode | coal shortage |  | 07-Compound Fault | No Compound Fault |  |
| 6 | `NNJ4BWXV_E032` | `contains` | 05-Fault Mode | mill fire |  | 07-Compound Fault | No Compound Fault |  |
| 7 | `NNJ4BWXV_E033` | `contains` | 05-Fault Mode | reject choked |  | 07-Compound Fault | No Compound Fault |  |
| 8 | `NNJ4BWXV_E034` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | coal mill |  |
| 9 | `NNJ4BWXV_E035` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | coal feeder |  |
| 10 | `NNJ4BWXV_E036` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | reject line |  |
| 11 | `NNJ4BWXV_E037` | `is collected on` | 11-Sensor Information | differential pressure sensor |  | 04-Fault Location | coal mill |  |
| 12 | `NNJ4BWXV_E038` | `is collected on` | 11-Sensor Information | differential pressure sensor |  | 04-Fault Location | coal feeder |  |
| 13 | `NNJ4BWXV_E039` | `is collected on` | 11-Sensor Information | differential pressure sensor |  | 04-Fault Location | reject line |  |
| 14 | `NNJ4BWXV_E040` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | coal mill |  |
| 15 | `NNJ4BWXV_E041` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | coal feeder |  |
| 16 | `NNJ4BWXV_E042` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | reject line |  |
| 17 | `NNJ4BWXV_E043` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | coal mill |  |
| 18 | `NNJ4BWXV_E044` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | coal feeder |  |
| 19 | `NNJ4BWXV_E045` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | reject line |  |
| 20 | `NNJ4BWXV_E046` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | coal mill |  |
| 21 | `NNJ4BWXV_E047` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | coal feeder |  |
| 22 | `NNJ4BWXV_E048` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | reject line |  |
| 23 | `NNJ4BWXV_E049` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | mill choking |  |
| 24 | `NNJ4BWXV_E050` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | coal shortage |  |
| 25 | `NNJ4BWXV_E051` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | mill fire |  |
| 26 | `NNJ4BWXV_E052` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | reject choked |  |
| 27 | `NNJ4BWXV_E053` | `can obviously reflect` | 11-Sensor Information | differential pressure sensor |  | 05-Fault Mode | mill choking |  |
| 28 | `NNJ4BWXV_E054` | `can obviously reflect` | 11-Sensor Information | differential pressure sensor |  | 05-Fault Mode | coal shortage |  |
| 29 | `NNJ4BWXV_E055` | `can obviously reflect` | 11-Sensor Information | differential pressure sensor |  | 05-Fault Mode | mill fire |  |
| 30 | `NNJ4BWXV_E056` | `can obviously reflect` | 11-Sensor Information | differential pressure sensor |  | 05-Fault Mode | reject choked |  |

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
