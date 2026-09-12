# Test Plan and Test Cases

## Testing Objectives
- Verify functional requirements.
- Verify data preprocessing behaviour.
- Verify optimization workflow.
- Verify evaluation calculations.
- Verify XAI output generation.
- Verify reproducibility and error handling.

## Test Cases

| ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Load valid dataset | Dataset loads successfully |
| TC02 | Load invalid/missing dataset | Clear error is reported |
| TC03 | Detect missing values | Missing values are identified/handled according to preprocessing rules |
| TC04 | Split features and target | Correct X and y are produced |
| TC05 | Train baseline model | Model trains without unexpected failure |
| TC06 | Run optimization | Optimization completes and records trials |
| TC07 | Retrieve best parameters | Best parameter configuration is returned |
| TC08 | Evaluate baseline model | Required metrics are generated |
| TC09 | Evaluate optimized model | Required metrics are generated |
| TC10 | Generate global XAI explanation | Feature importance/summary explanation is produced |
| TC11 | Generate local XAI explanation | Individual prediction explanation is produced |
| TC12 | Compare models | Baseline and optimized results are clearly compared |
| TC13 | Repeat experiment with same seed | Results are reproducible within expected numerical tolerance |
| TC14 | Verify documentation | Requirements, UML and test records are consistent with implementation |

## Test Levels
- Unit Testing
- Integration Testing
- System Testing
- Regression Testing
- Reproducibility Testing

## Exit Criteria
Testing is complete when all critical test cases pass, unresolved defects are documented, and the final workflow produces valid results.
