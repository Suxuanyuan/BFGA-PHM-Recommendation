# 4-Class Classifier Testing Statistics — Stage 1: Method Paradigm

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
| Stage 1: Method Paradigm | 0.2538 | 0.3293 | 0.1943 | 0.1414 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.2538 | 0.3293 | 0.1943 | 0.1414 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.8769 | 0.8519 | 0.8221 | 0.8174 |

---

## Scenario: Missing-Top3

### Metric: Strict Top-1 Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.2621 | 0.2781 | 0.1493 | 0.0969 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.2621 | 0.2781 | 0.1493 | 0.0969 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.8769 | 0.8026 | 0.7805 | 0.8019 |

---

## Scenario: Missing-Top5

### Metric: Strict Top-1 Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.2726 | 0.2815 | 0.1405 | 0.0789 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.2726 | 0.2815 | 0.1405 | 0.0789 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.8789 | 0.7628 | 0.7750 | 0.8149 |

---

## Scenario: Missing-Top0

### Metric: Strict Top-1 Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.2705 | 0.3321 | 0.2733 | 0.1593 |

### Metric: Relaxed Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.2705 | 0.3321 | 0.2733 | 0.1593 |

### Metric: Relaxed Top-N Consistency

| Method | Language Model | LSTM | CNN | Decision Tree |
| --- | --- | --- | --- | --- |
| Stage 1: Method Paradigm | 0.8769 | 0.8864 | 0.8281 | 0.8126 |

---
