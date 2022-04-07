# instance
# objects
#init
#use of self inside init method


class Employee:
    emp_count = 0

    def __init__(self, name, empid):
        self.name = name
        self.empid = empid
        Employee.emp_count = Employee.emp_count + 1

    def nname(self):
        print(self.name)

    def emppid(self):
        print(self.empid)
'''
 #   def emp_count(self):
 #       print(Employee.emp_count)


a1 = Employee("Soumya", 1)
a2 = Employee("So", 2)
a1.nname()
a1.emppid()
a2.nname()
a2.emppid()
print(Employee.emp_count)
'''



