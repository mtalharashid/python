#create a simple calculator that adds two numbers
#im using integers for simplicity

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Result:", x + y)

#------------- FLOAT VERSION -------------

x = float(input("Enter the first float number: "))
y = float(input("Enter the second float number: "))

#print float value
print("Result:", x + y)

# print float value with nearest integer using round 
print("Result:", f"{round(x + y): ,}")

# divide two numbers in python
print("divide two  numbers")
x = float(input("Enter the first float number: "))
y = float(input("Enter the second float number: "))

#print float value
print("Result:", x / y)
print("Result:", round(x / y))
