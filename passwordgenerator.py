import random
import csv
key = int(input("Enter your key between -10 and 10:"))
hint = input("Enter the hint for where the password is applied:")
n = int(input("Enter the number of characters required:"))
print("Your ciphered password have been added to csv")
print("Your orginal password: ",end="")
password = ""
passwordcipher = ""
for i in range(n):
    x = random.randint(33,126)
    password += chr(x)
    passwordcipher += chr(x+key)
print(password)
with open("passwords.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow([hint,passwordcipher])