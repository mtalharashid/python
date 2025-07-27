# ---------------- greater then or Equal Condition in python ---------------

x = int(input("What is the value of x? "))
y = int(input("what is the value of y? "))

if x > y:
    print("x is greater then y")
elif x < y:
    print("y is greater then x")
else:
    print("y is equal to x")

#------------------------------ OR Condition --------------------------------

if x > y or x < y:
    print("x is not equal to y")


#------------------------------ not equal to Condition --------------------------------

if x != y:
    print("x is not equal to y")


# -------------------- check Score program ------------------------------------

# Ask the user to enter their marks
marks = int(input("Enter your marks (0-100): "))

# Check if marks are within a valid range
if marks < 0 or marks > 100:
    print("Invalid input! Marks should be between 0 and 100.")
else:
    # Grade logic using all comparison operators
    if marks == 100:
        print("Perfect Score! Your grade is A+")
    elif marks >= 90 and marks != 100:
        print("Excellent! Your grade is A")
    elif marks >= 80 and marks < 90:
        print("Very Good! Your grade is B")
    elif marks >= 70 and marks < 80:
        print("Good! Your grade is C")
    elif marks >= 60 and marks < 70:
        print("Fair! Your grade is D")
    elif marks > 50 and marks < 60:
        print("Passed! Your grade is E")
    elif marks <= 50 and marks != 0:
        print("Sorry, you have failed. Your grade is F")
    elif marks == 0:
        print("You scored zero. Were you even present? Grade: F")

