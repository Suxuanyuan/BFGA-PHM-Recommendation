# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：8TA9ZRKQ
- **Paper Title**：An Advanced PLS Approach for Key Performance Indicator-Related Prediction and Diagnosis in Case of Outliers
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `8TA9ZRKQ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "8TA9ZRKQ_E098", "edge_description": "chemical production process contains reactor"},
    {"edge_id": "8TA9ZRKQ_E099", "edge_description": "chemical production process contains condenser"},
    {"edge_id": "8TA9ZRKQ_E100", "edge_description": "chemical production process contains vapor-liquid separator"},
    {"edge_id": "8TA9ZRKQ_E101", "edge_description": "chemical production process contains compressor"},
    {"edge_id": "8TA9ZRKQ_E102", "edge_description": "chemical production process contains stripper"},
    {"edge_id": "8TA9ZRKQ_E104", "edge_description": "step change contains No Compound Fault"},
    {"edge_id": "8TA9ZRKQ_E105", "edge_description": "drift contains No Compound Fault"},
    {"edge_id": "8TA9ZRKQ_E106", "edge_description": "random variation contains No Compound Fault"},
    {"edge_id": "8TA9ZRKQ_E107", "edge_description": "flow sensor is collected on reactor"},
    {"edge_id": "8TA9ZRKQ_E108", "edge_description": "flow sensor is collected on condenser"},
    {"edge_id": "8TA9ZRKQ_E109", "edge_description": "flow sensor is collected on vapor-liquid separator"},
    {"edge_id": "8TA9ZRKQ_E110", "edge_description": "flow sensor is collected on compressor"},
    {"edge_id": "8TA9ZRKQ_E111", "edge_description": "flow sensor is collected on stripper"},
    {"edge_id": "8TA9ZRKQ_E112", "edge_description": "pressure sensor is collected on reactor"},
    {"edge_id": "8TA9ZRKQ_E113", "edge_description": "pressure sensor is collected on condenser"},
    {"edge_id": "8TA9ZRKQ_E114", "edge_description": "pressure sensor is collected on vapor-liquid separator"},
    {"edge_id": "8TA9ZRKQ_E115", "edge_description": "pressure sensor is collected on compressor"},
    {"edge_id": "8TA9ZRKQ_E116", "edge_description": "pressure sensor is collected on stripper"},
    {"edge_id": "8TA9ZRKQ_E117", "edge_description": "temperature sensor is collected on reactor"},
    {"edge_id": "8TA9ZRKQ_E118", "edge_description": "temperature sensor is collected on condenser"},
    {"edge_id": "8TA9ZRKQ_E119", "edge_description": "temperature sensor is collected on vapor-liquid separator"},
    {"edge_id": "8TA9ZRKQ_E120", "edge_description": "temperature sensor is collected on compressor"},
    {"edge_id": "8TA9ZRKQ_E121", "edge_description": "temperature sensor is collected on stripper"},
    {"edge_id": "8TA9ZRKQ_E122", "edge_description": "level sensor is collected on reactor"},
    {"edge_id": "8TA9ZRKQ_E123", "edge_description": "level sensor is collected on condenser"},
    {"edge_id": "8TA9ZRKQ_E124", "edge_description": "level sensor is collected on vapor-liquid separator"},
    {"edge_id": "8TA9ZRKQ_E125", "edge_description": "level sensor is collected on compressor"},
    {"edge_id": "8TA9ZRKQ_E126", "edge_description": "level sensor is collected on stripper"},
    {"edge_id": "8TA9ZRKQ_E127", "edge_description": "analyzer is collected on reactor"},
    {"edge_id": "8TA9ZRKQ_E128", "edge_description": "analyzer is collected on condenser"}
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
| 1 | `8TA9ZRKQ_E098` | `contains` | 02-Object Type | chemical production process |  | 04-Fault Location | reactor |  |
| 2 | `8TA9ZRKQ_E099` | `contains` | 02-Object Type | chemical production process |  | 04-Fault Location | condenser |  |
| 3 | `8TA9ZRKQ_E100` | `contains` | 02-Object Type | chemical production process |  | 04-Fault Location | vapor-liquid separator |  |
| 4 | `8TA9ZRKQ_E101` | `contains` | 02-Object Type | chemical production process |  | 04-Fault Location | compressor |  |
| 5 | `8TA9ZRKQ_E102` | `contains` | 02-Object Type | chemical production process |  | 04-Fault Location | stripper |  |
| 6 | `8TA9ZRKQ_E104` | `contains` | 05-Fault Mode | step change |  | 07-Compound Fault | No Compound Fault |  |
| 7 | `8TA9ZRKQ_E105` | `contains` | 05-Fault Mode | drift |  | 07-Compound Fault | No Compound Fault |  |
| 8 | `8TA9ZRKQ_E106` | `contains` | 05-Fault Mode | random variation |  | 07-Compound Fault | No Compound Fault |  |
| 9 | `8TA9ZRKQ_E107` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | reactor |  |
| 10 | `8TA9ZRKQ_E108` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | condenser |  |
| 11 | `8TA9ZRKQ_E109` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | vapor-liquid separator |  |
| 12 | `8TA9ZRKQ_E110` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | compressor |  |
| 13 | `8TA9ZRKQ_E111` | `is collected on` | 11-Sensor Information | flow sensor |  | 04-Fault Location | stripper |  |
| 14 | `8TA9ZRKQ_E112` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | reactor |  |
| 15 | `8TA9ZRKQ_E113` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | condenser |  |
| 16 | `8TA9ZRKQ_E114` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | vapor-liquid separator |  |
| 17 | `8TA9ZRKQ_E115` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | compressor |  |
| 18 | `8TA9ZRKQ_E116` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | stripper |  |
| 19 | `8TA9ZRKQ_E117` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | reactor |  |
| 20 | `8TA9ZRKQ_E118` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | condenser |  |
| 21 | `8TA9ZRKQ_E119` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | vapor-liquid separator |  |
| 22 | `8TA9ZRKQ_E120` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | compressor |  |
| 23 | `8TA9ZRKQ_E121` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | stripper |  |
| 24 | `8TA9ZRKQ_E122` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | reactor |  |
| 25 | `8TA9ZRKQ_E123` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | condenser |  |
| 26 | `8TA9ZRKQ_E124` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | vapor-liquid separator |  |
| 27 | `8TA9ZRKQ_E125` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | compressor |  |
| 28 | `8TA9ZRKQ_E126` | `is collected on` | 11-Sensor Information | level sensor |  | 04-Fault Location | stripper |  |
| 29 | `8TA9ZRKQ_E127` | `is collected on` | 11-Sensor Information | analyzer |  | 04-Fault Location | reactor |  |
| 30 | `8TA9ZRKQ_E128` | `is collected on` | 11-Sensor Information | analyzer |  | 04-Fault Location | condenser |  |

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
