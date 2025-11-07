        # --odd even -------->
# a = int (input("enter any number :"))
# if a%2 ==0:
#       print(f"{a} is even")
# else:
#        print(f"{a} is odd")


# age = int (input("Enter the age :"))


# voting ------------>

# if age<=0:
#     print("invalid age given")
# elif age<18:
    
#     print("sorry not enough age to vote")
# else:
#     print("can go for vote")


# greater smaller ----------->

# num1 = int (input("Enter the number 1 :"))
# num2 = int(input("Enter the number 2 :"))

# if num1 == num2 :
#     print(f"{num1} and {num2} are equall")
# elif num1 > num2:
#     print(f"{num1 } is greater then {num2}")
# else:
#     print(f"{num2} is greater then {num1} ")


# for loop --------------->
# for i in range(1,10):
#     print(i)

# for i in range(1,10):
#         print("sasin")
      
# var = "Lumbini ict campus"
# for i in var:
#         print(i)      



# #break-->>
# num = 0
# for i in range(10):
#     num +=1 
#     if num == 8:
#         break
#     print("the number has value :",num)
# print("out of looop..!!")  


#continue--------->
# num = 0
# for i in range(10):
#     num +=1 
#     if num == 8:
#         continue
#     print("the number has value :",num)
# print("out of looop..!!") 


#Match case--------->

# day = int(input("enter the number from 1 to 7 :"))
# match day:
#     case 1:
#         print ("sunday")
#     case 2:
#         print ("monday")
#     case 3:
#         print ("tuesday")
#     case 4:
#         print ("wednesday")
#     case 5:
#         print ("thursday")
#     case 6:
#         print ("friday")
#     case 7:
#         print ("saturday")
#     case _:
#         print ("invalid number entered" )
    


# for i in range(1,50):
#     if (i%2)!=0:
#         continue
#     print(i)



#pyramid
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("\r")    


# n = int(input("Enter any number you want:"))
# for i in range(1,11):
#     print(f"{n} * {i} =",n*i)

#multiply 1 * 10 to 10 * 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = ", i*j)   
 


# import random

# a= random.random()
# print(a)

# num = random.randint(1,50)
# print(num)




#int 
# a=3
# b=7
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# Float

# a=3.9
# b=7.2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

#complex
# z1 = 1 + 2j
# z2 = 3- 4j

# print(z1 + z2)
# print(z1  - z2)
# print(z1 / z2)
# print(z1.real)
# print(z2.imag)



#String

# str = '--string'
# str1 = "--string1"
# str2 = '''this is 
#  multiline 
#  string'''
# print(str)
# print(str1)
# print(str2)


#indexing and slicing in string

# s = "lumbini ict campus"

#positive indexing
# print(s[3])
# print(s[6])

#negatice indexing
# print(s[-1])
# print(s[-5])

#slicing
# print(s[:7])
# print(s[12:])
# print(s[8:11])
# print(s[:])

#using steps
# print(s[1:12:2])
# print(s[-6:-1:2])

#reverse the given string
# print(s[ : : -1])


# Escape sequence

# s = "hello ,\n world" 
# print(s)  
# s1 = "hello ,\t world"
# print(s1)
# s2 = 'It\'s a wonderful day'
# print(s2)
# s3 = "She said,\"I am beautiful\" "
# print(s3)

#Boolean
# result = 5 > 3
# print(result)


#List comprehensive

words = ["Hello","World","python","is","good"]
cap = [word.upper() for word in words]
low = [word.lower() for word in words]
print(cap)
print(low)

#Unpacking

# t1 = (1,2,3,4,5)
# a, *b , c = t1
# print(a)  ---> a vannni ma place garni
# print(b)   ----> * x so remaining sab tesma because 2 ta ma sab aatauna xa 
# print(c)    --- > c ma last wala 







    
    
    
   





