import random

n = int(input("Enter the number of characters required:"))
print("Your password: ",end="")
for i in range(n):
    x = random.randint(33,126)
    print(chr(x),end="")
print("")