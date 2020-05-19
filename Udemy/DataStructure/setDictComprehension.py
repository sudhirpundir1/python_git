names ={'tom','Anne','JOHN','dan'}
new_names = {n.title() for n in names}
#new_names = {n.capitalize() for n in names}
print(new_names)

#--Multiplying values by 2 method 1
d1={'a':1,'b':2,'c':3}
for k,v in d1.items():
    print(f'{k}:{v*2}')
# method 2
d2={k.upper():v*2 for k,v in d1.items()}
print(d2)

#----returns the key value pairs where value is divisible by 3

d2 = {k.upper():v for k,v in d1.items() if v % 3 ==0}
print(f'the new dictionary are {d2}')

##-------
