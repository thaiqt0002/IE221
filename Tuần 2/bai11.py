class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def input_point(self):
        self.x = float(input("Nhap x: "))
        self.y = float(input("Nhap y: "))
    
    def output_point(self):
        print(f"Toa do diem: ({self.x}, {self.y})")
    
    def change_coordinates(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def get_x_coordinate(self):
        return self.x
    
    def get_y_coordinate(self):
        return self.y
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

class TamGiac:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    
    def input_triangle(self):
        print("Nhap diem A:")
        xA = float(input("Nhap x: "))
        yA = float(input("Nhap y: "))
        self.A = Point(xA, yA)
        
        print("Nhap diem B:")
        xB = float(input("Nhap x: "))
        yB = float(input("Nhap y: "))
        self.B = Point(xB, yB)
        
        print("Nhap diem C:")
        xC = float(input("Nhap x: "))
        yC = float(input("Nhap y: "))
        self.C = Point(xC, yC)
    
    def output_triangle(self):
        print("Toa do tam giac:")
        print("Diem A:", end=" ")
        self.A.output_point()
        print("Diem B:", end=" ")
        self.B.output_point()
        print("Diem C:", end=" ")
        self.C.output_point()
    
    def translate(self, dx, dy):
        self.A.translate(dx, dy)
        self.B.translate(dx, dy)
        self.C.translate(dx, dy)
    
    def get_centroid(self):
        x = (self.A.get_x_coordinate() + self.B.get_x_coordinate() + self.C.get_x_coordinate()) / 3
        y = (self.A.get_y_coordinate() + self.B.get_y_coordinate() + self.C.get_y_coordinate()) / 3
        return Point(x, y)

class DaGiac:
    def __init__(self, vertices):
        self.vertices = vertices
    
    def input_polygon(self):
        num_vertices = int(input("Nhap so dinh: "))
        self.vertices = []
        for i in range(num_vertices):
            print(f"Nhap toa do cua diem {i+1}:")
            x = float(input("Nhap x: "))
            y = float(input("Nhap y: "))
            point = Point(x, y)
            self.vertices.append(point)
    
    def output_polygon(self):
        print("Toa do cua da giac:")
        for i, point in enumerate(self.vertices):
            print(f"Diem {i+1}:", end=" ")
            point.output_point()
    
    def translate(self, dx, dy):
        for point in self.vertices:
            point.translate(dx, dy)
    
    def get_centroid(self):
        num_vertices = len(self.vertices)
        sum_x = sum(point.get_x_coordinate() for point in self.vertices)
        sum_y = sum(point.get_y_coordinate() for point in self.vertices)
        x = sum_x / num_vertices
        y = sum_y / num_vertices
        return Point(x, y)

p = Point()
p.input_point()
p.output_point()
p.change_coordinates(3, 4)
print('Sau khi tinh tien: ')
p.output_point()

print('---------------------------')
t = TamGiac(Point(1, 2), Point(3, 4), Point(5, 6))
t.output_triangle()
t.translate(1, 1)
print('Sau khi tinh tien:')
t.output_triangle()
centroid = t.get_centroid()
print("Trong tam cua tam giac:")
centroid.output_point()

print('---------------------------')
d = DaGiac([])
d.input_polygon()
d.output_polygon()
d.translate(1, 1)
d.output_polygon()
centroid = d.get_centroid()
print("Trong tam cua da giac:")
centroid.output_point()