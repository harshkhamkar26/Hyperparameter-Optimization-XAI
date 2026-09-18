# Imbalanced Tabular Classification — Reference Papers & Related Topics

This folder contains the 10-paper literature foundation selected for the research project:

**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing**

## Research direction

**Imbalanced Tabular Classification → Imbalance Handling → Hyperparameter Optimization → Predictive Evaluation → XAI/SHAP → Explanation Stability**

The papers are arranged as a learning sequence rather than as unrelated references.

## What we are trying to gain from this literature

We are not studying these papers only to collect citations. We are using them to understand:

1. Why class imbalance creates a classification challenge.
2. How data-level methods such as SMOTE, random oversampling and undersampling work.
3. Why rebalancing should not automatically be assumed to improve performance.
4. When the effect of rebalancing depends on dataset/model characteristics.
5. How algorithm-level methods such as class weighting and weighted/focal losses provide alternatives to data modification.
6. How imbalance handling, HPO, calibration and XAI can be combined in a reproducible tabular ML pipeline.
7. Why external validation and distribution shift matter for real-world generalization.
8. How systematic HPO can be performed with methods such as Optuna/TPE and pruning.
9. Why model explanations themselves need stability evaluation.
10. How counterfactuals can be used to investigate the robustness/fragility of SHAP-based explanations.

## Central research learning path

```
Paper 1: Understand the field
        ↓
Paper 2: Learn SMOTE
        ↓
Paper 3: Question automatic SMOTE
        ↓
Paper 4: Study when rebalancing helps
        ↓
Paper 5: Learn algorithm/loss-level handling
        ↓
Paper 6: Combine imbalance + HPO + XAI + calibration
        ↓
Paper 7: Consider ensembles + distribution shift + external validation
        ↓
Paper 8: Learn systematic HPO with Optuna
        ↓
Paper 9: Study explanation stability
        ↓
Paper 10: Study explanation fragility using counterfactuals
        ↓
Our research:
Imbalance treatment × HPO × performance × efficiency × explanation stability
```

## Important experimental principle

The literature does **not** justify assuming that one imbalance technique is universally best. The project should therefore retain a meaningful **no-rebalancing baseline**, compare multiple treatments fairly, tune models without contaminating the test set, and evaluate minority-class performance rather than relying on accuracy alone.

---

## 10-paper sequence

| # | Paper | Main topic | What the paper contributes | What we are trying to gain |
|---|---|---|---|---|
| 1 | A Survey on Imbalanced Learning: Latest Research, Applications and Future Directions | Imbalanced learning foundations | Maps major approaches: data-level, algorithm-level, hybrid, ensemble and related areas | Build the conceptual foundation and research vocabulary |
| 2 | SMOTE: Synthetic Minority Over-sampling Technique | Synthetic oversampling | Introduces SMOTE for generating synthetic minority samples using minority-neighbor information | Understand exactly how SMOTE works and what assumptions/risks it introduces |
| 3 | To SMOTE, or not to SMOTE? | Rebalancing vs no rebalancing | Empirically questions whether balancing is always beneficial, including the role of strong classifiers and tuning | Learn why SMOTE must be tested rather than automatically applied |
| 4 | Do We Need Rebalancing Strategies? A Theoretical and Empirical Study Around SMOTE and Its Variants | Conditions for rebalancing | Studies when rebalancing is useful across tabular datasets and SMOTE variants | Move from “does SMOTE work?” to “when does rebalancing help?” |
| 5 | Imbalance-XGBoost: Leveraging Weighted and Focal Losses for Binary Label-Imbalanced Classification with XGBoost | Algorithm-level imbalance handling | Uses weighted/focal loss ideas inside XGBoost instead of relying only on resampling | Compare data-level and algorithm-level strategies |
| 6 | Marketing Analytics in Banking 4.0: A Two-stage Explainable AI Framework for High-accuracy and Well-calibrated Predictions | Bank Marketing + imbalance + HPO + XAI | Integrates imbalance treatments, optimization, calibration and explainability in a bank-marketing setting | Understand an end-to-end pipeline close to our target domain |
| 7 | Using Ensemble Learning and Explainable AI to Predict Bank Marketing Customer Subscription | Ensemble + XAI + generalization | Studies bank-marketing prediction with imbalance/distribution-shift considerations and explainability | Learn how model combination, external validation and distribution shift affect conclusions |
| 8 | Optuna: A Next-generation Hyperparameter Optimization Framework | HPO | Introduces Optuna's define-by-run approach, efficient search and pruning concepts | Learn the HPO methodology/tooling needed for controlled experiments |
| 9 | Evaluating the Stability of Model Explanations in Instance-dependent Cost-sensitive Credit Scoring | XAI stability | Examines stability of model explanations under credit-scoring and cost-sensitive settings | Learn how to evaluate whether explanations remain consistent |
| 10 | Assessing the Fragility of SHAP-Based Model Explanations Using Counterfactuals | SHAP robustness | Investigates SHAP explanation fragility using counterfactual perturbations | Learn how to test whether explanations remain meaningful under realistic changes |

## Master takeaway

The literature journey moves from **understanding class imbalance**, to **changing the data**, to **questioning whether changing the data is necessary**, to **understanding alternative loss-level methods**, then to **HPO and XAI**, and finally to **the reliability of explanations themselves**.

This supports our intended research direction:

> **Study the interaction between imbalance treatment and hyperparameter optimization on imbalanced tabular classification, while evaluating not only predictive performance and computational efficiency but also the stability of SHAP explanations.**

## Related topics to study

- Class imbalance
- Majority/minority classes
- Imbalanced tabular classification
- Random oversampling (ROS)
- Random undersampling (RUS)
- SMOTE
- Borderline-SMOTE
- ADASYN
- Safe-Level-SMOTE
- Class weighting
- Cost-sensitive learning
- Weighted loss
- Focal loss
- Bagging
- Boosting
- Ensemble learning
- Hyperparameter optimization
- Grid Search
- Random Search
- Bayesian/TPE-style optimization
- Optuna
- Pruning
- Cross-validation
- Data leakage prevention
- Precision
- Recall
- F1-score
- Balanced Accuracy
- G-mean
- ROC-AUC
- PR-AUC
- Probability calibration
- SHAP
- LIME
- Global explanations
- Local explanations
- Explanation stability
- Explanation robustness/fragility
- Counterfactual explanations
- Distribution shift
- External validation

## Project-specific research questions suggested by the sequence

1. How does the choice of imbalance treatment affect different tabular classifiers?
2. Does hyperparameter optimization change the apparent benefit of rebalancing?
3. Which imbalance-treatment/model combinations provide strong minority-class performance?
4. What is the computational cost of obtaining optimized configurations?
5. Does imbalance treatment change global and local SHAP explanations?
6. Are SHAP explanations stable across different imbalance treatments and optimized models?
7. How robust are explanations to realistic input perturbations?
8. Can a controlled comparison identify conditions under which rebalancing is useful rather than assuming a universal best method?

> **Note:** The “What we are trying to gain” column describes our study purpose/interpretation; it is not a claim that each paper itself proposed our research objective.
