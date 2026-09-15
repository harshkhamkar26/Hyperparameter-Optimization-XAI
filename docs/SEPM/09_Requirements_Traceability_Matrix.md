# Requirements Traceability Matrix

| Requirement | Design Component | Test |
|---|---|---|
| FR-01 Dataset loading | Dataset Manager | TC01 |
| FR-02 Data validation | Validation Layer | TC02-TC04 |
| FR-03 Leakage-safe preprocessing | Preprocessing Layer | TC07 |
| FR-04 Reproducible splitting | Validation Layer | TC06 |
| FR-05 Imbalance analysis | Imbalance Layer | TC05 |
| FR-06 Baseline IDS | Model Layer | TC08 |
| FR-07 HPO search spaces | HPO Layer | TC11-TC13 |
| FR-08 HPO comparison | HPO Layer | TC11-TC14 |
| FR-09 Imbalance treatments | Imbalance Layer | TC09-TC10 |
| FR-10 Performance evaluation | Evaluation Layer | TC15 |
| FR-11 Trial logging | Experiment Logger | TC11-TC14 |
| FR-12 SHAP explanations | XAI Layer | TC16-TC17 |
| FR-13 Explanation comparison | XAI Layer | TC16-TC17 |
| FR-14 Explanation stability | Stability Layer | TC18 |
| FR-15 Reproducibility | Experiment Logger | TC19 |
| FR-16 Reporting | Reporting Layer | TC20 |

## Traceability Rule
Every research conclusion must be traceable to a defined experiment, metric, configuration and test result.
