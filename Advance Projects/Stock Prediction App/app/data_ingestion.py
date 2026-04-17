import yfinance as yf 
import pandas as pd 
from app.config import config
from app.logger import logger

def normalize_indian_ticke(ticker:str) -> str:
    ticker= ticker.strip().upper()

    if ticker.endswith(".NS") or ticker.endswith(".BO"):
        return ticker
    
    return f"{ticker}.NS"


def validate_stock_data(df:pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Download a stock data is empty. Check ticker or date  range.")
    
    required_columns = ["Open","High","Low","Close","Volume"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required Columns : {missing_columns}")
    
def download_stock_data(ticker:str,start_date:str=None,end_date:str=None) -> pd.DataFrame:
    if start_date is None:
        start_date= config.default_start_date
    
    if end_date is None:
        end_date= config.default_end_date

    normalize_ticker = normalize_indian_ticke(ticker)
    logger.info(f"downloading data for ticker= {normalize_ticker},start={start_date}, end={end_date}")

    try:
        df= yf.download(
            normalize_ticker,
            start=start_date,
            end=end_date,
            progress=False,
            auto_adjust=False
        )
        
        df.index.name= "Date"

        df= df.reset_index()

        df= df.dropna(subset=["Open","High","Low","Close","Volume"])

        validate_stock_data(df)
        logger.info(f"Downloaded {len(df)} rows for {normalize_ticker}")
        return df
    except Exception as error:
        logger.error(f"Failed to download stock data for {normalize_ticker}: {error}")
        raise

if __name__== "__main__":
    sample_df= download_stock_data("RELIANCE","2022-01-01", "2024-12-31")
    print(sample_df.head())
