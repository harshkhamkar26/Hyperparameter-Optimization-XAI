# Risk Management

| Risk | Impact | Mitigation |
|---|---|---|
| Historical dataset may not represent current campaigns | High | State scope clearly and avoid deployment/generalization claims |
| Class imbalance | High | Class-sensitive metrics, class weights/SMOTE where valid, PR-AUC |
| Data leakage | Critical | Audit features, define prediction-time policy, leakage-safe splitting/preprocessing |
| Post-contact variables create unrealistic prediction | Critical | Treat variables such as call duration according to a pre-defined prediction-time protocol |
| HPO runtime | High | Fixed trial budget, pruning and resource limits |
| Overfitting to validation | High | Untouched test set and repeated validation |
| No improvement from HPO | Medium | Report negative findings rather than tuning until desired results |
| SHAP computational cost | Medium | Controlled background/sample size and documented settings |
| Explanation instability | High | Measure stability across seeds/folds/samples |
| SMOTE changes data distribution | Medium | Apply only inside training folds and compare against class weighting |
| Library incompatibility | Medium | Pin versions and record environment |
| Weak research gap | High | Domain-specific literature review before implementation |
| Reproducibility failure | High | Fixed seeds, configs, splits, search spaces and experiment logs |
| Documentation drift | Medium | Update SEPM artifacts whenever methodology changes |
| Data/privacy issue | Critical | Use the public benchmark and never commit private customer data or secrets |

## Risk Priority
Critical risks are leakage, inappropriate feature timing and reproducibility failures. High risks are class imbalance, HPO runtime/overfitting and explanation instability.
