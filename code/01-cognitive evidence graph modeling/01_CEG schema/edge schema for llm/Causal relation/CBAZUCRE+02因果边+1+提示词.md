# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：CBAZUCRE
- **Paper Title**：Multi-Physics Graphical Model-Based Fault Detection and Isolation in Wind Turbines
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `CBAZUCRE`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "CBAZUCRE_E061", "edge_description": "Wind Energy / Wind Turbines contains Doubly-Fed Induction Generator"},
    {"edge_id": "CBAZUCRE_E062", "edge_description": "Wind Energy / Wind Turbines contains Gearbox and drive-train"},
    {"edge_id": "CBAZUCRE_E063", "edge_description": "Wind Energy / Wind Turbines contains Hydraulic pitch actuator"},
    {"edge_id": "CBAZUCRE_E064", "edge_description": "Wind Energy / Wind Turbines contains AC/DC/AC back-to-back power converter"},
    {"edge_id": "CBAZUCRE_E065", "edge_description": "Doubly-Fed Induction Generator contains rotor windings"},
    {"edge_id": "CBAZUCRE_E066", "edge_description": "Doubly-Fed Induction Generator contains switches of power converter"},
    {"edge_id": "CBAZUCRE_E067", "edge_description": "Doubly-Fed Induction Generator contains DC-Link capacitor"},
    {"edge_id": "CBAZUCRE_E068", "edge_description": "Doubly-Fed Induction Generator contains hydraulic pitch actuator"},
    {"edge_id": "CBAZUCRE_E069", "edge_description": "Doubly-Fed Induction Generator contains gear connected to LSS"},
    {"edge_id": "CBAZUCRE_E070", "edge_description": "Gearbox and drive-train contains rotor windings"},
    {"edge_id": "CBAZUCRE_E071", "edge_description": "Gearbox and drive-train contains switches of power converter"},
    {"edge_id": "CBAZUCRE_E072", "edge_description": "Gearbox and drive-train contains DC-Link capacitor"},
    {"edge_id": "CBAZUCRE_E073", "edge_description": "Gearbox and drive-train contains hydraulic pitch actuator"},
    {"edge_id": "CBAZUCRE_E074", "edge_description": "Gearbox and drive-train contains gear connected to LSS"},
    {"edge_id": "CBAZUCRE_E075", "edge_description": "Hydraulic pitch actuator contains rotor windings"},
    {"edge_id": "CBAZUCRE_E076", "edge_description": "Hydraulic pitch actuator contains switches of power converter"},
    {"edge_id": "CBAZUCRE_E077", "edge_description": "Hydraulic pitch actuator contains DC-Link capacitor"},
    {"edge_id": "CBAZUCRE_E078", "edge_description": "Hydraulic pitch actuator contains hydraulic pitch actuator"},
    {"edge_id": "CBAZUCRE_E079", "edge_description": "Hydraulic pitch actuator contains gear connected to LSS"},
    {"edge_id": "CBAZUCRE_E080", "edge_description": "AC/DC/AC back-to-back power converter contains rotor windings"},
    {"edge_id": "CBAZUCRE_E081", "edge_description": "AC/DC/AC back-to-back power converter contains switches of power converter"},
    {"edge_id": "CBAZUCRE_E082", "edge_description": "AC/DC/AC back-to-back power converter contains DC-Link capacitor"},
    {"edge_id": "CBAZUCRE_E083", "edge_description": "AC/DC/AC back-to-back power converter contains hydraulic pitch actuator"},
    {"edge_id": "CBAZUCRE_E084", "edge_description": "AC/DC/AC back-to-back power converter contains gear connected to LSS"},
    {"edge_id": "CBAZUCRE_E085", "edge_description": "Doubly-Fed Induction Generator contains hybrid dynamical system under wind speed excitation and maximum power point tracking control"},
    {"edge_id": "CBAZUCRE_E086", "edge_description": "Gearbox and drive-train contains hybrid dynamical system under wind speed excitation and maximum power point tracking control"},
    {"edge_id": "CBAZUCRE_E087", "edge_description": "Hydraulic pitch actuator contains hybrid dynamical system under wind speed excitation and maximum power point tracking control"},
    {"edge_id": "CBAZUCRE_E088", "edge_description": "AC/DC/AC back-to-back power converter contains hybrid dynamical system under wind speed excitation and maximum power point tracking control"},
    {"edge_id": "CBAZUCRE_E089", "edge_description": "inter-turn short circuit contains No Compound Fault"},
    {"edge_id": "CBAZUCRE_E090", "edge_description": "open circuit fault contains No Compound Fault"}
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
| 1 | `CBAZUCRE_E061` | `contains` | 01-Object Domain | Wind Energy / Wind Turbines(Industrial) |  | 02-Object Type | Doubly-Fed Induction Generator |  |
| 2 | `CBAZUCRE_E062` | `contains` | 01-Object Domain | Wind Energy / Wind Turbines(Industrial) |  | 02-Object Type | Gearbox and drive-train |  |
| 3 | `CBAZUCRE_E063` | `contains` | 01-Object Domain | Wind Energy / Wind Turbines(Industrial) |  | 02-Object Type | Hydraulic pitch actuator |  |
| 4 | `CBAZUCRE_E064` | `contains` | 01-Object Domain | Wind Energy / Wind Turbines(Industrial) |  | 02-Object Type | AC/DC/AC back-to-back power converter |  |
| 5 | `CBAZUCRE_E065` | `contains` | 02-Object Type | Doubly-Fed Induction Generator |  | 04-Fault Location | rotor windings |  |
| 6 | `CBAZUCRE_E066` | `contains` | 02-Object Type | Doubly-Fed Induction Generator |  | 04-Fault Location | switches of power converter |  |
| 7 | `CBAZUCRE_E067` | `contains` | 02-Object Type | Doubly-Fed Induction Generator |  | 04-Fault Location | DC-Link capacitor |  |
| 8 | `CBAZUCRE_E068` | `contains` | 02-Object Type | Doubly-Fed Induction Generator |  | 04-Fault Location | hydraulic pitch actuator |  |
| 9 | `CBAZUCRE_E069` | `contains` | 02-Object Type | Doubly-Fed Induction Generator |  | 04-Fault Location | gear connected to LSS |  |
| 10 | `CBAZUCRE_E070` | `contains` | 02-Object Type | Gearbox and drive-train |  | 04-Fault Location | rotor windings |  |
| 11 | `CBAZUCRE_E071` | `contains` | 02-Object Type | Gearbox and drive-train |  | 04-Fault Location | switches of power converter |  |
| 12 | `CBAZUCRE_E072` | `contains` | 02-Object Type | Gearbox and drive-train |  | 04-Fault Location | DC-Link capacitor |  |
| 13 | `CBAZUCRE_E073` | `contains` | 02-Object Type | Gearbox and drive-train |  | 04-Fault Location | hydraulic pitch actuator |  |
| 14 | `CBAZUCRE_E074` | `contains` | 02-Object Type | Gearbox and drive-train |  | 04-Fault Location | gear connected to LSS |  |
| 15 | `CBAZUCRE_E075` | `contains` | 02-Object Type | Hydraulic pitch actuator |  | 04-Fault Location | rotor windings |  |
| 16 | `CBAZUCRE_E076` | `contains` | 02-Object Type | Hydraulic pitch actuator |  | 04-Fault Location | switches of power converter |  |
| 17 | `CBAZUCRE_E077` | `contains` | 02-Object Type | Hydraulic pitch actuator |  | 04-Fault Location | DC-Link capacitor |  |
| 18 | `CBAZUCRE_E078` | `contains` | 02-Object Type | Hydraulic pitch actuator |  | 04-Fault Location | hydraulic pitch actuator |  |
| 19 | `CBAZUCRE_E079` | `contains` | 02-Object Type | Hydraulic pitch actuator |  | 04-Fault Location | gear connected to LSS |  |
| 20 | `CBAZUCRE_E080` | `contains` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 04-Fault Location | rotor windings |  |
| 21 | `CBAZUCRE_E081` | `contains` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 04-Fault Location | switches of power converter |  |
| 22 | `CBAZUCRE_E082` | `contains` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 04-Fault Location | DC-Link capacitor |  |
| 23 | `CBAZUCRE_E083` | `contains` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 04-Fault Location | hydraulic pitch actuator |  |
| 24 | `CBAZUCRE_E084` | `contains` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 04-Fault Location | gear connected to LSS |  |
| 25 | `CBAZUCRE_E085` | `contains` | 02-Object Type | Doubly-Fed Induction Generator |  | 03-Operating Conditions | hybrid dynamical system under wind speed excitation and maximum power point tracking control(Variable Conditions) |  |
| 26 | `CBAZUCRE_E086` | `contains` | 02-Object Type | Gearbox and drive-train |  | 03-Operating Conditions | hybrid dynamical system under wind speed excitation and maximum power point tracking control(Variable Conditions) |  |
| 27 | `CBAZUCRE_E087` | `contains` | 02-Object Type | Hydraulic pitch actuator |  | 03-Operating Conditions | hybrid dynamical system under wind speed excitation and maximum power point tracking control(Variable Conditions) |  |
| 28 | `CBAZUCRE_E088` | `contains` | 02-Object Type | AC/DC/AC back-to-back power converter |  | 03-Operating Conditions | hybrid dynamical system under wind speed excitation and maximum power point tracking control(Variable Conditions) |  |
| 29 | `CBAZUCRE_E089` | `contains` | 05-Fault Mode | inter-turn short circuit |  | 07-Compound Fault | No Compound Fault |  |
| 30 | `CBAZUCRE_E090` | `contains` | 05-Fault Mode | open circuit fault |  | 07-Compound Fault | No Compound Fault |  |

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
