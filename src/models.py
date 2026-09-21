
"""
Model construction utilities.

Models used in the research:
- Logistic Regression
- Decision Tree
- Random Forest
"""

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def build_logistic_regression(
    preprocessor,
    C=1.0,
    class_weight=None,
    random_state=42
):
    """Build Logistic Regression pipeline."""
    
    model = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "classifier",
                LogisticRegression(
                    C=C,
                    class_weight=class_weight,
                    max_iter=1000,
                    random_state=random_state
                )
            )
        ]
    )
    
    return model


def build_decision_tree(
    preprocessor,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features=None,
    criterion="gini",
    class_weight=None,
    random_state=42
):
    """Build Decision Tree pipeline."""
    
    model = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "classifier",
                DecisionTreeClassifier(
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    min_samples_leaf=min_samples_leaf,
                    max_features=max_features,
                    criterion=criterion,
                    class_weight=class_weight,
                    random_state=random_state
                )
            )
        ]
    )
    
    return model


def build_random_forest(
    preprocessor,
    n_estimators=100,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features="sqrt",
    class_weight=None,
    random_state=42
):
    """Build Random Forest pipeline."""
    
    model = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    min_samples_leaf=min_samples_leaf,
                    max_features=max_features,
                    class_weight=class_weight,
                    random_state=random_state,
                    n_jobs=-1
                )
            )
        ]
    )
    
    return model


def get_default_models(
    preprocessor,
    random_state=42
):
    """Return the three default research models."""
    
    return {
        "Logistic Regression":
            build_logistic_regression(
                preprocessor,
                random_state=random_state
            ),
        
        "Decision Tree":
            build_decision_tree(
                preprocessor,
                random_state=random_state
            ),
        
        "Random Forest":
            build_random_forest(
                preprocessor,
                random_state=random_state
            )
    }
