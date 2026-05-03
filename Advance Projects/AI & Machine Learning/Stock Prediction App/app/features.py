import pandas as pd

from config import config
from logger import logger

def add_target_column(df: pd.DataFrame, target_column: str = None, forecast_horizon: int = None) -> pd.DataFrame:
    if target_column is None:
        target_column = config.target_column

    if forecast_horizon is None:
        forecast_horizon = config.forecast_horizon

    df = df.copy()
    df["Target"] = df[target_column].shift(-forecast_horizon)
    return df

def add_return_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Return_1D"] = df["Close"].pct_change()
    df["Return_5D"] = df["Close"].pct_change(periods=5)
    df["Return_10D"] = df["Close"].pct_change(periods=10)
    return df

def add_rolling_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    short_w = config.short_window
    medium_w = config.medium_window
    long_w = config.long_window

    df[f"SMA_{short_w}"] = df["Close"].rolling(window=short_w).mean()
    df[f"SMA_{medium_w}"] = df["Close"].rolling(window=medium_w).mean()
    df[f"SMA_{long_w}"] = df["Close"].rolling(window=long_w).mean()

    df[f"Volatility_{short_w}"] = df["Return_1D"].rolling(window=short_w).std()
    df[f"Volatility_{medium_w}"] = df["Return_1D"].rolling(window=medium_w).std()

    df[f"Volume_MA_{short_w}"] = df["Volume"].rolling(window=short_w).mean()
    df[f"Volume_MA_{medium_w}"] = df["Volume"].rolling(window=medium_w).mean()

    return df

def add_lag_features(df: pd.DataFrame, lags: list[int] = None) -> pd.DataFrame:
    if lags is None:
        lags = [1, 2, 3, 5, 10]

    df = df.copy()

    for lag in lags:
        df[f"Close_Lag_{lag}"] = df["Close"].shift(lag)

    return df

def add_price_range_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["High_Low_Spread"] = df["High"] - df["Low"]
    df["Close_Open_Spread"] = df["Close"] - df["Open"]
    df["Range_Pct"] = (df["High"] - df["Low"]) / df["Close"]
    return df

def add_rsi_feature(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    df = df.copy()

    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    df[f"RSI_{period}"] = 100 - (100 / (1 + rs))

    return df

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting feature engineering pipeline")

    df = add_return_features(df)
    df = add_rolling_features(df)
    df = add_lag_features(df)
    df = add_price_range_features(df)
    df = add_rsi_feature(df)
    df = add_target_column(df)

    df = df.dropna().reset_index(drop=True)

    logger.info(f"Feature engineering completed. Final rows: {len(df)}")
    return df

def get_feature_columns(df: pd.DataFrame) -> list[str]:
    excluded_columns = ["Date", "Target"]
    feature_columns = [col for col in df.columns if col not in excluded_columns]
    return feature_columns