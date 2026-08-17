# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：QWJURFDW
- **Paper Title**：Matching Demodulation Transform With Application to Feature Extraction of Rotor Rub-Impact Fault
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `QWJURFDW`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "QWJURFDW_E058", "edge_description": "rotating machinery / heavy oil catalytic cracking machine set contains rotor system"},
    {"edge_id": "QWJURFDW_E059", "edge_description": "rotating machinery / heavy oil catalytic cracking machine set contains heavy oil catalytic cracking machine set"},
    {"edge_id": "QWJURFDW_E060", "edge_description": "rotor system contains shaft"},
    {"edge_id": "QWJURFDW_E061", "edge_description": "rotor system contains hub"},
    {"edge_id": "QWJURFDW_E062", "edge_description": "rotor system contains gas seal"},
    {"edge_id": "QWJURFDW_E063", "edge_description": "heavy oil catalytic cracking machine set contains shaft"},
    {"edge_id": "QWJURFDW_E064", "edge_description": "heavy oil catalytic cracking machine set contains hub"},
    {"edge_id": "QWJURFDW_E065", "edge_description": "heavy oil catalytic cracking machine set contains gas seal"},
    {"edge_id": "QWJURFDW_E066", "edge_description": "rotor system contains operation speed of 2000 rpm / rotating speed of about 5800 rpm"},
    {"edge_id": "QWJURFDW_E067", "edge_description": "heavy oil catalytic cracking machine set contains operation speed of 2000 rpm / rotating speed of about 5800 rpm"},
    {"edge_id": "QWJURFDW_E069", "edge_description": "eddy current sensor is collected on shaft"},
    {"edge_id": "QWJURFDW_E070", "edge_description": "eddy current sensor is collected on hub"},
    {"edge_id": "QWJURFDW_E071", "edge_description": "eddy current sensor is collected on gas seal"},
    {"edge_id": "QWJURFDW_E073", "edge_description": "Bently RK-4 rotor kit can be used for rotor fault diagnosis / feature extraction of rub-impact fault"},
    {"edge_id": "QWJURFDW_E074", "edge_description": "heavy oil catalytic cracking machine set can be used for rotor fault diagnosis / feature extraction of rub-impact fault"},
    {"edge_id": "QWJURFDW_E075", "edge_description": "shaft has_fault_mode rub-impact"},
    {"edge_id": "QWJURFDW_E076", "edge_description": "hub has_fault_mode rub-impact"},
    {"edge_id": "QWJURFDW_E077", "edge_description": "gas seal has_fault_mode rub-impact"},
    {"edge_id": "QWJURFDW_E079", "edge_description": "rotor system contains_phm_task rotor fault diagnosis / feature extraction of rub-impact fault"},
    {"edge_id": "QWJURFDW_E080", "edge_description": "heavy oil catalytic cracking machine set contains_phm_task rotor fault diagnosis / feature extraction of rub-impact fault"},
    {"edge_id": "QWJURFDW_E081", "edge_description": "shaft contains_phm_task rotor fault diagnosis / feature extraction of rub-impact fault"},
    {"edge_id": "QWJURFDW_E082", "edge_description": "hub contains_phm_task rotor fault diagnosis / feature extraction of rub-impact fault"},
    {"edge_id": "QWJURFDW_E083", "edge_description": "gas seal contains_phm_task rotor fault diagnosis / feature extraction of rub-impact fault"},
    {"edge_id": "QWJURFDW_E086", "edge_description": "rotor system induces_problem highly oscillatory frequency modulation (FM) feature / nonstationary signals"},
    {"edge_id": "QWJURFDW_E087", "edge_description": "rotor system induces_problem noise / model uncertainty"},
    {"edge_id": "QWJURFDW_E088", "edge_description": "heavy oil catalytic cracking machine set induces_problem highly oscillatory frequency modulation (FM) feature / nonstationary signals"},
    {"edge_id": "QWJURFDW_E089", "edge_description": "heavy oil catalytic cracking machine set induces_problem noise / model uncertainty"},
    {"edge_id": "QWJURFDW_E090", "edge_description": "operation speed of 2000 rpm / rotating speed of about 5800 rpm induces_problem highly oscillatory frequency modulation (FM) feature / nonstationary signals"},
    {"edge_id": "QWJURFDW_E091", "edge_description": "operation speed of 2000 rpm / rotating speed of about 5800 rpm induces_problem noise / model uncertainty"},
    {"edge_id": "QWJURFDW_E092", "edge_description": "small rubbing fault induces_problem highly oscillatory frequency modulation (FM) feature / nonstationary signals"}
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
| 1 | `QWJURFDW_E058` | `contains` | 01-Object Domain | rotating machinery / heavy oil catalytic cracking machine set(Industrial) |  | 02-Object Type | rotor system |  |
| 2 | `QWJURFDW_E059` | `contains` | 01-Object Domain | rotating machinery / heavy oil catalytic cracking machine set(Industrial) |  | 02-Object Type | heavy oil catalytic cracking machine set |  |
| 3 | `QWJURFDW_E060` | `contains` | 02-Object Type | rotor system |  | 04-Fault Location | shaft |  |
| 4 | `QWJURFDW_E061` | `contains` | 02-Object Type | rotor system |  | 04-Fault Location | hub |  |
| 5 | `QWJURFDW_E062` | `contains` | 02-Object Type | rotor system |  | 04-Fault Location | gas seal |  |
| 6 | `QWJURFDW_E063` | `contains` | 02-Object Type | heavy oil catalytic cracking machine set |  | 04-Fault Location | shaft |  |
| 7 | `QWJURFDW_E064` | `contains` | 02-Object Type | heavy oil catalytic cracking machine set |  | 04-Fault Location | hub |  |
| 8 | `QWJURFDW_E065` | `contains` | 02-Object Type | heavy oil catalytic cracking machine set |  | 04-Fault Location | gas seal |  |
| 9 | `QWJURFDW_E066` | `contains` | 02-Object Type | rotor system |  | 03-Operating Conditions | operation speed of 2000 rpm / rotating speed of about 5800 rpm(Multiple Conditions) |  |
| 10 | `QWJURFDW_E067` | `contains` | 02-Object Type | heavy oil catalytic cracking machine set |  | 03-Operating Conditions | operation speed of 2000 rpm / rotating speed of about 5800 rpm(Multiple Conditions) |  |
| 11 | `QWJURFDW_E069` | `is collected on` | 11-Sensor Information | eddy current sensor |  | 04-Fault Location | shaft |  |
| 12 | `QWJURFDW_E070` | `is collected on` | 11-Sensor Information | eddy current sensor |  | 04-Fault Location | hub |  |
| 13 | `QWJURFDW_E071` | `is collected on` | 11-Sensor Information | eddy current sensor |  | 04-Fault Location | gas seal |  |
| 14 | `QWJURFDW_E073` | `can be used for` | 10-Dataset | Bently RK-4 rotor kit |  | 08-PHM Task | rotor fault diagnosis / feature extraction of rub-impact fault(Diagnosis Task) |  |
| 15 | `QWJURFDW_E074` | `can be used for` | 10-Dataset | heavy oil catalytic cracking machine set |  | 08-PHM Task | rotor fault diagnosis / feature extraction of rub-impact fault(Diagnosis Task) |  |
| 16 | `QWJURFDW_E075` | `has_fault_mode` | 04-Fault Location | shaft |  | 05-Fault Mode | rub-impact |  |
| 17 | `QWJURFDW_E076` | `has_fault_mode` | 04-Fault Location | hub |  | 05-Fault Mode | rub-impact |  |
| 18 | `QWJURFDW_E077` | `has_fault_mode` | 04-Fault Location | gas seal |  | 05-Fault Mode | rub-impact |  |
| 19 | `QWJURFDW_E079` | `contains_phm_task` | 02-Object Type | rotor system |  | 08-PHM Task | rotor fault diagnosis / feature extraction of rub-impact fault(Diagnosis Task) |  |
| 20 | `QWJURFDW_E080` | `contains_phm_task` | 02-Object Type | heavy oil catalytic cracking machine set |  | 08-PHM Task | rotor fault diagnosis / feature extraction of rub-impact fault(Diagnosis Task) |  |
| 21 | `QWJURFDW_E081` | `contains_phm_task` | 04-Fault Location | shaft |  | 08-PHM Task | rotor fault diagnosis / feature extraction of rub-impact fault(Diagnosis Task) |  |
| 22 | `QWJURFDW_E082` | `contains_phm_task` | 04-Fault Location | hub |  | 08-PHM Task | rotor fault diagnosis / feature extraction of rub-impact fault(Diagnosis Task) |  |
| 23 | `QWJURFDW_E083` | `contains_phm_task` | 04-Fault Location | gas seal |  | 08-PHM Task | rotor fault diagnosis / feature extraction of rub-impact fault(Diagnosis Task) |  |
| 24 | `QWJURFDW_E086` | `induces_problem` | 02-Object Type | rotor system |  | 09-Problem Scenario | highly oscillatory frequency modulation (FM) feature / nonstationary signals(Other) |  |
| 25 | `QWJURFDW_E087` | `induces_problem` | 02-Object Type | rotor system |  | 09-Problem Scenario | noise / model uncertainty(Uncertainty) |  |
| 26 | `QWJURFDW_E088` | `induces_problem` | 02-Object Type | heavy oil catalytic cracking machine set |  | 09-Problem Scenario | highly oscillatory frequency modulation (FM) feature / nonstationary signals(Other) |  |
| 27 | `QWJURFDW_E089` | `induces_problem` | 02-Object Type | heavy oil catalytic cracking machine set |  | 09-Problem Scenario | noise / model uncertainty(Uncertainty) |  |
| 28 | `QWJURFDW_E090` | `induces_problem` | 03-Operating Conditions | operation speed of 2000 rpm / rotating speed of about 5800 rpm(Multiple Conditions) |  | 09-Problem Scenario | highly oscillatory frequency modulation (FM) feature / nonstationary signals(Other) |  |
| 29 | `QWJURFDW_E091` | `induces_problem` | 03-Operating Conditions | operation speed of 2000 rpm / rotating speed of about 5800 rpm(Multiple Conditions) |  | 09-Problem Scenario | noise / model uncertainty(Uncertainty) |  |
| 30 | `QWJURFDW_E092` | `induces_problem` | 06-Fault Severity | small rubbing fault(Single Severity) |  | 09-Problem Scenario | highly oscillatory frequency modulation (FM) feature / nonstationary signals(Other) |  |

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
