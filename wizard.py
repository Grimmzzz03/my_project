class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

class Student(Wizard):
    def __init__(self,name, house, patronus):
        super().__init__(name)
        if house not in ['gryffindor','hufflepuff','slytherin','ravenclaw']:
            raise ValueError("Invalid house")
        self.house = house
        self.patronus = patronus

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        if not subject:
            raise ValueError("Subject cannot be empty")
        self.subject = subject



