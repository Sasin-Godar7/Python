
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of rectangle:{self.length*self.width}")

    def perimeter(self):
        print(f"Perimeter of rectangle:{2*(self.length + self.width)}")

l = int(input("Enter length"))
b = int (input("Enter breadth"))
obj = Rectangle(l,b)
obj.area()
obj.perimeter()        

    