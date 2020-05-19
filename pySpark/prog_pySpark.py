from pyspark import *
##from pyspark.sql import *
##from pyspark.sql.types import *


#sc= SparkContext(master="local",appName="Spark Demo")

#print(sc.textFile("C:\\Talend Training\\Output\\EMP_Normalise.txt").first())

# create Spark context with Spark configuration
conf = SparkConf().setAppName("read text file in pyspark")
sc = SparkContext(conf=conf)

# Read file into RDD
lines = sc.textFile("C:\\Talend Training\\Output\\EMP_Normalise.txt")

# Call collect() to get all data
llist = lines.collect()
print(llist)