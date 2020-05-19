student={'name':'sudhir','age':32}
print(student['name'])
#adding a key value
student['gender']='male'
print(student)
# deletiong of perticular key value pairs:-
student.pop('name')
print(student)

#Clear/Del a dictionary
print(student.clear())

#update a value based on a key
students={'name':'sudhir','age':32}
students['name']='robin'
print(students)

#get length of dict
print(len(students))

#get length of dict
print(len(students))
#returns list of keys
print(students.keys())
#returns list of values
print(students.values())
#returns list of key-value tuple pairs
print(students.items())

for key in students:
    print(key,students[key])

for k, v in students.items():
    print(k,v)