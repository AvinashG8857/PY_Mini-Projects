import numpy as np
import pandas as pd
from sklearn.metrics import (mean_absolute_error,mean_squared_error,mean_absolute_percentage_error)

from app.logger import logger

def calculate_metrics(y_true,y_pred)-> dict:
    mae= mean_absolute_error(y_true,y_pred)
    rmse= np.sqrt(mean_squared_error(y_true,y_pred))
    mape= mean_absolute_percentage_error(y_true,y_pred)

    return {
        "MAE":mae,
        "RMSE": rmse,
        "MAPE":mape
    }

def evaluate_model(models:dict,X_val,Y_val,X_test,Y_test)-> tuple[pd.DataFrame,dict]:
    metrics_rows=[]
    predtiction_dict={}
    for model_name,model in models.items():
        logger.info(f"Evaluating Model: {model_name}")
        val_pred= model.predict(X_val)
        test_pred= model.predict(X_test)
        predtiction_dict[model_name]={
            "val_pred": val_pred,
            "test_pred":test_pred
        }

    val_metrics=calculate_metrics(Y_val,val_pred)
    test_metrics= calculate_metrics(Y_test,test_pred)
    metrics_rows.append({
        "Model":model_name,
        "Validation_MAE":val_metrics["MAE"],
        "Validation_RMSE":val_metrics["RMSE"],
        "Validation_MAPE":val_metrics["MAPE"],
        "Test_MAE":test_metrics["MAE"],
        "Test_RMSE":test_metrics["RMSE"],
        "Test_MAPE": test_metrics["MAPE"]
    })

    metrics_df=pd.DataFrame(metrics_rows)
    metrics_df= metrics_df.sort_values(by="Test_RMSE").reset_index(drop=True)
    return metrics_df,predtiction_dict

def build_predictin_dataFrame(df_test:pd.DataFrame,y_test,y_pred,model_name:str)->pd.DataFrame:
    comparision_df= pd.DataFrame({
        "Date":df_test["Date"].values,
        "Actual":y_test.values,
        "Predicted":y_pred
    })
    comparision_df["Model"]= model_name

    return comparision_df
    