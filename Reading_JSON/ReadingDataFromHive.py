#! /usr/bin/python
import os

hive_cmd = "beeline -u 'jdbc:hive2://hs2stage.corp.adobe.com:10000/default;principal=hive/_HOST@ADOBENET.GLOBAL.ADOBE.COM' --showHeader=false --outputformat=tsv2 -e 'select * from darwin.ets_events_config_v2'"
result = os.popen(hive_cmd).read()
contents = result.splitlines()
# print(contents)

dict = {}
for i in contents:
    splitData = i.split("\t")
    # print(splitData)
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
    threshold = "2"
    lookback = "-3"
    listFinal = [event_name, event_category, is_max, is_gravity, raw_table_name, max_table_name, freequency,
                 created_time, created_by, updated_time, updated_by, threshold, lookback]
    print(listFinal)
    if event_name in dict.keys():
        data_key = dict.get(event_name)
        if is_max == "True":
            data_key['is_max'] = is_max
        if is_gravity == "True":
            data_key['is_gravity'] = is_gravity
        dict[event_name] = data_key
    else:
        dict[event_name] = {"event_name": listFinal[0], "event_category": listFinal[1], "is_max": is_max,
                            "is_gravity": is_gravity, "raw_table_name": listFinal[4], "max_table_name": listFinal[5],
                            "freequency": listFinal[6], "created_time": listFinal[7], "created_by": listFinal[8],
                            "updated_time": listFinal[9], "updated_by": listFinal[10], "threshold": listFinal[11],
                            "lookback": listFinal[12]}
print(dict)

beeline_cmd = "beeline -u 'jdbc:hive2://hs2stage.corp.adobe.com:10000/default;principal=hive/_HOST@ADOBENET.GLOBAL.ADOBE.COM' -e 'CREATE EXTERNAL TABLE IF NOT EXISTS `darwin.output_event_Config`( event_name string, event_category string, is_max string, is_gravity string, raw_table_name string, max_table_name string, freequency string, created_time string, created_by string, updated_time string, updated_by string, threshold string, lookback string) Row format delimited Fields terminated by ',' stored as orc;' "

