x= range(1,26,1)
print(list(x))

my_sum=0
my_product=1
for i in range(1,26):
    my_sum=my_sum+i
    my_product=my_product*i

print(f'Sum of list is :{my_sum}')
print(f'Sum of list is :{my_product}')

