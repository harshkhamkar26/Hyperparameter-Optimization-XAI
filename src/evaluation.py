"""Model evaluation utilities."""

from sklearn.metrics import accuracy_score, classification_report, mean_absolute_error, mean_squared_error, r2_score


def classification_metrics(y_true, y_pred):
    """Return common classification metrics."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "classification_report": classification_report(y_true, y_pred, output_dict=True),
    }


def regression_metrics(y_true, y_pred):
    """Return common regression metrics."""
    mse = mean_squared_error(y_true, y_pred)
    return {
        "mae": mean_absolute_error(y_true, y_pred),
        "mse": mse,
        "rmse": mse ** 0.5,
        "r2": r2_score(y_true, y_pred),
    }
