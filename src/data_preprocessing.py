"""Data loading and preprocessing utilities."""


def load_data(path):
    """Load a CSV dataset into a pandas DataFrame."""
    import pandas as pd
    return pd.read_csv(path)


def split_features_target(df, target_column):
    """Separate predictors from the target column."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y
