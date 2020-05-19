import os
import subprocess
hive_cmd = "beeline -u 'jdbc:hive2://hs2prod.corp.adobe.com:10000/default;principal=hive/hs2prod.corp.adobe.com@ADOBENET.GLOBAL.ADOBE.COM' --showHeader=false --outputformat=tsv2 -e 'select event_name,max_table_name from darwin_uat.event_config_meta_data where is_max='True''"
result = os.popen(hive_cmd).read()
contents = result.splitlines()
print(contents)



import os
import subprocess
hive_cmd = "beeline -u 'jdbc:hive2://hs2stage.corp.adobe.com:10000/default;principal=hive/_HOST@ADOBENET.GLOBAL.ADOBE.COM' --showHeader=false --outputformat=tsv2 -e 'select * from darwin.ets_events_config_v2'"
result = os.popen(hive_cmd).read()
contents = result.splitlines()
#print(contents)