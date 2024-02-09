class Point:
    def __init__(self, x_axis_point, y_axis_point):
        self.x_axis_point = x_axis_point
        self.y_axis_point = y_axis_point

    def show(self):
        print(f"x = {self.x_axis_point}, y = {self.y_axis_point}.")

    def move(self):
        self.x_axis_point = int(input())
        self.y_axis_point = int(input())

    def dist(self):
        from math import sqrt
        return sqrt(self.x_axis_point ** 2 + self.y_axis_point ** 2)