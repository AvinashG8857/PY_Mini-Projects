import pandas as pd

from app.features import add_target_column, build_features

def test_add_target_column():
    df = pd.DataFrame({
        "Close": [100, 101, 102, 103]
    })

    result = add_target_column(df, target_column="Close", forecast_horizon=1)

    assert result["Target"].iloc[0] == 101
    assert result["Target"].iloc[1] == 102

def test_build_features_returns_dataframe():
    data = {
        "Date": pd.date_range(start="2022-01-01", periods=100),
        "Open": range(100, 200),
        "High": range(101, 201),
        "Low": range(99, 199),
        "Close": range(100, 200),
        "Volume": [1000] * 100
    }

    df = pd.DataFrame(data)
    result = build_features(df)

    assert not result.empty
    assert "Target" in result.columns