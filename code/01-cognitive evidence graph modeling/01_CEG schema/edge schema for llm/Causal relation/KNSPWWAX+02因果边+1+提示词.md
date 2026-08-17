# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：KNSPWWAX
- **Paper Title**：An improved local mean decomposition method and its application for fault diagnosis of reciprocating compressor
- **Number of Candidate Edges to Judge**：28 

---

## II. LLM Input

> **Input Material**: Reference ID `KNSPWWAX`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "KNSPWWAX_E052", "edge_description": "petroleum and chemical industry contains reciprocating compressor"},
    {"edge_id": "KNSPWWAX_E053", "edge_description": "petroleum and chemical industry contains bearing"},
    {"edge_id": "KNSPWWAX_E054", "edge_description": "reciprocating compressor contains bearing between the crankshaft pin and first stage connecting rod"},
    {"edge_id": "KNSPWWAX_E055", "edge_description": "bearing contains bearing between the crankshaft pin and first stage connecting rod"},
    {"edge_id": "KNSPWWAX_E056", "edge_description": "reciprocating compressor contains motor rotation speed of 496 rpm"},
    {"edge_id": "KNSPWWAX_E057", "edge_description": "bearing contains motor rotation speed of 496 rpm"},
    {"edge_id": "KNSPWWAX_E061", "edge_description": "Simulated signal can be used for fault diagnosis"},
    {"edge_id": "KNSPWWAX_E062", "edge_description": "Vibration signals of 2D12 reciprocating compressor can be used for fault diagnosis"},
    {"edge_id": "KNSPWWAX_E065", "edge_description": "reciprocating compressor contains_phm_task fault diagnosis"},
    {"edge_id": "KNSPWWAX_E066", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "KNSPWWAX_E070", "edge_description": "reciprocating compressor induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E071", "edge_description": "reciprocating compressor induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E072", "edge_description": "bearing induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E073", "edge_description": "bearing induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E074", "edge_description": "motor rotation speed of 496 rpm induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E075", "edge_description": "motor rotation speed of 496 rpm induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E076", "edge_description": "Single Severity induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E077", "edge_description": "Single Severity induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E078", "edge_description": "No Compound Fault induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E079", "edge_description": "No Compound Fault induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E080", "edge_description": "fault diagnosis induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E081", "edge_description": "fault diagnosis induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E082", "edge_description": "100 vibration signal samples induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E083", "edge_description": "100 vibration signal samples induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E084", "edge_description": "signals contaminated with noise induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E085", "edge_description": "signals contaminated with noise induces_problem signals contaminated with noise"},
    {"edge_id": "KNSPWWAX_E086", "edge_description": "calculation time induces_problem nonlinearity and nonstationarity of vibration signals"},
    {"edge_id": "KNSPWWAX_E087", "edge_description": "calculation time induces_problem signals contaminated with noise"}
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
| 1 | `KNSPWWAX_E052` | `contains` | 01-Object Domain | petroleum and chemical industry(Industrial) |  | 02-Object Type | reciprocating compressor |  |
| 2 | `KNSPWWAX_E053` | `contains` | 01-Object Domain | petroleum and chemical industry(Industrial) |  | 02-Object Type | bearing |  |
| 3 | `KNSPWWAX_E054` | `contains` | 02-Object Type | reciprocating compressor |  | 04-Fault Location | bearing between the crankshaft pin and first stage connecting rod |  |
| 4 | `KNSPWWAX_E055` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing between the crankshaft pin and first stage connecting rod |  |
| 5 | `KNSPWWAX_E056` | `contains` | 02-Object Type | reciprocating compressor |  | 03-Operating Conditions | motor rotation speed of 496 rpm(Single Condition) |  |
| 6 | `KNSPWWAX_E057` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | motor rotation speed of 496 rpm(Single Condition) |  |
| 7 | `KNSPWWAX_E061` | `can be used for` | 10-Dataset | Simulated signal |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 8 | `KNSPWWAX_E062` | `can be used for` | 10-Dataset | Vibration signals of 2D12 reciprocating compressor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 9 | `KNSPWWAX_E065` | `contains_phm_task` | 02-Object Type | reciprocating compressor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `KNSPWWAX_E066` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `KNSPWWAX_E070` | `induces_problem` | 02-Object Type | reciprocating compressor |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 12 | `KNSPWWAX_E071` | `induces_problem` | 02-Object Type | reciprocating compressor |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 13 | `KNSPWWAX_E072` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 14 | `KNSPWWAX_E073` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 15 | `KNSPWWAX_E074` | `induces_problem` | 03-Operating Conditions | motor rotation speed of 496 rpm(Single Condition) |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 16 | `KNSPWWAX_E075` | `induces_problem` | 03-Operating Conditions | motor rotation speed of 496 rpm(Single Condition) |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 17 | `KNSPWWAX_E076` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 18 | `KNSPWWAX_E077` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 19 | `KNSPWWAX_E078` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 20 | `KNSPWWAX_E079` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 21 | `KNSPWWAX_E080` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 22 | `KNSPWWAX_E081` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 23 | `KNSPWWAX_E082` | `induces_problem` | 12-Training Data Availability | 100 vibration signal samples(Sufficient) |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 24 | `KNSPWWAX_E083` | `induces_problem` | 12-Training Data Availability | 100 vibration signal samples(Sufficient) |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 25 | `KNSPWWAX_E084` | `induces_problem` | 13-Noise Level | signals contaminated with noise(High Noise) |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 26 | `KNSPWWAX_E085` | `induces_problem` | 13-Noise Level | signals contaminated with noise(High Noise) |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |
| 27 | `KNSPWWAX_E086` | `induces_problem` | 14-Computational Resource | calculation time(Low Resource Consumption) |  | 09-Problem Scenario | nonlinearity and nonstationarity of vibration signals(Other) |  |
| 28 | `KNSPWWAX_E087` | `induces_problem` | 14-Computational Resource | calculation time(Low Resource Consumption) |  | 09-Problem Scenario | signals contaminated with noise(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 28 edges)*
