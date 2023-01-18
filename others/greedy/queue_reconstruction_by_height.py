# 406. Queue Reconstruction by Height
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        res = []
        for h, k in people:
            res.insert(k, [h, k])
        return res
