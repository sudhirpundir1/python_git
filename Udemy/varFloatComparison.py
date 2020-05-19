from math import isclose
a=0.0000001
b=0.0000002
x=999999.01
y=999999.02

z=isclose(a,b,rel_tol=0.001,abs_tol=0.001)
w=isclose(x,y,rel_tol=0.001,abs_tol=0.001)
print(z)
print(w)

#to show the value in 29 decimal
print(format(a,'.29f'))