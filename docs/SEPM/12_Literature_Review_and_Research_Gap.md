# Literature Review and Research Gap

## 1. Purpose
This document records the literature review used to justify the selected dataset, binary classification problem and research direction. It is intended to prevent the project from presenting an already-published combination as a new contribution.

## 2. Selected Dataset and Classification Task
The project uses the UCI Bank Marketing dataset. The binary target `y` represents whether a customer subscribed to a term deposit (`yes`/`no`). This is a practically meaningful classification problem because marketing resources are limited and the cost of contacting customers who are unlikely to convert differs from the value of reaching likely subscribers.

## 3. Relevant Literature

### Paper 1 — Nasir et al. (2026)
**Marketing analytics in banking 4.0: A two-stage explainable AI framework for high-accuracy and well-calibrated predictions.** PLOS ONE, 21(5), e0348767. DOI: 10.1371/journal.pone.0348767.

The paper uses the Bank Marketing dataset and studies ensemble/deep-learning models, class-imbalance sampling, hyperparameter tuning, computational cost and SHAP explanations. It evaluates discrimination, calibration, computational complexity and explainability. The authors explicitly identify future work involving many-objective optimization, fairness and explanation-stability measures.

**Relevance:** This is the closest recent prior work and establishes that simple “Bank Marketing + HPO + SHAP” is not a sufficient novelty claim.

### Paper 2 — Recent Bank Marketing Explainable Ensemble Work (2026)
A 2026 Scientific Reports study, **Using ensemble learning and explainable AI to predict bank marketing customer subscription**, investigates class imbalance/distribution shifts using CatBoost ensemble learning and hierarchical SHAP explanations.

**Relevance:** It reinforces the need to differentiate the project through its HPO-strategy comparison and explanation-stability analysis rather than only predictive accuracy.

### Paper 3 — Risk-Sensitive Machine Learning for Financial Decision Modeling Under Imbalanced Data (2026)
This study evaluates Bank Telemarketing/Bank Marketing-style prediction using risk-sensitive evaluation, calibration and multi-level SHAP analysis, including global, interaction and local explanations.

**Relevance:** It supports the decision to treat imbalance, calibration/risk and explainability as integrated evaluation dimensions.

## 4. Research Gap
The literature demonstrates that:
- Hyperparameter tuning is already used on Bank Marketing.
- SHAP is already used to explain Bank Marketing models.
- Class-imbalance treatment is already an important research direction.
- Computational cost and calibration are increasingly being evaluated alongside predictive metrics.

Therefore, the project will **not** claim novelty from using Optuna, SHAP or Bank Marketing independently.

The proposed research gap is a controlled, reproducible comparison of **HPO strategy × class-imbalance treatment × predictive performance × computational efficiency × explanation stability**.

## 5. Proposed Research Questions
1. Which HPO strategy provides the strongest positive-class performance under a fixed computational budget?
2. How much improvement does HPO provide over default/reference configurations?
3. How does the optimization objective (for example F1 versus ROC-AUC) affect the selected model and positive-class behaviour?
4. How does imbalance treatment affect both predictive performance and explanations?
5. How stable are global and local SHAP explanations before and after optimization?
6. Is the best predictive model also the best model when computational efficiency and explanation stability are considered?

## 6. Expected Contribution
The expected contribution is an empirical framework and comparison rather than a claim of a new ML algorithm. The project will provide:
- Reproducible HPO experiments.
- Fair baseline-vs-optimized comparisons.
- Class-sensitive evaluation.
- Optimization-efficiency measurements.
- SHAP-based global/local analysis.
- Quantitative explanation-stability analysis.
- Transparent reporting of limitations and negative findings.

## 7. Important Methodological Rule
The final test set must remain untouched during HPO. Preprocessing and resampling must be performed inside training folds where applicable. The HPO budget, evaluation objective and stability procedure should be fixed before the main experiment to reduce researcher degrees of freedom.

## 8. References
1. Nasir, F., Ali Ahmed, A., Yevseyeva, I., & Kiraz, M. S. (2026). *Marketing analytics in banking 4.0: A two-stage explainable AI framework for high-accuracy and well-calibrated predictions*. PLOS ONE, 21(5), e0348767. DOI: 10.1371/journal.pone.0348767.
2. *Using ensemble learning and explainable AI to predict bank marketing customer subscription*. Scientific Reports (2026). DOI: 10.1038/s41598-026-58149-y.
3. *Risk-Sensitive Machine Learning for Financial Decision Modeling Under Imbalanced Data: Evidence from Bank Telemarketing*. Entropy (2026), 28(3), 354.
4. UCI Machine Learning Repository. *Bank Marketing* dataset.
