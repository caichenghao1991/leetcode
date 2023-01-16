# 797. All Paths From Source to Target
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, cur_path = [], []

        def dfs(curr):
            cur_path.append(curr)
            if curr == len(graph) - 1:
                res.append(cur_path[:])
            for i in graph[curr]:
                dfs(i)
            cur_path.pop()

        dfs(0)
        return res
