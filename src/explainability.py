"""Explainable AI utilities using SHAP."""


def create_explainer(model, X_background):
    """Create a SHAP TreeExplainer for tree-based models."""
    import shap
    return shap.TreeExplainer(model, X_background)


def get_shap_values(explainer, X):
    """Calculate SHAP values for a dataset."""
    return explainer(X)
