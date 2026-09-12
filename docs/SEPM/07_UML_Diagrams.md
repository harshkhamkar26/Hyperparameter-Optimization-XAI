# UML Diagrams

## 1. Use Case Diagram

```mermaid
flowchart LR
    U[Student / Researcher]
    G[Project Guide / Evaluator]
    S((HPO-XAI Research System))
    A[Load Bank Marketing Dataset]
    B[Validate & Preprocess]
    C[Analyze Class Imbalance]
    D[Train Baseline]
    E[Configure HPO]
    F[Run HPO Strategies]
    H[Evaluate Models]
    I[Generate SHAP Explanations]
    J[Analyze Explanation Stability]
    K[Compare Results]
    L[Generate Research Report]
    U --> A
    U --> B
    U --> C
    U --> D
    U --> E
    U --> F
    U --> H
    U --> I
    U --> J
    U --> K
    U --> L
    G --> K
    G --> L
```

## 2. Class Diagram

```mermaid
classDiagram
    class DatasetManager {
      +load_dataset()
      +validate_schema()
      +validate_target()
      +check_class_distribution()
    }
    class Preprocessor {
      +build_pipeline()
      +encode_features()
      +split_stratified()
    }
    class ImbalanceManager {
      +analyze_distribution()
      +apply_training_strategy()
    }
    class ModelManager {
      +train_baseline()
      +train_optimized()
    }
    class Optimizer {
      +define_search_space()
      +run_grid_search()
      +run_random_search()
      +run_tpe_search()
      +get_best_parameters()
    }
    class Evaluator {
      +calculate_metrics()
      +measure_runtime()
      +compare_models()
    }
    class Explainer {
      +global_shap()
      +local_shap()
      +feature_ranking()
    }
    class StabilityAnalyzer {
      +compare_rankings()
      +calculate_consistency()
    }
    class Reporter {
      +save_results()
      +generate_plots()
      +generate_report()
    }
    DatasetManager --> Preprocessor
    Preprocessor --> ImbalanceManager
    ImbalanceManager --> ModelManager
    ModelManager --> Optimizer
    Optimizer --> Evaluator
    ModelManager --> Evaluator
    ModelManager --> Explainer
    Explainer --> StabilityAnalyzer
    Evaluator --> Reporter
    StabilityAnalyzer --> Reporter
```

## 3. Activity Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Load UCI Bank Marketing]
    B --> C[Validate Schema and Target]
    C --> D[Analyze Class Imbalance]
    D --> E[Build Leakage-Safe Preprocessing]
    E --> F[Train Baseline Model]
    F --> G[Evaluate Baseline]
    G --> H[Define HPO Search Spaces]
    H --> I[Run Grid / Random / TPE Search]
    I --> J[Select Best Configuration]
    J --> K[Train Optimized Model]
    K --> L[Evaluate Optimized Model]
    L --> M[Generate SHAP Explanations]
    M --> N[Analyze Explanation Stability]
    N --> O[Compare Performance, Cost and XAI]
    O --> P[Generate Research Report]
    P --> Q([End])
```

## 4. Sequence Diagram

```mermaid
sequenceDiagram
    actor Researcher
    participant Data as Dataset Manager
    participant Prep as Preprocessor
    participant Model as Model Manager
    participant Opt as HPO Engine
    participant Eval as Evaluator
    participant XAI as SHAP Explainer
    participant Stab as Stability Analyzer
    participant Rep as Reporter
    Researcher->>Data: Load Bank Marketing
    Data->>Prep: Validated data
    Prep->>Model: Train/test-ready features
    Model->>Eval: Baseline predictions
    Eval-->>Researcher: Baseline metrics
    Researcher->>Opt: Start HPO strategies
    Opt->>Model: Candidate hyperparameters
    Model->>Eval: Candidate predictions
    Eval-->>Opt: Validation objective
    Opt-->>Model: Best configuration
    Model->>Eval: Optimized predictions
    Eval-->>Rep: Performance + runtime
    Model->>XAI: Model + evaluation samples
    XAI->>Stab: SHAP explanations
    Stab-->>Rep: Stability results
    Rep-->>Researcher: Comparative research report
```

## 5. Component Diagram

```mermaid
flowchart LR
    UI[Notebook / Research Interface] --> DATA[Dataset Component]
    DATA --> PREP[Preprocessing Component]
    PREP --> IMB[Imbalance Component]
    IMB --> MODEL[ML Model Component]
    MODEL --> HPO[HPO Component]
    MODEL --> EVAL[Evaluation Component]
    MODEL --> XAI[XAI Component]
    XAI --> STAB[Stability Component]
    EVAL --> REPORT[Reporting Component]
    STAB --> REPORT
```

## 6. Deployment Diagram

```mermaid
flowchart TB
    Laptop[Student Laptop]
    Python[Python / Jupyter Environment]
    Pipeline[HPO + ML + XAI Pipeline]
    Data[Local Copy of Public Dataset]
    Output[Experiment Results / Charts / Reports]
    GitHub[GitHub SEPM Repository]
    Laptop --> Python
    Python --> Pipeline
    Pipeline --> Data
    Pipeline --> Output
    Python <--> GitHub
```
