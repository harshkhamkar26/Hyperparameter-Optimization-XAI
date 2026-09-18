# Project Management

## Project
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing**

## Management Objectives
- Maintain a fixed and traceable Bank Marketing research scope.
- Keep dataset, prediction-time policy, methodology and experiment changes documented.
- Ensure reproducibility of every reported result.
- Separate research documentation from implementation until the protocol is approved.

## Work Areas
| Area | Responsibility |
|---|---|
| Literature | Bank Marketing, imbalance, HPO and XAI review |
| Dataset | UCI dataset validation, feature timing and preprocessing |
| ML | Random Forest, XGBoost and CatBoost baselines and optimized models |
| HPO | Search spaces, objectives, budgets and trial logging |
| XAI | SHAP explanations and stability |
| Evaluation | Metrics, statistical/repeated-seed analysis |
| SEPM | SRS, proposal, feasibility, UML, testing and traceability |
| Reporting | Research paper, figures and conclusions |

## Change Control
Any change to target definition, prediction-time feature policy, split strategy, primary HPO objective, model family, imbalance treatment or stability metric must be documented with its reason and impact before being used in the main experiment.

## Reproducibility Record
Record dataset version/hash where possible, software versions, hardware, seeds, data split, preprocessing, model parameters, search space, HPO budget, objective and output artifacts.

## Quality Rules
No result is reported from a test set used during HPO. Failed experiments are logged. Negative findings are retained. No private customer data or credentials are committed to GitHub.
