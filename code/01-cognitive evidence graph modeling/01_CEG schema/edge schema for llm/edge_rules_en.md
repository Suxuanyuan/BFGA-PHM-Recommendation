# 1. Scenario 1 Candidate Edges (Default Connection Relations)

| source_node_type | target_node_type | edge_type | edge_group |
| ---------------- | ---------------- | --------- | ---------- |
| 01-Object Domain | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 01-Object Domain | 16-Feature Extraction Algorithm | connect | Default Edge |
| 01-Object Domain | 17-Core Classifier Algorithm | connect | Default Edge |
| 01-Object Domain | 18-Data Generation Algorithm | connect | Default Edge |
| 01-Object Domain | 19-Training Optimization Algorithm | connect | Default Edge |
| 02-Object Type | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 02-Object Type | 16-Feature Extraction Algorithm | connect | Default Edge |
| 02-Object Type | 17-Core Classifier Algorithm | connect | Default Edge |
| 02-Object Type | 18-Data Generation Algorithm | connect | Default Edge |
| 02-Object Type | 19-Training Optimization Algorithm | connect | Default Edge |
| 03-Operating Conditions | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 03-Operating Conditions | 16-Feature Extraction Algorithm | connect | Default Edge |
| 03-Operating Conditions | 17-Core Classifier Algorithm | connect | Default Edge |
| 03-Operating Conditions | 18-Data Generation Algorithm | connect | Default Edge |
| 03-Operating Conditions | 19-Training Optimization Algorithm | connect | Default Edge |
| 04-Fault Location | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 04-Fault Location | 16-Feature Extraction Algorithm | connect | Default Edge |
| 04-Fault Location | 17-Core Classifier Algorithm | connect | Default Edge |
| 04-Fault Location | 18-Data Generation Algorithm | connect | Default Edge |
| 04-Fault Location | 19-Training Optimization Algorithm | connect | Default Edge |
| 05-Fault Mode | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 05-Fault Mode | 16-Feature Extraction Algorithm | connect | Default Edge |
| 05-Fault Mode | 17-Core Classifier Algorithm | connect | Default Edge |
| 05-Fault Mode | 18-Data Generation Algorithm | connect | Default Edge |
| 05-Fault Mode | 19-Training Optimization Algorithm | connect | Default Edge |
| 06-Fault Severity | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 06-Fault Severity | 16-Feature Extraction Algorithm | connect | Default Edge |
| 06-Fault Severity | 17-Core Classifier Algorithm | connect | Default Edge |
| 06-Fault Severity | 18-Data Generation Algorithm | connect | Default Edge |
| 06-Fault Severity | 19-Training Optimization Algorithm | connect | Default Edge |
| 07-Compound Fault | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 07-Compound Fault | 16-Feature Extraction Algorithm | connect | Default Edge |
| 07-Compound Fault | 17-Core Classifier Algorithm | connect | Default Edge |
| 07-Compound Fault | 18-Data Generation Algorithm | connect | Default Edge |
| 07-Compound Fault | 19-Training Optimization Algorithm | connect | Default Edge |
| 08-PHM Task | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 08-PHM Task | 16-Feature Extraction Algorithm | connect | Default Edge |
| 08-PHM Task | 17-Core Classifier Algorithm | connect | Default Edge |
| 08-PHM Task | 18-Data Generation Algorithm | connect | Default Edge |
| 08-PHM Task | 19-Training Optimization Algorithm | connect | Default Edge |
| 09-Problem Scenario | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 09-Problem Scenario | 16-Feature Extraction Algorithm | connect | Default Edge |
| 09-Problem Scenario | 17-Core Classifier Algorithm | connect | Default Edge |
| 09-Problem Scenario | 18-Data Generation Algorithm | connect | Default Edge |
| 09-Problem Scenario | 19-Training Optimization Algorithm | connect | Default Edge |
| 10-Dataset | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 10-Dataset | 16-Feature Extraction Algorithm | connect | Default Edge |
| 10-Dataset | 17-Core Classifier Algorithm | connect | Default Edge |
| 10-Dataset | 18-Data Generation Algorithm | connect | Default Edge |
| 10-Dataset | 19-Training Optimization Algorithm | connect | Default Edge |
| 11-Sensor Information | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 11-Sensor Information | 16-Feature Extraction Algorithm | connect | Default Edge |
| 11-Sensor Information | 17-Core Classifier Algorithm | connect | Default Edge |
| 11-Sensor Information | 18-Data Generation Algorithm | connect | Default Edge |
| 11-Sensor Information | 19-Training Optimization Algorithm | connect | Default Edge |
| 12-Training Data Availability | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 12-Training Data Availability | 16-Feature Extraction Algorithm | connect | Default Edge |
| 12-Training Data Availability | 17-Core Classifier Algorithm | connect | Default Edge |
| 12-Training Data Availability | 18-Data Generation Algorithm | connect | Default Edge |
| 12-Training Data Availability | 19-Training Optimization Algorithm | connect | Default Edge |
| 13-Noise Level | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 13-Noise Level | 16-Feature Extraction Algorithm | connect | Default Edge |
| 13-Noise Level | 17-Core Classifier Algorithm | connect | Default Edge |
| 13-Noise Level | 18-Data Generation Algorithm | connect | Default Edge |
| 13-Noise Level | 19-Training Optimization Algorithm | connect | Default Edge |
| 14-Computational Resource | 15-Data Preprocessing Algorithm | connect | Default Edge |
| 14-Computational Resource | 16-Feature Extraction Algorithm | connect | Default Edge |
| 14-Computational Resource | 17-Core Classifier Algorithm | connect | Default Edge |
| 14-Computational Resource | 18-Data Generation Algorithm | connect | Default Edge |
| 14-Computational Resource | 19-Training Optimization Algorithm | connect | Default Edge |


