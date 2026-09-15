# References and Research Papers

## Project
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing**

## 1. Bank Marketing and Directly Related Research

1. Moro, S., Cortez, P., & Rita, P. (2014). *A data-driven approach to predict the success of bank telemarketing*. Decision Support Systems, 62, 22–31. DOI: 10.1016/j.dss.2014.03.001.

2. Nasir, M. et al. (2026). *Marketing analytics in banking 4.0: A two-stage explainable AI framework for high-accuracy and well-calibrated predictions*. PLOS ONE. DOI: 10.1371/journal.pone.0348767.

3. Wang, Y. et al. (2026). *Using ensemble learning and explainable AI to predict bank marketing customer subscription*. Scientific Reports. DOI: 10.1038/s41598-026-58149-y.

4. Yu, Q. (2025). *Enhancing Bank Term Deposit Predictions: A Machine Learning Approach with CatBoost and SHAP*. DOI: 10.54254/2755-2721/2025.19485.

5. Abidin, D. Z. et al. (2025). *Improving Term Deposit Customer Prediction Using Support Vector Machine with SMOTE and Hyperparameter Tuning in Bank Marketing Campaigns*. Jurnal Teknik Informatika, 6(3). DOI: 10.52436/1.jutif.2025.6.3.4585.

6. Saket, M., Sahlaoui, H., Alaoui, E. A. A., & Merras, M. (2025). *Interpreting Bank Term Deposit Prediction Models: A Comprehensive SHAP Approach*. 4th International Conference on Embedded Systems and Artificial Intelligence (ESAI 2025). DOI: 10.1109/ESAI67033.2025.11438631.

## 2. Hyperparameter Optimization

7. Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). *Optuna: A Next-generation Hyperparameter Optimization Framework*. Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. DOI: 10.1145/3292500.3330701.

8. Bergstra, J., & Bengio, Y. (2012). *Random Search for Hyper-Parameter Optimization*. Journal of Machine Learning Research, 13, 281–305.

9. Feurer, M., & Hutter, F. (2019). *Hyperparameter Optimization*. In *Automated Machine Learning: Methods, Systems, Challenges*. Springer.

## 3. Explainable AI and SHAP

10. Lundberg, S. M., & Lee, S.-I. (2017). *A Unified Approach to Interpreting Model Predictions*. Advances in Neural Information Processing Systems 30 (NeurIPS).

11. Lundberg, S. M. et al. (2020). *From local explanations to global understanding with explainable AI for trees*. Nature Machine Intelligence, 2, 56–67. DOI: 10.1038/s42256-019-0138-9.

12. Ballegeer, M., Bogaert, M., & Benoit, D. F. (2025). *Evaluating the stability of model explanations in instance-dependent cost-sensitive credit scoring*. European Journal of Operational Research, 326(3), 630–640. DOI: 10.1016/j.ejor.2025.05.039.

## 4. Imbalanced Learning and Evaluation

13. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). *SMOTE: Synthetic Minority Over-sampling Technique*. Journal of Artificial Intelligence Research, 16, 321–357. DOI: 10.1613/jair.953.

14. Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432. DOI: 10.1371/journal.pone.0118432.

## 5. Tabular Machine Learning

15. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). *Why do tree-based models still outperform deep learning on typical tabular data?* Advances in Neural Information Processing Systems 35 (NeurIPS).

16. McElfresh, D. et al. (2023). *When Do Neural Nets Outperform Boosted Trees on Tabular Data?* Advances in Neural Information Processing Systems (NeurIPS).

## 6. Official Dataset / Software References

17. UCI Machine Learning Repository. *Bank Marketing Dataset*. University of California, Irvine.

18. Scikit-learn. *Model selection, preprocessing and classification metrics documentation*.

19. Optuna. *Hyperparameter optimization framework documentation*.

20. SHAP. *SHapley Additive exPlanations documentation*.

21. imbalanced-learn. *Tools for classification with imbalanced datasets*.

## 7. Research Positioning

Recent Bank Marketing literature already demonstrates class balancing, hyperparameter tuning, Optuna/TPE, CatBoost/XGBoost, SHAP and computational evaluation. Therefore, the proposed project must not claim novelty from any one of these components alone.

The intended research contribution is the controlled empirical study of:

**HPO strategy × imbalance treatment × predictive performance × computational efficiency × explanation stability**

## 8. Paper Study Priorities

**Tier 1 — Must study deeply:** Moro et al. (2014); Nasir et al. (2026); Wang et al. (2026); Saket et al. (2025); Abidin et al. (2025); Ballegeer et al. (2025); Akiba et al. (2019); Lundberg & Lee (2017).

**Tier 2 — Methodology foundation:** Bergstra & Bengio (2012); Lundberg et al. (2020); Chawla et al. (2002); Saito & Rehmsmeier (2015); Grinsztajn et al. (2022); McElfresh et al. (2023).

## 9. What We Must Extract From Each Paper

For the literature matrix, record: problem, research gap, dataset, preprocessing, models, HPO method, objective function, imbalance treatment, metrics, XAI method, stability/robustness method, main results, limitations and claimed contribution.

## 10. Verification Rule
Before final paper submission, verify all author lists, DOI, venue, publication year, volume/issue/pages and dataset citations against the publisher or DOI record.
