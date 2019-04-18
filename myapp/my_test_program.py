from os import getenv
import sys
from socket import gethostbyname, gethostname 
from pyspark.sql import SparkSession
from pyspark.mllib.random import RandomRDDs

SPARK_MASTER= getenv('SPARK_MASTER','local[2]')
SIZE_X = int(getenv('SIZE_X',10))
SIZE_Y = int(getenv('SIZE_Y',10))
OUTPUT_DIR=getenv('OUTPUT_DIR')

if(OUTPUT_DIR==None):
	raise Exception('OUTPUT_DIR cannot be null');

spark = SparkSession.builder \
	.appName("my_app") \
	.config("spark.driver.host",gethostbyname(gethostname())) \
	.master(SPARK_MASTER) \
	.getOrCreate()

data  = RandomRDDs.uniformVectorRDD(spark.sparkContext, SIZE_X, SIZE_Y).map(lambda a : a.tolist()).toDF()

data.write.mode("overwrite").save(OUTPUT_DIR);
