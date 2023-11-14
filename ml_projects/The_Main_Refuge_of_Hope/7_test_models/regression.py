from sktime.performance_metrics.forecasting import  MeanAbsolutePercentageError
from sklearn.metrics import mean_squared_error,mean_absolute_error #метрики
from catboost import CatBoostRegressor
import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient
mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("cost test MinMax")

smape = MeanAbsolutePercentageError(symmetric = True)#метрика sMAPE

with mlflow.start_run():
    X_valid = pd.read_parquet('/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_split/cost_X_valid.parquet')
    y_valid = pd.read_parquet('/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_split/cost_y_valid.parquet')
    
    loaded_modelR = CatBoostRegressor()
    loaded_modelR.load_model('/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/load_models/catboost_cost_Min_Max_valid.bin')
    score = loaded_modelR.predict(X_valid)
    print('sMAPE', smape(y_valid, score).round(4))
    print("mae",mean_absolute_error(y_valid, score).round(4))
    print("mse", mean_squared_error(y_valid, score).round(4))
     # Логирование артефактов 
    mlflow.log_artifact(
        local_path="/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/7_7_test_models/regression.py", 
        artifact_path="Catboost cost MinMax"
        )
mlflow.end_run()           