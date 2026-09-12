# Risk Management

| ID | Risk | Probability | Impact | Mitigation | Contingency |
|---|---|---|---|---|---|
| R1 | Dataset or target unsuitable | Low | High | Validate UCI dataset and target before experiments | Switch to a documented secondary public dataset |
| R2 | Severe class imbalance makes accuracy misleading | High | High | Use stratified splits and F1/recall/PR-AUC | Apply documented class weighting/resampling |
| R3 | HPO takes too long | Medium | High | Bound trials, search spaces and CV folds | Reduce budget or use efficient TPE/pruning |
| R4 | Optimization overfits validation data | Medium | High | Keep an untouched test set and use cross-validation on training data | Repeat with a new seed and verify on hold-out test data |
| R5 | Data leakage during preprocessing | Medium | Critical | Fit transformations only on training folds using pipelines | Re-run experiments with leakage checks |
| R6 | Optimized model does not improve baseline | Medium | Medium | Compare several justified search spaces and report negative results honestly | Reconsider objective/model while preserving the experiment record |
| R7 | SHAP analysis is computationally expensive | Medium | Medium | Use appropriate explainers and controlled samples | Reduce explanation sample size and document it |
| R8 | Explanation instability | Medium | High | Repeat SHAP analysis across samples/folds and quantify stability | Report instability as a research finding |
| R9 | Library incompatibility | Medium | Medium | Pin versions and record environment | Use compatible versions and rerun validation tests |
| R10 | Results are not reproducible | Low | High | Fix seeds, record configs and preserve experiment metadata | Repeat experiment from a clean environment |
| R11 | Literature gap is too weak | Medium | High | Review recent HPO/XAI literature before finalizing methodology | Refine research question without changing the dataset unnecessarily |
| R12 | Documentation becomes inconsistent | Medium | Medium | Update SEPM artifacts at every major decision | Perform final traceability audit |

## Risk Response Strategy
High-impact risks are reviewed at each milestone. Any change to dataset, target, optimization objective, model family or evaluation protocol must be recorded in the change-management process before becoming part of the final experiment.
