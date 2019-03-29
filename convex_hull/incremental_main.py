import sort as Sort
import polygon as Polygon
import convex as Convex

from point import Point
  
def main():
  convex_hull = []

  a = Point(1, 1, 'A')
  b = Point(9, 0, 'B')
  c = Point(2, 9, 'C')
  d = Point(10, 9, 'D')
  
  Convex.add(convex_hull, a)
  Convex.add(convex_hull, b)
  Convex.add(convex_hull, c)
  print(len(convex_hull))
  Convex.add(convex_hull, d)
  print(len(convex_hull))

  insidePoint = Point(4, 4, 'Inside')
  Convex.add(convex_hull, insidePoint)
  print("inside")
  print(len(convex_hull))

  outsidePoint = Point(16, 16, 'Outside')
  Convex.add(convex_hull, outsidePoint)
  print("outside")
  print(len(convex_hull))

  




if __name__ == '__main__':
  main()  
