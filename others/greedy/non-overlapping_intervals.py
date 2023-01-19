# 435. Non-overlapping Intervals
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i, j, count = 0, 0, 0

        while i < len(intervals):

            if i + 1 < len(intervals) and intervals[i + 1][0] < intervals[j][1]:
                count += 1
                if intervals[j][1] > intervals[i + 1][1]:
                    j = i + 1
            else:
                j = i + 1
            i += 1
        return count