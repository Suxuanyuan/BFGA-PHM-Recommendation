# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：RM9DUXE2
- **Paper Title**：A feature extraction method based on HLMD and MFE for bearing clearance fault of reciprocating compressor
- **Number of Candidate Edges to Judge**：24 

---

## II. LLM Input

> **Input Material**: Reference ID `RM9DUXE2`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "RM9DUXE2_E049", "edge_description": "petroleum and chemical production processes contains reciprocating compressor"},
    {"edge_id": "RM9DUXE2_E050", "edge_description": "petroleum and chemical production processes contains bearing"},
    {"edge_id": "RM9DUXE2_E051", "edge_description": "reciprocating compressor contains bearing"},
    {"edge_id": "RM9DUXE2_E052", "edge_description": "bearing contains bearing"},
    {"edge_id": "RM9DUXE2_E053", "edge_description": "reciprocating compressor contains shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm"},
    {"edge_id": "RM9DUXE2_E054", "edge_description": "bearing contains shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm"},
    {"edge_id": "RM9DUXE2_E061", "edge_description": "reciprocating compressor contains_phm_task fault diagnosis"},
    {"edge_id": "RM9DUXE2_E062", "edge_description": "bearing contains_phm_task fault diagnosis"},
    {"edge_id": "RM9DUXE2_E066", "edge_description": "reciprocating compressor induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E067", "edge_description": "reciprocating compressor induces_problem susceptible to the noise interference"},
    {"edge_id": "RM9DUXE2_E068", "edge_description": "bearing induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E069", "edge_description": "bearing induces_problem susceptible to the noise interference"},
    {"edge_id": "RM9DUXE2_E070", "edge_description": "shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E071", "edge_description": "shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm induces_problem susceptible to the noise interference"},
    {"edge_id": "RM9DUXE2_E072", "edge_description": "normal clearance state, slight worn, medium worn and severe worn induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E073", "edge_description": "normal clearance state, slight worn, medium worn and severe worn induces_problem susceptible to the noise interference"},
    {"edge_id": "RM9DUXE2_E074", "edge_description": "No Compound Fault induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E075", "edge_description": "No Compound Fault induces_problem susceptible to the noise interference"},
    {"edge_id": "RM9DUXE2_E076", "edge_description": "fault diagnosis induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E077", "edge_description": "fault diagnosis induces_problem susceptible to the noise interference"},
    {"edge_id": "RM9DUXE2_E078", "edge_description": "100 vibration signal samples selected from each bearing clearance states ... 60 were used as training samples induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E079", "edge_description": "100 vibration signal samples selected from each bearing clearance states ... 60 were used as training samples induces_problem susceptible to the noise interference"},
    {"edge_id": "RM9DUXE2_E080", "edge_description": "The original signal of mechanical system is susceptible to the noise interference induces_problem nonlinearity, nonstationarity and multi-component coupling characteristics"},
    {"edge_id": "RM9DUXE2_E081", "edge_description": "The original signal of mechanical system is susceptible to the noise interference induces_problem susceptible to the noise interference"}
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
| 1 | `RM9DUXE2_E049` | `contains` | 01-Object Domain | petroleum and chemical production processes(Industrial) |  | 02-Object Type | reciprocating compressor |  |
| 2 | `RM9DUXE2_E050` | `contains` | 01-Object Domain | petroleum and chemical production processes(Industrial) |  | 02-Object Type | bearing |  |
| 3 | `RM9DUXE2_E051` | `contains` | 02-Object Type | reciprocating compressor |  | 04-Fault Location | bearing |  |
| 4 | `RM9DUXE2_E052` | `contains` | 02-Object Type | bearing |  | 04-Fault Location | bearing |  |
| 5 | `RM9DUXE2_E053` | `contains` | 02-Object Type | reciprocating compressor |  | 03-Operating Conditions | shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm(Single Condition) |  |
| 6 | `RM9DUXE2_E054` | `contains` | 02-Object Type | bearing |  | 03-Operating Conditions | shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm(Single Condition) |  |
| 7 | `RM9DUXE2_E061` | `contains_phm_task` | 02-Object Type | reciprocating compressor |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 8 | `RM9DUXE2_E062` | `contains_phm_task` | 02-Object Type | bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 9 | `RM9DUXE2_E066` | `induces_problem` | 02-Object Type | reciprocating compressor |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 10 | `RM9DUXE2_E067` | `induces_problem` | 02-Object Type | reciprocating compressor |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |
| 11 | `RM9DUXE2_E068` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 12 | `RM9DUXE2_E069` | `induces_problem` | 02-Object Type | bearing |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |
| 13 | `RM9DUXE2_E070` | `induces_problem` | 03-Operating Conditions | shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm(Single Condition) |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 14 | `RM9DUXE2_E071` | `induces_problem` | 03-Operating Conditions | shaft power of 500 kW, a piston stroke of 240 mm and a motor speed of 496 rpm(Single Condition) |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |
| 15 | `RM9DUXE2_E072` | `induces_problem` | 06-Fault Severity | normal clearance state, slight worn, medium worn and severe worn(Multiple Severities) |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 16 | `RM9DUXE2_E073` | `induces_problem` | 06-Fault Severity | normal clearance state, slight worn, medium worn and severe worn(Multiple Severities) |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |
| 17 | `RM9DUXE2_E074` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 18 | `RM9DUXE2_E075` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |
| 19 | `RM9DUXE2_E076` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 20 | `RM9DUXE2_E077` | `induces_problem` | 08-PHM Task | fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |
| 21 | `RM9DUXE2_E078` | `induces_problem` | 12-Training Data Availability | 100 vibration signal samples selected from each bearing clearance states ... 60 were used as training samples(Sufficient) |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 22 | `RM9DUXE2_E079` | `induces_problem` | 12-Training Data Availability | 100 vibration signal samples selected from each bearing clearance states ... 60 were used as training samples(Sufficient) |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |
| 23 | `RM9DUXE2_E080` | `induces_problem` | 13-Noise Level | The original signal of mechanical system is susceptible to the noise interference(High Noise) |  | 09-Problem Scenario | nonlinearity, nonstationarity and multi-component coupling characteristics(Complex Systems) |  |
| 24 | `RM9DUXE2_E081` | `induces_problem` | 13-Noise Level | The original signal of mechanical system is susceptible to the noise interference(High Noise) |  | 09-Problem Scenario | susceptible to the noise interference(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 24 edges)*
