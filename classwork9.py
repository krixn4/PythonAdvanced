#Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class Student:
    def __init__(self):
        self.rollno=int(input("enter rollno:"))
        self.name=input("enter name:")
        self.marks=int(input("enter mark:"))
    def updatemarks(self):
        newmark=int(input("enter mark:"))
        self.marks=newmark
    def display(self):
        print(self.rollno,self.name,self.marks)
l=[]
while(1):
    print("1.Add student. \n2.Update marks. \n3.Display. \n4.Search. \n5.Delete. \n6..Exit")
    ch=int(input("enter the choice:"))
    if ch==1:
        s=Student()
        l.append(s)
        print(l)
    elif ch==2:
        rno=int(input("enter rollno"))
        for i in l:
            if i.rollno==rno:
                i.updatemarks()
                break
        else:
            print("roll no not found")
    elif ch==3:
        for i in l:
            i.display()
    elif ch==4:
        rno=int(input("enter rollno:"))
        for i in l:
            if i.rollno==rno:
                i.display()
                break
        else:
            print("not found")
    elif ch==5:
        rno=int(input("enter rollno:"))
        for i in l:
            if i.rollno==rno:
                l.remove(i)
    elif ch==6:
        break
