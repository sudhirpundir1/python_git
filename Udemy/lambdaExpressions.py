'''Anonymous func'''
def square(x):
    return x**2

sq = lambda x=1: x**2

print(sq(5))
print(sq())

sum_1 =lambda x,y: x+y
print(sum_1(5,9))
#--------------------

def my_func(x, fn):
    return fn(x)


result = my_func('a:b:c', lambda x: x.split(':'))
print(result)
