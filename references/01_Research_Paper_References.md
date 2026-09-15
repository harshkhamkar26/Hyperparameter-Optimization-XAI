# Research Paper References

## A. Bank Marketing and Directly Related Studies

1. Moro, S., Cortez, P., & Rita, P. (2014). *A data-driven approach to predict the success of bank telemarketing*. Decision Support Systems, 62, 22–31. https://doi.org/10.1016/j.dss.2014.03.001

2. Nasir, M. et al. (2026). *Marketing analytics in banking 4.0: A two-stage explainable AI framework for high-accuracy and well-calibrated predictions*. PLOS ONE. https://doi.org/10.1371/journal.pone.0348767

3. Wang, Y. et al. (2026). *Using ensemble learning and explainable AI to predict bank marketing customer subscription*. Scientific Reports. https://doi.org/10.1038/s41598-026-58149-y

4. Abidin, Z. et al. (2025). *Improving Term Deposit Customer Prediction Using Support Vector Machine with SMOTE and Hyperparameter Tuning in Bank Marketing Campaigns*. Jurnal Teknik Informatika, 6(3). https://doi.org/10.52436/1.jutif.2025.6.3.4585

5. Saket, M., Sahlaoui, H., Alaoui, E. A. A., & Merras, M. (2025). *Interpreting Bank Term Deposit Prediction Models: A Comprehensive SHAP Approach*. 4th International Conference on Embedded Systems and Artificial Intelligence (ESAI 2025). DOI: 10.1109/ESAI67033.2025.11438631.

## B. Hyperparameter Optimization / AutoML

6. Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). *Optuna: A Next-generation Hyperparameter Optimization Framework*. Proceedings of KDD. https://doi.org/10.1145/3292500.3330701

7. Bergstra, J., & Bengio, Y. (2012). *Random Search for Hyper-Parameter Optimization*. Journal of Machine Learning Research, 13, 281–305.

8. Feurer, M., & Hutter, F. (2019). *Hyperparameter Optimization*. In *Automated Machine Learning: Methods, Systems, Challenges*. Springer.

9. *Automated imbalanced classification via meta-learning* (ATOMIC). This work frames joint workflow selection and hyperparameter optimization for imbalanced binary classification and evaluates the approach across 101 datasets. It is useful for positioning the project against broader automated imbalanced-learning research.

## C. Explainable AI and Explanation Stability

10. Lundberg, S. M., & Lee, S.-I. (2017). *A Unified Approach to Interpreting Model Predictions*. NeurIPS 30.

11. Lundberg, S. M. et al. (2020). *From local explanations to global understanding with explainable AI for trees*. Nature Machine Intelligence, 2, 56–67. https://doi.org/10.1038/s42256-019-0138-9

12. Ballegeer, M., Bogaert, M., & Benoit, D. F. (2025). *Evaluating the stability of model explanations in instance-dependent cost-sensitive credit scoring*. European Journal of Operational Research, 326(3), 630–640. https://doi.org/10.1016/j.ejor.2025.05.039

13. Kasbohrer, et al. (2026). *Assessing the Fragility of SHAP-Based Model Explanations Using Counterfactuals*. Proceedings of Machine Learning Research, vol. 307. This recent work is relevant to the project's planned multi-seed and perturbation-based explanation stability analysis.

14. *Stakeholder-centric explanations for black-box decisions: an XAI process model and its application to automotive goodwill assessments* (2024). Relevant for the distinction between explanation quality, faithfulness, and stability and for formalizing stability under input perturbations.

## D. Imbalanced Classification

15. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). *SMOTE: Synthetic Minority Over-sampling Technique*. Journal of Artificial Intelligence Research, 16, 321–357. https://doi.org/10.1613/jair.953

16. Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432. https://doi.org/10.1371/journal.pone.0118432

17. *Evaluating Ensemble Learning Techniques for Class Imbalance in Machine Learning: A Comparative Analysis of Balanced Random Forest, SMOTE-RF, SMOTEBoost, and RUSBoost* (2024). Scientific Journal of Informatics, 11(4), 969–980. https://doi.org/10.15294/sji.v11i4.15937

## E. Tabular ML / Conference Benchmark Context

18. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). *Why do tree-based models still outperform deep learning on typical tabular data?* NeurIPS 35.

