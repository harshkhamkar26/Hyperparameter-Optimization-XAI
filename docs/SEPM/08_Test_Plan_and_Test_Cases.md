# Test Plan and Test Cases

## Test Objective
Verify correctness, reproducibility, leakage safety and research validity of the Bank Marketing HPO/XAI framework.

| ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Load UCI Bank Marketing dataset | Dataset loads successfully |
| TC02 | Validate required columns/target | Schema and target `y` are valid |
| TC03 | Check missing/unknown values | Issues are identified and handled |
| TC04 | Check duplicate records | Duplicates are quantified/handled |
| TC05 | Analyze target distribution | Class imbalance is reported |
| TC06 | Split train/validation/test | Stratified splits follow protocol |
| TC07 | Check prediction-time feature policy | Features unavailable at prediction time are excluded/controlled |
| TC08 | Check preprocessing leakage | Test information is not used in fitting |
| TC09 | Train Random Forest, XGBoost and CatBoost baselines | Baseline metrics are produced for each model |
| TC09A | Validate model configuration | Only the predefined core model set is used: Random Forest, XGBoost, CatBoost |
| TC10 | Apply class weighting | Model trains and results are logged |
| TC11 | Apply SMOTE/valid resampling | Resampling occurs only on training folds |
| TC12 | Run Grid Search | Trials and best parameters are recorded |
| TC13 | Run Random Search | Trials and best parameters are recorded |
| TC14 | Run Optuna/TPE | Trials, objective and runtime are recorded |
| TC15 | Validate HPO budget | Trial/time budget is respected |
| TC16 | Evaluate optimized model | Class-sensitive metrics are generated |
| TC17 | Generate SHAP global explanation | Feature importance summary is produced |
| TC18 | Generate SHAP local explanation | Individual prediction is explained |
| TC19 | Measure explanation stability | Stability statistic is produced |
| TC20 | Repeat experiment with fixed seed | Results are reproducible within tolerance |
| TC21 | Export research results | Tables/plots/logs are complete |

## Acceptance
All critical data, leakage, HPO, evaluation and XAI tests must pass before final conclusions are reported.
