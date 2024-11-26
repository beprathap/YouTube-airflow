from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from include.main import main

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id="youtube_data_pipeline",
    default_args=default_args,
    description="YouTube Data Pipeline DAG",
    schedule_interval="@daily",  # Adjust the schedule as needed
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Task to run the existing main.py functionality
    run_youtube_pipeline = PythonOperator(
        task_id="extract_youtube_data",
        python_callable=main,  # Call the main function from main.py
    )

    # Define task dependencies (only one task here)
    run_youtube_pipeline