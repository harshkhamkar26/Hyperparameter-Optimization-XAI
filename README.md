# Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — SEPM Documentation

This repository contains the **Software Engineering and Project Management (SEPM)** documentation for an academic research project on hyperparameter optimization and Explainable AI.

## Current Research Scope

**Dataset:** UCI Bank Marketing Dataset  
**Task:** Binary classification of term-deposit subscription (`yes` / `no`)  
**Core theme:** Hyperparameter optimization + Explainable AI  
**Research focus:** Predictive performance, optimization efficiency, class-imbalance handling and explanation stability

The project does **not** claim novelty merely from applying HPO and SHAP to Bank Marketing. Recent literature already covers that combination. The intended contribution is a controlled comparison of optimization strategies and their effect on performance, computational cost and explanation stability.

## SEPM Documents

1. Project Proposal
2. Software Requirements Specification (SRS)
3. Feasibility Study
4. Project Plan
5. Risk Management
6. System Design and Architecture
7. UML Diagrams
8. Test Plan and Test Cases
9. Requirements Traceability Matrix
10. Project Management
11. Detailed Design Description
12. Literature Review and Research Gap

All project documentation is stored under `docs/SEPM/`.

## Proposed Research Workflow

**Dataset → Validation → Leakage-safe preprocessing → Imbalance analysis → Baseline → HPO strategies → Evaluation → SHAP → Explanation stability → Comparative analysis → Research report**

## Planned Technology Stack

Python, Pandas, NumPy, Scikit-learn, Optuna, SHAP, imbalanced-learn, Matplotlib/Seaborn and Jupyter Notebook.

## Version Control

GitHub is used to track requirements, design decisions, UML, testing and research-document changes. Implementation will be added only after the SEPM scope is approved.
