# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：YBJNUU4I
- **Paper Title**：Remote Monitoring and Fault Diagnosis of Ocean Current Energy Hydraulic Transmission and Control Power Generation System
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `YBJNUU4I`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "YBJNUU4I_E073", "edge_description": "Ocean current energy power generation contains hydraulic pump"},
    {"edge_id": "YBJNUU4I_E074", "edge_description": "Ocean current energy power generation contains hydraulic motor"},
    {"edge_id": "YBJNUU4I_E075", "edge_description": "Ocean current energy power generation contains relief valve"},
    {"edge_id": "YBJNUU4I_E076", "edge_description": "Ocean current energy power generation contains accumulator"},
    {"edge_id": "YBJNUU4I_E077", "edge_description": "hydraulic pump contains accumulator"},
    {"edge_id": "YBJNUU4I_E078", "edge_description": "hydraulic pump contains relief valve"},
    {"edge_id": "YBJNUU4I_E079", "edge_description": "hydraulic pump contains motor"},
    {"edge_id": "YBJNUU4I_E080", "edge_description": "hydraulic motor contains accumulator"},
    {"edge_id": "YBJNUU4I_E081", "edge_description": "hydraulic motor contains relief valve"},
    {"edge_id": "YBJNUU4I_E082", "edge_description": "hydraulic motor contains motor"},
    {"edge_id": "YBJNUU4I_E083", "edge_description": "relief valve contains accumulator"},
    {"edge_id": "YBJNUU4I_E084", "edge_description": "relief valve contains relief valve"},
    {"edge_id": "YBJNUU4I_E085", "edge_description": "relief valve contains motor"},
    {"edge_id": "YBJNUU4I_E086", "edge_description": "accumulator contains accumulator"},
    {"edge_id": "YBJNUU4I_E087", "edge_description": "accumulator contains relief valve"},
    {"edge_id": "YBJNUU4I_E088", "edge_description": "accumulator contains motor"},
    {"edge_id": "YBJNUU4I_E089", "edge_description": "hydraulic pump contains pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition"},
    {"edge_id": "YBJNUU4I_E090", "edge_description": "hydraulic motor contains pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition"},
    {"edge_id": "YBJNUU4I_E091", "edge_description": "relief valve contains pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition"},
    {"edge_id": "YBJNUU4I_E092", "edge_description": "accumulator contains pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition"},
    {"edge_id": "YBJNUU4I_E093", "edge_description": "accumulator failure contains No Compound Fault"},
    {"edge_id": "YBJNUU4I_E094", "edge_description": "relief valve failure contains No Compound Fault"},
    {"edge_id": "YBJNUU4I_E095", "edge_description": "motor failure contains No Compound Fault"},
    {"edge_id": "YBJNUU4I_E096", "edge_description": "GW636 model speed sensor is collected on accumulator"},
    {"edge_id": "YBJNUU4I_E097", "edge_description": "GW636 model speed sensor is collected on relief valve"},
    {"edge_id": "YBJNUU4I_E098", "edge_description": "GW636 model speed sensor is collected on motor"},
    {"edge_id": "YBJNUU4I_E099", "edge_description": "pressure sensor is collected on accumulator"},
    {"edge_id": "YBJNUU4I_E100", "edge_description": "pressure sensor is collected on relief valve"},
    {"edge_id": "YBJNUU4I_E101", "edge_description": "pressure sensor is collected on motor"},
    {"edge_id": "YBJNUU4I_E102", "edge_description": "temperature sensor is collected on accumulator"}
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
| 1 | `YBJNUU4I_E073` | `contains` | 01-Object Domain | Ocean current energy power generation(Industrial) |  | 02-Object Type | hydraulic pump |  |
| 2 | `YBJNUU4I_E074` | `contains` | 01-Object Domain | Ocean current energy power generation(Industrial) |  | 02-Object Type | hydraulic motor |  |
| 3 | `YBJNUU4I_E075` | `contains` | 01-Object Domain | Ocean current energy power generation(Industrial) |  | 02-Object Type | relief valve |  |
| 4 | `YBJNUU4I_E076` | `contains` | 01-Object Domain | Ocean current energy power generation(Industrial) |  | 02-Object Type | accumulator |  |
| 5 | `YBJNUU4I_E077` | `contains` | 02-Object Type | hydraulic pump |  | 04-Fault Location | accumulator |  |
| 6 | `YBJNUU4I_E078` | `contains` | 02-Object Type | hydraulic pump |  | 04-Fault Location | relief valve |  |
| 7 | `YBJNUU4I_E079` | `contains` | 02-Object Type | hydraulic pump |  | 04-Fault Location | motor |  |
| 8 | `YBJNUU4I_E080` | `contains` | 02-Object Type | hydraulic motor |  | 04-Fault Location | accumulator |  |
| 9 | `YBJNUU4I_E081` | `contains` | 02-Object Type | hydraulic motor |  | 04-Fault Location | relief valve |  |
| 10 | `YBJNUU4I_E082` | `contains` | 02-Object Type | hydraulic motor |  | 04-Fault Location | motor |  |
| 11 | `YBJNUU4I_E083` | `contains` | 02-Object Type | relief valve |  | 04-Fault Location | accumulator |  |
| 12 | `YBJNUU4I_E084` | `contains` | 02-Object Type | relief valve |  | 04-Fault Location | relief valve |  |
| 13 | `YBJNUU4I_E085` | `contains` | 02-Object Type | relief valve |  | 04-Fault Location | motor |  |
| 14 | `YBJNUU4I_E086` | `contains` | 02-Object Type | accumulator |  | 04-Fault Location | accumulator |  |
| 15 | `YBJNUU4I_E087` | `contains` | 02-Object Type | accumulator |  | 04-Fault Location | relief valve |  |
| 16 | `YBJNUU4I_E088` | `contains` | 02-Object Type | accumulator |  | 04-Fault Location | motor |  |
| 17 | `YBJNUU4I_E089` | `contains` | 02-Object Type | hydraulic pump |  | 03-Operating Conditions | pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition(Variable Conditions) |  |
| 18 | `YBJNUU4I_E090` | `contains` | 02-Object Type | hydraulic motor |  | 03-Operating Conditions | pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition(Variable Conditions) |  |
| 19 | `YBJNUU4I_E091` | `contains` | 02-Object Type | relief valve |  | 03-Operating Conditions | pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition(Variable Conditions) |  |
| 20 | `YBJNUU4I_E092` | `contains` | 02-Object Type | accumulator |  | 03-Operating Conditions | pump speed is set in the range of 30–60 r/min to simulate the actual sea current energy condition(Variable Conditions) |  |
| 21 | `YBJNUU4I_E093` | `contains` | 05-Fault Mode | accumulator failure |  | 07-Compound Fault | No Compound Fault |  |
| 22 | `YBJNUU4I_E094` | `contains` | 05-Fault Mode | relief valve failure |  | 07-Compound Fault | No Compound Fault |  |
| 23 | `YBJNUU4I_E095` | `contains` | 05-Fault Mode | motor failure |  | 07-Compound Fault | No Compound Fault |  |
| 24 | `YBJNUU4I_E096` | `is collected on` | 11-Sensor Information | GW636 model speed sensor |  | 04-Fault Location | accumulator |  |
| 25 | `YBJNUU4I_E097` | `is collected on` | 11-Sensor Information | GW636 model speed sensor |  | 04-Fault Location | relief valve |  |
| 26 | `YBJNUU4I_E098` | `is collected on` | 11-Sensor Information | GW636 model speed sensor |  | 04-Fault Location | motor |  |
| 27 | `YBJNUU4I_E099` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | accumulator |  |
| 28 | `YBJNUU4I_E100` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | relief valve |  |
| 29 | `YBJNUU4I_E101` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | motor |  |
| 30 | `YBJNUU4I_E102` | `is collected on` | 11-Sensor Information | temperature sensor |  | 04-Fault Location | accumulator |  |

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
