# System Design and Architecture

## Architecture

```text
+-------------------+
| Public Dataset    |
+---------+---------+
          |
          v
+-------------------+
| Data Preprocessing|
+---------+---------+
          |
          v
+-------------------+
| Baseline Model    |
+---------+---------+
          |
          v
+-------------------+
| Hyperparameter    |
| Optimization      |
+---------+---------+
          |
          v
+-------------------+
| Optimized Model   |
+----+----------+---+
     |          |
     v          v
+---------+  +---------+
|Evaluation| | XAI     |
+----+----+  +----+----+
     |            |
     +------+-----+
            v
      +-----------+
      | Reports   |
      | & Charts  |
      +-----------+
```

## Main Components

1. **Dataset Manager:** obtains and validates the selected public dataset.
2. **Preprocessing Module:** handles cleaning, encoding, missing values and feature preparation.
3. **Model Module:** trains the selected baseline ML model.
4. **Optimization Module:** defines and searches the hyperparameter space.
5. **Evaluation Module:** calculates appropriate performance metrics.
6. **XAI Module:** generates feature importance and prediction explanations.
7. **Reporting Module:** organizes metrics, visualizations and conclusions.

## Design Principles
- Separation of concerns
- Reproducibility
- Modular implementation
- Testability
- Traceability from requirements to results
