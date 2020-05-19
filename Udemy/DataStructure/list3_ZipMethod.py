name = ['Edwin','Bob','Sandy', 'Michal']
age = [24,21, 65, 32]
hobby = ['Cooking', 'Cricket', 'Cycling', 'Reading']

for n,a,h in zip(name, age, hobby):
    print(n+' is '+str(a)+' year old. His hobby is '+h)