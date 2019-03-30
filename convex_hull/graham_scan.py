#!/usr/bin/env python
import time
import random
import sys

from collections import namedtuple  

import matplotlib.pyplot as plt  
import sort as Sort
import segment as Segment
import point as PointUtil


Point = namedtuple('Point', 'x y')

class ConvexHull(object):  
    _points = []
    _hull_points = []
    _steps = sys.float_info.max

    def __init__(self):
        pass
    
    def update_steps_count(self, count):
      self._steps = count

    def add(self, point):
        self._points.append(point)

    def graham_sort(self): 
      Sort.points_by_x(self._points)
      self._points.reverse()

      pivot = self._points[0]

      def slope(point):
        if ((pivot.x - point.y) == 0): 
          return 0
        else:
          return (pivot.y - point.y) / \
               (pivot.x - point.y)

      return self._points[:1] + sorted(self._points[1:], key=slope)

    def compute_hull(self):
      points = self._points

      # get leftmost point and add to the hull
      ordered_points = self.graham_sort()
      i = 0

      print("TAMANHO DO ARRAY")
      print(len(ordered_points))

      for p in ordered_points:
        if (i < self._steps):
          while(len(self._hull_points) > 1 and (
             Segment.orientation(self._hull_points[-2], self._hull_points[-1], p) >= 0)):
            self._hull_points.pop()
          self._hull_points.append(p)
          self.display()
      # to close the convex polygon
      self._hull_points.append(self._hull_points[0])

          
    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def display(self):
        # all points
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='D', linestyle='None')

        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)

        plt.title('Convex Hull - Gift Wrapping')
        plt.show()


def main():
    NUMBER_OF_POINTS = 5
    ch = ConvexHull()
    ch.update_steps_count(100)
    for _ in range(NUMBER_OF_POINTS):
      ch.add(Point(random.randint(1, 100), random.randint(1, 100)))
#    ch.add(Point(1, 1))
#    ch.add(Point(4, 4))
#    ch.add(Point(1, 9))
#    ch.add(Point(3, 5))
#    ch.add(Point(16, 16))
#    ch.add(Point(15, 15))
#    ch.add(Point(10, 4))
#    ch.add(Point(10, 10))
#    ch.add(Point(16, 1))


    # start timer
    start = time.time()
    print("Points on hull:", ch.get_hull_points())

    # end timer
    end = time.time()
    print('This script runs ' + str(NUMBER_OF_POINTS) + ' points in ' + str(end - start))
    ch.display()


if __name__ == '__main__':  
    main()


# ref: https://startupnextdoor.com/computing-convex-hull-in-python/
