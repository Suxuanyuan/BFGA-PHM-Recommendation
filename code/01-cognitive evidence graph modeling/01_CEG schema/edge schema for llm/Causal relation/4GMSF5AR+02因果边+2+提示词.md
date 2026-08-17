# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：4GMSF5AR
- **Paper Title**：A framework to automate fault detection and diagnosis based on moving window principal component analysis and Bayesian network
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `4GMSF5AR`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "4GMSF5AR_E103", "edge_description": "Real operational database of a 50 MW generating unit from a Brazilian Hydroelectric Power Plant (HPP) can be used for fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E104", "edge_description": "Simulated operational data for hydrogenerator fault scenarios can be used for fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E105", "edge_description": "Generator shaft has_fault_mode Excessive vibration"},
    {"edge_id": "4GMSF5AR_E106", "edge_description": "Generator shaft has_fault_mode Premature degradation of copper insulation"},
    {"edge_id": "4GMSF5AR_E107", "edge_description": "Generator shaft has_fault_mode Does not indicate the actual temperature value"},
    {"edge_id": "4GMSF5AR_E108", "edge_description": "Stator has_fault_mode Excessive vibration"},
    {"edge_id": "4GMSF5AR_E109", "edge_description": "Stator has_fault_mode Premature degradation of copper insulation"},
    {"edge_id": "4GMSF5AR_E110", "edge_description": "Stator has_fault_mode Does not indicate the actual temperature value"},
    {"edge_id": "4GMSF5AR_E111", "edge_description": "Temperature sensor of combined bearing heat exchanger exit (hot) water has_fault_mode Excessive vibration"},
    {"edge_id": "4GMSF5AR_E112", "edge_description": "Temperature sensor of combined bearing heat exchanger exit (hot) water has_fault_mode Premature degradation of copper insulation"},
    {"edge_id": "4GMSF5AR_E113", "edge_description": "Temperature sensor of combined bearing heat exchanger exit (hot) water has_fault_mode Does not indicate the actual temperature value"},
    {"edge_id": "4GMSF5AR_E114", "edge_description": "Excessive vibration contains exponential gain as a function of time"},
    {"edge_id": "4GMSF5AR_E115", "edge_description": "Premature degradation of copper insulation contains exponential gain as a function of time"},
    {"edge_id": "4GMSF5AR_E116", "edge_description": "Does not indicate the actual temperature value contains exponential gain as a function of time"},
    {"edge_id": "4GMSF5AR_E117", "edge_description": "hydrogenerator contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E118", "edge_description": "turbine contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E119", "edge_description": "heat exchanger contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E120", "edge_description": "Generator shaft contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E121", "edge_description": "Stator contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E122", "edge_description": "Temperature sensor of combined bearing heat exchanger exit (hot) water contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E123", "edge_description": "Excessive vibration contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E124", "edge_description": "Premature degradation of copper insulation contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E125", "edge_description": "Does not indicate the actual temperature value contains_phm_task fault detection and diagnosis"},
    {"edge_id": "4GMSF5AR_E127", "edge_description": "hydrogenerator induces_problem absence of labeled fault data"},
    {"edge_id": "4GMSF5AR_E128", "edge_description": "hydrogenerator induces_problem complex systems"},
    {"edge_id": "4GMSF5AR_E129", "edge_description": "hydrogenerator induces_problem uncertainty"},
    {"edge_id": "4GMSF5AR_E130", "edge_description": "turbine induces_problem absence of labeled fault data"},
    {"edge_id": "4GMSF5AR_E131", "edge_description": "turbine induces_problem complex systems"},
    {"edge_id": "4GMSF5AR_E132", "edge_description": "turbine induces_problem uncertainty"},
    {"edge_id": "4GMSF5AR_E133", "edge_description": "heat exchanger induces_problem absence of labeled fault data"}
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
| 1 | `4GMSF5AR_E103` | `can be used for` | 10-Dataset | Real operational database of a 50 MW generating unit from a Brazilian Hydroelectric Power Plant (HPP) |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 2 | `4GMSF5AR_E104` | `can be used for` | 10-Dataset | Simulated operational data for hydrogenerator fault scenarios |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 3 | `4GMSF5AR_E105` | `has_fault_mode` | 04-Fault Location | Generator shaft |  | 05-Fault Mode | Excessive vibration |  |
| 4 | `4GMSF5AR_E106` | `has_fault_mode` | 04-Fault Location | Generator shaft |  | 05-Fault Mode | Premature degradation of copper insulation |  |
| 5 | `4GMSF5AR_E107` | `has_fault_mode` | 04-Fault Location | Generator shaft |  | 05-Fault Mode | Does not indicate the actual temperature value |  |
| 6 | `4GMSF5AR_E108` | `has_fault_mode` | 04-Fault Location | Stator |  | 05-Fault Mode | Excessive vibration |  |
| 7 | `4GMSF5AR_E109` | `has_fault_mode` | 04-Fault Location | Stator |  | 05-Fault Mode | Premature degradation of copper insulation |  |
| 8 | `4GMSF5AR_E110` | `has_fault_mode` | 04-Fault Location | Stator |  | 05-Fault Mode | Does not indicate the actual temperature value |  |
| 9 | `4GMSF5AR_E111` | `has_fault_mode` | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  | 05-Fault Mode | Excessive vibration |  |
| 10 | `4GMSF5AR_E112` | `has_fault_mode` | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  | 05-Fault Mode | Premature degradation of copper insulation |  |
| 11 | `4GMSF5AR_E113` | `has_fault_mode` | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  | 05-Fault Mode | Does not indicate the actual temperature value |  |
| 12 | `4GMSF5AR_E114` | `contains` | 05-Fault Mode | Excessive vibration |  | 06-Fault Severity | exponential gain as a function of time(Multiple Severities) |  |
| 13 | `4GMSF5AR_E115` | `contains` | 05-Fault Mode | Premature degradation of copper insulation |  | 06-Fault Severity | exponential gain as a function of time(Multiple Severities) |  |
| 14 | `4GMSF5AR_E116` | `contains` | 05-Fault Mode | Does not indicate the actual temperature value |  | 06-Fault Severity | exponential gain as a function of time(Multiple Severities) |  |
| 15 | `4GMSF5AR_E117` | `contains_phm_task` | 02-Object Type | hydrogenerator |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 16 | `4GMSF5AR_E118` | `contains_phm_task` | 02-Object Type | turbine |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 17 | `4GMSF5AR_E119` | `contains_phm_task` | 02-Object Type | heat exchanger |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 18 | `4GMSF5AR_E120` | `contains_phm_task` | 04-Fault Location | Generator shaft |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 19 | `4GMSF5AR_E121` | `contains_phm_task` | 04-Fault Location | Stator |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 20 | `4GMSF5AR_E122` | `contains_phm_task` | 04-Fault Location | Temperature sensor of combined bearing heat exchanger exit (hot) water |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 21 | `4GMSF5AR_E123` | `contains_phm_task` | 05-Fault Mode | Excessive vibration |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 22 | `4GMSF5AR_E124` | `contains_phm_task` | 05-Fault Mode | Premature degradation of copper insulation |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 23 | `4GMSF5AR_E125` | `contains_phm_task` | 05-Fault Mode | Does not indicate the actual temperature value |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 24 | `4GMSF5AR_E127` | `induces_problem` | 02-Object Type | hydrogenerator |  | 09-Problem Scenario | absence of labeled fault data(Zero Fault Samples) |  |
| 25 | `4GMSF5AR_E128` | `induces_problem` | 02-Object Type | hydrogenerator |  | 09-Problem Scenario | complex systems(Complex Systems) |  |
| 26 | `4GMSF5AR_E129` | `induces_problem` | 02-Object Type | hydrogenerator |  | 09-Problem Scenario | uncertainty(Uncertainty) |  |
| 27 | `4GMSF5AR_E130` | `induces_problem` | 02-Object Type | turbine |  | 09-Problem Scenario | absence of labeled fault data(Zero Fault Samples) |  |
| 28 | `4GMSF5AR_E131` | `induces_problem` | 02-Object Type | turbine |  | 09-Problem Scenario | complex systems(Complex Systems) |  |
| 29 | `4GMSF5AR_E132` | `induces_problem` | 02-Object Type | turbine |  | 09-Problem Scenario | uncertainty(Uncertainty) |  |
| 30 | `4GMSF5AR_E133` | `induces_problem` | 02-Object Type | heat exchanger |  | 09-Problem Scenario | absence of labeled fault data(Zero Fault Samples) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
