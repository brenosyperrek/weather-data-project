import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from insert_records import main
    main()

default_args = {
    'description': 'Orquestrador para coletar e inserir dados meteorológicos',
    'start_date': datetime(2025, 1, 1),
    'catchup': False,
}

dag = DAG(
    dag_id='weather_api_orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='fetch_and_insert_weather_data',
        python_callable=safe_main_callable
    )