# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：WJGJ3ZKC
- **Paper Title**：Demodulation for hydraulic pump fault signals based on local mean decomposition and improved adaptive multiscale morphology analysis
- **Number of Candidate Edges to Judge**：25 

---

## II. LLM Input

> **Input Material**: Reference ID `WJGJ3ZKC`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "WJGJ3ZKC_E050", "edge_description": "swash plate axial plunger pump contains slipper"},
    {"edge_id": "WJGJ3ZKC_E051", "edge_description": "swash plate axial plunger pump contains center spring"},
    {"edge_id": "WJGJ3ZKC_E053", "edge_description": "wear contains No Compound Fault"},
    {"edge_id": "WJGJ3ZKC_E054", "edge_description": "loose contains No Compound Fault"},
    {"edge_id": "WJGJ3ZKC_E055", "edge_description": "vibration sensor is collected on slipper"},
    {"edge_id": "WJGJ3ZKC_E056", "edge_description": "vibration sensor is collected on center spring"},
    {"edge_id": "WJGJ3ZKC_E057", "edge_description": "vibration sensor can obviously reflect wear"},
    {"edge_id": "WJGJ3ZKC_E058", "edge_description": "vibration sensor can obviously reflect loose"},
    {"edge_id": "WJGJ3ZKC_E060", "edge_description": "slipper has_fault_mode wear"},
    {"edge_id": "WJGJ3ZKC_E061", "edge_description": "slipper has_fault_mode loose"},
    {"edge_id": "WJGJ3ZKC_E062", "edge_description": "center spring has_fault_mode wear"},
    {"edge_id": "WJGJ3ZKC_E063", "edge_description": "center spring has_fault_mode loose"},
    {"edge_id": "WJGJ3ZKC_E064", "edge_description": "wear contains Single Severity"},
    {"edge_id": "WJGJ3ZKC_E065", "edge_description": "loose contains Single Severity"},
    {"edge_id": "WJGJ3ZKC_E067", "edge_description": "slipper contains_phm_task Fault diagnosis of hydraulic pump"},
    {"edge_id": "WJGJ3ZKC_E068", "edge_description": "center spring contains_phm_task Fault diagnosis of hydraulic pump"},
    {"edge_id": "WJGJ3ZKC_E069", "edge_description": "wear contains_phm_task Fault diagnosis of hydraulic pump"},
    {"edge_id": "WJGJ3ZKC_E070", "edge_description": "loose contains_phm_task Fault diagnosis of hydraulic pump"},
    {"edge_id": "WJGJ3ZKC_E072", "edge_description": "swash plate axial plunger pump induces_problem susceptible to noises"},
    {"edge_id": "WJGJ3ZKC_E073", "edge_description": "exit pressure of 15 MPa and rotational speed of 1470 r/min induces_problem susceptible to noises"},
    {"edge_id": "WJGJ3ZKC_E074", "edge_description": "Single Severity induces_problem susceptible to noises"},
    {"edge_id": "WJGJ3ZKC_E075", "edge_description": "No Compound Fault induces_problem susceptible to noises"},
    {"edge_id": "WJGJ3ZKC_E076", "edge_description": "Fault diagnosis of hydraulic pump induces_problem susceptible to noises"},
    {"edge_id": "WJGJ3ZKC_E077", "edge_description": "Sufficient induces_problem susceptible to noises"},
    {"edge_id": "WJGJ3ZKC_E078", "edge_description": "noises induces_problem susceptible to noises"}
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
| 1 | `WJGJ3ZKC_E050` | `contains` | 02-Object Type | swash plate axial plunger pump |  | 04-Fault Location | slipper |  |
| 2 | `WJGJ3ZKC_E051` | `contains` | 02-Object Type | swash plate axial plunger pump |  | 04-Fault Location | center spring |  |
| 3 | `WJGJ3ZKC_E053` | `contains` | 05-Fault Mode | wear |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `WJGJ3ZKC_E054` | `contains` | 05-Fault Mode | loose |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `WJGJ3ZKC_E055` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | slipper |  |
| 6 | `WJGJ3ZKC_E056` | `is collected on` | 11-Sensor Information | vibration sensor |  | 04-Fault Location | center spring |  |
| 7 | `WJGJ3ZKC_E057` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | wear |  |
| 8 | `WJGJ3ZKC_E058` | `can obviously reflect` | 11-Sensor Information | vibration sensor |  | 05-Fault Mode | loose |  |
| 9 | `WJGJ3ZKC_E060` | `has_fault_mode` | 04-Fault Location | slipper |  | 05-Fault Mode | wear |  |
| 10 | `WJGJ3ZKC_E061` | `has_fault_mode` | 04-Fault Location | slipper |  | 05-Fault Mode | loose |  |
| 11 | `WJGJ3ZKC_E062` | `has_fault_mode` | 04-Fault Location | center spring |  | 05-Fault Mode | wear |  |
| 12 | `WJGJ3ZKC_E063` | `has_fault_mode` | 04-Fault Location | center spring |  | 05-Fault Mode | loose |  |
| 13 | `WJGJ3ZKC_E064` | `contains` | 05-Fault Mode | wear |  | 06-Fault Severity | Single Severity |  |
| 14 | `WJGJ3ZKC_E065` | `contains` | 05-Fault Mode | loose |  | 06-Fault Severity | Single Severity |  |
| 15 | `WJGJ3ZKC_E067` | `contains_phm_task` | 04-Fault Location | slipper |  | 08-PHM Task | Fault diagnosis of hydraulic pump(Diagnosis Task) |  |
| 16 | `WJGJ3ZKC_E068` | `contains_phm_task` | 04-Fault Location | center spring |  | 08-PHM Task | Fault diagnosis of hydraulic pump(Diagnosis Task) |  |
| 17 | `WJGJ3ZKC_E069` | `contains_phm_task` | 05-Fault Mode | wear |  | 08-PHM Task | Fault diagnosis of hydraulic pump(Diagnosis Task) |  |
| 18 | `WJGJ3ZKC_E070` | `contains_phm_task` | 05-Fault Mode | loose |  | 08-PHM Task | Fault diagnosis of hydraulic pump(Diagnosis Task) |  |
| 19 | `WJGJ3ZKC_E072` | `induces_problem` | 02-Object Type | swash plate axial plunger pump |  | 09-Problem Scenario | susceptible to noises(Uncertainty) |  |
| 20 | `WJGJ3ZKC_E073` | `induces_problem` | 03-Operating Conditions | exit pressure of 15 MPa and rotational speed of 1470 r/min(Single Condition) |  | 09-Problem Scenario | susceptible to noises(Uncertainty) |  |
| 21 | `WJGJ3ZKC_E074` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | susceptible to noises(Uncertainty) |  |
| 22 | `WJGJ3ZKC_E075` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | susceptible to noises(Uncertainty) |  |
| 23 | `WJGJ3ZKC_E076` | `induces_problem` | 08-PHM Task | Fault diagnosis of hydraulic pump(Diagnosis Task) |  | 09-Problem Scenario | susceptible to noises(Uncertainty) |  |
| 24 | `WJGJ3ZKC_E077` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | susceptible to noises(Uncertainty) |  |
| 25 | `WJGJ3ZKC_E078` | `induces_problem` | 13-Noise Level | noises(High Noise) |  | 09-Problem Scenario | susceptible to noises(Uncertainty) |  |

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

### ▶ For `can obviously reflect` (Sensor Information type → Fault Mode type)

**Very High Standard**: All of the following **conditions must be met** to be judged as "existing":
1. The paper explicitly states that the sensor **collects** data of this fault mode (i.e., the sensor appears in the fault data acquisition scenario)
2. The paper explicitly states that the sensor can **directly reflect/characterize** the physical features of this fault
3. The mere appearance of the sensor and fault mode in the dataset description is **insufficient** for judgment — the sensor must play an active role in the research method
**Trap to Watch Out For**: The mere appearance of the sensor and fault mode as dataset description does not equal the existence of a causal chain
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses a sensor→fault-feature causal relation, rather than exact matching of English phrases

### ▶ For `is collected on` (Sensor Information type → Fault Location type)

**High Standard**: The paper must explicitly express that the sensor is **physically installed/arranged on** the target fault location, i.e., there is a description of the **physical positional relationship** between the sensor and the fault location.
The mere appearance in the dataset description of "a sensor used for a certain fault" is insufficient — the physical arrangement or installation context of the sensor must be reflected
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the relationship between the physical installation position of the sensor and the fault location, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 25 edges)*
