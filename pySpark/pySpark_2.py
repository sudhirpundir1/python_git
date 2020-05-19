import pyspark
sc = pyspark.SparkContext('local[*]')
t1 = range(10000)
rdd = sc.parallelize(t1,2)
odds = rdd.filter(lambda x : x%2 !=0)
print(odds.take(10))
