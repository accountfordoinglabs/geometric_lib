import unittest
import math


def area(r):
    '''Принимает число  r, возвращает площадь круга радиуса r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число  r, возвращает длину окружности радиуса r'''
    return 2 * math.pi * r

class  CircleTestCase (unittest.TestCase):
    def test_circle_area(self):
        res=area(5)
        self.assertEqual (res,25*math.pi)
    def test_circle_perimeter(self):
        res=perimeter(5)
        self.assertEqual (res,10*math.pi)