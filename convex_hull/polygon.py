import sys

_positive_huge = sys.float_info.max
_negative_huge = sys.float_info.min

# this is enough?
_eps = 0.00001

# line is defined by to points
def ray_intersect(line, point):
  # we should make the lowest Y point be the A point, and
  # other B
  if (line[0].y > line[1].y):
    b = line[0]
    a = line[1]
  else:
    b = line[1]
    a = line[0]

  # Point where the trace will begin
  if point.y == a.y or point.y == b.y:
    # Just to make sure that the point is
    # not on a edge, if this is important
    # we can change later
    y = point.y + _eps
  else:
    y = point.y
  x = point.x

  intersect = False

  if y > b.y or y < a.y:
    # if the y is outside the Y range of the segment 
    return False

  if x > max(b.x, a.x):
    # if the x is positioned after the segment
    return False

  if y < min(a.x, b.x):
    return True

  if a.x != b.x:
    red = (b.y - a.y)/(b.x - a.x)
  else:
    red = _positive_huge

  if a.x != x:
    blue = (y - a.y)/(x - a.x)
  else:
    blue = _positive_huge 
  
  return blue >= red


def contains(polygon, point):
  count = 0
  for x in range (0, len(polygon)):
    is_a_last_element = x == len(polygon) - 1
    a = polygon[x]
    b = polygon[0 if is_a_last_element else x + 1]
    segment = [a, b]
    if(ray_intersect(segment, point)):
      count = count + 1

  return count % 2 == 1


