import sys

# good enough?
_huge = sys.float_info.max
_tiny = sys.float_info.min

_eps = 0.00001

def ray_intersect(segment_begin, segment_end, x, y):
  # We should get to points where the lowest on y should be called A, and the other B
  if (segment_begin[1] > segment_end[1]):
    a = segment_end
    b = segment_begin
  else:
    b = segment_begin
    a = segment_end

  if y == a[1] or y == b[1]:
    # CAREFUL, we are just adding one to make
    # sure that the point is not some edge
    y = y + _eps

  intersect = False

  if (y > b[1] or y < a[1]):
    return False

  if (x > max(b[1], a[1])):
    return False

  if x < min(a[0], b[0]):
    return True

  if abs(a[0] - b[0]) > _tiny:
    m_red = (b[1] - a[1]) / float(b[0] - a[0])
  else:
    m_red = _huge

  if abs(a[0] - x) > _tiny:
    m_blue = (y - a[1]) / float(x - a[0])
  else:
    m_blue = _huge

  return m_blue >= m_red

def contains_ray_casting(polygon, x, y):
  # Use ray tracing to find ou if point is inside polygon
  count = 0
  for x in range(0, len(polygon)):
    segment_begin = polygon[x]
    is_begin_last_element = x < len(polygon) - 1
    segment_end = polygon[0 if is_begin_last_element else x]
    if (ray_intersect(segment_begin, segment_end, x, y)):
      count = count + 1
  return count % 2 == 1
