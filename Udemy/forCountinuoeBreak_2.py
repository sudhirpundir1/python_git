## for ... continue -> it prints out all letters of the string without 'o'
for letter in 'Python Go and Java Cobol':
    if letter == 'o':
        continue  # go to the beginning of the for loop and do the next iteration
    print(letter, end='')

## for ... break
sequence = [1, 5, 19, 3, 31, 100, 55, 34]
for item in sequence:
    if item % 17 == 0:
        print('A number divisible by 17 has been found! Breaking the loop...')
        break  # breaks out of the loop (executes the first instruction (if any) after the else block of code)
else:
    print('There is no number divisible by 17 in the sequence')