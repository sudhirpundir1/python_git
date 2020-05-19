def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print('1.Addition')
print('2.Substraction')
print('3.Multiplication')
print('4.Divison\n')
func = int(input('Please enter value to perform the Operation: '))
a = int(input('Please enter value for a: '))
b = int(input('Please enter value for b: '))

if func == 1:
    s1 = add(a,b)
    print(s1)
elif func == 2:
    s1 = sub(a,b)
    print(s1)
elif func == 3:
    s1 = mul(a,b)
    print(s1)
elif func == 4:
    s1 = div(a,b)
    print(s1)
else:
    print('Invalid Options')