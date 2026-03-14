import csv

with open('customers-100.csv','r') as f:
    customersData =  csv.DictReader(f,delimiter='|')
    print(customersData)
    for customer in customersData:
        print(customer['Customer Id'])
