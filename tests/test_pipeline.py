"""Basic tests for the project starter package."""

import pandas as pd

from src.data_preprocessing import split_features_target


def test_split_features_target():
    df = pd.DataFrame({"feature": [1, 2, 3], "target": [0, 1, 0]})
    X, y = split_features_target(df, "target")
    assert list(X.columns) == ["feature"]
    assert y.tolist() == [0, 1, 0]
