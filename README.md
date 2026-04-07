# Airflow + Spark Data Pipeline

## 📌 Overview

This project demonstrates an end-to-end data pipeline using Apache Airflow and Apache Spark.

## ⚙️ Tech Stack

* Python
* Apache Spark
* Apache Airflow

## 🔄 Workflow

1. Airflow DAG triggers Spark job
2. Spark processes input data
3. Output is stored in `output/processed_data/` in Parquet format

## 📂 Output

The processed data is saved in Parquet format:

* `output/processed_data/`

## 📸 Screenshots

* DAG execution success
* Task logs
* Output files

## ▶️ How to Run

```bash
airflow scheduler
airflow webserver
```

Then trigger DAG from UI.

## 💡 Learnings

* Integrated Spark with Airflow
* Handled environment setup (Java, Spark)
* Built end-to-end ETL pipeline

## 🙋 Author

Komal Kokate

This project is for learning purposes only. Unauthorized commercial use is not allowed.
