a = 9
b = int(input('Please provide value for B: '))
try:
    c = a/b
except:
    print('Exception Occured...!')
else:
    print(f'C : {c}')

print('other code starts here...Continued execution.')
for x in range(10):
    print(x, end=' ')