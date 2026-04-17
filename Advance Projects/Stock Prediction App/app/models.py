import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from app.logger import logger
from app.config import config

def time_series_split(df:pd.DataFrame,feature_columns:list[str],target_column:str="Target"):
    n= len(df)
    train_end= int(n* config.val_ratio)
    val_end= train_end+int(n*config.val_ratio)

    df_train= df.iloc[:train_end].copy()
    df_val=df.iloc[train_end:val_end].copy()
    df_test= df.iloc[val_end:].copy()
    X_train= df_train[feature_columns]
    X_val= df_val[feature_columns]
    X_test= df_test[feature_columns]

    Y_train=df_train[target_column]
    Y_val=df_val[target_column]
    y_test = df_test[target_column]

    logger.info(
        f"Split sizes -> Train: {len(df_train)}, Validation: {len(df_val)}, Test: {len(df_test)}"
    )
    return X_train,X_val,X_test,Y_train,Y_val,y_test,df_train,df_val,df_test

def train_linear_regression(X_train:pd.DataFrame,y_train:pd.Series) -> Pipeline:
    logger.info("training Linear Regression Model")

    model= Pipeline([("scaler",StandardScaler()),
    ("model",LinearRegression())
    ])

    model.fit(X_train,y_train)

    return model

def train_random_forest(X_train:pd.DataFrame,y_train:pd.Series)-> RandomForestRegressor:
    logger.info("Trainning Random Forest Model")
    model= RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=config.random_state,
        n_jobs=1
    )

    model.fit(X_train,y_train)
    return model

def generate_Predictions(model, X_data:pd.DataFrame)-> np.ndarray:
    predictions= model.predict(X_data)
    return predictions

def train_all_models(X_train: pd.DataFrame,Y_train:pd.Series)-> dict:
    linear_model= train_all_models(X_train,Y_train)
    rf_model= train_random_forest(X_train,Y_train)
    return{
        "Linear Regression": linear_model,
        "Random Forest":rf_model
    }