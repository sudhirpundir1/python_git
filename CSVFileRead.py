import csv

with open("C:\\Users\\spundir\\Desktop\\Python\\names.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file,delimiter=',')
    #    next(csv_reader)        #skip header

    for lines in csv_reader:
        print(lines)