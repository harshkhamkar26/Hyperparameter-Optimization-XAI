# UML Diagrams

## 1. Use Case Diagram

```mermaid
flowchart LR
    U[User / Analyst]
    G[Project Guide / Evaluator]
    S((ML Optimization & XAI System))
    A[Upload / Select Dataset]
    B[Preprocess Data]
    C[Train Baseline Model]
    D[Run Hyperparameter Optimization]
    E[Evaluate Model]
    F[Generate XAI Explanation]
    H[View Reports]
    U --> A
    U --> B
    U --> C
    U --> D
    U --> E
    U --> F
    U --> H
    G --> H
```

## 2. Class Diagram

```mermaid
classDiagram
    class DatasetManager {
      +load_dataset()
      +validate_dataset()
    }
    class Preprocessor {
      +clean_data()
      +transform_features()
      +split_data()
    }
    class ModelManager {
      +train_baseline()
      +train_optimized()
    }
    class Optimizer {
      +define_search_space()
      +run_optimization()
      +get_best_parameters()
    }
    class Evaluator {
      +calculate_metrics()
      +compare_models()
    }
    class Explainer {
      +global_explanation()
      +local_explanation()
      +feature_importance()
    }
    DatasetManager --> Preprocessor
    Preprocessor --> ModelManager
    ModelManager --> Optimizer
    Optimizer --> Evaluator
    ModelManager --> Evaluator
    ModelManager --> Explainer
```

## 3. Activity Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Select Dataset]
    B --> C[Validate and Preprocess]
    C --> D[Train Baseline Model]
    D --> E[Evaluate Baseline]
    E --> F[Define Hyperparameter Search Space]
    F --> G[Run Optimization]
    G --> H[Select Best Parameters]
    H --> I[Train Optimized Model]
    I --> J[Evaluate Optimized Model]
    J --> K[Generate SHAP/XAI Explanations]
    K --> L[Compare Results]
    L --> M[Generate Documentation]
    M --> N([End])
```

## 4. Sequence Diagram

```mermaid
sequenceDiagram
    actor User
    participant Data as Dataset Manager
    participant Prep as Preprocessor
    participant Model as Model Manager
    participant Opt as Optimizer
    participant Eval as Evaluator
    participant XAI as Explainer
    User->>Data: Select dataset
    Data->>Prep: Send validated data
    Prep->>Model: Prepared train/test data
    Model->>Eval: Baseline predictions
    Eval-->>Model: Baseline metrics
    Model->>Opt: Request optimization
    Opt->>Model: Candidate parameters
    Model->>Eval: Candidate predictions
    Eval-->>Opt: Validation score
    Opt-->>Model: Best parameters
    Model->>Eval: Optimized predictions
    Eval-->>User: Final metrics
    Model->>XAI: Optimized model + data
    XAI-->>User: Feature and prediction explanations
```

## 5. Component Diagram

```mermaid
flowchart LR
    UI[User / Notebook Interface] --> DATA[Data Component]
    DATA --> PREP[Preprocessing Component]
    PREP --> MODEL[ML Model Component]
    MODEL --> OPT[Optimization Component]
    MODEL --> EVAL[Evaluation Component]
    MODEL --> XAI[XAI Component]
    EVAL --> REPORT[Reporting Component]
    XAI --> REPORT
```

## 6. Deployment Diagram

```mermaid
flowchart TB
    Laptop[Developer Laptop]
    IDE[Python / Jupyter Environment]
    Laptop --> IDE
    IDE --> Pipeline[ML + Optimization + XAI Pipeline]
    Pipeline --> Dataset[Local/Public Dataset]
    Pipeline --> Output[Reports / Charts / Documentation]
    GitHub[GitHub Repository]
    IDE <--> GitHub
```
