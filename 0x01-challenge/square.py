#!/usr/bin/python3
"""
Square class to be fixed
"""


class Square:
    """ Square class """

    def __init__(self, width=0, height=0):
        """ Constructor method"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of Square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of Square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Main """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
