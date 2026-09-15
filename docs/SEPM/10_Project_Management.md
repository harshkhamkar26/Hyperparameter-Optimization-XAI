# Project Management

## Project
**An Explainable Hyperparameter Optimization Framework for Imbalanced Cybersecurity Intrusion Detection**

## Management Objectives
- Maintain a fixed and traceable research scope.
- Keep dataset, methodology and experiment changes documented.
- Ensure reproducibility of every reported result.
- Separate research documentation from implementation until the protocol is approved.

## Work Areas
| Area | Responsibility |
|---|---|
| Literature | IDS, imbalance, HPO and XAI review |
| Dataset | Selection, licensing, audit and preprocessing |
| ML | Baselines and optimized models |
| HPO | Search spaces, objectives, budgets and trial logging |
| XAI | SHAP explanations and stability |
| Evaluation | Metrics, statistical/repeated-seed analysis |
| SEPM | SRS, proposal, feasibility, UML, testing and traceability |
| Reporting | Research paper, figures and conclusions |

## Change Control
Any change to dataset, target definition, split strategy, primary HPO objective, model family or stability metric must be documented with its reason and impact before being used in the main experiment.

## Reproducibility Record
Record dataset version/hash where possible, software versions, hardware, seeds, data split, preprocessing, model parameters, search space, HPO budget, objective and output artifacts.

## Quality Rules
No result is reported from a test set used during HPO. Failed experiments are logged. Negative findings are retained. No credentials or private security data are committed to GitHub.
