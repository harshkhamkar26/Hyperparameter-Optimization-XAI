# Test Plan and Test Cases

## 1. Testing Objectives
- Verify dataset integrity and target definition.
- Verify leakage-safe preprocessing.
- Verify stratified splitting and imbalance handling.
- Verify baseline model training.
- Verify each HPO strategy and trial recording.
- Verify evaluation metrics for the positive class.
- Verify SHAP global/local explanations.
- Verify explanation stability calculations.
- Verify reproducibility and documentation consistency.

## 2. Test Cases

| ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Load valid UCI Bank Marketing data | Dataset loads and expected columns are present |
| TC02 | Missing/corrupt dataset | Clear validation error is generated |
| TC03 | Validate target `y` | Target contains expected binary classes `yes` and `no` |
| TC04 | Check class distribution | Class counts/ratio are reported correctly |
| TC05 | Detect unknown/missing values | Values are identified and handled according to preprocessing rules |
| TC06 | Verify stratified split | Train/validation/test preserve class proportions within tolerance |
| TC07 | Verify leakage-safe preprocessing | Transformers are fitted only on training folds |
| TC08 | Train baseline model | Reference model trains successfully |
| TC09 | Run Grid/Random/TPE search | Valid trials complete and invalid trials are handled |
| TC10 | Retrieve best configuration | Best parameters match the defined optimization objective |
| TC11 | Evaluate baseline | Accuracy, precision, recall, F1, ROC-AUC and confusion matrix are produced |
| TC12 | Evaluate optimized model | Same metrics are produced for fair comparison |
| TC13 | Record HPO efficiency | Trial count and runtime are recorded |
| TC14 | Generate global SHAP | Feature importance/summary explanation is produced |
| TC15 | Generate local SHAP | Individual prediction explanation is produced |
| TC16 | Compare feature rankings | Baseline and optimized rankings can be compared |
| TC17 | Analyze explanation stability | Stability/consistency measure is produced using documented procedure |
| TC18 | Repeat with same seed | Results are reproducible within documented tolerance |
| TC19 | Verify report outputs | Tables/charts match stored experiment results |
| TC20 | Verify traceability | Requirements, design and tests remain consistent |

## 3. Test Levels
- Unit Testing
- Integration Testing
- System Testing
- Regression Testing
- Data Validation Testing
- Experiment/Reproducibility Testing

## 4. Model-Specific Validation
The test plan must ensure that the optimization objective is not evaluated only on accuracy. The positive class (`yes`) must be explicitly assessed using recall, precision and F1. PR-AUC may be used because the target is imbalanced.

## 5. Exit Criteria
Testing is complete when all critical test cases pass, unresolved defects are documented, leakage checks are satisfactory, reproducibility checks are completed and the final experiment produces valid comparative results.
