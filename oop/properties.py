class student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name 
        self.house =  house
        
        
        def __str__(self):
            return f"{self.name} from {self.house}"

        
        @property
        def house(self): #getter
            return self._house
        
        @house.setter
        def house(self, house): #setter
            if house not in ["london", "lahore"]:
                raise ValueError("invalid house")
            self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("name: ")
    house = input("house: ")
    return student(name, house)

if __name__ == "__main__":
    main()
    
    
# property is a function in python
# decorators use to modify function 