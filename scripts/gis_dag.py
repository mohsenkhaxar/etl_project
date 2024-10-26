from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from gis_pipeline.data_ingest import fetch_data

dag = DAG("gis_data_pipeline", start_date=datetime(2024, 1, 1))
fetch_task = PythonOperator(
    task_id="fetch_data",
    python_callable=fetch_data,
    op_kwargs={'api_url': 'dynamic_value1', 'param2': 'dynamic_value2'},
    dag=dag
)
fetch_task
