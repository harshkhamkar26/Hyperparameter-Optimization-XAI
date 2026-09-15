# Requirements Traceability Matrix

| Requirement | Design Component | Test |
|---|---|---|
| FR-01 Bank Marketing dataset loading | Dataset Manager | TC01 |
| FR-02 Data validation | Validation Layer | TC02-TC04 |
| FR-03 Leakage-safe preprocessing | Preprocessing Layer | TC08 |
| FR-04 Reproducible splitting | Validation Layer | TC06 |
| FR-05 Imbalance analysis | Imbalance Layer | TC05 |
| FR-06 Baseline classifier | Model Layer | TC09 |
| FR-07 HPO search spaces | HPO Layer | TC12-TC14 |
| FR-08 HPO comparison | HPO Layer | TC12-TC15 |
| FR-09 Imbalance treatments | Imbalance Layer | TC10-TC11 |
| FR-10 Performance evaluation | Evaluation Layer | TC16 |
| FR-11 Trial logging | Experiment Logger | TC12-TC15 |
| FR-12 SHAP explanations | XAI Layer | TC17-TC18 |
| FR-13 Explanation comparison | XAI Layer | TC17-TC18 |
| FR-14 Explanation stability | Stability Layer | TC19 |
| FR-15 Reproducibility | Experiment Logger | TC20 |
| FR-16 Reporting | Reporting Layer | TC21 |

## Additional Control
Prediction-time feature policy is tested by TC07 to prevent the research from using information that would not be available when a marketing decision is made.

## Traceability Rule
Every research conclusion must be traceable to a defined experiment, metric, configuration and test result.
