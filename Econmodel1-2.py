import random
class Point:
    def __init__(self, x, y):
        """
        This will be called when instantiating an object
        :param x: the value of x
        :param y: the value of y
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        This will return the string value used in printing the point
        :return:
        """
        return f"({self.x}, {self.y})"

a = Point(2,3)
b = Point(7,9)
print(f"a=({a.x}, {a.y})")
print(f"b=({b.x}, {b.y})")


points  = []
for _ in range(5):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    random_point = Point(x, y)
    points.append(random_point)

# or in a single line like this
points.append(Point(random.randint(-100, 100),
                    random.randint(-100, 100)))

for point in points:
    print(f"p({point.x}, {point.y})")

#try to print the first point
print("printing a point value"points[0])
print(points)