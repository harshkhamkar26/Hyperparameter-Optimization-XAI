# Project Plan

## Project
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing**

## Phase Plan

| Phase | Activity | Output |
|---|---|---|
| 1 | Problem definition | Final Bank Marketing research topic and RQs |
| 2 | Literature study | Bank Marketing/HPO/imbalance/XAI matrix |
| 3 | Dataset validation | UCI Bank Marketing selection and prediction-time policy |
| 4 | SEPM | Updated SRS, proposal, feasibility and UML |
| 5 | Data preparation | Leakage-safe preprocessing pipeline |
| 6 | Baselines | Reference classification results |
| 7 | Imbalance study | Class-weight/SMOTE comparison where valid |
| 8 | HPO | Grid/Random/Optuna experiments |
| 9 | Evaluation | Performance and efficiency tables |
| 10 | XAI | Global/local SHAP explanations |
| 11 | Stability | Repeated-seed/fold explanation stability |
| 12 | Analysis | Trade-off and research-gap findings |
| 13 | Reporting | Paper, presentation and final documentation |

## Experiment Control
The test set must not be used for HPO. Search budgets, seeds, splits, primary objective and stability procedure should be predefined. Every trial should record parameters, objective, runtime and model configuration.

## Controlled Experiment Matrix

| Configuration | HPO | Imbalance treatment |
|---|---|---|
| A | Default | None |
| B | HPO | None |
| C | Default | Class weighting |
| D | HPO | Class weighting |
| E | Default | SMOTE where valid |
| F | HPO | SMOTE where valid |

The final matrix may be reduced only if justified by computational constraints.
