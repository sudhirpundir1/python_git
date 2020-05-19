person={'name':'John','age':30,'grades':[7,9,10]}
for k in person.keys():
    print(f'Keys are: {k}')

for v in person.values():
    print(f'Values are: {v}')

for k,v in person.items():
    print(f'key: {k}, value: {v}')