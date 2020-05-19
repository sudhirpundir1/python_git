letters=list('abcd')
print(letters)

#letters.clear()
print(letters)

letters.pop() # by default removes the last elements
print(letters)

letters.pop(0) #it will remove the first element
print(letters)

let= list('anmcdcbjaksdbjasl')
print(let)

while 'a'  in let:
    let.remove('a')  #-- to remove something from the list
print(let)


y=let.count('s')
print(f'Count of S in list are: {y}')

print(let.index('s')) ## only provide the index of 1st occurance.

