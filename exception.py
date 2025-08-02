while True:
    try:
        x = int(input("Enter the value of x? "))
    except ValueError:
        print("x is not a interger")
    else: 
        break
print(f"value of x is {x}")
