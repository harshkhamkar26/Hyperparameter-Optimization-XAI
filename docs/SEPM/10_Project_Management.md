# Project Management

## 1. Team Responsibilities

| Role | Responsibility |
|---|---|
| Project Lead / Student | Overall research direction, integration and documentation |
| Data/ML Responsibility | Dataset validation, preprocessing and baseline models |
| HPO Responsibility | Search-space design, optimization experiments and efficiency analysis |
| XAI Responsibility | SHAP analysis and explanation-stability study |
| QA/Documentation | Testing, traceability, SEPM artifacts and reproducibility records |
| Project Guide | Review, feedback and academic approval |

For a single-student project, these are responsibility areas rather than separate people.

## 2. Change Management
Any change to the dataset, target definition, model family, HPO strategy, optimization objective, imbalance method or XAI method must record:
1. Change description
2. Reason
3. Impact on research questions and requirements
4. Impact on schedule
5. Review/approval
6. Updated SEPM documents

## 3. Configuration Management
GitHub is the authoritative version-control repository for the project documentation. Major methodological decisions should be committed with meaningful messages. Dataset files and generated large artifacts should not be committed unless explicitly required and legally appropriate.

## 4. Experiment Configuration Management
Each experiment should record:
- Dataset version/source
- Train/validation/test strategy
- Random seed
- Preprocessing configuration
- Model and model version
- HPO strategy
- Search space
- Number of trials
- Optimization objective
- Evaluation metrics
- Runtime
- SHAP configuration

## 5. Communication
Progress should be reviewed at milestones with the project guide. Major research decisions and deviations from the approved methodology should be documented rather than communicated only verbally.

## 6. Quality Management
Quality will be maintained through:
- Requirement traceability
- Literature review
- Guide review
- Leakage prevention
- Reproducible experiments
- Controlled HPO budgets
- Consistent evaluation metrics
- XAI sanity/stability checks
- Version control
- Final documentation audit

## 7. Research Integrity
The project will report both improvements and non-improvements. Results will not be selectively presented to support a predetermined conclusion. SHAP outputs will be interpreted as model explanations and not as proof of causality.
