a = 9
b = int(input('please provide value for b: '))

try:
    c = a/b
except ZeroDivisionError as e:
    print('Exception Occured :', e)
except TypeError as e:
    print('Exception Occured :',e)
except:
    print('Exception Occured')
else:
    print('No exception')
    print("value of C: ",c)
print('Another block of code...Continued Execution...!')
for i in range(10):
    print(i, end=' ')

