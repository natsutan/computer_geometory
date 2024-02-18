import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance(self, other):
        return (self - other).length()

    def angle(self, other):
        return math.acos(self.dot(other) / (self.length() * other.length()))

    def rotate(self, center, angle):
        x = self.x - center.x
        y = self.y - center.y
        # angleをラジアンに変換する
        angle = math.radians(angle)

        x1 = x * math.cos(angle) - y * math.sin(angle)
        y1 = x * math.sin(angle) + y * math.cos(angle)
        return Point(x1 + center.x, y1 + center.y)

class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'({self.p1}, {self.p2})'

    def __repr__(self):
        return f'Line({self.p1}, {self.p2})'

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2

    def __ne__(self, other):
        return not self.__eq__(other)



def midpoint(p1:Point, p2:Point) -> Point:
    x = (p1.x + p2.x) / 2
    y = (p1.y + p2.y) / 2

    return Point(int(x), int(y))

