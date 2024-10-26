from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GIS Processing").getOrCreate()
df = spark.read.csv("hdfs://hadoop:9000/data/gis_data.csv")
# Perform transformations
