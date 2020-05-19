def my_function(name):
    '''
    This is my first function. It prints a string.
    '''
    print("Hello Python World...!"+'My Name is:'+ name)

def function1(x,y):
    print(f'1st argument:{x}')
    print(f'2nd argument:{y}')

function1(55,'Python')
my_function('Sudhir')

print(my_function.__doc__)