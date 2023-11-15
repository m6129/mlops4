from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
import datetime as dt

# Определяем аргументы по умолчанию для DAG
args = {
    "owner": "admin",  # Владелец DAG
    "start_date": dt.datetime(2023, 11, 15),  # Начальная дата выполнения DAG
    "retries": 1,  # Количество попыток выполнения для каждой задачи
    "retry_delays": dt.timedelta(minutes=1),  # Время задержки между повторными попытками
    "depends_on_past": False  # Зависят ли задачи от успешного выполнения предыдущих задач
}

# Создаем новый DAG в Airflow с указанным идентификатором, аргументами по умолчанию и без интервала выполнения
with DAG(dag_id='sandstorm', default_args=args, schedule=None, tags=['ADA']) as dag:
    # Определяем каждую задачу как BashOperator, предоставляя идентификатор задачи и команду Bash для выполнения

    # Задача для получения данных 
    get_data = BashOperator(task_id='get',
        bash_command='python3 /home/an/mlops4/ml_projects/sandstorm/0_get_data/get.py',
        dag=dag)

    # Задача для подготовки данных 
    prepare_data = BashOperator(task_id='kurtosis_preprocessing',
        bash_command='python3 /home/an/mlops4/ml_projects/sandstorm/2_prerocessing/process_kurtosis.py',
        dag=dag)

    # Задача для разделения данных на обучающую и тестовую выборки 
    train_test_split = BashOperator(task_id='train_test_split',
        bash_command='python3 /home/an/mlops4/ml_projects/sandstorm/4_split/split_data.py',
        dag=dag)

    # Задача для обучения модели машинного обучения 
    train_model = BashOperator(task_id='catboost',
        bash_command='python3 /home/an/mlops4/ml_projects/sandstorm/5_model_learning/train_model.py',
        dag=dag)

    # Задача для тестирования модели машинного обучения 
    test_model = BashOperator(task_id='test',
        bash_command='python3 mlops4/ml_projects/sandstorm/6_test_models/test_model.py',
        dag=dag)

    # Определяем зависимости задач, указывая порядок их выполнения, чтобы обеспечить выполнение в нужной последовательности
    get_data >> prepare_data >> train_test_split >> train_model >> test_model