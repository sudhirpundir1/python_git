numbers=[0,4,5,8,13,140]
for i in numbers:
    if i==0:
        print(f'This is Zero: {i}')
    elif i!=0 and i%2==0:
        print(f'Even Number: {i}')
    else:
        print(f'Odd Number: {i}')

##------
for i in range(4,20,2):
    print(i)