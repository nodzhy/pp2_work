class Shape:
    def __init__(self, length=0):
        self.length=length

    def area(self):
        return self.length
class Circle(Shape):
    def __init__(self, length=0):
        super().__init__(length)

    def area(self=0):
        return 3.14*self.length*self.length
class S(Circle):
    def __init__(self, lenght=0):
        super().__init__(lenght)

    def v(self):
        return 4 *(self.length**3 *3.14)/3
shape = Shape(5)
print("shape:", shape.area())
circle = Circle(4)
print("circle", circle.area())
s=S(6)
print("volume", s.area())
    