# Import necessary modules and classes from Airflow
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime

# Import the custom function 'run_twitter_etl' from 'twitter_etl' module
from twitter_etl import run_twitter_etl

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the DAG (Directed Acyclic Graph)
dag = DAG(
    'twitter_dag',                          # DAG identifier
    default_args=default_args,              # Default arguments dictionary
    description='Our first DAG with ETL process!',  # Description of the DAG
    schedule_interval=timedelta(days=1),    # Set the execution frequency (every day in this case)
)

# Define a PythonOperator task named 'complete_twitter_etl'
run_etl = PythonOperator(
    task_id='complete_twitter_etl',        # Task identifier
    python_callable=run_twitter_etl,        # Python function to be executed
    dag=dag,                                # Reference to the DAG
)

# Set up the task dependencies (if any) - here, there are no dependencies
# 'run_etl' does not depend on any other task
# Uncomment and modify the following line if you have dependencies:
# run_etl.set_upstream([other_task_id])

# Return the DAG to Airflow for processing
# Note: This line is not necessary, but it's included for clarity
run_etl
