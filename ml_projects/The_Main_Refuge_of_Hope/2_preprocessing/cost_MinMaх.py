import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import mlflow

# Set the MLflow tracking URI and experiment name
mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("cost MinMaxScaler")

# Start a new MLflow run
with mlflow.start_run():
    # Read data from a Parquet file
    cost = pd.read_parquet('/home/an/mlops4/ml_projects/The_Main_Refuge_of_Hope/0_get_data/df_cost.parquet')
    
    # Transform the data (example: normalize 'cost' column)
    scaler = MinMaxScaler()
    cost_normalized = scaler.fit_transform(cost[['cost']])
    cost['cost_normalized'] = cost_normalized
    cost['datetime_int'] = cost['date'].astype(int)
    X = cost.drop(['date', 'cost'], axis=1)
    X = pd.get_dummies(X)
    y = cost['cost']
    y = pd.DataFrame(y)
    
    # Log the transformation type
    mlflow.log_param("transformation", "Normalization")
    
    # Log additional information about the transformation
    mlflow.log_param("normalized_columns", ["cost"])

    # Save the transformed data to Parquet files
    X.to_parquet("costX.parquet")
    y.to_parquet("cost_y.parquet")

# End the MLflow run
mlflow.end_run()  


'''Изменения:

    Добавлен импорт MinMaxScaler из библиотеки sklearn.preprocessing для проведения нормализации.
    Применена нормализация значений столбца 'cost' с использованием MinMaxScaler.
    Новый столбец 'cost_normalized' добавлен к исходному DataFrame.
    Логирован параметр transformation с указанием примененного метода трансформации данных (в данном случае, нормализация).'''

