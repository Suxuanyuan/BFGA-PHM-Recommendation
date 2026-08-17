# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AILJECD7
- **Paper Title**：Fault template extraction to assist operators during industrial alarm floods
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AILJECD7`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AILJECD7_E173", "edge_description": "temperature sensor can obviously reflect broken"},
    {"edge_id": "AILJECD7_E174", "edge_description": "temperature sensor can obviously reflect sensor problem"},
    {"edge_id": "AILJECD7_E176", "edge_description": "bottles has_fault_mode leak"},
    {"edge_id": "AILJECD7_E177", "edge_description": "bottles has_fault_mode blockage"},
    {"edge_id": "AILJECD7_E178", "edge_description": "bottles has_fault_mode stoppage"},
    {"edge_id": "AILJECD7_E179", "edge_description": "bottles has_fault_mode broken"},
    {"edge_id": "AILJECD7_E180", "edge_description": "bottles has_fault_mode sensor problem"},
    {"edge_id": "AILJECD7_E181", "edge_description": "Buffer has_fault_mode leak"},
    {"edge_id": "AILJECD7_E182", "edge_description": "Buffer has_fault_mode blockage"},
    {"edge_id": "AILJECD7_E183", "edge_description": "Buffer has_fault_mode stoppage"},
    {"edge_id": "AILJECD7_E184", "edge_description": "Buffer has_fault_mode broken"},
    {"edge_id": "AILJECD7_E185", "edge_description": "Buffer has_fault_mode sensor problem"},
    {"edge_id": "AILJECD7_E186", "edge_description": "mass flow controllers has_fault_mode leak"},
    {"edge_id": "AILJECD7_E187", "edge_description": "mass flow controllers has_fault_mode blockage"},
    {"edge_id": "AILJECD7_E188", "edge_description": "mass flow controllers has_fault_mode stoppage"},
    {"edge_id": "AILJECD7_E189", "edge_description": "mass flow controllers has_fault_mode broken"},
    {"edge_id": "AILJECD7_E190", "edge_description": "mass flow controllers has_fault_mode sensor problem"},
    {"edge_id": "AILJECD7_E191", "edge_description": "pump has_fault_mode leak"},
    {"edge_id": "AILJECD7_E192", "edge_description": "pump has_fault_mode blockage"},
    {"edge_id": "AILJECD7_E193", "edge_description": "pump has_fault_mode stoppage"},
    {"edge_id": "AILJECD7_E194", "edge_description": "pump has_fault_mode broken"},
    {"edge_id": "AILJECD7_E195", "edge_description": "pump has_fault_mode sensor problem"},
    {"edge_id": "AILJECD7_E196", "edge_description": "bubblers has_fault_mode leak"},
    {"edge_id": "AILJECD7_E197", "edge_description": "bubblers has_fault_mode blockage"},
    {"edge_id": "AILJECD7_E198", "edge_description": "bubblers has_fault_mode stoppage"},
    {"edge_id": "AILJECD7_E199", "edge_description": "bubblers has_fault_mode broken"},
    {"edge_id": "AILJECD7_E200", "edge_description": "bubblers has_fault_mode sensor problem"},
    {"edge_id": "AILJECD7_E201", "edge_description": "sensor has_fault_mode leak"},
    {"edge_id": "AILJECD7_E202", "edge_description": "sensor has_fault_mode blockage"},
    {"edge_id": "AILJECD7_E203", "edge_description": "sensor has_fault_mode stoppage"}
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
| 1 | `AILJECD7_E173` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | broken |  |
| 2 | `AILJECD7_E174` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | sensor problem |  |
| 3 | `AILJECD7_E176` | `has_fault_mode` | 04-Fault Location | bottles |  | 05-Fault Mode | leak |  |
| 4 | `AILJECD7_E177` | `has_fault_mode` | 04-Fault Location | bottles |  | 05-Fault Mode | blockage |  |
| 5 | `AILJECD7_E178` | `has_fault_mode` | 04-Fault Location | bottles |  | 05-Fault Mode | stoppage |  |
| 6 | `AILJECD7_E179` | `has_fault_mode` | 04-Fault Location | bottles |  | 05-Fault Mode | broken |  |
| 7 | `AILJECD7_E180` | `has_fault_mode` | 04-Fault Location | bottles |  | 05-Fault Mode | sensor problem |  |
| 8 | `AILJECD7_E181` | `has_fault_mode` | 04-Fault Location | Buffer |  | 05-Fault Mode | leak |  |
| 9 | `AILJECD7_E182` | `has_fault_mode` | 04-Fault Location | Buffer |  | 05-Fault Mode | blockage |  |
| 10 | `AILJECD7_E183` | `has_fault_mode` | 04-Fault Location | Buffer |  | 05-Fault Mode | stoppage |  |
| 11 | `AILJECD7_E184` | `has_fault_mode` | 04-Fault Location | Buffer |  | 05-Fault Mode | broken |  |
| 12 | `AILJECD7_E185` | `has_fault_mode` | 04-Fault Location | Buffer |  | 05-Fault Mode | sensor problem |  |
| 13 | `AILJECD7_E186` | `has_fault_mode` | 04-Fault Location | mass flow controllers |  | 05-Fault Mode | leak |  |
| 14 | `AILJECD7_E187` | `has_fault_mode` | 04-Fault Location | mass flow controllers |  | 05-Fault Mode | blockage |  |
| 15 | `AILJECD7_E188` | `has_fault_mode` | 04-Fault Location | mass flow controllers |  | 05-Fault Mode | stoppage |  |
| 16 | `AILJECD7_E189` | `has_fault_mode` | 04-Fault Location | mass flow controllers |  | 05-Fault Mode | broken |  |
| 17 | `AILJECD7_E190` | `has_fault_mode` | 04-Fault Location | mass flow controllers |  | 05-Fault Mode | sensor problem |  |
| 18 | `AILJECD7_E191` | `has_fault_mode` | 04-Fault Location | pump |  | 05-Fault Mode | leak |  |
| 19 | `AILJECD7_E192` | `has_fault_mode` | 04-Fault Location | pump |  | 05-Fault Mode | blockage |  |
| 20 | `AILJECD7_E193` | `has_fault_mode` | 04-Fault Location | pump |  | 05-Fault Mode | stoppage |  |
| 21 | `AILJECD7_E194` | `has_fault_mode` | 04-Fault Location | pump |  | 05-Fault Mode | broken |  |
| 22 | `AILJECD7_E195` | `has_fault_mode` | 04-Fault Location | pump |  | 05-Fault Mode | sensor problem |  |
| 23 | `AILJECD7_E196` | `has_fault_mode` | 04-Fault Location | bubblers |  | 05-Fault Mode | leak |  |
| 24 | `AILJECD7_E197` | `has_fault_mode` | 04-Fault Location | bubblers |  | 05-Fault Mode | blockage |  |
| 25 | `AILJECD7_E198` | `has_fault_mode` | 04-Fault Location | bubblers |  | 05-Fault Mode | stoppage |  |
| 26 | `AILJECD7_E199` | `has_fault_mode` | 04-Fault Location | bubblers |  | 05-Fault Mode | broken |  |
| 27 | `AILJECD7_E200` | `has_fault_mode` | 04-Fault Location | bubblers |  | 05-Fault Mode | sensor problem |  |
| 28 | `AILJECD7_E201` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | leak |  |
| 29 | `AILJECD7_E202` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | blockage |  |
| 30 | `AILJECD7_E203` | `has_fault_mode` | 04-Fault Location | sensor |  | 05-Fault Mode | stoppage |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
