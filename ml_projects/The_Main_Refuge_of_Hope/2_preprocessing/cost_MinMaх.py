import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("cost MinMaxScaler")

with mlflow.start_run():
    # Чтение данных из файла
    cost = pd.read_parquet('/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/0_get_data/cost.parquet')

    # Преобразование данных (пример: нормализация значений 'cost')
    scaler = MinMaxScaler()
    cost_normalized = scaler.fit_transform(cost[['cost']])
    cost['cost_normalized'] = cost_normalized
    costMinMax = cost.set_index('date')
    costMinMax['datetime_int'] = costMinMax['datetime'].astype(int)
    X = costMinMax.drop(['datetime','cost'],axis=1)
    X = pd.get_dummies(X)
    y = costMinMax['cost']

    # Логирование преобразованных данных
    mlflow.log_param("transformation", "Normalization")
    mlflow.log_artifact(
        local_path='/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_preprocessing/costX.parquet',
        artifact_path='costMinMax X.parquet'
        )
    mlflow.log_artifact(
        local_path='/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_preprocessing/costy.parquet',
        artifact_path='costMinMax y.parquet'
        )
    X.to_parquet(
        "/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_preprocessing/costX.parquet")
    y.to_parquet(
        "/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/datasets_preprocessing/cost_y.parquet")

    # Логирование артефактов
    mlflow.log_artifact(
        local_path="/home/an/mlops4/ml_project/The_Main_Refuge_of_Hope/2_preprocessing/cost_MinMaх.py", 
        artifact_path="costX MinMax"
        )

# Завершение MLflow запуска
mlflow.end_run()

'''Изменения:

    Добавлен импорт MinMaxScaler из библиотеки sklearn.preprocessing для проведения нормализации.
    Применена нормализация значений столбца 'cost' с использованием MinMaxScaler.
    Новый столбец 'cost_normalized' добавлен к исходному DataFrame.
    Логирован параметр transformation с указанием примененного метода трансформации данных (в данном случае, нормализация).'''

