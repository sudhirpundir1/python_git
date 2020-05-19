import sys

t1 = tuple(range(100001))
l1 = list(range(100001))
print(t1)
print(l1)

languages = ('Python', 'Java', 'Go', 'C++', 'PHP', 'Scala', 'Solidity')

## Using a negative index extract the last element of the tuple in a variable called x
x = languages[-1]
print(x)
## Return a new tuple called y using slicing and a step
## y should be ('Python', 'Scala')
y = languages[::5]
print(y)
