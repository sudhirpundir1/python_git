
import csv

with open("C:\\Users\\spundir\\Desktop\\Python\\names.csv",'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    #    next(csv_reader)        #skip header
    with open("C:\\Users\\spundir\\Desktop\\Python\\new_names.csv",'w') as new_file:
        csv_Writer=csv.writer(new_file,delimiter='\t')

        for lines in csv_reader:
            print(lines)
            csv_Writer.writerow(lines)
            #print(lines)