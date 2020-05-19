t1 =tuple(range(100))
print(t1)

x=10 ## Global Scope
def my_func():
    x=5  ##Local Scope
    print(f'x inside the function: {x}')

my_func()
print(f'x outside the function: {x}')

a=10
def my_func1(b):
    global a # Global keyword update the value of a
    a= a+b
    print(f'a inside the function: {a}')


my_func1(7)
print(f'a Outside the function: {a}')

