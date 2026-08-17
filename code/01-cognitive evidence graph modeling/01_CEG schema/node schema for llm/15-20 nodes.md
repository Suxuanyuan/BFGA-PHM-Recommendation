# Nodes 15-20: Unified Extraction and Calibration of Algorithm-Type Nodes (v5)

## [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

---

## [Task]

Extract 6 types of algorithm nodes (15-20) involved in the paper's algorithm flow in one pass, then perform a global calibration of the role-importance level for nodes 15-19 ("Highest Importance" applies to only one).

### The 6 Types of Nodes Involved

| No. | Node Type | Multiple Nodes | "Not Mentioned" Allowed |
|------|---------|-------|------------|
| 15 | Data Preprocessing Algorithm | No (1) | Yes |
| 16 | Feature Extraction Algorithm | No (1) | Yes |
| 17 | Core Classifier Algorithm | **No (Required, 1)** | **No** |
| 18 | Data Generation Algorithm | No (1) | Yes |
| 19 | Training Optimization Algorithm | No (1) | Yes |
| 20 | Role-Importance Calibration | — | — |

⚠️ Each type (15-19) **outputs only 1 node**, selecting the most typical / important one of that type.

---

## [JSON Format]

**⚠️ Outer `[...]`, all 6 nodes must be output without omission.**

```json
[
  { "node_id": "<case_id>_15_N1", "node_type": "15-Data Preprocessing Algorithm", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_16_N1", "node_type": "16-Feature Extraction Algorithm", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_17_N1", "node_type": "17-Core Classifier Algorithm", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_18_N1", "node_type": "18-Data Generation Algorithm", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_19_N1", "node_type": "19-Training Optimization Algorithm", "node_original_name": "", "node_name": null, "node_description": "", "node_case_id_list": null },
  { "node_id": "<case_id>_20_N1", "node_type": "20-Algorithm Node Role-Importance Calibration", "node_original_name": "Calibration Node", "node_name": null, "node_description": "", "node_case_id_list": null }
]
```

---

## [Definitions of Each Node Type]

### Node 15: Data Preprocessing Algorithm

**Definition**: Algorithms that perform cleaning, enhancement, or normalization on the signal before the accurate signal enters the feature extraction or classification model.

**Discrimination**: Denoising / filtering / resampling / normalization / framing / sliding-window segmentation / outlier removal.

| Example | Classification |
|------|------|
| Wavelet denoising / EMD / VMD used only for signal decomposition | →15 |
| EMD / VMD used for extracting time-frequency features | →16 |
| Generating new samples via a generative model | →18 |
| Simple noise addition / cropping as data augmentation | →15 |

**Fields**: `node_original_name` = the most core algorithm in English; `node_description` = describe the role in English. **Extract only those used in the paper's own method.**

---

### Node 16: Feature Extraction Algorithm

**Definition**: Extracting feature vectors or representations that characterize equipment state from signals / data.

**Discrimination**: Signal → feature vector / embedding representation (not the final classification / regression result).

| Example | Classification |
|------|------|
| Autoencoder using only the encoder output as features | →16 |
| Autoencoder using the decoder to generate new samples | →18 |
| CNN / ResNet backbone | →16 |
| Classification head / inseparable end-to-end model | →17 |
| EMD / VMD extracting modal components as features | →16 |
| Attention used only for feature weighting | →16 |
| Attention as the core of the classifier model | →17 |

**Fields**: `node_original_name` = the most core algorithm in English; `node_description` = describe the role in English. **Extract only those used in the paper's own method.**

---

### Node 17: Core Classifier Algorithm

⚠️ **Each paper must extract exactly 1; "Not Mentioned" is not allowed.**

**Definition**: The decision model that directly outputs the fault diagnosis / anomaly detection / life prediction result; it is the terminal decision component of the PHM algorithm chain.

**Discrimination**: The most downstream decision module in the paper's algorithm flow.

| Example | Classification |
|------|------|
| End-to-end deep model directly outputs the diagnosis result | →17 |
| Ensemble model (RF / XGBoost / AdaBoost) | →17 |
| SVM / KNN / Softmax | →17 |
| Backbone + classification head split | Backbone →16, classification head →17 |

