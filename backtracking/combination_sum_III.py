# 216. Combination Sum III
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, track = [], []
        self.s = 0

        def backtrack(start, count):
            if self.s == n and count == 0:
                res.append(track[:])
                return
            elif self.s > n or count < 0:
                return
            for i in range(start, 10):
                track.append(i)
                self.s += i
                backtrack(i + 1, count - 1)
                self.s -= i
                track.pop()

        backtrack(1, k)
        return res
