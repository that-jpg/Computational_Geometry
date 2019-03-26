def points_by_x(points):
  return points.sort(key=lambda point: point.x)

def points_by_y(points):
  return points.sort(key=lambda point: point.x)

def points_by_clockwise(points):
  avg_x = (sum(point.a for point in points) / len(points))
  avg_y = (sum(point.a for point in points) / len(points))
  avg_point = Point(avg_x, avg_y, 'Average Point')
   
