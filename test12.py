import sys
import json
import datetime
#import csv
args=sys.argv[1:]
category=sys.argv[1]
thread = sys.argv[2]
jobType=""
processDate=""
pipeLine=""
dict={}
categoryData = []
#print(category)
readFile=open("C:\\Users\\spundir\\Desktop\\Python\\Event_Config_out.csv","r")

if readFile.mode == "r":
    contents=readFile.readlines()
    #print(contents)
for i in contents:
     contentList = i.split(",")
     event_name = contentList[0]
     content_cateogry = contentList[1]
     lookback=contentList[12].replace('\n','')
     #print(lookback)
     if category == content_cateogry:
         categoryData.append(i)
         for i in categoryData:
                splitContent= i.split(",")
                #print(splitContent)
                if splitContent[0] !="":
                    dict[event_name] = {"event_code": splitContent[0],"lookback": lookback,
                                        "max_table_name": splitContent[5],"raw_table_name": splitContent[4],
                                        "max": splitContent[2],"gravity": splitContent[3],
                                        "freequency": splitContent[6],"event_category": splitContent[1],
                                        "threshold": splitContent[11]}
                print(dict)
jsonData = json.dumps(dict)
#print(jsonData)
#print(dict)
