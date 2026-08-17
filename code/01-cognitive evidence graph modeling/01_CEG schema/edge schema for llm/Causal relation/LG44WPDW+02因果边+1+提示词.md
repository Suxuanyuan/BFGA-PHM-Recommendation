# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：LG44WPDW
- **Paper Title**：An Effective Approach for Rotor Electrical Asymmetry Detection in Wind Turbine DFIGs
- **Number of Candidate Edges to Judge**：20 

---

## II. LLM Input

> **Input Material**: Reference ID `LG44WPDW`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "LG44WPDW_E037", "edge_description": "current sensor is collected on generator rotor"},
    {"edge_id": "LG44WPDW_E038", "edge_description": "speed sensor is collected on generator rotor"},
    {"edge_id": "LG44WPDW_E039", "edge_description": "current sensor can obviously reflect rotor electrical asymmetry"},
    {"edge_id": "LG44WPDW_E040", "edge_description": "speed sensor can obviously reflect rotor electrical asymmetry"},
    {"edge_id": "LG44WPDW_E048", "edge_description": "Doubly fed induction generator (DFIG) induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E049", "edge_description": "Doubly fed induction generator (DFIG) induces_problem Time-varying and nonstationary signal characteristics"},
    {"edge_id": "LG44WPDW_E050", "edge_description": "Time-varying generator speed and load conditions induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E051", "edge_description": "Time-varying generator speed and load conditions induces_problem Time-varying and nonstationary signal characteristics"},
    {"edge_id": "LG44WPDW_E052", "edge_description": "two levels of rotor unbalance of 23% and 46% induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E053", "edge_description": "two levels of rotor unbalance of 23% and 46% induces_problem Time-varying and nonstationary signal characteristics"},
    {"edge_id": "LG44WPDW_E054", "edge_description": "No Compound Fault induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E055", "edge_description": "No Compound Fault induces_problem Time-varying and nonstationary signal characteristics"},
    {"edge_id": "LG44WPDW_E056", "edge_description": "Rotor electrical asymmetry detection induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E057", "edge_description": "Rotor electrical asymmetry detection induces_problem Time-varying and nonstationary signal characteristics"},
    {"edge_id": "LG44WPDW_E058", "edge_description": "At each test, the test rig was run for a period of 150 s after which the 23% and 46% unbalance fault conditions were applied at 150 s and 300 s, respectively. ... sampling frequency of 5 kHz. induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E059", "edge_description": "At each test, the test rig was run for a period of 150 s after which the 23% and 46% unbalance fault conditions were applied at 150 s and 300 s, respectively. ... sampling frequency of 5 kHz. induces_problem Time-varying and nonstationary signal characteristics"},
    {"edge_id": "LG44WPDW_E060", "edge_description": "resulting in FSCs manifesting themselves in the vicinity of the supply frequency and its harmonics with extraneous noise induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E061", "edge_description": "resulting in FSCs manifesting themselves in the vicinity of the supply frequency and its harmonics with extraneous noise induces_problem Time-varying and nonstationary signal characteristics"},
    {"edge_id": "LG44WPDW_E062", "edge_description": "it is able to accurately detect fault frequencies with minimal computational requirements when compared with a CWT induces_problem FSCs merged with supply frequency harmonics and noise robustness"},
    {"edge_id": "LG44WPDW_E063", "edge_description": "it is able to accurately detect fault frequencies with minimal computational requirements when compared with a CWT induces_problem Time-varying and nonstationary signal characteristics"}
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
| 1 | `LG44WPDW_E037` | `is collected on` | 11-Sensor Information | current sensor |  | 04-Fault Location | generator rotor |  |
| 2 | `LG44WPDW_E038` | `is collected on` | 11-Sensor Information | speed sensor |  | 04-Fault Location | generator rotor |  |
| 3 | `LG44WPDW_E039` | `can obviously reflect` | 11-Sensor Information | current sensor |  | 05-Fault Mode | rotor electrical asymmetry |  |
| 4 | `LG44WPDW_E040` | `can obviously reflect` | 11-Sensor Information | speed sensor |  | 05-Fault Mode | rotor electrical asymmetry |  |
| 5 | `LG44WPDW_E048` | `induces_problem` | 02-Object Type | Doubly fed induction generator (DFIG) |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 6 | `LG44WPDW_E049` | `induces_problem` | 02-Object Type | Doubly fed induction generator (DFIG) |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |
| 7 | `LG44WPDW_E050` | `induces_problem` | 03-Operating Conditions | Time-varying generator speed and load conditions(Variable Conditions) |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 8 | `LG44WPDW_E051` | `induces_problem` | 03-Operating Conditions | Time-varying generator speed and load conditions(Variable Conditions) |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |
| 9 | `LG44WPDW_E052` | `induces_problem` | 06-Fault Severity | two levels of rotor unbalance of 23% and 46%(Multiple Severities) |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 10 | `LG44WPDW_E053` | `induces_problem` | 06-Fault Severity | two levels of rotor unbalance of 23% and 46%(Multiple Severities) |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |
| 11 | `LG44WPDW_E054` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 12 | `LG44WPDW_E055` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |
| 13 | `LG44WPDW_E056` | `induces_problem` | 08-PHM Task | Rotor electrical asymmetry detection(Detection Task) |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 14 | `LG44WPDW_E057` | `induces_problem` | 08-PHM Task | Rotor electrical asymmetry detection(Detection Task) |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |
| 15 | `LG44WPDW_E058` | `induces_problem` | 12-Training Data Availability | At each test, the test rig was run for a period of 150 s after which the 23% and 46% unbalance fault conditions were applied at 150 s and 300 s, respectively. ... sampling frequency of 5 kHz.(Sufficient) |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 16 | `LG44WPDW_E059` | `induces_problem` | 12-Training Data Availability | At each test, the test rig was run for a period of 150 s after which the 23% and 46% unbalance fault conditions were applied at 150 s and 300 s, respectively. ... sampling frequency of 5 kHz.(Sufficient) |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |
| 17 | `LG44WPDW_E060` | `induces_problem` | 13-Noise Level | resulting in FSCs manifesting themselves in the vicinity of the supply frequency and its harmonics with extraneous noise(High Noise) |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 18 | `LG44WPDW_E061` | `induces_problem` | 13-Noise Level | resulting in FSCs manifesting themselves in the vicinity of the supply frequency and its harmonics with extraneous noise(High Noise) |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |
| 19 | `LG44WPDW_E062` | `induces_problem` | 14-Computational Resource | it is able to accurately detect fault frequencies with minimal computational requirements when compared with a CWT(Low Resource Consumption) |  | 09-Problem Scenario | FSCs merged with supply frequency harmonics and noise robustness(Uncertainty) |  |
| 20 | `LG44WPDW_E063` | `induces_problem` | 14-Computational Resource | it is able to accurately detect fault frequencies with minimal computational requirements when compared with a CWT(Low Resource Consumption) |  | 09-Problem Scenario | Time-varying and nonstationary signal characteristics(Other) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 20 edges)*
