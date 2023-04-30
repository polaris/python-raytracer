import math


class Vec3:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, t):
        return Vec3(self.x * t, self.y * t, self.z * t)

    def div(self, t):
        return self.mul(1 / t)

    def length(self):
        return math.sqrt(self.squared_length())

    def squared_length(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def print(self):
        print(str(self.x) + " " + str(self.y) + " " + str(self.z))

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3(self.y * other.z - self.z * other.y,
                    self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.x)

    def unit_vector(self):
        return self.div(self.length())


Point3 = Vec3
