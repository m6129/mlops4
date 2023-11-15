import mlflow
import wget

# Set the MLflow tracking URI and choose an experiment
mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("1_Refuge_of_Hope")

with mlflow.start_run():  # Start a new MLflow run
    # Define the URL of the Parquet file
    parquet_url = "https://github.com/m6129/UrFU_2022_python/raw/main/all_xackatons/GPN2023/df_cost.parquet"

    # Download the Parquet file using wget
    parquet_file = "/home/an/mlops4/ml_projects/The_Main_Refuge_of_Hope/0_get_data/df_cost.parquet"
    wget.download(parquet_url, out=parquet_file)

    # Log the Parquet file as an artifact
    mlflow.log_artifact(local_path=parquet_file, artifact_path="get_data_code")