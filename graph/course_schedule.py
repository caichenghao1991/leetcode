# 207. Course Schedule   need rework
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        current_path = [False] * numCourses
        self.cycle = False
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(curr):
            if current_path[curr]:
                self.cycle = True
                return
            if visited[curr]: return

            current_path[curr] = True
            visited[curr] = True
            for i in graph[curr]:
                dfs(i)
            current_path[curr] = False

        for i in range(numCourses):
            dfs(i)
        return not self.cycle