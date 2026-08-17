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
    {"edge_id": "EU3F5TIE_E120", "edge_description": "inter-turn fault contains_phm_task online fault diagnosis and aging monitoring"},
    {"edge_id": "EU3F5TIE_E122", "edge_description": "non-isolated DC-DC converter induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E123", "edge_description": "non-isolated DC-DC converter induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E124", "edge_description": "non-isolated DC-DC converter induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E125", "edge_description": "power switch induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E126", "edge_description": "power switch induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E127", "edge_description": "power switch induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E128", "edge_description": "diode induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E129", "edge_description": "diode induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E130", "edge_description": "diode induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E131", "edge_description": "electrolytic capacitor induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E132", "edge_description": "electrolytic capacitor induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E133", "edge_description": "electrolytic capacitor induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E134", "edge_description": "inductor induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E135", "edge_description": "inductor induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E136", "edge_description": "inductor induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E137", "edge_description": "different operating conditions including variations of frequency and temperature induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E138", "edge_description": "different operating conditions including variations of frequency and temperature induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E139", "edge_description": "different operating conditions including variations of frequency and temperature induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E140", "edge_description": "0.5 ohm resistor, 20% inductance reduction induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E141", "edge_description": "0.5 ohm resistor, 20% inductance reduction induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E142", "edge_description": "0.5 ohm resistor, 20% inductance reduction induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E143", "edge_description": "No Compound Fault induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E144", "edge_description": "No Compound Fault induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E145", "edge_description": "No Compound Fault induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E146", "edge_description": "online fault diagnosis and aging monitoring induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E147", "edge_description": "online fault diagnosis and aging monitoring induces_problem noise robustness and temperature-induced parameter drift"},
    {"edge_id": "EU3F5TIE_E148", "edge_description": "online fault diagnosis and aging monitoring induces_problem comprehensive multi-component monitoring with minimal sensors"},
    {"edge_id": "EU3F5TIE_E149", "edge_description": "N/A induces_problem aging detection and monitoring of capacitor and switch"},
    {"edge_id": "EU3F5TIE_E150", "edge_description": "N/A induces_problem noise robustness and temperature-induced parameter drift"}
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
| 1 | `EU3F5TIE_E120` | `contains_phm_task` | 05-Fault Mode | inter-turn fault |  | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  |
| 2 | `EU3F5TIE_E122` | `induces_problem` | 02-Object Type | non-isolated DC-DC converter |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 3 | `EU3F5TIE_E123` | `induces_problem` | 02-Object Type | non-isolated DC-DC converter |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 4 | `EU3F5TIE_E124` | `induces_problem` | 02-Object Type | non-isolated DC-DC converter |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 5 | `EU3F5TIE_E125` | `induces_problem` | 02-Object Type | power switch |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 6 | `EU3F5TIE_E126` | `induces_problem` | 02-Object Type | power switch |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 7 | `EU3F5TIE_E127` | `induces_problem` | 02-Object Type | power switch |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 8 | `EU3F5TIE_E128` | `induces_problem` | 02-Object Type | diode |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 9 | `EU3F5TIE_E129` | `induces_problem` | 02-Object Type | diode |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 10 | `EU3F5TIE_E130` | `induces_problem` | 02-Object Type | diode |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 11 | `EU3F5TIE_E131` | `induces_problem` | 02-Object Type | electrolytic capacitor |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 12 | `EU3F5TIE_E132` | `induces_problem` | 02-Object Type | electrolytic capacitor |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 13 | `EU3F5TIE_E133` | `induces_problem` | 02-Object Type | electrolytic capacitor |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 14 | `EU3F5TIE_E134` | `induces_problem` | 02-Object Type | inductor |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 15 | `EU3F5TIE_E135` | `induces_problem` | 02-Object Type | inductor |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 16 | `EU3F5TIE_E136` | `induces_problem` | 02-Object Type | inductor |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 17 | `EU3F5TIE_E137` | `induces_problem` | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 18 | `EU3F5TIE_E138` | `induces_problem` | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 19 | `EU3F5TIE_E139` | `induces_problem` | 03-Operating Conditions | different operating conditions including variations of frequency and temperature(Multiple Conditions) |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 20 | `EU3F5TIE_E140` | `induces_problem` | 06-Fault Severity | 0.5 ohm resistor, 20% inductance reduction(Single Severity) |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 21 | `EU3F5TIE_E141` | `induces_problem` | 06-Fault Severity | 0.5 ohm resistor, 20% inductance reduction(Single Severity) |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 22 | `EU3F5TIE_E142` | `induces_problem` | 06-Fault Severity | 0.5 ohm resistor, 20% inductance reduction(Single Severity) |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 23 | `EU3F5TIE_E143` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 24 | `EU3F5TIE_E144` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 25 | `EU3F5TIE_E145` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 26 | `EU3F5TIE_E146` | `induces_problem` | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 27 | `EU3F5TIE_E147` | `induces_problem` | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |
| 28 | `EU3F5TIE_E148` | `induces_problem` | 08-PHM Task | online fault diagnosis and aging monitoring(Diagnosis Task) |  | 09-Problem Scenario | comprehensive multi-component monitoring with minimal sensors(Other) |  |
| 29 | `EU3F5TIE_E149` | `induces_problem` | 12-Training Data Availability | N/A(Sufficient) |  | 09-Problem Scenario | aging detection and monitoring of capacitor and switch(Early Degradation Prediction) |  |
| 30 | `EU3F5TIE_E150` | `induces_problem` | 12-Training Data Availability | N/A(Sufficient) |  | 09-Problem Scenario | noise robustness and temperature-induced parameter drift(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 4, total 30 edges)*
