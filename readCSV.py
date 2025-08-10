# with open("name.csv") as file:
#     for line in file:

        # row = line.rstrip ().split(",")
        # print(f"{row[0]} is in {row[1]}")

        # name, house = line.rstrip ().split(",")
        # print(f"{name} is in {house}")
        
# ---------------------------------- Save data into Dictionary ----------------------

students = []

# with open("name.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {} # create an empty dictionary 
#         student = {"name": name, "house": house}
#         students.append(student)
        
        
# def get_name(student): #to sort student dict by name 
#     return student["name"]

# def get_house(student): #to get sorted by house
#     return student["house"]
        
# for student in sorted(students, key=lambda student: student["name"]): #lambda use for unknown function 
#     print(f"{student['name']} is in {student['house']}")

# ---------------------------------- Using CSV Library ------------------------------

import csv

with open("name.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")