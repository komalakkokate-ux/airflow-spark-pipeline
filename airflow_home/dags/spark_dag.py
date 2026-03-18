from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'komal',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    'spark_dag',
    default_args=default_args,
    description='Run Spark job via BashOperator',
    schedule_interval=None,
    start_date=datetime(2026, 3, 18),
    catchup=False,
) as dag:

    run_spark_job = BashOperator(
        task_id='run_spark_job',
        bash_command="""
        export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
        export SPARK_HOME=/home/komal/spark

        export PYSPARK_PYTHON=/home/komal/data-engineering-projects/airflow-spark-pipeline/airflow_venv/bin/python3
        export PYSPARK_DRIVER_PYTHON=/home/komal/data-engineering-projects/airflow-spark-pipeline/airflow_venv/bin/python3

        export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$PATH

        $SPARK_HOME/bin/spark-submit --master local[*] /home/komal/data-engineering-projects/airflow-spark-pipeline/spark_jobs/sample_spark_job.py
        """
    )
