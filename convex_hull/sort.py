from point import Point
from segment import inner_angle

def points_by_x(points):
  return points.sort(key=lambda point: point.x)

def points_by_y(points):
  return points.sort(key=lambda point: point.x)

def points_by_clockwise(points):
  avg_x = (sum(point.x for point in points) / len(points))
  avg_y = (sum(point.y for point in points) / len(points))
  avg_point = Point(avg_x, avg_y, 'Average Point')
  return points.sort(key=lambda point: inner_angle(avg_point, point))

   
