class student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["london", "new york"]:
            raise ValueError("Missing house")
        self.name = name 
        self.house =  house
        
        def __str__(self):
            return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    # print(student)

def get_student():
    name = input("name: ")
    house = input("house: ")
    return student(name, house)

if __name__ == "__main__":
    main()
    
    
# declair an object in python