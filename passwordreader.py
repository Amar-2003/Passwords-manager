import csv
hint = input("enter hint for the password:")
with open("passwords.csv","r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if(row[0] == hint):
            print(row[1])