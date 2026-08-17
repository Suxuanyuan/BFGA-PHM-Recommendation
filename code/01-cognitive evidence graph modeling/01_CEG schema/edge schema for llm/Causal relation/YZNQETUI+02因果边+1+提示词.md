# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：YZNQETUI
- **Paper Title**：Modeling and Diagnostic of Incipient Interturn Faults for a Three-Phase Permanent Magnet Synchronous Motor
- **Number of Candidate Edges to Judge**：12 

---

## II. LLM Input

> **Input Material**: Reference ID `YZNQETUI`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "YZNQETUI_E050", "edge_description": "Current probes is collected on stator end winding"},
    {"edge_id": "YZNQETUI_E051", "edge_description": "Voltage probes is collected on stator end winding"},
    {"edge_id": "YZNQETUI_E052", "edge_description": "Current probes can obviously reflect intermittent inter-turn short circuit"},
    {"edge_id": "YZNQETUI_E053", "edge_description": "Voltage probes can obviously reflect intermittent inter-turn short circuit"},
    {"edge_id": "YZNQETUI_E061", "edge_description": "permanent magnet synchronous motor induces_problem incipient inter-turn fault detection"},
    {"edge_id": "YZNQETUI_E062", "edge_description": "operating points (iqref = 3 A / 5 A, speed = 450 rpm / 1050 rpm) induces_problem incipient inter-turn fault detection"},
    {"edge_id": "YZNQETUI_E063", "edge_description": "50% of a stator phase winding induces_problem incipient inter-turn fault detection"},
    {"edge_id": "YZNQETUI_E064", "edge_description": "No Compound Fault induces_problem incipient inter-turn fault detection"},
    {"edge_id": "YZNQETUI_E065", "edge_description": "fault detection induces_problem incipient inter-turn fault detection"},
    {"edge_id": "YZNQETUI_E066", "edge_description": "learning period in order to record the detection threshold induces_problem incipient inter-turn fault detection"},
    {"edge_id": "YZNQETUI_E067", "edge_description": "measurement noise, ripples, sampling effects induces_problem incipient inter-turn fault detection"},
    {"edge_id": "YZNQETUI_E068", "edge_description": "online method induces_problem incipient inter-turn fault detection"}
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
| 1 | `YZNQETUI_E050` | `is collected on` | 11-Sensor Information | Current probes |  | 04-Fault Location | stator end winding |  |
| 2 | `YZNQETUI_E051` | `is collected on` | 11-Sensor Information | Voltage probes |  | 04-Fault Location | stator end winding |  |
| 3 | `YZNQETUI_E052` | `can obviously reflect` | 11-Sensor Information | Current probes |  | 05-Fault Mode | intermittent inter-turn short circuit |  |
| 4 | `YZNQETUI_E053` | `can obviously reflect` | 11-Sensor Information | Voltage probes |  | 05-Fault Mode | intermittent inter-turn short circuit |  |
| 5 | `YZNQETUI_E061` | `induces_problem` | 02-Object Type | permanent magnet synchronous motor |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |
| 6 | `YZNQETUI_E062` | `induces_problem` | 03-Operating Conditions | operating points (iqref = 3 A / 5 A, speed = 450 rpm / 1050 rpm)(Multiple Conditions) |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |
| 7 | `YZNQETUI_E063` | `induces_problem` | 06-Fault Severity | 50% of a stator phase winding(Single Severity) |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |
| 8 | `YZNQETUI_E064` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |
| 9 | `YZNQETUI_E065` | `induces_problem` | 08-PHM Task | fault detection(Detection Task) |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |
| 10 | `YZNQETUI_E066` | `induces_problem` | 12-Training Data Availability | learning period in order to record the detection threshold(Sufficient) |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |
| 11 | `YZNQETUI_E067` | `induces_problem` | 13-Noise Level | measurement noise, ripples, sampling effects(High Noise) |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |
| 12 | `YZNQETUI_E068` | `induces_problem` | 14-Computational Resource | online method(Low Resource Consumption) |  | 09-Problem Scenario | incipient inter-turn fault detection(Early Degradation Prediction) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 12 edges)*
