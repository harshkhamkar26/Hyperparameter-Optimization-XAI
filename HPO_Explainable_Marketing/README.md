# Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing

Research project using the UCI Bank Marketing dataset for imbalanced binary classification, hyperparameter optimization (HPO), multi-objective optimization, threshold optimization, robustness analysis, and explainable AI (SHAP).

## Dataset
Place the UCI Bank Marketing file locally at:
data/raw/bank-additional-full.csv

Target variable: y
- yes: customer subscribed to a term deposit
- no: customer did not subscribe

The dataset itself is not committed to GitHub; use the official UCI Bank Marketing source and keep the raw CSV locally.

## Research Pipeline
1. Data understanding
2. EDA and class-imbalance analysis
3. Leakage-safe preprocessing
4. Baseline models
5. Imbalance strategies
6. Hyperparameter optimization
7. Multi-objective HPO
8. Threshold optimization
9. Robustness analysis
10. SHAP explainability
11. Explanation stability
12. Final research results

## Reproducibility
All preprocessing, imbalance handling, model training, optimization, evaluation, and explainability steps should be leakage-safe and reproducible.
