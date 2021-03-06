import random
import csv
import tkinter as tk
window = tk.Tk()
window.title("Password Manager(Generator)")
window.geometry("600x600")
#Password generator part
#heading password generator
title = tk.Label(text = "Password Generator",font =('Arial',20))
title.grid(column = 0,row = 0)
hintq1 = tk.Label(text = "Enter hint for the password:")
hintq1.grid(column = 0,row = 1)
hint1entry = tk.Entry()
hint1entry.grid(column = 1,row = 1)
key1q = tk.Label(text = "Enter your preferred key(between -40 and 10):")
key1q.grid(column = 0,row = 2)
key1 = tk.Entry()
key1.grid(column = 1,row = 2)

#hint = input("Enter the hint for where the password is applied:")
#n = int(input("Enter the number of characters required:"))
#key = int(input("Enter your key between -40 and 10:"))
#print("Your ciphered password have been added to csv")
#print("Your orginal password: ",end="")
#password = ""
#passwordcipher = ""
#for i in range(n):
#    x = random.randint(33,126)
#    password += chr(x)
#    passwordcipher += chr(x+key)
#print(password)
#with open("passwords.csv","w") as file:
#    writer = csv.writer(file)
#    writer.writerow([hint,passwordcipher])