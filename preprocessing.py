import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from datetime import datetime
import re

spark = SparkSession.builder.appName("RealEstateData").getOrCreate()
date = datetime.today().strftime('%Y-%m-%d')
def clean_data():
    df1 = spark.read.option('header', 'True').csv(f'data/bayut_{date}.csv')
    df2 = spark.read.option('header', 'True').csv(f'data/property_finder_{date}.csv')
    df = df1.unionByName(df2)
    cleaned_cols = [re.sub("[^a-zA-Z0-9]", '', c) for c in df.columns]
    df = df.toDF(*cleaned_cols)
    df = df.withColumn('Price', regexp_replace(col('Price'), '[^0-9]', '').cast(IntegerType()))
    df = df.withColumn('Area', regexp_replace(col('Area'), '[^0-9]', '').cast(IntegerType()))
    df = df.withColumn('DownPayment', regexp_replace(col('DownPayment'), '[^0-9]', '').cast(IntegerType()))
    df = df.withColumn('DownPayment', when(col('DownPayment').isNull(), 0).otherwise(col('DownPayment')))
    df = df.withColumn('Bedrooms', regexp_replace(col('Bedrooms'), '[^0-9]', '').cast(IntegerType()))
    df = df.withColumn('Bathrooms', regexp_replace(col('Bathrooms'), '[^0-9]', '').cast(IntegerType()))
    df = df.withColumn('SubLocation', reverse(split(col('Location'), ',')).getItem(1).cast(StringType()))
    df = df.withColumn('Location', reverse(split(col('Location'), ',')).getItem(0).cast(StringType()))
    df = df.withColumn('Bedrooms', when(col('Bedrooms').isNull(), 1).otherwise(col('Bedrooms')))
    df = df.drop('Description')
    return df