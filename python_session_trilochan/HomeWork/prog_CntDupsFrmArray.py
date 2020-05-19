#Write a program to count total number of duplicate elements from below array  [22, 15, 63, 45, 15, 81, 22, 12]

l1 =  [22, 15, 63, 45, 15, 81, 22, 12]
l1_len = len(l1)
s1 = set(l1)
s1_len = len(s1)
dups = l1_len - s1_len
print(dups)
#for i in l1:
