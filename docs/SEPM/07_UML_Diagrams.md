# UML Diagrams

## System
**An Explainable Hyperparameter Optimization Framework for Imbalanced Cybersecurity Intrusion Detection**

## 1. Use Case Diagram

```mermaid
flowchart LR
    Analyst[Security / ML Analyst]
    System[IDS Research Framework]
    Analyst -->|Select dataset| System
    Analyst -->|Configure experiments| System
    Analyst -->|Run baseline| System
    Analyst -->|Run HPO| System
    Analyst -->|Evaluate models| System
    Analyst -->|Generate SHAP| System
    Analyst -->|Run stability analysis| System
    Analyst -->|View results| System
```

## 2. Activity Diagram

```mermaid
flowchart TD
A[Load IDS Dataset] --> B[Validate and Audit]
B --> C[Split Data]
C --> D[Preprocess]
D --> E[Analyze Imbalance]
E --> F[Train Baseline]
F --> G[Apply HPO / Imbalance Strategy]
G --> H[Evaluate]
H --> I[Generate SHAP]
I --> J[Measure Explanation Stability]
J --> K[Compare Results]
K --> L[Research Report]
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
A->>D: Load and validate dataset
D->>M: Prepared training data
M->>O: Baseline/model configuration
O->>M: Trial parameters
M->>O: Validation metrics
O->>X: Best models
X->>R: SHAP + stability results
R->>A: Comparative report
```

## 4. Component View

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
 ├── Dataset Storage
 ├── Experiment Logs
 └── GitHub Documentation
```

Dataset-specific labels and model names will be finalized after dataset selection.
