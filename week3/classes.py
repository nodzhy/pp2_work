#task 1
"""class StringInputAndOutput:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Введите строку: ")

    def printString(self):
        print("Строка в верхнем регистре:", self.input_string.upper())

string = StringInputAndOutput()
string.getString()
string.printString()
"""
#task 2
"""class Shape:
    def __init__(self, length=0):
        self.length = length
    def area(self):
        return self.length
class Square(Shape):
    def __init__(self, length=0):
        super().__init__(length)
    def area(self):
        return self.length * self.length
shape = Shape(5)
print("shape:", shape.area())
square = Square(4)
print("square:", square.area())
"""
#task 3
"""class Shape:
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
rectangle = Rectangle(5, 2)
rectangle.area()
"""
#task 4
"""import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f'x={self.x}  y={self.y}')
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
p1 = Point(2, 4)
p2 = Point(6, 8)
p1.show()
p2.show()
p1.move(3, 6)
p1.show()
print(f'dist: {p1.dist(p2)}')
"""
#task 5
"""class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def checkBal(self):
        print(f"Balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money on balance")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from deposit")

own1 = Account("Anuar")

own1.checkBal()
own1.deposit(5000)
own1.checkBal()
own1.withdraw(2000)
own1.checkBal()
"""