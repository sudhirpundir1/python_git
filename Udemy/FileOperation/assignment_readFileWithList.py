with open('original.txt','r') as file:
    content = file.read().split()
#    print(content)
newList =[]
for i in content:
    tmp = i.split(":")
    newList.append(tmp)
print(newList)