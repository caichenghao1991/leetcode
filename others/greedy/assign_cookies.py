# 455. Assign Cookies
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        res = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                res += 1
                j += 1
            i += 1
        return res
