import random

class Hat:
    houses = ["Hufflepuff", "Gryffindor", "Slytherin", "Ravenclaw"]
        
    @classmethod
    def sort(cls,name):
        print(name, "belongs to House", random.choice(cls.houses))
    
name = input("Enter your name: ").capitalize()
Hat.sort(name)
