import sys
import datetime
#import csv
args=sys.argv[1:]
category, pipeLine, thread = sys.argv[1:4]
jobType=""
processDate=""
dict={}
categoryData = []
print(category+thread+pipeLine)
readFile=open("C:\\Users\\spundir\\Desktop\\Python\\Event_Config_out.csv","r")

if readFile.mode == "r":
    contents=readFile.readlines()
    #print(contents)
for i in contents:
     contentList = i.split(",")
     event_name = contentList[0]
     content_cateogry = contentList[1]
     is_max = contentList[2]
     is_gravity = contentList[3]
     categoryData_1 = []
     print(contentList)
     #print(content_cateogry)
     if category == content_cateogry:
         categoryData_1.append(i)
         #print(categoryData_1)