# Design Description

## 1. Data Flow

```text
UCI Bank Marketing Dataset
  ↓
Audit + Target Validation
  ↓
Prediction-time Feature Policy
  ↓
Train/Validation/Test Split
  ↓
Leakage-safe Preprocessing
  ↓
Imbalance Treatment
  ↓
Baseline / HPO Model
  ↓
Validation Metrics
  ↓
Final Test Evaluation
  ↓
SHAP Global + Local Explanation
  ↓
Explanation Stability
  ↓
Research Comparison
```

## 2. Domain and Model Design
The application domain is **Marketing / Banking Marketing Analytics**, using the **UCI Bank Marketing Dataset** to predict term-deposit subscription (`yes`/`no`). The core classifiers are **Random Forest, XGBoost and CatBoost**. These are evaluated first as default/reference models and then under controlled hyperparameter optimization.

## 3. Imbalance Design
The `yes`/`no` target distribution will be measured before modeling. Candidate treatments include class weighting and SMOTE where assumptions are appropriate. Resampling must occur only inside training folds.

## 3. HPO Design
Search strategies may include Grid Search, Random Search and Optuna/TPE. The primary objective must be selected before the main experiment. F1, recall or PR-AUC are candidates depending on the research question. All strategies should receive comparable compute budgets.

## 4. Evaluation Design
Report precision, recall, F1, balanced accuracy, ROC-AUC and PR-AUC, along with confusion matrices. Also report trial count and runtime. Mean ± SD across repeated seeds/folds should be used where computationally feasible.

## 5. XAI Design
SHAP will provide global feature importance and local explanations for representative predictions. Default and optimized models, and different imbalance treatments, will be compared.

## 6. Explanation Stability
Stability will be evaluated by repeating explanations across predefined seeds, folds or controlled samples. Candidate measures include Spearman/Kendall rank correlation and top-k feature overlap. The final measure will be fixed before the main experiment.

## 7. Error Handling
Invalid rows, failed HPO trials, unsupported configurations and resource failures will be logged rather than silently discarded.

## 8. Prediction-time Feature Policy
Features whose values are only known after the marketing contact, especially `duration`, require explicit treatment. The project will define and document whether the primary experiment is a pre-contact targeting model or a post-contact analytical model. This decision will be fixed before HPO.
