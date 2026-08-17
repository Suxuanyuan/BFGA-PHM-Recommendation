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
    {"edge_id": "IBM8CMIV_E189", "edge_description": "acoustic sensor can obviously reflect pitting"},
    {"edge_id": "IBM8CMIV_E190", "edge_description": "acoustic sensor can obviously reflect broken tooth"},
    {"edge_id": "IBM8CMIV_E191", "edge_description": "acoustic sensor can obviously reflect groove"},
    {"edge_id": "IBM8CMIV_E192", "edge_description": "acoustic emission sensor can obviously reflect clearance"},
    {"edge_id": "IBM8CMIV_E193", "edge_description": "acoustic emission sensor can obviously reflect slackness"},
    {"edge_id": "IBM8CMIV_E194", "edge_description": "acoustic emission sensor can obviously reflect pitting"},
    {"edge_id": "IBM8CMIV_E195", "edge_description": "acoustic emission sensor can obviously reflect broken tooth"},
    {"edge_id": "IBM8CMIV_E196", "edge_description": "acoustic emission sensor can obviously reflect groove"},
    {"edge_id": "IBM8CMIV_E197", "edge_description": "3D Dataset_1 can be used for fault diagnosis"},
    {"edge_id": "IBM8CMIV_E198", "edge_description": "3D Dataset_2 can be used for fault diagnosis"},
    {"edge_id": "IBM8CMIV_E199", "edge_description": "WT Dataset_1 can be used for fault diagnosis"},
    {"edge_id": "IBM8CMIV_E200", "edge_description": "WT Dataset_2 can be used for fault diagnosis"},
    {"edge_id": "IBM8CMIV_E201", "edge_description": "joint bearing has_fault_mode clearance"},
    {"edge_id": "IBM8CMIV_E202", "edge_description": "joint bearing has_fault_mode slackness"},
    {"edge_id": "IBM8CMIV_E203", "edge_description": "joint bearing has_fault_mode pitting"},
    {"edge_id": "IBM8CMIV_E204", "edge_description": "joint bearing has_fault_mode broken tooth"},
    {"edge_id": "IBM8CMIV_E205", "edge_description": "joint bearing has_fault_mode groove"},
    {"edge_id": "IBM8CMIV_E206", "edge_description": "synchronous belt has_fault_mode clearance"},
    {"edge_id": "IBM8CMIV_E207", "edge_description": "synchronous belt has_fault_mode slackness"},
    {"edge_id": "IBM8CMIV_E208", "edge_description": "synchronous belt has_fault_mode pitting"},
    {"edge_id": "IBM8CMIV_E209", "edge_description": "synchronous belt has_fault_mode broken tooth"},
    {"edge_id": "IBM8CMIV_E210", "edge_description": "synchronous belt has_fault_mode groove"},
    {"edge_id": "IBM8CMIV_E211", "edge_description": "sun gear has_fault_mode clearance"},
    {"edge_id": "IBM8CMIV_E212", "edge_description": "sun gear has_fault_mode slackness"},
    {"edge_id": "IBM8CMIV_E213", "edge_description": "sun gear has_fault_mode pitting"},
    {"edge_id": "IBM8CMIV_E214", "edge_description": "sun gear has_fault_mode broken tooth"},
    {"edge_id": "IBM8CMIV_E215", "edge_description": "sun gear has_fault_mode groove"},
    {"edge_id": "IBM8CMIV_E216", "edge_description": "clearance contains 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth"},
    {"edge_id": "IBM8CMIV_E217", "edge_description": "slackness contains 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth"},
    {"edge_id": "IBM8CMIV_E218", "edge_description": "pitting contains 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth"}
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
| 1 | `IBM8CMIV_E189` | `can obviously reflect` | 11-Sensor Information | acoustic sensor |  | 05-Fault Mode | pitting |  |
| 2 | `IBM8CMIV_E190` | `can obviously reflect` | 11-Sensor Information | acoustic sensor |  | 05-Fault Mode | broken tooth |  |
| 3 | `IBM8CMIV_E191` | `can obviously reflect` | 11-Sensor Information | acoustic sensor |  | 05-Fault Mode | groove |  |
| 4 | `IBM8CMIV_E192` | `can obviously reflect` | 11-Sensor Information | acoustic emission sensor |  | 05-Fault Mode | clearance |  |
| 5 | `IBM8CMIV_E193` | `can obviously reflect` | 11-Sensor Information | acoustic emission sensor |  | 05-Fault Mode | slackness |  |
| 6 | `IBM8CMIV_E194` | `can obviously reflect` | 11-Sensor Information | acoustic emission sensor |  | 05-Fault Mode | pitting |  |
| 7 | `IBM8CMIV_E195` | `can obviously reflect` | 11-Sensor Information | acoustic emission sensor |  | 05-Fault Mode | broken tooth |  |
| 8 | `IBM8CMIV_E196` | `can obviously reflect` | 11-Sensor Information | acoustic emission sensor |  | 05-Fault Mode | groove |  |
| 9 | `IBM8CMIV_E197` | `can be used for` | 10-Dataset | 3D Dataset_1 |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `IBM8CMIV_E198` | `can be used for` | 10-Dataset | 3D Dataset_2 |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `IBM8CMIV_E199` | `can be used for` | 10-Dataset | WT Dataset_1 |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `IBM8CMIV_E200` | `can be used for` | 10-Dataset | WT Dataset_2 |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `IBM8CMIV_E201` | `has_fault_mode` | 04-Fault Location | joint bearing |  | 05-Fault Mode | clearance |  |
| 14 | `IBM8CMIV_E202` | `has_fault_mode` | 04-Fault Location | joint bearing |  | 05-Fault Mode | slackness |  |
| 15 | `IBM8CMIV_E203` | `has_fault_mode` | 04-Fault Location | joint bearing |  | 05-Fault Mode | pitting |  |
| 16 | `IBM8CMIV_E204` | `has_fault_mode` | 04-Fault Location | joint bearing |  | 05-Fault Mode | broken tooth |  |
| 17 | `IBM8CMIV_E205` | `has_fault_mode` | 04-Fault Location | joint bearing |  | 05-Fault Mode | groove |  |
| 18 | `IBM8CMIV_E206` | `has_fault_mode` | 04-Fault Location | synchronous belt |  | 05-Fault Mode | clearance |  |
| 19 | `IBM8CMIV_E207` | `has_fault_mode` | 04-Fault Location | synchronous belt |  | 05-Fault Mode | slackness |  |
| 20 | `IBM8CMIV_E208` | `has_fault_mode` | 04-Fault Location | synchronous belt |  | 05-Fault Mode | pitting |  |
| 21 | `IBM8CMIV_E209` | `has_fault_mode` | 04-Fault Location | synchronous belt |  | 05-Fault Mode | broken tooth |  |
| 22 | `IBM8CMIV_E210` | `has_fault_mode` | 04-Fault Location | synchronous belt |  | 05-Fault Mode | groove |  |
| 23 | `IBM8CMIV_E211` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | clearance |  |
| 24 | `IBM8CMIV_E212` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | slackness |  |
| 25 | `IBM8CMIV_E213` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | pitting |  |
| 26 | `IBM8CMIV_E214` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | broken tooth |  |
| 27 | `IBM8CMIV_E215` | `has_fault_mode` | 04-Fault Location | sun gear |  | 05-Fault Mode | groove |  |
| 28 | `IBM8CMIV_E216` | `contains` | 05-Fault Mode | clearance |  | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  |
| 29 | `IBM8CMIV_E217` | `contains` | 05-Fault Mode | slackness |  | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  |
| 30 | `IBM8CMIV_E218` | `contains` | 05-Fault Mode | pitting |  | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  |

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

### ▶ For `can be used for` (Dataset type → PHM Task type)

**High Standard**: The paper must explicitly express that the dataset is an **input at the methodological level**, rather than merely a background for experimental evaluation.
Merely mentioning "using a dataset to evaluate model performance" is insufficient — the methodological association between dataset and task must be reflected (e.g., "selecting a dataset for a specific task")
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the methodological relation of the dataset serving a certain PHM task, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
