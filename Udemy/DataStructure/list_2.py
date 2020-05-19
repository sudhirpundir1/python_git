my_ips = ['192.87.00.198','176.98.123.90','198.12.90.188']
for i in my_ips:
    print(f'Connecting to: {i}')

##-----
list1 = [1,2]
list2= list1+[3,4]
print(list2)
list3= list2+ ['abc','xyz']
print(list3)
list3.append('xx')
print(list3)