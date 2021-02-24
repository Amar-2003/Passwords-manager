import random
import csv
hint = input("Enter the hint for where the password is applied:")
n = int(input("Enter the number of characters required:"))
print("Your password: ",end="")
password = ""
for i in range(n):
    x = random.randint(33,126)
    password += chr(x)
print(password)
with open("passwords.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow([hint,password])