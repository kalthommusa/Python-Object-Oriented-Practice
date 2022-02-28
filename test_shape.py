import unittest  
from object_oriented_mathematical_operations import Shape, Point, Line

class TestShape(unittest.TestCase):

  def setUp(self):
    # Create objects(instances) of Point class
    self.point1 = Point(4, 0)
    self.point2 = Point(6, 6)
    self.point = Point(5, 4)
    # Create another line's endpoints
    self.line2point1 = Point(3, 1)
    self.line2point2 = Point(8, 4)
    # Create an object(instance) of Line class
    # And passing the points objects as an arguments 
    self.line1 = Line(self.point1, self.point2) 
    # And here passing the line's coordinates as an arguments
    self.line1_coo = Line(7, 6, 5, 8)
    # Create another instance of the Line class
    self.line2 = Line(self.line2point1, self.line2point2)

  def test_point_point_distance(self):
    # Calling a method and passing another point
    # Print(self.point1.point_point_distance(self.point2))
    self.assertEqual(self.point1.point_point_distance(self.point2), 6.324555320336759)

  def test_fromline_point_point_distance(self):
    # Calling a method and passing the another point
    # Print(self.line1.point_point_distance(self.point))
    # Print(self.line1_coo.point_point_distance(self.point))
    self.assertEqual(self.line1.point_point_distance(self.point), 4.123105625617661)

  def test_point_line_distance(self):
    # Calling a method and passing another line
    # Print(self.line1.point_line_distance(self.line2))
    # Print(self.line1_coo.point_line_distance(self.line2))
    self.assertEqual(self.line1.point_line_distance(self.line2), 1.3719886811400706)

  def test_line_line_intersection_point(self):
    # Calling a method and passing another line
    # Print(self.line1.line_line_intersection_point(self.line2))
    # Print(self.line1_coo.line_line_intersection_point(self.line2))
    self.assertEqual(self.line1.line_line_intersection_point(self.line2), (-120.33333333333333, -73.0))

  def test_line_line_intersection_angle(self):
    # Calling a method and passing another line
    # Print(self.line1.line_line_intersection_angle(self.line2))
    # Print(self.line1_coo.line_line_intersection_angle(self.line2))
    self.assertEqual(self.line1.line_line_intersection_angle(self.line2), (0.5404195002705843, 179.4595804997294))


if __name__ == '__main__':
    unittest.main()