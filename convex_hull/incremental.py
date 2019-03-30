#!/usr/bin/env python
import sys

from collections import namedtuple  
import matplotlib.pyplot as plt  
import random

import polygon as Polygon
import sort as Sort
import segment as Segment

_huge = sys.float_info.max
Point = namedtuple('Point', 'x y')

class ConvexHull(object):  
    _points = []
    _hull_points = []
    _steps = _huge

    def __init__(self):
        pass

    def update_step_count(self, count):
      self._steps = count    

    def add(self, point):
        self._points.append(point)

    def add_to_hull(self, point):
      if (len(self._hull_points) < 3):
        self._hull_points.append(point)
      elif not (Polygon.contains(self._hull_points, point)):
        special_vertices_of_tangency = []
        # looking from the edges one end intercept the convex and the other
        # do not
        for i in range(0, len(self._hull_points)):
          is_last_vertex = i == len(self._hull_points) - 1
          curr_vertex = self._hull_points[i]
          next_vertex = self._hull_points[0 if is_last_vertex else i + 1]
          prev_vertex = self._hull_points[len(self._hull_points) - 1 if i == 0 else i - 1]
      
          line_curr_new_point = [curr_vertex, point]
          previous_edge = [prev_vertex, curr_vertex]
          next_edge = [curr_vertex, next_vertex]
      
          has_prev_intersect = Segment.intersect(line_curr_new_point, previous_edge)
          has_next_intersect = Segment.intersect(line_curr_new_point, next_edge)

          print('has_prev_intersect')
          print(has_prev_intersect)
          print('has_next_intersect')
          print(has_next_intersect)

          if (has_prev_intersect and not(has_next_intersect)):
            special_vertices_of_tangency.append(i)
          elif(not(has_prev_intersect) and has_next_intersect):
            special_vertices_of_tangency.append(i)

        # Remove 'dead points'      
        # all the points between the special vertices should be removed
        # first we need to find the bigger
        if (len(special_vertices_of_tangency) > 0):
          print(special_vertices_of_tangency)
          if (special_vertices_of_tangency[0] < special_vertices_of_tangency[1]):
            a = special_vertices_of_tangency[0]
            b = special_vertices_of_tangency[1]
          else:
            a = special_vertices_of_tangency[1]
            b = special_vertices_of_tangency[0]
 
          del self._hull_points[a:b]
        self._hull_points.append(point)
        Sort.points_by_clockwise(self._hull_points)
 

    def compute_hull(self):
        points = self._points
        steps = self._steps
        i = 0
        for point in points:
          if (i < steps):
            self.add_to_hull(point)
            i = i + 1

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()


        ## add the first element again so we can close the hull
        self._hull_points.append(self._hull_points[0])
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

        plt.title('Convex Hull')
        plt.show()


def main():  
    ch = ConvexHull()
    ch.update_step_count(50)
    for _ in range(50):
        ch.add(Point(random.randint(-100, 100), random.randint(-100, 100)))

    print("Points on hull:", ch.get_hull_points())
    ch.display()


if __name__ == '__main__':  
    main()


#ref: https://startupnextdoor.com/computing-convex-hull-in-python/
