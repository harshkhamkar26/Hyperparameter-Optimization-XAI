# References and Research Papers

## Purpose
This document records the principal academic papers, methodological references, and official dataset/tool documentation supporting the project **Explainable Hyperparameter Optimization for Imbalanced Tabular Classification**.

## Core Bank Marketing References

1. Moro, S., Cortez, P., & Rita, P. (2014). *A data-driven approach to predict the success of bank telemarketing*. Decision Support Systems, 62, 22–31. https://doi.org/10.1016/j.dss.2014.03.001

2. Nasir, M. et al. (2026). *Marketing analytics in banking 4.0: A two-stage explainable AI framework for high-accuracy and well-calibrated predictions*. PLOS ONE. https://doi.org/10.1371/journal.pone.0348767

3. Wang, Y. et al. (2026). *Using ensemble learning and explainable AI to predict bank marketing customer subscription*. Scientific Reports. https://doi.org/10.1038/s41598-026-58149-y

4. Abidin, Z. et al. (2025). *Improving Term Deposit Customer Prediction Using Support Vector Machine with SMOTE and Hyperparameter Tuning in Bank Marketing Campaigns*. Jurnal Teknik Informatika, 6(3). https://doi.org/10.52436/1.jutif.2025.6.3.4585

## Hyperparameter Optimization

5. Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). *Optuna: A Next-generation Hyperparameter Optimization Framework*. Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. https://doi.org/10.1145/3292500.3330701

6. Bergstra, J., & Bengio, Y. (2012). *Random Search for Hyper-Parameter Optimization*. Journal of Machine Learning Research, 13, 281–305.

7. Feurer, M., & Hutter, F. (2019). *Hyperparameter Optimization*. In Automated Machine Learning: Methods, Systems, Challenges. Springer.

## Explainable AI / SHAP

8. Lundberg, S. M., & Lee, S.-I. (2017). *A Unified Approach to Interpreting Model Predictions*. Advances in Neural Information Processing Systems 30 (NeurIPS).

9. Lundberg, S. M. et al. (2020). *From local explanations to global understanding with explainable AI for trees*. Nature Machine Intelligence, 2, 56–67. https://doi.org/10.1038/s42256-019-0138-9

## Imbalanced Learning and Evaluation

10. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). *SMOTE: Synthetic Minority Over-sampling Technique*. Journal of Artificial Intelligence Research, 16, 321–357. https://doi.org/10.1613/jair.953

11. Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432. https://doi.org/10.1371/journal.pone.0118432

## Tabular Machine Learning Benchmark Context

12. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). *Why do tree-based models still outperform deep learning on typical tabular data?* Advances in Neural Information Processing Systems 35 (NeurIPS).

13. McElfresh, D. et al. (2023). *When Do Neural Nets Outperform Boosted Trees on Tabular Data?* Advances in Neural Information Processing Systems.

## Dataset and Official Tool Documentation

14. UCI Machine Learning Repository. *Bank Marketing Dataset*. University of California, Irvine.

15. Scikit-learn documentation. *Model selection, preprocessing, metrics, RandomizedSearchCV, GridSearchCV and classification utilities*.

16. Optuna documentation. *Hyperparameter optimization framework and samplers*.

17. SHAP documentation. *SHapley Additive exPlanations for machine learning models*.

18. imbalanced-learn documentation. *Tools for classification with imbalanced datasets, including SMOTE and related methods*.

## Research Positioning

The project should not claim that combining hyperparameter optimization with SHAP is, by itself, a novel contribution. Existing work already demonstrates tuning, imbalance handling, and explainability on the Bank Marketing problem.

The proposed research contribution is instead positioned around a controlled empirical comparison of:

**HPO strategy × imbalance treatment × predictive performance × computational efficiency × explanation stability**

The experiments should therefore compare default and optimized models under a fixed evaluation protocol and compute budget, while measuring not only predictive metrics but also runtime/trial efficiency and the stability of SHAP-based explanations.

## Bibliographic Verification Note

Before using these references in a final conference/research-paper submission, verify author lists, volume/issue/pages, publication year, DOI, and publisher metadata against the official publisher or DOI record. This repository intentionally keeps the references focused on sources directly relevant to the proposed methodology and research gap.