**Fields**: `node_original_name` = the most core algorithm in English (**required**); `node_description` = describe the role in English. **Extract only those used in the paper's own method.**

---

### Node 18: Data Generation Algorithm

**Definition**: Producing new training samples / simulation data (sample augmentation / few-shot supplementation / virtual data construction).

**Discrimination**: The algorithm's purpose is to generate new samples.

| Example | Classification |
|------|------|
| GAN / VAE / diffusion model used for generation | →18 |
| SMOTE / oversampling / interpolation generation | →18 |
| Simple cropping / noise addition | →15 |
| Digital twin simulation | →18 |

**Fields**: `node_original_name` = the most core algorithm in English, fill in `"Not Mentioned"` if none; `node_description` = describe the role in English, fill in `"Not Mentioned"` if not mentioned. **Extract only those used in the paper's own method.**

---

### Node 19: Training Optimization Algorithm

**Definition**: Advanced learning strategies used in the paper to **optimize model parameters** or **solve multi-task / multi-objective problems**; they are the core methodological research focus of the authors.

**⚠️ The following should NOT be classified into Node 19**: General optimizers like Adam / SGD / RMSprop / Adagrad; general loss functions like CrossEntropyLoss / MSELoss; regularization techniques like BatchNormalization / Dropout.

**Discrimination**: Whether the paper treats this as a methodological innovation or research focus, rather than only as a default configuration.

| Category | Example |
|------|------|
| Transfer Learning / Domain Adaptation | Pre-training-fine-tuning, domain generalization, meta-learning (MAML, etc.) |
| Multi-Task Learning | MTL shared encoders, GradNorm, task weight optimization |
| Reinforcement Learning Decision-Making | Policy Gradient / DQN / PPO |
| Loss Function Design | Custom composite loss (classification + contrastive + alignment, etc.) |
| Curriculum Learning / Adversarial Training | Easy-to-hard staged training, GAN adversarial robustness |

| Example | Classification |
|------|------|
| Pre-training-fine-tuning / meta-learning / MTL | →19 |
| Domain Adaptation (DANN / CDAN / CORAL) | →19 |
| Knowledge Distillation (cross-domain transfer) | →19 |
| Knowledge Distillation (model compression) | Not →19 |
| Adam / SGD / RMSprop / CrossEntropy | Not →19 |
| CycleGAN for cross-domain alignment | →19 |
| CycleGAN for sample augmentation | →18 |

**Fields**: `node_original_name` = the most core algorithm in English, fill in `"Not Mentioned"` if none; `node_description` = describe the role in English, fill in `"Not Mentioned"` if not mentioned. **Extract only those used in the paper's own method.**

---

## [Node 20: Global Calibration]

⚠️ **Among all 5 algorithm nodes (15-19) of the same paper, "Highest Importance" must be exactly 1; 2 or more are prohibited.**

**Decision**:
1. Collect the original role descriptions of nodes 15-19
2. Read the paper's methods / ablation experiments / discussion sections
3. When quantitative comparisons exist: removing a certain algorithm causes the largest performance drop → that algorithm = **Highest Importance**
4. When no quantitative comparisons exist: the authors explicitly point out "core contribution" → Highest Importance; multiple algorithms equally important → choose the most downstream in the algorithm flow
5. Unable to distinguish → all → **General Importance**

**Node 20 `node_description` Format**: List each node's description and calibration level in node_id order, formatted as `<node_id> (<one-sentence description>) → <level>`, separated by semicolons.
For example: `15 (signal normalization) → General Importance; 16 (1DCNN feature extraction) → Highest Importance; 17 (softmax classification layer) → Not Mentioned; 18 (SMOTE augmentation) → Not Mentioned; 19 (pre-training-fine-tuning) → General Importance`

---

## [Mandatory Constraints]

1. **node_original_name fills in only the accurate English name of the single most core algorithm**; commas / enumeration commas / semicolons / slashes connecting multiple are prohibited
2. `node_name` is always `null`
3. "Highest Importance" appears **only once** among 15-19
4. Node 17 **is required**; "Not Mentioned" is not allowed
5. **Extract only those used in the paper's own method**, ignoring Introduction / Baseline methods
6. When `node_description` is not "Not Mentioned", fill in an English description
