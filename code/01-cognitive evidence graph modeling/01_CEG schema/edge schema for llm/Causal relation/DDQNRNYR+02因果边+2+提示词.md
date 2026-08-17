# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：DDQNRNYR
- **Paper Title**：Intelligent fault diagnosis of wind turbines using multi-dimensional kernel domain spectrum technique
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `DDQNRNYR`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "DDQNRNYR_E103", "edge_description": "bearing has_fault_mode tooth broken"},
    {"edge_id": "DDQNRNYR_E104", "edge_description": "bearing has_fault_mode root crack of tooth"},
    {"edge_id": "DDQNRNYR_E105", "edge_description": "bearing has_fault_mode overheating"},
    {"edge_id": "DDQNRNYR_E106", "edge_description": "coupling has_fault_mode loose coupling"},
    {"edge_id": "DDQNRNYR_E107", "edge_description": "coupling has_fault_mode spalling"},
    {"edge_id": "DDQNRNYR_E108", "edge_description": "coupling has_fault_mode tooth broken"},
    {"edge_id": "DDQNRNYR_E109", "edge_description": "coupling has_fault_mode root crack of tooth"},
    {"edge_id": "DDQNRNYR_E110", "edge_description": "coupling has_fault_mode overheating"},
    {"edge_id": "DDQNRNYR_E111", "edge_description": "gear ring has_fault_mode loose coupling"},
    {"edge_id": "DDQNRNYR_E112", "edge_description": "gear ring has_fault_mode spalling"},
    {"edge_id": "DDQNRNYR_E113", "edge_description": "gear ring has_fault_mode tooth broken"},
    {"edge_id": "DDQNRNYR_E114", "edge_description": "gear ring has_fault_mode root crack of tooth"},
    {"edge_id": "DDQNRNYR_E115", "edge_description": "gear ring has_fault_mode overheating"},
    {"edge_id": "DDQNRNYR_E116", "edge_description": "planet gear has_fault_mode loose coupling"},
    {"edge_id": "DDQNRNYR_E117", "edge_description": "planet gear has_fault_mode spalling"},
    {"edge_id": "DDQNRNYR_E118", "edge_description": "planet gear has_fault_mode tooth broken"},
    {"edge_id": "DDQNRNYR_E119", "edge_description": "planet gear has_fault_mode root crack of tooth"},
    {"edge_id": "DDQNRNYR_E120", "edge_description": "planet gear has_fault_mode overheating"},
    {"edge_id": "DDQNRNYR_E121", "edge_description": "loose coupling contains Single Severity"},
    {"edge_id": "DDQNRNYR_E122", "edge_description": "spalling contains Single Severity"},
    {"edge_id": "DDQNRNYR_E123", "edge_description": "tooth broken contains Single Severity"},
    {"edge_id": "DDQNRNYR_E124", "edge_description": "root crack of tooth contains Single Severity"},
    {"edge_id": "DDQNRNYR_E125", "edge_description": "overheating contains Single Severity"},
    {"edge_id": "DDQNRNYR_E126", "edge_description": "generator bearing contains_phm_task fault diagnosis"},
    {"edge_id": "DDQNRNYR_E127", "edge_description": "gearbox contains_phm_task fault diagnosis"},
    {"edge_id": "DDQNRNYR_E128", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "DDQNRNYR_E129", "edge_description": "coupling contains_phm_task fault diagnosis"},
    {"edge_id": "DDQNRNYR_E130", "edge_description": "gear ring contains_phm_task fault diagnosis"},
    {"edge_id": "DDQNRNYR_E131", "edge_description": "planet gear contains_phm_task fault diagnosis"},
    {"edge_id": "DDQNRNYR_E132", "edge_description": "loose coupling contains_phm_task fault diagnosis"}
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
| 1 | `DDQNRNYR_E103` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | tooth broken |  |
| 2 | `DDQNRNYR_E104` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | root crack of tooth |  |
| 3 | `DDQNRNYR_E105` | `has_fault_mode` | 04-Fault Location | bearing |  | 05-Fault Mode | overheating |  |
| 4 | `DDQNRNYR_E106` | `has_fault_mode` | 04-Fault Location | coupling |  | 05-Fault Mode | loose coupling |  |
| 5 | `DDQNRNYR_E107` | `has_fault_mode` | 04-Fault Location | coupling |  | 05-Fault Mode | spalling |  |
| 6 | `DDQNRNYR_E108` | `has_fault_mode` | 04-Fault Location | coupling |  | 05-Fault Mode | tooth broken |  |
| 7 | `DDQNRNYR_E109` | `has_fault_mode` | 04-Fault Location | coupling |  | 05-Fault Mode | root crack of tooth |  |
| 8 | `DDQNRNYR_E110` | `has_fault_mode` | 04-Fault Location | coupling |  | 05-Fault Mode | overheating |  |
| 9 | `DDQNRNYR_E111` | `has_fault_mode` | 04-Fault Location | gear ring |  | 05-Fault Mode | loose coupling |  |
| 10 | `DDQNRNYR_E112` | `has_fault_mode` | 04-Fault Location | gear ring |  | 05-Fault Mode | spalling |  |
| 11 | `DDQNRNYR_E113` | `has_fault_mode` | 04-Fault Location | gear ring |  | 05-Fault Mode | tooth broken |  |
| 12 | `DDQNRNYR_E114` | `has_fault_mode` | 04-Fault Location | gear ring |  | 05-Fault Mode | root crack of tooth |  |
| 13 | `DDQNRNYR_E115` | `has_fault_mode` | 04-Fault Location | gear ring |  | 05-Fault Mode | overheating |  |
| 14 | `DDQNRNYR_E116` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | loose coupling |  |
| 15 | `DDQNRNYR_E117` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | spalling |  |
| 16 | `DDQNRNYR_E118` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | tooth broken |  |
| 17 | `DDQNRNYR_E119` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | root crack of tooth |  |
| 18 | `DDQNRNYR_E120` | `has_fault_mode` | 04-Fault Location | planet gear |  | 05-Fault Mode | overheating |  |
| 19 | `DDQNRNYR_E121` | `contains` | 05-Fault Mode | loose coupling |  | 06-Fault Severity | Single Severity |  |
| 20 | `DDQNRNYR_E122` | `contains` | 05-Fault Mode | spalling |  | 06-Fault Severity | Single Severity |  |
| 21 | `DDQNRNYR_E123` | `contains` | 05-Fault Mode | tooth broken |  | 06-Fault Severity | Single Severity |  |
| 22 | `DDQNRNYR_E124` | `contains` | 05-Fault Mode | root crack of tooth |  | 06-Fault Severity | Single Severity |  |
| 23 | `DDQNRNYR_E125` | `contains` | 05-Fault Mode | overheating |  | 06-Fault Severity | Single Severity |  |
| 24 | `DDQNRNYR_E126` | `contains_phm_task` | 02-Object Type | generator bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 25 | `DDQNRNYR_E127` | `contains_phm_task` | 02-Object Type | gearbox |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 26 | `DDQNRNYR_E128` | `contains_phm_task` | 04-Fault Location | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 27 | `DDQNRNYR_E129` | `contains_phm_task` | 04-Fault Location | coupling |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 28 | `DDQNRNYR_E130` | `contains_phm_task` | 04-Fault Location | gear ring |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 29 | `DDQNRNYR_E131` | `contains_phm_task` | 04-Fault Location | planet gear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 30 | `DDQNRNYR_E132` | `contains_phm_task` | 05-Fault Mode | loose coupling |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |

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
