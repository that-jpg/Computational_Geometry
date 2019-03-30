import sys
import polygon as Polygon
import sort as Sort 
import segment as Segment

_positive_huge = sys.float_info.max
_negative_huge = sys.float_info.min

from point import Point

# ------ The incremental algorithm
# The first argument is guaranted to be a 
# convex hull
def add(convex_hull, point):
  if (len(convex_hull) <= 2):
    convex_hull.append(point) 
  elif not(Polygon.contains(convex_hull, point)):
    Sort.points_by_clockwise(convex_hull)
    print("The point is part of the hull " + point.alias)
    special_vertices_of_tangency = []
    # find the points that are 'special vertices of tangency'
    # looking from the edges one end intercept the convex and the other
    # do not
    for i in range(0, len(convex_hull)):
      is_last_vertex = i == len(convex_hull) - 1
      curr_vertex = convex_hull[i]
      next_vertex = convex_hull[0 if is_last_vertex else i + 1]
      prev_vertex = convex_hull[len(convex_hull) - 1 if i == 0 else i - 1]
      
      line_curr_new_point = [curr_vertex, point]
      previous_edge = [prev_vertex, curr_vertex]
      next_edge = [curr_vertex, next_vertex]
      
      has_prev_intersect = Segment.intersect(line_curr_new_point, previous_edge)
      has_next_intersect = Segment.intersect(line_curr_new_point, next_edge)

      if (has_prev_intersect and not(has_next_intersect)):
        special_vertices_of_tangency.append(i)
      elif(not(has_prev_intersect) and has_next_intersect):
        special_vertices_of_tangency.append(i)
      
    # Remove 'dead points'      
    # all the points between the special vertices should be removed
    # first we need to find the bigger
    if (len(special_vertices_of_tangency) > 0):
      print(special_vertices_of_tangency)
      if (special_vertices_of_tangency[0] < special_vertices_of_tangency[1]):
        a = special_vertices_of_tangency[0]
        b = special_vertices_of_tangency[1]
      else:
        a = special_vertices_of_tangency[1]
        b = special_vertices_of_tangency[0]
 
      del convex_hull[a:b]
    convex_hull.append(point)
  return convex_hull


# ---- the gift wrapping algorithm ----
def gift_wrap(points_set):
  # find the the bottom-right-most point in the set
  lowest = points_set[0]
  print(points_set[1].y)
  for i in range(1, len(points_set)):
    if (lowest.y > points_set[i].y):
      lowest = points_set[i]
    elif (lowest.y == points_set[i].y) and (lowest.x < points_set[i].x):
      lowest = points_set[i]

  # the first one should be a horizontal vector
  point_to_compare = lowest
  convex_hull = [lowest];
  for i in range(0, len(points_set)):
    point_to_add = find_heigher_inner_angle(point_to_compare, points_set)
    if point_to_add not in convex_hull:
      point_to_compare = point_to_add
      convex_hull.append(point_to_add)

  return convex_hull

def find_heigher_inner_angle(point, points_set):
  bigger_angle = -2
  bigger_vertex = None
  for i in range(0, len(points_set)):
     if point != points_set[i]:
      # we do not want to considerer the vector at origin,
      # but rather it coming from point
      # PQ→=(xQ−xP,yQ−yP)
      curr_angle = Segment.inner_angle(Point(points_set[i].x - point.x, points_set[i].y - point.y, 'new vector'), point)
      if (curr_angle > bigger_angle):
        bigger_angle = curr_angle
        bigger_vertex = points_set[i]
   
  return bigger_vertex


# ref: http://www.personal.kent.edu/~rmuhamma/Compgeometry/MyCG/ConvexHull/incrementCH.htm