# Output JSON Format for Scenario 1 Candidate Edges

```json
[
  {
    "case_id": "<case_id>",
    "paper_title": "<paper_title>",
    "publish_year": <publish_year>,
    "publish_source": "<publish_source>",
    "cite_count": <cite_count>,
    "algorithm_hyperparameters": "<algorithm_hyperparameters>",
    "training_config": "<training_config>",
    "performance_metrics": "<performance_metrics>",
    "nodes": []
    "edges": [
    {
        "edge_id": "<case_id>_E001",
        "source_node_id": "<node_id>",
        "source_node_type": "<node_type>",
        "source_node_name": "<node_name>",
        "source_node_original_name": "<node_original_name>",
        "target_node_id": "<node_id>",
        "target_node_type": "<node_type>",
        "target_node_name": "<node_name>",
        "target_node_original_name": "<node_original_name>",
        "edge_type": "connects",
        "edge_group": "01-Default Edge",
        "evidence_level": "Low confidence",
        "edge_description": "<source_node_name/source_node_original_name> + connects + <target_node_name/target_node_original_name>",
        "edge_weight": null,
        "edge_nums": null
    }
    ]
  }
]
```


# 2. Scenario 2 Candidate Edges (Causal Relations)

## 2-0 Node Matching Cardinality and Processing Method

Before generating candidate edges, first count the **number of valid nodes** of the source class and target class respectively (see Note 1 for the validity criteria), to determine the edge processing method:

| Cardinality Case | Processing Method | Description |
| --- | --- | --- |
| source valid node count = 1, target valid node count >= 1 | **Program Directly Generated** | One-to-N, the matching relation is determined, directly assign edge_description |
| source valid node count >= 1, target valid node count = 1 | **Program Directly Generated** | N-to-One, the matching relation is determined, directly assign edge_description |
| source valid node count >= 2, target valid node count >= 2 | **LLM Judgment** | Many-to-many, the matching relation is uncertain, edge_description leaves null, and LLM subsequently determines which matching pairs truly exist in the literature |

> **Note**: Whether a node is "valid" is determined by Note 1: when **both** source_node_original_name and target_node_original_name are null, skip this edge.

> **Important: About Node 09 (Problem Scenario)**:
> - Node 09 allows multiple nodes in one paper (09_N1, 09_N2, 09_N3... incrementing), as long as the paper clearly points out multiple problems, all of them must be extracted.
> - Each 09 node independently participates in candidate edge generation, without mutual influence. For example, if the paper has 09_N1=Small Fault Samples and 09_N2=Distribution Discrepancy, then both 09 nodes will each generate candidate edges in Scenario 2-4 (induces_problem) and Scenario 3 (motivates).
> - When generating candidate edges, the `nodes_by_type["09-Problem Scenario"]` list will contain all 09 nodes, no special handling needed.

## 2-1 Program Directly Generated Causal Edges (Determined Matching Relation)

The following candidate edges have natural, almost certain causal associations in domain knowledge between source and target. **If the number of nodes satisfies the "One-to-N" or "N-to-One" condition, the program directly generates edge_description without LLM judgment**.

