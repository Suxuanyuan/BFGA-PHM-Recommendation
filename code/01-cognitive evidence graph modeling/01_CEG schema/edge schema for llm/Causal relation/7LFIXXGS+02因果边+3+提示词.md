# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：7LFIXXGS
- **Paper Title**：Distribution Adaptation and Manifold Alignment for complex processes fault diagnosis
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `7LFIXXGS`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "7LFIXXGS_E151", "edge_description": "temperature sensor can obviously reflect component exception"},
    {"edge_id": "7LFIXXGS_E152", "edge_description": "temperature sensor can obviously reflect blockage"},
    {"edge_id": "7LFIXXGS_E153", "edge_description": "temperature sensor can obviously reflect flow exception"},
    {"edge_id": "7LFIXXGS_E154", "edge_description": "level sensor can obviously reflect temperature exception"},
    {"edge_id": "7LFIXXGS_E155", "edge_description": "level sensor can obviously reflect feed rate exception"},
    {"edge_id": "7LFIXXGS_E156", "edge_description": "level sensor can obviously reflect component exception"},
    {"edge_id": "7LFIXXGS_E157", "edge_description": "level sensor can obviously reflect blockage"},
    {"edge_id": "7LFIXXGS_E158", "edge_description": "level sensor can obviously reflect flow exception"},
    {"edge_id": "7LFIXXGS_E159", "edge_description": "flow sensor can obviously reflect temperature exception"},
    {"edge_id": "7LFIXXGS_E160", "edge_description": "flow sensor can obviously reflect feed rate exception"},
    {"edge_id": "7LFIXXGS_E161", "edge_description": "flow sensor can obviously reflect component exception"},
    {"edge_id": "7LFIXXGS_E162", "edge_description": "flow sensor can obviously reflect blockage"},
    {"edge_id": "7LFIXXGS_E163", "edge_description": "flow sensor can obviously reflect flow exception"},
    {"edge_id": "7LFIXXGS_E164", "edge_description": "Tennessee–Eastman (TE) process simulation data can be used for fault detection and diagnosis"},
    {"edge_id": "7LFIXXGS_E165", "edge_description": "real ore grinding-classification process dataset can be used for fault detection and diagnosis"},
    {"edge_id": "7LFIXXGS_E166", "edge_description": "reactor has_fault_mode temperature exception"},
    {"edge_id": "7LFIXXGS_E167", "edge_description": "reactor has_fault_mode feed rate exception"},
    {"edge_id": "7LFIXXGS_E168", "edge_description": "reactor has_fault_mode component exception"},
    {"edge_id": "7LFIXXGS_E169", "edge_description": "reactor has_fault_mode blockage"},
    {"edge_id": "7LFIXXGS_E170", "edge_description": "reactor has_fault_mode flow exception"},
    {"edge_id": "7LFIXXGS_E171", "edge_description": "condenser has_fault_mode temperature exception"},
    {"edge_id": "7LFIXXGS_E172", "edge_description": "condenser has_fault_mode feed rate exception"},
    {"edge_id": "7LFIXXGS_E173", "edge_description": "condenser has_fault_mode component exception"},
    {"edge_id": "7LFIXXGS_E174", "edge_description": "condenser has_fault_mode blockage"},
    {"edge_id": "7LFIXXGS_E175", "edge_description": "condenser has_fault_mode flow exception"},
    {"edge_id": "7LFIXXGS_E176", "edge_description": "feed line has_fault_mode temperature exception"},
    {"edge_id": "7LFIXXGS_E177", "edge_description": "feed line has_fault_mode feed rate exception"},
    {"edge_id": "7LFIXXGS_E178", "edge_description": "feed line has_fault_mode component exception"},
    {"edge_id": "7LFIXXGS_E179", "edge_description": "feed line has_fault_mode blockage"},
    {"edge_id": "7LFIXXGS_E180", "edge_description": "feed line has_fault_mode flow exception"}
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
| 1 | `7LFIXXGS_E151` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | component exception |  |
| 2 | `7LFIXXGS_E152` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | blockage |  |
| 3 | `7LFIXXGS_E153` | `can obviously reflect` | 11-Sensor Information | temperature sensor |  | 05-Fault Mode | flow exception |  |
| 4 | `7LFIXXGS_E154` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | temperature exception |  |
| 5 | `7LFIXXGS_E155` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | feed rate exception |  |
| 6 | `7LFIXXGS_E156` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | component exception |  |
| 7 | `7LFIXXGS_E157` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | blockage |  |
| 8 | `7LFIXXGS_E158` | `can obviously reflect` | 11-Sensor Information | level sensor |  | 05-Fault Mode | flow exception |  |
| 9 | `7LFIXXGS_E159` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | temperature exception |  |
| 10 | `7LFIXXGS_E160` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | feed rate exception |  |
| 11 | `7LFIXXGS_E161` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | component exception |  |
| 12 | `7LFIXXGS_E162` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | blockage |  |
| 13 | `7LFIXXGS_E163` | `can obviously reflect` | 11-Sensor Information | flow sensor |  | 05-Fault Mode | flow exception |  |
| 14 | `7LFIXXGS_E164` | `can be used for` | 10-Dataset | Tennessee–Eastman (TE) process simulation data |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 15 | `7LFIXXGS_E165` | `can be used for` | 10-Dataset | real ore grinding-classification process dataset |  | 08-PHM Task | fault detection and diagnosis(Diagnosis Task) |  |
| 16 | `7LFIXXGS_E166` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | temperature exception |  |
| 17 | `7LFIXXGS_E167` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | feed rate exception |  |
| 18 | `7LFIXXGS_E168` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | component exception |  |
| 19 | `7LFIXXGS_E169` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | blockage |  |
| 20 | `7LFIXXGS_E170` | `has_fault_mode` | 04-Fault Location | reactor |  | 05-Fault Mode | flow exception |  |
| 21 | `7LFIXXGS_E171` | `has_fault_mode` | 04-Fault Location | condenser |  | 05-Fault Mode | temperature exception |  |
| 22 | `7LFIXXGS_E172` | `has_fault_mode` | 04-Fault Location | condenser |  | 05-Fault Mode | feed rate exception |  |
| 23 | `7LFIXXGS_E173` | `has_fault_mode` | 04-Fault Location | condenser |  | 05-Fault Mode | component exception |  |
| 24 | `7LFIXXGS_E174` | `has_fault_mode` | 04-Fault Location | condenser |  | 05-Fault Mode | blockage |  |
| 25 | `7LFIXXGS_E175` | `has_fault_mode` | 04-Fault Location | condenser |  | 05-Fault Mode | flow exception |  |
| 26 | `7LFIXXGS_E176` | `has_fault_mode` | 04-Fault Location | feed line |  | 05-Fault Mode | temperature exception |  |
| 27 | `7LFIXXGS_E177` | `has_fault_mode` | 04-Fault Location | feed line |  | 05-Fault Mode | feed rate exception |  |
| 28 | `7LFIXXGS_E178` | `has_fault_mode` | 04-Fault Location | feed line |  | 05-Fault Mode | component exception |  |
| 29 | `7LFIXXGS_E179` | `has_fault_mode` | 04-Fault Location | feed line |  | 05-Fault Mode | blockage |  |
| 30 | `7LFIXXGS_E180` | `has_fault_mode` | 04-Fault Location | feed line |  | 05-Fault Mode | flow exception |  |

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

### ▶ For `can obviously reflect` (Sensor Information type → Fault Mode type)

**Very High Standard**: All of the following **conditions must be met** to be judged as "existing":
1. The paper explicitly states that the sensor **collects** data of this fault mode (i.e., the sensor appears in the fault data acquisition scenario)
2. The paper explicitly states that the sensor can **directly reflect/characterize** the physical features of this fault
3. The mere appearance of the sensor and fault mode in the dataset description is **insufficient** for judgment — the sensor must play an active role in the research method
**Trap to Watch Out For**: The mere appearance of the sensor and fault mode as dataset description does not equal the existence of a causal chain
**Meaning of "Directly Mentioned"**: Means that the paper explicitly expresses a sensor→fault-feature causal relation, rather than exact matching of English phrases

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

*This prompt is automatically generated by edge_02_prompt.py (Batch 3, total 30 edges)*
