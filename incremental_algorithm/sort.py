from math import acos
from math import sqrt
from math import pi
from point import Point

def length(point):
    # Pythagorical distance
    return sqrt(point.x**2 + point.y**2)

def dot_product(a, b):
   # The sum of the products
   return a.x*b.x + a.y*b.y


def determinant(a , b):
   return (a.x * b.x) - (a.y * b.y)

# the return is in cos of clockwise angle
def inner_angle(a , b):
   return dot_product(a , b)/(length(a)*length(b))

def points_by_x(points):
  return points.sort(key=lambda point: point.x)

def points_by_y(points):
  return points.sort(key=lambda point: point.x)

def points_by_clockwise(points):
  avg_x = (sum(point.x for point in points) / len(points))
  avg_y = (sum(point.y for point in points) / len(points))
  avg_point = Point(avg_x, avg_y, 'Average Point')
  return points.sort(key=lambda point: inner_angle(avg_point, point))

   
