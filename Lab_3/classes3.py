class Shape():
    def __init__(self) -> None:
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        Shape.__init__(self)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


x = int(input())
y = int(input())
s = Rectangle(x, y)
print(s.area())

print(Rectangle().area())