file = open("new-file.txt",'w')

file.write("this is the first line \n")
file.write("this is the second line \n")
file.close()

lines = ['lumbini\n' , 'ICT\n','Campus\n']
# file = open("new-file.txt",'a')
file = open("new-file.txt",'w')
file.writelines(lines)
file.close()

# file = open("new-file.txt",'r')            # this reads as a whole
# content = file.read()
# print(content)
# file.close()

# file = open("new-file.txt",'r')            # this reads the content line by line wise
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# print("line1 is  :",line1)
# print("line2 is  :",line2)
# print("line3 is  :",line3)
# file.close()

file = open("new-file.txt",'r+')
content = file.read()
print("current content :")
print(content)
#Append new content in it
file.write("yo line paxi append gareko haii>>\n")
file.seek(0)
content = file.read()
print("updated content after appending :")
print(content)
file.close()

