
"""
Model evaluation utilities for binary imbalanced classification.
"""

import numpy as np
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix
)


def calculate_metrics(
    y_true,
    y_prediction,
    y_probability=None
):
    """
    Calculate classification metrics.
    """
    
    results = {
        "Accuracy": accuracy_score(
            y_true,
            y_prediction
        ),
        
        "Precision": precision_score(
            y_true,
            y_prediction,
            zero_division=0
        ),
        
        "Recall": recall_score(
            y_true,
            y_prediction,
            zero_division=0
        ),
        
        "F1": f1_score(
            y_true,
            y_prediction,
            zero_division=0
        ),
        
        "Balanced_Accuracy":
            balanced_accuracy_score(
                y_true,
                y_prediction
            )
    }
    
    if y_probability is not None:
        
        results["ROC_AUC"] = (
            roc_auc_score(
                y_true,
                y_probability
            )
        )
        
        results["PR_AUC"] = (
            average_precision_score(
                y_true,
                y_probability
            )
        )
    
    return results


def calculate_threshold_metrics(
    y_true,
    y_probability,
    threshold
):
    """Calculate metrics at a specific threshold."""
    
    y_prediction = (
        y_probability >= threshold
    ).astype(int)
    
    metrics = calculate_metrics(
        y_true,
        y_prediction,
        y_probability
    )
    
    metrics["Threshold"] = threshold
    
    return metrics


def evaluate_threshold_range(
    y_true,
    y_probability,
    thresholds=None
):
    """Evaluate a range of classification thresholds."""
    
    if thresholds is None:
        thresholds = np.round(
            np.arange(
                0.10,
                0.91,
                0.01
            ),
            2
        )
    
    results = []
    
    for threshold in thresholds:
        
        metrics = calculate_threshold_metrics(
            y_true,
            y_probability,
            threshold
        )
        
        results.append(metrics)
    
    return pd.DataFrame(results)


def get_confusion_matrix(
    y_true,
    y_prediction
):
    """Return confusion matrix."""
    
    return confusion_matrix(
        y_true,
        y_prediction
    )


def compare_thresholds(
    y_true,
    y_probability,
    default_threshold=0.50,
    optimized_threshold=0.22
):
    """Compare default and optimized thresholds."""
    
    default_metrics = calculate_threshold_metrics(
        y_true,
        y_probability,
        default_threshold
    )
    
    optimized_metrics = calculate_threshold_metrics(
        y_true,
        y_probability,
        optimized_threshold
    )
    
    default_metrics["Threshold_Type"] = (
        "Default 0.50"
    )
    
    optimized_metrics["Threshold_Type"] = (
        "F1 Optimized"
    )
    
    return pd.DataFrame([
        default_metrics,
        optimized_metrics
    ])
