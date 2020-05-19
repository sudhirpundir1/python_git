#Programm with MapReduce.

import pyspark
from functools import reduce

sc = pyspark.SparkContext('local[*]')
textFile = sc.textFile('C:\\Users\\sudhi\\PycharmProjects\\Adobe_Proj\\Udemy\\Pandas\\original.csv')
#print(textFile.take(10))
# textFileFiltered = textFile.filter(lambda x : 'europe' in x.lower() ) #Filtering country where region = EUROPE
textFileFiltered = textFile.filter(lambda p : 'europe' in p.split(",")[1].lower()) #Filtering country where region = EUROPE

textFileFilteredPopulation = textFileFiltered.filter(lambda x: int(x.split(",")[2]) >= 1000000 and int(x.split(",")[2]) <= 5000000)
textFileFilteredPopulationCoastLine = textFileFilteredPopulation.map(lambda cl : float(cl.split(",")[4]))
EuropeCostLine = textFileFilteredPopulationCoastLine.reduce(lambda x,y : x+y)
print(f'Europe CostLine Area is: {EuropeCostLine}')