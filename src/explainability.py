
"""
Explainable AI utilities using SHAP.

Primary model:
Logistic Regression

Purpose:
- Global feature importance
- Local prediction explanations
- Explanation stability analysis
"""

import numpy as np
import pandas as pd
import shap


def get_transformed_feature_names(
    fitted_pipeline
):
    """Extract transformed feature names from pipeline."""
    
    preprocessor = (
        fitted_pipeline
        .named_steps["preprocessor"]
    )
    
    return (
        preprocessor
        .get_feature_names_out()
        .tolist()
    )


def get_classifier(
    fitted_pipeline
):
    """Extract classifier from fitted pipeline."""
    
    return fitted_pipeline.named_steps[
        "classifier"
    ]


def get_transformed_data(
    fitted_pipeline,
    X
):
    """Transform raw data using fitted preprocessing."""
    
    preprocessor = (
        fitted_pipeline
        .named_steps["preprocessor"]
    )
    
    return preprocessor.transform(X)


def create_logistic_shap_explainer(
    fitted_pipeline,
    X_background
):
    """
    Create SHAP LinearExplainer for
    Logistic Regression.
    """
    
    transformed_background = (
        get_transformed_data(
            fitted_pipeline,
            X_background
        )
    )
    
    classifier = get_classifier(
        fitted_pipeline
    )
    
    explainer = shap.LinearExplainer(
        classifier,
        transformed_background
    )
    
    return explainer


def calculate_shap_values(
    fitted_pipeline,
    X_background,
    X_explain
):
    """
    Calculate SHAP values for Logistic Regression.
    """
    
    explainer = create_logistic_shap_explainer(
        fitted_pipeline,
        X_background
    )
    
    transformed_data = (
        get_transformed_data(
            fitted_pipeline,
            X_explain
        )
    )
    
    shap_values = explainer(
        transformed_data
    )
    
    return shap_values


def calculate_global_shap_importance(
    shap_values,
    feature_names
):
    """
    Calculate mean absolute SHAP importance.
    """
    
    values = shap_values.values
    
    if values.ndim == 3:
        values = values[:, :, 1]
    
    importance = np.abs(values).mean(
        axis=0
    )
    
    result = pd.DataFrame({
        "Feature": feature_names,
        "Mean_Absolute_SHAP": importance
    })
    
    result = (
        result
        .sort_values(
            "Mean_Absolute_SHAP",
            ascending=False
        )
        .reset_index(drop=True)
    )
    
    return result


def create_local_explanation(
    shap_values,
    feature_names,
    sample_index=0
):
    """Create a local SHAP explanation table."""
    
    values = shap_values.values
    
    if values.ndim == 3:
        values = values[:, :, 1]
    
    row = values[sample_index]
    
    explanation = pd.DataFrame({
        "Feature": feature_names,
        "SHAP_Value": row,
        "Absolute_SHAP": np.abs(row)
    })
    
    explanation = (
        explanation
        .sort_values(
            "Absolute_SHAP",
            ascending=False
        )
        .reset_index(drop=True)
    )
    
    return explanation


def calculate_top_feature_overlap(
    importance_tables,
    top_n=10
):
    """
    Calculate Jaccard overlap of top-N
    SHAP features across experiments.
    """
    
    feature_sets = []
    
    for table in importance_tables:
        
        top_features = set(
            table
            .head(top_n)["Feature"]
            .tolist()
        )
        
        feature_sets.append(
            top_features
        )
    
    overlaps = []
    
    for i in range(
        len(feature_sets)
    ):
        
        for j in range(
            i + 1,
            len(feature_sets)
        ):
            
            intersection = (
                feature_sets[i]
                .intersection(
                    feature_sets[j]
                )
            )
            
            union = (
                feature_sets[i]
                .union(
                    feature_sets[j]
                )
            )
            
            jaccard = (
                len(intersection) /
                len(union)
                if union
                else 0
            )
            
            overlaps.append({
                "Experiment_A": i,
                "Experiment_B": j,
                "Jaccard": jaccard
            })
    
    return pd.DataFrame(overlaps)
