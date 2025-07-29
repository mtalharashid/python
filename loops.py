#---------------------- While Loops ----------------------#
# This script demonstrates the use of while loops in Python.

i = 3
while i != 0:
    print("Current value of i:", i)
    i -= 1


#---------------------- For Loop ----------------------#
for i in (0, 1, 2, 3, 4, 5):
    print("using for loop in python:", i)
    
for i in range(3):
    print("using range in for loop:", i)
    
#---------------------- Nested Loops ----------------------#
for i in range(3):  
    for j in range(2):
        print("Nested loop iteration i:", i, "j:", j)   
        
        
#---------------------- Loop with Break ----------------------#
for i in range(5):  
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("Loop iteration:", i)     
    
#---------------------- Loop with Continue ----------------------#
for i in range(5):  
    if i == 2:
        print("Skipping the iteration at i =", i)
        continue
    print("Loop iteration:", i)     
    
#---------------------- Loop with Else ----------------------#
for i in range(3):
    print("Loop iteration with else:", i)
else:   
    print("Loop completed without break")       
    
#---------------------- Loop with Else and Break ----------------------#
for i in range(3):
    if i == 1:
        print("Breaking the loop at i =", i)
        break
    print("Loop iteration with else and break:", i) 
else:
    print("This will not be printed because the loop was broken")
    
#---------------------- print using multiply value ----------------------#
print("Print \n" * 3)
print("use end \n" * 3, end="")

#-------------- Ask user to enter an integer and print it --------------#
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    
for i in range(n):
    print("meaow ")
    
#------------- Create function and use loop -----------------

def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("how many time cat say meow? "))
        if n > 0:
            break
    return n

def meow(n):
    for i in range(n):
        print("meow")
        
main()
        
#---------------- List in python -----------------

Students = ["Ali", "Ahmed", "Sara", "Fatima"]
print(Students[0])
print(Students[1])
print(Students[2])
print(Students[3])

for student in Students:
    print("Student in the list:", student) 
    

#----------------------Dictionary in Python-----------------------


for i in range(len(Students)):
    print("Student at index", i + 1, "is", Students[i])


students = [
    {"name": "Ali", "age": 20},
    {"name": "Ahmed", "age": 22},
    {"name": "Sara", "age": 19},
    {"name": "Fatima", "age": 21}
]

for student in students:
    print("Student Name:", student["name"], "Age:", student["age"])

