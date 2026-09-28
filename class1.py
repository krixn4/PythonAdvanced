class Person:
    def __init__(self):
        print("Enter the details")
        self.name = input("Enter name")
        self.age = int(input("Enter age"))

    def show(self):
        print(self.name, self.age)


p1=Person()  #Object p1 of Class Person
p1.show()
p2=Person()  #Object p2 of class Person
p2.show()
