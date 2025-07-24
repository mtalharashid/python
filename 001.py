# write my first python code and print "Hello World"
print("Hello World")

# get user name and greet them
name = input("whats your name? ")
# print("Hello " + name)

""" this is a comment"""

# get user age and print it
age = input("whats your age? ")
print("Hello", name ,"You are", age, "years old.")
# the comma add a space between the strings and the variable

# using print function with multiple arguments and separator using sep
print("Hello", name ,"You are", age, "years old.", sep=" -- ")

# using print function with end argument
# this will print "Hello" and then stay on the same line
print("Hello", name , end=" ")
print("You are", age, "years old.")


# using f-string to format the string
print(f"Hello {name}, You are {age} years old.")    

# remove white spaces from the string
name = name.strip()
# print the name in uppercase

print(name.upper())     

# print the name in lowercase
print(name.lower())     

# print the name in title case
print(name.title())

# print the name in reverse order
print(name[::-1])

# print the length of the name
print(len(name))



