import polygon as Polygon
import sort as Sort 
import segment as Segment

# The first argument is guaranted to be a 
# convex hull
def add(convex_hull, point):
  if (len(convex_hull) <= 2):
    convex_hull.append(point) 
  elif not(Polygon.contains(convex_hull, point)):

    print("The point is part of the hull " + point.alias)

  return Sort.points_by_clockwise(convex_hull) 




# ref: http://www.personal.kent.edu/~rmuhamma/Compgeometry/MyCG/ConvexHull/incrementCH.htm
