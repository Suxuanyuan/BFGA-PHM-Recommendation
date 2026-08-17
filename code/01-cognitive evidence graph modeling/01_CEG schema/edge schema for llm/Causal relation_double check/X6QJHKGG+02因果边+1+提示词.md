# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**: X6QJHKGG
- **Paper Title**: Rapid Fault Diagnosis of PEM Fuel Cells through Optimal Electrochemical Impedance Spectroscopy Tests
- **Number of Candidate Edges to Judge**: 18

---

## II. LLM Input

> **Input Material**: Reference ID `X6QJHKGG` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "X6QJHKGG_E072", "edge_description": "thermo-couples is collected on proton exchange membrane"},
    {"edge_id": "X6QJHKGG_E073", "edge_description": "thermo-couples is collected on gas diffusion layer"},
    {"edge_id": "X6QJHKGG_E074", "edge_description": "thermo-couples is collected on catalyst layer"},
    {"edge_id": "X6QJHKGG_E075", "edge_description": "pressure transducers is collected on proton exchange membrane"},
    {"edge_id": "X6QJHKGG_E076", "edge_description": "pressure transducers is collected on gas diffusion layer"},
    {"edge_id": "X6QJHKGG_E077", "edge_description": "pressure transducers is collected on catalyst layer"},
    {"edge_id": "X6QJHKGG_E078", "edge_description": "digital flow meters is collected on proton exchange membrane"},
    {"edge_id": "X6QJHKGG_E079", "edge_description": "digital flow meters is collected on gas diffusion layer"},
    {"edge_id": "X6QJHKGG_E080", "edge_description": "digital flow meters is collected on catalyst layer"},
    {"edge_id": "X6QJHKGG_E081", "edge_description": "thermo-couples can obviously reflect dehydration"},
    {"edge_id": "X6QJHKGG_E082", "edge_description": "thermo-couples can obviously reflect flooding"},
    {"edge_id": "X6QJHKGG_E083", "edge_description": "thermo-couples can obviously reflect electrocatalyst degradation"},
    {"edge_id": "X6QJHKGG_E084", "edge_description": "pressure transducers can obviously reflect dehydration"},
    {"edge_id": "X6QJHKGG_E085", "edge_description": "pressure transducers can obviously reflect flooding"},
    {"edge_id": "X6QJHKGG_E086", "edge_description": "pressure transducers can obviously reflect electrocatalyst degradation"},
    {"edge_id": "X6QJHKGG_E087", "edge_description": "digital flow meters can obviously reflect dehydration"},
    {"edge_id": "X6QJHKGG_E088", "edge_description": "digital flow meters can obviously reflect flooding"},
    {"edge_id": "X6QJHKGG_E089", "edge_description": "digital flow meters can obviously reflect electrocatalyst degradation"}
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
| 1 | `X6QJHKGG_E072` | `is collected on` | 11-Sensor Information | thermo-couples |  | 04-Fault Location | proton exchange membrane |  |
| 2 | `X6QJHKGG_E073` | `is collected on` | 11-Sensor Information | thermo-couples |  | 04-Fault Location | gas diffusion layer |  |
| 3 | `X6QJHKGG_E074` | `is collected on` | 11-Sensor Information | thermo-couples |  | 04-Fault Location | catalyst layer |  |
| 4 | `X6QJHKGG_E075` | `is collected on` | 11-Sensor Information | pressure transducers |  | 04-Fault Location | proton exchange membrane |  |
| 5 | `X6QJHKGG_E076` | `is collected on` | 11-Sensor Information | pressure transducers |  | 04-Fault Location | gas diffusion layer |  |
| 6 | `X6QJHKGG_E077` | `is collected on` | 11-Sensor Information | pressure transducers |  | 04-Fault Location | catalyst layer |  |
| 7 | `X6QJHKGG_E078` | `is collected on` | 11-Sensor Information | digital flow meters |  | 04-Fault Location | proton exchange membrane |  |
| 8 | `X6QJHKGG_E079` | `is collected on` | 11-Sensor Information | digital flow meters |  | 04-Fault Location | gas diffusion layer |  |
| 9 | `X6QJHKGG_E080` | `is collected on` | 11-Sensor Information | digital flow meters |  | 04-Fault Location | catalyst layer |  |
| 10 | `X6QJHKGG_E081` | `can obviously reflect` | 11-Sensor Information | thermo-couples |  | 05-Fault Mode | dehydration |  |
| 11 | `X6QJHKGG_E082` | `can obviously reflect` | 11-Sensor Information | thermo-couples |  | 05-Fault Mode | flooding |  |
| 12 | `X6QJHKGG_E083` | `can obviously reflect` | 11-Sensor Information | thermo-couples |  | 05-Fault Mode | electrocatalyst degradation |  |
| 13 | `X6QJHKGG_E084` | `can obviously reflect` | 11-Sensor Information | pressure transducers |  | 05-Fault Mode | dehydration |  |
| 14 | `X6QJHKGG_E085` | `can obviously reflect` | 11-Sensor Information | pressure transducers |  | 05-Fault Mode | flooding |  |
| 15 | `X6QJHKGG_E086` | `can obviously reflect` | 11-Sensor Information | pressure transducers |  | 05-Fault Mode | electrocatalyst degradation |  |
| 16 | `X6QJHKGG_E087` | `can obviously reflect` | 11-Sensor Information | digital flow meters |  | 05-Fault Mode | dehydration |  |
| 17 | `X6QJHKGG_E088` | `can obviously reflect` | 11-Sensor Information | digital flow meters |  | 05-Fault Mode | flooding |  |
| 18 | `X6QJHKGG_E089` | `can obviously reflect` | 11-Sensor Information | digital flow meters |  | 05-Fault Mode | electrocatalyst degradation |  |

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

