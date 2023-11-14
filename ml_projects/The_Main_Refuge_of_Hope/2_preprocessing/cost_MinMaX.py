import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("process_data cost")

with mlflow.start_run():
    # Чтение данных из файла
    cost = pd.read_parquet('/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/cost.parquet')

    # Преобразование данных (пример: нормализация значений 'cost')
    scaler = MinMaxScaler()
    cost_normalized = scaler.fit_transform(cost[['cost']])
    cost['cost_normalized'] = cost_normalized
    cost = cost.set_index('date')

    # Логирование преобразованных данных
    mlflow.log_param("transformation", "Normalization")
    mlflow.log_artifact(local_path='/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/cost_MinMax.parquet', artifact_path='costMinMax.parquet')

# Завершение MLflow запуска
mlflow.end_run()

'''Изменения:

    Добавлен импорт MinMaxScaler из библиотеки sklearn.preprocessing для проведения нормализации.
    Применена нормализация значений столбца 'cost' с использованием MinMaxScaler.
    Новый столбец 'cost_normalized' добавлен к исходному DataFrame.
    Логирован параметр transformation с указанием примененного метода трансформации данных (в данном случае, нормализация).'''

