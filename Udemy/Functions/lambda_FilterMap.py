#1: FIlter out all even values from given list
#2: Now multiply even number by 2
def is_even(n):
    return n%2==0
def double(x):
    return x*2
nums = [4,8,5,7,12,3,6,19,22]
even= list(filter(is_even,nums))
print('even list are:',even)
double = list(map(double,even))
print('Even no*2:',double)

#-------
print('\n***Using Lambda method - Implementation***\n')
even1 = list(filter(lambda n : n% 2==0,nums))
print(even1)
double1 = list(map(lambda x : x*2,even1))
print(double1)
