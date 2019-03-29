import sys
from math import acos
from math import pi
from math import sqrt

_positive_huge = sys.float_info.max
_negative_huge = sys.float_info.min

# get the tangency of given two points
def tangency(a, b):
  if (a.x - b.x == 0):
    if (a.y > b.y): 
      return _negative_huge
    else:
      return _positive_huge
  else:
    return (a.y - b.y) / (a.x - b.x)
  # y-y0 = m(x-x0)  -> m = y-(y0)/(x-x0)

# 0 for co-linear 
# 1 for Clockwise 
# 2 for Counterclockwise 
# crossproduct of q-p and q-r
# https://stackoverflow.com/questions/17592800/how-to-find-the-orientation-of-three-points-in-a-two-dimensional-space-given-coo
# @param - three points
def orientation(a, b, c): 
  val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y); 
  if (val == 0):
    return 0 
  else:
    return 1 if (val > 0) else 2

# @param - two segments
def intersect(a, b):
  # p = start 
  # q = end
  o1 = orientation(a[0], a[1], b[0]); 
  o2 = orientation(a[0], a[1], b[1]); 
  o3 = orientation(b[0], b[1], a[0]); 
  o4 = orientation(b[0], b[1], a[1]); 
  
  if (o1 != o2 and o3 != o4):
    return True
  
  if (o1 == 0 and onSegment(a[0], b[0], a[1])):
    return True
  
  if (o2 == 0 and onSegment(a[0], b[1], a[1])):
    return True
  
  if (o3 == 0 and onSegment(b[0], a[0], b[1])):
    return True
  
  if (o4 == 0 and onSegment(b[0], a[1], b[1])):
    return True
  
  return False

def length(point):
  # Pythagorical distance
  return sqrt(point.x**2 + point.y**2)

def dot_product(a, b):
  return a.x*b.x + a.y*b.y

def determinant(a, b):
  return (a.x * b.x) - (a.y * b.y)

def inner_angle(a, b):
  return dot_product(a, b)/(length(a)*length(b))


