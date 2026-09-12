# Project Proposal

## 1. Project Title
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification**

## 2. Selected Application Problem
The project will study **binary classification of Bank Marketing customers**. The target variable `y` indicates whether a customer subscribed to a term deposit (`yes`/`no`). The task has direct business relevance because a bank wants to identify customers who are more likely to convert while avoiding unnecessary marketing contacts.

## 3. Problem Statement
Machine-learning models can be sensitive to hyperparameter choices. Manual tuning is slow and may miss strong configurations. At the same time, the positive class in marketing-response prediction is substantially smaller than the negative class, making raw accuracy an inadequate optimization objective. High-performing models may also be difficult to interpret.

## 4. Proposed Solution
Develop a reproducible experimental framework that compares baseline and hyperparameter-optimized classifiers on the UCI Bank Marketing dataset. The study will compare multiple search strategies, evaluate predictive performance and optimization cost, and use SHAP to examine how model explanations change after optimization.

## 5. Research Gap
Existing work has already studied Bank Marketing using hyperparameter tuning, ensemble models, sampling methods and SHAP. A 2026 PLOS ONE study, for example, evaluates hyperparameter tuning, sampling, computational cost and SHAP-based explainability on the dataset. Therefore, this project will focus on a narrower research question: **how optimization strategy and class-imbalance treatment affect the trade-off between predictive performance, computational efficiency and explanation stability.**

## 6. Research Questions
1. Which HPO strategy gives the strongest validation performance for the selected classification models?
2. How much improvement does optimization provide over default/reference hyperparameters?
3. Does optimizing for F1/recall-oriented objectives change model behaviour compared with optimizing for accuracy or ROC-AUC?
4. How does class-imbalance treatment affect model performance and SHAP explanations?
5. Does hyperparameter optimization materially change global feature rankings or local explanations?
6. Which approach provides the best practical trade-off between predictive quality, computational cost and explanation stability?

## 7. Objectives
- Establish reproducible baseline models.
- Compare Grid Search, Random Search and TPE/Bayesian optimization where feasible.
- Evaluate class-sensitive metrics.
- Measure optimization time and trial efficiency.
- Generate global and local SHAP explanations.
- Compare explanation stability before and after optimization.
- Produce a transparent research report rather than only a high-accuracy model.

## 8. High-Level Modules
1. Dataset Management
2. Data Validation and Preprocessing
3. Class-Imbalance Analysis
4. Baseline Model Training
5. Hyperparameter Search
6. Model Evaluation
7. SHAP Explainability
8. Explanation Stability Analysis
9. Experiment Tracking and Reporting

## 9. Proposed Models
The initial study will prioritize models that work well on tabular data, such as Random Forest and gradient-boosting models. The final model set will be fixed after a small baseline experiment and computational feasibility assessment.

## 10. Proposed Tools
- Python
- Pandas / NumPy
- Scikit-learn
- Optuna
- SHAP
- imbalanced-learn where required
- Matplotlib / Seaborn for visualization
- Jupyter Notebook
- GitHub for version control

## 11. Evaluation Strategy
Primary metrics:
- F1-score
- Recall
- Precision
- ROC-AUC
- PR-AUC where appropriate
- Accuracy
- Confusion matrix

Efficiency metrics:
- Number of trials
- Optimization runtime
- Training runtime
- Best objective value per computational budget

Explainability metrics/analysis:
- Mean absolute SHAP importance
- Top-k feature overlap between models
- Rank correlation of feature importance
- Explanation consistency across repeated samples/folds

## 12. Expected Contribution
The expected contribution is an experimental framework for comparing HPO strategies under an imbalanced tabular classification setting while treating explainability and computational cost as first-class evaluation dimensions. The project will explicitly report negative or statistically insignificant improvements instead of assuming that optimization always improves a model.

## 13. Deliverables
- SRS
- Project Proposal
- Feasibility Study
- Project Plan and schedule
- Risk Register
- System Design and Architecture
- UML diagrams
- Test Plan and Test Cases
- Requirements Traceability Matrix
- Project Management document
- Detailed Design Description
- Literature Review and Research Gap document
- Final experimental report and presentation
