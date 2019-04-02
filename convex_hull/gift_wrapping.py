#!/usr/bin/env python
import time
from collections import namedtuple  
import matplotlib.pyplot as plt  
import random

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

        # get leftmost point
        start = PointUtil.most_left(points)
        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # find the point that is at the most 
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = Segment.orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def display(self):
        # all points
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker=',', linestyle='None')

        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)

        plt.title('Convex Hull - Gift Wrapping')
        plt.show()


def main():
    NUMBER_OF_POINTS = 50000
    ch = ConvexHull()
    for _ in range(NUMBER_OF_POINTS):
        ch.add(Point(random.randint(-1000, 1000), random.randint(-1000, 1000)))

    # start timer
    start = time.time()
    print("Points on hull:", ch.get_hull_points())

    # end timer
    end = time.time()
    print('This script runs ' + str(NUMBER_OF_POINTS) + ' points in ' + str(end - start))
    ch.display()


if __name__ == '__main__':  
    main()

