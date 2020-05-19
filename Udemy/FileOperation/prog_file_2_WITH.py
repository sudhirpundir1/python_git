with open('C:\\Talend Training\\Output\\EMP_Normalise.txt','r') as file:  #with automatically close the file.
    print(file.read())

print(file.closed)      #USING with keyword automatically close the file.