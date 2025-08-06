# ---------------------------------------------------------------------------------
# create a simple test case where main is only execute if its excist 

def main():
    x = int(input("Entert he value of x? "))
    print("Square of x is: ", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
