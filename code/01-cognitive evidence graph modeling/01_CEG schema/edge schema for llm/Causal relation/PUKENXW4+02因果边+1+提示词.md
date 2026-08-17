# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PUKENXW4
- **Paper Title**：A method for multiple soft fault diagnosis of linear analog circuits
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `PUKENXW4`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PUKENXW4_E021", "edge_description": "linear analog electronic circuits contains Sallen-Key filter"},
    {"edge_id": "PUKENXW4_E022", "edge_description": "linear analog electronic circuits contains Tow-Thomas filter"},
    {"edge_id": "PUKENXW4_E023", "edge_description": "linear analog electronic circuits contains second-order elliptic filter"},
    {"edge_id": "PUKENXW4_E024", "edge_description": "Sallen-Key filter contains resistor"},
    {"edge_id": "PUKENXW4_E025", "edge_description": "Sallen-Key filter contains capacitor"},
    {"edge_id": "PUKENXW4_E026", "edge_description": "Tow-Thomas filter contains resistor"},
    {"edge_id": "PUKENXW4_E027", "edge_description": "Tow-Thomas filter contains capacitor"},
    {"edge_id": "PUKENXW4_E028", "edge_description": "second-order elliptic filter contains resistor"},
    {"edge_id": "PUKENXW4_E029", "edge_description": "second-order elliptic filter contains capacitor"},
    {"edge_id": "PUKENXW4_E030", "edge_description": "Sallen-Key filter contains AC state at discrete frequencies"},
    {"edge_id": "PUKENXW4_E031", "edge_description": "Tow-Thomas filter contains AC state at discrete frequencies"},
    {"edge_id": "PUKENXW4_E032", "edge_description": "second-order elliptic filter contains AC state at discrete frequencies"},
    {"edge_id": "PUKENXW4_E034", "edge_description": "digital multimeter is collected on resistor"},
    {"edge_id": "PUKENXW4_E035", "edge_description": "digital multimeter is collected on capacitor"},
    {"edge_id": "PUKENXW4_E037", "edge_description": "Laboratory measurements of Sallen-Key filter can be used for multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E038", "edge_description": "Laboratory measurements of Tow-Thomas filter can be used for multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E039", "edge_description": "Laboratory measurements of second-order elliptic filter can be used for multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E040", "edge_description": "resistor has_fault_mode soft fault"},
    {"edge_id": "PUKENXW4_E041", "edge_description": "capacitor has_fault_mode soft fault"},
    {"edge_id": "PUKENXW4_E043", "edge_description": "Sallen-Key filter contains_phm_task multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E044", "edge_description": "Tow-Thomas filter contains_phm_task multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E045", "edge_description": "second-order elliptic filter contains_phm_task multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E046", "edge_description": "resistor contains_phm_task multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E047", "edge_description": "capacitor contains_phm_task multiple soft fault diagnosis"},
    {"edge_id": "PUKENXW4_E050", "edge_description": "Sallen-Key filter induces_problem multiple soft faults"},
    {"edge_id": "PUKENXW4_E051", "edge_description": "Sallen-Key filter induces_problem deviations of the healthy parameters and measurement uncertainty"},
    {"edge_id": "PUKENXW4_E052", "edge_description": "Tow-Thomas filter induces_problem multiple soft faults"},
    {"edge_id": "PUKENXW4_E053", "edge_description": "Tow-Thomas filter induces_problem deviations of the healthy parameters and measurement uncertainty"},
    {"edge_id": "PUKENXW4_E054", "edge_description": "second-order elliptic filter induces_problem multiple soft faults"},
    {"edge_id": "PUKENXW4_E055", "edge_description": "second-order elliptic filter induces_problem deviations of the healthy parameters and measurement uncertainty"}
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
| 1 | `PUKENXW4_E021` | `contains` | 01-Object Domain | linear analog electronic circuits(Electronics) |  | 02-Object Type | Sallen-Key filter |  |
| 2 | `PUKENXW4_E022` | `contains` | 01-Object Domain | linear analog electronic circuits(Electronics) |  | 02-Object Type | Tow-Thomas filter |  |
| 3 | `PUKENXW4_E023` | `contains` | 01-Object Domain | linear analog electronic circuits(Electronics) |  | 02-Object Type | second-order elliptic filter |  |
| 4 | `PUKENXW4_E024` | `contains` | 02-Object Type | Sallen-Key filter |  | 04-Fault Location | resistor |  |
| 5 | `PUKENXW4_E025` | `contains` | 02-Object Type | Sallen-Key filter |  | 04-Fault Location | capacitor |  |
| 6 | `PUKENXW4_E026` | `contains` | 02-Object Type | Tow-Thomas filter |  | 04-Fault Location | resistor |  |
| 7 | `PUKENXW4_E027` | `contains` | 02-Object Type | Tow-Thomas filter |  | 04-Fault Location | capacitor |  |
| 8 | `PUKENXW4_E028` | `contains` | 02-Object Type | second-order elliptic filter |  | 04-Fault Location | resistor |  |
| 9 | `PUKENXW4_E029` | `contains` | 02-Object Type | second-order elliptic filter |  | 04-Fault Location | capacitor |  |
| 10 | `PUKENXW4_E030` | `contains` | 02-Object Type | Sallen-Key filter |  | 03-Operating Conditions | AC state at discrete frequencies(Multiple Conditions) |  |
| 11 | `PUKENXW4_E031` | `contains` | 02-Object Type | Tow-Thomas filter |  | 03-Operating Conditions | AC state at discrete frequencies(Multiple Conditions) |  |
| 12 | `PUKENXW4_E032` | `contains` | 02-Object Type | second-order elliptic filter |  | 03-Operating Conditions | AC state at discrete frequencies(Multiple Conditions) |  |
| 13 | `PUKENXW4_E034` | `is collected on` | 11-Sensor Information | digital multimeter |  | 04-Fault Location | resistor |  |
| 14 | `PUKENXW4_E035` | `is collected on` | 11-Sensor Information | digital multimeter |  | 04-Fault Location | capacitor |  |
| 15 | `PUKENXW4_E037` | `can be used for` | 10-Dataset | Laboratory measurements of Sallen-Key filter |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 16 | `PUKENXW4_E038` | `can be used for` | 10-Dataset | Laboratory measurements of Tow-Thomas filter |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 17 | `PUKENXW4_E039` | `can be used for` | 10-Dataset | Laboratory measurements of second-order elliptic filter |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 18 | `PUKENXW4_E040` | `has_fault_mode` | 04-Fault Location | resistor |  | 05-Fault Mode | soft fault |  |
| 19 | `PUKENXW4_E041` | `has_fault_mode` | 04-Fault Location | capacitor |  | 05-Fault Mode | soft fault |  |
| 20 | `PUKENXW4_E043` | `contains_phm_task` | 02-Object Type | Sallen-Key filter |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 21 | `PUKENXW4_E044` | `contains_phm_task` | 02-Object Type | Tow-Thomas filter |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 22 | `PUKENXW4_E045` | `contains_phm_task` | 02-Object Type | second-order elliptic filter |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 23 | `PUKENXW4_E046` | `contains_phm_task` | 04-Fault Location | resistor |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 24 | `PUKENXW4_E047` | `contains_phm_task` | 04-Fault Location | capacitor |  | 08-PHM Task | multiple soft fault diagnosis(Diagnosis Task) |  |
| 25 | `PUKENXW4_E050` | `induces_problem` | 02-Object Type | Sallen-Key filter |  | 09-Problem Scenario | multiple soft faults(Compound Faults) |  |
| 26 | `PUKENXW4_E051` | `induces_problem` | 02-Object Type | Sallen-Key filter |  | 09-Problem Scenario | deviations of the healthy parameters and measurement uncertainty(Uncertainty) |  |
| 27 | `PUKENXW4_E052` | `induces_problem` | 02-Object Type | Tow-Thomas filter |  | 09-Problem Scenario | multiple soft faults(Compound Faults) |  |
| 28 | `PUKENXW4_E053` | `induces_problem` | 02-Object Type | Tow-Thomas filter |  | 09-Problem Scenario | deviations of the healthy parameters and measurement uncertainty(Uncertainty) |  |
| 29 | `PUKENXW4_E054` | `induces_problem` | 02-Object Type | second-order elliptic filter |  | 09-Problem Scenario | multiple soft faults(Compound Faults) |  |
| 30 | `PUKENXW4_E055` | `induces_problem` | 02-Object Type | second-order elliptic filter |  | 09-Problem Scenario | deviations of the healthy parameters and measurement uncertainty(Uncertainty) |  |

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

### ▶ For `is collected on` (Sensor Information type → Fault Location type)

**High Standard**: The paper must explicitly express that the sensor is **physically installed/arranged on** the target fault location, i.e., there is a description of the **physical positional relationship** between the sensor and the fault location.
The mere appearance in the dataset description of "a sensor used for a certain fault" is insufficient — the physical arrangement or installation context of the sensor must be reflected
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the relationship between the physical installation position of the sensor and the fault location, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
