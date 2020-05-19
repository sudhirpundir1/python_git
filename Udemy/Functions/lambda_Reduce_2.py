from functools import reduce
str = ['Python', 'programming', 'is', 'awesome!']
result = reduce(lambda val1, val2: val1 + val2, str)
print(result)
