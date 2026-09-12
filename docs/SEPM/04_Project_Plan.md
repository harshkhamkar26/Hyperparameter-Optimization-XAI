# Project Plan

## 1. Development and Research Phases

| Phase | Activities | Deliverable |
|---|---|---|
| 1. Requirements | Problem definition, stakeholders, scope, FR/NFR | SRS |
| 2. Literature Review | Prior work, dataset research, research gap, research questions | Literature Review |
| 3. Feasibility | Technical, economic, operational, research and ethical analysis | Feasibility Study |
| 4. System Design | Architecture, data flow and UML | Design + UML |
| 5. Dataset Analysis | UCI Bank Marketing validation, target analysis, imbalance study | Dataset specification |
| 6. Preprocessing Design | Encoding, splitting, leakage prevention and imbalance strategy | Preprocessing specification |
| 7. Baseline Experiments | Reference models and baseline metrics | Baseline results |
| 8. HPO Experiments | Grid/Random/TPE search with bounded budgets | Optimization results |
| 9. Explainability | SHAP global/local analysis and stability comparison | XAI results |
| 10. Integrated Evaluation | Performance, efficiency and explanation trade-off analysis | Comparative results |
| 11. Testing | Functional, data, experiment and reproducibility tests | Test report |
| 12. Documentation | Final report, references, limitations and conclusions | Final report |
| 13. Presentation | Demonstration, viva and research presentation | Final presentation |

## 2. Milestones
- **M1:** SRS approved
- **M2:** Literature review and research gap approved
- **M3:** Dataset and binary classification target finalized
- **M4:** UML/design approved
- **M5:** Baseline experiments completed
- **M6:** HPO experiments completed
- **M7:** XAI and explanation-stability analysis completed
- **M8:** Integrated evaluation completed
- **M9:** Testing and reproducibility checks completed
- **M10:** Final report and presentation completed

## 3. Suggested Academic Timeline

| Week | Main Work |
|---|---|
| 1 | Requirements + literature search |
| 2 | Research gap + SRS/proposal revision |
| 3 | Dataset validation + UML/design |
| 4 | Preprocessing + baseline models |
| 5 | HPO strategy implementation |
| 6 | HPO experiments + efficiency analysis |
| 7 | SHAP global/local explanations |
| 8 | Explanation stability + comparative analysis |
| 9 | Testing + reproducibility |
| 10 | Final report + presentation |

## 4. Version Control
GitHub will be used as the authoritative documentation repository. Every major methodological decision should have a meaningful commit. Experimental implementation, when added later, must remain consistent with the approved SEPM documents.

## 5. Dependencies
Literature review and dataset selection must precede final requirements. Dataset validation precedes preprocessing. Baseline experiments precede HPO comparison. Final optimized models precede SHAP comparison.
