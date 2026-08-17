# Average Consistency Statistics Across 5 Scenarios (Paradigm-Induction)

> This report computes the arithmetic mean of the four percentages in `#### Region 1: Consistency Metrics (-Paradigm)` from `00-overall_statistics.md` for every hyperparameter subdirectory under `selected_test_set/output_data/<scenario>-Paradigm/`, across 5 test scenarios (Missing Top0/1/3/5/7) in the `selected_test_set` case_id sets.
>> Data source: `selected_test_set/output_data/<scenario>-Paradigm/<hyperparameter_subdir>/00-overall_statistics.md`; the 4 metrics are `Strict Consistency / Top-K Strict Consistency / Relaxed Consistency / Top-K Relaxed Consistency` (already aggregated to category-level consistency for 15-19 `*-Paradigm`).

## 1. Summary Table

### Region 1: Added Induction-Graph Inference Consistency

| Test Scenario | Hyperparameter Config | Hit Case Count | Strict Consistency | Top-K Strict Consistency | Relaxed Consistency | Top-K Relaxed Consistency |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Missing-Top0 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.52% | 85.43% | 45.52% | 85.43% |
| Missing-Top0 | Config 2 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 46.95% | 87.33% | 46.95% | 87.33% |
| Missing-Top0 | Config 3 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.88% | 86.26% | 45.88% | 86.26% |
| Missing-Top0 | Config 4 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.29% | 87.81% | 45.29% | 87.81% |
| Missing-Top0 | Config 5 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.17% | 87.81% | 45.17% | 87.81% |
| Missing-Top0 | Config 6 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 46.00% | 86.38% | 46.00% | 86.38% |
| Missing-Top1 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.12% | 85.26% | 45.12% | 85.26% |
| Missing-Top1 | Config 2 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 46.38% | 85.50% | 46.38% | 85.50% |
| Missing-Top1 | Config 3 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.60% | 85.98% | 45.60% | 85.98% |
| Missing-Top1 | Config 4 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 44.76% | 86.45% | 44.76% | 86.45% |
| Missing-Top1 | Config 5 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.00% | 86.81% | 45.00% | 86.81% |
| Missing-Top1 | Config 6 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 44.64% | 84.91% | 44.64% | 84.91% |
| Missing-Top3 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 44.05% | 84.95% | 44.05% | 84.95% |
| Missing-Top3 | Config 2 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 45.55% | 85.98% | 45.55% | 85.98% |
| Missing-Top3 | Config 3 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 43.93% | 86.74% | 43.93% | 86.74% |
| Missing-Top3 | Config 4 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 43.93% | 86.38% | 43.93% | 86.38% |
| Missing-Top3 | Config 5 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 43.21% | 86.38% | 43.21% | 86.38% |
| Missing-Top3 | Config 6 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 70 | 43.21% | 85.67% | 43.21% | 85.67% |
| Missing-Top5 | Config 1 `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 56 | 42.26% | 84.41% | 42.26% | 84.41% |
| Missing-Top5 | Config 2 `Epoch_max=13_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 56 | 41.82% | 83.51% | 41.82% | 83.51% |
| Missing-Top5 | Config 3 `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 56 | 44.58% | 84.26% | 44.58% | 84.26% |
| Missing-Top5 | Config 4 `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 56 | 43.45% | 85.15% | 43.45% | 85.15% |
| Missing-Top5 | Config 5 `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 56 | 42.71% | 83.21% | 42.71% | 83.21% |
| Missing-Top5 | Config 6 `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 56 | 42.11% | 84.41% | 42.11% | 84.41% |
| Missing-Top5 | Config 7 `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm` | 56 | 43.30% | 84.41% | 43.30% | 84.41% |


---

1、Test Scenario: Missing-Top0-Paradigm。
1-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.52%；
     - Top-K Strict Consistency average: 85.43%；
     - Relaxed Consistency average: 45.52%；
     - Top-K Relaxed Consistency average: 85.43%；
     - Hit Case Count: 70。

1-2, Hyperparameter Config 2: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 46.95%；
     - Top-K Strict Consistency average: 87.33%；
     - Relaxed Consistency average: 46.95%；
     - Top-K Relaxed Consistency average: 87.33%；
     - Hit Case Count: 70。

1-3, Hyperparameter Config 3: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.88%；
     - Top-K Strict Consistency average: 86.26%；
     - Relaxed Consistency average: 45.88%；
     - Top-K Relaxed Consistency average: 86.26%；
     - Hit Case Count: 70。

1-4, Hyperparameter Config 4: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.29%；
     - Top-K Strict Consistency average: 87.81%；
     - Relaxed Consistency average: 45.29%；
     - Top-K Relaxed Consistency average: 87.81%；
     - Hit Case Count: 70。

1-5, Hyperparameter Config 5: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.17%；
     - Top-K Strict Consistency average: 87.81%；
     - Relaxed Consistency average: 45.17%；
     - Top-K Relaxed Consistency average: 87.81%；
     - Hit Case Count: 70。

1-6, Hyperparameter Config 6: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 46.00%；
     - Top-K Strict Consistency average: 86.38%；
     - Relaxed Consistency average: 46.00%；
     - Top-K Relaxed Consistency average: 86.38%；
     - Hit Case Count: 70。