| source_node_type | target_node_type | edge_type | edge_group |
| --- | --- | --- | --- |
| 02-Object Type | 08-PHM Task | contains_phm_task | 02-Causal Edge |
| 04-Fault Location | 08-PHM Task | contains_phm_task | 02-Causal Edge |
| 05-Fault Mode | 08-PHM Task | contains_phm_task | 02-Causal Edge |
| 06-Fault Severity | 08-PHM Task | contains_phm_task | 02-Causal Edge |
| 04-Fault Location | 05-Fault Mode | has_fault_mode | 02-Causal Edge |

> **Note**: For the edge of 04-Fault Location -> 05-Fault Mode, see Note 5-1 for the exception rule of edge_description assignment.
>
> **Note (Severity Classification of 06 Nodes)**: The node_name of 06 nodes (Fault Severity) is divided into "Single Severity" and "Multiple Severities". "Multiple Severities" includes: explicitly mentioned grading, multiple fault diameter/depth values being compared, and slowly developing faults involving performance degradation/life degradation (such as RUL, degradation, remaining useful life, health state degradation curves). **Special Tip**: Slowly developing faults such as performance degradation, life prediction, RUL degradation are very easily misjudged as "Single Severity", but should actually be defined as "Multiple Severities".

## 2-2 Program Directly Generated Causal Edges (05→06 Special Rule)

| source_node_type | target_node_type | edge_type | edge_group |
| --- | --- | --- | --- |
| 05-Fault Mode | 06-Fault Severity | contains | 02-Causal Edge |

- **When 05 is a single node**: Program directly generates edge_description.
- **When 05 has multiple nodes**: Categorized into Scenario 2-3, where LLM judges which specific fault mode node forms a matching relation with the 06 node.

## 2-3 LLM Judgment Causal Edges (Many-to-Many, Uncertain Matching Relation)

The following candidate edges have causal associations in domain knowledge between source and target, but the matching relation is uncertain (many-to-many). **edge_description uniformly leaves null**, and LLM judges from the literature PDF which matching pairs truly exist.

| source_node_type | target_node_type | edge_type | edge_group |
| --- | --- | --- | --- |
| 01-Object Domain | 02-Object Type | contains | 02-Causal Edge |
| 02-Object Type | 04-Fault Location | contains | 02-Causal Edge |
| 02-Object Type | 03-Operating Conditions | contains | 02-Causal Edge |
| 05-Fault Mode (multiple nodes case) | 06-Fault Severity | contains | 02-Causal Edge |
| 05-Fault Mode | 07-Compound Fault | contains | 02-Causal Edge |
| 11-Sensor Information | 04-Fault Location | is collected on | 02-Causal Edge |
| 11-Sensor Information | 05-Fault Mode | can reflect  | 02-Causal Edge |
| 10-Dataset | 08-PHM Task | can be used for | 02-Causal Edge |

### 2-3 LLM Judgment Output Specification

LLM judges each source-target pair in the permutation and combination, and outputs a pure JSON array. Each record corresponds to a matching pair judged as "existing":

```json
[
  {"edge_id": "<edge_id>", "source_node_id": "<node_id>", "target_node_id": "<node_id>"},
  ...
]
```

**Program Parsing Rule**: After parsing the LLM output, assign the edge_description of the corresponding candidate edge in the edge_id list as `{source} contains {target}` (the program concatenates according to existing rules); candidate edges not appearing in the output are deleted from the candidate set.

## 2-4 Relations Requiring LLM Extraction (induces_problem)

The following candidate edges express "a factor causes/induces a problem scenario". The edge_description needs to be extracted verbatim from the PDF (different from the "yes/no judgment" of 2-3), and edge_description leaves null for LLM to supplement.

| source_node_type | target_node_type | edge_type | edge_group |
| --- | --- | --- | --- |
| 03-Operating Conditions | 09-Problem Scenario | induces_problem | 02-Causal Edge |
| 06-Fault Severity | 09-Problem Scenario | induces_problem | 02-Causal Edge |
| 07-Compound Fault | 09-Problem Scenario | induces_problem | 02-Causal Edge |
| 08-PHM Task | 09-Problem Scenario | induces_problem | 02-Causal Edge |
| 12-Training Data Availability | 09-Problem Scenario | induces_problem | 02-Causal Edge |
| 13-Noise Level | 09-Problem Scenario | induces_problem | 02-Causal Edge |
| 14-Computational Resource | 09-Problem Scenario | induces_problem | 02-Causal Edge |


# Output JSON Format for Scenario 2 Candidate Edges

