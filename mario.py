#----------- create a column and row using loops -------------#

def main():
    print_column(3)
    print_row(5)

def print_column(height):
    for _ in range(height):
        print("#")
              
def print_row(width):
    print("#" * width)
              
main()


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

mario()

#4:05:00 python