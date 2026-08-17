# Candidate Causal Edge Relation Judgment Task

---

## I. Overview

Based on the paper PDF specified below, complete the **candidate causal edge relation judgment and description completion** task.

- **Reference ID**：JLHCNWGV
- **Paper Title**：A Classification Approach for Model-Based Fault Diagnosis in Power Generation Systems Based on Solid Oxide Fuel Cells
- **Number of Candidate Edges to Judge**：30 

---

## II. LLM Input

> **Input Material**: Reference ID `JLHCNWGV`  PDF full text (see the [PDF Full Text Content] section at the end of this prompt).
>
> Please first read the paper in full, understand its research background, methods, experiments and conclusions, and then judge each of the following candidate edges one by one.

---

## III. LLM Output Specification

### 3.0 [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

### 3.1 Output Format

```json
[
    {"edge_id": "JLHCNWGV_E112", "edge_description": "solid oxide fuel cell (SOFC) power generation system contains SOFC stack"},
    {"edge_id": "JLHCNWGV_E113", "edge_description": "solid oxide fuel cell (SOFC) power generation system contains reformer"},
    {"edge_id": "JLHCNWGV_E115", "edge_description": "degradation contains No Compound Fault"},
    {"edge_id": "JLHCNWGV_E116", "edge_description": "leakage contains No Compound Fault"},
    {"edge_id": "JLHCNWGV_E117", "edge_description": "power inverter is collected on SOFC stack"},
    {"edge_id": "JLHCNWGV_E118", "edge_description": "power inverter is collected on reformer"},
    {"edge_id": "JLHCNWGV_E119", "edge_description": "air flow meter, flow rate sensor is collected on SOFC stack"},
    {"edge_id": "JLHCNWGV_E120", "edge_description": "air flow meter, flow rate sensor is collected on reformer"},
    {"edge_id": "JLHCNWGV_E121", "edge_description": "pressure sensor is collected on SOFC stack"},
    {"edge_id": "JLHCNWGV_E122", "edge_description": "pressure sensor is collected on reformer"},
    {"edge_id": "JLHCNWGV_E123", "edge_description": "temperature sensor, thermocouple is collected on SOFC stack"},
    {"edge_id": "JLHCNWGV_E124", "edge_description": "temperature sensor, thermocouple is collected on reformer"},
    {"edge_id": "JLHCNWGV_E125", "edge_description": "voltage sensor is collected on SOFC stack"},
    {"edge_id": "JLHCNWGV_E126", "edge_description": "voltage sensor is collected on reformer"},
    {"edge_id": "JLHCNWGV_E127", "edge_description": "power inverter can obviously reflect degradation"},
    {"edge_id": "JLHCNWGV_E128", "edge_description": "power inverter can obviously reflect leakage"},
    {"edge_id": "JLHCNWGV_E129", "edge_description": "air flow meter, flow rate sensor can obviously reflect degradation"},
    {"edge_id": "JLHCNWGV_E130", "edge_description": "air flow meter, flow rate sensor can obviously reflect leakage"},
    {"edge_id": "JLHCNWGV_E131", "edge_description": "pressure sensor can obviously reflect degradation"},
    {"edge_id": "JLHCNWGV_E132", "edge_description": "pressure sensor can obviously reflect leakage"},
    {"edge_id": "JLHCNWGV_E133", "edge_description": "temperature sensor, thermocouple can obviously reflect degradation"},
    {"edge_id": "JLHCNWGV_E134", "edge_description": "temperature sensor, thermocouple can obviously reflect leakage"},
    {"edge_id": "JLHCNWGV_E135", "edge_description": "voltage sensor can obviously reflect degradation"},
    {"edge_id": "JLHCNWGV_E136", "edge_description": "voltage sensor can obviously reflect leakage"},
    {"edge_id": "JLHCNWGV_E137", "edge_description": "GENIUS project SOFC experimental data can be used for fault detection and isolation (FDI)"},
    {"edge_id": "JLHCNWGV_E138", "edge_description": "Simulated fault dataset from SOFC plant model can be used for fault detection and isolation (FDI)"},
    {"edge_id": "JLHCNWGV_E139", "edge_description": "SOFC stack has_fault_mode degradation"},
    {"edge_id": "JLHCNWGV_E140", "edge_description": "SOFC stack has_fault_mode leakage"},
    {"edge_id": "JLHCNWGV_E141", "edge_description": "reformer has_fault_mode degradation"},
    {"edge_id": "JLHCNWGV_E142", "edge_description": "reformer has_fault_mode leakage"}
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
| 1 | `JLHCNWGV_E112` | `contains` | 02-Object Type | solid oxide fuel cell (SOFC) power generation system |  | 04-Fault Location | SOFC stack |  |
| 2 | `JLHCNWGV_E113` | `contains` | 02-Object Type | solid oxide fuel cell (SOFC) power generation system |  | 04-Fault Location | reformer |  |
| 3 | `JLHCNWGV_E115` | `contains` | 05-Fault Mode | degradation |  | 07-Compound Fault | No Compound Fault |  |
| 4 | `JLHCNWGV_E116` | `contains` | 05-Fault Mode | leakage |  | 07-Compound Fault | No Compound Fault |  |
| 5 | `JLHCNWGV_E117` | `is collected on` | 11-Sensor Information | power inverter |  | 04-Fault Location | SOFC stack |  |
| 6 | `JLHCNWGV_E118` | `is collected on` | 11-Sensor Information | power inverter |  | 04-Fault Location | reformer |  |
| 7 | `JLHCNWGV_E119` | `is collected on` | 11-Sensor Information | air flow meter, flow rate sensor |  | 04-Fault Location | SOFC stack |  |
| 8 | `JLHCNWGV_E120` | `is collected on` | 11-Sensor Information | air flow meter, flow rate sensor |  | 04-Fault Location | reformer |  |
| 9 | `JLHCNWGV_E121` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | SOFC stack |  |
| 10 | `JLHCNWGV_E122` | `is collected on` | 11-Sensor Information | pressure sensor |  | 04-Fault Location | reformer |  |
| 11 | `JLHCNWGV_E123` | `is collected on` | 11-Sensor Information | temperature sensor, thermocouple |  | 04-Fault Location | SOFC stack |  |
| 12 | `JLHCNWGV_E124` | `is collected on` | 11-Sensor Information | temperature sensor, thermocouple |  | 04-Fault Location | reformer |  |
| 13 | `JLHCNWGV_E125` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | SOFC stack |  |
| 14 | `JLHCNWGV_E126` | `is collected on` | 11-Sensor Information | voltage sensor |  | 04-Fault Location | reformer |  |
| 15 | `JLHCNWGV_E127` | `can obviously reflect` | 11-Sensor Information | power inverter |  | 05-Fault Mode | degradation |  |
| 16 | `JLHCNWGV_E128` | `can obviously reflect` | 11-Sensor Information | power inverter |  | 05-Fault Mode | leakage |  |
| 17 | `JLHCNWGV_E129` | `can obviously reflect` | 11-Sensor Information | air flow meter, flow rate sensor |  | 05-Fault Mode | degradation |  |
| 18 | `JLHCNWGV_E130` | `can obviously reflect` | 11-Sensor Information | air flow meter, flow rate sensor |  | 05-Fault Mode | leakage |  |
| 19 | `JLHCNWGV_E131` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | degradation |  |
| 20 | `JLHCNWGV_E132` | `can obviously reflect` | 11-Sensor Information | pressure sensor |  | 05-Fault Mode | leakage |  |
| 21 | `JLHCNWGV_E133` | `can obviously reflect` | 11-Sensor Information | temperature sensor, thermocouple |  | 05-Fault Mode | degradation |  |
| 22 | `JLHCNWGV_E134` | `can obviously reflect` | 11-Sensor Information | temperature sensor, thermocouple |  | 05-Fault Mode | leakage |  |
| 23 | `JLHCNWGV_E135` | `can obviously reflect` | 11-Sensor Information | voltage sensor |  | 05-Fault Mode | degradation |  |
| 24 | `JLHCNWGV_E136` | `can obviously reflect` | 11-Sensor Information | voltage sensor |  | 05-Fault Mode | leakage |  |
| 25 | `JLHCNWGV_E137` | `can be used for` | 10-Dataset | GENIUS project SOFC experimental data |  | 08-PHM Task | fault detection and isolation (FDI)(Diagnosis Task) |  |
| 26 | `JLHCNWGV_E138` | `can be used for` | 10-Dataset | Simulated fault dataset from SOFC plant model |  | 08-PHM Task | fault detection and isolation (FDI)(Diagnosis Task) |  |
| 27 | `JLHCNWGV_E139` | `has_fault_mode` | 04-Fault Location | SOFC stack |  | 05-Fault Mode | degradation |  |
| 28 | `JLHCNWGV_E140` | `has_fault_mode` | 04-Fault Location | SOFC stack |  | 05-Fault Mode | leakage |  |
| 29 | `JLHCNWGV_E141` | `has_fault_mode` | 04-Fault Location | reformer |  | 05-Fault Mode | degradation |  |
| 30 | `JLHCNWGV_E142` | `has_fault_mode` | 04-Fault Location | reformer |  | 05-Fault Mode | leakage |  |

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
