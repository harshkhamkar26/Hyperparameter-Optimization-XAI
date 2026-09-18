# Feasibility Study

## 1. Technical Feasibility
The project is technically feasible using Python, Pandas, NumPy, Scikit-learn, Optuna, SHAP and imbalanced-learn. The core model set is **Random Forest, XGBoost and CatBoost**, selected for tabular classification and compatibility with SHAP-based interpretation. The UCI Bank Marketing dataset is a manageable tabular benchmark suitable for academic CPU/RAM resources and controlled HPO experiments.

## 2. Research Feasibility
The topic is supported by established Bank Marketing, imbalanced learning, hyperparameter optimization and explainable AI research. Recent studies already combine HPO, class balancing and SHAP on this dataset. Therefore, the defensible research gap is the controlled joint comparison of optimization strategy, imbalance treatment, predictive performance, computational efficiency and explanation stability.

## 3. Economic Feasibility
The software stack is open source and the public dataset can be used for academic research subject to its stated terms. No paid infrastructure is required for the planned experiments.

## 4. Operational Feasibility
The workflow is suitable for a student research project. Experiments can be run in Jupyter Notebook with documented configurations, fixed budgets and reproducible seeds.

## 5. Schedule Feasibility
Phases: literature review → dataset validation → SEPM revision → preprocessing → baselines → imbalance experiments → HPO → evaluation → SHAP → stability → analysis → paper/report.

## 6. Risks Affecting Feasibility
HPO and repeated SHAP experiments may require resource-aware trial/sample limits. The dataset contains historical campaign variables and potential target leakage risks, especially if post-contact variables such as call duration are included without a clearly defined prediction-time protocol.

## 7. Conclusion
The project is feasible provided that the prediction-time feature policy, experimental budget and evaluation protocol are frozen before the main experiments and that preprocessing, resampling and HPO remain leakage-safe and reproducible.
