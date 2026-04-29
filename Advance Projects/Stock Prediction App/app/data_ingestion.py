import pandas as pd
import yfinance as yf

from config import config
from logger import logger

def normalize_indian_ticker(ticker: str) -> str:
    ticker = ticker.strip().upper()

    if ticker.endswith(".NS") or ticker.endswith(".BO"):
        return ticker

    return f"{ticker}.NS"

def validate_stock_data(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Downloaded stock data is empty. Check ticker or date range.")

    required_columns = ["Open", "High", "Low", "Close", "Volume"]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

def download_stock_data(ticker: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    if start_date is None:
        start_date = config.default_start_date

    if end_date is None:
        end_date = config.default_end_date

    normalized_ticker = normalize_indian_ticker(ticker)

    logger.info(
        f"Downloading data for ticker={normalized_ticker}, start={start_date}, end={end_date}"
    )

    try:
        df = yf.download(
            normalized_ticker,
            start=start_date,
            end=end_date,
            progress=False,
            auto_adjust=False
        )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df.index.name = "Date"
        df = df.reset_index()
        df = df.dropna(subset=["Open", "High", "Low", "Close", "Volume"])

        validate_stock_data(df)

        logger.info(f"Downloaded {len(df)} rows for {normalized_ticker}")
        return df

    except Exception as error:
        logger.error(f"Failed to download stock data for {normalized_ticker}: {error}")
        raise