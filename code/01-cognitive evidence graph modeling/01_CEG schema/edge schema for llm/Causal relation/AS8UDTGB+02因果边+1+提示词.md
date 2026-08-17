# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：AS8UDTGB
- **Paper Title**：Intermittent Connection Fault Diagnosis for CAN Using Data Link Layer Information
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `AS8UDTGB`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "AS8UDTGB_E053", "edge_description": "Controller Area Network (CAN) contains drop cable"},
    {"edge_id": "AS8UDTGB_E054", "edge_description": "Controller Area Network (CAN) contains trunk cable"},
    {"edge_id": "AS8UDTGB_E057", "edge_description": "CAN transceiver is collected on drop cable"},
    {"edge_id": "AS8UDTGB_E058", "edge_description": "CAN transceiver is collected on trunk cable"},
    {"edge_id": "AS8UDTGB_E061", "edge_description": "drop cable has_fault_mode intermittent connection fault"},
    {"edge_id": "AS8UDTGB_E062", "edge_description": "trunk cable has_fault_mode intermittent connection fault"},
    {"edge_id": "AS8UDTGB_E065", "edge_description": "drop cable contains_phm_task fault localization"},
    {"edge_id": "AS8UDTGB_E066", "edge_description": "trunk cable contains_phm_task fault localization"},
    {"edge_id": "AS8UDTGB_E069", "edge_description": "Controller Area Network (CAN) induces_problem multiple IC faults"},
    {"edge_id": "AS8UDTGB_E070", "edge_description": "Controller Area Network (CAN) induces_problem global interference"},
    {"edge_id": "AS8UDTGB_E071", "edge_description": "Controller Area Network (CAN) induces_problem network topology representation"},
    {"edge_id": "AS8UDTGB_E072", "edge_description": "various fault scenarios with different injection rates induces_problem multiple IC faults"},
    {"edge_id": "AS8UDTGB_E073", "edge_description": "various fault scenarios with different injection rates induces_problem global interference"},
    {"edge_id": "AS8UDTGB_E074", "edge_description": "various fault scenarios with different injection rates induces_problem network topology representation"},
    {"edge_id": "AS8UDTGB_E075", "edge_description": "fault injection rate induces_problem multiple IC faults"},
    {"edge_id": "AS8UDTGB_E076", "edge_description": "fault injection rate induces_problem global interference"},
    {"edge_id": "AS8UDTGB_E077", "edge_description": "fault injection rate induces_problem network topology representation"},
    {"edge_id": "AS8UDTGB_E078", "edge_description": "multiple IC faults induces_problem multiple IC faults"},
    {"edge_id": "AS8UDTGB_E079", "edge_description": "multiple IC faults induces_problem global interference"},
    {"edge_id": "AS8UDTGB_E080", "edge_description": "multiple IC faults induces_problem network topology representation"},
    {"edge_id": "AS8UDTGB_E081", "edge_description": "fault localization induces_problem multiple IC faults"},
    {"edge_id": "AS8UDTGB_E082", "edge_description": "fault localization induces_problem global interference"},
    {"edge_id": "AS8UDTGB_E083", "edge_description": "fault localization induces_problem network topology representation"},
    {"edge_id": "AS8UDTGB_E084", "edge_description": "2055 / 10714 / 7089 error records induces_problem multiple IC faults"},
    {"edge_id": "AS8UDTGB_E085", "edge_description": "2055 / 10714 / 7089 error records induces_problem global interference"},
    {"edge_id": "AS8UDTGB_E086", "edge_description": "2055 / 10714 / 7089 error records induces_problem network topology representation"},
    {"edge_id": "AS8UDTGB_E087", "edge_description": "global interference (e.g. EMI) induces_problem multiple IC faults"},
    {"edge_id": "AS8UDTGB_E088", "edge_description": "global interference (e.g. EMI) induces_problem global interference"},
    {"edge_id": "AS8UDTGB_E089", "edge_description": "global interference (e.g. EMI) induces_problem network topology representation"},
    {"edge_id": "AS8UDTGB_E090", "edge_description": "FPGA based data acquisition on NI CompactRIO hardware induces_problem multiple IC faults"}
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
| 1 | `AS8UDTGB_E053` | `contains` | 02-Object Type | Controller Area Network (CAN) |  | 04-Fault Location | drop cable |  |
| 2 | `AS8UDTGB_E054` | `contains` | 02-Object Type | Controller Area Network (CAN) |  | 04-Fault Location | trunk cable |  |
| 3 | `AS8UDTGB_E057` | `is collected on` | 11-Sensor Information | CAN transceiver |  | 04-Fault Location | drop cable |  |
| 4 | `AS8UDTGB_E058` | `is collected on` | 11-Sensor Information | CAN transceiver |  | 04-Fault Location | trunk cable |  |
| 5 | `AS8UDTGB_E061` | `has_fault_mode` | 04-Fault Location | drop cable |  | 05-Fault Mode | intermittent connection fault |  |
| 6 | `AS8UDTGB_E062` | `has_fault_mode` | 04-Fault Location | trunk cable |  | 05-Fault Mode | intermittent connection fault |  |
| 7 | `AS8UDTGB_E065` | `contains_phm_task` | 04-Fault Location | drop cable |  | 08-PHM Task | fault localization(Diagnosis Task) |  |
| 8 | `AS8UDTGB_E066` | `contains_phm_task` | 04-Fault Location | trunk cable |  | 08-PHM Task | fault localization(Diagnosis Task) |  |
| 9 | `AS8UDTGB_E069` | `induces_problem` | 02-Object Type | Controller Area Network (CAN) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |
| 10 | `AS8UDTGB_E070` | `induces_problem` | 02-Object Type | Controller Area Network (CAN) |  | 09-Problem Scenario | global interference(Uncertainty) |  |
| 11 | `AS8UDTGB_E071` | `induces_problem` | 02-Object Type | Controller Area Network (CAN) |  | 09-Problem Scenario | network topology representation(Complex Systems) |  |
| 12 | `AS8UDTGB_E072` | `induces_problem` | 03-Operating Conditions | various fault scenarios with different injection rates(Multiple Conditions) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |
| 13 | `AS8UDTGB_E073` | `induces_problem` | 03-Operating Conditions | various fault scenarios with different injection rates(Multiple Conditions) |  | 09-Problem Scenario | global interference(Uncertainty) |  |
| 14 | `AS8UDTGB_E074` | `induces_problem` | 03-Operating Conditions | various fault scenarios with different injection rates(Multiple Conditions) |  | 09-Problem Scenario | network topology representation(Complex Systems) |  |
| 15 | `AS8UDTGB_E075` | `induces_problem` | 06-Fault Severity | fault injection rate(Single Severity) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |
| 16 | `AS8UDTGB_E076` | `induces_problem` | 06-Fault Severity | fault injection rate(Single Severity) |  | 09-Problem Scenario | global interference(Uncertainty) |  |
| 17 | `AS8UDTGB_E077` | `induces_problem` | 06-Fault Severity | fault injection rate(Single Severity) |  | 09-Problem Scenario | network topology representation(Complex Systems) |  |
| 18 | `AS8UDTGB_E078` | `induces_problem` | 07-Compound Fault | multiple IC faults(Compound Fault Within Same Structure) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |
| 19 | `AS8UDTGB_E079` | `induces_problem` | 07-Compound Fault | multiple IC faults(Compound Fault Within Same Structure) |  | 09-Problem Scenario | global interference(Uncertainty) |  |
| 20 | `AS8UDTGB_E080` | `induces_problem` | 07-Compound Fault | multiple IC faults(Compound Fault Within Same Structure) |  | 09-Problem Scenario | network topology representation(Complex Systems) |  |
| 21 | `AS8UDTGB_E081` | `induces_problem` | 08-PHM Task | fault localization(Diagnosis Task) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |
| 22 | `AS8UDTGB_E082` | `induces_problem` | 08-PHM Task | fault localization(Diagnosis Task) |  | 09-Problem Scenario | global interference(Uncertainty) |  |
| 23 | `AS8UDTGB_E083` | `induces_problem` | 08-PHM Task | fault localization(Diagnosis Task) |  | 09-Problem Scenario | network topology representation(Complex Systems) |  |
| 24 | `AS8UDTGB_E084` | `induces_problem` | 12-Training Data Availability | 2055 / 10714 / 7089 error records(Sufficient) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |
| 25 | `AS8UDTGB_E085` | `induces_problem` | 12-Training Data Availability | 2055 / 10714 / 7089 error records(Sufficient) |  | 09-Problem Scenario | global interference(Uncertainty) |  |
| 26 | `AS8UDTGB_E086` | `induces_problem` | 12-Training Data Availability | 2055 / 10714 / 7089 error records(Sufficient) |  | 09-Problem Scenario | network topology representation(Complex Systems) |  |
| 27 | `AS8UDTGB_E087` | `induces_problem` | 13-Noise Level | global interference (e.g. EMI)(High Noise) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |
| 28 | `AS8UDTGB_E088` | `induces_problem` | 13-Noise Level | global interference (e.g. EMI)(High Noise) |  | 09-Problem Scenario | global interference(Uncertainty) |  |
| 29 | `AS8UDTGB_E089` | `induces_problem` | 13-Noise Level | global interference (e.g. EMI)(High Noise) |  | 09-Problem Scenario | network topology representation(Complex Systems) |  |
| 30 | `AS8UDTGB_E090` | `induces_problem` | 14-Computational Resource | FPGA based data acquisition on NI CompactRIO hardware(Low Resource Consumption) |  | 09-Problem Scenario | multiple IC faults(Compound Faults) |  |

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
