# Average Consistency Statistics Across 5 Scenarios (Algorithm)

> This report computes the arithmetic mean of the four percentages in `#### Region 1: Consistency Metrics` from `00-overall_statistics.md` for every hyperparameter subdirectory under `selected_test_set/output_data/<scenario>/`, across 5 test scenarios (Missing Top0/1/3/5/7) in the `selected_test_set` case_id sets.
>> Data source: `selected_test_set/output_data/<scenario>/<hyperparameter_subdir>/00-overall_statistics.md`; the 4 metrics are `Strict Consistency / Top-K Strict Consistency / Relaxed Consistency / Top-K Relaxed Consistency`.

## 1. Summary Table

### Region 1: Added Algorithm-Graph Inference Consistency

| Test Scenario | Hyperparameter Config | Hit Case Count | Strict Consistency | Top-K Strict Consistency | Relaxed Consistency | Top-K Relaxed Consistency |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Missing-Top0 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.43% | 40.00% | 37.98% | 58.55% |
| Missing-Top0 | Config 2 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 30.29% | 40.29% | 44.74% | 60.45% |
| Missing-Top0 | Config 3 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 26.00% | 41.43% | 38.93% | 62.12% |
| Missing-Top0 | Config 4 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.43% | 42.00% | 38.21% | 62.95% |
| Missing-Top0 | Config 5 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.43% | 41.14% | 38.21% | 61.29% |
| Missing-Top0 | Config 6 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 24.86% | 40.29% | 37.02% | 59.38% |
| Missing-Top1 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 24.86% | 38.57% | 36.90% | 55.93% |
| Missing-Top1 | Config 2 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 30.57% | 39.43% | 45.24% | 58.79% |
| Missing-Top1 | Config 3 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 27.43% | 40.29% | 40.52% | 59.98% |
| Missing-Top1 | Config 4 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.71% | 41.43% | 38.57% | 61.64% |
| Missing-Top1 | Config 5 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.14% | 40.57% | 37.50% | 60.10% |
| Missing-Top1 | Config 6 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 24.57% | 40.00% | 36.43% | 59.02% |
| Missing-Top3 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.14% | 39.14% | 37.14% | 57.60% |
| Missing-Top3 | Config 2 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 30.57% | 38.57% | 45.24% | 57.60% |
| Missing-Top3 | Config 3 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 30.00% | 40.00% | 44.21% | 59.74% |
| Missing-Top3 | Config 4 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 26.00% | 40.86% | 38.57% | 60.93% |
| Missing-Top3 | Config 5 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.14% | 40.86% | 37.26% | 60.57% |
| Missing-Top3 | Config 6 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 70 | 25.14% | 41.14% | 37.38% | 61.05% |
| Missing-Top5 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 25.00% | 39.29% | 37.20% | 58.16% |
| Missing-Top5 | Config 2 `Epoch_max=13_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 25.36% | 38.93% | 37.50% | 57.26% |
| Missing-Top5 | Config 3 `Epoch_max=15_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 25.00% | 38.93% | 37.05% | 57.26% |
| Missing-Top5 | Config 4 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 30.00% | 37.86% | 43.90% | 56.22% |
| Missing-Top5 | Config 5 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 28.93% | 38.93% | 42.02% | 57.71% |
| Missing-Top5 | Config 6 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 27.50% | 39.64% | 40.09% | 58.30% |
| Missing-Top5 | Config 7 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 25.36% | 40.00% | 37.65% | 58.90% |
| Missing-Top5 | Config 8 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10` | 56 | 24.64% | 40.36% | 36.61% | 59.50% |

---

1、Test Scenario: Missing-Top0.
1-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.43%；
     - Top-K Strict Consistency average: 40.00%；
     - Relaxed Consistency average: 37.98%；
     - Top-K Relaxed Consistency average: 58.55%；
     - Hit Case Count: 70。

1-2, Hyperparameter Config 2: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 30.29%；
     - Top-K Strict Consistency average: 40.29%；
     - Relaxed Consistency average: 44.74%；
     - Top-K Relaxed Consistency average: 60.45%；
     - Hit Case Count: 70。

1-3, Hyperparameter Config 3: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 26.00%；
     - Top-K Strict Consistency average: 41.43%；
     - Relaxed Consistency average: 38.93%；
     - Top-K Relaxed Consistency average: 62.12%；
     - Hit Case Count: 70。

1-4, Hyperparameter Config 4: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.43%；
     - Top-K Strict Consistency average: 42.00%；
     - Relaxed Consistency average: 38.21%；
     - Top-K Relaxed Consistency average: 62.95%；
     - Hit Case Count: 70。

1-5, Hyperparameter Config 5: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.43%；
     - Top-K Strict Consistency average: 41.14%；
     - Relaxed Consistency average: 38.21%；
     - Top-K Relaxed Consistency average: 61.29%；
     - Hit Case Count: 70。

1-6, Hyperparameter Config 6: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 24.86%；
     - Top-K Strict Consistency average: 40.29%；
     - Relaxed Consistency average: 37.02%；
     - Top-K Relaxed Consistency average: 59.38%；
     - Hit Case Count: 70。



2、Test Scenario: Missing-Top1.
2-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 24.86%；
     - Top-K Strict Consistency average: 38.57%；
     - Relaxed Consistency average: 36.90%；
     - Top-K Relaxed Consistency average: 55.93%；
     - Hit Case Count: 70。

2-2, Hyperparameter Config 2: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 30.57%；
     - Top-K Strict Consistency average: 39.43%；
     - Relaxed Consistency average: 45.24%；
     - Top-K Relaxed Consistency average: 58.79%；
     - Hit Case Count: 70。

2-3, Hyperparameter Config 3: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 27.43%；
     - Top-K Strict Consistency average: 40.29%；
     - Relaxed Consistency average: 40.52%；
     - Top-K Relaxed Consistency average: 59.98%；
     - Hit Case Count: 70。

2-4, Hyperparameter Config 4: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.71%；
     - Top-K Strict Consistency average: 41.43%；
     - Relaxed Consistency average: 38.57%；
     - Top-K Relaxed Consistency average: 61.64%；
     - Hit Case Count: 70。

2-5, Hyperparameter Config 5: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.14%；
     - Top-K Strict Consistency average: 40.57%；
     - Relaxed Consistency average: 37.50%；
     - Top-K Relaxed Consistency average: 60.10%；
     - Hit Case Count: 70。

2-6, Hyperparameter Config 6: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 24.57%；
     - Top-K Strict Consistency average: 40.00%；
     - Relaxed Consistency average: 36.43%；
     - Top-K Relaxed Consistency average: 59.02%；
     - Hit Case Count: 70。



3、Test Scenario: Missing-Top3.
3-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.14%；
     - Top-K Strict Consistency average: 39.14%；
     - Relaxed Consistency average: 37.14%；
     - Top-K Relaxed Consistency average: 57.60%；
     - Hit Case Count: 70。

3-2, Hyperparameter Config 2: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 30.57%；
     - Top-K Strict Consistency average: 38.57%；
     - Relaxed Consistency average: 45.24%；
     - Top-K Relaxed Consistency average: 57.60%；
     - Hit Case Count: 70。

3-3, Hyperparameter Config 3: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 30.00%；
     - Top-K Strict Consistency average: 40.00%；
     - Relaxed Consistency average: 44.21%；
     - Top-K Relaxed Consistency average: 59.74%；
     - Hit Case Count: 70。

3-4, Hyperparameter Config 4: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 26.00%；
     - Top-K Strict Consistency average: 40.86%；
     - Relaxed Consistency average: 38.57%；
     - Top-K Relaxed Consistency average: 60.93%；
     - Hit Case Count: 70。

3-5, Hyperparameter Config 5: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.14%；
     - Top-K Strict Consistency average: 40.86%；
     - Relaxed Consistency average: 37.26%；
     - Top-K Relaxed Consistency average: 60.57%；
     - Hit Case Count: 70。

3-6, Hyperparameter Config 6: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.14%；
     - Top-K Strict Consistency average: 41.14%；
     - Relaxed Consistency average: 37.38%；
     - Top-K Relaxed Consistency average: 61.05%；
     - Hit Case Count: 70。



4、Test Scenario: Missing-Top5.
4-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.00%；
     - Top-K Strict Consistency average: 39.29%；
     - Relaxed Consistency average: 37.20%；
     - Top-K Relaxed Consistency average: 58.16%；
     - Hit Case Count: 56。

4-2, Hyperparameter Config 2: `Epoch_max=13_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.36%；
     - Top-K Strict Consistency average: 38.93%；
     - Relaxed Consistency average: 37.50%；
     - Top-K Relaxed Consistency average: 57.26%；
     - Hit Case Count: 56。

