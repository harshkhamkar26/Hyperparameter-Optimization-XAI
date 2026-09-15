# An Explainable Hyperparameter Optimization Framework for Imbalanced Cybersecurity Intrusion Detection

This repository contains the **Software Engineering and Project Management (SEPM) documentation** for an academic research project on cybersecurity intrusion detection, hyperparameter optimization, class imbalance and Explainable AI.

## Corrected Research Topic

**An Explainable Hyperparameter Optimization Framework for Imbalanced Cybersecurity Intrusion Detection**

## Research Scope

- **Domain:** Cybersecurity / Intrusion Detection Systems (IDS)
- **Task:** Intrusion/attack detection using supervised machine learning
- **Core problem:** Class imbalance in cybersecurity traffic, especially minority attack classes
- **Optimization:** Grid Search, Random Search and Bayesian/TPE-based optimization such as Optuna, subject to compute budget
- **Explainability:** SHAP-based global and local explanations
- **Research focus:** Predictive performance, imbalance handling, optimization efficiency and explanation stability

The dataset will be selected after a focused literature and dataset comparison. Candidate datasets include CIC-IDS2017, CSE-CIC-IDS2018, UNSW-NB15, TON_IoT and CIC-DDoS2019. The final choice will be justified using class imbalance, attack coverage, size, reproducibility, literature support, leakage risk and computational feasibility.

## Research Gap Positioning

The project will **not** claim novelty merely from applying HPO or SHAP to an IDS dataset. The intended contribution is a controlled, reproducible evaluation of:

**HPO strategy × imbalance treatment × IDS performance × computational efficiency × explanation stability**

A central research question is whether the model with the best predictive performance also provides the most stable and trustworthy explanations.

## Proposed Workflow

**Cybersecurity Dataset → Data Validation → Leakage-safe Preprocessing → Imbalance Analysis → Baseline IDS Models → HPO Strategies → Evaluation → SHAP Explanations → Explanation Stability → Comparative Analysis → Research Findings**

## Planned Technology Stack

Python, Pandas, NumPy, Scikit-learn, XGBoost/other suitable tree models, Optuna, SHAP, imbalanced-learn, Matplotlib and Jupyter Notebook.

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

GitHub is used to track requirements, design decisions, UML, testing and research-document changes. Implementation will begin only after the research scope, dataset and experimental protocol are approved.
