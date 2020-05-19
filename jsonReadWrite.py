import json

data={"name":"Rajeev sharma","website":"www.jbc.com"}
with open("C:\\Users\\spundir\\Desktop\\Python\\demo.json","w") as json_file:
    json.dump(data,json_file)

with open("C:\\Users\\spundir\\Desktop\\Python\\demo.json", "r") as json_file:
    data=json.load(json_file)
    data["website"]="vvvvv.in"
    print(data)

with open("C:\\Users\\spundir\\Desktop\\Python\\demo.json","w") as json_file:
    json.dump(data,json_file)