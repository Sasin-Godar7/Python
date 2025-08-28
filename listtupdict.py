
# list is given in big bracket[] and it is mutuable
# list------------------->>>>> 

# list = [1,'a',"string",5+9]
# print(list)
# print(type(list))
# list.append(7)
# list.append("lumbini")
# print(list)

#append is use to insert the data and pop is used to remove the data form last
# list.pop()
# print(list)

# print(list[1]) --->SHOW THE ELEMENT FROM THE INDEX[1]

# list1= list  + ["ict",4,"campus",100+100]
# print(list1)



#Assignment

# names = ["sasin","ashok","abin","as"]
# newnames = []

# for word in names:
#     if len(word) > 3 and word[0] =='a':
#         newnames.append(word)
#         print(newnames)
# newnames.sort()
# print(newnames)






# ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>

# d = {
#     "Faculty " : "bca",
#     "sem" : 4,
#     "Location":"gaidakot"

# }
# print(d)
# print(type(d))

















#--------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

#Tuple

# t = (1,'c',"lumbini",2+2)
# print(t)
# print(type(t))

# l= list(t)
# print(l)
# print(type(l))
# l.append("campus")
# print(l)

# t1 = tuple(l)
# print(t1) 
# print(type(t1)) 
#here we cant append un tuple so we change it into list then append to it and later convert the list into tuple






# ----------------------------------->>>>>>>>>>>>>>>>

#Dictionary 

# simple student marks

students = { }
for i in range(5):
    name = input("Enter the name of the student :")
    marks = int(input(f"Enter the marks of {name}"))
    students[name] = marks 

    #dispplayy

    print("\n --------- student marks")
    for name,marks in students.item():
        print(f"{name} : { marks}")



