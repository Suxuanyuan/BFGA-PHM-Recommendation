# Node 00: Hyperparameter Extraction

## [Output Requirements] (Must be strictly followed)

**Directly output a pure JSON array, starting from `[` and ending with `]`, without any other text in between.**

---

## [Task]

Extract hyperparameter configuration information from the paper and output a JSON array.

## [JSON Format]

```json
[
  { "node_id": "N1", "node_type": "00-Hyperparameter Extraction", "algorithm_hyperparameters": "", "training_config": "", "performance_metrics": "" }
]
```

## [Extraction Content]

| Field | Meaning | Paper Example |
|------|------|---------|
| algorithm_hyperparameters | Algorithm hyperparameters (learning rate / batch size / layers, etc.) | learning rate=0.001, batch size=32, epochs=100 |
| training_config | Training configuration (optimizer / epochs / decay / regularization) | optimizer=Adam, lr schedule=step, dropout=0.5 |
| performance_metrics | Performance metrics (accuracy / F1 / AUC / RMSE, etc.) | accuracy=97.34%, F1=0.965, AUC=0.98 |

When encountering new expressions: training management (early stopping / scheduler) → training_config; model architecture (layers / width) → algorithm_hyperparameters; experimental result values → performance_metrics.

---

## [Mandatory Constraints]

1. **The content of the three fields must be the original English text**, no translation or fabrication
2. **Extract only those used by the paper's own method**, ignore hyperparameters of Introduction / Baseline methods
3. node_id is fixed as `N1`
