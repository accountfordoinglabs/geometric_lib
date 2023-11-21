import unittest

def area(a, h):
    '''Принимает числа  a и h, возвращает площадь треугольника со стороной a и высотой h'''
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает числа  a, b и c, возвращает периметр треугольника со сторонами a, b и c'''
    return a + b + c

class  TriangletestCase (unittest.TestCase):
    def test_triangle_area(self):
        res=area(0.5,1)
        self.assertEqual (res,0.25)
    def test_triangle_perimeter(self):
        res=perimeter(0.5,0.5,1.5)
        self.assertEqual (res,2.5)