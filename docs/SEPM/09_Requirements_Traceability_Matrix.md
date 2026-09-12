# Requirements Traceability Matrix

| Requirement | Design Component | Test Case(s) | Status |
|---|---|---|---|
| FR-01 Dataset input | Dataset Manager | TC01, TC02 | Planned |
| FR-02 Data validation | Dataset Manager | TC03-TC05 | Planned |
| FR-03 Preprocessing | Preprocessor | TC05, TC07 | Planned |
| FR-04 Stratified split | Preprocessor | TC06 | Planned |
| FR-05 Baseline model | Model Manager | TC08 | Planned |
| FR-06 Search spaces | HPO Engine | TC09 | Planned |
| FR-07 Multiple HPO strategies | HPO Engine | TC09 | Planned |
| FR-08 Best configuration | HPO Engine | TC10 | Planned |
| FR-09 Model evaluation | Evaluation Engine | TC11, TC12 | Planned |
| FR-10 Experiment recording | Reporting / HPO | TC13, TC19 | Planned |
| FR-11 SHAP explanations | XAI Module | TC14, TC15 | Planned |
| FR-12 Explanation comparison | XAI / Stability | TC16 | Planned |
| FR-13 Explanation stability | Stability Module | TC17 | Planned |
| FR-14 Visualizations/reports | Reporting Module | TC19 | Planned |
| FR-15 Reproducibility metadata | Experiment Manager | TC18 | Planned |
| FR-16 Documentation | Documentation / QA | TC20 | Planned |

## Research Objective Traceability

| Research Objective | Evidence | Test/Validation |
|---|---|---|
| Compare HPO strategies | Best objective + runtime + trial count | TC09, TC13 |
| Measure improvement over baseline | Metric comparison | TC11, TC12 |
| Handle class imbalance responsibly | Class distribution + class-sensitive metrics | TC04, TC11 |
| Study explanation changes | SHAP rankings/distributions | TC14-TC16 |
| Study explanation stability | Repeated explanation analysis | TC17, TC18 |
| Ensure reproducibility | Seeds + experiment metadata | TC18 |

This matrix should be updated from **Planned** to **Implemented/Tested** as implementation progresses.
