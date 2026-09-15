# Design Description

## 1. Data Flow

```text
IDS Dataset
  ↓
Audit + Label Validation
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

## 2. Imbalance Design
The class distribution will be measured before modeling. Candidate treatments include class weighting and SMOTE-family methods where their assumptions are appropriate. Resampling must occur only inside training folds.

## 3. HPO Design
Search strategies may include Grid Search, Random Search and Optuna/TPE. The primary objective must be selected before the main experiment. F1, recall or PR-AUC are candidates depending on the final task formulation. All strategies should receive comparable compute budgets.

## 4. Evaluation Design
Report precision, recall, F1, balanced accuracy, ROC-AUC and PR-AUC. For multiclass IDS tasks, include macro/weighted metrics and per-attack-class results. Also report trial count and runtime.

## 5. XAI Design
SHAP will provide global feature importance and local explanations for representative predictions. Baseline and optimized models will be compared.

## 6. Explanation Stability
Stability will be evaluated by repeating explanations across predefined seeds, folds or controlled samples. Candidate measures include rank correlation and top-k feature overlap; the final measure will be fixed before the main experiment.

## 7. Error Handling
Invalid rows, failed HPO trials, unsupported configurations and resource failures will be logged rather than silently discarded.

## 8. Dataset Decision
The dataset remains intentionally TBD until the literature review compares CIC-IDS2017, CSE-CIC-IDS2018, UNSW-NB15, TON_IoT and CIC-DDoS2019.
