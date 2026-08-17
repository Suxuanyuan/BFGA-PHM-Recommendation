# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：EU3F5TIE
- **Paper Title**：A Comprehensive Monitoring System for Online Fault Diagnosis and Aging Detection of Non-Isolated DC-DC Converters' Components
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `EU3F5TIE`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "EU3F5TIE_E029", "edge_description": "industrial applications contains non-isolated DC-DC converter"},
    {"edge_id": "EU3F5TIE_E030", "edge_description": "industrial applications contains power switch"},
    {"edge_id": "EU3F5TIE_E031", "edge_description": "industrial applications contains diode"},
    {"edge_id": "EU3F5TIE_E032", "edge_description": "industrial applications contains electrolytic capacitor"},
    {"edge_id": "EU3F5TIE_E033", "edge_description": "industrial applications contains inductor"},
    {"edge_id": "EU3F5TIE_E034", "edge_description": "non-isolated DC-DC converter contains power switch"},
    {"edge_id": "EU3F5TIE_E035", "edge_description": "non-isolated DC-DC converter contains diode"},
    {"edge_id": "EU3F5TIE_E036", "edge_description": "non-isolated DC-DC converter contains capacitor"},
    {"edge_id": "EU3F5TIE_E037", "edge_description": "non-isolated DC-DC converter contains inductor"},
    {"edge_id": "EU3F5TIE_E038", "edge_description": "power switch contains power switch"},
    {"edge_id": "EU3F5TIE_E039", "edge_description": "power switch contains diode"},
    {"edge_id": "EU3F5TIE_E040", "edge_description": "power switch contains capacitor"},
    {"edge_id": "EU3F5TIE_E041", "edge_description": "power switch contains inductor"},
    {"edge_id": "EU3F5TIE_E042", "edge_description": "diode contains power switch"},
    {"edge_id": "EU3F5TIE_E043", "edge_description": "diode contains diode"},
    {"edge_id": "EU3F5TIE_E044", "edge_description": "diode contains capacitor"},
    {"edge_id": "EU3F5TIE_E045", "edge_description": "diode contains inductor"},
    {"edge_id": "EU3F5TIE_E046", "edge_description": "electrolytic capacitor contains power switch"},
    {"edge_id": "EU3F5TIE_E047", "edge_description": "electrolytic capacitor contains diode"},
    {"edge_id": "EU3F5TIE_E048", "edge_description": "electrolytic capacitor contains capacitor"},
    {"edge_id": "EU3F5TIE_E049", "edge_description": "electrolytic capacitor contains inductor"},
    {"edge_id": "EU3F5TIE_E050", "edge_description": "inductor contains power switch"},
    {"edge_id": "EU3F5TIE_E051", "edge_description": "inductor contains diode"},
    {"edge_id": "EU3F5TIE_E052", "edge_description": "inductor contains capacitor"},
    {"edge_id": "EU3F5TIE_E053", "edge_description": "inductor contains inductor"},
    {"edge_id": "EU3F5TIE_E054", "edge_description": "non-isolated DC-DC converter contains different operating conditions including variations of frequency and temperature"},
    {"edge_id": "EU3F5TIE_E055", "edge_description": "power switch contains different operating conditions including variations of frequency and temperature"},
    {"edge_id": "EU3F5TIE_E056", "edge_description": "diode contains different operating conditions including variations of frequency and temperature"},
    {"edge_id": "EU3F5TIE_E057", "edge_description": "electrolytic capacitor contains different operating conditions including variations of frequency and temperature"},
    {"edge_id": "EU3F5TIE_E058", "edge_description": "inductor contains different operating conditions including variations of frequency and temperature"}
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
| 1 | `EU3F5TIE_E029` | `contains` | 01-Object Domain | industrial applications(Industrial) |  | 02-Object Type | non-isolated DC-DC converter |  |
| 2 | `EU3F5TIE_E030` | `contains` | 01-Object Domain | industrial applications(Industrial) |  | 02-Object Type | power switch |  |
| 3 | `EU3F5TIE_E031` | `contains` | 01-Object Domain | industrial applications(Industrial) |  | 02-Object Type | diode |  |
| 4 | `EU3F5TIE_E032` | `contains` | 01-Object Domain | industrial applications(Industrial) |  | 02-Object Type | electrolytic capacitor |  |
| 5 | `EU3F5TIE_E033` | `contains` | 01-Object Domain | industrial applications(Industrial) |  | 02-Object Type | inductor |  |
| 6 | `EU3F5TIE_E034` | `contains` | 02-Object Type | non-isolated DC-DC converter |  | 04-Fault Location | power switch |  |
| 7 | `EU3F5TIE_E035` | `contains` | 02-Object Type | non-isolated DC-DC converter |  | 04-Fault Location | diode |  |
| 8 | `EU3F5TIE_E036` | `contains` | 02-Object Type | non-isolated DC-DC converter |  | 04-Fault Location | capacitor |  |
| 9 | `EU3F5TIE_E037` | `contains` | 02-Object Type | non-isolated DC-DC converter |  | 04-Fault Location | inductor |  |
| 10 | `EU3F5TIE_E038` | `contains` | 02-Object Type | power switch |  | 04-Fault Location | power switch |  |
| 11 | `EU3F5TIE_E039` | `contains` | 02-Object Type | power switch |  | 04-Fault Location | diode |  |
| 12 | `EU3F5TIE_E040` | `contains` | 02-Object Type | power switch |  | 04-Fault Location | capacitor |  |
| 13 | `EU3F5TIE_E041` | `contains` | 02-Object Type | power switch |  | 04-Fault Location | inductor |  |
| 14 | `EU3F5TIE_E042` | `contains` | 02-Object Type | diode |  | 04-Fault Location | power switch |  |
| 15 | `EU3F5TIE_E043` | `contains` | 02-Object Type | diode |  | 04-Fault Location | diode |  |
| 16 | `EU3F5TIE_E044` | `contains` | 02-Object Type | diode |  | 04-Fault Location | capacitor |  |
| 17 | `EU3F5TIE_E045` | `contains` | 02-Object Type | diode |  | 04-Fault Location | inductor |  |
| 18 | `EU3F5TIE_E046` | `contains` | 02-Object Type | electrolytic capacitor |  | 04-Fault Location | power switch |  |
| 19 | `EU3F5TIE_E047` | `contains` | 02-Object Type | electrolytic capacitor |  | 04-Fault Location | diode |  |
| 20 | `EU3F5TIE_E048` | `contains` | 02-Object Type | electrolytic capacitor |  | 04-Fault Location | capacitor |  |
| 21 | `EU3F5TIE_E049` | `contains` | 02-Object Type | electrolytic capacitor |  | 04-Fault Location | inductor |  |
| 22 | `EU3F5TIE_E050` | `contains` | 02-Object Type | inductor |  | 04-Fault Location | power switch |  |
| 23 | `EU3F5TIE_E051` | `contains` | 02-Object Type | inductor |  | 04-Fault Location | diode |  |
| 24 | `EU3F5TIE_E052` | `contains` | 02-Object Type | inductor |  | 04-Fault Location | capacitor |  |
| 25 | `EU3F5TIE_E053` | `contains` | 02-Object Type | inductor |  | 04-Fault Location | inductor |  |
| 26 | `EU3F5TIE_E054` | `contains` | 02-Object Type | non-isolated DC-DC converter |  | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  |
| 27 | `EU3F5TIE_E055` | `contains` | 02-Object Type | power switch |  | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  |
| 28 | `EU3F5TIE_E056` | `contains` | 02-Object Type | diode |  | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  |
| 29 | `EU3F5TIE_E057` | `contains` | 02-Object Type | electrolytic capacitor |  | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  |
| 30 | `EU3F5TIE_E058` | `contains` | 02-Object Type | inductor |  | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  |

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
