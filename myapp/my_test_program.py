from os import getenv
from socket import gethostbyname, gethostname
from pyspark.sql import SparkSession,Row
from pyspark.mllib.random import RandomRDDs

SPARK_MASTER= getenv('SPARK_MASTER','local[2]')
OUTPUT_DIR=getenv('OUTPUT_DIR')
if(OUTPUT_DIR==None):
        raise Exception('OUTPUT_DIR cannot be null');

spark = SparkSession.builder \
        .appName("my_app") \
        .config("spark.driver.host",gethostbyname(gethostname())) \
        .master(SPARK_MASTER) \
        .getOrCreate()

l=[('alex',25),('cristina',22),('sergiu',20),('john',26)]
rdd = spark.sparkContext.parallelize(l)
people = rdd.map(lambda x: Row(name=x[0], age=int(x[1])))

data = spark.createDataFrame(people)

data.write.mode("overwrite").save(OUTPUT_DIR);
