"""Hyperparameter optimization utilities."""

import optuna
from sklearn.model_selection import cross_val_score


def optimize_model(objective, n_trials=20, seed=42):
    """Run an Optuna study using a user-defined objective function."""
    sampler = optuna.samplers.TPESampler(seed=seed)
    study = optuna.create_study(direction="maximize", sampler=sampler)
    study.optimize(objective, n_trials=n_trials)
    return study


def evaluate_cv(model, X, y, cv=5, scoring="accuracy"):
    """Evaluate a model with cross-validation."""
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    return scores.mean(), scores.std()
