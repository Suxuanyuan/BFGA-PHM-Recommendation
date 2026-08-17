# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：FQZR7ZH2
- **Paper Title**：PV Module Fault Diagnosis Based on Microconvertes and Day-Ahead Forecast
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `FQZR7ZH2`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "FQZR7ZH2_E055", "edge_description": "photovoltaic (PV) systems contains PV module"},
    {"edge_id": "FQZR7ZH2_E056", "edge_description": "photovoltaic (PV) systems contains micro-converter"},
    {"edge_id": "FQZR7ZH2_E057", "edge_description": "PV module contains PV module"},
    {"edge_id": "FQZR7ZH2_E058", "edge_description": "PV module contains micro-converter"},
    {"edge_id": "FQZR7ZH2_E059", "edge_description": "PV module contains data transmitter"},
    {"edge_id": "FQZR7ZH2_E060", "edge_description": "micro-converter contains PV module"},
    {"edge_id": "FQZR7ZH2_E061", "edge_description": "micro-converter contains micro-converter"},
    {"edge_id": "FQZR7ZH2_E062", "edge_description": "micro-converter contains data transmitter"},
    {"edge_id": "FQZR7ZH2_E063", "edge_description": "PV module contains intermittent and variable environmental conditions"},
    {"edge_id": "FQZR7ZH2_E064", "edge_description": "micro-converter contains intermittent and variable environmental conditions"},
    {"edge_id": "FQZR7ZH2_E066", "edge_description": "monitoring system for electrical parameters is collected on PV module"},
    {"edge_id": "FQZR7ZH2_E067", "edge_description": "monitoring system for electrical parameters is collected on micro-converter"},
    {"edge_id": "FQZR7ZH2_E068", "edge_description": "monitoring system for electrical parameters is collected on data transmitter"},
    {"edge_id": "FQZR7ZH2_E071", "edge_description": "PV module has_fault_mode micro-cracks"},
    {"edge_id": "FQZR7ZH2_E072", "edge_description": "micro-converter has_fault_mode micro-cracks"},
    {"edge_id": "FQZR7ZH2_E073", "edge_description": "data transmitter has_fault_mode micro-cracks"},
    {"edge_id": "FQZR7ZH2_E075", "edge_description": "PV module contains_phm_task PV module fault diagnosis"},
    {"edge_id": "FQZR7ZH2_E076", "edge_description": "micro-converter contains_phm_task PV module fault diagnosis"},
    {"edge_id": "FQZR7ZH2_E077", "edge_description": "PV module contains_phm_task PV module fault diagnosis"},
    {"edge_id": "FQZR7ZH2_E078", "edge_description": "micro-converter contains_phm_task PV module fault diagnosis"},
    {"edge_id": "FQZR7ZH2_E079", "edge_description": "data transmitter contains_phm_task PV module fault diagnosis"},
    {"edge_id": "FQZR7ZH2_E082", "edge_description": "PV module induces_problem uncertainty affecting predictions"},
    {"edge_id": "FQZR7ZH2_E083", "edge_description": "PV module induces_problem distinguishing anomalies from regular shadings and ageing"},
    {"edge_id": "FQZR7ZH2_E084", "edge_description": "micro-converter induces_problem uncertainty affecting predictions"},
    {"edge_id": "FQZR7ZH2_E085", "edge_description": "micro-converter induces_problem distinguishing anomalies from regular shadings and ageing"},
    {"edge_id": "FQZR7ZH2_E086", "edge_description": "intermittent and variable environmental conditions induces_problem uncertainty affecting predictions"},
    {"edge_id": "FQZR7ZH2_E087", "edge_description": "intermittent and variable environmental conditions induces_problem distinguishing anomalies from regular shadings and ageing"},
    {"edge_id": "FQZR7ZH2_E088", "edge_description": "soft fault, hard fault induces_problem uncertainty affecting predictions"},
    {"edge_id": "FQZR7ZH2_E089", "edge_description": "soft fault, hard fault induces_problem distinguishing anomalies from regular shadings and ageing"},
    {"edge_id": "FQZR7ZH2_E090", "edge_description": "No Compound Fault induces_problem uncertainty affecting predictions"}
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
| 1 | `FQZR7ZH2_E055` | `contains` | 01-Object Domain | photovoltaic (PV) systems(Industrial) |  | 02-Object Type | PV module |  |
| 2 | `FQZR7ZH2_E056` | `contains` | 01-Object Domain | photovoltaic (PV) systems(Industrial) |  | 02-Object Type | micro-converter |  |
| 3 | `FQZR7ZH2_E057` | `contains` | 02-Object Type | PV module |  | 04-Fault Location | PV module |  |
| 4 | `FQZR7ZH2_E058` | `contains` | 02-Object Type | PV module |  | 04-Fault Location | micro-converter |  |
| 5 | `FQZR7ZH2_E059` | `contains` | 02-Object Type | PV module |  | 04-Fault Location | data transmitter |  |
| 6 | `FQZR7ZH2_E060` | `contains` | 02-Object Type | micro-converter |  | 04-Fault Location | PV module |  |
| 7 | `FQZR7ZH2_E061` | `contains` | 02-Object Type | micro-converter |  | 04-Fault Location | micro-converter |  |
| 8 | `FQZR7ZH2_E062` | `contains` | 02-Object Type | micro-converter |  | 04-Fault Location | data transmitter |  |
| 9 | `FQZR7ZH2_E063` | `contains` | 02-Object Type | PV module |  | 03-Operating Conditions | intermittent and variable environmental conditions(Variable Conditions) |  |
| 10 | `FQZR7ZH2_E064` | `contains` | 02-Object Type | micro-converter |  | 03-Operating Conditions | intermittent and variable environmental conditions(Variable Conditions) |  |
| 11 | `FQZR7ZH2_E066` | `is collected on` | 11-Sensor Information | monitoring system for electrical parameters |  | 04-Fault Location | PV module |  |
| 12 | `FQZR7ZH2_E067` | `is collected on` | 11-Sensor Information | monitoring system for electrical parameters |  | 04-Fault Location | micro-converter |  |
| 13 | `FQZR7ZH2_E068` | `is collected on` | 11-Sensor Information | monitoring system for electrical parameters |  | 04-Fault Location | data transmitter |  |
| 14 | `FQZR7ZH2_E071` | `has_fault_mode` | 04-Fault Location | PV module |  | 05-Fault Mode | micro-cracks |  |
| 15 | `FQZR7ZH2_E072` | `has_fault_mode` | 04-Fault Location | micro-converter |  | 05-Fault Mode | micro-cracks |  |
| 16 | `FQZR7ZH2_E073` | `has_fault_mode` | 04-Fault Location | data transmitter |  | 05-Fault Mode | micro-cracks |  |
| 17 | `FQZR7ZH2_E075` | `contains_phm_task` | 02-Object Type | PV module |  | 08-PHM Task | PV module fault diagnosis(Diagnosis Task) |  |
| 18 | `FQZR7ZH2_E076` | `contains_phm_task` | 02-Object Type | micro-converter |  | 08-PHM Task | PV module fault diagnosis(Diagnosis Task) |  |
| 19 | `FQZR7ZH2_E077` | `contains_phm_task` | 04-Fault Location | PV module |  | 08-PHM Task | PV module fault diagnosis(Diagnosis Task) |  |
| 20 | `FQZR7ZH2_E078` | `contains_phm_task` | 04-Fault Location | micro-converter |  | 08-PHM Task | PV module fault diagnosis(Diagnosis Task) |  |
| 21 | `FQZR7ZH2_E079` | `contains_phm_task` | 04-Fault Location | data transmitter |  | 08-PHM Task | PV module fault diagnosis(Diagnosis Task) |  |
| 22 | `FQZR7ZH2_E082` | `induces_problem` | 02-Object Type | PV module |  | 09-Problem Scenario | uncertainty affecting predictions(Uncertainty) |  |
| 23 | `FQZR7ZH2_E083` | `induces_problem` | 02-Object Type | PV module |  | 09-Problem Scenario | distinguishing anomalies from regular shadings and ageing(Other) |  |
| 24 | `FQZR7ZH2_E084` | `induces_problem` | 02-Object Type | micro-converter |  | 09-Problem Scenario | uncertainty affecting predictions(Uncertainty) |  |
| 25 | `FQZR7ZH2_E085` | `induces_problem` | 02-Object Type | micro-converter |  | 09-Problem Scenario | distinguishing anomalies from regular shadings and ageing(Other) |  |
| 26 | `FQZR7ZH2_E086` | `induces_problem` | 03-Operating Conditions | intermittent and variable environmental conditions(Variable Conditions) |  | 09-Problem Scenario | uncertainty affecting predictions(Uncertainty) |  |
| 27 | `FQZR7ZH2_E087` | `induces_problem` | 03-Operating Conditions | intermittent and variable environmental conditions(Variable Conditions) |  | 09-Problem Scenario | distinguishing anomalies from regular shadings and ageing(Other) |  |
| 28 | `FQZR7ZH2_E088` | `induces_problem` | 06-Fault Severity | soft fault, hard fault(Multiple Severities) |  | 09-Problem Scenario | uncertainty affecting predictions(Uncertainty) |  |
| 29 | `FQZR7ZH2_E089` | `induces_problem` | 06-Fault Severity | soft fault, hard fault(Multiple Severities) |  | 09-Problem Scenario | distinguishing anomalies from regular shadings and ageing(Other) |  |
| 30 | `FQZR7ZH2_E090` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | uncertainty affecting predictions(Uncertainty) |  |

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
