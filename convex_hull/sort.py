from math import atan
from segment import inner_angle
from segment import orientation

def points_by_x(points):
  return points.sort(key=lambda point: point.x)

def points_by_y(points):
  return points.sort(key=lambda point: point.x)
   
def sort_points_by_angle_horizontal_line(points, pivot):
   # sorting them by polar cordenate
   def tg(currentPoint):
     if (pivot.x - currentPoint.x == 0):
       return 0
     else:
       return (pivot.y - currentPoint.y) / (pivot.x - currentPoint.x)
   return list(sorted(points, key=lambda point: tg(point)))
 