4-3, Hyperparameter Config 3: `Epoch_max=15_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.00%；
     - Top-K Strict Consistency average: 38.93%；
     - Relaxed Consistency average: 37.05%；
     - Top-K Relaxed Consistency average: 57.26%；
     - Hit Case Count: 56。

4-4, Hyperparameter Config 4: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 30.00%；
     - Top-K Strict Consistency average: 37.86%；
     - Relaxed Consistency average: 43.90%；
     - Top-K Relaxed Consistency average: 56.22%；
     - Hit Case Count: 56。

4-5, Hyperparameter Config 5: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 28.93%；
     - Top-K Strict Consistency average: 38.93%；
     - Relaxed Consistency average: 42.02%；
     - Top-K Relaxed Consistency average: 57.71%；
     - Hit Case Count: 56。

4-6, Hyperparameter Config 6: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 27.50%；
     - Top-K Strict Consistency average: 39.64%；
     - Relaxed Consistency average: 40.09%；
     - Top-K Relaxed Consistency average: 58.30%；
     - Hit Case Count: 56。

4-7, Hyperparameter Config 7: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 25.36%；
     - Top-K Strict Consistency average: 40.00%；
     - Relaxed Consistency average: 37.65%；
     - Top-K Relaxed Consistency average: 58.90%；
     - Hit Case Count: 56。

4-8, Hyperparameter Config 8: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10`。
   - Region 1: Added Algorithm-Graph Inference Consistency
     - Strict Consistency average: 24.64%；
     - Top-K Strict Consistency average: 40.36%；
     - Relaxed Consistency average: 36.61%；
     - Top-K Relaxed Consistency average: 59.50%；
     - Hit Case Count: 56。

