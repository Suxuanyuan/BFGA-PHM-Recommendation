# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：NYEZIYYG
- **Paper Title**：Gear Fault Diagnosis Based on Empirical Mode Decomposition and 1.5 Dimension Spectrum
- **Number of Candidate Edges to Judge**：10 

---

## II. LLM Input

> **Input Material**: Reference ID `NYEZIYYG`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "NYEZIYYG_E052", "edge_description": "Simulation: Simulated gear fault signals can be used for gear fault diagnosis"},
    {"edge_id": "NYEZIYYG_E053", "edge_description": "Self-collected: Gearbox vibration signal from comprehensive fault simulation test bench can be used for gear fault diagnosis"},
    {"edge_id": "NYEZIYYG_E060", "edge_description": "gear induces_problem Gaussian noise interference, strong background noise"},
    {"edge_id": "NYEZIYYG_E061", "edge_description": "motor speed fr1 = 720 rpm, rotating frequency of gear axis fr2 = 480 rpm, meshing frequency fz = 120 Hz induces_problem Gaussian noise interference, strong background noise"},
    {"edge_id": "NYEZIYYG_E062", "edge_description": "0.1 mm width and 3 mm depth induces_problem Gaussian noise interference, strong background noise"},
    {"edge_id": "NYEZIYYG_E063", "edge_description": "No Compound Fault induces_problem Gaussian noise interference, strong background noise"},
    {"edge_id": "NYEZIYYG_E064", "edge_description": "gear fault diagnosis induces_problem Gaussian noise interference, strong background noise"},
    {"edge_id": "NYEZIYYG_E065", "edge_description": "Sufficient induces_problem Gaussian noise interference, strong background noise"},
    {"edge_id": "NYEZIYYG_E066", "edge_description": "Gauss noise, strong background noise induces_problem Gaussian noise interference, strong background noise"},
    {"edge_id": "NYEZIYYG_E067", "edge_description": "low computational complexity, good real-time performance induces_problem Gaussian noise interference, strong background noise"}
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
| 1 | `NYEZIYYG_E052` | `can be used for` | 10-Dataset | Simulation: Simulated gear fault signals |  | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  |
| 2 | `NYEZIYYG_E053` | `can be used for` | 10-Dataset | Self-collected: Gearbox vibration signal from comprehensive fault simulation test bench |  | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  |
| 3 | `NYEZIYYG_E060` | `induces_problem` | 02-Object Type | gear |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |
| 4 | `NYEZIYYG_E061` | `induces_problem` | 03-Operating Conditions | motor speed fr1 = 720 rpm, rotating frequency of gear axis fr2 = 480 rpm, meshing frequency fz = 120 Hz(Single Condition) |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |
| 5 | `NYEZIYYG_E062` | `induces_problem` | 06-Fault Severity | 0.1 mm width and 3 mm depth(Single Severity) |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |
| 6 | `NYEZIYYG_E063` | `induces_problem` | 07-Compound Fault | No Compound Fault |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |
| 7 | `NYEZIYYG_E064` | `induces_problem` | 08-PHM Task | gear fault diagnosis(Diagnosis Task) |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |
| 8 | `NYEZIYYG_E065` | `induces_problem` | 12-Training Data Availability | Sufficient |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |
| 9 | `NYEZIYYG_E066` | `induces_problem` | 13-Noise Level | Gauss noise, strong background noise(High Noise) |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |
| 10 | `NYEZIYYG_E067` | `induces_problem` | 14-Computational Resource | low computational complexity, good real-time performance(Low Resource Consumption) |  | 09-Problem Scenario | Gaussian noise interference, strong background noise(Uncertainty) |  |

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 1, total 10 edges)*
