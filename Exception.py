# Exception - is an event/error condition occurs during execution of a pgm
#if an exception occurs it will stop the execution of the current pgm and displays a message showing error

#execption eccurs due to various reasons
# 1.invalid input/data - value error
# 2.unable to access file - FileNotFoundError
# 3.undefined variable - NameError
# 4.invalid type - TypeError
# 5.zero division error - ZeroDivisionError
# 6.unable to access a module - ModuleNotFoundError
# 7.KeyError - Unable to access a key in dict
# 8. AttributeError - unable to access an attribute in a class
# 9.IndexError - Unable to access a list index
# 10.IOError - Invalid file input/output

# EXCEPTION HANDLING

# try:
    #normal code
# except:
    # handling code if exception occur
# else:
    #code execute if no exception
#finally:
    # code to execute whether or not execution occurs


# try:
#     n1=int(input("Enter number:"))
#     n2=int(input("Enter number:"))
#     r=n1/n2
# except ValueError:
#     print("Value Error")
# except ZeroDivisionError:
#     print("Zero Division Error")
# except:
#     print("Error")
# else:
#     print("Result:",r)
# finally:
#     print("Done")

# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

# import math
# def fact():
#     try:
#         n=int(input("Enter a number:"))
#         f=math.factorial(n)
#         print("Factorial:",f)
#     except ValueError as e:
#         print(e)
#         print(type(e))
#         fact()
# fact()
# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
#
# try:
#     n1=int(input("Enter n1:"))
#     n2=int(input("Enter n2:"))
#     op=input("Enter operator:")
#     if op=="+":
#         print("Sum:",n1+n2)
#     elif op=="-":
#         print("Difference:",n1-n2)
#     elif op=="*":
#         print("Product:",n1*n2)
#     elif op=="/":
#         print("Quotient:",n1/n2)
#     else:
#         print("Invalid operator")
# except ZeroDivisionError:
#     print("Zero Division Error")
# except:
#     print("Invalid input")

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
# try:
#     filename=input("Enter filename:")
#     f=open(filename,"r")
#     print("File opened successfully")
#     f.close()
# except:
#     print("File does not exist")

#Given a Dictionary
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
# d={"name":"arun","age":23,"place":"ekm"}
# try:
#     k=input("Enter key:")
#     print(d[k])
# except KeyError:
#     print("key does not exist")



#to manually generate an exception


    #raise ExceptionType("message")
#raise ValueError("number must be positive")

# try:
#     age=int(input("enter age:"))
#     if age<18:
#         raise ValueError("not eligible for voting")
#     else:
#         print("eligible for voting")
# except ValueError as e:
#     print(e)


#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

# try:
#     num=int(input("enter the no:"))
#     if num<=0:
#         raise ValueError("Number must be positive")
# except ValueError as e:
#     print(e)

#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")

# class InvalidPasswordError(Exception):
#     pass
# try:
#     passw=input("enter password:")
#     if len(passw)<8:
#         raise InvalidPasswordError("Password should be 8 characters")
# except InvalidPasswordError as e:
#     print(e)


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsufficientBalanceError(Exception):
    pass
try:
    bal = int(input("enter balance:"))
    amount=int(input("enter amount:"))
    if amount>bal:
        raise InsufficientBalanceError("Not Enough Balance.Transaction Failed")
except InsufficientBalanceError as e:
    print(e)