from functools import reduce
#1: FIlter out all even values from given list and create even[]
#2: Now multiply even number by 2 and make double[]
#3: Add all evements of the double list
def is_even(n):
    return n%2==0

def double(x):
    return x*2

def add_all(a,b):
    return a+b

nums = [4,8,5,7,12,3,6,19,22]
even= list(filter(is_even,nums))
print('even list are:',even)

double = list(map(double,even))
print('Even no*2:',double)

sum = reduce(add_all,double)
print(sum)

#-------
print('\n***Using Lambda method - Implementation***\n')
even1 = list(filter(lambda n : n% 2==0,nums))
print(even1)
double1 = list(map(lambda x : x*2,even1))
print(double1)
sum1 = reduce(lambda a,b : a+b,double1)
print(sum1)