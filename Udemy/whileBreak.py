while True:
    guess = input('Guess the lucy number between 1 & 10:')
    if int(guess)==8:
        print('You WOn..!')
        break
    print(f'{guess} was not a lucky number')