**General Principle**: If the paper directly mentions that source_node and target_node have the edge_type relation, it can be retained; or if the dataset used in the paper reflects the edge_type relation between source_node and target_node, it can also be retained.

**Judgment Basis**: Use contextual semantic understanding to judge whether the relation exists, rather than exact matching of the edge_type characters.


---

## V. [Key Constraints] Strict Judgment Criteria for Specific edge_type

### ▶ For `can obviously reflect` (Sensor Information type → Fault Mode type)

**Moderate Standard**: Any of the following **conditions** is sufficient to be judged as "existing":
1. The paper describes that the sensor was used to collect data of the fault mode (with a specific correspondence)
2. The paper discusses the analysis of the fault mode through the sensor signal
**Trap to Watch Out For**: The sensor and the fault mode may not have a particularly clear correspondence in a certain dataset / research scheme; if not stated, judge based on the context and common knowledge. **Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses a sensor→fault-type causal association, rather than exact matching of English phrases

### ▶ For `is collected on` (Sensor Information type → Fault Location type)

**Moderate Standard**: Any of the following **conditions** is sufficient to be judged as "existing":
1. The paper describes that the sensor is installed/arranged on the fault location / research object
2. The paper uses expressions such as "data from this sensor" to establish the association between the sensor and the fault location / research object
3. The paper discusses the signal acquisition method for the fault location / research object
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the methodological or physical association between the sensor and the research object, rather than exact matching of English phrases

---

## VI. LLM Constraints
### 6.1 Output Cleanliness Principle

- The output JSON must **not contain** any non-standard JSON content (e.g., comments, prefix descriptions, etc.)
- Each `edge_description` in the JSON array must be strictly extracted from the table above; do not rewrite it yourself

---

*This prompt is automatically generated by edge_02_prompt_v2.py (Batch 1, total 18 edges)*
*V2 Modification Date: 2026-06-17 | Modification: Added specific constraints for contains/has_fault_mode/contains_phm_task; reduced the judgment standard for can obviously reflect and is collected on*
