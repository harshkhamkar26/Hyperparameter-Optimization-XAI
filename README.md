# Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing

This repository contains the **Software Engineering and Project Management (SEPM) documentation** for an academic research project on hyperparameter optimization, class imbalance and Explainable AI in bank marketing analytics.

## Current Research Scope

**Dataset:** UCI Bank Marketing Dataset  
**Task:** Binary classification of term-deposit subscription (`yes` / `no`)  
**Domain:** Marketing / Banking Marketing Analytics  
**Core theme:** Hyperparameter optimization + imbalanced learning + Explainable AI  
**Research focus:** Predictive performance, optimization efficiency, class-imbalance handling and explanation stability

The project does **not** claim novelty merely from applying HPO and SHAP to Bank Marketing. Recent literature already covers that combination. The intended contribution is a controlled, reproducible comparison of:

**HPO strategy × imbalance treatment × predictive performance × computational efficiency × explanation stability**

## Central Research Question

How can hyperparameter optimization be systematically combined with imbalance handling and explainable AI to improve bank-marketing classification performance while maintaining computational efficiency and stable, trustworthy explanations?

## Proposed Research Workflow

**UCI Bank Marketing → Validation → Leakage-safe preprocessing → Imbalance analysis → Baseline → HPO strategies → Evaluation → SHAP → Explanation stability → Comparative analysis → Research findings**

## Planned Models and Methods

- Random Forest
- XGBoost
- CatBoost where computationally feasible
- Grid Search
- Random Search
- Optuna/TPE
- Class weighting
- SMOTE within training folds where appropriate
- SHAP global and local explanations

## Evaluation

Accuracy, Precision, Recall, F1, ROC-AUC, PR-AUC, Balanced Accuracy, confusion matrix, HPO trial count, runtime and explanation-stability measures will be considered. The test set will remain untouched during HPO.

## SEPM Documents

All project documentation is stored under `docs/SEPM/`.

1. SRS
2. Project Proposal
3. Feasibility Study
4. Project Plan
5. Risk Management
6. System Design and Architecture
7. UML Diagrams
8. Test Plan and Test Cases
9. Requirements Traceability Matrix
10. Project Management
11. Design Description
12. Literature Review and Research Gap
13. References and Research Papers

## Version Control

GitHub is used to track requirements, design decisions, UML, testing and research-document changes. Implementation will be added after the SEPM scope and experimental protocol are approved.
