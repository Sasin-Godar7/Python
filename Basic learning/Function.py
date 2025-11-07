

#function 

# def sum(a,b):
#     sum = a + b 
#     print(f"sum = {a+b}")

# a = int(input("enter the first number :")) 
# b = int(input("enter the second number :")) 

# sum(a,b)


#wap that takes three input and display the greater one

# def comp(a,b,c):
#     if(a>b and a > c):
#         print(f"greater number is : {a}")
#     elif(b>a and b>c):
#         print(f"greater number is :{b}")
#     else:
#         print(f"greater number is :{c}")        

# a = int(input("enter the first number :")) 
# b = int(input("enter the second number :")) 
# c = int(input("enter the third number :")) 
# comp(a,b,c)


#wap that takes an input from user and check wheather it is palindrome or not ..using function

def is_palindrome(num):
    og_num = num
    reversed_num = 0
    
    while num > 0:
     rem = num % 10
     reversed_num = reversed_num * 10 + rem
     num = num//10
    return og_num == reversed_num 

num = int(input("Enter a number to check wheather it is palindrome or not :"))
if is_palindrome(num):
   print("it is palindrome")
else:
   print("not palindrome")




 






