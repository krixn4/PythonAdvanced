class Employee:
    def __init__(self):
        self.name=input("enter name:")
        self.age=int(input("enter age:"))
        self.salary=int(input("enter salary:"))
    def getsalary(self):
        print(self.salary)
    def showpersonaldetails(self):
        print(self.name)
        print(self.age)
e=Employee()
e.getsalary()
e.showpersonaldetails()