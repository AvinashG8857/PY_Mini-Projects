from datetime import date

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from config import config
from data_ingestion import download_stock_data
from evaluate import build_prediction_dataframe, evaluate_models
from features import build_features, get_feature_columns
from logger import logger
from models import time_series_split, train_all_models

st.set_page_config(
    page_title=config.app_title,
    page_icon=config.page_icon,
    layout="wide"
)

st.title("📈 Indian Stock Market Prediction App")

st.markdown(
    """
    This app predicts future stock prices for Indian stocks using historical data,
    feature engineering, and machine learning models.
    """
)

st.sidebar.header("User Input")

ticker = st.sidebar.text_input("Enter NSE ticker", value=config.default_ticker)

start_date = st.sidebar.date_input("Start date", value=date(2018, 1, 1))
end_date = st.sidebar.date_input("End date", value=date(2026, 1, 1))

run_button = st.sidebar.button("Run Prediction")

def plot_historical_chart(df: pd.DataFrame, ticker_symbol: str):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["Close"],
            mode="lines",
            name="Close Price"
        )
    )

    fig.update_layout(
        title=f"Historical Close Price - {ticker_symbol}",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_prediction_chart(comparison_df: pd.DataFrame, model_name: str):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=comparison_df["Date"],
            y=comparison_df["Actual"],
            mode="lines",
            name="Actual"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=comparison_df["Date"],
            y=comparison_df["Predicted"],
            mode="lines",
            name="Predicted"
        )
    )

    fig.update_layout(
        title=f"Actual vs Predicted Prices - {model_name}",
        xaxis_title="Date",
        yaxis_title="Target Price",
        template="plotly_white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

if run_button:
    try:
        start_date_str = str(start_date)
        end_date_str = str(end_date)

        with st.spinner("Downloading data and training models..."):
            raw_df = download_stock_data(ticker, start_date_str, end_date_str)

            st.subheader("Historical Stock Chart")
            plot_historical_chart(raw_df, ticker)

            st.subheader("Raw Data Preview")
            st.dataframe(raw_df.tail(10), use_container_width=True)

            featured_df = build_features(raw_df)
            feature_columns = get_feature_columns(featured_df)

            X_train, X_val, X_test, y_train, y_val, y_test, df_train, df_val, df_test = time_series_split(
                featured_df,
                feature_columns,
                target_column="Target"
            )

            models = train_all_models(X_train, y_train)

            metrics_df, predictions_dict = evaluate_models(
                models,
                X_val,
                y_val,
                X_test,
                y_test
            )

            st.subheader("Model Evaluation Metrics")
            st.dataframe(metrics_df, use_container_width=True)

            best_model_name = metrics_df.iloc[0]["Model"]
            best_test_pred = predictions_dict[best_model_name]["test_pred"]

            comparison_df = build_prediction_dataframe(
                df_test,
                y_test,
                best_test_pred,
                best_model_name
            )

            st.subheader(f"Best Model: {best_model_name}")
            plot_prediction_chart(comparison_df, best_model_name)

            st.subheader("Prediction Comparison Table")
            st.dataframe(comparison_df.tail(20), use_container_width=True)

            st.success("Prediction workflow completed successfully!")

    except Exception as error:
        logger.error(f"App failed: {error}")
        st.error(f"Something went wrong: {error}")
else:
    st.info("Enter an Indian stock ticker like RELIANCE, TCS, INFY, SBIN and click 'Run Prediction'.")