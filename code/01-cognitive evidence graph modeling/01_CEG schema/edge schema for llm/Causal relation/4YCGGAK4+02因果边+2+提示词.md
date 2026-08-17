# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：4YCGGAK4
- **Paper Title**：Hierarchical Monitoring and Root-Cause Diagnosis Framework for Key Performance Indicator-Related Multiple Faults in Process Industries
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `4YCGGAK4`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "4YCGGAK4_E100", "edge_description": "E1 edger mill has_fault_mode malfunction of speed control loop"},
    {"edge_id": "4YCGGAK4_E101", "edge_description": "F4 stand has_fault_mode malfunction of gap control loop"},
    {"edge_id": "4YCGGAK4_E102", "edge_description": "F4 stand has_fault_mode fault of cooling valve"},
    {"edge_id": "4YCGGAK4_E103", "edge_description": "F4 stand has_fault_mode malfunction of speed control loop"},
    {"edge_id": "4YCGGAK4_E104", "edge_description": "cooling valve between F2 and F3 stands has_fault_mode malfunction of gap control loop"},
    {"edge_id": "4YCGGAK4_E105", "edge_description": "cooling valve between F2 and F3 stands has_fault_mode fault of cooling valve"},
    {"edge_id": "4YCGGAK4_E106", "edge_description": "cooling valve between F2 and F3 stands has_fault_mode malfunction of speed control loop"},
    {"edge_id": "4YCGGAK4_E107", "edge_description": "R1 rough roll has_fault_mode malfunction of gap control loop"},
    {"edge_id": "4YCGGAK4_E108", "edge_description": "R1 rough roll has_fault_mode fault of cooling valve"},
    {"edge_id": "4YCGGAK4_E109", "edge_description": "R1 rough roll has_fault_mode malfunction of speed control loop"},
    {"edge_id": "4YCGGAK4_E110", "edge_description": "malfunction of gap control loop contains Single Severity"},
    {"edge_id": "4YCGGAK4_E111", "edge_description": "fault of cooling valve contains Single Severity"},
    {"edge_id": "4YCGGAK4_E112", "edge_description": "malfunction of speed control loop contains Single Severity"},
    {"edge_id": "4YCGGAK4_E114", "edge_description": "E1 edger mill contains_phm_task hierarchical monitoring and root-cause diagnosis"},
    {"edge_id": "4YCGGAK4_E115", "edge_description": "F4 stand contains_phm_task hierarchical monitoring and root-cause diagnosis"},
    {"edge_id": "4YCGGAK4_E116", "edge_description": "cooling valve between F2 and F3 stands contains_phm_task hierarchical monitoring and root-cause diagnosis"},
    {"edge_id": "4YCGGAK4_E117", "edge_description": "R1 rough roll contains_phm_task hierarchical monitoring and root-cause diagnosis"},
    {"edge_id": "4YCGGAK4_E118", "edge_description": "malfunction of gap control loop contains_phm_task hierarchical monitoring and root-cause diagnosis"},
    {"edge_id": "4YCGGAK4_E119", "edge_description": "fault of cooling valve contains_phm_task hierarchical monitoring and root-cause diagnosis"},
    {"edge_id": "4YCGGAK4_E120", "edge_description": "malfunction of speed control loop contains_phm_task hierarchical monitoring and root-cause diagnosis"},
    {"edge_id": "4YCGGAK4_E122", "edge_description": "hot strip mill induces_problem multiple faults"},
    {"edge_id": "4YCGGAK4_E123", "edge_description": "hot strip mill induces_problem plant-wide process / process industries"},
    {"edge_id": "4YCGGAK4_E124", "edge_description": "normal operating conditions induces_problem multiple faults"},
    {"edge_id": "4YCGGAK4_E125", "edge_description": "normal operating conditions induces_problem plant-wide process / process industries"},
    {"edge_id": "4YCGGAK4_E126", "edge_description": "Single Severity induces_problem multiple faults"},
    {"edge_id": "4YCGGAK4_E127", "edge_description": "Single Severity induces_problem plant-wide process / process industries"},
    {"edge_id": "4YCGGAK4_E128", "edge_description": "multiple faults induces_problem multiple faults"},
    {"edge_id": "4YCGGAK4_E129", "edge_description": "multiple faults induces_problem plant-wide process / process industries"},
    {"edge_id": "4YCGGAK4_E130", "edge_description": "hierarchical monitoring and root-cause diagnosis induces_problem multiple faults"},
    {"edge_id": "4YCGGAK4_E131", "edge_description": "hierarchical monitoring and root-cause diagnosis induces_problem plant-wide process / process industries"}
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
| 1 | `4YCGGAK4_E100` | `has_fault_mode` | 04-Fault Location | E1 edger mill |  | 05-Fault Mode | malfunction of speed control loop |  |
| 2 | `4YCGGAK4_E101` | `has_fault_mode` | 04-Fault Location | F4 stand |  | 05-Fault Mode | malfunction of gap control loop |  |
| 3 | `4YCGGAK4_E102` | `has_fault_mode` | 04-Fault Location | F4 stand |  | 05-Fault Mode | fault of cooling valve |  |
| 4 | `4YCGGAK4_E103` | `has_fault_mode` | 04-Fault Location | F4 stand |  | 05-Fault Mode | malfunction of speed control loop |  |
| 5 | `4YCGGAK4_E104` | `has_fault_mode` | 04-Fault Location | cooling valve between F2 and F3 stands |  | 05-Fault Mode | malfunction of gap control loop |  |
| 6 | `4YCGGAK4_E105` | `has_fault_mode` | 04-Fault Location | cooling valve between F2 and F3 stands |  | 05-Fault Mode | fault of cooling valve |  |
| 7 | `4YCGGAK4_E106` | `has_fault_mode` | 04-Fault Location | cooling valve between F2 and F3 stands |  | 05-Fault Mode | malfunction of speed control loop |  |
| 8 | `4YCGGAK4_E107` | `has_fault_mode` | 04-Fault Location | R1 rough roll |  | 05-Fault Mode | malfunction of gap control loop |  |
| 9 | `4YCGGAK4_E108` | `has_fault_mode` | 04-Fault Location | R1 rough roll |  | 05-Fault Mode | fault of cooling valve |  |
| 10 | `4YCGGAK4_E109` | `has_fault_mode` | 04-Fault Location | R1 rough roll |  | 05-Fault Mode | malfunction of speed control loop |  |
| 11 | `4YCGGAK4_E110` | `contains` | 05-Fault Mode | malfunction of gap control loop |  | 06-Fault Severity | Single Severity |  |
| 12 | `4YCGGAK4_E111` | `contains` | 05-Fault Mode | fault of cooling valve |  | 06-Fault Severity | Single Severity |  |
| 13 | `4YCGGAK4_E112` | `contains` | 05-Fault Mode | malfunction of speed control loop |  | 06-Fault Severity | Single Severity |  |
| 14 | `4YCGGAK4_E114` | `contains_phm_task` | 04-Fault Location | E1 edger mill |  | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  |
| 15 | `4YCGGAK4_E115` | `contains_phm_task` | 04-Fault Location | F4 stand |  | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  |
| 16 | `4YCGGAK4_E116` | `contains_phm_task` | 04-Fault Location | cooling valve between F2 and F3 stands |  | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  |
| 17 | `4YCGGAK4_E117` | `contains_phm_task` | 04-Fault Location | R1 rough roll |  | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  |
| 18 | `4YCGGAK4_E118` | `contains_phm_task` | 05-Fault Mode | malfunction of gap control loop |  | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  |
| 19 | `4YCGGAK4_E119` | `contains_phm_task` | 05-Fault Mode | fault of cooling valve |  | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  |
| 20 | `4YCGGAK4_E120` | `contains_phm_task` | 05-Fault Mode | malfunction of speed control loop |  | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  |
| 21 | `4YCGGAK4_E122` | `induces_problem` | 02-Object Type | hot strip mill |  | 09-Problem Scenario | multiple faults(Compound Faults) |  |
| 22 | `4YCGGAK4_E123` | `induces_problem` | 02-Object Type | hot strip mill |  | 09-Problem Scenario | plant-wide process / process industries(Complex Systems) |  |
| 23 | `4YCGGAK4_E124` | `induces_problem` | 03-Operating Conditions | normal operating conditions(Single Condition) |  | 09-Problem Scenario | multiple faults(Compound Faults) |  |
| 24 | `4YCGGAK4_E125` | `induces_problem` | 03-Operating Conditions | normal operating conditions(Single Condition) |  | 09-Problem Scenario | plant-wide process / process industries(Complex Systems) |  |
| 25 | `4YCGGAK4_E126` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | multiple faults(Compound Faults) |  |
| 26 | `4YCGGAK4_E127` | `induces_problem` | 06-Fault Severity | Single Severity |  | 09-Problem Scenario | plant-wide process / process industries(Complex Systems) |  |
| 27 | `4YCGGAK4_E128` | `induces_problem` | 07-Compound Fault | multiple faults(Compound Fault Across Structures) |  | 09-Problem Scenario | multiple faults(Compound Faults) |  |
| 28 | `4YCGGAK4_E129` | `induces_problem` | 07-Compound Fault | multiple faults(Compound Fault Across Structures) |  | 09-Problem Scenario | plant-wide process / process industries(Complex Systems) |  |
| 29 | `4YCGGAK4_E130` | `induces_problem` | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  | 09-Problem Scenario | multiple faults(Compound Faults) |  |
| 30 | `4YCGGAK4_E131` | `induces_problem` | 08-PHM Task | hierarchical monitoring and root-cause diagnosis(Diagnosis Task) |  | 09-Problem Scenario | plant-wide process / process industries(Complex Systems) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 2, total 30 edges)*
