class Dog:
    def __init__(self):
        self.name = "shyro"
        self.breed = "dog"


    def bark(self):
        print(f"{self.breed} {self.name} bark bark....")


dog1 = Dog()
dog1.bark()