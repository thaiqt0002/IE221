class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        return self.x, self.y
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def display(self):
        print(f"Point coordinates: ({self.x}, {self.y})")


# Test the Point class
point = Point(0, 0)
point.display()

point.set_coordinates(3, 4)
point.display()

dx, dy = 2, -1
point.translate(dx, dy)
point.display()