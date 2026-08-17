# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：2VKGSYJ7
- **Paper Title**：Feature extraction using adaptive multiwavelets and synthetic detection index for rotor fault diagnosis of rotating machinery
- **Number of Candidate Edges to Judge**：27 

---

## II. LLM Input

> **Input Material**: Reference ID `2VKGSYJ7`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "2VKGSYJ7_E115", "edge_description": "unbalance contains 2 g mass block"},
    {"edge_id": "2VKGSYJ7_E116", "edge_description": "misalignment contains 2 g mass block"},
    {"edge_id": "2VKGSYJ7_E117", "edge_description": "rotor-to-stator rub contains 2 g mass block"},
    {"edge_id": "2VKGSYJ7_E118", "edge_description": "rotor contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E119", "edge_description": "power generator contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E120", "edge_description": "rotor contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E121", "edge_description": "coupling contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E122", "edge_description": "stator contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E123", "edge_description": "unbalance contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E124", "edge_description": "misalignment contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E125", "edge_description": "rotor-to-stator rub contains_phm_task rotor fault diagnosis"},
    {"edge_id": "2VKGSYJ7_E127", "edge_description": "rotor induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E128", "edge_description": "rotor induces_problem sensitivity of NSPs to the changes of machine condition"},
    {"edge_id": "2VKGSYJ7_E129", "edge_description": "power generator induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E130", "edge_description": "power generator induces_problem sensitivity of NSPs to the changes of machine condition"},
    {"edge_id": "2VKGSYJ7_E131", "edge_description": "1200 rpm, 500 rpm induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E132", "edge_description": "1200 rpm, 500 rpm induces_problem sensitivity of NSPs to the changes of machine condition"},
    {"edge_id": "2VKGSYJ7_E133", "edge_description": "2 g mass block induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E134", "edge_description": "2 g mass block induces_problem sensitivity of NSPs to the changes of machine condition"},
    {"edge_id": "2VKGSYJ7_E135", "edge_description": "No Compound Fault induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E136", "edge_description": "No Compound Fault induces_problem sensitivity of NSPs to the changes of machine condition"},
    {"edge_id": "2VKGSYJ7_E137", "edge_description": "rotor fault diagnosis induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E138", "edge_description": "rotor fault diagnosis induces_problem sensitivity of NSPs to the changes of machine condition"},
    {"edge_id": "2VKGSYJ7_E139", "edge_description": "20 training data files, 16 training data files induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E140", "edge_description": "20 training data files, 16 training data files induces_problem sensitivity of NSPs to the changes of machine condition"},
    {"edge_id": "2VKGSYJ7_E141", "edge_description": "submerged in substantial noise induces_problem noise"},
    {"edge_id": "2VKGSYJ7_E142", "edge_description": "submerged in substantial noise induces_problem sensitivity of NSPs to the changes of machine condition"}
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
| 1 | `2VKGSYJ7_E115` | `contains` | 05-Fault Mode | unbalance |  | 06-Fault Severity | 2 g mass block(Single Severity) |  |
| 2 | `2VKGSYJ7_E116` | `contains` | 05-Fault Mode | misalignment |  | 06-Fault Severity | 2 g mass block(Single Severity) |  |
| 3 | `2VKGSYJ7_E117` | `contains` | 05-Fault Mode | rotor-to-stator rub |  | 06-Fault Severity | 2 g mass block(Single Severity) |  |
| 4 | `2VKGSYJ7_E118` | `contains_phm_task` | 02-Object Type | rotor |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 5 | `2VKGSYJ7_E119` | `contains_phm_task` | 02-Object Type | power generator |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 6 | `2VKGSYJ7_E120` | `contains_phm_task` | 04-Fault Location | rotor |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 7 | `2VKGSYJ7_E121` | `contains_phm_task` | 04-Fault Location | coupling |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 8 | `2VKGSYJ7_E122` | `contains_phm_task` | 04-Fault Location | stator |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 9 | `2VKGSYJ7_E123` | `contains_phm_task` | 05-Fault Mode | unbalance |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 10 | `2VKGSYJ7_E124` | `contains_phm_task` | 05-Fault Mode | misalignment |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 11 | `2VKGSYJ7_E125` | `contains_phm_task` | 05-Fault Mode | rotor-to-stator rub |  | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  |
| 12 | `2VKGSYJ7_E127` | `induces_problem` | 02-Object Type | rotor |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 13 | `2VKGSYJ7_E128` | `induces_problem` | 02-Object Type | rotor |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |
| 14 | `2VKGSYJ7_E129` | `induces_problem` | 02-Object Type | power generator |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 15 | `2VKGSYJ7_E130` | `induces_problem` | 02-Object Type | power generator |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |
| 16 | `2VKGSYJ7_E131` | `induces_problem` | 03-Operating Conditions | 1200 rpm, 500 rpm(Multiple Conditions) |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 17 | `2VKGSYJ7_E132` | `induces_problem` | 03-Operating Conditions | 1200 rpm, 500 rpm(Multiple Conditions) |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |
| 18 | `2VKGSYJ7_E133` | `induces_problem` | 06-Fault Severity | 2 g mass block(Single Severity) |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 19 | `2VKGSYJ7_E134` | `induces_problem` | 06-Fault Severity | 2 g mass block(Single Severity) |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |
| 20 | `2VKGSYJ7_E135` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 21 | `2VKGSYJ7_E136` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |
| 22 | `2VKGSYJ7_E137` | `induces_problem` | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 23 | `2VKGSYJ7_E138` | `induces_problem` | 08-PHM Task | rotor fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |
| 24 | `2VKGSYJ7_E139` | `induces_problem` | 12-Training Data Availability | 20 training data files, 16 training data files(Scarce) |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 25 | `2VKGSYJ7_E140` | `induces_problem` | 12-Training Data Availability | 20 training data files, 16 training data files(Scarce) |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |
| 26 | `2VKGSYJ7_E141` | `induces_problem` | 13-Noise Level | submerged in substantial noise(High Noise) |  | 09-Problem Scenario | noise(Uncertainty) |  |
| 27 | `2VKGSYJ7_E142` | `induces_problem` | 13-Noise Level | submerged in substantial noise(High Noise) |  | 09-Problem Scenario | sensitivity of NSPs to the changes of machine condition(Other) |  |

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

### ▶ For `induces_problem` (X type → 09-Problem Scenario type)

**Retention Principle**: Encourage retaining but do not retain incorrect candidate edges. Specifically:
- **Retainable**: The paper **directly mentions** that source induces/causes the target problem scenario; or although not directly mentioned, it is **very likely to indirectly exist** when combining context/domain knowledge
- **Not Retainable**: The paper **does not mention it at all**, and it is **impossible to indirectly infer** this causal relation from the text content or domain knowledge(such edges will pollute the graph and must be deleted)
**Judgment Basis**: Comprehensively understand the full text, examining whether the problem description, experimental motivation, method design, etc., imply the source→target causal logic.

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 27 edges)*
