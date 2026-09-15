# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Project Title
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing**

### 1.2 Project Context
The project investigates how hyperparameter optimization and imbalance-handling strategies affect machine-learning-based prediction of customer subscription to a bank term deposit. It additionally evaluates whether optimized models produce stable and interpretable SHAP explanations.

### 1.3 Dataset
**UCI Bank Marketing Dataset**. The target variable is `y`, indicating whether the contacted client subscribed to a term deposit (`yes`/`no`).

### 1.4 Problem Statement
Bank marketing response data is imbalanced, with substantially fewer positive subscription outcomes than non-subscriptions. A model can therefore obtain high accuracy while performing poorly on the customers the campaign wants to identify. Hyperparameter tuning can improve predictive performance but can increase computational cost, while model explanations may vary across models, folds or random seeds. A reproducible framework is required to jointly study performance, imbalance handling, optimization efficiency and explanation stability.

### 1.5 Research Motivation and Gap
Existing Bank Marketing research already includes machine learning, class balancing, hyperparameter tuning and SHAP-based explainability. The project will therefore not claim novelty from HPO + SHAP alone. The research focus is a controlled comparison of HPO strategies and imbalance treatments under comparable computational budgets, together with quantitative explanation-stability analysis.

### 1.6 Scope
Data validation, preprocessing, imbalance analysis, baseline classification, multiple HPO strategies, imbalance treatments, class-sensitive evaluation, optimization-efficiency measurement, SHAP global/local explanations, explanation-stability analysis, experiment tracking and research reporting.

### 1.7 Objectives
- Use the UCI Bank Marketing dataset for reproducible binary classification.
- Establish leakage-safe baseline classifiers.
- Compare default and HPO-optimized configurations.
- Compare suitable imbalance treatments such as class weighting and SMOTE.
- Compare at least two HPO strategies under a fixed computational budget.
- Evaluate precision, recall, F1, balanced accuracy, ROC-AUC and PR-AUC.
- Record trials, hyperparameters, metrics and runtime.
- Generate global and local SHAP explanations.
- Quantify explanation stability across repeated seeds/folds or controlled samples.
- Determine whether the best predictive model is also efficient and explanation-stable.

## 2. Stakeholders

| Stakeholder | Responsibility |
|---|---|
| Student/Developer | Research, design, implementation, experiments and documentation |
| Project Guide | Methodology review and academic approval |
| Marketing/ML Analyst | Interpretation of customer-response results and explanations |
| Evaluator | Assessment of SEPM artifacts and research quality |

## 3. Functional Requirements

**FR-01:** Load the UCI Bank Marketing dataset.

**FR-02:** Validate schema, target, duplicates, missing/unknown values and data types.

**FR-03:** Perform leakage-safe preprocessing of numerical and categorical marketing features.

**FR-04:** Use stratified train/validation/test splitting.

**FR-05:** Quantify the target-class distribution and imbalance.

**FR-06:** Train reproducible baseline classifiers.

**FR-07:** Define documented hyperparameter search spaces.

**FR-08:** Compare at least two HPO strategies subject to computational feasibility.

**FR-09:** Compare documented imbalance treatments where technically appropriate.

**FR-10:** Evaluate models using precision, recall, F1, balanced accuracy, ROC-AUC and PR-AUC.

**FR-11:** Record HPO trials, selected parameters, objectives and execution time.

**FR-12:** Generate global and local SHAP explanations for supported models.

**FR-13:** Compare feature rankings and explanations between baseline and optimized models.

**FR-14:** Calculate explanation stability using a documented repeated-seed/fold or sample-based procedure.

**FR-15:** Store experiment configuration, dataset version and random seeds for reproducibility.

**FR-16:** Generate tables, plots and research findings and document limitations.

## 4. Non-Functional Requirements

- **Performance:** Experiments shall fit available academic CPU/RAM resources.
- **Reliability:** Failed trials and invalid configurations shall be detected and recorded.
- **Maintainability:** Data, modeling, optimization, evaluation and XAI modules shall be separated.
- **Reproducibility:** Seeds, splits, preprocessing, search spaces, software versions and budgets shall be recorded.
- **Traceability:** Research objectives shall map to requirements, design and tests.
- **Data protection:** No credentials, private customer data or secrets shall be committed.

## 5. Constraints

- The Bank Marketing dataset is historical and may not represent current campaign behaviour.
- The target is imbalanced, making accuracy alone misleading.
- HPO and SHAP can be computationally expensive.
- SMOTE can alter the training distribution and must be applied only within training folds.
- SHAP explains model behaviour and is not causal evidence.

## 6. Assumptions

- The public UCI dataset is available for academic research under its stated terms.
- Open-source Python ML/XAI libraries are available.
- The final protocol will use fixed compute budgets and reproducible seeds.
- The test set will remain untouched during HPO and model-selection decisions.

## 7. Acceptance Criteria

1. The UCI Bank Marketing dataset is loaded and documented.
2. Leakage-safe preprocessing and class-distribution analysis are completed.
3. Baseline and optimized models are reproducibly trained.
4. At least two HPO strategies are compared where feasible.
5. Suitable imbalance treatments are compared.
6. Class-sensitive performance and efficiency metrics are reported.
7. SHAP global/local explanations are generated.
8. Explanation stability is quantitatively evaluated.
9. Findings, limitations and the final research gap are documented reproducibly.
