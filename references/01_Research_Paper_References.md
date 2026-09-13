# Research Paper References

This file is the compact reference list for the project **Explainable Hyperparameter Optimization for Imbalanced Tabular Classification**.

1. Moro, S., Cortez, P., & Rita, P. (2014). *A data-driven approach to predict the success of bank telemarketing*. Decision Support Systems, 62, 22–31. https://doi.org/10.1016/j.dss.2014.03.001

2. Nasir, M. et al. (2026). *Marketing analytics in banking 4.0: A two-stage explainable AI framework for high-accuracy and well-calibrated predictions*. PLOS ONE. https://doi.org/10.1371/journal.pone.0348767

3. Wang, Y. et al. (2026). *Using ensemble learning and explainable AI to predict bank marketing customer subscription*. Scientific Reports. https://doi.org/10.1038/s41598-026-58149-y

4. Abidin, Z. et al. (2025). *Improving Term Deposit Customer Prediction Using Support Vector Machine with SMOTE and Hyperparameter Tuning in Bank Marketing Campaigns*. Jurnal Teknik Informatika, 6(3). https://doi.org/10.52436/1.jutif.2025.6.3.4585

5. Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). *Optuna: A Next-generation Hyperparameter Optimization Framework*. KDD. https://doi.org/10.1145/3292500.3330701

6. Bergstra, J., & Bengio, Y. (2012). *Random Search for Hyper-Parameter Optimization*. Journal of Machine Learning Research, 13, 281–305.

7. Lundberg, S. M., & Lee, S.-I. (2017). *A Unified Approach to Interpreting Model Predictions*. NeurIPS 30.

8. Lundberg, S. M. et al. (2020). *From local explanations to global understanding with explainable AI for trees*. Nature Machine Intelligence, 2, 56–67. https://doi.org/10.1038/s42256-019-0138-9

9. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). *SMOTE: Synthetic Minority Over-sampling Technique*. Journal of Artificial Intelligence Research, 16, 321–357. https://doi.org/10.1613/jair.953

10. Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432. https://doi.org/10.1371/journal.pone.0118432

11. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). *Why do tree-based models still outperform deep learning on typical tabular data?* NeurIPS 35.

12. UCI Machine Learning Repository. *Bank Marketing Dataset*. University of California, Irvine.

## Research Gap Used in This Project

Existing studies cover combinations of Bank Marketing prediction, hyperparameter tuning, imbalance handling, and explainable AI. Therefore, the project does not claim simple “HPO + SHAP” as novelty.

The research instead investigates the interaction between:

**HPO strategy × imbalance treatment × predictive performance × computational efficiency × explanation stability**

The final experimental study should compare default and optimized configurations using a fixed, leakage-safe evaluation protocol and compute budget.
