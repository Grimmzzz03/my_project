class student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.marks)

    def on_a_honor(self):
        if self.marks >= 90:
            print("honor roll")
        else:
            print("not a honor roll")


s1 = student("sachin", 23, 90)
s1.display()
s1.on_a_honor()
s2 = student("rahul", 24, 80)
s2.display()
s2.on_a_honor()
s3 = student("peter", 25, 70)
s3.display()
s3.on_a_honor()
