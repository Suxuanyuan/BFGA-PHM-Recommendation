# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：FAYJBWAM
- **Paper Title**：A neuro-inspired computational model for adaptive fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `FAYJBWAM`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "FAYJBWAM_E102", "edge_description": "turbofan engine contains Fan"},
    {"edge_id": "FAYJBWAM_E103", "edge_description": "turbofan engine contains High-pressure turbine"},
    {"edge_id": "FAYJBWAM_E104", "edge_description": "turbofan engine contains Variable stator vanes"},
    {"edge_id": "FAYJBWAM_E105", "edge_description": "turbofan engine contains Sensor"},
    {"edge_id": "FAYJBWAM_E107", "edge_description": "Fan fault contains No Compound Fault"},
    {"edge_id": "FAYJBWAM_E108", "edge_description": "HPT fault contains No Compound Fault"},
    {"edge_id": "FAYJBWAM_E109", "edge_description": "Variable stator vanes fault contains No Compound Fault"},
    {"edge_id": "FAYJBWAM_E110", "edge_description": "Sensor fault contains No Compound Fault"},
    {"edge_id": "FAYJBWAM_E111", "edge_description": "temperature sensor is collected on Fan"},
    {"edge_id": "FAYJBWAM_E112", "edge_description": "temperature sensor is collected on High-pressure turbine"},
    {"edge_id": "FAYJBWAM_E113", "edge_description": "temperature sensor is collected on Variable stator vanes"},
    {"edge_id": "FAYJBWAM_E114", "edge_description": "temperature sensor is collected on Sensor"},
    {"edge_id": "FAYJBWAM_E115", "edge_description": "pressure sensor is collected on Fan"},
    {"edge_id": "FAYJBWAM_E116", "edge_description": "pressure sensor is collected on High-pressure turbine"},
    {"edge_id": "FAYJBWAM_E117", "edge_description": "pressure sensor is collected on Variable stator vanes"},
    {"edge_id": "FAYJBWAM_E118", "edge_description": "pressure sensor is collected on Sensor"},
    {"edge_id": "FAYJBWAM_E119", "edge_description": "speed sensor is collected on Fan"},
    {"edge_id": "FAYJBWAM_E120", "edge_description": "speed sensor is collected on High-pressure turbine"},
    {"edge_id": "FAYJBWAM_E121", "edge_description": "speed sensor is collected on Variable stator vanes"},
    {"edge_id": "FAYJBWAM_E122", "edge_description": "speed sensor is collected on Sensor"},
    {"edge_id": "FAYJBWAM_E123", "edge_description": "fuel flow sensor is collected on Fan"},
    {"edge_id": "FAYJBWAM_E124", "edge_description": "fuel flow sensor is collected on High-pressure turbine"},
    {"edge_id": "FAYJBWAM_E125", "edge_description": "fuel flow sensor is collected on Variable stator vanes"},
    {"edge_id": "FAYJBWAM_E126", "edge_description": "fuel flow sensor is collected on Sensor"},
    {"edge_id": "FAYJBWAM_E127", "edge_description": "temperature sensor can obviously reflect Fan fault"},
    {"edge_id": "FAYJBWAM_E128", "edge_description": "temperature sensor can obviously reflect HPT fault"},
    {"edge_id": "FAYJBWAM_E129", "edge_description": "temperature sensor can obviously reflect Variable stator vanes fault"},
    {"edge_id": "FAYJBWAM_E130", "edge_description": "temperature sensor can obviously reflect Sensor fault"},
    {"edge_id": "FAYJBWAM_E131", "edge_description": "pressure sensor can obviously reflect Fan fault"},
    {"edge_id": "FAYJBWAM_E132", "edge_description": "pressure sensor can obviously reflect HPT fault"}
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
| 1 | `FAYJBWAM_E102` | `contains` | 02-Object Type | turbofan engine |  | 04-Fault Location | Fan |  |
| 2 | `FAYJBWAM_E103` | `contains` | 02-Object Type | turbofan engine |  | 04-Fault Location | High-pressure turbine |  |
| 3 | `FAYJBWAM_E104` | `contains` | 02-Object Type | turbofan engine |  | 04-Fault Location | Variable stator vanes |  |
| 4 | `FAYJBWAM_E105` | `contains` | 02-Object Type | turbofan engine |  | 04-Fault Location | Sensor |  |
| 5 | `FAYJBWAM_E107` | `contains` | 05-Fault Mode | Fan fault |  | 07-Compound Fault | No Compound Fault |  |
| 6 | `FAYJBWAM_E108` | `contains` | 05-Fault Mode | HPT fault |  | 07-Compound Fault | No Compound Fault |  |
| 7 | `FAYJBWAM_E109` | `contains` | 05-Fault Mode | Variable stator vanes fault |  | 07-Compound Fault | No Compound Fault |  |
| 8 | `FAYJBWAM_E110` | `contains` | 05-Fault Mode | Sensor fault |  | 07-Compound Fault | No Compound Fault |  |
| 9 | `FAYJBWAM_E111` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | Fan |  |
| 10 | `FAYJBWAM_E112` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | High-pressure turbine |  |
| 11 | `FAYJBWAM_E113` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | Variable stator vanes |  |
| 12 | `FAYJBWAM_E114` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | Sensor |  |
| 13 | `FAYJBWAM_E115` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | Fan |  |
| 14 | `FAYJBWAM_E116` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | High-pressure turbine |  |
| 15 | `FAYJBWAM_E117` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | Variable stator vanes |  |
| 16 | `FAYJBWAM_E118` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | Sensor |  |
| 17 | `FAYJBWAM_E119` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | Fan |  |
| 18 | `FAYJBWAM_E120` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | High-pressure turbine |  |
| 19 | `FAYJBWAM_E121` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | Variable stator vanes |  |
| 20 | `FAYJBWAM_E122` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | Sensor |  |
| 21 | `FAYJBWAM_E123` | `is collected on` | 11-Sensor Information | fuel flow sensor |  | 04-Fault Location | Fan |  |
| 22 | `FAYJBWAM_E124` | `is collected on` | 11-Sensor Information | fuel flow sensor |  | 04-Fault Location | High-pressure turbine |  |
| 23 | `FAYJBWAM_E125` | `is collected on` | 11-Sensor Information | fuel flow sensor |  | 04-Fault Location | Variable stator vanes |  |
| 24 | `FAYJBWAM_E126` | `is collected on` | 11-Sensor Information | fuel flow sensor |  | 04-Fault Location | Sensor |  |
| 25 | `FAYJBWAM_E127` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | Fan fault |  |
| 26 | `FAYJBWAM_E128` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | HPT fault |  |
| 27 | `FAYJBWAM_E129` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | Variable stator vanes fault |  |
| 28 | `FAYJBWAM_E130` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | Sensor fault |  |
| 29 | `FAYJBWAM_E131` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | Fan fault |  |
| 30 | `FAYJBWAM_E132` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | HPT fault |  |

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
