# List of strings
subject = ["physics", "chemistry", "maths", "hindi"]

# List of ints
games = ["football","cricket","tenis"]

#append
subject.append("history")
print(subject)
#insert
games.insert(1,"snooker")
print(subject)
#extend
subject.extend(games)
print(subject)
#remove
subject.remove('chemistry')
print(subject)
#reverse
subject.reverse()
print(subject)

subject.__delitem__(2)
print(subject)