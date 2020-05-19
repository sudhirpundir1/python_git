#Write a program to check whether given string is palindrome or not.

def palindromCheck(myStr):
    str1 = myStr
    length = len(str1)
    str2=str1[length::-1]
    if str1.lower().strip() == str2.lower().strip():
        print('Given string is palindrom')
    else:
        print('Given number is not Palindrom')

palindromCheck('SOS')