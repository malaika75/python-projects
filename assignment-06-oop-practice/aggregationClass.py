class Employee:
    def __init__(self , name):
        self.name = name
    
    def show(self):
        return self.name


class Department:
    def __init__(self , employee , department_name):
        self.employee = employee  #aggregation 
        self.department_name  = department_name

    def show_details(self):
        print(f"{self.employee.show()} is in the {self.department_name}")


epl = Employee("ayesha")
epl.show()
dept = Department(epl , "finance department")
dept.show_details()

ep2 = Employee("fariha")
ep2.show
dept2 = Department(ep2 , "accounts department")
dept2.show_details()

