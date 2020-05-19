def sum1(a,b):
    sum = a+b
    print(f'Sum: {sum}')

def sum2(a,b):
    sum = a+b
    return sum

def sum_and_product(a,b):
    sum = a+b
    return sum,a*b

sum1(3,9)

s= sum2(12,54)
print(f'The return sum from the function is : {s}')

sum,product = sum_and_product(8,6)
print(f'The return sum from the function is : {sum}')
print(f'The return product from the function is : {product}')