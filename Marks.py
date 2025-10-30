class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def total(self):
        sum1 += self.marks 
        print(f"The total marks is {sum1}")

    def avarage(self,total):
        avg1 = total/3 
        print(f"The avarage marks is {avg1}")

            