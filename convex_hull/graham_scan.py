#!/usr/bin/env python
import time
import random
import sys

from collections import namedtuple  
from math import atan2

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

    def compute_hull(self):
      pivo = None
      def polar_angle(p1, p2=None):
        if (p2 == None): p2 = pivo
        return atan2((p1.y - p2.y), (p1.x - p2.x))
   
      def distance(p1, p2=None):
        if (p2 == None): p2 = pivo
        return (p1.x - p2.x)**2 + (p1.y - p2.y)**2
      
      def graham_sort(a):
        if len(a) <= 1: return a
        smaller, equal, larger = [], [], [] 
        piv_ang = polar_angle(a[random.randint(0, len(a) - 1)])
        for pt in a:
          pt_ang = polar_angle(pt) 
          if pt_ang < piv_ang: smaller.append(pt)
          elif pt_ang == piv_ang: equal.append(pt)
          else: larger.append(pt)
        return graham_sort(smaller) + \
               sorted(equal, key=distance) + graham_sort(larger)

      # if the determinant is positive the tree points 
      # represent a counter-clockwise turn, if negative a clockwise
      # and colinear if 0 
      def det(p1, p2, p3):
        return  (p2.x - p1.x) * (p3.y - p1.y) \
               -(p2.y - p1.y) * (p3.x - p1.x)
      

      points = self._points
      min_idx=None
      for i, (x,y) in enumerate(points):
        if min_idx == None or y < points[min_idx].y:
           min_idx = i
        if y == points[min_idx].y and x < points[min_idx].x:
           min_idx = i
        
      pivo = points[min_idx]
      sorted_points = graham_sort(points)
      del sorted_points[sorted_points.index(pivo)]

      self._hull_points = []
      self._hull_points.append(pivo)
      self._hull_points.append(sorted_points[0])
      print('mermao')
      print(sorted_points[0])
      for s in sorted_points[1:]:
        while det(self._hull_points[-2], self._hull_points[-1], s) <= 0:
          del self._hull_points[-1]
          if len(self._hull_points) == 1: break
        self._hull_points.append(s)

        self.display()

      self._hull_points = self._hull_points + [self._hull_points[0]]
      
 
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
    NUMBER_OF_POINTS = 100
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
