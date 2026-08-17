# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：CBAZUCRE
- **Paper Title**：Multi-Physics Graphical Model-Based Fault Detection and Isolation in Wind Turbines
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `CBAZUCRE`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "CBAZUCRE_E121", "edge_description": "current sensor can obviously reflect inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E122", "edge_description": "current sensor can obviously reflect open circuit fault"},
    {"edge_id": "CBAZUCRE_E123", "edge_description": "current sensor can obviously reflect short circuit fault"},
    {"edge_id": "CBAZUCRE_E124", "edge_description": "current sensor can obviously reflect capacitance reduction"},
    {"edge_id": "CBAZUCRE_E125", "edge_description": "current sensor can obviously reflect pressure drop"},
    {"edge_id": "CBAZUCRE_E126", "edge_description": "current sensor can obviously reflect broken tooth"},
    {"edge_id": "CBAZUCRE_E127", "edge_description": "speed sensor can obviously reflect inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E128", "edge_description": "speed sensor can obviously reflect open circuit fault"},
    {"edge_id": "CBAZUCRE_E129", "edge_description": "speed sensor can obviously reflect short circuit fault"},
    {"edge_id": "CBAZUCRE_E130", "edge_description": "speed sensor can obviously reflect capacitance reduction"},
    {"edge_id": "CBAZUCRE_E131", "edge_description": "speed sensor can obviously reflect pressure drop"},
    {"edge_id": "CBAZUCRE_E132", "edge_description": "speed sensor can obviously reflect broken tooth"},
    {"edge_id": "CBAZUCRE_E133", "edge_description": "anemometer can obviously reflect inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E134", "edge_description": "anemometer can obviously reflect open circuit fault"},
    {"edge_id": "CBAZUCRE_E135", "edge_description": "anemometer can obviously reflect short circuit fault"},
    {"edge_id": "CBAZUCRE_E136", "edge_description": "anemometer can obviously reflect capacitance reduction"},
    {"edge_id": "CBAZUCRE_E137", "edge_description": "anemometer can obviously reflect pressure drop"},
    {"edge_id": "CBAZUCRE_E138", "edge_description": "anemometer can obviously reflect broken tooth"},
    {"edge_id": "CBAZUCRE_E140", "edge_description": "rotor windings has_fault_mode inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E141", "edge_description": "rotor windings has_fault_mode open circuit fault"},
    {"edge_id": "CBAZUCRE_E142", "edge_description": "rotor windings has_fault_mode short circuit fault"},
    {"edge_id": "CBAZUCRE_E143", "edge_description": "rotor windings has_fault_mode capacitance reduction"},
    {"edge_id": "CBAZUCRE_E144", "edge_description": "rotor windings has_fault_mode pressure drop"},
    {"edge_id": "CBAZUCRE_E145", "edge_description": "rotor windings has_fault_mode broken tooth"},
    {"edge_id": "CBAZUCRE_E146", "edge_description": "switches of power converter has_fault_mode inter-turn short circuit"},
    {"edge_id": "CBAZUCRE_E147", "edge_description": "switches of power converter has_fault_mode open circuit fault"},
    {"edge_id": "CBAZUCRE_E148", "edge_description": "switches of power converter has_fault_mode short circuit fault"},
    {"edge_id": "CBAZUCRE_E149", "edge_description": "switches of power converter has_fault_mode capacitance reduction"},
    {"edge_id": "CBAZUCRE_E150", "edge_description": "switches of power converter has_fault_mode pressure drop"},
    {"edge_id": "CBAZUCRE_E151", "edge_description": "switches of power converter has_fault_mode broken tooth"}
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
| 1 | `CBAZUCRE_E121` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | inter-turn short circuit |  |
| 2 | `CBAZUCRE_E122` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | open circuit fault |  |
| 3 | `CBAZUCRE_E123` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | short circuit fault |  |
| 4 | `CBAZUCRE_E124` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | capacitance reduction |  |
| 5 | `CBAZUCRE_E125` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | pressure drop |  |
| 6 | `CBAZUCRE_E126` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | broken tooth |  |
| 7 | `CBAZUCRE_E127` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | inter-turn short circuit |  |
| 8 | `CBAZUCRE_E128` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | open circuit fault |  |
| 9 | `CBAZUCRE_E129` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | short circuit fault |  |
| 10 | `CBAZUCRE_E130` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | capacitance reduction |  |
| 11 | `CBAZUCRE_E131` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | pressure drop |  |
| 12 | `CBAZUCRE_E132` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | broken tooth |  |
| 13 | `CBAZUCRE_E133` | `can obviously reflect` | 11-Sensor Information | anemometer |  | 05-Fault Mode | inter-turn short circuit |  |
| 14 | `CBAZUCRE_E134` | `can obviously reflect` | 11-Sensor Information | anemometer |  | 05-Fault Mode | open circuit fault |  |
| 15 | `CBAZUCRE_E135` | `can obviously reflect` | 11-Sensor Information | anemometer |  | 05-Fault Mode | short circuit fault |  |
| 16 | `CBAZUCRE_E136` | `can obviously reflect` | 11-Sensor Information | anemometer |  | 05-Fault Mode | capacitance reduction |  |
| 17 | `CBAZUCRE_E137` | `can obviously reflect` | 11-Sensor Information | anemometer |  | 05-Fault Mode | pressure drop |  |
| 18 | `CBAZUCRE_E138` | `can obviously reflect` | 11-Sensor Information | anemometer |  | 05-Fault Mode | broken tooth |  |
| 19 | `CBAZUCRE_E140` | `has_fault_mode` | 04-Fault Location | rotor windings |  | 05-Fault Mode | inter-turn short circuit |  |
| 20 | `CBAZUCRE_E141` | `has_fault_mode` | 04-Fault Location | rotor windings |  | 05-Fault Mode | open circuit fault |  |
| 21 | `CBAZUCRE_E142` | `has_fault_mode` | 04-Fault Location | rotor windings |  | 05-Fault Mode | short circuit fault |  |
| 22 | `CBAZUCRE_E143` | `has_fault_mode` | 04-Fault Location | rotor windings |  | 05-Fault Mode | capacitance reduction |  |
| 23 | `CBAZUCRE_E144` | `has_fault_mode` | 04-Fault Location | rotor windings |  | 05-Fault Mode | pressure drop |  |
| 24 | `CBAZUCRE_E145` | `has_fault_mode` | 04-Fault Location | rotor windings |  | 05-Fault Mode | broken tooth |  |
| 25 | `CBAZUCRE_E146` | `has_fault_mode` | 04-Fault Location | switches of power converter |  | 05-Fault Mode | inter-turn short circuit |  |
| 26 | `CBAZUCRE_E147` | `has_fault_mode` | 04-Fault Location | switches of power converter |  | 05-Fault Mode | open circuit fault |  |
| 27 | `CBAZUCRE_E148` | `has_fault_mode` | 04-Fault Location | switches of power converter |  | 05-Fault Mode | short circuit fault |  |
| 28 | `CBAZUCRE_E149` | `has_fault_mode` | 04-Fault Location | switches of power converter |  | 05-Fault Mode | capacitance reduction |  |
| 29 | `CBAZUCRE_E150` | `has_fault_mode` | 04-Fault Location | switches of power converter |  | 05-Fault Mode | pressure drop |  |
| 30 | `CBAZUCRE_E151` | `has_fault_mode` | 04-Fault Location | switches of power converter |  | 05-Fault Mode | broken tooth |  |

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
