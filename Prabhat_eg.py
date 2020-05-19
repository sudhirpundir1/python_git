import sys
import datetime
#import csv
args=sys.argv[1:]
category=sys.argv[1]
thread = sys.argv[2]
jobType=""
processDate=""
pipeLine=""
dict ={}
categoryData = []
#print(category)
with open("C:\\Users\\spundir\\Desktop\\Python\\Event_Config_out.csv","r") as readFile:
    lines = readFile.readlines()
    lines = lines[1:] #skip first trow
#print(lines)

for line in lines :
    splitContent = line.split(",")
    #print(splitContent)
    event_name,event_category,is_max,is_gravity,raw_table_name=splitContent[:5]
    #print(splitContent)
###Converting List into Dictionary:
    dict_value={}
    #categoryData=[]
    dict_value["event_category"]=event_category
    dict_value["is_max"] = is_max
    dict_value["is_gravity"] = is_gravity
    dict_value["raw_table_name"] = raw_table_name
    dict_value["event_name"] = event_name
    #print(dict_value)
###converting multiline dictionary to single line list
    categoryData.append(dict_value)
print(categoryData)
#converting List into Dictionary
dict["eventList"]=categoryData

#print(dict)
