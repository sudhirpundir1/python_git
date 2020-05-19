my_sum=0
for i in range(1,100,2):
    my_sum=my_sum+i
print(my_sum)

##--------

## Solution 1
my_sum = 0
x = 100
while x:
    if x % 2 != 0:
        my_sum += x
    x -= 1

print(my_sum)
#######################

## Solution 2
my_sum = 0
x = 100

while x:
    x -= 1
    if x % 2 == 0:
        continue
    my_sum += x

print(my_sum)
#######################