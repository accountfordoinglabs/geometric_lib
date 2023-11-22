import unittest
import math
import circle
import rectangle 
import square 
import triangle 

class  CircleTestCase (unittest.TestCase):
    def test_circle_area(self):
        res=circle.area(5)
        self.assertEqual (res,25*math.pi)
    def test_circle_perimeter(self):
        res=circle.perimeter(5)
        self.assertEqual (res,10*math.pi)

class  RectangleTestCase (unittest.TestCase):
    def test_rectangle_area(self):
        res=rectangle.area(0,0)
        self.assertEqual (res,0)
    def test_rectangle_perimeter(self):
        res=rectangle.perimeter(0,0)
        self.assertEqual (res,0)

class  SquareletestCase (unittest.TestCase):
    def test_square_area(self):
        res=square.area(10)
        self.assertEqual (res,100)
    def test_square_perimeter(self):
        res=square.perimeter(10)
        self.assertEqual (res,40)

class  TriangletestCase (unittest.TestCase):
    def test_triangle_area(self):
        res=triangle.area(0.5,1)
        self.assertEqual (res,0.25)
    def test_triangle_perimeter(self):
        res=triangle.perimeter(0.5,0.5,1.5)
        self.assertEqual (res,2.5)