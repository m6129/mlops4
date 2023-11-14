import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient
from sklearn.model_selection import TimeSeriesSplit

mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("cost MinMaxScaler")

with mlflow.start_run():
    # Чтение данных из файла
    X = pd.read_parquet('/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/cost.parquet')
    y = pd.read_parquet('/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/cost.parquet')
    tscv = TimeSeriesSplit(n_splits=12)
    for fold,(train_index, valid_index) in enumerate(tscv.split(X,y)):
        X_train, X_valid = X.iloc[train_index], X.iloc[valid_index]
        y_train, y_valid = y.iloc[train_index], y.iloc[valid_index]
    X_train.to_parquet(
        "/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_split/cost_X_train.parquet")
    X_valid.to_parquet(
        "/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_split/cost_X_valid.parquet")
    y_train.to_parquet(
        "/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_split/cost_y_train.parquet")
    y_valid.to_parquet(
        "/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_split/cost_y_valid.parquet")