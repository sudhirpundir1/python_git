def fibbo(n):
    '''Fibonacchi Series Sum'''
    a =0
    b =1
    c =0
    if n < 0 :
        print('Invalid Input')
    elif n == 0:
        return (a)
    elif n == 1:
        return(b)
    else:
        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return(c)

s1 = fibbo(100)
print(s1)
#-------------------------------------
a=int(input("Enter the terms"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s
        print(next,end=" ")
        f=s
        s=next