import unittest

def area(a):
    '''Принимает число  a, возвращает площадь квадрата со стороной a'''
    return a * a


def perimeter(a):
    '''Принимает число  a, возвращает периметр квадрата со стороной a'''
    return 4 * a

class  SquareletestCase (unittest.TestCase):
    def test_square_area(self):
        res=area(10)
        self.assertEqual (res,100)
    def test_square_perimeter(self):
        res=perimeter(10)
        self.assertEqual (res,40)