#String Slicing
my_str = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
mac=my_str.split(' ')[-1]
print(mac)
movie='The Godfather' ;
print(movie[5])
print(movie[-2])

print(movie *5)

print(movie[0:2])

print(movie[2:6])

print(movie[:2])
print(movie[4:])
print(movie[0:10:2])
print(movie[::-1])
print(movie[:2]+movie[2:])
print(movie[:6]+movie[6:])

print(movie[-2:])

print(movie[99:])