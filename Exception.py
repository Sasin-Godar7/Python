a = int(input("enter the numerator :"))
b= int(input("enter the denominator:"))

try:
    r = a/b 
    print("result is :",r)

except:
    print("erorr!!!!cannot divide by zero ..")

finally:
   
    print("this is the finally block that runs anyway")

