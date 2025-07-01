class Engine:
    def __init__(self):
        print("engine start")


class Car:
    def __init__(self , engine):
        self.engine = engine

car1 = Engine()
start = Car(car1)
        