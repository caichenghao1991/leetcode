# 77. Combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, track = [], []

        def backtrack(start):
            if len(track) == k:
                res.append(track[:])
                return
            for i in range(start, n + 1 - (k - len(track) - 1)):
                track.append(i)
                backtrack(i + 1)
                track.pop()

        backtrack(1)
        return res
