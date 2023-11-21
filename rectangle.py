import unittest

def area(a, b): 
    '''Принимает числа  a и b, возвращает площадь прямоугольника со сторонами a и b'''
    return a * b 

def perimeter(a, b):
    '''Принимает числа  a и b, возвращает периметр прямоугольника со сторонами a и b'''
    return 2*(a + b) 

class  RectangleTestCase (unittest.TestCase):
    def test_rectangle_area(self):
        res=area(0,0)
        self.assertEqual (res,0)
    def test_rectangle_perimeter(self):
        res=perimeter(0,0)
        self.assertEqual (res,0)