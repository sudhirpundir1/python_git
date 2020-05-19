price=500
balance=90

if balance >= price:
    print(f'You can buy this product and new balance will be: {balance - price}')
else:
    print(f'Insufficient funds. Please deposit {price-balance}')

##------------
answer = input('Do you want to continue? Enter yes / no:')
if answer.lower() == 'yes':
    print('We\'ll move on')
    x=7
    print(x)
elif answer.lower() == 'no':
    print('We\'ll Stop here.')
else:
    print('Invalid answer. Please provide correct answer.')