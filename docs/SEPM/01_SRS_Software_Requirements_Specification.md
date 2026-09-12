# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Project Title
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification**

### 1.2 Project Context
The project studies how different hyperparameter optimization strategies affect predictive performance, computational efficiency, and explainability for an imbalanced binary-classification problem.

### 1.3 Selected Dataset
**UCI Bank Marketing Dataset**. The primary target is `y`, where `yes` means the customer subscribed to a term deposit and `no` means the customer did not subscribe. The dataset is publicly available through the UCI Machine Learning Repository.

### 1.4 Problem Statement
Default model hyperparameters may not provide the best predictive performance, while exhaustive tuning can be computationally expensive. In an imbalanced classification problem, accuracy alone can also be misleading. The system therefore needs to compare baseline and optimized models using class-sensitive metrics and explain how optimization changes model decisions.

### 1.5 Research Motivation and Gap
Recent studies have already applied hyperparameter tuning and SHAP to the Bank Marketing dataset. Therefore, the project will not claim novelty from simply combining Optuna and SHAP. Instead, it will investigate the trade-off among predictive performance, optimization efficiency, class-imbalance handling, and explanation stability across optimization strategies.

### 1.6 Scope
The system covers data validation, preprocessing, class-imbalance analysis, baseline classification, multiple hyperparameter optimization strategies, model evaluation, SHAP-based explainability, explanation comparison/stability analysis, experiment recording, and reporting.

### 1.7 Objectives
- Establish reproducible baseline classifiers for Bank Marketing.
- Compare Grid Search, Random Search and Bayesian/TPE-based optimization where computationally practical.
- Optimize selected tree-based classifiers using an explicitly defined validation objective.
- Evaluate positive-class performance using precision, recall and F1 in addition to ROC-AUC and accuracy.
- Measure optimization efficiency such as trials and execution time.
- Generate global and local SHAP explanations.
- Compare feature importance and explanation stability before and after optimization.
- Document limitations and ensure reproducibility.

## 2. Stakeholders

| Stakeholder | Responsibility |
|---|---|
| Student/Developer | Analysis, design, implementation, experiments and documentation |
| Project Guide | Requirements review, methodology feedback and academic approval |
| End User/Analyst | Interpretation of predictions and explanations |
| Evaluator | Assessment of research methodology, SEPM artifacts and results |

## 3. Functional Requirements

**FR-01:** The system shall load the selected public UCI Bank Marketing dataset.

**FR-02:** The system shall validate schema, target availability, duplicates, missing/unknown values and data types.

**FR-03:** The system shall preprocess categorical and numerical features without leaking test-set information.

**FR-04:** The system shall use a stratified train/validation/test methodology appropriate for an imbalanced binary target.

**FR-05:** The system shall train at least one baseline classification model using documented default or reference hyperparameters.

**FR-06:** The system shall define reproducible hyperparameter search spaces for selected models.

**FR-07:** The system shall perform at least two hyperparameter search strategies, subject to computational feasibility.

**FR-08:** The system shall select the best configuration using a predefined validation objective such as F1 or a documented multi-metric selection rule.

**FR-09:** The system shall evaluate baseline and optimized models using accuracy, precision, recall, F1-score, ROC-AUC and confusion matrix; PR-AUC may be included because of class imbalance.

**FR-10:** The system shall record optimization trials, selected hyperparameters, metrics and execution time.

**FR-11:** The system shall generate global and local SHAP explanations for supported optimized models and comparable baseline models.

**FR-12:** The system shall compare feature-importance rankings and SHAP distributions between baseline and optimized models.

**FR-13:** The system shall evaluate explanation stability/consistency using a documented procedure across repeated samples or folds.

**FR-14:** The system shall generate tables and visualizations for performance, optimization efficiency and explainability results.

**FR-15:** The system shall store experiment configuration and random seeds required for reproducibility.

**FR-16:** The system shall document assumptions, limitations, research gap, findings and conclusions.

## 4. Non-Functional Requirements

- **Performance:** Experiments shall complete within reasonable academic-project computing limits.
- **Usability:** Results and explanations shall be understandable to a student evaluator and non-specialist analyst.
- **Reliability:** Data leakage, invalid configurations and failed trials shall be detected and handled.
- **Maintainability:** Data, modeling, optimization, evaluation and XAI responsibilities shall remain modular.
- **Reproducibility:** Dataset version, preprocessing rules, seeds, search spaces, software versions and experiment settings shall be recorded.
- **Traceability:** Each major research objective shall map to requirements, design components and test cases.
- **Security:** No credentials, private customer data or secrets shall be committed to GitHub.

## 5. Constraints

- The Bank Marketing data represents historical campaigns and may not generalize to current banking environments.
- The target is imbalanced, so accuracy cannot be the only selection metric.
- Hyperparameter optimization can become computationally expensive.
- SHAP values explain model behaviour, not causality.
- The project is constrained by academic time and available CPU/RAM resources.

## 6. Assumptions

- The public UCI dataset and its usage conditions remain suitable for academic use.
- Python and open-source ML/XAI libraries will be used.
- The final implementation will prioritize reproducibility over very large optimization budgets.
- The primary binary classification task is term-deposit subscription prediction (`yes`/`no`).

## 7. Acceptance Criteria

The project is successful when:
1. The Bank Marketing dataset is validated and processed without data leakage.
2. Baseline and optimized classifiers are trained reproducibly.
3. At least two HPO strategies are compared where feasible.
4. Performance is evaluated using class-sensitive metrics.
5. Optimization settings and results are recorded.
6. SHAP global/local explanations are generated.
7. Baseline versus optimized explanations are compared, including a documented stability analysis.
8. Results, limitations and research conclusions are reproducible and documented.
