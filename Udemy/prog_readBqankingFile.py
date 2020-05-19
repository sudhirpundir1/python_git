with open('banking.txt') as file:
    content = file.read().splitlines()
    print(content)
    diposit,withdraws =0,0
    for i in content:
        tmp = i.split(':')
#        print(tmp)
#        print(tmp[0])

        if tmp[0] == 'D':
           diposit = diposit+int(tmp[1])

        elif tmp[0] == 'W':
            withdraws = withdraws+int(tmp[1])
        else:
            print('Invalid Format')
    balance = diposit - withdraws
    print(balance)