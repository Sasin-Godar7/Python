class Rectangle:
    def __init__(self,length,width): # this __init__ is the constructor
        self.length = length
        self.width = width

    def  area(self):
        print(f"area of rectangle is {self.length * self.width}")

    def perimeter(self):
        print(f"perimeter of rectangle is {2*(self.length * self.width)}")

l = int(input("Enter the length of rectangle :> "))  
w = int(input("Enter the width of rectangle :> "))

obj = Rectangle(l, w)
obj.area()
obj.perimeter()      
  
        