# System Design and Architecture

## 1. System Objective
Design a reproducible research framework for optimizing imbalanced cybersecurity intrusion-detection models and evaluating their explanations.

## 2. High-Level Architecture

```text
Public Cybersecurity IDS Dataset
            ↓
     Data Validation/Audit
            ↓
 Leakage-safe Preprocessing
            ↓
     Imbalance Analysis
            ↓
       Baseline Models
            ↓
 ┌──────────┼─────────────┐
 │          │             │
Grid      Random      Optuna/TPE
Search    Search      Optimization
 └──────────┼─────────────┘
            ↓
   Optimized IDS Models
            ↓
 Performance + Efficiency
            ↓
      SHAP Explanations
            ↓
 Explanation Stability
            ↓
 Comparative Research Analysis
```

## 3. Major Components

1. **Dataset Layer:** selected public IDS dataset.
2. **Validation Layer:** schema, labels, missing values, duplicates and leakage checks.
3. **Preprocessing Layer:** numerical/categorical processing and train-fold-only transformations.
4. **Imbalance Layer:** class distribution analysis and suitable mitigation strategies.
5. **Model Layer:** baseline and optimized tree-based/tabular IDS classifiers.
6. **Optimization Layer:** reproducible HPO strategies under a fixed budget.
7. **Evaluation Layer:** F1, precision, recall, balanced accuracy, ROC-AUC, PR-AUC, confusion matrix and runtime.
8. **XAI Layer:** SHAP global and local explanations.
9. **Stability Layer:** ranking/top-k/association stability across seeds, folds or controlled samples.
10. **Reporting Layer:** experiment logs, tables, figures and research conclusions.

## 4. Design Principles

- No test-set information during HPO.
- Resampling only inside training folds where applicable.
- Fixed random seeds and search budgets.
- Modular experiment configuration.
- Explicit recording of failed/invalid trials.
- Security-conscious handling of data and credentials.
