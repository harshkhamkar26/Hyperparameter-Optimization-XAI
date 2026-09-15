# Project Proposal

## Title
**An Explainable Hyperparameter Optimization Framework for Imbalanced Cybersecurity Intrusion Detection**

## 1. Background
Intrusion Detection Systems use machine learning to identify malicious or anomalous network activity. Cybersecurity traffic datasets are frequently imbalanced, with some attack classes occurring much less often than normal traffic or dominant attack types. This creates a risk that conventional accuracy-focused models under-detect important minority attacks.

## 2. Problem Statement
Model performance depends strongly on hyperparameters and the treatment of imbalanced classes. Different optimization strategies may produce different performance, runtime and decision behaviour. Furthermore, an accurate IDS model is difficult to trust if its predictions cannot be explained or if explanations are unstable. This project proposes a reproducible framework to study these factors together.

## 3. Objectives
1. Select and justify a public cybersecurity intrusion dataset.
2. Establish leakage-safe baseline IDS models.
3. Analyze class imbalance and compare suitable mitigation strategies.
4. Compare default models with HPO-optimized models.
5. Compare Grid Search, Random Search and Optuna/TPE where computationally feasible.
6. Evaluate class-sensitive IDS metrics and computational efficiency.
7. Generate SHAP global and local explanations.
8. Quantify explanation stability across repeated experiments.
9. Identify the trade-off between predictive performance, efficiency and explanation stability.

## 4. Research Questions
- RQ1: Which HPO strategy provides the strongest IDS performance under a fixed computational budget?
- RQ2: How does imbalance treatment affect minority-attack detection?
- RQ3: Does HPO improve performance consistently across attack classes?
- RQ4: How does optimization affect SHAP feature importance and local explanations?
- RQ5: Are explanations stable across seeds/folds and model configurations?
- RQ6: Is the best-performing IDS model also the most computationally efficient and explanation-stable?

## 5. Proposed Methodology
**Dataset → Validation → Leakage-safe preprocessing → Imbalance analysis → Baseline → HPO + imbalance treatments → Evaluation → SHAP → Stability analysis → Comparative study → Conclusions**

Candidate datasets: CIC-IDS2017, CSE-CIC-IDS2018, UNSW-NB15, TON_IoT and CIC-DDoS2019. The final dataset will be frozen only after literature-based comparison.

## 6. Expected Contribution
The contribution is an empirical and reproducible framework, not a new ML algorithm. It will jointly compare HPO strategy, imbalance handling, IDS performance, computational efficiency and explanation stability.

## 7. Boundaries
The project focuses on supervised tabular/network-flow intrusion detection. It does not claim real-time SOC deployment, zero-day detection or causal interpretation of SHAP values unless separately validated.

## 8. Deliverables
SEPM documentation, literature review, dataset justification, experimental protocol, reproducible experiments, performance comparison, SHAP analysis, explanation-stability analysis and research paper/report.
