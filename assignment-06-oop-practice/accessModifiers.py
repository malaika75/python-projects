class Employee:
    def __init__(self):
        self.name = "hania"
        self._salary = 500000
        self.__ssn = "12345-76543"

num1 = Employee()
print(num1.name) #public variable 
print(num1._salary) #protected variable
print(num1._Employee__ssn) #private variable