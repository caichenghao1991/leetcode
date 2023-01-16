# 131. Palindrome Partitioning
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, track = [], []
        self.count = 0

        def backtrack(start):
            if start == len(s):
                res.append(track[:])
                return
            for i in range(start, len(s)):
                st = s[start:i + 1]
                if st == st[::-1]:
                    track.append(st)
                    backtrack(i + 1)
                    track.pop()

        backtrack(0)
        return res

        # res = []
        #
        # def dfs(start, path):
        #     if start == len(s):
        #         res.append(path[:])
        #     for i in range(start, len(s)):
        #         st = s[start:i + 1]
        #         if st == st[::-1]:
        #             dfs(i + 1, path + [st])
        #
        # dfs(0, [])
        # return res
