#-String FUnctions
x='My name is Khan'
l1=[1,5,7,9,3]
print(len(l1))

print(x.lower())
print(x.upper())

#-Trim
ip= '  192.187.87.110    '
print(ip)
print(ip.strip())

str1= '$$$192.00.23.4$$'
print(str1.strip('$'))
#--Replace
ip=ip.strip()
print(ip.replace('.',':'))

#--Split method
str2='who1    Link encap:Ethernet  ip_add 192.34.00.187'
print(str2.split())
print(str2.split()[3])

#--Join method
str3='who1    Link encap:Ethernet  ip_add 192.34.00.187'
str3=str3.split()
print(str3)

str4=' '.join(str3)
print(str4)
str5='!'.join(str3)
print(str5)

#--In keyword
x='I am learning python'
y='python' in x
print(y)
w='PY' in x.upper()
print(w)
z='pythonn' not in x
print(z)
#####################
print(':'.join('abc'))


############
s1 = 'Python Java Go Ruby Rust'
x = s1.find('y')
print(x)