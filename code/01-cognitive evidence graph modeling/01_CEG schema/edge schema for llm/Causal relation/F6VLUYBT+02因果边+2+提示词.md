# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：F6VLUYBT
- **Paper Title**：Evaluation of the Influence of Rotor Magnetic Anisotropy on Condition Monitoring of Two-Pole Induction Motors
- **Number of Candidate Edges to Judge**：18 

---

## II. LLM Input

> **Input Material**: Reference ID `F6VLUYBT`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "F6VLUYBT_E071", "edge_description": "Field data from 3.3-kV crude oil pump induction motors can be used for rotor fault detection"},
    {"edge_id": "F6VLUYBT_E072", "edge_description": "Experimental data from custom-built 380-V lab motors can be used for rotor fault detection"},
    {"edge_id": "F6VLUYBT_E079", "edge_description": "induction motor induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E080", "edge_description": "induction motor induces_problem uncertainty in fault detection due to random fault location"},
    {"edge_id": "F6VLUYBT_E081", "edge_description": "multiple load conditions induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E082", "edge_description": "multiple load conditions induces_problem uncertainty in fault detection due to random fault location"},
    {"edge_id": "F6VLUYBT_E083", "edge_description": "0-2 broken bars induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E084", "edge_description": "0-2 broken bars induces_problem uncertainty in fault detection due to random fault location"},
    {"edge_id": "F6VLUYBT_E085", "edge_description": "No Compound Fault induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E086", "edge_description": "No Compound Fault induces_problem uncertainty in fault detection due to random fault location"},
    {"edge_id": "F6VLUYBT_E087", "edge_description": "rotor fault detection induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E088", "edge_description": "rotor fault detection induces_problem uncertainty in fault detection due to random fault location"},
    {"edge_id": "F6VLUYBT_E089", "edge_description": "Not explicitly mentioned induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E090", "edge_description": "Not explicitly mentioned induces_problem uncertainty in fault detection due to random fault location"},
    {"edge_id": "F6VLUYBT_E091", "edge_description": "Not mentioned induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E092", "edge_description": "Not mentioned induces_problem uncertainty in fault detection due to random fault location"},
    {"edge_id": "F6VLUYBT_E093", "edge_description": "Not mentioned induces_problem false rotor fault alarms due to rotor core anisotropy"},
    {"edge_id": "F6VLUYBT_E094", "edge_description": "Not mentioned induces_problem uncertainty in fault detection due to random fault location"}
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
| 1 | `F6VLUYBT_E071` | `can be used for` | 10-Dataset | Field data from 3.3-kV crude oil pump induction motors |  | 08-PHM Task | rotor fault detection(Detection Task) |  |
| 2 | `F6VLUYBT_E072` | `can be used for` | 10-Dataset | Experimental data from custom-built 380-V lab motors |  | 08-PHM Task | rotor fault detection(Detection Task) |  |
| 3 | `F6VLUYBT_E079` | `induces_problem` | 02-Object Type | induction motor |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 4 | `F6VLUYBT_E080` | `induces_problem` | 02-Object Type | induction motor |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |
| 5 | `F6VLUYBT_E081` | `induces_problem` | 03-Operating Conditions | multiple load conditions(Multiple Conditions) |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 6 | `F6VLUYBT_E082` | `induces_problem` | 03-Operating Conditions | multiple load conditions(Multiple Conditions) |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |
| 7 | `F6VLUYBT_E083` | `induces_problem` | 06-Fault Severity | 0-2 broken bars(Multiple Severities) |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 8 | `F6VLUYBT_E084` | `induces_problem` | 06-Fault Severity | 0-2 broken bars(Multiple Severities) |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |
| 9 | `F6VLUYBT_E085` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 10 | `F6VLUYBT_E086` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |
| 11 | `F6VLUYBT_E087` | `induces_problem` | 08-PHM Task | rotor fault detection(Detection Task) |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 12 | `F6VLUYBT_E088` | `induces_problem` | 08-PHM Task | rotor fault detection(Detection Task) |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |
| 13 | `F6VLUYBT_E089` | `induces_problem` | 12-Training Data Availability | Not explicitly mentioned(Sufficient) |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 14 | `F6VLUYBT_E090` | `induces_problem` | 12-Training Data Availability | Not explicitly mentioned(Sufficient) |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |
| 15 | `F6VLUYBT_E091` | `induces_problem` | 13-Noise Level | Not mentioned(Normal) |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 16 | `F6VLUYBT_E092` | `induces_problem` | 13-Noise Level | Not mentioned(Normal) |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |
| 17 | `F6VLUYBT_E093` | `induces_problem` | 14-Computational Resource | Not mentioned |  | 09-Problem Scenario | false rotor fault alarms due to rotor core anisotropy(Other) |  |
| 18 | `F6VLUYBT_E094` | `induces_problem` | 14-Computational Resource | Not mentioned |  | 09-Problem Scenario | uncertainty in fault detection due to random fault location(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 18 edges)*
