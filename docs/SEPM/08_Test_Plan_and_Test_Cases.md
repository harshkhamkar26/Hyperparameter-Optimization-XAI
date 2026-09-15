# Test Plan and Test Cases

## Test Objective
Verify correctness, reproducibility, leakage safety and research validity of the cybersecurity IDS HPO/XAI framework.

| ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Load selected IDS dataset | Dataset loads successfully |
| TC02 | Validate required columns/labels | Schema and target are valid |
| TC03 | Check missing/invalid values | Issues are identified and handled |
| TC04 | Check duplicate records | Duplicates are quantified/handled |
| TC05 | Analyze class distribution | Class imbalance is reported |
| TC06 | Split train/validation/test | Splits follow predefined protocol |
| TC07 | Check preprocessing leakage | Test information is not used in fitting |
| TC08 | Train baseline model | Baseline metrics are produced |
| TC09 | Apply class weighting | Model trains and results are logged |
| TC10 | Apply SMOTE/valid resampling | Resampling occurs only on training folds |
| TC11 | Run Grid Search | Trials and best parameters are recorded |
| TC12 | Run Random Search | Trials and best parameters are recorded |
| TC13 | Run Optuna/TPE | Trials, objective and runtime are recorded |
| TC14 | Validate HPO budget | Trial/time budget is respected |
| TC15 | Evaluate optimized model | Class-sensitive metrics are generated |
| TC16 | Generate SHAP global explanation | Feature importance summary is produced |
| TC17 | Generate SHAP local explanation | Individual prediction is explained |
| TC18 | Measure explanation stability | Stability statistic is produced |
| TC19 | Repeat experiment with fixed seed | Results are reproducible within tolerance |
| TC20 | Export research results | Tables/plots/logs are complete |

## Acceptance
All critical data, leakage, HPO, evaluation and XAI tests must pass before final conclusions are reported.
