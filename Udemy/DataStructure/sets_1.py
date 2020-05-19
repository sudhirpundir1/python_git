s1=set()  #Its a set

s1={}  ##-- Its a blank dictionary
print(type(s1))

s2={1,4.5,'abc'}
print(s2)
s3={1,3.4,(1,4,'s')}
print(s3)
#s4={1,2,[1,2,3]} #We can not assign list in between set
#print(s4)

l1=[1,2,4,6,2,2]    #sets removes the duplicate values
t1=(1,1,55,66,77,55)
s3=set('Python Programming is cool!!!')
s1=set(l1)
print(s1)
s2=set(t1)
print(s2)
print(s3)

print(len(set(s1)))

for item in s2:
    print(item)

sx={1,'abc',5.3,'xx'}
print(sx)

z1=1 in sx
print(z1)
z2='x' in sx
print(z2)
z3='xx' in sx
print(z3)