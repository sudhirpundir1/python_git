import pyspark

sc = pyspark.SparkContext('local[*]')
inputInteger = list(range(1,20))
print(inputInteger)
integerRDD = sc.parallelize(inputInteger)
print(integerRDD)