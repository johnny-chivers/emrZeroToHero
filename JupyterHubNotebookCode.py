# Step 1 
import sys
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Step 2
input_path = "s3://<YourS3BucketName>/input/tripdata.csv"
output_path = "s3://<YourS3BucketName>/output/"

# Step 3
nyTaxi = spark.read.option("inferSchema", "true").option("header", "true").csv(input_path)

# Step 4
nyTaxi.count()

# Step 5
nyTaxi.show()

# Step 6 
nyTaxi.printSchema()

# Step 7
updatedNYTaxi = nyTaxi.withColumn("current_date", lit(datetime.now()))

# Step 8 
updatedNYTaxi.printSchema()
