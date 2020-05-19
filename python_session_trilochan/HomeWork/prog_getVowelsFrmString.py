#3. Write a program to find total no of vowels from below string
my_str = "You learn more from failure than from success"
vowelList = 'aeiou'
t1 = 0
for c in my_str:
    if c in vowelList:
        t1 = t1+1
print(f'tota number of vowels in str is: {t1}')