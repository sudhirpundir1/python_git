os=['Windows', 'Linux','Mac','Android']

for item in os:
    print(f'The name of the item in list is: {item}')
##-- with Reversed Method
for item in reversed(os):
    print(f'-->The name of the item in list is: {item}')
##-- with Sorted Method
for item in sorted(os):
    print(f'***The name of the item in list is: {item}')

##------
str1='I learn Python Programming'
for char in str1:
    print(char, end='-')


