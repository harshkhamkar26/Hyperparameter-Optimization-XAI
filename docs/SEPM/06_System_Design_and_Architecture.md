# System Design and Architecture

## 1. System Objective
Design a reproducible research framework for optimizing imbalanced Bank Marketing classification models and evaluating their explanations.

## 2. High-Level Architecture

```text
UCI Bank Marketing Dataset
            ↓
     Data Validation/Audit
            ↓
 Prediction-time Feature Policy
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
   Optimized Classifiers
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

1. **Dataset Layer:** UCI Bank Marketing data.
2. **Validation Layer:** schema, target, missing/unknown values, duplicates and feature-timing checks.
3. **Preprocessing Layer:** numerical/categorical processing and train-fold-only transformations.
4. **Imbalance Layer:** class distribution analysis, class weighting and SMOTE where valid.
5. **Model Layer:** baseline and optimized tree-based/tabular classifiers.
6. **Optimization Layer:** reproducible HPO strategies under a fixed budget.
7. **Evaluation Layer:** precision, recall, F1, balanced accuracy, ROC-AUC, PR-AUC, confusion matrix and runtime.
8. **XAI Layer:** SHAP global and local explanations.
9. **Stability Layer:** ranking/top-k/association stability across seeds, folds or controlled samples.
10. **Reporting Layer:** experiment logs, tables, figures and research conclusions.

## 4. Design Principles

- No test-set information during HPO.
- Resampling only inside training folds where applicable.
- Prediction-time feature policy is fixed before experiments.
- Fixed random seeds and search budgets.
- Modular experiment configuration.
- Explicit recording of failed/invalid trials.
- No private customer data or credentials in the repository.
