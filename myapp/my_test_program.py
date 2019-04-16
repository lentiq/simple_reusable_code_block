#!/usr/bin/python
from os import getenv
import sys

SPARK_MASTER= getenv('SPARK_MASTER','local[2]')
SIZE_X = getenv('SIZE_X',10)
SIZE_Y = getenv('SIZE_Y',10)
OUTPUT_DIR=getenv('OUTPUT_DIR')

if(OUTPUT_DIR==None):
	raise Exception('OUTPUT_DIR cannot be null');

from pyspark.sql import SparkSession

spark = SparkSession.builder \
	.master(SPARK_MASTER) \
	.getOrCreate()

#this program simply writes a random table to the data lake

from pyspark.mllib.random import RandomRDDs

data  = RandomRDDs.uniformVectorRDD(spark.sparkContext, SIZE_X, SIZE_Y).map(lambda a : a.tolist()).toDF()

data.write.save(OUTPUT_DIR);
