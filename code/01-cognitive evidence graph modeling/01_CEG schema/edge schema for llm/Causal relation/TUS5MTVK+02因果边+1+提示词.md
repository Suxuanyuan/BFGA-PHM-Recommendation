# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：TUS5MTVK
- **Paper Title**：A Performance Evaluation of Two Bispectrum Analysis Methods Applied to Electrical Current Signals for Monitoring Induction Motor-Driven Systems
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `TUS5MTVK`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "TUS5MTVK_E085", "edge_description": "industrial motor-driven systems contains induction motor"},
    {"edge_id": "TUS5MTVK_E086", "edge_description": "industrial motor-driven systems contains gearbox"},
    {"edge_id": "TUS5MTVK_E087", "edge_description": "industrial motor-driven systems contains reciprocating compressor"},
    {"edge_id": "TUS5MTVK_E088", "edge_description": "induction motor contains rotor bar"},
    {"edge_id": "TUS5MTVK_E089", "edge_description": "induction motor contains gear"},
    {"edge_id": "TUS5MTVK_E090", "edge_description": "induction motor contains discharge valve"},
    {"edge_id": "TUS5MTVK_E091", "edge_description": "induction motor contains transmission belt"},
    {"edge_id": "TUS5MTVK_E092", "edge_description": "induction motor contains intercooler"},
    {"edge_id": "TUS5MTVK_E093", "edge_description": "gearbox contains rotor bar"},
    {"edge_id": "TUS5MTVK_E094", "edge_description": "gearbox contains gear"},
    {"edge_id": "TUS5MTVK_E095", "edge_description": "gearbox contains discharge valve"},
    {"edge_id": "TUS5MTVK_E096", "edge_description": "gearbox contains transmission belt"},
    {"edge_id": "TUS5MTVK_E097", "edge_description": "gearbox contains intercooler"},
    {"edge_id": "TUS5MTVK_E098", "edge_description": "reciprocating compressor contains rotor bar"},
    {"edge_id": "TUS5MTVK_E099", "edge_description": "reciprocating compressor contains gear"},
    {"edge_id": "TUS5MTVK_E100", "edge_description": "reciprocating compressor contains discharge valve"},
    {"edge_id": "TUS5MTVK_E101", "edge_description": "reciprocating compressor contains transmission belt"},
    {"edge_id": "TUS5MTVK_E102", "edge_description": "reciprocating compressor contains intercooler"},
    {"edge_id": "TUS5MTVK_E103", "edge_description": "induction motor contains steady conditions"},
    {"edge_id": "TUS5MTVK_E104", "edge_description": "gearbox contains steady conditions"},
    {"edge_id": "TUS5MTVK_E105", "edge_description": "reciprocating compressor contains steady conditions"},
    {"edge_id": "TUS5MTVK_E106", "edge_description": "broken rotor bar contains No Compound Fault"},
    {"edge_id": "TUS5MTVK_E107", "edge_description": "gear wear contains No Compound Fault"},
    {"edge_id": "TUS5MTVK_E108", "edge_description": "discharge valve leakage contains No Compound Fault"},
    {"edge_id": "TUS5MTVK_E109", "edge_description": "transmission belt looseness contains No Compound Fault"},
    {"edge_id": "TUS5MTVK_E110", "edge_description": "intercooler leakage contains No Compound Fault"},
    {"edge_id": "TUS5MTVK_E111", "edge_description": "current sensor is collected on rotor bar"},
    {"edge_id": "TUS5MTVK_E112", "edge_description": "current sensor is collected on gear"},
    {"edge_id": "TUS5MTVK_E113", "edge_description": "current sensor is collected on discharge valve"},
    {"edge_id": "TUS5MTVK_E114", "edge_description": "current sensor is collected on transmission belt"}
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
| 1 | `TUS5MTVK_E085` | `contains` | 01-Object Domain | industrial motor-driven systems(Industrial) |  | 02-Object Type | induction motor |  |
| 2 | `TUS5MTVK_E086` | `contains` | 01-Object Domain | industrial motor-driven systems(Industrial) |  | 02-Object Type | gearbox |  |
| 3 | `TUS5MTVK_E087` | `contains` | 01-Object Domain | industrial motor-driven systems(Industrial) |  | 02-Object Type | reciprocating compressor |  |
| 4 | `TUS5MTVK_E088` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | rotor bar |  |
| 5 | `TUS5MTVK_E089` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | gear |  |
| 6 | `TUS5MTVK_E090` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | discharge valve |  |
| 7 | `TUS5MTVK_E091` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | transmission belt |  |
| 8 | `TUS5MTVK_E092` | `contains` | 02-Object Type | induction motor |  | 04-Fault Location | intercooler |  |
| 9 | `TUS5MTVK_E093` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | rotor bar |  |
| 10 | `TUS5MTVK_E094` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | gear |  |
| 11 | `TUS5MTVK_E095` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | discharge valve |  |
| 12 | `TUS5MTVK_E096` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | transmission belt |  |
| 13 | `TUS5MTVK_E097` | `contains` | 02-Object Type | gearbox |  | 04-Fault Location | intercooler |  |
| 14 | `TUS5MTVK_E098` | `contains` | 02-Object Type | reciprocating compressor |  | 04-Fault Location | rotor bar |  |
| 15 | `TUS5MTVK_E099` | `contains` | 02-Object Type | reciprocating compressor |  | 04-Fault Location | gear |  |
| 16 | `TUS5MTVK_E100` | `contains` | 02-Object Type | reciprocating compressor |  | 04-Fault Location | discharge valve |  |
| 17 | `TUS5MTVK_E101` | `contains` | 02-Object Type | reciprocating compressor |  | 04-Fault Location | transmission belt |  |
| 18 | `TUS5MTVK_E102` | `contains` | 02-Object Type | reciprocating compressor |  | 04-Fault Location | intercooler |  |
| 19 | `TUS5MTVK_E103` | `contains` | 02-Object Type | induction motor |  | 03-Operating Conditions | steady conditions(Single Condition) |  |
| 20 | `TUS5MTVK_E104` | `contains` | 02-Object Type | gearbox |  | 03-Operating Conditions | steady conditions(Single Condition) |  |
| 21 | `TUS5MTVK_E105` | `contains` | 02-Object Type | reciprocating compressor |  | 03-Operating Conditions | steady conditions(Single Condition) |  |
| 22 | `TUS5MTVK_E106` | `contains` | 05-Fault Mode | broken rotor bar |  | 07-Compound Fault | No Compound Fault |  |
| 23 | `TUS5MTVK_E107` | `contains` | 05-Fault Mode | gear wear |  | 07-Compound Fault | No Compound Fault |  |
| 24 | `TUS5MTVK_E108` | `contains` | 05-Fault Mode | discharge valve leakage |  | 07-Compound Fault | No Compound Fault |  |
| 25 | `TUS5MTVK_E109` | `contains` | 05-Fault Mode | transmission belt looseness |  | 07-Compound Fault | No Compound Fault |  |
| 26 | `TUS5MTVK_E110` | `contains` | 05-Fault Mode | intercooler leakage |  | 07-Compound Fault | No Compound Fault |  |
| 27 | `TUS5MTVK_E111` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | rotor bar |  |
| 28 | `TUS5MTVK_E112` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | gear |  |
| 29 | `TUS5MTVK_E113` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | discharge valve |  |
| 30 | `TUS5MTVK_E114` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | transmission belt |  |

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
