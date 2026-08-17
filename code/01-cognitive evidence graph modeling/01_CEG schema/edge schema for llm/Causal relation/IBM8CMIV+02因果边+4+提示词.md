# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：IBM8CMIV
- **Paper Title**：Evolving Deep Echo State Networks for Intelligent Fault Diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `IBM8CMIV`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "IBM8CMIV_E219", "edge_description": "broken tooth contains 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth"},
    {"edge_id": "IBM8CMIV_E220", "edge_description": "groove contains 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth"},
    {"edge_id": "IBM8CMIV_E221", "edge_description": "joint bearing contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E222", "edge_description": "synchronous belt contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E223", "edge_description": "gearbox (sun gear) contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E224", "edge_description": "joint bearing contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E225", "edge_description": "synchronous belt contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E226", "edge_description": "sun gear contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E227", "edge_description": "clearance contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E228", "edge_description": "slackness contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E229", "edge_description": "pitting contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E230", "edge_description": "broken tooth contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E231", "edge_description": "groove contains_phm_task fault diagnosis"},
    {"edge_id": "IBM8CMIV_E233", "edge_description": "joint bearing induces_problem noise / data noise"},
    {"edge_id": "IBM8CMIV_E234", "edge_description": "joint bearing induces_problem triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor"},
    {"edge_id": "IBM8CMIV_E235", "edge_description": "joint bearing induces_problem compound fault (single-point pitting + half broken tooth)"},
    {"edge_id": "IBM8CMIV_E236", "edge_description": "synchronous belt induces_problem noise / data noise"},
    {"edge_id": "IBM8CMIV_E237", "edge_description": "synchronous belt induces_problem triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor"},
    {"edge_id": "IBM8CMIV_E238", "edge_description": "synchronous belt induces_problem compound fault (single-point pitting + half broken tooth)"},
    {"edge_id": "IBM8CMIV_E239", "edge_description": "gearbox (sun gear) induces_problem noise / data noise"},
    {"edge_id": "IBM8CMIV_E240", "edge_description": "gearbox (sun gear) induces_problem triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor"},
    {"edge_id": "IBM8CMIV_E241", "edge_description": "gearbox (sun gear) induces_problem compound fault (single-point pitting + half broken tooth)"},
    {"edge_id": "IBM8CMIV_E242", "edge_description": "single operating condition induces_problem noise / data noise"},
    {"edge_id": "IBM8CMIV_E243", "edge_description": "single operating condition induces_problem triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor"},
    {"edge_id": "IBM8CMIV_E244", "edge_description": "single operating condition induces_problem compound fault (single-point pitting + half broken tooth)"},
    {"edge_id": "IBM8CMIV_E245", "edge_description": "0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth induces_problem noise / data noise"},
    {"edge_id": "IBM8CMIV_E246", "edge_description": "0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth induces_problem triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor"},
    {"edge_id": "IBM8CMIV_E247", "edge_description": "0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth induces_problem compound fault (single-point pitting + half broken tooth)"},
    {"edge_id": "IBM8CMIV_E248", "edge_description": "single-point pitting + half broken tooth induces_problem noise / data noise"},
    {"edge_id": "IBM8CMIV_E249", "edge_description": "single-point pitting + half broken tooth induces_problem triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor"}
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
| 1 | `IBM8CMIV_E219` | `contains` | 05-Fault Mode | broken tooth |  | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  |
| 2 | `IBM8CMIV_E220` | `contains` | 05-Fault Mode | groove |  | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  |
| 3 | `IBM8CMIV_E221` | `contains_phm_task` | 02-Object Type | joint bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 4 | `IBM8CMIV_E222` | `contains_phm_task` | 02-Object Type | synchronous belt |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 5 | `IBM8CMIV_E223` | `contains_phm_task` | 02-Object Type | gearbox (sun gear) |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 6 | `IBM8CMIV_E224` | `contains_phm_task` | 04-Fault Location | joint bearing |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 7 | `IBM8CMIV_E225` | `contains_phm_task` | 04-Fault Location | synchronous belt |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 8 | `IBM8CMIV_E226` | `contains_phm_task` | 04-Fault Location | sun gear |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 9 | `IBM8CMIV_E227` | `contains_phm_task` | 05-Fault Mode | clearance |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 10 | `IBM8CMIV_E228` | `contains_phm_task` | 05-Fault Mode | slackness |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 11 | `IBM8CMIV_E229` | `contains_phm_task` | 05-Fault Mode | pitting |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 12 | `IBM8CMIV_E230` | `contains_phm_task` | 05-Fault Mode | broken tooth |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 13 | `IBM8CMIV_E231` | `contains_phm_task` | 05-Fault Mode | groove |  | 08-PHM Task | fault diagnosis(Diagnosis Task) |  |
| 14 | `IBM8CMIV_E233` | `induces_problem` | 02-Object Type | joint bearing |  | 09-Problem Scenario | noise / data noise(Uncertainty) |  |
| 15 | `IBM8CMIV_E234` | `induces_problem` | 02-Object Type | joint bearing |  | 09-Problem Scenario | triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor(Multi-Source Heterogeneous / Multimodal Data) |  |
| 16 | `IBM8CMIV_E235` | `induces_problem` | 02-Object Type | joint bearing |  | 09-Problem Scenario | compound fault (single-point pitting + half broken tooth)(Compound Faults) |  |
| 17 | `IBM8CMIV_E236` | `induces_problem` | 02-Object Type | synchronous belt |  | 09-Problem Scenario | noise / data noise(Uncertainty) |  |
| 18 | `IBM8CMIV_E237` | `induces_problem` | 02-Object Type | synchronous belt |  | 09-Problem Scenario | triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor(Multi-Source Heterogeneous / Multimodal Data) |  |
| 19 | `IBM8CMIV_E238` | `induces_problem` | 02-Object Type | synchronous belt |  | 09-Problem Scenario | compound fault (single-point pitting + half broken tooth)(Compound Faults) |  |
| 20 | `IBM8CMIV_E239` | `induces_problem` | 02-Object Type | gearbox (sun gear) |  | 09-Problem Scenario | noise / data noise(Uncertainty) |  |
| 21 | `IBM8CMIV_E240` | `induces_problem` | 02-Object Type | gearbox (sun gear) |  | 09-Problem Scenario | triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor(Multi-Source Heterogeneous / Multimodal Data) |  |
| 22 | `IBM8CMIV_E241` | `induces_problem` | 02-Object Type | gearbox (sun gear) |  | 09-Problem Scenario | compound fault (single-point pitting + half broken tooth)(Compound Faults) |  |
| 23 | `IBM8CMIV_E242` | `induces_problem` | 03-Operating Conditions | single operating condition(Single Condition) |  | 09-Problem Scenario | noise / data noise(Uncertainty) |  |
| 24 | `IBM8CMIV_E243` | `induces_problem` | 03-Operating Conditions | single operating condition(Single Condition) |  | 09-Problem Scenario | triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor(Multi-Source Heterogeneous / Multimodal Data) |  |
| 25 | `IBM8CMIV_E244` | `induces_problem` | 03-Operating Conditions | single operating condition(Single Condition) |  | 09-Problem Scenario | compound fault (single-point pitting + half broken tooth)(Compound Faults) |  |
| 26 | `IBM8CMIV_E245` | `induces_problem` | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  | 09-Problem Scenario | noise / data noise(Uncertainty) |  |
| 27 | `IBM8CMIV_E246` | `induces_problem` | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  | 09-Problem Scenario | triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor(Multi-Source Heterogeneous / Multimodal Data) |  |
| 28 | `IBM8CMIV_E247` | `induces_problem` | 06-Fault Severity | 0.175 mm clearance, 1.05 mm clearance, 1 tooth (1.5 mm) relaxed, 3 teeth (4.5 mm) relaxed, slight single-point pitting, serious single point pitting, half broken tooth, broken tooth(Multiple Severities) |  | 09-Problem Scenario | compound fault (single-point pitting + half broken tooth)(Compound Faults) |  |
| 29 | `IBM8CMIV_E248` | `induces_problem` | 07-Compound Fault | single-point pitting + half broken tooth(Compound Fault Within Same Structure) |  | 09-Problem Scenario | noise / data noise(Uncertainty) |  |
| 30 | `IBM8CMIV_E249` | `induces_problem` | 07-Compound Fault | single-point pitting + half broken tooth(Compound Fault Within Same Structure) |  | 09-Problem Scenario | triaxial accelerometer sensor, three-phase current sensor, acoustic sensor, acoustic emission sensor(Multi-Source Heterogeneous / Multimodal Data) |  |

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
