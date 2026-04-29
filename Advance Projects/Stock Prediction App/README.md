# Indian Stock Market Prediction App

A modular Python machine learning project that predicts future stock prices for Indian stocks using historical market data.

## Features

- Download real stock data using yfinance
- Support Indian stock tickers like RELIANCE.NS, TCS.NS, INFY.NS
- Feature engineering:
  - Returns
  - Rolling averages
  - Volatility
  - Lag features
  - RSI
  - Price spread features
- Train two machine learning models:
  - Linear Regression
  - Random Forest Regressor
- Evaluate with:
  - MAE
  - RMSE
  - MAPE
- Interactive web dashboard using Streamlit
- Unit tests included
- Modular clean architecture

## Project Structure

```text
stock-market-prediction-app/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── logger.py
│   ├── data_ingestion.py
│   ├── features.py
│   ├── models.py
│   └── evaluate.py
│
├── tests/
│   ├── test_features.py
│   ├── test_data_ingestion.py
│   └── test_models.py
│
├── logs/
├── outputs/
├── requirements.txt
└── README.md
```

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the environment:

### Windows
```bash
venv\Scripts\activate
```

### Linux / macOS
```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app/app.py
```

## Example Tickers

- RELIANCE.NS
- TCS.NS
- INFY.NS
- HDFCBANK.NS
- SBIN.NS

You can also type plain names like RELIANCE or TCS, and the app will automatically convert them to `.NS`.

## Run Tests

```bash
pytest
```

## ML Workflow

1. Download historical stock data
2. Create technical and lag-based features
3. Build future target column
4. Split into train, validation, and test sets
5. Train models
6. Compare evaluation metrics
7. Show results in dashboard

## Future Improvements

- Add XGBoost
- Add LSTM / GRU model
- Add model saving with joblib
- Add candlestick charts
- Add multi-step forecasting
- Add portfolio comparison