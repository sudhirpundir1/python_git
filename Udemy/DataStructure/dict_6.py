person={'name':'John','age':30,'grades':[7,9,10]}
p1={'location':'Berlin','job':'developer'}

person.update(p1)

print(person)

########------------
money = {
    'bank': 8564.61,
    'paypal': 1998.21,
    'cash': 480,
    'payoneer': 250.5
}

## YOUR CODE STARTS HERE

# Use a for loop to iterate over the dictionary and calculate the total amount.
# Save it to a variable called total_amount and print its value!
total_amount = 0
for v in money.values():
    total_amount = total_amount + v

print(total_amount)
