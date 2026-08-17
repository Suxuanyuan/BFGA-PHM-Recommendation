# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：4C7UAXLZ
- **Paper Title**：Representational Learning for Fault Diagnosis of Wind Turbine Equipment: A Multi-Layered Extreme Learning Machines Approach
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `4C7UAXLZ`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "4C7UAXLZ_E106", "edge_description": "tri-axial accelerometers can obviously reflect gear crack"},
    {"edge_id": "4C7UAXLZ_E107", "edge_description": "tri-axial accelerometers can obviously reflect chipped tooth"},
    {"edge_id": "4C7UAXLZ_E109", "edge_description": "gearbox has_fault_mode unbalance"},
    {"edge_id": "4C7UAXLZ_E110", "edge_description": "gearbox has_fault_mode looseness"},
    {"edge_id": "4C7UAXLZ_E111", "edge_description": "gearbox has_fault_mode mechanical misalignment"},
    {"edge_id": "4C7UAXLZ_E112", "edge_description": "gearbox has_fault_mode wear"},
    {"edge_id": "4C7UAXLZ_E113", "edge_description": "gearbox has_fault_mode gear tooth broken"},
    {"edge_id": "4C7UAXLZ_E114", "edge_description": "gearbox has_fault_mode gear crack"},
    {"edge_id": "4C7UAXLZ_E115", "edge_description": "gearbox has_fault_mode chipped tooth"},
    {"edge_id": "4C7UAXLZ_E116", "edge_description": "bearing has_fault_mode unbalance"},
    {"edge_id": "4C7UAXLZ_E117", "edge_description": "bearing has_fault_mode looseness"},
    {"edge_id": "4C7UAXLZ_E118", "edge_description": "bearing has_fault_mode mechanical misalignment"},
    {"edge_id": "4C7UAXLZ_E119", "edge_description": "bearing has_fault_mode wear"},
    {"edge_id": "4C7UAXLZ_E120", "edge_description": "bearing has_fault_mode gear tooth broken"},
    {"edge_id": "4C7UAXLZ_E121", "edge_description": "bearing has_fault_mode gear crack"},
    {"edge_id": "4C7UAXLZ_E122", "edge_description": "bearing has_fault_mode chipped tooth"},
    {"edge_id": "4C7UAXLZ_E123", "edge_description": "output shaft has_fault_mode unbalance"},
    {"edge_id": "4C7UAXLZ_E124", "edge_description": "output shaft has_fault_mode looseness"},
    {"edge_id": "4C7UAXLZ_E125", "edge_description": "output shaft has_fault_mode mechanical misalignment"},
    {"edge_id": "4C7UAXLZ_E126", "edge_description": "output shaft has_fault_mode wear"},
    {"edge_id": "4C7UAXLZ_E127", "edge_description": "output shaft has_fault_mode gear tooth broken"},
    {"edge_id": "4C7UAXLZ_E128", "edge_description": "output shaft has_fault_mode gear crack"},
    {"edge_id": "4C7UAXLZ_E129", "edge_description": "output shaft has_fault_mode chipped tooth"},
    {"edge_id": "4C7UAXLZ_E130", "edge_description": "unbalance contains Single Severity"},
    {"edge_id": "4C7UAXLZ_E131", "edge_description": "looseness contains Single Severity"},
    {"edge_id": "4C7UAXLZ_E132", "edge_description": "mechanical misalignment contains Single Severity"},
    {"edge_id": "4C7UAXLZ_E133", "edge_description": "wear contains Single Severity"},
    {"edge_id": "4C7UAXLZ_E134", "edge_description": "gear tooth broken contains Single Severity"},
    {"edge_id": "4C7UAXLZ_E135", "edge_description": "gear crack contains Single Severity"},
    {"edge_id": "4C7UAXLZ_E136", "edge_description": "chipped tooth contains Single Severity"}
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
| 1 | `4C7UAXLZ_E106` | `can obviously reflect` | 11-Sensor Information | tri-axial accelerometers |  | 05-Fault Mode | gear crack |  |
| 2 | `4C7UAXLZ_E107` | `can obviously reflect` | 11-Sensor Information | tri-axial accelerometers |  | 05-Fault Mode | chipped tooth |  |
| 3 | `4C7UAXLZ_E109` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | unbalance |  |
| 4 | `4C7UAXLZ_E110` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | looseness |  |
| 5 | `4C7UAXLZ_E111` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | mechanical misalignment |  |
| 6 | `4C7UAXLZ_E112` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | wear |  |
| 7 | `4C7UAXLZ_E113` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | gear tooth broken |  |
| 8 | `4C7UAXLZ_E114` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | gear crack |  |
| 9 | `4C7UAXLZ_E115` | `has_fault_mode` | 04-Fault Location | gearbox |  | 05-Fault Mode | chipped tooth |  |
| 10 | `4C7UAXLZ_E116` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | unbalance |  |
| 11 | `4C7UAXLZ_E117` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | looseness |  |
| 12 | `4C7UAXLZ_E118` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | mechanical misalignment |  |
| 13 | `4C7UAXLZ_E119` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | wear |  |
| 14 | `4C7UAXLZ_E120` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | gear tooth broken |  |
| 15 | `4C7UAXLZ_E121` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | gear crack |  |
| 16 | `4C7UAXLZ_E122` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | chipped tooth |  |
| 17 | `4C7UAXLZ_E123` | `has_fault_mode` | 04-Fault Location | output shaft |  | 05-Fault Mode | unbalance |  |
| 18 | `4C7UAXLZ_E124` | `has_fault_mode` | 04-Fault Location | output shaft |  | 05-Fault Mode | looseness |  |
| 19 | `4C7UAXLZ_E125` | `has_fault_mode` | 04-Fault Location | output shaft |  | 05-Fault Mode | mechanical misalignment |  |
| 20 | `4C7UAXLZ_E126` | `has_fault_mode` | 04-Fault Location | output shaft |  | 05-Fault Mode | wear |  |
| 21 | `4C7UAXLZ_E127` | `has_fault_mode` | 04-Fault Location | output shaft |  | 05-Fault Mode | gear tooth broken |  |
| 22 | `4C7UAXLZ_E128` | `has_fault_mode` | 04-Fault Location | output shaft |  | 05-Fault Mode | gear crack |  |
| 23 | `4C7UAXLZ_E129` | `has_fault_mode` | 04-Fault Location | output shaft |  | 05-Fault Mode | chipped tooth |  |
| 24 | `4C7UAXLZ_E130` | `contains` | 05-Fault Mode | unbalance |  | 06-Fault Severity | Single Severity |  |
| 25 | `4C7UAXLZ_E131` | `contains` | 05-Fault Mode | looseness |  | 06-Fault Severity | Single Severity |  |
| 26 | `4C7UAXLZ_E132` | `contains` | 05-Fault Mode | mechanical misalignment |  | 06-Fault Severity | Single Severity |  |
| 27 | `4C7UAXLZ_E133` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | Single Severity |  |
| 28 | `4C7UAXLZ_E134` | `contains` | 05-Fault Mode | gear tooth broken |  | 06-Fault Severity | Single Severity |  |
| 29 | `4C7UAXLZ_E135` | `contains` | 05-Fault Mode | gear crack |  | 06-Fault Severity | Single Severity |  |
| 30 | `4C7UAXLZ_E136` | `contains` | 05-Fault Mode | chipped tooth |  | 06-Fault Severity | Single Severity |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
