#-map() automatically calls the lambda function on all the items, effectively replacing a for loop like the following:
results = []
str = ['Python', 'programming', 'is', 'awesome!']
for item in str:
    results.append(item.upper())

print(results)
#--2nd way using lambda
results1 = list(map(lambda item : item.upper(),str))
print(results1)