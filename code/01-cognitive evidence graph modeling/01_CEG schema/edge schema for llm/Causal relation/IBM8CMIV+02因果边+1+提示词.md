# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：IBM8CMIV
- **Paper Title**：Evolving Deep Echo State Networks for Intelligent Fault Diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `IBM8CMIV`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "IBM8CMIV_E129", "edge_description": "3D printer, wind turbine gearbox contains joint bearing"},
    {"edge_id": "IBM8CMIV_E130", "edge_description": "3D printer, wind turbine gearbox contains synchronous belt"},
    {"edge_id": "IBM8CMIV_E131", "edge_description": "3D printer, wind turbine gearbox contains gearbox (sun gear)"},
    {"edge_id": "IBM8CMIV_E132", "edge_description": "joint bearing contains joint bearing"},
    {"edge_id": "IBM8CMIV_E133", "edge_description": "joint bearing contains synchronous belt"},
    {"edge_id": "IBM8CMIV_E134", "edge_description": "joint bearing contains sun gear"},
    {"edge_id": "IBM8CMIV_E135", "edge_description": "synchronous belt contains joint bearing"},
    {"edge_id": "IBM8CMIV_E136", "edge_description": "synchronous belt contains synchronous belt"},
    {"edge_id": "IBM8CMIV_E137", "edge_description": "synchronous belt contains sun gear"},
    {"edge_id": "IBM8CMIV_E138", "edge_description": "gearbox (sun gear) contains joint bearing"},
    {"edge_id": "IBM8CMIV_E139", "edge_description": "gearbox (sun gear) contains synchronous belt"},
    {"edge_id": "IBM8CMIV_E140", "edge_description": "gearbox (sun gear) contains sun gear"},
    {"edge_id": "IBM8CMIV_E141", "edge_description": "joint bearing contains single operating condition"},
    {"edge_id": "IBM8CMIV_E142", "edge_description": "synchronous belt contains single operating condition"},
    {"edge_id": "IBM8CMIV_E143", "edge_description": "gearbox (sun gear) contains single operating condition"},
    {"edge_id": "IBM8CMIV_E144", "edge_description": "clearance contains single-point pitting + half broken tooth"},
    {"edge_id": "IBM8CMIV_E145", "edge_description": "slackness contains single-point pitting + half broken tooth"},
    {"edge_id": "IBM8CMIV_E146", "edge_description": "pitting contains single-point pitting + half broken tooth"},
    {"edge_id": "IBM8CMIV_E147", "edge_description": "broken tooth contains single-point pitting + half broken tooth"},
    {"edge_id": "IBM8CMIV_E148", "edge_description": "groove contains single-point pitting + half broken tooth"},
    {"edge_id": "IBM8CMIV_E149", "edge_description": "attitude sensor (BWT901), triaxial accelerometer sensor is collected on joint bearing"},
    {"edge_id": "IBM8CMIV_E150", "edge_description": "attitude sensor (BWT901), triaxial accelerometer sensor is collected on synchronous belt"},
    {"edge_id": "IBM8CMIV_E151", "edge_description": "attitude sensor (BWT901), triaxial accelerometer sensor is collected on sun gear"},
    {"edge_id": "IBM8CMIV_E152", "edge_description": "attitude sensor (BWT901) is collected on joint bearing"},
    {"edge_id": "IBM8CMIV_E153", "edge_description": "attitude sensor (BWT901) is collected on synchronous belt"},
    {"edge_id": "IBM8CMIV_E154", "edge_description": "attitude sensor (BWT901) is collected on sun gear"},
    {"edge_id": "IBM8CMIV_E155", "edge_description": "attitude sensor (BWT901) is collected on joint bearing"},
    {"edge_id": "IBM8CMIV_E156", "edge_description": "attitude sensor (BWT901) is collected on synchronous belt"},
    {"edge_id": "IBM8CMIV_E157", "edge_description": "attitude sensor (BWT901) is collected on sun gear"},
    {"edge_id": "IBM8CMIV_E158", "edge_description": "three-phase current sensor is collected on joint bearing"}
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
| 1 | `IBM8CMIV_E129` | `contains` | 01-Object Domain | 3D printer, wind turbine gearbox(Industrial) |  | 02-Object Type | joint bearing |  |
| 2 | `IBM8CMIV_E130` | `contains` | 01-Object Domain | 3D printer, wind turbine gearbox(Industrial) |  | 02-Object Type | synchronous belt |  |
| 3 | `IBM8CMIV_E131` | `contains` | 01-Object Domain | 3D printer, wind turbine gearbox(Industrial) |  | 02-Object Type | gearbox (sun gear) |  |
| 4 | `IBM8CMIV_E132` | `contains` | 02-Object Type | joint bearing |  | 04-Fault Location | joint bearing |  |
| 5 | `IBM8CMIV_E133` | `contains` | 02-Object Type | joint bearing |  | 04-Fault Location | synchronous belt |  |
| 6 | `IBM8CMIV_E134` | `contains` | 02-Object Type | joint bearing |  | 04-Fault Location | sun gear |  |
| 7 | `IBM8CMIV_E135` | `contains` | 02-Object Type | synchronous belt |  | 04-Fault Location | joint bearing |  |
| 8 | `IBM8CMIV_E136` | `contains` | 02-Object Type | synchronous belt |  | 04-Fault Location | synchronous belt |  |
| 9 | `IBM8CMIV_E137` | `contains` | 02-Object Type | synchronous belt |  | 04-Fault Location | sun gear |  |
| 10 | `IBM8CMIV_E138` | `contains` | 02-Object Type | gearbox (sun gear) |  | 04-Fault Location | joint bearing |  |
| 11 | `IBM8CMIV_E139` | `contains` | 02-Object Type | gearbox (sun gear) |  | 04-Fault Location | synchronous belt |  |
| 12 | `IBM8CMIV_E140` | `contains` | 02-Object Type | gearbox (sun gear) |  | 04-Fault Location | sun gear |  |
| 13 | `IBM8CMIV_E141` | `contains` | 02-Object Type | joint bearing |  | 03-Operating Conditions | single operating condition(Single Condition) |  |
| 14 | `IBM8CMIV_E142` | `contains` | 02-Object Type | synchronous belt |  | 03-Operating Conditions | single operating condition(Single Condition) |  |
| 15 | `IBM8CMIV_E143` | `contains` | 02-Object Type | gearbox (sun gear) |  | 03-Operating Conditions | single operating condition(Single Condition) |  |
| 16 | `IBM8CMIV_E144` | `contains` | 05-Fault Mode | clearance |  | 07-Compound Fault | single-point pitting + half broken tooth(Compound Fault Within Same Structure) |  |
| 17 | `IBM8CMIV_E145` | `contains` | 05-Fault Mode | slackness |  | 07-Compound Fault | single-point pitting + half broken tooth(Compound Fault Within Same Structure) |  |
| 18 | `IBM8CMIV_E146` | `contains` | 05-Fault Mode | pitting |  | 07-Compound Fault | single-point pitting + half broken tooth(Compound Fault Within Same Structure) |  |
| 19 | `IBM8CMIV_E147` | `contains` | 05-Fault Mode | broken tooth |  | 07-Compound Fault | single-point pitting + half broken tooth(Compound Fault Within Same Structure) |  |
| 20 | `IBM8CMIV_E148` | `contains` | 05-Fault Mode | groove |  | 07-Compound Fault | single-point pitting + half broken tooth(Compound Fault Within Same Structure) |  |
| 21 | `IBM8CMIV_E149` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901), triaxial accelerometer sensor |  | 04-Fault Location | joint bearing |  |
| 22 | `IBM8CMIV_E150` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901), triaxial accelerometer sensor |  | 04-Fault Location | synchronous belt |  |
| 23 | `IBM8CMIV_E151` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901), triaxial accelerometer sensor |  | 04-Fault Location | sun gear |  |
| 24 | `IBM8CMIV_E152` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901) |  | 04-Fault Location | joint bearing |  |
| 25 | `IBM8CMIV_E153` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901) |  | 04-Fault Location | synchronous belt |  |
| 26 | `IBM8CMIV_E154` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901) |  | 04-Fault Location | sun gear |  |
| 27 | `IBM8CMIV_E155` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901) |  | 04-Fault Location | joint bearing |  |
| 28 | `IBM8CMIV_E156` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901) |  | 04-Fault Location | synchronous belt |  |
| 29 | `IBM8CMIV_E157` | `is collected on` | 11-Sensor Information | attitude sensor (BWT901) |  | 04-Fault Location | sun gear |  |
| 30 | `IBM8CMIV_E158` | `is collected on` | 11-Sensor Information | three-phase current sensor |  | 04-Fault Location | joint bearing |  |

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
