names1= ['John','Dan','Marry','sherry']
names2= ['Tim','Steve','Dan','John', 'Sherry']

name_in_both_list= [name for name in names1 if name in names2]
print(name_in_both_list)

'''Needs to fix the code to work with case'''

name1_lower = [n.lower() for n in names1]
name2_lower = [n.lower() for n in names2]
print(name1_lower)
print(name2_lower)

name_in_both_list2= [name for name in name1_lower if name in name2_lower]
print(name_in_both_list2)
