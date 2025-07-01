class Student:
    def __init__ (self, name , marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

s1 = Student("Ali" , 87)
s2 = Student("Mahnoor" , 88)
s3 = Student("fahad" , 58)

s1.display()
s3.display()

