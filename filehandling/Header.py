import csv

def check_csv(file):
    with open(file,'r') as f:
        csvData = csv.reader(f,delimiter='|')
        header = next(csvData)
        print("The header of file : " , len(header))

check_csv("customers-100.csv")