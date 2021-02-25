import csv

hint = input("enter hint for the password:")
key = int(input("Enter key given in passwordgenerator.py:"))

with open("passwords.csv","r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if(row[0] == hint):
            ciphered = split(row[1])
            for letter in ciphered:
                value = ord(letter)
                value -= key
                print(chr(value),end="")
print("")
def split(word):
    return [char for char in word] 
