# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**: S52HNMMF
- **Paper Title**: Bearing diagnostics: A method based on differential geometry
- **Number of Candidate Edges to Judge**: 10

---

## II. LLM Input

> **Input Material**: Reference ID `S52HNMMF` PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "S52HNMMF_E061", "edge_description": "spalling contains No Compound Fault"},
    {"edge_id": "S52HNMMF_E062", "edge_description": "pitting contains No Compound Fault"},
    {"edge_id": "S52HNMMF_E064", "edge_description": "vibration sensor can obviously reflect spalling"},
    {"edge_id": "S52HNMMF_E065", "edge_description": "vibration sensor can obviously reflect pitting"},
    {"edge_id": "S52HNMMF_E069", "edge_description": "bearing has_fault_mode spalling"},
    {"edge_id": "S52HNMMF_E070", "edge_description": "bearing has_fault_mode pitting"},
    {"edge_id": "S52HNMMF_E071", "edge_description": "spalling contains 0.007 in., run-to-failure"},
    {"edge_id": "S52HNMMF_E072", "edge_description": "pitting contains 0.007 in., run-to-failure"},
    {"edge_id": "S52HNMMF_E075", "edge_description": "spalling contains_phm_task fault diagnosis"},
    {"edge_id": "S52HNMMF_E076", "edge_description": "pitting contains_phm_task fault diagnosis"}
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
| 1 | `S52HNMMF_E061` | `contains` | 05-Fault Mode | spalling |  | 07-Compound Fault | No Compound Fault |  |
| 2 | `S52HNMMF_E062` | `contains` | 05-Fault Mode | pitting |  | 07-Compound Fault | No Compound Fault |  |
| 3 | `S52HNMMF_E064` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | spalling |  |
| 4 | `S52HNMMF_E065` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | pitting |  |
| 5 | `S52HNMMF_E069` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | spalling |  |
| 6 | `S52HNMMF_E070` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | pitting |  |
| 7 | `S52HNMMF_E071` | `contains` | 05-Fault Mode | spalling |  | 06-Fault Severity | 0.007 in., run-to-failure(Multiple Severities) |  |
| 8 | `S52HNMMF_E072` | `contains` | 05-Fault Mode | pitting |  | 06-Fault Severity | 0.007 in., run-to-failure(Multiple Severities) |  |
| 9 | `S52HNMMF_E075` | `contains_phm_task` | 05-Fault Mode | spalling |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `S52HNMMF_E076` | `contains_phm_task` | 05-Fault Mode | pitting |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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

### ▶ For `contains` (Containment / Belonging / Part-of Relation) [New in V2]

**Semantic Explanation**: `contains` indicates that the entity represented by source conceptually **encompasses, contains, belongs to, or is part of** the entity represented by target. This is a very common conceptual hierarchical relation in the PHM domain.

**Applicable Scenarios and Judgment Criteria**:
- **Object Type contains Fault Location**: The paper mentions that the object type contains the fault location, or the dataset actually used in the paper belongs to the object type and contains data of the fault location — - **Object Type contains Operating Conditions**: The paper discusses that the object type operates under the operating conditions, or the dataset used in the paper belongs to the object type and contains the operating conditions — e.g., "aero-engine operates under high-altitude / low-altitude conditions" implies a containment relation
- **Fault Mode contains Compound Fault**: The paper discusses that the fault mode contains the compound fault characteristics, or the dataset used in the paper contains the fault mode and the fault mode is mentioned as belonging to the compound fault mode — - **Fault Mode contains Fault Severity**: The paper discusses that the fault mode has the fault severity, or the dataset used in the paper contains the fault mode and the fault mode clearly has the fault severity in the dataset **Trap to Watch Out For**: The mere isolated appearance of source and target in the paper is insufficient for judgment; there must be a direct expression of the relation or an indirect relation reflected through the dataset.

### ▶ For `has_fault_mode` (Fault Location → Fault Mode) [New in V2]

**Semantic Explanation**: `has_fault_mode` indicates that source (fault location) **has / exhibits / produces** target (fault mode). This is one of the most core relations in the PHM domain — a certain location will develop a certain type of fault.

**Judgment Criteria**: Any of the following can be used to judge
- The paper explicitly describes that the fault mode exists at the location
- The experiment / dataset used in the paper reflects an association between the location and the fault mode
**Lenient Principle**: As long as the paper explicitly discusses "the fault mode of this location", it is regarded as "directly mentioned".


### ▶ For `contains_phm_task` (Fault-related type → PHM Task type) [New in V2]

**Semantic Explanation**: `contains_phm_task` indicates that source (fault location / fault mode / fault severity / object type, etc.) **involves or is used in** target (PHM task, such as fault diagnosis, life prediction, remaining useful life prediction, health management, etc.).

**Judgment Criteria**: Any of the following can be used to judge
- The paper's research topic is this PHM task, and the paper explicitly analyzes / studies the fault location / fault mode / fault severity / object type
- The paper's research topic is this PHM task, and the dataset actually used in the paper contains the fault location / fault mode / fault severity / object type
**Trap to Watch Out For**: The source entity must be an entity actually studied in the paper or mentioned in the dataset; the reviews of other people's methods in sections like Introduction should not be included.

---

## VI. LLM Constraints
### 6.1 Output Cleanliness Principle

- The output JSON must **not contain** any non-standard JSON content (e.g., comments, prefix descriptions, etc.)
- Each `edge_description` in the JSON array must be strictly extracted from the table above; do not rewrite it yourself

---

*This prompt is automatically generated by edge_02_prompt_v2.py (Batch 1, total 10 edges)*
*V2 Modification Date: 2026-06-17 | Modification: Added specific constraints for contains/has_fault_mode/contains_phm_task; reduced the judgment standard for can obviously reflect and is collected on*
