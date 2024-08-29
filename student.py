class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade


student1 = Student("suresh", 1, "A")
print(student1.roll_no)
