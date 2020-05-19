#- To Search a text from the File.
import pyspark

sc = pyspark.SparkContext('local[*]')
lines = sc.textFile("C:\\Talend Training\\Output\\EMP_Normalise.txt")
linesWithSuresh = lines.filter(lambda n :  'suresh' in n.lower())
print(lines.collect())
print(lines.count())
print(lines.first())
print('\n2nd RDD**',linesWithSuresh.collect())
