#Suppose we have a list of integers >>> numbers = [1, 2, 3, 4, 5, 6]
#1.What do we need to do add 5 to each number?
#2.What if we want to add 5 to only the second to the fifth number?
#3.What if we want to add 5 to numbers with an even-numbered offsets?
res2 = []
l1 = [1, 2, 3, 4, 5, 6]

res = [x+5 for x in l1]
print(f'after adding 5 to each element: {res}')

#------------------------
for x in l1:
    if x/2 == 0:
        x = x+5
        res2.append(x)
    else:
        x
        res2.append(x)
print(res2)