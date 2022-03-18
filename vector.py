import math

"""
with in this file, we are trying to calculate the distance between the pacman and its target object
"""

class Vector2(object):
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector2(self.x / float(scalar), self.y / float(scalar))
        return None

    def __truediv__(self, scalar):
        return self.__div__(scalar)

    # checking the equality between 2 vectors
    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    # the magnitude method returns the actual length of the vector
    """ the magnitude method requires using square root, but can also be avoided"""
    def magnitudeSquared(self):
        return self.x**2 + self.y**2

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    # create a copy method to avoid reusing the object
    """it copies any vector so we get & use the new instance of the object created"""
    def copy(self):
        return Vector2(self.x, self.y)

    def asTuple(self):
        return self.x, self.y

    def asInt(self):
        return int(self.x), int(self.y)

    def __str__(self):
        return "<" + str(self.x)+", " + str(self.y) + ">"
