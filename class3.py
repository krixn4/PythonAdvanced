class Student:
    def __init__(self):
        self.rollno=int(input("enter rollno:"))
        self.name=input("enter name:")
        self.mark1=int(input("enter mark1:"))
        self.mark2=int(input("enter mark2:"))
        self.mark3=int(input("enter mark3:"))
    def display(self):
        print(self.rollno)
        print(self.mark1+self.mark2+self.mark3)
s=Student()
s.display()