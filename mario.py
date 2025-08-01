#----------- create a column and row using loops -------------#

def main():
    print_column(3)
    print_row(5)

def print_column(height):
    for _ in range(height):
        print("#")
              
def print_row(width):
    print("#" * width)
              
# main()


#--------------------- Create a square using loops ---------------------#


def mario():
    print_square(5)
    mario_square(5)

def print_square(size):
    # iterate through the rows
    for i in range(size):
        # for each row, iterate through the columns
        for j in range(size):
                # print a hash symbol for each column in the row
                print("#", end="")
        # create a new line after each row
        print()  
        
def mario_square(size):
    for i in range(size):
        # print a row of hashes
        print("*" * size)

# mario()



#----------------------- Python Loops -----------------------#

#-------------- Print Odd Numbers --------------#

def odd_num():
    for i in range(1,21):
        if i % 2 == 0:
            print(i, end=" ")
        
        print("\n---------------------------------------------------------------------------")

# odd_num()

#-------------- sum of numbers divided by 3 or 5 --------------#

def sum():
    total = 0
    for i in range(1, 50):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            total += i
    print("Total:", total)

# sum()

#------------------------- Prime Numbers -------------------------#

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers():
    for i in range(1, 50):
        if is_prime(i):
            print(i)
# prime_numbers()   


#----------------------- Create Table -----------------------#

def table():
    number = int(input("Enter a number to create a multiplication table: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        
# table()

#----------------------- vowel --------------------------

def vowels():
    letters = ["a","e","i","o","u"]
    get_string = input("Enter a string: ")
    
    for i in get_string:
        for j in letters:
            if i == j:    
                print(i)
    
vowels()       
     