# Literature Review and Research Gap

## 1. Research Domain
The project focuses on **bank marketing analytics**, specifically prediction of term-deposit subscription using the UCI Bank Marketing dataset, with emphasis on class imbalance, hyperparameter optimization and Explainable AI.

## 2. Key Literature Directions

### A. Bank Marketing prediction
Moro, Cortez and Rita established a data-driven approach for predicting bank telemarketing success using the Portuguese bank marketing dataset. This work provides the foundational benchmark for the project.

Recent work continues to use the same task with tree ensembles, CatBoost, SHAP and imbalance-aware evaluation. Therefore, simple model comparison on this dataset is not a sufficient research contribution.

### B. Imbalance and marketing analytics
Recent PLOS ONE research on Banking 4.0 evaluates imbalanced UCI Bank Marketing data using Grid Search, Random Search and Optuna/TPE with Hyperband pruning. It reports that TPE can improve optimization efficiency and emphasizes discrimination and calibration rather than accuracy alone. This directly establishes that HPO on Bank Marketing is already an active research area.

### C. Explainable Bank Marketing
Recent work has applied CatBoost + SHAP to bank term-deposit prediction and has used class balancing and hyperparameter tuning. A 2025 ESAI conference paper also combines CatBoost, class balancing, hyperparameter tuning and SHAP on the UCI Bank Marketing dataset.

### D. HPO methodology
Optuna/TPE and Random Search are established HPO methods. The project should therefore compare them under controlled budgets rather than claiming the use of Optuna as novelty.

### E. Explanation stability
Recent credit-scoring research evaluates SHAP/LIME stability under class imbalance and reports that explanation stability can deteriorate as imbalance increases. This provides methodological motivation for measuring explanation stability in Bank Marketing rather than reporting SHAP plots alone.

## 3. Research Gap
The literature establishes that:
- Bank Marketing subscription prediction is well studied.
- Class imbalance is a central issue in the dataset.
- HPO has already been applied using Grid Search, Random Search and Optuna/TPE.
- SHAP-based explanations have already been applied to Bank Marketing.
- Recent work combines HPO, imbalance treatment and explainability.

Therefore, the project will **not** claim novelty from using Optuna, SHAP, SMOTE or the UCI Bank Marketing dataset individually.

### Proposed Gap
The project will investigate the controlled interaction of:

**HPO strategy × imbalance treatment × predictive performance × computational efficiency × explanation stability**

The key additional dimension is quantitative explanation stability across repeated seeds/folds/samples, studied together with predictive and computational performance.

## 4. Research Questions
1. Which HPO strategy provides the strongest positive-class performance under a fixed computational budget?
2. How much improvement does HPO provide over default/reference configurations?
3. How does the HPO objective affect the selected model and positive-class behaviour?
4. How does imbalance treatment affect predictive performance and explanations?
5. How stable are global and local SHAP explanations before and after optimization?
6. Is the best predictive model also the most computationally efficient and explanation-stable?

## 5. Methodological Controls
The test set must remain untouched during HPO. Preprocessing and resampling must occur inside training folds where applicable. Search budgets, seeds, primary objective and explanation-stability procedure will be fixed before the main experiment.

The project will also explicitly document the prediction-time interpretation of post-contact variables such as `duration`, because including such variables changes the business meaning of the model.

## 6. Expected Contribution
An empirical, reproducible framework that demonstrates how optimization and imbalance handling influence not only Bank Marketing predictive performance but also computational cost and the stability of explanations.

## 7. Core References
- Moro, Cortez & Rita (2014), bank telemarketing prediction.
- Nasir et al. (2026), Marketing Analytics in Banking 4.0.
- Wang et al. (2026), ensemble learning and XAI for bank marketing subscription.
- Yu (2025), CatBoost and SHAP for bank term-deposit prediction.
- Abidin et al. (2025), SVM + SMOTE + hyperparameter tuning for bank marketing.
- Saket et al. (2025), SHAP-based interpretation of bank term-deposit prediction.
- Akiba et al. (2019), Optuna.
- Bergstra & Bengio (2012), Random Search.
- Lundberg & Lee (2017), SHAP.
- Lundberg et al. (2020), SHAP for tree models.
- Chawla et al. (2002), SMOTE.
- Saito & Rehmsmeier (2015), Precision-Recall evaluation.
- Ballegeer, Bogaert & Benoit (2025), explanation stability under imbalance.
