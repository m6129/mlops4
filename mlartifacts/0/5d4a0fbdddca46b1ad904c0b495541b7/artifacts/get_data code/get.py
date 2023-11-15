import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient
import requests

mlflow.set_tracking_uri("http://0.0.0.0:5000")
with mlflow.start_run():
    df = requests.get("https://raw.githubusercontent.com/m6129/UrFU_2022_python/main/all_xackatons/train.csv")
    
    with open("/home/an/mlops4/ml_projects/sandstorm/get_datasets/df.csv", "w") as f:
        f.write(df.text)
        mlflow.log_artifact(local_path="/home/an/mlops4/ml_projects/sandstorm/0_get_data/get.py",artifact_path="get_data code")
        mlflow.end_run()