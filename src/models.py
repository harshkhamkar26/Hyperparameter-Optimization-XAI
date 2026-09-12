"""Baseline model definitions."""

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


def get_random_forest_classifier(random_state=42):
    """Return a baseline Random Forest classifier."""
    return RandomForestClassifier(random_state=random_state)


def get_random_forest_regressor(random_state=42):
    """Return a baseline Random Forest regressor."""
    return RandomForestRegressor(random_state=random_state)
