# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：HK5DWGTC
- **Paper Title**：Bidirectional deep recurrent neural networks for process fault classification
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `HK5DWGTC`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "HK5DWGTC_E059", "edge_description": "industrial processes / chemical processes contains reactor"},
    {"edge_id": "HK5DWGTC_E060", "edge_description": "industrial processes / chemical processes contains condenser"},
    {"edge_id": "HK5DWGTC_E061", "edge_description": "industrial processes / chemical processes contains compressor"},
    {"edge_id": "HK5DWGTC_E062", "edge_description": "industrial processes / chemical processes contains separator"},
    {"edge_id": "HK5DWGTC_E063", "edge_description": "industrial processes / chemical processes contains stripper"},
    {"edge_id": "HK5DWGTC_E064", "edge_description": "reactor contains reactor"},
    {"edge_id": "HK5DWGTC_E065", "edge_description": "reactor contains condenser"},
    {"edge_id": "HK5DWGTC_E066", "edge_description": "reactor contains valve"},
    {"edge_id": "HK5DWGTC_E067", "edge_description": "reactor contains feed line"},
    {"edge_id": "HK5DWGTC_E068", "edge_description": "condenser contains reactor"},
    {"edge_id": "HK5DWGTC_E069", "edge_description": "condenser contains condenser"},
    {"edge_id": "HK5DWGTC_E070", "edge_description": "condenser contains valve"},
    {"edge_id": "HK5DWGTC_E071", "edge_description": "condenser contains feed line"},
    {"edge_id": "HK5DWGTC_E072", "edge_description": "compressor contains reactor"},
    {"edge_id": "HK5DWGTC_E073", "edge_description": "compressor contains condenser"},
    {"edge_id": "HK5DWGTC_E074", "edge_description": "compressor contains valve"},
    {"edge_id": "HK5DWGTC_E075", "edge_description": "compressor contains feed line"},
    {"edge_id": "HK5DWGTC_E076", "edge_description": "separator contains reactor"},
    {"edge_id": "HK5DWGTC_E077", "edge_description": "separator contains condenser"},
    {"edge_id": "HK5DWGTC_E078", "edge_description": "separator contains valve"},
    {"edge_id": "HK5DWGTC_E079", "edge_description": "separator contains feed line"},
    {"edge_id": "HK5DWGTC_E080", "edge_description": "stripper contains reactor"},
    {"edge_id": "HK5DWGTC_E081", "edge_description": "stripper contains condenser"},
    {"edge_id": "HK5DWGTC_E082", "edge_description": "stripper contains valve"},
    {"edge_id": "HK5DWGTC_E083", "edge_description": "stripper contains feed line"},
    {"edge_id": "HK5DWGTC_E084", "edge_description": "reactor contains closed loop condition"},
    {"edge_id": "HK5DWGTC_E085", "edge_description": "condenser contains closed loop condition"},
    {"edge_id": "HK5DWGTC_E086", "edge_description": "compressor contains closed loop condition"},
    {"edge_id": "HK5DWGTC_E087", "edge_description": "separator contains closed loop condition"},
    {"edge_id": "HK5DWGTC_E088", "edge_description": "stripper contains closed loop condition"}
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
| 1 | `HK5DWGTC_E059` | `contains` | 01-Object Domain | industrial processes / chemical processes(Industrial) |  | 02-Object Type | reactor |  |
| 2 | `HK5DWGTC_E060` | `contains` | 01-Object Domain | industrial processes / chemical processes(Industrial) |  | 02-Object Type | condenser |  |
| 3 | `HK5DWGTC_E061` | `contains` | 01-Object Domain | industrial processes / chemical processes(Industrial) |  | 02-Object Type | compressor |  |
| 4 | `HK5DWGTC_E062` | `contains` | 01-Object Domain | industrial processes / chemical processes(Industrial) |  | 02-Object Type | separator |  |
| 5 | `HK5DWGTC_E063` | `contains` | 01-Object Domain | industrial processes / chemical processes(Industrial) |  | 02-Object Type | stripper |  |
| 6 | `HK5DWGTC_E064` | `contains` | 02-Object Type | reactor |  | 04-Fault Location | reactor |  |
| 7 | `HK5DWGTC_E065` | `contains` | 02-Object Type | reactor |  | 04-Fault Location | condenser |  |
| 8 | `HK5DWGTC_E066` | `contains` | 02-Object Type | reactor |  | 04-Fault Location | valve |  |
| 9 | `HK5DWGTC_E067` | `contains` | 02-Object Type | reactor |  | 04-Fault Location | feed line |  |
| 10 | `HK5DWGTC_E068` | `contains` | 02-Object Type | condenser |  | 04-Fault Location | reactor |  |
| 11 | `HK5DWGTC_E069` | `contains` | 02-Object Type | condenser |  | 04-Fault Location | condenser |  |
| 12 | `HK5DWGTC_E070` | `contains` | 02-Object Type | condenser |  | 04-Fault Location | valve |  |
| 13 | `HK5DWGTC_E071` | `contains` | 02-Object Type | condenser |  | 04-Fault Location | feed line |  |
| 14 | `HK5DWGTC_E072` | `contains` | 02-Object Type | compressor |  | 04-Fault Location | reactor |  |
| 15 | `HK5DWGTC_E073` | `contains` | 02-Object Type | compressor |  | 04-Fault Location | condenser |  |
| 16 | `HK5DWGTC_E074` | `contains` | 02-Object Type | compressor |  | 04-Fault Location | valve |  |
| 17 | `HK5DWGTC_E075` | `contains` | 02-Object Type | compressor |  | 04-Fault Location | feed line |  |
| 18 | `HK5DWGTC_E076` | `contains` | 02-Object Type | separator |  | 04-Fault Location | reactor |  |
| 19 | `HK5DWGTC_E077` | `contains` | 02-Object Type | separator |  | 04-Fault Location | condenser |  |
| 20 | `HK5DWGTC_E078` | `contains` | 02-Object Type | separator |  | 04-Fault Location | valve |  |
| 21 | `HK5DWGTC_E079` | `contains` | 02-Object Type | separator |  | 04-Fault Location | feed line |  |
| 22 | `HK5DWGTC_E080` | `contains` | 02-Object Type | stripper |  | 04-Fault Location | reactor |  |
| 23 | `HK5DWGTC_E081` | `contains` | 02-Object Type | stripper |  | 04-Fault Location | condenser |  |
| 24 | `HK5DWGTC_E082` | `contains` | 02-Object Type | stripper |  | 04-Fault Location | valve |  |
| 25 | `HK5DWGTC_E083` | `contains` | 02-Object Type | stripper |  | 04-Fault Location | feed line |  |
| 26 | `HK5DWGTC_E084` | `contains` | 02-Object Type | reactor |  | 03-Operating Conditions | closed loop condition(Single Condition) |  |
| 27 | `HK5DWGTC_E085` | `contains` | 02-Object Type | condenser |  | 03-Operating Conditions | closed loop condition(Single Condition) |  |
| 28 | `HK5DWGTC_E086` | `contains` | 02-Object Type | compressor |  | 03-Operating Conditions | closed loop condition(Single Condition) |  |
| 29 | `HK5DWGTC_E087` | `contains` | 02-Object Type | separator |  | 03-Operating Conditions | closed loop condition(Single Condition) |  |
| 30 | `HK5DWGTC_E088` | `contains` | 02-Object Type | stripper |  | 03-Operating Conditions | closed loop condition(Single Condition) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 30 edges)*
