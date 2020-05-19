### read file and populate output Step2
import sys
#import datetime
#import csv
args=sys.argv[1:]
category, pipeLine, thread = sys.argv[1:4]
maxPipeLine = pipeLine.replace('max','TRUE')
gravitypipeLine = pipeLine.replace('gravity','TRUE')
jobType=""
processDate=""
dict={}
categoryData = []
#print(category+thread+pipeLine)
#print('max is:' + maxPipeLine)
#print('gravity is_1:' + gravitypipeLine)
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
     #print("is_max_2"+is_max )
     #print("gravity_2:" + is_gravity)
     if category == content_cateogry:
         if maxPipeLine == is_max:
             categoryData_1.append(i)
             #print(categoryData_1)
         if gravitypipeLine == is_gravity:
             categoryData_1.append(i)
             #print(categoryData_1)
         for i in categoryData_1:
                dict_value = {}
                splitContent= i.split(",")
                #print(splitContent)
                dict_value["eventCode"] = splitContent[0]
                dict_value["lookBack"] = splitContent[12]
                dict_value["maxTableName"] = splitContent[5]
                dict_value["raw_table_name"] = splitContent[4]
                dict_value["max"] = splitContent[2]
                dict_value["gravity"] = splitContent[3]
                dict_value["frequency"] = splitContent[6]
                dict_value["eventCategory"] = splitContent[1]
                dict_value["thersold"] = splitContent[11]
                #print(dict_value)
                categoryData.append(dict_value)

dict["eventList"]=categoryData
print(dict)
