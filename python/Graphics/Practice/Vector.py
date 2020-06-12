"""
3D Vector Class
"""
from math import sqrt


class Vector3(object):
    """
    Vector class
    can be either 3D or 2D
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, addend):
        """
        :param (vector) addend: the vector to add to the personal vector
        :description: adds two vectors together
        :return: (Vector) if the dimensions match, (None) if dimensions do not match
        """
        return Vector3(x=self.x + addend.x, y=self.y + addend.y, z=self.z + addend.z)

    def __sub__(self, other):
        """
        :param (vector) addend: the vector to add to the personal vector
        :description: adds two vectors together
        :return: (Vector) if the dimensions match, (None) if dimensions do not match
        """
        return Vector3(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    def __mul__(self, src):
        """

        :param src:
        :return:
        """
        if type(src) == Vector3:
            x = (self.y * src.z) - (self.z * src.y)
            y = (self.z * src.x) - (self.x * src.z)
            z = (self.x * src.y) - (self.y * src.x)
            return Vector3(x=x, y=y, z=z)
        else:
            # probably a float
            return Vector3(x=self.x*src, y=self.y*src, z=self.z*src)

    def get_magnitude(self):
        """
        :description: calculate the distance of the vector
        :return:
        """
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        """
        :return: (str) : convert class to a string
        """
        return "({}, {}, {})".format(self.x, self.y, self.z)


class Vector(object):
    """
    Vector class
    can be either 3D or 2D
    """

    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        if z is None:
            self.third_dimension = False
        else:
            self.third_dimension = True
            self.z = z

    def __add__(self, addend):
        """
        :param (vector) addend: the vector to add to the personal vector
        :description: adds two vectors together
        :return: (Vector) if the dimensions match, (None) if dimensions do not match
        """
        if self.third_dimension:
            if addend.third_dimension:
                # the other addend should be 3 dimensional
                return Vector(x=self.x + addend.x, y=self.y + addend.y, z=self.z + addend.z)
            else:
                return None

        else:
            if not addend.third_dimension:
                # the other addend should be 2 dimensional
                return Vector(x=self.x + addend.x, y=self.y + addend.y)
            else:
                return None

    def get_magnitude(self):
        """
        :description: calculate the distance of the vector
        :return:
        """
        if self.third_dimension:
            return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        else:
            return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        """
        :return: (str) : convert class to a string
        """
        if self.third_dimension:
            return "({}, {}, {})".format(self.x, self.y, self.z)
        else:
            return "({}, {})".format(self.x, self.y)


# A = Vector(6, 8, 12)
# B = Vector(10, 16, 12)
# C = A + B
#
# print(A)
# print(B)
# print(C)

