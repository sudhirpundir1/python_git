x= lambda x:x*2
print(x(5))
#-----------
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
#--
new_list1 =[]
for i in my_list:
    if i % 2 == 0:
        new_list1.append(i)
print(new_list1)
