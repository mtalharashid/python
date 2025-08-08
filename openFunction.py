name = input("Whats your name: ")

# the letter w is create a new file each time user run this program
# file = open("name.txt", "w")

# the letter "a" append new record into the exciting file 
# Using f string to store data in a readable formate by using \n 

with open("name.csv", "a") as file:
    file.write(f"{name}\n")


# -----------------------------------------------------------------------------------------------------------------
# ---------------------------------------------READ FROM FILE------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
    
# Read Name form "name.txt" file

with open("name.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
     print("Hello, ", line.rstrip())
     
print("---------------------------------- Print Method 1 -------------------------------------------")

# --------------------------------------- Alternative Method -------------------------------------

names = []

with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
    
print("---------------------------------- Print Method 2 -------------------------------------------")


# --------------------------------------- Make it more short -------------------------------------

with open("name.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
        
print("---------------------------------- Print Method 3 -------------------------------------------")

