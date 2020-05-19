import os
import csv



f = open('C:/Users/sudhi/Input_Files/Data Set- Inc5000 Company List_2014.csv','r')
g = open('C:/Users/sudhi/Input_Files/sample.csv','a')
#print(f.read())
#--
#print(f.readline())
#print(f.readline())
for x in f:
   # print(x)
    print(f.readline())
    g.write(x)
f.close()
g.close()