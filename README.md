
# Explainable Hyperparameter Optimization for Imbalanced Tabular Classification

## Project Overview

This project investigates an explainable and imbalance-aware hyperparameter optimization framework for binary tabular classification.

The current case study uses the UCI Bank Marketing dataset to predict whether a customer subscribes to a term deposit.

The research combines:

- Imbalanced classification
- Hyperparameter optimization
- Multi-objective optimization
- Threshold optimization
- Robustness analysis
- Explainable AI
- SHAP explanation stability

The goal is not only to obtain a predictive model, but to study how optimization objectives, class imbalance handling, decision thresholds, model robustness, and explanations interact.

---

## Research Problem

Binary tabular classification datasets frequently contain class imbalance.

For the Bank Marketing dataset, the positive subscription class is substantially smaller than the negative class.

Therefore, accuracy alone can provide a misleading assessment of model performance.

This project evaluates models using metrics such as:

- Precision
- Recall
- F1 Score
- PR-AUC
- ROC-AUC
- Balanced Accuracy

The project additionally investigates whether hyperparameter optimization and threshold selection can improve minority-class performance while maintaining robust and interpretable predictions.

---

## Dataset

Dataset:

UCI Bank Marketing Dataset

File used:

`bank-full.csv`

Target variable:

`y`

Target encoding:

- `no` = 0
- `yes` = 1

Dataset size:

45,211 observations

Number of variables:

17

The raw dataset is not required to be committed to the repository.

---

## Research Questions

### RQ1

Does imbalance-aware learning improve minority-class classification performance?

### RQ2

Can hyperparameter optimization improve performance compared with default model configurations?

### RQ3

How do different optimization objectives affect model performance?

### RQ4

How does classification threshold optimization change the precision-recall trade-off?

### RQ5

How robust are the model results across different random seeds?

### RQ6

How stable are SHAP-based explanations across repeated experiments?

---

## Models

The experimental study evaluates:

1. Logistic Regression
2. Decision Tree
3. Random Forest

---

## Imbalance Strategies

The project investigates:

1. Original imbalanced training data
2. Class weighting
3. SMOTENC

SMOTENC is applied only to training data to prevent data leakage.

---

## Hyperparameter Optimization

Optuna is used for hyperparameter optimization.

The primary single-objective optimization metric is F1 Score.

The study uses stratified cross-validation.

The actual Stage 6 trial counts were:

- Logistic Regression: 20 trials
- Decision Tree: 20 trials
- Random Forest: 40 completed trials

The Random Forest study was continued beyond the initially planned budget, and the actual number of completed trials is reported for reproducibility.

---

## Multi-objective Optimization

A separate experimental stage evaluates simultaneous optimization of:

- F1 Score
- PR-AUC

The resulting Pareto solutions are analyzed rather than assuming that one metric is universally optimal.

---

## Threshold Optimization

Classification threshold selection is investigated using out-of-fold training probabilities.

The default threshold is:

`0.50`

The F1-oriented threshold search evaluates:

`0.10` through `0.90`

in increments of `0.01`.

The selected threshold is determined using training OOF predictions and is subsequently evaluated on the untouched test set.

---

## Robustness

Robustness is evaluated using repeated stratified experiments across multiple random seeds.

The results are summarized using mean and standard deviation where applicable.

---

## Explainable AI

SHAP is used to investigate:

### Global explanations

Mean absolute SHAP importance is used to identify influential transformed features.

### Local explanations

Individual predictions are analyzed through their SHAP contributions.

### Explanation stability

Repeated experiments are compared using feature-overlap and ranking-based stability measures.

SHAP explanations represent model behavior and should not automatically be interpreted as causal relationships.

---

## Project Structure

```text
HPO_Explainable_Marketing/
│
├── data/
│   └── raw/
│       └── bank-full.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda_imbalance.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_baseline_models.ipynb
│   ├── 05_imbalance_strategies.ipynb
│   ├── 06_hpo_experiments.ipynb
│   ├── 07_multiobjective_hpo.ipynb
│   ├── 08_threshold_optimization.ipynb
│   ├── 09_robustness_analysis.ipynb
│   ├── 10_xai_shap.ipynb
│   ├── 11_explanation_stability.ipynb
│   └── 12_final_results.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   ├── imbalance.py
│   ├── hpo.py
│   ├── evaluation.py
│   └── explainability.py
│
├── results/
│   ├── metrics/
│   ├── hpo/
│   ├── plots/
│   └── shap/
│
├── references/
│
├── requirements.txt
└── README.md
