#Immutable  ... We can not modify tuple after initialization...!
tuple1 = tuple()
tuple2=()
tuple3=(1,2,3)
my_tuple = (1,2.3, 'string',(1,2,3),[5,6,'abc'])

tuple5=(4.5,)
print(tuple5)

print(my_tuple[4]) # 5th index of my_tuple

print(my_tuple[4][2]) # now access the 3rd element of the list

#tuple[1]=55 # we can update /modify tuple.