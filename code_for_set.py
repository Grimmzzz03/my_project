#code for set
# Refactored code
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Neville", "house": "Gryffindor"},
    {"name": "Luna", "house": "Ravenclaw"}
]

houses = sorted(set(student["house"] for student in students))

for house in houses:
    print(house)
    
    