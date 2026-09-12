# Detailed Design Description

## 1. Data Flow
1. Load the UCI Bank Marketing dataset.
2. Validate schema, target values and data quality.
3. Separate target `y` from predictors.
4. Create stratified train/validation/test partitions.
5. Build preprocessing pipelines using training data only.
6. Analyze class imbalance.
7. Train baseline classifier(s).
8. Evaluate baseline using class-sensitive metrics.
9. Define HPO search spaces and optimization strategies.
10. Run bounded HPO experiments and record every trial.
11. Select the best configuration using the predefined validation objective.
12. Retrain/evaluate the optimized model without touching the final test set during tuning.
13. Generate global and local SHAP explanations.
14. Compare baseline and optimized feature attributions.
15. Calculate explanation stability/consistency using the documented repeated-sample or fold procedure.
16. Produce final performance, efficiency and XAI comparisons.

## 2. Primary Classification Task
The binary target is:
- `yes` = customer subscribed to a term deposit.
- `no` = customer did not subscribe.

The positive class is the minority class and therefore receives explicit evaluation through precision, recall and F1 rather than relying only on accuracy.

## 3. Inputs
- Public UCI Bank Marketing dataset
- Target variable `y`
- Model configuration
- HPO strategy
- Hyperparameter search space
- Validation objective
- Random seed
- Experiment budget

## 4. Outputs
- Data-quality report
- Class-distribution analysis
- Baseline metrics
- HPO trial history
- Best hyperparameters
- Optimized-model metrics
- Runtime/trial efficiency measurements
- SHAP global feature importance
- SHAP local explanations
- Explanation stability measurements
- Baseline-vs-optimized comparison
- Final research report

## 5. Preprocessing Design
Categorical variables will be encoded through a reproducible pipeline. Numerical features will be handled according to the selected model requirements. Any imputation, encoding or scaling must be fitted only within training data/folds to prevent leakage.

## 6. HPO Design
The initial comparison will consider:
- Grid Search as a structured exhaustive baseline where feasible.
- Random Search as a stochastic baseline.
- TPE/Bayesian optimization through Optuna as the intelligent search method.

Search spaces and trial budgets will be fixed before the final comparison. The primary objective will be selected from class-sensitive metrics, with secondary metrics reported for transparency.

## 7. Explainability Design
SHAP will be used to provide:
- Global mean absolute feature importance.
- SHAP summary/beeswarm plots.
- Local waterfall/force-style explanations where supported.
- Comparison of feature rankings between baseline and optimized models.

## 8. Explanation Stability Design
Explanation stability will be treated as an experimental property rather than assumed. A documented repeated-sample/fold procedure will compare feature rankings or attribution distributions across runs. The selected stability measure will be finalized before the main experiment.

## 9. Error Handling
The system should provide clear errors for missing files, invalid target values, unsupported feature types, failed trials, invalid hyperparameters, insufficient class samples and unsupported XAI/model combinations.

## 10. Design Constraints
- Academic laptop CPU/RAM constraints.
- Imbalanced target distribution.
- Historical nature of the dataset.
- Bounded HPO budget.
- SHAP computational cost.
- Explanations describe model behaviour and are not causal claims.
