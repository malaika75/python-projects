class Counter:
    count = 0 #count ek class variable hai jo Counter class ke sab objects ke liye common hai.
    def __init__(self):
        Counter.count += 1

    @classmethod #@classmethod decorator use karke display method ko class level par banaya gaya hai.
    def display(cls):
        print(f"total count {cls.count}")
        #cls.count ka matlab hai class variable count ko access karna.

obj1 = Counter()
obj1 = Counter()
obj1 = Counter()
obj1 = Counter()
#Har baar jab new object banega (obj1, obj2, obj3), to __init__ method call hoga aur Counter.count ki value 1 se increase ho jayegi.


Counter.display()
#Counter.display_count() call karke total objects ka count print kiya gaya.

