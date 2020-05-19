#4. Write a program to find common characters from below strings.  "SMASH", "FLASH"
str1, str2 = "SMASH", "FLASH"
commonChar =''
for i in str1:
    if i in str2 and i not in commonChar:
        commonChar= commonChar+i
print(commonChar)


#------------------