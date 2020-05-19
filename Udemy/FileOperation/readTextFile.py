f = open('C:\\Talend Training\\Output\\EMP_Normalise.txt','r')  #default mode is read only mode # t is for the text file
content = f.read()
print(content)
x=content.split('\n')
print(x)
f.close()
print(f.closed)
#2 types of file
#binary file: photo, exe, video
#text file: .txt,.csv, data file