# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：BL5IIH2E
- **Paper Title**：Fault Diagnosis Research on Impact System of Hydraulic Rock Drill Based on Internal Mechanism Testing Method
- **Number of Candidate Edges to Judge**：21 

---

## II. LLM Input

> **Input Material**: Reference ID `BL5IIH2E`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "BL5IIH2E_E033", "edge_description": "mining, tunneling, and building industries contains hydraulic rock drill"},
    {"edge_id": "BL5IIH2E_E034", "edge_description": "mining, tunneling, and building industries contains impact piston"},
    {"edge_id": "BL5IIH2E_E035", "edge_description": "mining, tunneling, and building industries contains reversing valve"},
    {"edge_id": "BL5IIH2E_E036", "edge_description": "hydraulic rock drill contains reversing valve"},
    {"edge_id": "BL5IIH2E_E037", "edge_description": "impact piston contains reversing valve"},
    {"edge_id": "BL5IIH2E_E038", "edge_description": "reversing valve contains reversing valve"},
    {"edge_id": "BL5IIH2E_E039", "edge_description": "hydraulic rock drill contains inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa"},
    {"edge_id": "BL5IIH2E_E040", "edge_description": "impact piston contains inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa"},
    {"edge_id": "BL5IIH2E_E041", "edge_description": "reversing valve contains inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa"},
    {"edge_id": "BL5IIH2E_E048", "edge_description": "hydraulic rock drill contains_phm_task Fault Diagnosis"},
    {"edge_id": "BL5IIH2E_E049", "edge_description": "impact piston contains_phm_task Fault Diagnosis"},
    {"edge_id": "BL5IIH2E_E050", "edge_description": "reversing valve contains_phm_task Fault Diagnosis"},
    {"edge_id": "BL5IIH2E_E054", "edge_description": "hydraulic rock drill induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E055", "edge_description": "impact piston induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E056", "edge_description": "reversing valve induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E057", "edge_description": "inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E058", "edge_description": "impact frequency of about 36 Hz induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E059", "edge_description": "No Compound Fault induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E060", "edge_description": "Fault Diagnosis induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E061", "edge_description": "Sufficient induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"},
    {"edge_id": "BL5IIH2E_E062", "edge_description": "Normal induces_problem coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel"}
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
| 1 | `BL5IIH2E_E033` | `contains` | 01-Object Domain | mining, tunneling, and building industries(Industrial) |  | 02-Object Type | hydraulic rock drill |  |
| 2 | `BL5IIH2E_E034` | `contains` | 01-Object Domain | mining, tunneling, and building industries(Industrial) |  | 02-Object Type | impact piston |  |
| 3 | `BL5IIH2E_E035` | `contains` | 01-Object Domain | mining, tunneling, and building industries(Industrial) |  | 02-Object Type | reversing valve |  |
| 4 | `BL5IIH2E_E036` | `contains` | 02-Object Type | hydraulic rock drill |  | 04-Fault Location | reversing valve |  |
| 5 | `BL5IIH2E_E037` | `contains` | 02-Object Type | impact piston |  | 04-Fault Location | reversing valve |  |
| 6 | `BL5IIH2E_E038` | `contains` | 02-Object Type | reversing valve |  | 04-Fault Location | reversing valve |  |
| 7 | `BL5IIH2E_E039` | `contains` | 02-Object Type | hydraulic rock drill |  | 03-Operating Conditions | inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa(Single Condition) |  |
| 8 | `BL5IIH2E_E040` | `contains` | 02-Object Type | impact piston |  | 03-Operating Conditions | inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa(Single Condition) |  |
| 9 | `BL5IIH2E_E041` | `contains` | 02-Object Type | reversing valve |  | 03-Operating Conditions | inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa(Single Condition) |  |
| 10 | `BL5IIH2E_E048` | `contains_phm_task` | 02-Object Type | hydraulic rock drill |  | 08-PHM Task | Fault Diagnosis(Diagnosis Task) |  |
| 11 | `BL5IIH2E_E049` | `contains_phm_task` | 02-Object Type | impact piston |  | 08-PHM Task | Fault Diagnosis(Diagnosis Task) |  |
| 12 | `BL5IIH2E_E050` | `contains_phm_task` | 02-Object Type | reversing valve |  | 08-PHM Task | Fault Diagnosis(Diagnosis Task) |  |
| 13 | `BL5IIH2E_E054` | `induces_problem` | 02-Object Type | hydraulic rock drill |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 14 | `BL5IIH2E_E055` | `induces_problem` | 02-Object Type | impact piston |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 15 | `BL5IIH2E_E056` | `induces_problem` | 02-Object Type | reversing valve |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 16 | `BL5IIH2E_E057` | `induces_problem` | 03-Operating Conditions | inflow pressure of impact 20 MPa, propulsion pressure 6 MPa, load damping pressure 8 MPa(Single Condition) |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 17 | `BL5IIH2E_E058` | `induces_problem` | 06-Fault Severity | impact frequency of about 36 Hz(Single Severity) |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 18 | `BL5IIH2E_E059` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 19 | `BL5IIH2E_E060` | `induces_problem` | 08-PHM Task | Fault Diagnosis(Diagnosis Task) |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 20 | `BL5IIH2E_E061` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |
| 21 | `BL5IIH2E_E062` | `induces_problem` | 13-Noise Level | Normal |  | 09-Problem Scenario | coupling between the movement of the impact piston and the movement of the reversing valve, complicated inner channel(Complex Systems) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 21 edges)*
