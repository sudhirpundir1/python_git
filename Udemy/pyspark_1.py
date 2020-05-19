import pyspark
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////C:\\Talend Training\\Output\\EMP_Normalise.txt')
print(txt.count())
print(txt.collect())
python_lines = txt.filter(lambda line: 'suresh' in line.lower())

print(python_lines.collect())