2、Test Scenario: Missing-Top1-Paradigm。
2-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.12%；
     - Top-K Strict Consistency average: 85.26%；
     - Relaxed Consistency average: 45.12%；
     - Top-K Relaxed Consistency average: 85.26%；
     - Hit Case Count: 70。

2-2, Hyperparameter Config 2: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 46.38%；
     - Top-K Strict Consistency average: 85.50%；
     - Relaxed Consistency average: 46.38%；
     - Top-K Relaxed Consistency average: 85.50%；
     - Hit Case Count: 70。

2-3, Hyperparameter Config 3: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.60%；
     - Top-K Strict Consistency average: 85.98%；
     - Relaxed Consistency average: 45.60%；
     - Top-K Relaxed Consistency average: 85.98%；
     - Hit Case Count: 70。

2-4, Hyperparameter Config 4: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 44.76%；
     - Top-K Strict Consistency average: 86.45%；
     - Relaxed Consistency average: 44.76%；
     - Top-K Relaxed Consistency average: 86.45%；
     - Hit Case Count: 70。

2-5, Hyperparameter Config 5: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.00%；
     - Top-K Strict Consistency average: 86.81%；
     - Relaxed Consistency average: 45.00%；
     - Top-K Relaxed Consistency average: 86.81%；
     - Hit Case Count: 70。

2-6, Hyperparameter Config 6: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 44.64%；
     - Top-K Strict Consistency average: 84.91%；
     - Relaxed Consistency average: 44.64%；
     - Top-K Relaxed Consistency average: 84.91%；
     - Hit Case Count: 70。



3、Test Scenario: Missing-Top3-Paradigm。
3-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 44.05%；
     - Top-K Strict Consistency average: 84.95%；
     - Relaxed Consistency average: 44.05%；
     - Top-K Relaxed Consistency average: 84.95%；
     - Hit Case Count: 70。

3-2, Hyperparameter Config 2: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 45.55%；
     - Top-K Strict Consistency average: 85.98%；
     - Relaxed Consistency average: 45.55%；
     - Top-K Relaxed Consistency average: 85.98%；
     - Hit Case Count: 70。

3-3, Hyperparameter Config 3: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 43.93%；
     - Top-K Strict Consistency average: 86.74%；
     - Relaxed Consistency average: 43.93%；
     - Top-K Relaxed Consistency average: 86.74%；
     - Hit Case Count: 70。

3-4, Hyperparameter Config 4: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 43.93%；
     - Top-K Strict Consistency average: 86.38%；
     - Relaxed Consistency average: 43.93%；
     - Top-K Relaxed Consistency average: 86.38%；
     - Hit Case Count: 70。

3-5, Hyperparameter Config 5: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 43.21%；
     - Top-K Strict Consistency average: 86.38%；
     - Relaxed Consistency average: 43.21%；
     - Top-K Relaxed Consistency average: 86.38%；
     - Hit Case Count: 70。

3-6, Hyperparameter Config 6: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 43.21%；
     - Top-K Strict Consistency average: 85.67%；
     - Relaxed Consistency average: 43.21%；
     - Top-K Relaxed Consistency average: 85.67%；
     - Hit Case Count: 70。



4、Test Scenario: Missing-Top5-Paradigm。
4-1, Hyperparameter Config 1: `Epoch_max=11_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 42.26%；
     - Top-K Strict Consistency average: 84.41%；
     - Relaxed Consistency average: 42.26%；
     - Top-K Relaxed Consistency average: 84.41%；
     - Hit Case Count: 56。

4-2, Hyperparameter Config 2: `Epoch_max=13_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 41.82%；
     - Top-K Strict Consistency average: 83.51%；
     - Relaxed Consistency average: 41.82%；
     - Top-K Relaxed Consistency average: 83.51%；
     - Hit Case Count: 56。

4-3, Hyperparameter Config 3: `Epoch_max=1_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 44.58%；
     - Top-K Strict Consistency average: 84.26%；
     - Relaxed Consistency average: 44.58%；
     - Top-K Relaxed Consistency average: 84.26%；
     - Hit Case Count: 56。

4-4, Hyperparameter Config 4: `Epoch_max=3_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 43.45%；
     - Top-K Strict Consistency average: 85.15%；
     - Relaxed Consistency average: 43.45%；
     - Top-K Relaxed Consistency average: 85.15%；
     - Hit Case Count: 56。

4-5, Hyperparameter Config 5: `Epoch_max=5_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 42.71%；
     - Top-K Strict Consistency average: 83.21%；
     - Relaxed Consistency average: 42.71%；
     - Top-K Relaxed Consistency average: 83.21%；
     - Hit Case Count: 56。

4-6, Hyperparameter Config 6: `Epoch_max=7_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 42.11%；
     - Top-K Strict Consistency average: 84.41%；
     - Relaxed Consistency average: 42.11%；
     - Top-K Relaxed Consistency average: 84.41%；
     - Hit Case Count: 56。

4-7, Hyperparameter Config 7: `Epoch_max=9_Belief_thred=0.95_TopK=5_pruning_gamma=2_pruning_hardcap=3_pruning_thred=1.10-Paradigm`。
   - Region 1: Added Induction-Graph Inference Consistency
     - Strict Consistency average: 43.30%；
     - Top-K Strict Consistency average: 84.41%；
     - Relaxed Consistency average: 43.30%；
     - Top-K Relaxed Consistency average: 84.41%；
     - Hit Case Count: 56。


