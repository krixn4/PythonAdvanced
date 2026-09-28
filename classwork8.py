# # # #write a program to read a text file and displays the number of lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(len(s))
# f.close()
# # # #write a program to display the number of words in a file
# f=open('k.txt','r')
# s=f.read()
# print(len(s.split()))
# f.close()
# # # #write a program to update the second line in a file
# f=open('k.txt','r')
# s=f.readlines()
# s[1]='hii'
# f.close()
# f=open('k.txt','w')
# f.writelines(s)
# f.close()


# # #write a program to display the last 5 lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(s[-5:])
# f.close()
#
# #program to search a particular word in a file
# f=open('k.txt','r')
# s=f.read()
# w=input("enter word:")
# if w in s:
#     print("found")
# else:
#     print("not found")
# f.close()
#
# #find the number of letters,digits,and spaces in a file
# f=open('k.txt','r')
# l_count=0
# d_count=0
# s_count=0
# s=f.read()
# for i in s:
#     if i.isalpha():
#         l_count+=1
#     elif i.isspace():
#         s_count+=1
#     elif i.isdigit():
#         d_count+=1
# print("letter count:",l_count)
# print("digit count:",d_count)
# print("space count:",s_count)
# f.close()
# #reverse the lines in a file
f=open('k.txt','r')
s=f.readlines()
f.close()
f=open('k.txt','w')
f.writelines(s[::-1])
f.close()

# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.

f=open('total_students.txt','r')
k=open('passed_students.txt','r')
j=open('failed_students',"w")
t=f.read()
p=k.read()
for i in t.split():
    if i not in p.split():
        j.writelines(i)
        j.writelines('\n')
f.close()

