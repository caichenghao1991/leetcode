# 452. Minimum Number of Arrows to Burst Balloons
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i, count = 0, 0
        while i < len(points):
            end = points[i][1]
            while i < len(points) and points[i][0] <= end:
                end = min(end, points[i][1])
                i += 1
            count += 1
        return count