```json
[
  {
    "case_id": "<case_id>",
    "paper_title": "<paper_title>",
    "publish_year": <publish_year>,
    "publish_source": "<publish_source>",
    "cite_count": <cite_count>,
    "algorithm_hyperparameters": "<algorithm_hyperparameters>",
    "training_config": "<training_config>",
    "performance_metrics": "<performance_metrics>",
    "nodes": []
    "edges": [
    {
        "edge_id": "<case_id>_E001",
        "source_node_id": "<node_id>",
        "source_node_type": "<node_type>",
        "source_node_name": "<node_name>",
        "source_node_original_name": "<node_original_name>",
        "target_node_id": "<node_id>",
        "target_node_type": "<node_type>",
        "target_node_name": "<node_name>",
        "target_node_original_name": "<node_original_name>",
        "edge_type": "<edge_type>",
        "edge_group": "02-Causal Edge",
        "evidence_level": "Normal confidence",
        "edge_description": "<source_node_name/source_node_original_name> + <edge_type> + <target_node_name/target_node_original_name>",
        "edge_weight": null,
        "edge_nums": null
    }
    ]
  }
]
```



# 3. Scenario 3 Candidate Edges (Evidence Relations)

> **Important (About Multiple Nodes of 09 Class)**: 09 class nodes (Problem Scenario) allow multiple nodes in one paper (09_N1, 09_N2, 09_N3...). Multiple 09 nodes each independently generate `motivates` candidate edges. For example, if a paper has both "Small Fault Samples" and "Distribution Discrepancy Problem" as two 09 nodes, each will generate evidence edges to the corresponding algorithm nodes (possibly producing multiple parallel evidence edges), all participating in extraction and judgment.

| source_node_type | target_node_type | edge_type | edge_group |
| --- | --- | --- | --- |
| 09-Problem Scenario | 19-Training Optimization Algorithm | motivates | 03-Evidence Edge |
| 12-Training Data Availability | 18-Data Generation Algorithm | motivates | 03-Evidence Edge |
| 12-Training Data Availability | 19-Training Optimization Algorithm | motivates | 03-Evidence Edge |
| 13-Noise Level | 15-Data Preprocessing Algorithm | motivates | 03-Evidence Edge |
| 13-Noise Level | 16-Feature Extraction Algorithm | motivates | 03-Evidence Edge |
| 09-Problem Scenario | 18-Data Generation Algorithm | motivates | 03-Evidence Edge |
| 09-Problem Scenario | 15-Data Preprocessing Algorithm | motivates | 03-Evidence Edge |
| 09-Problem Scenario | 16-Feature Extraction Algorithm | motivates | 03-Evidence Edge |
| 09-Problem Scenario | 17-Core Classifier Algorithm | motivates | 03-Evidence Edge |
| 07-Compound Fault | 16-Feature Extraction Algorithm | motivates | 03-Evidence Edge |
| 07-Compound Fault | 17-Core Classifier Algorithm | motivates | 03-Evidence Edge |
| 06-Fault Severity | 17-Core Classifier Algorithm | motivates | 03-Evidence Edge |

# Output JSON Format for Scenario 3 Candidate Edges

```json
[
  {
    "case_id": "<case_id>",
    "paper_title": "<paper_title>",
    "publish_year": <publish_year>,
    "publish_source": "<publish_source>",
    "cite_count": <cite_count>,
    "algorithm_hyperparameters": "<algorithm_hyperparameters>",
    "training_config": "<training_config>",
    "performance_metrics": "<performance_metrics>",
    "nodes": []
    "edges": [
    {
        "edge_id": "<case_id>_E001",
        "source_node_id": "<node_id>",
        "source_node_type": "<node_type>",
        "source_node_name": "<node_name>",
        "source_node_original_name": "<node_original_name>",
        "target_node_id": "<node_id>",
        "target_node_type": "<node_type>",
        "target_node_name": "<node_name>",
        "target_node_original_name": "<node_original_name>",
        "edge_type": "motivates",
        "edge_group": "03-Evidence Edge",
        "evidence_level": "High confidence",
        "edge_description": "<source_node_name/source_node_original_name> + motivates + <target_node_name/target_node_original_name>【English original text, one-sentence description of the relation between the nodes】",
        "edge_weight": null,
        "edge_nums": null
    }
    ]
  }
]
```

## Notes:

**Note 1 (Skip Rule)**: If **both** source_node_original_name **and** target_node_original_name are null, skip this edge directly, do not include in the edge JSON array.

