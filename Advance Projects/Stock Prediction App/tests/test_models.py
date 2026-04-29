import pandas as pd

from app.models import time_series_split

def test_time_series_split_sizes():
    df = pd.DataFrame({
        "Date": pd.date_range(start="2022-01-01", periods=100),
        "Feature1": range(100),
        "Feature2": range(100, 200),
        "Target": range(200, 300)
    })

    feature_columns = ["Feature1", "Feature2"]

    X_train, X_val, X_test, y_train, y_val, y_test, df_train, df_val, df_test = time_series_split(
        df,
        feature_columns,
        target_column="Target"
    )

    assert len(X_train) > 0
    assert len(X_val) > 0
    assert len(X_test) > 0
    assert len(df_train) + len(df_val) + len(df_test) == len(df)