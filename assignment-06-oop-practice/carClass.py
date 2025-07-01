class Car:
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting....")

car1 = Car("toyota")
car1.start()

car2 = Car("civic")
car2.start()