# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：P6LXQZF8
- **Paper Title**：A Novel Incipient Fault Diagnosis Method for Analog Circuits Based on GMKL-SVM and Wavelet Fusion Features
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `P6LXQZF8`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "P6LXQZF8_E081", "edge_description": "Analog circuits contains Sallen-Key bandpass filter circuit"},
    {"edge_id": "P6LXQZF8_E082", "edge_description": "Analog circuits contains four-op-amp biquad high-pass filter circuit"},
    {"edge_id": "P6LXQZF8_E083", "edge_description": "Analog circuits contains leapfrog filter circuit"},
    {"edge_id": "P6LXQZF8_E084", "edge_description": "Sallen-Key bandpass filter circuit contains capacitor"},
    {"edge_id": "P6LXQZF8_E085", "edge_description": "Sallen-Key bandpass filter circuit contains resistor"},
    {"edge_id": "P6LXQZF8_E086", "edge_description": "four-op-amp biquad high-pass filter circuit contains capacitor"},
    {"edge_id": "P6LXQZF8_E087", "edge_description": "four-op-amp biquad high-pass filter circuit contains resistor"},
    {"edge_id": "P6LXQZF8_E088", "edge_description": "leapfrog filter circuit contains capacitor"},
    {"edge_id": "P6LXQZF8_E089", "edge_description": "leapfrog filter circuit contains resistor"},
    {"edge_id": "P6LXQZF8_E090", "edge_description": "Sallen-Key bandpass filter circuit contains pulse signal excitation"},
    {"edge_id": "P6LXQZF8_E091", "edge_description": "four-op-amp biquad high-pass filter circuit contains pulse signal excitation"},
    {"edge_id": "P6LXQZF8_E092", "edge_description": "leapfrog filter circuit contains pulse signal excitation"},
    {"edge_id": "P6LXQZF8_E094", "edge_description": "voltage sensor is collected on capacitor"},
    {"edge_id": "P6LXQZF8_E095", "edge_description": "voltage sensor is collected on resistor"},
    {"edge_id": "P6LXQZF8_E097", "edge_description": "Sallen-Key bandpass filter circuit simulation dataset can be used for incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E098", "edge_description": "Four-op-amp biquad high-pass filter circuit simulation dataset can be used for incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E099", "edge_description": "Leapfrog filter circuit simulation dataset can be used for incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E100", "edge_description": "capacitor has_fault_mode soft fault"},
    {"edge_id": "P6LXQZF8_E101", "edge_description": "resistor has_fault_mode soft fault"},
    {"edge_id": "P6LXQZF8_E103", "edge_description": "Sallen-Key bandpass filter circuit contains_phm_task incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E104", "edge_description": "four-op-amp biquad high-pass filter circuit contains_phm_task incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E105", "edge_description": "leapfrog filter circuit contains_phm_task incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E106", "edge_description": "capacitor contains_phm_task incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E107", "edge_description": "resistor contains_phm_task incipient fault diagnosis"},
    {"edge_id": "P6LXQZF8_E110", "edge_description": "Sallen-Key bandpass filter circuit induces_problem weak fault features of incipient soft faults"},
    {"edge_id": "P6LXQZF8_E111", "edge_description": "Sallen-Key bandpass filter circuit induces_problem component tolerances cause state overlap"},
    {"edge_id": "P6LXQZF8_E112", "edge_description": "four-op-amp biquad high-pass filter circuit induces_problem weak fault features of incipient soft faults"},
    {"edge_id": "P6LXQZF8_E113", "edge_description": "four-op-amp biquad high-pass filter circuit induces_problem component tolerances cause state overlap"},
    {"edge_id": "P6LXQZF8_E114", "edge_description": "leapfrog filter circuit induces_problem weak fault features of incipient soft faults"},
    {"edge_id": "P6LXQZF8_E115", "edge_description": "leapfrog filter circuit induces_problem component tolerances cause state overlap"}
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
| 1 | `P6LXQZF8_E081` | `contains` | 01-Object Domain | Analog circuits(Electronics) |  | 02-Object Type | Sallen-Key bandpass filter circuit |  |
| 2 | `P6LXQZF8_E082` | `contains` | 01-Object Domain | Analog circuits(Electronics) |  | 02-Object Type | four-op-amp biquad high-pass filter circuit |  |
| 3 | `P6LXQZF8_E083` | `contains` | 01-Object Domain | Analog circuits(Electronics) |  | 02-Object Type | leapfrog filter circuit |  |
| 4 | `P6LXQZF8_E084` | `contains` | 02-Object Type | Sallen-Key bandpass filter circuit |  | 04-Fault Location | capacitor |  |
| 5 | `P6LXQZF8_E085` | `contains` | 02-Object Type | Sallen-Key bandpass filter circuit |  | 04-Fault Location | resistor |  |
| 6 | `P6LXQZF8_E086` | `contains` | 02-Object Type | four-op-amp biquad high-pass filter circuit |  | 04-Fault Location | capacitor |  |
| 7 | `P6LXQZF8_E087` | `contains` | 02-Object Type | four-op-amp biquad high-pass filter circuit |  | 04-Fault Location | resistor |  |
| 8 | `P6LXQZF8_E088` | `contains` | 02-Object Type | leapfrog filter circuit |  | 04-Fault Location | capacitor |  |
| 9 | `P6LXQZF8_E089` | `contains` | 02-Object Type | leapfrog filter circuit |  | 04-Fault Location | resistor |  |
| 10 | `P6LXQZF8_E090` | `contains` | 02-Object Type | Sallen-Key bandpass filter circuit |  | 03-Operating Conditions | pulse signal excitation(Single Condition) |  |
| 11 | `P6LXQZF8_E091` | `contains` | 02-Object Type | four-op-amp biquad high-pass filter circuit |  | 03-Operating Conditions | pulse signal excitation(Single Condition) |  |
| 12 | `P6LXQZF8_E092` | `contains` | 02-Object Type | leapfrog filter circuit |  | 03-Operating Conditions | pulse signal excitation(Single Condition) |  |
| 13 | `P6LXQZF8_E094` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | capacitor |  |
| 14 | `P6LXQZF8_E095` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | resistor |  |
| 15 | `P6LXQZF8_E097` | `can be used for` | 10-Dataset | Sallen-Key bandpass filter circuit simulation dataset |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 16 | `P6LXQZF8_E098` | `can be used for` | 10-Dataset | Four-op-amp biquad high-pass filter circuit simulation dataset |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 17 | `P6LXQZF8_E099` | `can be used for` | 10-Dataset | Leapfrog filter circuit simulation dataset |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 18 | `P6LXQZF8_E100` | `has_fault_mode` | 04-Fault Location | capacitor |  | 05-Fault Mode | soft fault |  |
| 19 | `P6LXQZF8_E101` | `has_fault_mode` | 04-Fault Location | resistor |  | 05-Fault Mode | soft fault |  |
| 20 | `P6LXQZF8_E103` | `contains_phm_task` | 02-Object Type | Sallen-Key bandpass filter circuit |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 21 | `P6LXQZF8_E104` | `contains_phm_task` | 02-Object Type | four-op-amp biquad high-pass filter circuit |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 22 | `P6LXQZF8_E105` | `contains_phm_task` | 02-Object Type | leapfrog filter circuit |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 23 | `P6LXQZF8_E106` | `contains_phm_task` | 04-Fault Location | capacitor |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 24 | `P6LXQZF8_E107` | `contains_phm_task` | 04-Fault Location | resistor |  | 08-PHM Task | incipient fault diagnosis(Diagnosis Task) |  |
| 25 | `P6LXQZF8_E110` | `induces_problem` | 02-Object Type | Sallen-Key bandpass filter circuit |  | 09-Problem Scenario | weak fault features of incipient soft faults(Early Degradation Prediction) |  |
| 26 | `P6LXQZF8_E111` | `induces_problem` | 02-Object Type | Sallen-Key bandpass filter circuit |  | 09-Problem Scenario | component tolerances cause state overlap(Uncertainty) |  |
| 27 | `P6LXQZF8_E112` | `induces_problem` | 02-Object Type | four-op-amp biquad high-pass filter circuit |  | 09-Problem Scenario | weak fault features of incipient soft faults(Early Degradation Prediction) |  |
| 28 | `P6LXQZF8_E113` | `induces_problem` | 02-Object Type | four-op-amp biquad high-pass filter circuit |  | 09-Problem Scenario | component tolerances cause state overlap(Uncertainty) |  |
| 29 | `P6LXQZF8_E114` | `induces_problem` | 02-Object Type | leapfrog filter circuit |  | 09-Problem Scenario | weak fault features of incipient soft faults(Early Degradation Prediction) |  |
| 30 | `P6LXQZF8_E115` | `induces_problem` | 02-Object Type | leapfrog filter circuit |  | 09-Problem Scenario | component tolerances cause state overlap(Uncertainty) |  |

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

### ▶ For `is collected on` (Sensor Information type → Fault Location type)

**High Standard**: The paper must explicitly express that the sensor is **physically installed/arranged on** the target fault location, i.e., there is a description of the **physical positional relationship** between the sensor and the fault location.
The mere appearance in the dataset description of "a sensor used for a certain fault" is insufficient — the physical arrangement or installation context of the sensor must be reflected
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the relationship between the physical installation position of the sensor and the fault location, rather than exact matching of English phrases

### ▶ For `can be used for` (Dataset type → PHM Task type)

**High Standard**: The paper must explicitly express that the dataset is an **input at the methodological level**, rather than merely a background for experimental evaluation.
Merely mentioning "using a dataset to evaluate model performance" is insufficient — the methodological association between dataset and task must be reflected (e.g., "selecting a dataset for a specific task")
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses the methodological relation of the dataset serving a certain PHM task, rather than exact matching of English phrases

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
