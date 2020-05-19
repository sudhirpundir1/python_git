# Write a program to find total number of elements that are exactly divisible by 10 from below array  [22, 50, 80, 20, 46, 5]
l1 = [22, 50, 80, 20, 46, 5]
total = 0
l2 =[]
for i in l1:
    if i % 10 == 0:
        total = total+1
        l2.append(i)
print(f'total number of elements that are exactly divisible by 10: {total}')
print(l2)
#------------------------

