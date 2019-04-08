#!/usr/bin/env python
import time
import random
import sys
import math

from collections import namedtuple  
from math import atan2
from point import det

import matplotlib.pyplot as plt  
import sort as Sort
import segment as Segment
import point as PointUtil

Point = namedtuple('Point', 'x y')

class ConvexHull(object):  
    _points = []
    _hull_points = []

    def __init__(self):
        pass
    
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
      for s in sorted_points[1:]:
        while det(self._hull_points[-2], self._hull_points[-1], s) <= 0:
          del self._hull_points[-1]
          if len(self._hull_points) == 1: break
        self._hull_points.append(s)
#        self.display()

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

        plt.title('Convex Hull - Graham Scan')
        plt.show()


def main():
    NUMBER_OF_POINTS = 50000
    ch = ConvexHull()
    for _ in range(NUMBER_OF_POINTS):
      # radius of the circle
      circle_r = 1000
      # center of the circle (x, y)
      circle_x = 0
      circle_y = 0

      # random angle
      alpha = 2 * math.pi * random.random()
      # random radius
      r = circle_r * math.sqrt(random.random())
      # calculating coordinates
      x = r * math.cos(alpha) + circle_x
      y = r * math.sin(alpha) + circle_y
      ch.add(Point(x, y))

    # start timer
    start = time.time()
    print("Points on hull:", ch.get_hull_points())
    print("Points on hull:", len(ch.get_hull_points()))


    # end timer
    end = time.time()
    print('This script runs ' + str(NUMBER_OF_POINTS) + ' points in ' + str(end - start))
    ch.display()


if __name__ == '__main__':  
    main()
