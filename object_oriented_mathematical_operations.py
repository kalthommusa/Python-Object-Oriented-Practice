# Import the necessary packge 
import math

# Creat a superclass (parent class)
class Shape:
  pass

#create a subclass(chaild) from the Shape class(parent class)
class Point(Shape):
  # Creat a constructor of Point class
  def __init__(self, x, y):
    # Add properties(instance variables)   
    self.x = x
    self.y = y

  def point_point_distance(self, otherpoint):
    """ Calculate the dictance between two points """
    p_p_distance = math.sqrt((otherpoint.x - self.x)**2 + (otherpoint.y - self.y)**2)
    return p_p_distance

# Create a subclass(chaild) from the Shape class(parent class)
class Line(Shape):
  # Overloading constructors based on the arguments 
  def __init__(self, *args):
    # The value of the instance variables differ based on the arguments  
    if isinstance(args[0], int):
      self.x1 = args[0]
      self.y1 = args[1]
      self.x2 = args[2]
      self.y2 = args[3]
    elif isinstance(args, object):
      self.x1 = args[0].x
      self.y1 = args[0].y
      self.x2 = args[1].x
      self.y2 = args[1].y 

  def point_point_distance(self, otherpoint):
    """ Calculate the dictance between two points """
    p_p_distance = math.sqrt((otherpoint.x - self.x1)**2 + (otherpoint.y - self.y1)**2)
    return p_p_distance

  def point_line_distance(self, otherline):
    """ Calculate the dictance between point and line"""
    d = math.sqrt((otherline.x2 - otherline.x1)**2 + (otherline.y2 - otherline.y1)**2)
    p_l_distance = abs((otherline.x2 - otherline.x1)*(otherline.y1 - self.y1) -  \
    (otherline.x1 - self.x1)*(otherline.y2 - otherline.y1)) / d
    return p_l_distance

  def line_line_intersection_point(self, otherline):
    """ Calculate the intersection point between two lines """
    # Calculate the denominator
    d = (self.x1-self.x2)*(otherline.y1-otherline.y2) - (self.y1-self.y2)*(otherline.x1-otherline.x2)
    # Check if the lines are parallel 
    if d == 0:
       print("There is no an intersection point, these two lines are parallel!")
       return None
    else:
       intersection_pointx = (self.x1*self.y2-self.y1*self.x2)*(otherline.x1-otherline.x2) - \
       (self.x1-self.x2)*(otherline.x1*otherline.y2-otherline.y1*otherline.x2)/d

       intersection_pointy = (self.x1*self.y2-self.y1*self.x2)*(otherline.y1-otherline.y2) - \
       (self.y1-self.y2)*(otherline.x1*otherline.y2-otherline.y1*otherline.x2)/d

    return intersection_pointx, intersection_pointy

  def line_slope(self, x1, y1, x2, y2):
    """ Calculate the slope or gradient of a line """
    xdiff = (x2-x1)
    if xdiff == 0:
      raise ValueError ("Can not divide by zero!")
      return None
    else:
      slope = (y2-y1) / xdiff
      return slope

  def line_line_intersection_angle(self, otherline):
    """  Calculate the angle of intersection of two lines """
    # Slope (gradient) for 1st line
    m1 = self.line_slope(self.x1, self.y1, self.x2, self.y2)
    # Slope (gradient) for 2nd line
    m2 = self.line_slope(otherline.x1, otherline.y1, otherline.x2, otherline.y2) 
    
    z = abs(m2-m1 / 1+(m1*m2))
    angle = math.atan(z) 

    if (angle==0):
      print("The angle of intersection is {}, these two lines are parallel!".format(angle))
    elif(angle==90): 
      print("The angle of intersection is {}, these two lines are perpendicular!".format(angle))
    elif angle<90: 
      print("The acute angle of the lines intersection is {}".format(angle))
      b_angle = 180-angle
      print("The beta angle of the lines intersection is {}".format(b_angle))
    else:
      print("The obtuse angle of the lines intersection is {}".format(angle))
      b_angle = 180-angle
      print("The beta angle of the lines intersection is {}".format(b_angle))
    
    return angle , b_angle