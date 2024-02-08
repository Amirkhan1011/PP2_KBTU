import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    def dist(self, p2):
        print(math.sqrt((p2.x-self.x)**2 + (p2.y-self.y)**2))
        
p1 = Point(1,2)
p1.show()
p1.move(1,1)
p1.show()

p2 = Point(3,4)
p1.dist(p2)