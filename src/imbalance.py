
"""
Imbalance-handling utilities.

Strategies:
1. Original imbalanced data
2. Class weighting
3. SMOTENC
"""

import numpy as np

from imblearn.over_sampling import SMOTENC


def calculate_class_distribution(y):
    """Return class counts and percentages."""
    
    counts = y.value_counts().sort_index()
    
    percentages = (
        counts / len(y) * 100
    )
    
    return counts, percentages


def calculate_imbalance_ratio(y):
    """Calculate majority/minority class ratio."""
    
    counts = y.value_counts()
    
    if len(counts) != 2:
        raise ValueError(
            "This function requires a binary target."
        )
    
    return (
        counts.max() /
        counts.min()
    )


def get_class_weights(y):
    """
    Calculate balanced class weights.
    
    Returns:
        Dictionary suitable for sklearn class_weight.
    """
    
    counts = y.value_counts()
    
    total = len(y)
    n_classes = len(counts)
    
    weights = {}
    
    for class_value, count in counts.items():
        weights[class_value] = (
            total /
            (n_classes * count)
        )
    
    return weights


def apply_smotenc(
    X_train,
    y_train,
    categorical_columns,
    random_state=42
):
    """
    Apply SMOTENC to training data only.
    
    Important:
    SMOTENC must never be applied to the
    untouched test set.
    """
    
    categorical_indices = [
        X_train.columns.get_loc(column)
        for column in categorical_columns
    ]
    
    smotenc = SMOTENC(
        categorical_features=categorical_indices,
        random_state=random_state
    )
    
    X_resampled, y_resampled = (
        smotenc.fit_resample(
            X_train,
            y_train
        )
    )
    
    return (
        X_resampled,
        y_resampled,
        smotenc
    )


def get_resampled_distribution(y):
    """Return distribution after resampling."""
    
    counts = y.value_counts().sort_index()
    
    percentages = (
        counts / len(y) * 100
    )
    
    return counts, percentages
