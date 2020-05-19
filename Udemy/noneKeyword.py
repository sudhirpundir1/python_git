a=bool(None)
print(a)

print(type(None))

def f1(a=None):
    if a:
        print(f'a is {a}')
    else:
        print('Function called without args')
        print(f'a is {a}')

f1(4)
f1()