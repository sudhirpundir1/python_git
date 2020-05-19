numbers=list(range(1,11))
print(numbers)

doubled = []
for num in numbers:
    doubled.append(num*2)
print(doubled)

doubled_numbers =[num *2 for num in numbers]
print(doubled_numbers)
doubled_numbers_2 = [str(n) for n in numbers] # converting int to numbers
print(doubled_numbers_2)

#-------------------
#convert miles to KM
miles = [12, 10, 26, 80]

## 1 mile = 1.609 km

## YOUR CODE STARTS HERE
km = [k*1.609 for k in miles]
print(km)
