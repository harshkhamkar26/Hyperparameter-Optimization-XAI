# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Project Title
**An Explainable Hyperparameter Optimization Framework for Imbalanced Cybersecurity Intrusion Detection**

### 1.2 Project Context
The project investigates how hyperparameter optimization and imbalance-handling strategies affect machine-learning-based intrusion detection. It additionally evaluates whether optimized models produce stable and interpretable SHAP explanations.

### 1.3 Dataset
The final public cybersecurity IDS dataset is **TBD after literature and dataset evaluation**. Candidate datasets are CIC-IDS2017, CSE-CIC-IDS2018, UNSW-NB15, TON_IoT and CIC-DDoS2019. Dataset selection must be justified before implementation.

### 1.4 Problem Statement
Cybersecurity intrusion datasets commonly contain severe class imbalance, heterogeneous traffic features and multiple attack categories. A model can obtain high accuracy while performing poorly on minority attacks. Hyperparameter tuning can improve predictive performance but may increase computational cost, and model explanations can vary across models, folds or random seeds. A reproducible framework is therefore required to jointly study performance, imbalance handling, optimization efficiency and explanation stability.

### 1.5 Research Motivation and Gap
Existing IDS research includes machine learning, imbalance-handling methods, hyperparameter optimization and explainable IDS. However, these dimensions are often evaluated separately or with different protocols. The project will investigate their interaction through a controlled experimental framework rather than claiming novelty from HPO or SHAP alone.

### 1.6 Scope
Data validation, preprocessing, imbalance analysis, baseline IDS models, multiple HPO strategies, imbalance treatments, class-sensitive evaluation, optimization-efficiency measurement, SHAP global/local explanations, explanation-stability analysis, experiment tracking and research reporting.

### 1.7 Objectives
- Select and justify a reproducible public cybersecurity intrusion dataset.
- Establish leakage-safe baseline IDS models.
- Compare default and optimized model configurations.
- Compare suitable imbalance treatments such as class weighting and SMOTE variants where valid.
- Compare at least two HPO strategies under a fixed computational budget.
- Evaluate precision, recall, F1, balanced accuracy, ROC-AUC and PR-AUC, with attack-class analysis where applicable.
- Record trials, hyperparameters, metrics and runtime.
- Generate global and local SHAP explanations.
- Quantify explanation stability across repeated seeds/folds or controlled samples.
- Determine whether the best predictive model is also efficient and explanation-stable.

## 2. Stakeholders

| Stakeholder | Responsibility |
|---|---|
| Student/Developer | Research, design, implementation, experiments and documentation |
| Project Guide | Methodology review and academic approval |
| Security/ML Analyst | Interpretation of IDS results and explanations |
| Evaluator | Assessment of SEPM artifacts and research quality |

## 3. Functional Requirements

**FR-01:** The system shall load the selected public cybersecurity IDS dataset.

**FR-02:** The system shall validate schema, labels, duplicates, missing/invalid values and data types.

**FR-03:** The system shall perform leakage-safe preprocessing of numerical and categorical/network features.

**FR-04:** The system shall use stratified and/or attack-aware train/validation/test splitting as appropriate to the selected dataset.

**FR-05:** The system shall quantify class distribution and imbalance.

**FR-06:** The system shall train reproducible baseline IDS classifiers.

**FR-07:** The system shall define documented hyperparameter search spaces.

**FR-08:** The system shall compare at least two HPO strategies subject to computational feasibility.

**FR-09:** The system shall compare documented imbalance treatments where technically appropriate.

**FR-10:** The system shall evaluate models using class-sensitive metrics including precision, recall, F1, balanced accuracy and PR-AUC.

**FR-11:** The system shall record HPO trials, selected parameters, objectives and execution time.

**FR-12:** The system shall generate global and local SHAP explanations for supported models.

**FR-13:** The system shall compare feature rankings and explanations between baseline and optimized models.

**FR-14:** The system shall calculate explanation stability using a documented repeated-seed/fold or sample-based procedure.

**FR-15:** The system shall store experiment configuration, dataset version and random seeds for reproducibility.

**FR-16:** The system shall generate tables, plots and research findings and document limitations.

## 4. Non-Functional Requirements

- **Performance:** Experiments shall fit available academic CPU/RAM resources.
- **Reliability:** Failed trials and invalid configurations shall be detected and recorded.
- **Maintainability:** Data, modeling, optimization, evaluation and XAI modules shall be separated.
- **Reproducibility:** Seeds, splits, preprocessing, search spaces, software versions and budgets shall be recorded.
- **Traceability:** Research objectives shall map to requirements, design and tests.
- **Security:** No credentials, private traffic captures or secrets shall be committed.

## 5. Constraints

- Cybersecurity datasets may contain redundant records, leakage risks and dataset-specific artifacts.
- Severe imbalance can make accuracy misleading.
- Large IDS datasets can make exhaustive HPO and SHAP expensive.
- SHAP explains model behaviour and is not proof of causal attack indicators.
- Results on benchmark datasets may not generalize to live networks.

## 6. Assumptions

- A suitable public IDS dataset can be selected and downloaded legally for academic research.
- Open-source Python ML/XAI libraries are available.
- The final protocol will use a fixed compute budget and reproducible seeds.
- The test set will remain untouched during HPO and model-selection decisions.

## 7. Acceptance Criteria

1. A cybersecurity IDS dataset is selected with documented justification.
2. Leakage-safe preprocessing and class-distribution analysis are completed.
3. Baseline and optimized IDS models are reproducibly trained.
4. At least two HPO strategies are compared where feasible.
5. Suitable imbalance treatments are compared.
6. Class-sensitive performance and efficiency metrics are reported.
7. SHAP global/local explanations are generated.
8. Explanation stability is quantitatively evaluated.
9. Findings, limitations and the final research gap are documented reproducibly.
