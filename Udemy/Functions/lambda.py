#-filter() takes an iterable, calls the lambda function on each item, and returns the items where the lambda returned True.
str = ['Python', 'programming', 'is', 'awesome!']
a=sorted(str)
print(a)

str2 = sorted(str, key=lambda i : i.lower())
print(str2)
#---------
str3= list(filter(lambda i : len(i)<8,str))
print(str3)

#--
def is_less_than_8_characters(item):
    return len(item) < 8
results= []
for item in str:
    if is_less_than_8_characters(item):
        results.append(item)

print(results)