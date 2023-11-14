import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient

# Установка URI для отслеживания MLflow и выбор эксперимента 
mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("1_Refuge_of_Hope")  # Трекинг конкретного эксперимента

with mlflow.start_run():  # Начало нового MLflow запуска
    # Получение данных по URL
    weather = pd.read_parquet('https://github.com/m6129/UrFU_2022_python/raw/main/all_xackatons/GPN2023/weather_df.parquet')
    transaction = pd.read_parquet('https://github.com/m6129/UrFU_2022_python/raw/main/all_xackatons/GPN2023/transaction_df.parquet')
    cost = pd.read_parquet('https://github.com/m6129/UrFU_2022_python/raw/main/all_xackatons/GPN2023/df_cost.parquet')
    competitors = pd.read_parquet('https://github.com/m6129/UrFU_2022_python/raw/main/all_xackatons/GPN2023/df_competitors.parquet')

    # Запись данных в файлы
    weather.to_parquet("/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/weather.parquet")
    transaction.to_parquet("/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/transaction.parquet")
    cost.to_parquet("/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/cost.parquet")
    competitors.to_parquet("/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/competitors.parquet")

    # Логирование артефактов
    mlflow.log_artifact(local_path="/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/weather.parquet", artifact_path="weather parquet")
    mlflow.log_artifact(local_path="/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/transaction.parquet", artifact_path="transaction parquet")
    mlflow.log_artifact(local_path="/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/cost.parquet", artifact_path="cost parquet")
    mlflow.log_artifact(local_path="/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/competitors.parquet", artifact_path="competitors parquet")

# Завершение MLflow запуска
mlflow.end_run()