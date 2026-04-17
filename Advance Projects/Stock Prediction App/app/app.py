from datetime import date
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from app.config import config
from app.data_ingestion import download_stock_data
from app.features import build_features,get_feature_coloumn
from app.models import time_series_split, train_all_models
from app.evaluate import evaluate_model,build_predictin_dataFrame
from app.logger import logger


st.set_page_config(
    page_title=config.page_icon
    page_icon=con
)