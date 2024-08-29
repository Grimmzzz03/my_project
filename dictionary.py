# list of dictionaries
students = [
    {"name": "Yash", "age": 19, "course": "Btech"},
    {"name": "ashish", "age": 20, "course": "Btech"},
    {"name": "raj", "age": 21, "course": "Btech"},
    {"name": "rahul", "age": 22, "course": "Btech"}
]
for student in students:
    print(student["name"], student["age"], student["course"], sep=", ")