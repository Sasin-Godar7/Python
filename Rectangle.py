# l = int(input("Enter the length :"))
# b= int(input("Enter the breadth :"))
# area = l*b
# peri=2*(l+b)
# print(f"the area of rectangle is {area}")
# print(f"the perimeter of rectangle is {peri}")

# print(f"this is the product {2*2}")
# print(f"this is the power {2**3}")

print("Enter the sides :")
a = int(input("enter the side a "))
b=int(input("enter the side b "))
c=int(input("enter the side c "))

s = (a+b+c) / 2 

area = (s*(s-a) * (s-b) * (s-c))**0.5

print(f"the semi  of traingle is {s}")
print(f"the area of perimeter is {area}")




