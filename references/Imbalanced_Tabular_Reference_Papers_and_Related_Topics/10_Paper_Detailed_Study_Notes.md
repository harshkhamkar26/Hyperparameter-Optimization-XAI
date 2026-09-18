# 10-Paper Detailed Study Notes

## Paper 1 — A Survey on Imbalanced Learning: Latest Research, Applications and Future Directions

**Year:** 2024  
**Venue:** Artificial Intelligence Review  
**Link:** https://link.springer.com/article/10.1007/s10462-024-10759-6

### What problem does it address?
Real-world datasets frequently contain unequal class distributions. Conventional learning procedures can favor the majority class and overlook useful minority-class information.

### What the paper covers
The survey provides a broad map of imbalanced learning, including:
- data-level methods
- algorithm-level methods
- hybrid methods
- ensemble methods
- boosting/bagging
- cost-sensitive learning
- related imbalanced regression, clustering, long-tail and data-stream topics

### What the paper achieved
Its main value is a structured survey of the field and its major solution families rather than a single proposed classifier.

### What we are trying to gain
We use this paper as the **conceptual starting point**. Before implementing SMOTE or HPO, we need to understand what class imbalance is, why it matters, where it can be handled, and how it should be evaluated.

### Key lesson
**First understand the problem space; do not start with a technique.**

---

## Paper 2 — SMOTE: Synthetic Minority Over-sampling Technique

**Authors:** Chawla et al.  
**Year:** 2002  
**Venue:** Journal of Artificial Intelligence Research  
**Link:** https://doi.org/10.1613/jair.953

### What problem does it address?
Random oversampling can repeatedly duplicate minority observations. SMOTE was introduced to create synthetic minority examples rather than simply replicating existing minority samples.

### How it works — simple view
For a minority observation, SMOTE uses nearby minority observations and generates a synthetic point along the neighborhood relationship.

```
Minority A -------- Minority B
       \\          /
        \\        /
         Synthetic point
```

### What the paper achieved
It introduced a foundational synthetic oversampling technique that became central to subsequent imbalanced-learning research.

### What we are trying to gain
We need to understand the mechanics and assumptions of SMOTE so that later experiments do not treat it as a black-box “balance data” button.

### Key lesson
**SMOTE changes the training data by generating synthetic minority examples.**

---

## Paper 3 — To SMOTE, or not to SMOTE?

**Authors:** Yotam Elor; Hadar Averbuch-Elor  
**Year:** 2022  
**Link:** https://arxiv.org/abs/2201.08528

### What problem does it address?
The paper examines whether rebalancing/SMOTE is necessarily beneficial for imbalanced classification, particularly when strong classifiers and hyperparameter tuning are considered.

### What the paper achieved
It provides empirical evidence that challenges the automatic assumption that balancing must always improve classification.

### What we are trying to gain
This paper teaches us to include:
- original-data baselines
- rebalanced versions
- properly tuned models
- fair comparisons

### Key lesson
**“Imbalanced” does not automatically mean “apply SMOTE.”**

---

## Paper 4 — Do We Need Rebalancing Strategies? A Theoretical and Empirical Study Around SMOTE and Its Variants

**Authors:** Abdoulaye Sakho; Emmanuel Malherbe; Erwan Scornet  
**Year:** 2026  
**Venue:** AISTATS 2026 / PMLR 300  
**Link:** https://proceedings.mlr.press/v300/sakho26a.html

### What problem does it address?
It studies whether and when rebalancing strategies are needed, including SMOTE and variants, across tabular datasets.

### What the paper achieved
It provides a modern theoretical and empirical examination of rebalancing procedures rather than assuming a universal benefit.

### What we are trying to gain
We want to move from:

**“Does SMOTE work?”**

to:

**“Under what dataset/model conditions does rebalancing help?”**

### Key lesson
**The usefulness of rebalancing is context-dependent and should be investigated experimentally.**

---

## Paper 5 — Imbalance-XGBoost: Leveraging Weighted and Focal Losses for Binary Label-Imbalanced Classification with XGBoost

**Authors:** Chen Wang; Chengyuan Deng; Suzhen Wang  
**Year:** 2020  
**Link:** https://www.sciencedirect.com/science/article/pii/S0167865520302129

### What problem does it address?
Instead of relying only on resampling, the paper investigates handling binary label imbalance through weighted and focal loss ideas within XGBoost.

### What the paper achieved
It demonstrates the algorithm-level direction: modify the learning objective so that the learner pays appropriate attention to minority/difficult examples.

### What we are trying to gain
We need a direct conceptual comparison:

**Data-level:** change the dataset.

**Algorithm-level:** change the learning objective.

This gives our experiments a broader methodological basis than SMOTE alone.

### Key lesson
**You can address imbalance inside the learner, not only by modifying the dataset.**

---

## Paper 6 — Marketing Analytics in Banking 4.0: A Two-stage Explainable AI Framework for High-accuracy and Well-calibrated Predictions

**Authors:** Fahim Nasir; Abdulghani Ali Ahmed; Iryna Yevseyeva; Mehmet Sabir Kiraz  
**Year:** 2026  
**Venue:** PLOS ONE  
**Link:** https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0348767

### Setting
UCI Bank Marketing.

### Methods/topics relevant to us
- random oversampling
- random undersampling
- SMOTE
- ADASYN
- Borderline-SMOTE
- hyperparameter optimization
- calibration
- explainability/SHAP

