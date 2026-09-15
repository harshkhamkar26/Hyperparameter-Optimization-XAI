# Project Proposal

## Title
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing**

## 1. Background
Bank marketing campaigns aim to identify customers who are likely to subscribe to financial products such as term deposits. The UCI Bank Marketing dataset provides customer, contact-history and campaign-related variables for predicting subscription. The positive subscription class is substantially smaller than the negative class, making class-sensitive evaluation important.

## 2. Problem Statement
Model performance depends strongly on hyperparameters and the treatment of imbalanced classes. Different optimization strategies may produce different performance, runtime and decision behaviour. Furthermore, an accurate model can be difficult to trust if its predictions cannot be explained or if explanations are unstable. This project proposes a reproducible framework to study these factors together for Bank Marketing classification.

## 3. Objectives
1. Use and document the UCI Bank Marketing dataset.
2. Establish leakage-safe baseline classifiers.
3. Analyze class imbalance and compare suitable mitigation strategies.
4. Compare default models with HPO-optimized models.
5. Compare Grid Search, Random Search and Optuna/TPE where computationally feasible.
6. Evaluate class-sensitive metrics and computational efficiency.
7. Generate SHAP global and local explanations.
8. Quantify explanation stability across repeated experiments.
9. Identify the trade-off between predictive performance, efficiency and explanation stability.

## 4. Research Questions
- **RQ1:** Which HPO strategy provides the strongest positive-class performance under a fixed computational budget?
- **RQ2:** How much improvement does HPO provide over default/reference configurations?
- **RQ3:** How does the HPO objective affect the selected model and positive-class behaviour?
- **RQ4:** How does imbalance treatment affect predictive performance and explanations?
- **RQ5:** How stable are global and local SHAP explanations before and after optimization?
- **RQ6:** Is the best predictive model also the most computationally efficient and explanation-stable?

## 5. Proposed Methodology
**UCI Bank Marketing → Validation → Leakage-safe preprocessing → Imbalance analysis → Baseline → HPO + imbalance treatments → Evaluation → SHAP → Stability analysis → Comparative study → Conclusions**

The controlled experiment matrix will compare default versus optimized models under no imbalance treatment, class weighting and SMOTE where technically valid. Tree-based models such as Random Forest, XGBoost and CatBoost will be considered.

## 6. Expected Contribution
The contribution is an empirical and reproducible framework, not a new ML algorithm. The study will jointly compare **HPO strategy × imbalance treatment × predictive performance × computational efficiency × explanation stability**. The research will explicitly test whether improvements in predictive metrics also correspond to stable explanations.

## 7. Boundaries
The project focuses on supervised tabular classification for bank marketing response prediction. It does not claim causal interpretation of SHAP values, real-time banking deployment or guaranteed generalization to current customers.

## 8. Deliverables
SEPM documentation, literature review, dataset justification, experimental protocol, reproducible experiments, performance comparison, SHAP analysis, explanation-stability analysis and research paper/report.
