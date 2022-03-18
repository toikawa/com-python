class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")

point = Point(5,7)
print(point.x)
