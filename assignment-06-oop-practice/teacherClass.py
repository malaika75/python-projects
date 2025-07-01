class Person:
    def __init__(self , name):
        self.name = name

class Teacher(Person):
    def __init__(self, name , subject):
        super().__init__(name)
        self.subject = subject


teacher1 = Teacher("hamza syed" , "python")
print(f"{teacher1.name}  is teaching us {teacher1.subject}")