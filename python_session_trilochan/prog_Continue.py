#break...!
for number in range(10):
    if number ==7:
        break
    print(number)

#continue...!
for number in range(10):
    if number ==7:
        continue
    print(number)

#break
l1 = [5,10,15,20]
l2 = [10,20,30]
for i in l1:
    for j in l2:
        if j == 20:
            break
        print(i*j)
    print('this is a nested loop')
