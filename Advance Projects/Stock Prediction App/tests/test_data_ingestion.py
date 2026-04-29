import pandas as pd

from app.data_ingestion import normalize_indian_ticker, validate_stock_data

def test_normalize_indian_ticker_adds_ns():
    assert normalize_indian_ticker("RELIANCE") == "RELIANCE.NS"

def test_normalize_indian_ticker_keeps_existing_suffix():
    assert normalize_indian_ticker("TCS.NS") == "TCS.NS"

def test_validate_stock_data_accepts_valid_dataframe():
    df = pd.DataFrame({
        "Open": [1],
        "High": [2],
        "Low": [0.5],
        "Close": [1.5],
        "Volume": [1000]
    })

    validate_stock_data(df)