19. McElfresh, D. et al. (2023). *When Do Neural Nets Outperform Boosted Trees on Tabular Data?* NeurIPS.

20. Recent tabular benchmarking literature should be used to justify why tree-based models are strong baselines for structured data and why comparisons should be controlled by dataset, preprocessing, compute budget, and evaluation protocol.

## F. Dataset and Official Documentation

21. UCI Machine Learning Repository. *Bank Marketing Dataset*. University of California, Irvine.

22. Scikit-learn documentation. Model selection, preprocessing, metrics, and classification utilities.

23. Optuna documentation. Hyperparameter optimization framework and samplers.

24. SHAP documentation. SHapley Additive exPlanations.

25. imbalanced-learn documentation. Tools for classification with imbalanced datasets.

## Paper-by-Paper Lessons for Our Project

### Nasir et al. (2026)
Strongly relevant because it combines imbalanced Bank Marketing prediction, hyperparameter tuning, sampling strategies, computational cost, calibration, and SHAP. Its framework supports our decision to evaluate more than accuracy alone. Our project should differentiate itself by making **HPO strategy and explanation stability** central experimental variables rather than treating them only as supporting components.

### Abidin et al. (2025)
Shows that SMOTE + hyperparameter tuning can improve term-deposit prediction using SVM. This confirms that “SMOTE + tuning on Bank Marketing” is not sufficient novelty. We therefore need controlled comparisons across HPO methods, imbalance treatments, efficiency, and XAI stability.

### Saket et al. (2025)
Shows that Bank Marketing + CatBoost + SHAP + tuning has already been studied in a conference setting. Therefore, our contribution should not be framed as simply applying SHAP to a tuned Bank Marketing model.

### Akiba et al. (2019)
Provides the methodological foundation for Optuna. We should report search space, sampler, number of trials, objective function, seed, and compute budget so that our optimization experiment is reproducible.

### Lundberg & Lee (2017) and Lundberg et al. (2020)
Provide the theoretical and practical foundation for SHAP. We should distinguish global feature importance from local attribution and avoid presenting a SHAP plot as proof that an explanation is automatically reliable.

### Ballegeer et al. (2025)
This is particularly important for our research gap. It explicitly studies explanation stability together with imbalance and model performance, showing that more imbalance can degrade explanation stability. This means our stability experiment is well motivated, but our contribution must be a distinct controlled study of the **interaction between HPO, imbalance treatment, and explanation stability** on the Bank Marketing task.

### Kasbohrer et al. (2026)
Motivates testing explanation fragility under controlled perturbations and multiple seeds rather than reporting a single SHAP plot. We can adapt a simpler, reproducible version suitable for our undergraduate research scope.

### Grinsztajn et al. (2022)
Supports the use of tree-based models as strong baselines for tabular data. It also warns us not to assume that a more complex model is automatically better.

## Research Gap After Literature Analysis

The literature shows that the following have already been demonstrated independently or in combinations:

- Bank Marketing prediction
- SMOTE / imbalance handling
- Hyperparameter tuning
- Optuna-based optimization
- CatBoost/XGBoost/Random Forest models
- SHAP-based explanations
- Computational-cost comparison
- Explanation-stability analysis

Therefore, our research gap should **not** be stated as “no one has combined HPO and SHAP.”

Our proposed empirical contribution is:

> **A controlled evaluation of how HPO strategy and imbalance treatment jointly affect predictive performance, computational efficiency, and explanation stability for imbalanced tabular classification.**

The study should compare default, Grid Search, Random Search, and Optuna/TPE configurations under a fixed compute budget, while comparing imbalance treatments and measuring SHAP ranking stability across seeds/folds and controlled perturbations.

## Conference-Paper Study Strategy

For every important paper we read, we should extract:

1. Problem statement
2. Research gap
3. Dataset(s)
4. Preprocessing
5. Models
6. HPO/search method
7. Objective function
8. Imbalance treatment
9. Evaluation metrics
10. XAI method
11. Stability/robustness method
12. Main results
13. Limitations
14. Claimed contribution
15. What we can learn or improve

This structure will be used for the project's literature-review matrix and final research paper.

## Verification Note

Before final conference submission, verify complete author lists, venue, volume/issue/pages, DOI, and publication metadata from the official publisher or DOI record. The repository reference list is intended as a research-working bibliography and should be normalized to the target conference's citation style before submission.
