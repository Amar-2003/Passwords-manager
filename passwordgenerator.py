import random
import csv
import tkinter as tk
#Functions
def password_generator():
    hint1 = str(hint1entry.get())
    n = int(digits.get())
    key1 = int(key1entry.get())
    password = ""
    passwordcipher = ""
    for i in range(n):
        x = random.randint(33,126)
        password += chr(x)
        passwordcipher += chr(x+key1)
    password1 = tk.Label(text = "Your password for the hint "+hint1+" is "+password)
    password1.grid(column = 0,row = 5)
    with open("passwords.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow([hint1,passwordcipher])
    csvresult = tk.Label(text = "Your ciphered password have been stored ")
    csvresult.grid(column = 0,row = 6)
    

window = tk.Tk()
window.title("Password Manager(Generator)")
window.geometry("600x600")
#Password generator part
#heading password generator
title = tk.Label(text = "Password Generator",font =('Arial',20))
title.grid(column = 0,row = 0)
#getting hint for password
hintq1 = tk.Label(text = "Enter hint for the password:")
hintq1.grid(column = 0,row = 1)
hint1entry = tk.Entry()
hint1entry.grid(column = 1,row = 1)

#getting key for password
key1q = tk.Label(text = "Enter your preferred key(between -40 and 10):")
key1q.grid(column = 0,row = 2)
key1entry = tk.Entry()
key1entry.grid(column = 1,row = 2)

#getting number of digits for password
digitsq = tk.Label(text= "The number of digits required:")
digitsq.grid(column = 0,row = 3)
digits = tk.Entry()
digits.grid(column = 1,row = 3)

#button for creating password
btn1 = tk.Button(text = "Create a password",command = password_generator)
btn1.grid(column = 1,row = 4)


window.mainloop()
#hint = input("Enter the hint for where the password is applied:")
#n = int(input("Enter the number of characters required:"))
#key = int(input("Enter your key between -40 and 10:"))
#print("Your ciphered password have been added to csv")
#print("Your orginal password: ",end="")

#print(password)
#