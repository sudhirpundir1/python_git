s1={1,2,3}

print(s1.isdisjoint(s2)) # return true if any element is not common among both sets

set1 = {1,3,5}
set2= {9,5,7}
set3 = {6,7}
set4 = {6,7,8}
print(set3<=set4)

s2={3,4,5,6}
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)

print(s1.symmetric_difference(s2))

print(s1.union(s2))

print(s1.intersection(s2))