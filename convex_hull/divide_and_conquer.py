#!/usr/bin/env python
import time
from collections import namedtuple  
import matplotlib.pyplot as plt  
import random

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
        points = self._points

        # get leftmost point and add to the hull
        start = PointUtil.most_right(points)
        self._hull_points.append(start)

        # sort all points except the start by the
        # angle that it makes with the horizontal line
        # (polar coordenates)
        points_without_start = filter(lambda point: point != start, points)
        ordered_points = Sort.sort_points_by_angle_horizontal_line(points_without_start)
 


        a = start
        b = ordered_points[0]
        for j in range(1, len(ordered_points)):
          c = ordered_points[j]
          direction = Segment.orientation(a, b, c)
          if (direction < 0):
            self._hull_points.append(c)
            a = b
            b = c
          
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
    NUMBER_OF_POINTS = 50
    ch = ConvexHull()
    for _ in range(NUMBER_OF_POINTS):
        ch.add(Point(random.randint(1, 10), random.randint(1, 10)))

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
