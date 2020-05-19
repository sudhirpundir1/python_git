person={'name':'John','age':30,'grades':[7,9,10]}
print('name' in person)
person_keys = list(person.keys()) # converting tuple to list
person_values = list(person.values()) # converting tuple to list
print(person_keys)
print(person_values)
print(person.items())   #Returns tuple
Person_Item_List = list(person.items())
print(Person_Item_List)