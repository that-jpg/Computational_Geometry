import polygon as Polygon
import sort as Sort 
import segment as Segment

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


# ref: http://www.personal.kent.edu/~rmuhamma/Compgeometry/MyCG/ConvexHull/incrementCH.htm
