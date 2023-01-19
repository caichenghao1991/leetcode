# 763. Partition Labels
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start, end, res, index = 0, 0, [], {}
        for i in range(len(s)):
            index[s[i]] = i
        for i in range(len(s)):
            end = max(end, index.get(s[i]))
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