**Note 2**: For edge_description, if source_node_name or target_node_name exists (not null), then use source_node_name or target_node_name in edge_description.

**Note 3**: For edge_description, if source_node_name or target_node_name does not exist (is null), then use source_node_original_name or target_node_original_name in edge_description.

**Note 4**: For Scenario 1 candidate edges, if both source_node_original_name and target_node_original_name exist (candidate edge is valid), then while generating the candidate edge JSON, directly assign edge_description as "<source_node_name/source_node_original_name> + connects + <target_node_name/target_node_original_name>". See Note 2 and Note 3 for assignment rules.

**Note 5**: For Scenario 2-1 candidate edges, if both source_node_original_name and target_node_original_name exist (candidate edge is valid), then while generating the candidate edge JSON, directly assign edge_description as "<source_node_name/source_node_original_name> + <edge_type> + <target_node_name/target_node_original_name>". See Note 2 and Note 3 for assignment rules.

**Note 5-1**: For Scenario 2-1 "| 04-Fault Location | 05-Fault Mode | has_fault_mode |" candidate edge, there is one exception: if "04-Fault Location" has only 1 node in one paper (same case_id) in the "node JSON array", then follow Note 5 requirements and directly assign edge_description; if "04-Fault Location" has multiple nodes, then do not assign edge_description (leave null), wait for subsequent LLM extraction.

**Note 5-2**: In the "node JSON array", the same "node_type" may have multiple nodes (multiple "node_id"), each node should independently judge candidate edges, rather than mixing the same "node_type" together.

**Note 5-3 (05→06 Special Rule)**: For "| 05-Fault Mode | 06-Fault Severity | contains |" candidate edges: if the number of valid nodes of 05 class (Fault Mode) = 1, then the program directly generates edge_description; if the number of valid nodes of 05 class >= 2, then edge_description leaves null, categorized into Scenario 2-3 for LLM to judge which specific fault mode forms a matching relation with the 06 node.

**Note 6**: For Scenario 2-3 candidate edges (many-to-many, LLM judgment type), the matching relation between source and target nodes is uncertain, edge_description uniformly leaves null. After LLM judges which matching pairs truly exist in the literature, the program parses the LLM output, assigns edge_description to the matching pairs judged as "existing" according to Note 5 rules, and deletes the matching pairs judged as "not existing".

**Note 7**: For Scenario 2-4 candidate edges (induces_problem), edge_description needs to be extracted from the PDF original text, edge_description leaves null for LLM to supplement later.

**Note 8**: For Scenario 3 candidate edges, edge_description needs to extract tone judgment and evidence field from the PDF original text, edge_description leaves null for LLM to supplement later.

**Note 9 (Multiple Problem Scenarios of 09 Nodes)**: Node 09 (Problem Scenario) allows multiple nodes (09_N1, 09_N2, 09_N3...) in one paper, **at most 3 nodes can be extracted per paper**, and each node independently selects one from the 10 options: "Small Fault Samples", "Zero Fault Samples", "Distribution Discrepancy Problem", "Uncertainty Problem", "Compound Fault Problem", "Complex System Problem", "Early Degradation Prediction Problem", "Multi-source Heterogeneous / Multi-modal Data Problem", "Trustworthy / Interpretable Problem", "Other Problem". If it really cannot be categorized into 9 types, you can choose "Other Problem". Multiple 09 nodes each independently participate in candidate edge generation, without mutual influence. For example, if a paper has 09_N1=Small Fault Samples and 09_N2=Distribution Discrepancy, then both 09 nodes will each generate candidate edges in Scenario 2-4 (induces_problem) and Scenario 3 (motivates).

**Note 10 (Easy Misjudgment Issue of "Multiple Severities" for 06 Nodes)**: The node_name options for 06 nodes (Fault Severity) are "Single Severity" or "Multiple Severities". **Special Note**: Slowly developing faults such as performance degradation, remaining useful life (RUL) prediction, health state degradation are very easily misjudged as "Single Severity", but should actually be defined as "Multiple Severities". Specific judgment rules:
- ❌ Misjudged as "Single Severity": The paper discusses slowly developing fault characteristics such as performance degradation, RUL prediction, health state assessment (progressive wear, crack propagation)
- ✅ Correctly Judged as "Multiple Severities": Involves degradation curves / multi-stage degradation (e.g., early → middle → late), multiple severity comparison experiments
- ✅ Correctly Judged as "Single Severity": Only injects a single fixed fault parameter, without involving any degradation process
