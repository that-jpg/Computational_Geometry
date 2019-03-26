import sort as Sort
import polygon as Polygon
import convex as Convex

from point import Point
  
def main():
  convex_hull = []

  a = Point(0, 0, 'A')
  b = Point(9, 0, 'B')
  c = Point(1, 9, 'C')
  d = Point(10, 9, 'D')
  
  Convex.add(convex_hull, a)
  Convex.add(convex_hull, b)
  Convex.add(convex_hull, c)
  Convex.add(convex_hull, d)

  insidePoint = Point(2, 1, 'insidePoint')
  outsidePoint = Point(16, 16, 'outsidePoint')
  print(Polygon.contains(convex_hull, insidePoint))
  print(Polygon.contains(convex_hull, outsidePoint))


  Convex.add(convex_hull, insidePoint)
  Convex.add(convex_hull, outsidePoint)







if __name__ == '__main__':
  main()  
