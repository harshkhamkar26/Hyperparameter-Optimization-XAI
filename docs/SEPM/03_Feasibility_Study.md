# Feasibility Study

## 1. Technical Feasibility
The project is technically feasible using Python and open-source libraries. The UCI Bank Marketing dataset is a public tabular binary-classification dataset. Scikit-learn supports preprocessing, model training and evaluation; Optuna supports efficient hyperparameter optimization; SHAP supports post-hoc model explanations; and imbalanced-learn can support class-imbalance experiments.

The dataset size is practical for a student laptop. Optimization budgets can be capped to control runtime.

**Result:** Feasible.

## 2. Economic Feasibility
The proposed software stack is open source. The selected dataset is publicly available for academic use. No paid cloud service or commercial ML platform is required.

**Result:** Feasible at minimal cost.

## 3. Operational Feasibility
The workflow is suitable for a student research project and can produce understandable outputs for an evaluator: model comparisons, confusion matrices, ROC/PR curves, optimization histories and SHAP explanations.

**Result:** Feasible.

## 4. Schedule Feasibility
The project can be completed incrementally through requirements, literature review, dataset analysis, design, baseline experiments, HPO, XAI, testing and documentation. GitHub commits will provide an auditable progress history.

**Result:** Feasible with milestone-based planning.

## 5. Research Feasibility
The topic is academically feasible because the selected dataset has substantial prior literature. Existing work provides benchmarks against which the project can position itself. The project will avoid claiming that Bank Marketing + HPO + SHAP is itself novel. The research contribution will instead focus on comparative HPO strategy, class-sensitive objectives, computational efficiency and explanation stability.

**Result:** Feasible, with novelty dependent on the final experimental design.

## 6. Legal and Ethical Feasibility
The project will use a public research dataset and will document its source and usage conditions. The analysis is for academic experimentation, not real banking decisions. Results must not be presented as a production credit or customer-selection system. SHAP explanations will be treated as model explanations rather than causal conclusions.

**Result:** Feasible subject to correct citation, licensing and responsible interpretation.

## 7. Key Feasibility Risks
- HPO search spaces may be too large for available hardware.
- Class imbalance can make accuracy misleading.
- Repeated SHAP analysis may increase runtime.
- Results may not outperform recent literature.
- Explanation stability may be difficult to define consistently.

## Conclusion
The project is technically, economically, operationally and academically feasible. The main requirement is a controlled research scope: fixed datasets, reproducible splits, bounded optimization budgets and clearly defined evaluation criteria.
