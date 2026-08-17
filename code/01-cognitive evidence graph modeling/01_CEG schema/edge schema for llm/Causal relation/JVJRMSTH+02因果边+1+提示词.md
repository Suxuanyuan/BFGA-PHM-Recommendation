# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：JVJRMSTH
- **Paper Title**：Global geometric similarity scheme for feature selection in fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `JVJRMSTH`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "JVJRMSTH_E059", "edge_description": "wind turbine contains wind turbine"},
    {"edge_id": "JVJRMSTH_E060", "edge_description": "wind turbine contains bearing"},
    {"edge_id": "JVJRMSTH_E061", "edge_description": "wind turbine contains wind wheel"},
    {"edge_id": "JVJRMSTH_E062", "edge_description": "wind turbine contains blades"},
    {"edge_id": "JVJRMSTH_E063", "edge_description": "wind turbine contains yaw system"},
    {"edge_id": "JVJRMSTH_E064", "edge_description": "wind turbine contains shaft"},
    {"edge_id": "JVJRMSTH_E065", "edge_description": "wind turbine contains bearing chock"},
    {"edge_id": "JVJRMSTH_E066", "edge_description": "wind turbine contains bearing"},
    {"edge_id": "JVJRMSTH_E067", "edge_description": "bearing contains wind wheel"},
    {"edge_id": "JVJRMSTH_E068", "edge_description": "bearing contains blades"},
    {"edge_id": "JVJRMSTH_E069", "edge_description": "bearing contains yaw system"},
    {"edge_id": "JVJRMSTH_E070", "edge_description": "bearing contains shaft"},
    {"edge_id": "JVJRMSTH_E071", "edge_description": "bearing contains bearing chock"},
    {"edge_id": "JVJRMSTH_E072", "edge_description": "bearing contains bearing"},
    {"edge_id": "JVJRMSTH_E073", "edge_description": "wind turbine contains fixed speed"},
    {"edge_id": "JVJRMSTH_E074", "edge_description": "bearing contains fixed speed"},
    {"edge_id": "JVJRMSTH_E075", "edge_description": "mass imbalance contains No Compound Fault"},
    {"edge_id": "JVJRMSTH_E076", "edge_description": "aero-asymmetry contains No Compound Fault"},
    {"edge_id": "JVJRMSTH_E077", "edge_description": "changes in airfoil of blades contains No Compound Fault"},
    {"edge_id": "JVJRMSTH_E078", "edge_description": "yaw fault contains No Compound Fault"},
    {"edge_id": "JVJRMSTH_E079", "edge_description": "misalignment contains No Compound Fault"},
    {"edge_id": "JVJRMSTH_E080", "edge_description": "loosening contains No Compound Fault"},
    {"edge_id": "JVJRMSTH_E081", "edge_description": "bearing fault contains No Compound Fault"},
    {"edge_id": "JVJRMSTH_E082", "edge_description": "acceleration sensor is collected on wind wheel"},
    {"edge_id": "JVJRMSTH_E083", "edge_description": "acceleration sensor is collected on blades"},
    {"edge_id": "JVJRMSTH_E084", "edge_description": "acceleration sensor is collected on yaw system"},
    {"edge_id": "JVJRMSTH_E085", "edge_description": "acceleration sensor is collected on shaft"},
    {"edge_id": "JVJRMSTH_E086", "edge_description": "acceleration sensor is collected on bearing chock"},
    {"edge_id": "JVJRMSTH_E087", "edge_description": "acceleration sensor is collected on bearing"},
    {"edge_id": "JVJRMSTH_E088", "edge_description": "displacement sensor is collected on wind wheel"}
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
| 1 | `JVJRMSTH_E059` | `contains` | 01-Object Domain | wind turbine(Industrial) |  | 02-Object Type | wind turbine |  |
| 2 | `JVJRMSTH_E060` | `contains` | 01-Object Domain | wind turbine(Industrial) |  | 02-Object Type | bearing |  |
| 3 | `JVJRMSTH_E061` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | wind wheel |  |
| 4 | `JVJRMSTH_E062` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | blades |  |
| 5 | `JVJRMSTH_E063` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | yaw system |  |
| 6 | `JVJRMSTH_E064` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | shaft |  |
| 7 | `JVJRMSTH_E065` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | bearing chock |  |
| 8 | `JVJRMSTH_E066` | `contains` | 02-Object Type | wind turbine |  | 04-Fault Location | bearing |  |
| 9 | `JVJRMSTH_E067` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | wind wheel |  |
| 10 | `JVJRMSTH_E068` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | blades |  |
| 11 | `JVJRMSTH_E069` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | yaw system |  |
| 12 | `JVJRMSTH_E070` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | shaft |  |
| 13 | `JVJRMSTH_E071` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing chock |  |
| 14 | `JVJRMSTH_E072` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing |  |
| 15 | `JVJRMSTH_E073` | `contains` | 02-Object Type | wind turbine |  | 03-Operating Conditions | fixed speed(Single Condition) |  |
| 16 | `JVJRMSTH_E074` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | fixed speed(Single Condition) |  |
| 17 | `JVJRMSTH_E075` | `contains` | 05-Fault Mode | mass imbalance |  | 07-Compound Fault | No Compound Fault |  |
| 18 | `JVJRMSTH_E076` | `contains` | 05-Fault Mode | aero-asymmetry |  | 07-Compound Fault | No Compound Fault |  |
| 19 | `JVJRMSTH_E077` | `contains` | 05-Fault Mode | changes in airfoil of blades |  | 07-Compound Fault | No Compound Fault |  |
| 20 | `JVJRMSTH_E078` | `contains` | 05-Fault Mode | yaw fault |  | 07-Compound Fault | No Compound Fault |  |
| 21 | `JVJRMSTH_E079` | `contains` | 05-Fault Mode | misalignment |  | 07-Compound Fault | No Compound Fault |  |
| 22 | `JVJRMSTH_E080` | `contains` | 05-Fault Mode | loosening |  | 07-Compound Fault | No Compound Fault |  |
| 23 | `JVJRMSTH_E081` | `contains` | 05-Fault Mode | bearing fault |  | 07-Compound Fault | No Compound Fault |  |
| 24 | `JVJRMSTH_E082` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | wind wheel |  |
| 25 | `JVJRMSTH_E083` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | blades |  |
| 26 | `JVJRMSTH_E084` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | yaw system |  |
| 27 | `JVJRMSTH_E085` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | shaft |  |
| 28 | `JVJRMSTH_E086` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | bearing chock |  |
| 29 | `JVJRMSTH_E087` | `is collected on` | 11-Sensor Information | acceleration sensor |  | 04-Fault Location | bearing |  |
| 30 | `JVJRMSTH_E088` | `is collected on` | 11-Sensor Information | displacement sensor |  | 04-Fault Location | wind wheel |  |

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
