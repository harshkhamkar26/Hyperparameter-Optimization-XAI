
"""
Preprocessing utilities for the Explainable HPO
Imbalanced Tabular Classification project.
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline


def load_bank_marketing_data(
    data_path="../data/raw/bank-full.csv"
):
    """Load the UCI Bank Marketing dataset."""
    
    df = pd.read_csv(data_path)
    
    return df


def prepare_target(
    df,
    target_column="y"
):
    """Separate features and encode target: no=0, yes=1."""
    
    X = df.drop(columns=[target_column]).copy()
    
    y = df[target_column].map({
        "no": 0,
        "yes": 1
    })
    
    if y.isna().any():
        raise ValueError(
            "Target contains unexpected values. "
            "Expected 'no' and 'yes'."
        )
    
    return X, y.astype(int)


def identify_feature_types(X):
    """Identify numerical and categorical columns."""
    
    numeric_columns = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()
    
    categorical_columns = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()
    
    return numeric_columns, categorical_columns


def build_preprocessor(
    numeric_columns,
    categorical_columns
):
    """Build leakage-safe preprocessing transformer."""
    
    numeric_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler())
        ]
    )
    
    categorical_pipeline = Pipeline(
        steps=[
            (
                "onehot",
                OneHotEncoder(
                    handle_unknown="ignore"
                )
            )
        ]
    )
    
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                numeric_columns
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            )
        ],
        remainder="drop"
    )
    
    return preprocessor


def prepare_preprocessing(
    df,
    target_column="y"
):
    """Prepare X, y and preprocessing transformer."""
    
    X, y = prepare_target(
        df,
        target_column
    )
    
    numeric_columns, categorical_columns = (
        identify_feature_types(X)
    )
    
    preprocessor = build_preprocessor(
        numeric_columns,
        categorical_columns
    )
    
    return (
        X,
        y,
        preprocessor,
        numeric_columns,
        categorical_columns
    )


def get_transformed_feature_names(
    fitted_preprocessor
):
    """Return transformed feature names."""
    
    return (
        fitted_preprocessor
        .get_feature_names_out()
        .tolist()
    )
