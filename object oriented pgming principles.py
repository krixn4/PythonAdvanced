# #object oriented programming principles
# from multiprocessing import context
# from sys import implementation
#
# 1.class - defintion of its object,it contains properties and operation codes/functions
# 2.object - is a member/instance of a class. All objects of same class have similar properties and operations
# 3.encapsulation - Binding the properties and functions into a single unit
# 4.inheritance - deriving attributes(properties/operations) from one class(parent/base/super) into another class(child/derived/sub)
# 5.polymorphism - an entity(method/operator) behaves in different forms in different context
# 6.Abstraction - hiding implementation details and showing the essential details to the user
#
from dis import COMPILER_FLAG_NAMES
from logging import setLoggerClass


# INHERITANCE

# TYPES
# 1.single inheritance
# 2.multiple inheritance
# 3.multilevel inheritance
# 4.hierarchical inheritance
# 5.hybrid

# 1.SINGLE INHERITANCE

# class Parent:
#     def m1(self):
#         print("in Parent class method m1")
# class Child(Parent):
#     def m1(self):       #method overriding
#         super().m1()
#         print("in Child class method m1")
#     def m2(self):
#         print("in Child class method m2")
# c=Child()
# c.m1()
# c.m2()

# class Person:
#     def __init__(self):
#         self.name=input("enter name:")
#         self.age=input("enter age:")
#     def show(self):
#         print("name:",self.name,"age:",self.age)
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter rollno:"))
#         self.mark=int(input("enter mark:"))
#     def show(self):
#         super().show()
#         print("rollno:",self.rollno,"mark:",self.mark)
# s=Student()
# s.show()

# class Category:
#     def __init__(self):
#         self.category_name=input("enter category name:")
#     def showcategory(self):
#         print("category:",self.category_name)
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input("enter product name:")
#         self.price=int(input("enter price:"))
#         self.quantity=int(input("enter quantity:"))
#     def total_price(self):
#         super().showcategory()
#         print("total price:",self.quantity*self.price)
# p=Product()
# p.total_price()

# class Company:
#     def __init__(self):
#         self.company_name=input("enter company name:")
#         self.location=input("enter location")
#     def display_complany(self):
#         print("company name:",self.company_name,"location:",self.location)
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("enter id:"))
#         self.empname=input("enter name:")
#         self.salary=int(input("enter salary:"))
#     def display_details(self):
#         print("empid:",self.empid)
#         print("empname:",self.empname)
#         print("salary:",self.salary)
#         super().display_complany()
#     def update_salary(self):
#         self.salary=self.salary+self.salary*0.1
#         print("new salary:",self.salary)
# e=Employee()
# e.display_details()
# e.update_salary()

# POLYMORPHISM

# Polymorphism allow different classes to have same function name with different implementation/code

#METHOD OVERRIDING - it is OOPs principle that allows a child class to define a func that is already defined inside parent

