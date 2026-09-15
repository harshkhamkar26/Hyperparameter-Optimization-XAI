# Feasibility Study

## 1. Technical Feasibility
The project is technically feasible using Python, Pandas, NumPy, Scikit-learn, Optuna, SHAP and imbalanced-learn. Public IDS datasets such as CIC-IDS2017, CSE-CIC-IDS2018, UNSW-NB15, TON_IoT and CIC-DDoS2019 provide suitable tabular/network-flow data. Dataset selection will consider size and available CPU/RAM.

## 2. Research Feasibility
The topic is supported by established research in intrusion detection, imbalanced learning, hyperparameter optimization and explainable AI. The project can formulate a defensible research gap around their controlled joint evaluation and explanation stability rather than claiming that HPO+SHAP itself is novel.

## 3. Economic Feasibility
The software stack is open source and public datasets can be used for academic research subject to their licenses/terms. No paid infrastructure is required for the planned experiments.

## 4. Operational Feasibility
The workflow is suitable for a student research project. Experiments can be run in Jupyter Notebook with documented configurations and fixed budgets.

## 5. Schedule Feasibility
Phases: literature review → dataset selection → SEPM revision → preprocessing → baselines → imbalance experiments → HPO → evaluation → SHAP → stability → analysis → paper/report.

## 6. Risks Affecting Feasibility
Large IDS datasets may require sampling or resource-aware experiments. Dataset artifacts, duplicate traffic and leakage can inflate results. SHAP and repeated HPO experiments can be computationally expensive.

## 7. Conclusion
The project is feasible provided that the final dataset and compute budget are frozen before the main experiments and that all preprocessing, HPO and evaluation steps are leakage-safe and reproducible.
