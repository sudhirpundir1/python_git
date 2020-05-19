chelse='keep the blue flag flying high'
#length of a string
print(len(chelse))
print(chelse.__len__())
#print index of a perticular character
print(chelse.index('b'))
#to get the count of a character
print(chelse.count('f'))
#slicing
print(chelse[0:4])

#reverse string
print(chelse[::-1])
#upper case
print(chelse.upper())
#repetition
print(chelse*2)
#concatenation
print(chelse+" Lampard")

#Membership Testing
if 'z' not in chelse:
    print("it is not a element")

if 'k' in chelse:
    print("it is a element")