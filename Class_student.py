# Class= OOPS
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} from {self.house} has {self.patronus} patronus"
    
    @classmethod
    def get(cls):
        name = input("Name: ").capitalize()
        house = input("House: ").capitalize()
        patronus = input("Patronus: ").capitalize()
        return cls(name, house, patronus)
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, value):
        if value not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = value
    
        
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Strange"
            case "Otter":
                return "Wild"
            case "Fox":
                return "Crazy"
            case "Centipede":
                return "Evil"
            case _:
                return "Unkown"
            
                    
def main():
    student = Student.get()
    print(student)
    print("expecto patronum")
    print(student.charm())
    
if __name__ == "__main__":
    main()
