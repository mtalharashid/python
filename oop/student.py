def main():
    student = get_student()
    if student["name"] == "padma":
        student["house"] = "ravenlaw"
    print(f"{student["name"]} from {student["house"]}")

def get_student():
    name = input("name: ")
    house = input("hosue: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()

# Using dictionaries for better semantics and readability
# Immutable tuples cannot be changed, but lists can be used instead.