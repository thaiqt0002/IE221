import math

class Circle:
    a: int
    b: int 
    c: int
    def __init__(self, a=2, b=5, r=2):
        self.a = a
        self.b = b
        self.r = r

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        perimeter =  2 * math.pi * self.r
        print('Chu vi hình tròn: ', perimeter)

    def test_belongs(self, x=2, y=7):
        distance = math.sqrt((x - self.a)**2 + (y - self.b)**2)
        check =  (distance == self.r)
        print(f"Diem A{x,y} thuoc duong tron" if check else f"Diem A{x,y} khong thuoc duong tron")
        

circle = Circle()
circle.area()
circle.perimeter()
circle.test_belongs()
