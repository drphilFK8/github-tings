#classes

class Doodad:
    def __init__(self, name , age , DOB, Sex):
        self.name = name
        self.age = age
        self.date_of_birth = DOB
        self.sex = Sex


person1 = Doodad("Philip", 18, "May 13", "Male")

print(person1.name)