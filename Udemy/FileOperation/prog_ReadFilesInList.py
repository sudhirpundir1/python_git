with open('C:\\Talend Training\\Output\\EMP_Normalise.txt','r') as file:
    content = file.read().splitlines()
    print(content)

with open('C:\\Talend Training\\Output\\EMP_Normalise.txt','r') as file:
    content = file.readlines()
    print(content)

with open('C:\\Talend Training\\Output\\EMP_Normalise.txt','r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open('C:\\Talend Training\\Output\\EMP_Normalise.txt') as file:
    for lines in file:
        print(lines, end='')