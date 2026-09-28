#read

#import csv
#fopen("data.csv",'r')
#content=csv.reader(filereferance)

#content=csv.reader(F)
#print(content)
#f.close()

#write

#import csv
#f=open("data.csv","w")
#content=[['title','author','price],['book1','jj',100]]
#writer=csv.writer(F) #creates writer object

# import csv
# f=open("data.csv","r")
#
# content=csv.reader(f)
#
# for row in content:
#     print(row)
# f.close()

#write
import csv
f=open("book.csv",'w')
content=[
    ['title','author','place'],
    ['book1','a1',100],
    ['book2','a2',200]
]

writer=csv.writer(f)
writer.writerows(content)
f.close()