# Imports working with the cluster
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

from pyspark.sql.functions import lit

import pyspark.sql.functions as F

# Spark configurations
spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)

df_created_utc = spark.read.parquet("df_created_utc.parquet")

df_created_utc_month = df_created_utc.withColumn("month",from_unixtime(df_created_utc.created_utc,'MMM')).drop("created_utc")

df_comments_per_month = df_created_utc_month.groupby('month').count()

df_comments_per_month.write.mode("overwrite").parquet("df_comments_per_month.parquet")