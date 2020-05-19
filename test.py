import datetime
import csv
readFile=open("C:\\Users\\spundir\\Desktop\\Python\\Event_Config.csv","r")
if readFile.mode == "r":
    contents=readFile.readlines()
    #print(contents)

dict = {}
for i in contents:
    #print(i)
    splitdata=i.split() #converting lines to list
    #print(splitdata)
    splitData = i.split(",")
    event_name = splitData[0]
    event_category = splitData[3]
    max_table_name = splitData[4]
    event_category = "P1"
    pipeline_name = splitData[5]
    is_max = ""
    if (pipeline_name == "max"):
        is_max = 'True'
    else:
        is_max = 'False'
    is_gravity = ""
    if (pipeline_name == "gravity"):
        is_gravity = 'True'
    else:
        is_gravity = 'False'
    raw_table_name = "darwin.ets_events_" + event_name.lower() + "_raw"
    freequency = "Daily"
    created_time = "date"
    created_by = "mdpuser"
    updated_time = "updated_time"
    updated_by = "updated_by"
    listFinal = [event_name, event_category, is_max, is_gravity, raw_table_name, max_table_name, freequency,created_time, created_by, updated_time, updated_by]
    print(listFinal)