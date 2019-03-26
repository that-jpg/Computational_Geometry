import sort
import polygon

# Each point is a pair representing (x, y)
points = [(0, 0), (9, 0), (9, 9), (0, 9), (1, 1)]

def is_itself_convex_hull(points):
  # If there are three or less points then the list is
  # a convex hull
  return len(points) <= 3

def add_point_to_convex_hull(convex_hull, point):
  print(convex_hull)
  if (len(convex_hull) < 3):
    return convex_hull + [point]
  if (polygon.contains_ray_casting(convex_hull, point[0], point[1])):
    return convex_hull
  else:
    print("TODO: Logic when the point is not within the convex hull")
    return convex_hull

   

def incremental_convex_hull(points):
  if is_itself_convex_hull(points):
    return points
  ## Sort the list getting the right-top-most point
  sorted_points = sort.sort_points(points)

  ## create a empty list to hold our convex 
  convex_hull = []
  for point in points:
    convex_hull = add_point_to_convex_hull(convex_hull, point)

  return convex_hull

def gift_wrapping_convex_hull(points):
  if is_itself_convex_hull(points):
    return points

  ## Sort the list getting the right-top-most point
  sorted_points = sort.sort_points_by_x(points)


  

print(incremental_convex_hull(points))
