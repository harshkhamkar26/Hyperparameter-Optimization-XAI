# System Design and Architecture

## 1. System Context
The system is an experimental ML research workflow for binary prediction on the UCI Bank Marketing dataset. It compares baseline and optimized classifiers while measuring predictive performance, optimization efficiency and explainability.

## 2. Architecture

```text
+---------------------------+
| UCI Bank Marketing Data   |
| Target: y = yes / no      |
+-------------+-------------+
              |
              v
+---------------------------+
| Data Validation            |
| Schema / quality / target  |
+-------------+-------------+
              |
              v
+---------------------------+
| Preprocessing Pipeline     |
| Encoding / scaling / split |
+-------------+-------------+
              |
              v
+---------------------------+
| Class Imbalance Analysis   |
+-------------+-------------+
              |
        +-----+-----+
        |           |
        v           v
+---------------+  +-------------------+
| Baseline      |  | HPO Engine        |
| Classifier    |  | Grid/Random/TPE   |
+-------+-------+  +---------+---------+
        |                    |
        |          +---------v---------+
        |          | Optimized Model   |
        |          +---------+---------+
        |                    |
        +----------+---------+
                   v
        +-----------------------+
        | Evaluation Engine    |
        | F1 Recall Precision   |
        | ROC-AUC PR-AUC etc.   |
        +-----------+-----------+
                    |
          +---------+---------+
          |                   |
          v                   v
+----------------+   +--------------------+
| HPO Efficiency |   | SHAP XAI           |
| trials / time  |   | global / local     |
+--------+-------+   +---------+----------+
         |                     |
         +----------+----------+
                    v
        +-----------------------+
        | Explanation Stability |
        | ranking / consistency |
        +-----------+-----------+
                    v
        +-----------------------+
        | Reports & Research    |
        | comparison / findings |
        +-----------------------+
```

## 3. Main Components

1. **Dataset Manager:** loads and validates the public dataset.
2. **Preprocessing Module:** performs leakage-safe feature preparation.
3. **Imbalance Module:** measures class distribution and applies approved strategies only on training data when required.
4. **Baseline Model Module:** trains reference models.
5. **HPO Module:** executes defined search strategies and records trials.
6. **Evaluation Module:** computes predictive and efficiency metrics.
7. **XAI Module:** generates SHAP global and local explanations.
8. **Stability Module:** compares explanation consistency across repeated samples/folds.
9. **Reporting Module:** produces tables, plots and conclusions.

## 4. Design Principles
- Separation of concerns
- Leakage prevention
- Reproducibility
- Modular experimentation
- Controlled computational budget
- Requirement traceability
- Transparent reporting of positive and negative results
