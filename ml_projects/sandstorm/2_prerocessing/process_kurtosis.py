import pandas as pd
import numpy as np
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("process_data")
with mlflow.start_run():
    df = pd.read_csv('/home/an/mlops4/ml_projects/sandstorm/get_datasets/df.csv')

    mean_values = df[df.columns[:-1]].kurtosis(axis=1, skipna=True)
    X = np.reshape(np.array(mean_values), (-1, 1))
    y = df["label"]
    X = pd.DataFrame(X)

    X.to_csv('/home/an/mlops4/ml_projects/sandstorm/datasets_preprocessing/X.csv', index=False)
    y.to_csv('/home/an/mlops4/ml_projects/sandstorm/datasets_preprocessing/y.csv', index=False)
    mlflow.log_artifact(local_path="/home/an/mlops4/ml_projects/sandstorm/2_prerocessing/process_kurtosis.py.py",
                        artifact_path="process_kurtosis code")
    mlflow.end_run()