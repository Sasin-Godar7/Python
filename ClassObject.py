#Class

# class calculator:
#     def add(self,a,b):         
#         #    object le tyo method samma purauna kolagi self use vako 
#         print(f"sum of {a} and {b} is :{a+b}")

#     def sub(self,a,b):
#         d= a-b
#         return d

#     def mod(self,a,b):
#         print(f"mod of a and b is {a%b}")  

# obj = calculator()
# obj.add(5,7)
# obj.mod(2,2)
# diff = obj.sub(9,4)
# print(f"difference is :{diff}")


#INHERTITANCE

class Person:
    def __init__(self, fname, age):   # typo thik
        self.firstname = fname
        self.age = age
       
    def display(self):
        print(f"I am {self.firstname} and I am {self.age} years old.")

class Student(Person):
    def first(self):
        print("I am a good boy")

obj1 = Person("Sasin", 21)
obj1.display()

obj2 = Student("Samarpan", 24)
obj2.display()   # fixed
obj2.first()


print("-----------------------------------")


class Vehicle:
    def wheeler(self):
        print("Vehicle has wheels to move")

class Bike(Vehicle):   # Bike inherits from Vehicle
    def twowheeler(self):
        print("Bike has two wheels")

class Pulsor(Bike):    # Pulsor inherits from Bike
    def ns(self):
        print("NS is a type of Pulsor bike..")

# object create garne
obj1 = Pulsor()
obj1.wheeler()     # from Vehicle
obj1.twowheeler()  # from Bike
obj1.ns()          # from Pulsor


print("--------------------------------")

class bird:
    def types(self):
     print("there are many types of birds.")

class eagle(bird):
    def prey(self):
        print("eagle can hunt snakes too.")

class penguin(bird):
    def swim(self):
        print("penguin can swim in ice water.")

class ostrich(eagle,penguin):
    def size(self):
        print("ostrich are very big in size.")  

obj1 = ostrich()
obj1.types()
obj1.prey()
obj1.swim()  
obj1.size()           


        







