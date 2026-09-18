# UML Diagrams

## System
**Explainable Hyperparameter Optimization for Imbalanced Tabular Classification — Bank Marketing**

## 1. Use Case Diagram

```mermaid
flowchart LR
    Analyst[Marketing / ML Analyst]
    System[Bank Marketing Research Framework]
    Analyst -->|Load UCI dataset| System
    Analyst -->|Configure experiments| System
    Analyst -->|Run baseline| System
    Analyst -->|Run HPO| System
    Analyst -->|Apply imbalance strategy| System
    Analyst -->|Evaluate models| System
    Analyst -->|Generate SHAP| System
    Analyst -->|Run stability analysis| System
    Analyst -->|View results| System
```

## 2. Activity Diagram

```mermaid
flowchart TD
A[Load Bank Marketing Dataset] --> B[Validate and Audit]
B --> C[Apply Prediction-time Feature Policy]
C --> D[Split Data]
D --> E[Preprocess]
E --> F[Analyze Imbalance]
F --> G[Train Baseline]
G --> H[Apply HPO / Imbalance Strategy]
H --> I[Evaluate]
I --> J[Generate SHAP]
J --> K[Measure Explanation Stability]
K --> L[Compare Results]
L --> M[Research Report]
```

## 3. Sequence Diagram

```mermaid
sequenceDiagram
participant A as Analyst
participant D as Data Module
participant M as Model Module
participant O as HPO Module
participant X as XAI Module
participant R as Report Module
A->>D: Load and validate Bank Marketing data
D->>M: Prepared training data
M->>O: Baseline/model configuration
O->>M: Trial parameters
M->>O: Validation metrics
O->>X: Best models
X->>R: SHAP + stability results
R->>A: Comparative report
```

## 4. Model Scope

```text
Marketing / Banking Marketing Analytics
              ↓
       UCI Bank Marketing
              ↓
   ┌──────────┼──────────┐
   │          │          │
Random Forest XGBoost  CatBoost
   └──────────┼──────────┘
              ↓
       HPO + Imbalance
              ↓
          SHAP / XAI
              ↓
     Explanation Stability
```

## 5. Component View

```text
[Dataset Manager] → [Preprocessing] → [Imbalance Handler]
                                      ↓
[Experiment Config] → [Baseline/Model] → [HPO Engine]
                                      ↓
                              [Evaluation Engine]
                                      ↓
                                [SHAP Engine]
                                      ↓
                           [Stability Analyzer]
                                      ↓
                              [Report Generator]
```

## 5. Deployment View

```text
Student Workstation
 ├── Python/Jupyter
 ├── ML + HPO Libraries
 ├── UCI Bank Marketing Dataset
 ├── Experiment Logs
 └── GitHub Documentation
```
