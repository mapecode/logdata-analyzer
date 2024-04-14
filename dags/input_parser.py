import sys
import os
import logging
from airflow import DAG
from airflow.models.variable import Variable
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.config import LOG_FILE, HOSTNAME
from src.LogParser import LogParser

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime.utcnow(),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "logfile_parser",
    default_args=default_args,
    description="A DAG to parse logfiles every hour",
    schedule_interval=timedelta(hours=1),
)


def task_run_file_parser(**kwargs):
    last_position = Variable.get("last_position", default_var=0)
    execution_date = Variable.get("execution_date", default_var=datetime.utcnow())
    next_execution_date = execution_date + timedelta(hours=1)

    log_parser = LogParser(LOG_FILE)

    results, last_pos = log_parser.get_hostname_stats(HOSTNAME, execution_date, next_execution_date, last_position)

    kwargs['ti'].xcom_push(key='results', value=results)
    Variable.set("last_position", last_position)
    Variable.set("execution_date", execution_date)

    return results


run_file_parser = PythonOperator(
    task_id="run_file_parser",
    python_callable=task_run_file_parser,
    provide_context=True,
    dag=dag,
)
