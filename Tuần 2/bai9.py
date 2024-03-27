class Rectangle:
    def __init__(self, length = 2, width = 4):
        self.length = length
        self.width = width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.calcPerimeter())
        print("Area:", self.calcArea())

    def calcPerimeter(self):
        return 2 * (self.length + self.width)

    def calcArea(self):
        return self.length * self.width


class Parallelpipe(Rectangle):
    def __init__(self, length =2, width = 4, height = 8):
        super().__init__(length, width)
        self.height = height
    
    def display(self):
        print('volume: ', self.volume())
        
    def volume(self):
        return self.length * self.width * self.height
        
rectangle = Rectangle()
rectangle.display()
pipe = Parallelpipe()
pipe.display()


