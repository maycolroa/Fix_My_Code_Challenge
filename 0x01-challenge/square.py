#!/usr/bin/python3
"""module"""


class Square():
    """class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initialize"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if 'width' in kwargs.keys() and self.height != self.width:
                self.height = self.width
            if 'height' in kwargs.keys() and self.width != self.height:
                self.width = self.height

    def area(self):
        """area"""
        return self.width * self.width

    def perimeter(self):
        """perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.width)
    print(s.height)
    print(s.area())
    print(s.perimeter())
    print(s.__str__())
    print("--------------------------------")
    q = Square(width=2)
    print(q)
    print(q.width)
    print(q.height)
    print(q.area())
    print(q.perimeter())
    print(q.__str__())
    print("--------------------------------")
    u = Square(height=3)
    print(u)
    print(u.width)
    print(u.height)
    print(u.area())
    print(u.perimeter())
    print(u.__str__())
    print("--------------------------------")
    a = Square()
    print(a)
    print(a.width)
    print(a.height)
    print(a.area())
    print(a.perimeter())
    print(a.__str__())
