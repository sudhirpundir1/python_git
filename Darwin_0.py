import datetime
#import csv
readFile=open("C:\\Users\\spundir\\Desktop\\Python\\Event_Config.csv","r")
if readFile.mode == "r":
    contents=readFile.readlines()
    #print(contents)

dict = {}
for i in contents:
   splitData = i.split(",")
   event_name = splitData[0]
   event_category = splitData[3]
   max_table_name = splitData[4]
   event_category = "P1"
   pipeline_name = splitData[5]
   is_max=""
   if(pipeline_name=="max"):
       is_max='True'
   else:
        is_max='False'
   is_gravity=""
   if (pipeline_name == "gravity"):
       is_gravity = 'True'
   else:
       is_gravity = 'False'
   raw_table_name="darwin.ets_events_"+event_name.lower()+"_raw"
   freequency="Daily"
   created_time="date"
   created_by="mdpuser"
   updated_time="updated_time"
   updated_by="updated_by"
   threshold="2"
   lookback="-3"
   listFinal = [event_name,event_category,is_max,is_gravity,raw_table_name,max_table_name,freequency,created_time,created_by,updated_time,updated_by,threshold,lookback]
   #print(listFinal)
   #listFinal_2 = ','.join(listFinal)
   #print(listFinal_2)
   #list_2 = listFinal_2.split((","))
   #print(listFinal)
   #for i in listFinal:
   if event_name in dict.keys():
       data_key = dict.get(event_name)
       if is_max == "True" :
        data_key['is_max'] = is_max
       if is_gravity== "True":
            data_key['is_gravity'] = is_gravity
       dict[event_name] = data_key
   else:
        dict[event_name] ={"event_name":listFinal[0],"event_category":listFinal[1],"is_max":is_max,"is_gravity":is_gravity,"raw_table_name":listFinal[4],"max_table_name":listFinal[5],"freequency":listFinal[6],"created_time":listFinal[7],"created_by":listFinal[8],"updated_time":listFinal[9],"updated_by":listFinal[10],"threshold":listFinal[11],"lookback":listFinal[12]}
print(dict)

listFinal_2 = list()
with open("C:\\Users\\spundir\\Desktop\\Python\\out.csv","w") as file_obj:
    for x in dict:
        dict_value = dict.get(x)
        #print(dict_value['event_name'])
        listFinal_3=(dict_value['event_name'],dict_value['event_category'],dict_value['is_max'],dict_value['is_gravity'],dict_value['raw_table_name'],dict_value['max_table_name'],dict_value['freequency'],dict_value['created_time'],dict_value['created_by'],dict_value['updated_time'],dict_value['updated_by'],dict_value['threshold'],dict_value['lookback'])
        #print(listFinal_3)
        line = ",".join(listFinal_3)
        #print(line)
        file_obj.write(line+"\n")




