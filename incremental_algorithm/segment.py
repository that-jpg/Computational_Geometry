# get the tangency of given two points
def tangency(a, b):
  if (a.x - b.x == 0):
    print("Error, this will cause a division by zero")
  elif:
    return (a.y - b.y) / (a.x - b.x)
  # y-y0 = m(x-x0)  -> m = y-(y0)/(x-x0)
