class Point:
    count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1
        
        
    def draw(self):
        print("Object: {} - Point({}, {})".format(Point.count, self.x, self.y))
        
    
p1 = Point(5, 6)
p1.draw()
p2 = Point(6, 6)
p2.draw()
p3 = Point(7, 16)
p3.draw()
print("Total Point Object - {}".format(Point.count))