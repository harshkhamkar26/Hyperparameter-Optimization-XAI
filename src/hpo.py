
"""
Hyperparameter Optimization utilities.

Framework:
Optuna + Stratified K-Fold Cross Validation

Primary optimization metric:
F1 Score

Models:
- Logistic Regression
- Decision Tree
- Random Forest
"""

import optuna
import numpy as np

from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score
)

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def create_cv(
    n_splits=3,
    random_state=42
):
    """Create stratified cross-validation."""
    
    return StratifiedKFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=random_state
    )


def optimize_logistic_regression(
    X,
    y,
    preprocessor,
    n_trials=20,
    random_state=42,
    scoring="f1"
):
    """Optimize Logistic Regression using Optuna."""
    
    cv = create_cv(
        n_splits=3,
        random_state=random_state
    )
    
    def objective(trial):
        
        C = trial.suggest_float(
            "C",
            1e-3,
            10,
            log=True
        )
        
        class_weight = trial.suggest_categorical(
            "class_weight",
            [None, "balanced"]
        )
        
        model = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "classifier",
                    LogisticRegression(
                        C=C,
                        class_weight=class_weight,
                        max_iter=1000,
                        random_state=random_state
                    )
                )
            ]
        )
        
        scores = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring=scoring,
            n_jobs=-1
        )
        
        return scores.mean()
    
    study = optuna.create_study(
        direction="maximize"
    )
    
    study.optimize(
        objective,
        n_trials=n_trials
    )
    
    return study


def optimize_decision_tree(
    X,
    y,
    preprocessor,
    n_trials=20,
    random_state=42,
    scoring="f1"
):
    """Optimize Decision Tree using Optuna."""
    
    cv = create_cv(
        n_splits=3,
        random_state=random_state
    )
    
    def objective(trial):
        
        max_depth = trial.suggest_int(
            "max_depth",
            3,
            30
        )
        
        min_samples_split = trial.suggest_int(
            "min_samples_split",
            2,
            20
        )
        
        min_samples_leaf = trial.suggest_int(
            "min_samples_leaf",
            1,
            10
        )
        
        max_features = trial.suggest_categorical(
            "max_features",
            [None, "sqrt", "log2"]
        )
        
        criterion = trial.suggest_categorical(
            "criterion",
            ["gini", "entropy", "log_loss"]
        )
        
        class_weight = trial.suggest_categorical(
            "class_weight",
            [None, "balanced"]
        )
        
        model = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "classifier",
                    DecisionTreeClassifier(
                        max_depth=max_depth,
                        min_samples_split=min_samples_split,
                        min_samples_leaf=min_samples_leaf,
                        max_features=max_features,
                        criterion=criterion,
                        class_weight=class_weight,
                        random_state=random_state
                    )
                )
            ]
        )
        
        scores = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring=scoring,
            n_jobs=-1
        )
        
        return scores.mean()
    
    study = optuna.create_study(
        direction="maximize"
    )
    
    study.optimize(
        objective,
        n_trials=n_trials
    )
    
    return study


def optimize_random_forest(
    X,
    y,
    preprocessor,
    n_trials=20,
    random_state=42,
    scoring="f1"
):
    """Optimize Random Forest using Optuna."""
    
    cv = create_cv(
        n_splits=3,
        random_state=random_state
    )
    
    def objective(trial):
        
        n_estimators = trial.suggest_int(
            "n_estimators",
            100,
            500,
            step=50
        )
        
        max_depth = trial.suggest_int(
            "max_depth",
            5,
            30
        )
        
        min_samples_split = trial.suggest_int(
            "min_samples_split",
            2,
            20
        )
        
        min_samples_leaf = trial.suggest_int(
            "min_samples_leaf",
            1,
            10
        )
        
        max_features = trial.suggest_categorical(
            "max_features",
            ["sqrt", "log2", None]
        )
        
        class_weight = trial.suggest_categorical(
            "class_weight",
            [None, "balanced"]
        )
        
        model = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "classifier",
                    RandomForestClassifier(
                        n_estimators=n_estimators,
                        max_depth=max_depth,
                        min_samples_split=min_samples_split,
                        min_samples_leaf=min_samples_leaf,
                        max_features=max_features,
                        class_weight=class_weight,
                        random_state=random_state,
                        n_jobs=-1
                    )
                )
            ]
        )
        
        scores = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring=scoring,
            n_jobs=1
        )
        
        return scores.mean()
    
    study = optuna.create_study(
        direction="maximize"
    )
    
    study.optimize(
        objective,
        n_trials=n_trials
    )
    
    return study


def get_best_parameters(study):
    """Return best parameters from an Optuna study."""
    
    return study.best_params


def get_best_score(study):
    """Return best objective score."""
    
    return study.best_value
