# Literature Review and Research Gap

## 1. Research Domain
The project focuses on machine-learning-based **cybersecurity intrusion detection**, with specific emphasis on class imbalance, hyperparameter optimization and explainability.

## 2. Key Literature Directions

### A. Benchmark IDS datasets
CIC-IDS2017 provides labeled benign and attack network flows and is widely used for IDS evaluation. Its official documentation describes multiple attack scenarios and flow-level CSV data. See Reference 3.

UNSW-NB15 contains normal traffic and nine attack families, with 49 engineered features and more than 2.5 million records in the full dataset. UNSW also provides predefined training and testing files. See Reference 4.

### B. Explainable IDS
Recent work has used SHAP for explainable intrusion detection. A 2025 IEEE conference paper proposed an explainable IIoT intrusion-detection methodology using SHAP and LIME on WUSTL-IIoT-2021. See Reference 5.

A recent IEEE conference publication combines LightGBM, Optuna-based hyperparameter optimization and SHAP on CICIDS2017, showing that **HPO + SHAP + IDS is already an active combination**. Therefore, the project must not claim novelty from this combination alone. See Reference 6.

### C. Imbalance and evaluation
Recent IDS studies continue to emphasize skewed attack distributions and the need for metrics beyond accuracy. A 2026 comparative study using UNSW-NB15 and CIC-IDS2017 reports substantial benign/attack imbalance and evaluates precision, recall, F1, MCC and AUROC. See Reference 9.

### D. Cross-dataset and robustness considerations
Recent work evaluates IDS models across UNSW-NB15 and CIC-IDS2017 rather than relying on a single benchmark, reinforcing the importance of dataset-specific artifacts and generalization. See References 9 and 10.

## 3. Research Gap
The literature establishes that:
- ML-based IDS is well studied.
- Class imbalance is a significant IDS evaluation issue.
- HPO is increasingly used to improve IDS models.
- SHAP/LIME are already used for explainable IDS.
- HPO + SHAP has already appeared in recent IDS research.

Therefore, the project will **not** claim novelty from using Optuna, SHAP, SMOTE or a standard IDS dataset individually.

### Proposed Gap
The project will investigate the controlled interaction of:

**HPO strategy × imbalance treatment × IDS performance × computational efficiency × explanation stability**

The key additional dimension is quantitative **explanation stability** across repeated seeds/folds/samples, studied alongside predictive and computational performance.

## 4. Research Questions
1. Which HPO strategy performs best under a fixed computational budget for imbalanced IDS?
2. How does imbalance treatment affect minority-attack recall and PR-AUC?
3. Does HPO consistently improve performance across attack classes?
4. How does HPO change SHAP feature rankings and local explanations?
5. How stable are explanations across repeated seeds/folds?
6. Is the best predictive model also the most computationally efficient and explanation-stable?

## 5. Dataset Selection Criteria
The final dataset will be selected using:
- class imbalance severity
- number and diversity of attack classes
- dataset size and computational feasibility
- feature quality
- literature usage
- reproducibility and availability
- duplicate/leakage risk
- suitability for tree-based ML and SHAP

Candidates: **CIC-IDS2017, CSE-CIC-IDS2018, UNSW-NB15, TON_IoT and CIC-DDoS2019**.

## 6. Methodological Controls
The test set must remain untouched during HPO. Preprocessing and resampling must occur inside training folds where applicable. Search budgets, seeds, primary objective and explanation-stability procedure will be fixed before the main experiment.

## 7. Expected Contribution
An empirical, reproducible framework that demonstrates how optimization and imbalance handling influence not only IDS predictive performance but also computational cost and the stability of explanations.

## 8. References Used for This Review
1. Sharafaldin et al. (2018), CIC-IDS2017 dataset paper.
2. Moustafa & Slay (2015), UNSW-NB15 dataset paper.
3. Official CIC-IDS2017 dataset documentation.
4. Official UNSW-NB15 dataset documentation.
5. 2025 IEEE ICHORA paper on SHAP/LIME-based explainable IIoT intrusion detection, DOI: 10.1109/ICHORA65333.2025.11017105.
6. 2025 IEEE AECE paper on explainable/privacy-preserving multi-class IDS using LightGBM, Optuna and SHAP, DOI: 10.1109/AECE67531.2025.11386640.
7. Lundberg & Lee (2017), SHAP.
8. Akiba et al. (2019), Optuna.
9. 2026 Electronics paper comparing IDS approaches on UNSW-NB15 and CIC-IDS2017, DOI: 10.3390/electronics15081603.
10. 2026 Electronics paper using UNSW-NB15 and CIC-IDS2017 for network IDS evaluation, DOI: 10.3390/electronics15081737.
