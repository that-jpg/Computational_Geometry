import convex as Convex
from point import Point
  
def main():
  convex_hull = []

  a = Point(1, 1, 'A')
  b = Point(9, 0, 'B')
  c = Point(2, 9, 'C')
  d = Point(10, 9, 'D')
  
  insidePoint = Point(4, 4, 'Inside')
  outsidePoint = Point(16, 16, 'Outside')

  set_of_points = [a, b, c, d, insidePoint, outsidePoint]
 
  convex_hull = Convex.gift_wrap(set_of_points)

  print(convex_hull)

if __name__ == '__main__':
  main()  
