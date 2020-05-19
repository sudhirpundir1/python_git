#CHeck for input name whether thats a part of existing list of Banned player or not. if not then create another list for new player.

bannerdPlayers = ['John','Adam','Tom', 'Jack']
playerList = []
playerName =''
while True= 'quite':
    playerName = input('Please add player Name or Enter "quite" to Exit : ')
    if playerName.title() not in bannerdPlayers and playerName.title() != 'quite':
        playerList.append(playerName.capitalize())
    else:
        print(f'Input Player is the banned player :{playerName.title()}')
else:
    print("You Choosed to exit")
print(playerList)