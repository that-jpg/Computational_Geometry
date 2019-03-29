import polygon as Polygon
import sort as Sort 
import segment as Segment

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
  vector_to_compare = [Point(0, 0, 'unit h-vector'), Point(0, 1, 'unit h-vector')]
  point_to_compare = lowest
  convex_hull = [];
  for i in range(0, len(points_set)):
    next_index = find_heigher_inner_angle(vector_to_compare, point_to_compare, points_set)
    if points_set[next_index] not in convex_hull:
      convex_hull.append(points_set[next_index])
      vector_to_compare = [point_to_compare, points_set[next_index]]
      point_to_compare = points_set[next_index]

  return convex_hull

def find_heigher_inner_angle(segment, point, points_set):
  bigger_angle = 0
  bigger_index = 0
  for i in range(1, len(points_set)):
    if (point != points_set[i]):
     v1 = Point(segment[0].x - segment[1].x, segment[0].y - segment[1].y, 'vetor to compare')
     v2 = Point(point.x - points_set[i].x, point.y - points_set[i].y, 'vetor2 to compare')

     curr_angle = Segment.inner_angle(v1, v2)
     if (curr_angle > bigger_angle):
       bigger_angle = curr_angle
       bigger_index = i
        
   
  return bigger_index


# ref: http://www.personal.kent.edu/~rmuhamma/Compgeometry/MyCG/ConvexHull/incrementCH.htm
