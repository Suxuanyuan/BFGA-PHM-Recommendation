# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：PDECHWK4
- **Paper Title**：Ground Fault Detection Method for Variable Speed Drives
- **Number of Candidate Edges to Judge**：19 

---

## II. LLM Input

> **Input Material**: Reference ID `PDECHWK4`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "PDECHWK4_E076", "edge_description": "Variable speed drive induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E077", "edge_description": "Power converter induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E078", "edge_description": "Power converter induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E079", "edge_description": "Main power transformer induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E080", "edge_description": "Main power transformer induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E081", "edge_description": "Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E082", "edge_description": "Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E083", "edge_description": "ground fault resistance (Rf) induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E084", "edge_description": "ground fault resistance (Rf) induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E085", "edge_description": "No Compound Fault induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E086", "edge_description": "No Compound Fault induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E087", "edge_description": "Ground fault detection induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E088", "edge_description": "Ground fault detection induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E089", "edge_description": "Not applicable induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E090", "edge_description": "Not applicable induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E091", "edge_description": "high frequency noises induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E092", "edge_description": "high frequency noises induces_problem High ground fault resistance"},
    {"edge_id": "PDECHWK4_E093", "edge_description": "Not mentioned induces_problem Ground fault detection across different stages of variable speed drives"},
    {"edge_id": "PDECHWK4_E094", "edge_description": "Not mentioned induces_problem High ground fault resistance"}
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
| 1 | `PDECHWK4_E076` | `induces_problem` | 02-Object Type | Variable speed drive |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 2 | `PDECHWK4_E077` | `induces_problem` | 02-Object Type | Power converter |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 3 | `PDECHWK4_E078` | `induces_problem` | 02-Object Type | Power converter |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 4 | `PDECHWK4_E079` | `induces_problem` | 02-Object Type | Main power transformer |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 5 | `PDECHWK4_E080` | `induces_problem` | 02-Object Type | Main power transformer |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 6 | `PDECHWK4_E081` | `induces_problem` | 03-Operating Conditions | Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency(Single Condition) |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 7 | `PDECHWK4_E082` | `induces_problem` | 03-Operating Conditions | Variable frequency (f1’ = 25 Hz), 50 Hz grid frequency(Single Condition) |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 8 | `PDECHWK4_E083` | `induces_problem` | 06-Fault Severity | ground fault resistance (Rf)(Multiple Severities) |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 9 | `PDECHWK4_E084` | `induces_problem` | 06-Fault Severity | ground fault resistance (Rf)(Multiple Severities) |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 10 | `PDECHWK4_E085` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 11 | `PDECHWK4_E086` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 12 | `PDECHWK4_E087` | `induces_problem` | 08-PHM Task | Ground fault detection(Detection Task) |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 13 | `PDECHWK4_E088` | `induces_problem` | 08-PHM Task | Ground fault detection(Detection Task) |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 14 | `PDECHWK4_E089` | `induces_problem` | 12-Training Data Availability | Not applicable(Sufficient) |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 15 | `PDECHWK4_E090` | `induces_problem` | 12-Training Data Availability | Not applicable(Sufficient) |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 16 | `PDECHWK4_E091` | `induces_problem` | 13-Noise Level | high frequency noises(High Noise) |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 17 | `PDECHWK4_E092` | `induces_problem` | 13-Noise Level | high frequency noises(High Noise) |  | 09-Problem Scenario | High ground fault resistance(Other) |  |
| 18 | `PDECHWK4_E093` | `induces_problem` | 14-Computational Resource | Not mentioned |  | 09-Problem Scenario | Ground fault detection across different stages of variable speed drives(Complex Systems) |  |
| 19 | `PDECHWK4_E094` | `induces_problem` | 14-Computational Resource | Not mentioned |  | 09-Problem Scenario | High ground fault resistance(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 19 edges)*
