# Risk Management

| Risk | Impact | Mitigation |
|---|---|---|
| Dataset too large | High | Benchmark subset/resource-aware protocol; document sampling |
| Severe class imbalance | High | Stratified evaluation; class weights/SMOTE variants where valid; PR-AUC and per-class metrics |
| Data leakage/duplicates | Critical | Dataset audit, duplicate checks, leakage-safe splitting and preprocessing |
| Dataset artifacts | High | Literature review and cautious interpretation; document limitations |
| HPO runtime | High | Fixed trial budget, pruning and resource limits |
| Overfitting to validation | High | Untouched test set and repeated validation |
| No improvement from HPO | Medium | Report negative findings rather than tuning until desired results |
| SHAP computational cost | Medium | Controlled background/sample size and documented settings |
| Explanation instability | High | Measure stability across seeds/folds/samples |
| Library incompatibility | Medium | Pin versions and record environment |
| Weak research gap | High | Complete domain-specific literature review before implementation |
| Reproducibility failure | High | Fixed seeds, configs, splits, search spaces and experiment logs |
| Documentation drift | Medium | Update SEPM artifacts whenever methodology changes |
| Security/privacy issue | Critical | Use public/authorized datasets and never commit secrets |

## Risk Priority
Critical risks are leakage, inappropriate dataset use and reproducibility failures. High risks are imbalance, dataset artifacts, HPO overfitting/runtime and explanation instability.
