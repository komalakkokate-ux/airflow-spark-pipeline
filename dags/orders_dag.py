from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    "owner": "komal",
    "depends_on_past": False,
    "retries": 1,
}

dag = DAG(
    dag_id="orders_pipeline_dag",
    default_args=default_args,
    start_date=datetime(2026, 3, 17),
    schedule_interval=None,  # manual trigger
    catchup=False,
)

spark_task = SparkSubmitOperator(
    task_id="run_orders_pipeline",
    application="/home/komal/data-engineering-projects/data-lake-pipeline/spark_jobs/orders_pipeline.py",
    conn_id="spark_default",
    dag=dag,
)
