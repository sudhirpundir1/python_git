person={'name':'John','age':30}
person['city']='Berlin'
print(person)
person['city']='London'
print(person.get(5,'Key doent exist')) #default message in case of Key doent exist
print(person.get('city','Key doent exist'))
del person['age']
print(person)
print(person.pop('age', 'no key')) #default value in case of key doesnt exist

print(len(person))

person.clear()
print(person)