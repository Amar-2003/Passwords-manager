import random
import csv
import tkinter as tk
#******************************Functions****************************************


#Function for generator
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
    password1.grid(column = 2,row = 3)
    with open("passwords.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow([hint1,passwordcipher])
    csvresult = tk.Label(text = "Your ciphered password have been stored ")
    csvresult.grid(column = 2,row = 2)

#Function For reader
def password_reader():
    with open("passwords.csv","r") as file:
        csvreader = csv.reader(file)
        key2 = int(key2entry.get())
        hint2 = str(hint2entry.get())
        password = ""
        for row in csvreader:
            if(row[0] == hint2):
                ciphered = list(row[1])
                for letter in ciphered:
                    value = ord(letter)
                    value -= key2
                    password += chr(value)
    password2 = tk.Label(text = "Your password for the hint "+hint2+" is "+ password)
    password2.grid(column = 2,row = 9)
                    
    

window = tk.Tk()
window.title("Password Manager")
#window size
window.geometry("800x900")
#*************************Password generator**********************************
#heading password generator
title1 = tk.Label(text = "Password Generator",font =('Arial',20))
title1.grid(column = 1,row = 0)
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

#*************************Password Reader*************************************

#title
title2 = tk.Label(text = "Password Reader",font = ('Arial',20))
title2.grid(row = 5,column = 1)

#Getting hint
hintq2 = tk.Label(text = "Enter hint for password:")
hintq2.grid(column = 0,row = 6)
hint2entry = tk.Entry()
hint2entry.grid(column = 1,row = 6)
#getting key
key2q = tk.Label(text = "Enter the key:")
key2q.grid(column = 0,row = 7)
key2entry = tk.Entry()
key2entry.grid(column = 1,row = 7)
#Button
btn2 = tk.Button(text = "Get password",command = password_reader)
btn2.grid(column = 1,row = 8)



window.mainloop()

