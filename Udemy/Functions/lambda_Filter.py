##---Write a programm to filter out the even number from the given list:-
def is_even(n):
    return n%2 ==0
nums = [2,5,7,10,6,4]
even = list(filter(is_even, nums))
print('without Lambda-->',  even)

#---2nd way -- using Lambda Func
even = list(filter(lambda n : n%2==0,nums))
print('Using Lambda method-->',even)