### What the paper achieved
It provides an end-to-end bank-marketing framework connecting imbalance treatment, model optimization, probability calibration and explainability.

### What we are trying to gain
This is a major bridge between the general literature and our own domain.

We want to understand how to construct a controlled pipeline:

```
Bank Marketing
→ preprocessing
→ imbalance treatment
→ model
→ HPO
→ calibration
→ evaluation
→ SHAP
```

### Key lesson
**A useful research pipeline can evaluate prediction quality and explanation together rather than treating XAI as an afterthought.**

---

## Paper 7 — Using Ensemble Learning and Explainable AI to Predict Bank Marketing Customer Subscription

**Year:** 2026  
**Venue:** Scientific Reports  
**Link:** https://www.nature.com/articles/s41598-026-58149-y

### Problem/setting
Bank-marketing customer-subscription prediction, with attention to imbalance and differences between data distributions.

### What the paper achieved
It combines ensemble learning and explainability and considers external validation/distribution-shift issues.

### What we are trying to gain
We want to learn why a model that performs well on one dataset/test setting should still be examined for:
- generalization
- distribution shift
- external validation
- explanation behavior

### Key lesson
**A model's performance on one test distribution is not the entire evidence base for real-world reliability.**

---

## Paper 8 — Optuna: A Next-generation Hyperparameter Optimization Framework

**Authors:** Takuya Akiba; Shotaro Sano; Toshihiko Yanase; Takeru Ohta; Masanori Koyama  
**Year:** 2019  
**Venue:** KDD 2019  
**Link:** https://doi.org/10.1145/3292500.3330701

### Problem
Manual hyperparameter selection is inefficient and does not provide a systematic search.

### What the paper achieved
Optuna introduced a flexible define-by-run HPO framework with efficient search and pruning capabilities.

### What we are trying to gain
We need to understand how to run reproducible optimization experiments rather than selecting model parameters manually.

Example:

```
Search space
→ Trial
→ Train
→ Objective metric
→ Continue/prune
→ Repeat
→ Best configuration
```

### Key lesson
**HPO should be systematic, reproducible and computationally aware.**

---

## Paper 9 — Evaluating the Stability of Model Explanations in Instance-dependent Cost-sensitive Credit Scoring

**Authors:** Matteo Ballegeer; Matthias Bogaert; Dries F. Benoit  
**Year:** 2025  
**Venue:** European Journal of Operational Research  
**Link:** https://www.sciencedirect.com/science/article/pii/S0377221725004230

### Problem
A model explanation may look useful but can change when the data/model conditions change.

### What the paper achieved
It studies explanation stability in credit-scoring settings, including SHAP/LIME-related explanation behavior and cost-sensitive considerations.

### What we are trying to gain
We want to add a second dimension to our evaluation:

```
Predictive performance
+
Explanation stability
```

We should not assume that the best predictive model automatically has the most stable explanations.

### Key lesson
**XAI needs evaluation too.**

---

## Paper 10 — Assessing the Fragility of SHAP-Based Model Explanations Using Counterfactuals

**Authors:** Cornelia C. Käsbohrer; Sebastian Mair; Lili Jiang  
**Year:** 2026  
**Venue:** NLDL / PMLR 307  
**Link:** https://proceedings.mlr.press/v307/kasbohrer26a.html

### Problem
SHAP explanations can potentially be fragile under changes to the input.

### What the paper achieved
It investigates SHAP explanation fragility using counterfactual reasoning/perturbations.

### What we are trying to gain
We want to learn how to test whether explanations remain meaningful when input conditions change realistically.

### Simple idea

```
Original instance
      ↓
SHAP explanation
      ↓
Realistic counterfactual change
      ↓
New explanation
      ↓
Compare
```

### Key lesson
**An explanation should be treated as something that can be evaluated for robustness, not automatically as ground truth.**

---

# Final sequence summary

1. **Paper 1 — Foundation:** What is imbalanced learning?
2. **Paper 2 — Technique:** How does SMOTE work?
3. **Paper 3 — Critical thinking:** Do we really need SMOTE?
4. **Paper 4 — Conditions:** When does rebalancing help?
5. **Paper 5 — Alternative:** Can the learning objective handle imbalance?
6. **Paper 6 — Integration:** How do imbalance, HPO, calibration and XAI work together in Bank Marketing?
7. **Paper 7 — Generalization:** What happens under ensemble learning and distribution shift?
8. **Paper 8 — Optimization:** How do we systematically tune hyperparameters?
9. **Paper 9 — XAI reliability:** Are explanations stable?
10. **Paper 10 — XAI robustness:** Are SHAP explanations fragile under counterfactual changes?

## Final research direction

```
Imbalanced Tabular Classification
                +
       Multiple imbalance treatments
                +
      Multiple ML classifiers
                +
      Hyperparameter Optimization
                +
       Computational efficiency
                +
          SHAP / XAI
                +
      Explanation stability
                +
       Robustness analysis
                ↓
       Controlled research study
```

The intended contribution is **not** simply “SMOTE + XGBoost + SHAP.” The literature already contains combinations of these ideas. The stronger direction is a controlled, reproducible study of the interaction:

**HPO strategy × imbalance treatment × predictive performance × computational efficiency × explanation stability**
