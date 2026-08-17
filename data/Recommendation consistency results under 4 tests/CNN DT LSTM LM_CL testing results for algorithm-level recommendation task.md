# 4-Class Classifier Testing Statistics — Stage 2: Specific Algorithm

- Generated at: 2026-07-08 14:34:38
- Method column order: Language Model, LSTM, CNN, Decision Tree
- Missing scenario order: Missing-Top1, Missing-Top3, Missing-Top5, Missing-Top0

> Metric definitions (following the source MD specification):
> - **Strict Top-1 Consistency**: proportion of categories where the Top-1 recommendation exactly matches the GT node_name.
> - **Relaxed Consistency**: per the shared-module v10 specification (Top-N=1).
> - **Relaxed Top-N Consistency**: proportion of categories where the GT appears in the Top-N candidate list.

---

## Scenario: Missing-Top1

### Metric: Strict Top-1 Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.2019 | 0.1879 | 0.1362 | 0.0607 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.2019 | 0.1879 | 0.1362 | 0.0607 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.5021 | 0.5269 | 0.5195 | 0.4429 |

---

## Scenario: Missing-Top3

### Metric: Strict Top-1 Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.2043 | 0.1688 | 0.0933 | 0.0298 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.2043 | 0.1688 | 0.0933 | 0.0298 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.4986 | 0.5226 | 0.5124 | 0.4381 |

---

## Scenario: Missing-Top5

### Metric: Strict Top-1 Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.1824 | 0.0899 | 0.0170 | 0.0238 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.1824 | 0.0899 | 0.0170 | 0.0238 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.4923 | 0.4548 | 0.4842 | 0.4152 |

---


## Scenario: Missing-Top0

### Metric: Strict Top-1 Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.2102 | 0.1807 | 0.1457 | 0.1026 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.2102 | 0.1807 | 0.1457 | 0.1026 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 2: Specific Algorithm | 0.4950 | 0.5333 | 0.5124 | 0.4719 |

---
