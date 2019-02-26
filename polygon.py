# good enough?
HUGE_NUMBER = 999999999999

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
    y = y + 1

  intersect = False
  if (y > b[1] or y < a[1]):
    return False

  if (x > max(b[1], a[1])):
    return False

  if x < min(a[0], b[0]):
    return True

  if a[0] != b[0]:
    m_red = (b[1] - a[1]) / (b[0] - a[0])
  else:
    m_red = HUGE_NUMBER
  
  if a[0] != x:
    m_blue = (y - a[1]) / (x - a[0]) ;  
  else:
    m_blue = HUGE_NUMBER

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
  return count % 2 == 0
