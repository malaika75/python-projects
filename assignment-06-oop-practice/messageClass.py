class logger:
    def __init__(self):
        print("object is created constructor")

    def __del__ (self): #Automatically call hota hai jab object destroy ho jata hai. Memory cleanup ke liye use hota hai.
      print("object delete destructor")
    

ob1 = logger()
del ob1