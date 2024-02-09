class Shape:
    def area(self):
        shapes_area = 0
        print(shapes_area)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.width * self.width)