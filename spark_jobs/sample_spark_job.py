from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("UserDataPipeline").getOrCreate()

# Read CSV
df = spark.read.csv("/home/komal/data-engineering-projects/airflow-spark-pipeline/input/data.csv", header=True, inferSchema=True)


# Transformation
df_clean = df.dropna()
df_filtered = df_clean.filter(df_clean["age"] > 20)

# Write output
df_filtered.write.mode("overwrite").parquet("output/processed_data")

df_filtered.show()

spark.stop()
