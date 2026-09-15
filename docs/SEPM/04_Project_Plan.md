# Project Plan

## Project
**An Explainable Hyperparameter Optimization Framework for Imbalanced Cybersecurity Intrusion Detection**

## Phase Plan

| Phase | Activity | Output |
|---|---|---|
| 1 | Problem definition | Final research topic and RQs |
| 2 | Literature study | IDS/HPO/imbalance/XAI matrix |
| 3 | Dataset comparison | Dataset selection and justification |
| 4 | SEPM | Updated SRS, proposal, feasibility and UML |
| 5 | Data preparation | Leakage-safe preprocessing pipeline |
| 6 | Baselines | Reference IDS model results |
| 7 | Imbalance study | Class-weight/SMOTE comparison where valid |
| 8 | HPO | Grid/Random/Optuna experiments |
| 9 | Evaluation | Performance and efficiency tables |
| 10 | XAI | Global/local SHAP explanations |
| 11 | Stability | Repeated-seed/fold explanation stability |
| 12 | Analysis | Trade-off and research-gap findings |
| 13 | Reporting | Paper, presentation and final documentation |

## Experiment Control
The test set must not be used for HPO. Search budgets, seeds, splits, primary objective and stability procedure should be predefined. Every trial should record parameters, objective value, runtime and model configuration.

## Dataset Candidates
CIC-IDS2017, CSE-CIC-IDS2018, UNSW-NB15, TON_IoT and CIC-DDoS2019 will be compared before final selection.
